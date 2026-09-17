#!/usr/bin/env python3
"""Sur les marchés couverts par un titulaire FABRICANT_DM (cf.
couverture_fabricants.py), classe l'acheteur (`acheteur_nom`) en :
  - CENTRALE_GROUPEMENT : plateforme d'achat mutualisée entre plusieurs
    établissements (RESAH, UniHA, UGAP, GCS/GIE achats, GHT en tant
    qu'entité acheteuse) — pas un établissement de soins identifiable en soi
  - ETABLISSEMENT_IDENTIFIE : nom qui permet de savoir précisément quel
    établissement/collectivité a acheté (CHU de Tours, Hospices Civils de
    Lyon, Commune de Nantes...), même très grand ou multi-site
  - GENERIQUE_NON_IDENTIFIABLE : libellé DECP trop pauvre pour identifier
    l'établissement réel ("CENTRE HOSPITALIER UNIVERSITAIRE" ou "CENTRE
    HOSPITALIER GENERAL" sans aucune précision de lieu)

Classification construite par relecture manuelle des 368 acheteur_nom
distincts du sous-ensemble FABRICANT_DM (pas de champ DECP fiable pour ça :
`acheteur_categorie` ne distingue pas centrale vs établissement — vérifié,
toujours NaN pour RESAH/UniHA dans ce jeu de données).

Usage: python3 scripts/couverture_acheteurs_dm.py [cpv_prefix]
"""
import sys

import pandas as pd

from decp_utils import cluster_titulaire_names, classify_acheteur, load_cpv_segment, normalize_titulaire

CPV_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "33"
PARQUET_PATH = "data/decp_consolide.parquet"
CLASSES_PATH = "reports/titulaires_top200_classes.csv"
OUT_PATH = "reports/report_couverture_acheteurs_dm.md"


# ---------------------------------------------------------------------------
classes = pd.read_csv(CLASSES_PATH)
classes_map = dict(zip(classes["titulaire_normalise"], classes["categorie"]))

seg, _total_all_cpv = load_cpv_segment(CPV_PREFIX, PARQUET_PATH)
base = seg[seg["montant_anomalie"].isna()].copy()
base["titulaire_norm"] = base["titulaire_nom"].map(normalize_titulaire)
base_named = base[base["titulaire_norm"] != ""].copy()

distinct_names = sorted(set(base_named["titulaire_norm"]) | set(classes_map))
groups = cluster_titulaire_names(distinct_names)
name_to_categorie = {}
for members in groups.values():
    cats = {classes_map[m] for m in members if m in classes_map}
    if cats:
        lbl = " / ".join(sorted(cats))
        for m in members:
            name_to_categorie[m] = lbl

base_named["categorie"] = base_named["titulaire_norm"].map(name_to_categorie)
dm = base_named[base_named["categorie"] == "FABRICANT_DM"].copy()

dm["acheteur_classe"] = dm["acheteur_nom"].map(classify_acheteur)
vc = dm["acheteur_classe"].value_counts()
pct = (vc / len(dm) * 100).round(2)

lines = []
lines.append("# Couverture FABRICANT_DM — nature de l'acheteur\n")
lines.append("Sur les **%s marchés** du segment CPV `%s` dont le titulaire est classé "
              "`FABRICANT_DM` (cf. `report_couverture_fabricants.md`), répartition de "
              "`acheteur_nom` selon qu'il désigne une centrale/groupement d'achat "
              "mutualisé ou un établissement précisément identifiable.\n\n"
              % (f"{len(dm):,}".replace(",", " "), CPV_PREFIX))
lines.append("> ⚠️ Classification construite par relecture manuelle des 368 "
              "`acheteur_nom` distincts de ce sous-ensemble (aucun champ DECP fiable "
              "pour cette distinction — `acheteur_categorie` ne distingue pas centrale "
              "vs établissement et vaut toujours NaN pour RESAH/UniHA dans ce jeu de "
              "données). Voir la liste exacte dans `scripts/couverture_acheteurs_dm.py`.\n\n")

lines.append("| Catégorie | Marchés | % du sous-ensemble FABRICANT_DM |\n|---|---|---|\n")
for cat in ["ETABLISSEMENT_IDENTIFIE", "CENTRALE_GROUPEMENT", "GENERIQUE_NON_IDENTIFIABLE"]:
    lines.append("| %s | %s | %.2f%% |\n" % (cat, f"{vc.get(cat, 0):,}".replace(",", " "), pct.get(cat, 0.0)))
lines.append("\n")

lines.append("## Détail — CENTRALE_GROUPEMENT (%s marchés, %.2f%%)\n\n"
              % (f"{vc.get('CENTRALE_GROUPEMENT', 0):,}".replace(",", " "), pct.get("CENTRALE_GROUPEMENT", 0.0)))
lines.append("| Acheteur | Marchés |\n|---|---|\n")
for name, cnt in dm.loc[dm["acheteur_classe"] == "CENTRALE_GROUPEMENT", "acheteur_nom"].value_counts().items():
    lines.append("| %s | %d |\n" % (name, cnt))
lines.append("\n")

lines.append("## Détail — GENERIQUE_NON_IDENTIFIABLE (%s marchés, %.2f%%)\n\n"
              % (f"{vc.get('GENERIQUE_NON_IDENTIFIABLE', 0):,}".replace(",", " "), pct.get("GENERIQUE_NON_IDENTIFIABLE", 0.0)))
lines.append("| Acheteur | Marchés |\n|---|---|\n")
for name, cnt in dm.loc[dm["acheteur_classe"] == "GENERIQUE_NON_IDENTIFIABLE", "acheteur_nom"].value_counts().items():
    lines.append("| %s | %d |\n" % (name, cnt))
lines.append("\n")

lines.append("## Top 20 — ETABLISSEMENT_IDENTIFIE (aperçu)\n\n")
lines.append("| Acheteur | Marchés |\n|---|---|\n")
for name, cnt in dm.loc[dm["acheteur_classe"] == "ETABLISSEMENT_IDENTIFIE", "acheteur_nom"].value_counts().head(20).items():
    lines.append("| %s | %d |\n" % (name, cnt))
lines.append("\n")

with open(OUT_PATH, "w") as f:
    f.writelines(lines)

print("Report written to", OUT_PATH)
for cat in ["ETABLISSEMENT_IDENTIFIE", "CENTRALE_GROUPEMENT", "GENERIQUE_NON_IDENTIFIABLE"]:
    print("%s: %d (%.2f%%)" % (cat, vc.get(cat, 0), pct.get(cat, 0.0)))
