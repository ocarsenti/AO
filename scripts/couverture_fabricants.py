#!/usr/bin/env python3
"""Mesure la couverture du segment CPV par les titulaires classés dans
reports/titulaires_top200_classes.csv (colonnes titulaire_normalise,
categorie parmi FABRICANT_DM / FABRICANT_DIV / LABO_PHARMA / DISTRIBUTEUR /
AUTRE).

Usage: python3 scripts/couverture_fabricants.py [cpv_prefix]

Un marché du segment "matche" une entité classée si son titulaire_nom,
normalisé et regroupé exactement comme pour produire le classement
(cf. decp_utils.cluster_titulaire_names), tombe dans le même groupe que l'un
des 200 titulaires classés.
"""
import sys

import pandas as pd

from decp_utils import cluster_titulaire_names, load_cpv_segment, normalize_titulaire

CPV_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "33"
PARQUET_PATH = "data/decp_consolide.parquet"
CLASSES_PATH = "reports/titulaires_top200_classes.csv"
OUT_PATH = "reports/report_couverture_fabricants.md"

classes = pd.read_csv(CLASSES_PATH)
classes_map = dict(zip(classes["titulaire_normalise"], classes["categorie"]))

seg, _total_all_cpv = load_cpv_segment(CPV_PREFIX, PARQUET_PATH)
n_segment_total = len(seg)  # 75 784 pour CPV 33

base = seg[seg["montant_anomalie"].isna()].copy()
n_base = len(base)  # "segment ... hors montant_anomalie=1"

base["titulaire_norm"] = base["titulaire_nom"].map(normalize_titulaire)
base_named = base[base["titulaire_norm"] != ""].copy()

# Regroupement : même algorithme que pour titulaires_top.py, appliqué à
# l'union des noms présents dans `base` ET des 200 noms classés (au cas où un
# nom classé n'apparaîtrait plus exactement identique après une nouvelle
# exécution de normalize_titulaire - garantit qu'on peut toujours faire le lien).
distinct_names = sorted(set(base_named["titulaire_norm"]) | set(classes_map))
groups = cluster_titulaire_names(distinct_names)

# pour chaque nom, la catégorie du groupe = catégorie du (ou des) membre(s)
# classé(s) du même groupe, s'il y en a un
name_to_categorie = {}
for members in groups.values():
    cats_in_group = {classes_map[m] for m in members if m in classes_map}
    if not cats_in_group:
        continue
    # cas normal : un seul nom classé par groupe. S'il y en avait plusieurs
    # avec des catégories différentes, on les liste toutes (transparence).
    cat_label = " / ".join(sorted(cats_in_group))
    for m in members:
        name_to_categorie[m] = cat_label

base_named["categorie"] = base_named["titulaire_norm"].map(name_to_categorie)
base_named["annee"] = pd.to_datetime(base_named["dateNotification"], errors="coerce").dt.year

is_dm = base_named["categorie"] == "FABRICANT_DM"
is_dm_or_div = base_named["categorie"].isin(["FABRICANT_DM", "FABRICANT_DIV"])

n_dm = int(is_dm.sum())
n_dm_or_div = int(is_dm_or_div.sum())

lines = []
lines.append("# Couverture du segment CPV `%s` par les titulaires classés\n" % CPV_PREFIX)
lines.append("Source de classification : `%s` (200 titulaires les plus fréquents, "
              "catégorisés manuellement/semi-automatiquement).\n" % CLASSES_PATH)
lines.append("- Segment CPV `%s` dédupliqué : **%s marchés**\n"
              % (CPV_PREFIX, f"{n_segment_total:,}".replace(",", " ")))
lines.append("- dont hors `montant_anomalie` (suspect/aberrant) : **%s marchés** "
              "— c'est la base utilisée ci-dessous pour les comptages\n\n"
              % f"{n_base:,}".replace(",", " "))

lines.append("## Couverture par FABRICANT_DM\n")
lines.append("- **%s marchés** matchent un titulaire classé `FABRICANT_DM` "
             "— %.2f%% du segment total (%s), %.2f%% de la base hors anomalie (%s)\n\n"
             % (f"{n_dm:,}".replace(",", " "), n_dm / n_segment_total * 100,
                f"{n_segment_total:,}".replace(",", " "), n_dm / n_base * 100,
                f"{n_base:,}".replace(",", " ")))

lines.append("## Couverture par FABRICANT_DM + FABRICANT_DIV\n")
lines.append("- **%s marchés** matchent un titulaire classé `FABRICANT_DM` ou "
             "`FABRICANT_DIV` — %.2f%% du segment total (%s), %.2f%% de la base "
             "hors anomalie (%s)\n"
             % (f"{n_dm_or_div:,}".replace(",", " "), n_dm_or_div / n_segment_total * 100,
                f"{n_segment_total:,}".replace(",", " "), n_dm_or_div / n_base * 100,
                f"{n_base:,}".replace(",", " ")))
lines.append("- Impact de l'élargissement : +%s marchés (+%.2f pt de segment total)\n\n"
             % (f"{n_dm_or_div - n_dm:,}".replace(",", " "), (n_dm_or_div - n_dm) / n_segment_total * 100))

for label, mask in [("FABRICANT_DM", is_dm), ("FABRICANT_DM + FABRICANT_DIV", is_dm_or_div)]:
    sub = base_named[mask]
    lines.append("## Détail — %s (%s marchés)\n" % (label, f"{len(sub):,}".replace(",", " ")))

    lines.append("**Top 20 acheteurs (par nombre de marchés) :**\n\n")
    lines.append("| Acheteur | Marchés | Montant total (€) |\n|---|---|---|\n")
    top_acheteurs = (
        sub.groupby("acheteur_nom", dropna=True)
        .agg(marches=("uid", "count"), montant=("montant_rationalise", "sum"))
        .sort_values("marches", ascending=False)
        .head(20)
    )
    for acheteur, row in top_acheteurs.iterrows():
        montant_s = "—" if pd.isna(row["montant"]) else f"{row['montant']:,.0f}".replace(",", " ")
        lines.append("| %s | %d | %s |\n" % (acheteur, int(row["marches"]), montant_s))
    lines.append("\n")

    lines.append("**Répartition par année (dateNotification) :**\n\n")
    lines.append("| Année | Marchés |\n|---|---|\n")
    year_counts = sub["annee"].value_counts(dropna=False).sort_index()
    for year, count in year_counts.items():
        year_label = "inconnue" if pd.isna(year) else int(year)
        lines.append("| %s | %d |\n" % (year_label, count))
    lines.append("\n")

with open(OUT_PATH, "w") as f:
    f.writelines(lines)

print("Report written to", OUT_PATH)
print("FABRICANT_DM: %d / %d (%.2f%% segment total)" % (n_dm, n_segment_total, n_dm / n_segment_total * 100))
print("FABRICANT_DM+DIV: %d / %d (%.2f%% segment total)" % (n_dm_or_div, n_segment_total, n_dm_or_div / n_segment_total * 100))
