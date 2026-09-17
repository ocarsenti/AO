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
import sys

import pandas as pd

from decp_utils import cluster_titulaire_names, load_cpv_segment, normalize_titulaire

CPV_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "33"
TOP_N = int(sys.argv[2]) if len(sys.argv) > 2 else 200
PARQUET_PATH = "data/decp_consolide.parquet"

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

# 2) regroupement des variantes proches (union-find sur inclusion de tokens)
groups = cluster_titulaire_names(distinct_names)

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
