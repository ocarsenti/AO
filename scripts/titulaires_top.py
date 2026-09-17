#!/usr/bin/env python3
"""Agrégation par titulaire (fabricant/fournisseur) sur un segment CPV DECP.

Usage: python3 scripts/titulaires_top.py [cpv_prefix] [top_n]

Normalise `titulaire_nom` (majuscules, accents supprimés, suffixes juridiques
retirés, espaces réduits), regroupe les variantes proches du même nom
(ex. "MEDTRONIC" / "MEDTRONIC FRANCE" / "MEDTRONIC FRANCE SAS" -> un seul
groupe), exclut les lignes sans montant fiable (`montant_anomalie`
renseigné = "suspect"/"aberrant") et sans titulaire, puis exporte le top N
par nombre de marchés dans reports/titulaires_top<N>.csv.
"""
import re
import sys
import unicodedata

import pandas as pd

from decp_utils import load_cpv_segment

CPV_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "33"
TOP_N = int(sys.argv[2]) if len(sys.argv) > 2 else 200
PARQUET_PATH = "data/decp_consolide.parquet"

LEGAL_SUFFIXES = {"SA", "SAS", "SARL", "GMBH", "LTD", "INC"}

# tokens trop génériques pour, seuls, justifier un regroupement par inclusion
STOPWORDS = {
    "FRANCE", "GROUPE", "GROUP", "SOCIETE", "INTERNATIONAL", "EUROPE",
    "MEDICAL", "MEDICALE", "SANTE", "LABORATOIRE", "LABORATOIRES", "HOLDING",
    "DISTRIBUTION", "SERVICES", "SERVICE", "COMPAGNIE", "CIE", "PARIS",
}


def normalize_titulaire(raw):
    s = unicodedata.normalize("NFKD", str(raw)).upper()
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[.,;:'&/]", " ", s)
    tokens = [t for t in s.split() if t not in LEGAL_SUFFIXES]
    s = " ".join(tokens)
    s = re.sub(r"\s+", " ", s).strip()
    return s


class UnionFind:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


def can_merge(tokens_a, tokens_b):
    """True si tokens_a est un sous-ensemble "significatif" de tokens_b (ou l'inverse).

    "Significatif" exige qu'au moins un des tokens partagés ne soit pas un mot
    générique (STOPWORDS) : sans ça, deux tokens communs comme {MEDICAL, FRANCE}
    suffisaient à fusionner par transitivité des entités sans rapport (Abbott,
    Merit Medical, Fresenius Medical Care, Canon Medical... toutes "X MEDICAL
    FRANCE") — bug détecté et corrigé le 2026-09-17.
    """
    if tokens_a == tokens_b:
        return True
    small, big = (tokens_a, tokens_b) if len(tokens_a) <= len(tokens_b) else (tokens_b, tokens_a)
    if not small or not small.issubset(big):
        return False
    non_stop = small - STOPWORDS
    if not non_stop:
        return False
    if len(small) == 1:
        (tok,) = tuple(non_stop)
        return len(tok) >= 4
    return True


# ---------------------------------------------------------------------------
seg, _total_all_cpv = load_cpv_segment(CPV_PREFIX, PARQUET_PATH)
n_segment = len(seg)

n_no_titulaire = int(seg["titulaire_nom"].isna().sum())
n_anomalie = int(seg["montant_anomalie"].notna().sum())

clean = seg[seg["titulaire_nom"].notna() & seg["montant_anomalie"].isna()].copy()
n_clean = len(clean)

clean["titulaire_norm"] = clean["titulaire_nom"].map(normalize_titulaire)
clean = clean[clean["titulaire_norm"] != ""]

# 1) agrégation exacte par nom normalisé
per_name = clean.groupby("titulaire_norm").agg(
    marches=("uid", "count"),
    montant=("montant_rationalise", "sum"),
)
distinct_names = list(per_name.index)
token_sets = {name: frozenset(name.split()) for name in distinct_names}

# 2) regroupement des variantes proches (union-find sur inclusion de tokens)
uf = UnionFind(distinct_names)
# trie par longueur pour limiter les comparaisons quadratiques dans la pratique
names_sorted = sorted(distinct_names, key=lambda n: len(token_sets[n]))
for i, a in enumerate(names_sorted):
    ta = token_sets[a]
    for b in names_sorted[i + 1:]:
        tb = token_sets[b]
        if len(tb) - len(ta) > 3:
            # noms trop différents en taille de token : peu probable que ce soit
            # la même entité, et ça borne le coût du double-boucle
            continue
        if can_merge(ta, tb):
            uf.union(a, b)

groups = {}
for name in distinct_names:
    root = uf.find(name)
    groups.setdefault(root, []).append(name)

rows = []
for root, members in groups.items():
    sub = per_name.loc[members]
    total_marches = int(sub["marches"].sum())
    total_montant = sub["montant"].sum()
    canonical = sub["marches"].idxmax()  # variante la plus fréquente sert de libellé
    rows.append({
        "titulaire_normalise": canonical,
        "variantes_regroupees": len(members),
        "nombre_marches": total_marches,
        "montant_total": round(float(total_montant), 2) if pd.notna(total_montant) else 0.0,
    })

result = pd.DataFrame(rows).sort_values("nombre_marches", ascending=False).reset_index(drop=True)
result["part_cumulee_pct"] = (result["nombre_marches"].cumsum() / n_clean * 100).round(2)

top = result.head(TOP_N).drop(columns=["variantes_regroupees"])
out_path = "reports/titulaires_top%d.csv" % TOP_N
top.to_csv(out_path, index=False)

print("Segment CPV %s dédupliqué : %d marchés" % (CPV_PREFIX, n_segment))
print("Exclus - sans titulaire_nom : %d" % n_no_titulaire)
print("Exclus - montant_anomalie renseigné (suspect/aberrant) : %d" % n_anomalie)
print("Base d'agrégation (marchés avec titulaire + montant fiable) : %d" % n_clean)
print("Titulaires distincts (avant regroupement) : %d" % len(distinct_names))
print("Groupes après regroupement des variantes proches : %d" % len(groups))
print("Top %d exporté dans %s (part cumulée du top %d : %.2f%%)"
      % (TOP_N, out_path, TOP_N, top["part_cumulee_pct"].iloc[-1]))
