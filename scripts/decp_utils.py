"""Utilitaires partagés pour charger et dédupliquer le fichier DECP consolidé.

Le fichier consolidé de data.gouv.fr contient, pour un même marché (`uid`
constant), une ligne par version successive de sa déclaration
(`modification_id` croissant). Au 2026-09-17, ~43.75% des lignes du fichier
complet sont des versions historiques d'un marché déjà présent sous une
autre version — pas des marchés distincts. Le flag `donneesActuelles` est
censé marquer la version courante mais n'est pas fiable à 100% (~140k uid
ont plusieurs lignes à True, ~12k n'en ont aucune) : on déduplique donc en
gardant, pour chaque `uid`, la ligne au `modification_id` maximum.
"""
import re
import unicodedata

import pandas as pd

PARQUET_PATH = "data/decp_consolide.parquet"


def load_cpv_segment(cpv_prefix, parquet_path=PARQUET_PATH):
    """Charge le parquet, filtre par préfixe CPV, déduplique par uid (dernière
    version). Retourne (segment_dedupliqué, total_marchés_distincts_tous_cpv)."""
    df = pd.read_parquet(parquet_path)
    total_distinct = df["uid"].nunique()

    df["codeCPV"] = df["codeCPV"].astype("string")
    seg = df[df["codeCPV"].str.startswith(cpv_prefix, na=False)].copy()

    seg["_mod"] = seg["modification_id"].fillna(-1)
    seg = seg.sort_values(["uid", "_mod"]).drop_duplicates(subset="uid", keep="last")
    seg = seg.drop(columns=["_mod"])

    return seg, total_distinct


# ---------------------------------------------------------------------------
# Normalisation et regroupement des titulaires (utilisé par titulaires_top.py
# et couverture_fabricants.py — garder ici pour que les deux analyses
# utilisent strictement la même normalisation / le même regroupement)
# ---------------------------------------------------------------------------

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


def build_titulaire_canon_map(seg, classes_csv_path):
    """A partir d'un segment (avec titulaire_nom, montant_anomalie) et du
    fichier de classification titulaires_top200_classes.csv, retourne
    (base, name_to_categorie, name_to_canon) où `base` est le segment sans
    les lignes montant_anomalie renseignées ni titulaire_nom manquant, et les
    deux dicts associent chaque titulaire_norm rencontré à la catégorie /
    au nom canonique du groupe (parmi les 200 titulaires classés), quand il
    matche un groupe classé."""
    import pandas as pd

    classes = pd.read_csv(classes_csv_path)
    classes_map = dict(zip(classes["titulaire_normalise"], classes["categorie"]))

    base = seg[seg["montant_anomalie"].isna()].copy()
    base["titulaire_norm"] = base["titulaire_nom"].map(normalize_titulaire)
    base = base[base["titulaire_norm"] != ""].copy()

    distinct_names = sorted(set(base["titulaire_norm"]) | set(classes_map))
    groups = cluster_titulaire_names(distinct_names)

    name_to_categorie = {}
    name_to_canon = {}
    for members in groups.values():
        classified_members = [m for m in members if m in classes_map]
        if not classified_members:
            continue
        cats = {classes_map[m] for m in classified_members}
        canon = classified_members[0]
        lbl = " / ".join(sorted(cats))
        for m in members:
            name_to_categorie[m] = lbl
            name_to_canon[m] = canon

    return base, name_to_categorie, name_to_canon


# ---------------------------------------------------------------------------
# Classification de l'acheteur : centrale/groupement d'achat mutualisé vs
# établissement précisément identifiable vs libellé DECP trop générique.
# Construite par relecture manuelle des acheteur_nom du segment CPV 33 x
# FABRICANT_DM (cf. couverture_acheteurs_dm.py) — pas de champ DECP fiable
# pour cette distinction (acheteur_categorie ne la fait pas : NaN pour
# RESAH/UniHA dans ce jeu de données).
# ---------------------------------------------------------------------------

CENTRALE_GROUPEMENT = {
    "RESEAU DES ACHETEURS HOSPITALIERS",
    "GCS GROUPEMENT REGIONAL D'ACHATS DE PRODUITS DE SANTE GRAND EST",
    "GROUPEMENT COOPERATION SANITAIRE - UNION DES HOPITAUX POUR LES ACHATS",
    "GROUPEMENT DE COOPERATION SANITAIRE HACOM",
    "GROUPEMENT HOSPITALIER DE TERRITOIRE GRAND PARIS NORD-EST",
    "UNION DES GROUPEMENTS D'ACHATS PUBLICS (UGAP)",
    "GROUPEMENT DE COOPERATION SANITAIRE ACHATS DU CENTRE",
    "GROUPEMENT HOSPITALIER DE TERRITOIRE GRAND PARIS NORD-EST "
    "(GROUPEMENT HOSPITALIER DE TERRITOIRE 93 EST)",
    "GCS ACHATS EN NOUVELLE-AQUITAINE",
    "GIE CONSORTIUM D'ACHATS DES CLCC",
}

GENERIQUE_NON_IDENTIFIABLE = {
    "CENTRE HOSPITALIER UNIVERSITAIRE",
    "CENTRE HOSPITALIER GENERAL",
    "MAISON DE RETRAITE",
}


def classify_acheteur(name):
    if name in CENTRALE_GROUPEMENT:
        return "CENTRALE_GROUPEMENT"
    if name in GENERIQUE_NON_IDENTIFIABLE:
        return "GENERIQUE_NON_IDENTIFIABLE"
    return "ETABLISSEMENT_IDENTIFIE"


def cluster_titulaire_names(distinct_names):
    """Regroupe une liste de noms déjà normalisés (normalize_titulaire) par
    variantes proches (union-find sur inclusion "significative" de tokens).
    Retourne un dict {nom: nom_canonique_du_groupe} où nom_canonique est,
    pour l'instant, arbitrairement le premier membre trouvé (le choix du
    libellé le plus fréquent se fait chez l'appelant, qui a les comptes)."""
    token_sets = {name: frozenset(name.split()) for name in distinct_names}
    uf = UnionFind(distinct_names)
    names_sorted = sorted(distinct_names, key=lambda n: len(token_sets[n]))
    for i, a in enumerate(names_sorted):
        ta = token_sets[a]
        for b in names_sorted[i + 1:]:
            tb = token_sets[b]
            if len(tb) - len(ta) > 3:
                continue
            if can_merge(ta, tb):
                uf.union(a, b)

    groups = {}
    for name in distinct_names:
        root = uf.find(name)
        groups.setdefault(root, []).append(name)
    return groups
