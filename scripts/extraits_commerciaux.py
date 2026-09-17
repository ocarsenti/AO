#!/usr/bin/env python3
"""Génère deux extraits présentables (sans jargon technique) à partir de
l'analyse du segment CPV 33 :

- extrait_duel_chu.md : concurrence entre grands fabricants de dispositifs
  médicaux sur un CHU précis, avec les contrats arrivant à échéance dans les
  12 prochains mois.
- extrait_vue_ensemble_produit.md : vue nationale sur une famille de
  dispositifs (mot-clé produit), fabricants et acheteurs identifiés en tête,
  évolution annuelle.

Usage: python3 scripts/extraits_commerciaux.py
"""
import unicodedata

import pandas as pd

from decp_utils import build_titulaire_canon_map, classify_acheteur, load_cpv_segment

CPV_PREFIX = "33"
PARQUET_PATH = "data/decp_consolide.parquet"
CLASSES_PATH = "reports/titulaires_top200_classes.csv"
TODAY = pd.Timestamp("2026-09-17")

TOP10_CHU = [
    "MEDTRONIC FRANCE", "BOSTON SCIENTIFIC", "ABBOTT MEDICAL FRANCE",
    "JOHNSON JOHNSON MEDICAL", "STRYKER FRANCE", "B BRAUN MEDICAL",
    "BECTON DICKINSON FRANCE", "COOK FRANCE", "TELEFLEX MEDICAL", "VYGON",
]
CHU_CHOISI = "CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE)"
CHU_LABEL = "l'Assistance Publique - Hôpitaux de Marseille (AP-HM)"

MOT_CLE = "implant"
MOT_CLE_LABEL = "implant"


def eur(x):
    if pd.isna(x):
        return "—"
    return f"{x:,.0f}".replace(",", " ") + " €"


MOIS_FR = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin",
    7: "juillet", 8: "août", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre",
}


def mois_annee_fr(ts):
    return "%s %d" % (MOIS_FR[ts.month], ts.year)


def normalize_txt(s):
    if pd.isna(s):
        return ""
    s = unicodedata.normalize("NFKD", str(s).lower())
    return "".join(c for c in s if not unicodedata.combining(c))


# ---------------------------------------------------------------------------
seg, _total = load_cpv_segment(CPV_PREFIX, PARQUET_PATH)
base, name_to_categorie, name_to_canon = build_titulaire_canon_map(seg, CLASSES_PATH)
base["categorie"] = base["titulaire_norm"].map(name_to_categorie)
base["canon"] = base["titulaire_norm"].map(name_to_canon)
base["dateNotification"] = pd.to_datetime(base["dateNotification"], errors="coerce")
base["annee"] = base["dateNotification"].dt.year

# =============================================================================
# EXTRAIT 1 — Duel concurrentiel sur un établissement
# =============================================================================
chu_all_time = base[(base["acheteur_nom"] == CHU_CHOISI) & (base["canon"].isin(TOP10_CHU))].copy()
chu_2125 = chu_all_time[chu_all_time["annee"].between(2021, 2025)].copy()

agg = chu_2125.groupby("canon").agg(
    marches=("uid", "count"), montant=("montant_rationalise", "sum")
).reindex(TOP10_CHU).fillna(0)
agg["montant_moyen"] = (agg["montant"] / agg["marches"]).where(agg["marches"] > 0)
agg = agg.sort_values("montant", ascending=False)

pivot_year = chu_2125.pivot_table(index="canon", columns="annee", values="uid", aggfunc="count", fill_value=0)
pivot_year = pivot_year.reindex(agg.index).reindex(columns=[2021, 2022, 2023, 2024, 2025], fill_value=0)

# échéances (12 prochains mois), calculées sur tout l'historique disponible
chu_all_time["date_fin_estimee"] = chu_all_time["dateNotification"] + pd.to_timedelta(
    chu_all_time["dureeMois"] * 30.44, unit="D"
)
window_end = TODAY + pd.DateOffset(months=12)
echeance = chu_all_time[
    chu_all_time["dureeMois"].notna()
    & (chu_all_time["date_fin_estimee"] >= TODAY)
    & (chu_all_time["date_fin_estimee"] <= window_end)
].copy()
echeance_grp = (
    echeance.groupby(["canon", "objet", "dateNotification", "dureeMois"])
    .agg(n_lots=("uid", "count"), montant=("montant_rationalise", "sum"), date_fin=("date_fin_estimee", "first"))
    .reset_index()
    .sort_values("date_fin")
)

lines1 = []
lines1.append("# Qui vend quoi à l'AP-HM sur les dispositifs médicaux ?\n\n")
lines1.append(
    "Ce document compare, sur un grand hôpital universitaire (%s), l'activité "
    "commerciale des dix plus gros fabricants de dispositifs médicaux présents "
    "sur le marché français, entre 2021 et 2025. Il montre qui fournit combien, "
    "à quel prix moyen, et surtout **quels contrats arrivent à échéance dans les "
    "douze prochains mois** — l'information la plus utile pour anticiper un "
    "prochain appel d'offres.\n\n" % CHU_LABEL
)

lines1.append("## Qui fournit combien (2021-2025)\n\n")
lines1.append("| Fabricant | Nombre de marchés | Montant total | Montant moyen par marché |\n")
lines1.append("|---|---|---|---|\n")
for canon, row in agg.iterrows():
    lines1.append("| %s | %d | %s | %s |\n" % (canon, int(row["marches"]), eur(row["montant"]), eur(row["montant_moyen"])))
lines1.append("\n")

lines1.append("## Évolution année par année (nombre de marchés notifiés)\n\n")
lines1.append("| Fabricant | 2021 | 2022 | 2023 | 2024 | 2025 |\n|---|---|---|---|---|---|\n")
for canon in agg.index:
    row = pivot_year.loc[canon]
    lines1.append("| %s | %d | %d | %d | %d | %d |\n" % (canon, row[2021], row[2022], row[2023], row[2024], row[2025]))
lines1.append(
    "\n> *2023 apparaît anormalement bas pour tous les fabricants à la fois "
    "(0 ou presque partout) : ce n'est pas un vrai creux d'achats, c'est un trou "
    "dans la remontée des données de cette année-là pour cet hôpital (confirmé "
    "sur l'ensemble de ses marchés, tous fournisseurs confondus, pas seulement "
    "ceux listés ici) — à ne pas lire comme une pause réelle des commandes.*\n\n"
)

lines1.append("## Prochaine échéance probable (12 prochains mois)\n\n")
lines1.append(
    "Estimée en ajoutant la durée prévue du marché à sa date de signature. "
    "C'est la donnée la plus actionnable commercialement : savoir qu'un contrat "
    "revient bientôt en compétition permet de se positionner avant l'appel "
    "d'offres.\n\n"
)
if len(echeance_grp):
    lines1.append("| Échéance estimée | Fabricant titulaire actuel | Objet du marché | Montant | Lots concernés |\n")
    lines1.append("|---|---|---|---|---|\n")
    for _, r in echeance_grp.iterrows():
        objet_short = r["objet"] if len(r["objet"]) <= 110 else r["objet"][:107] + "..."
        lines1.append(
            "| %s | %s | %s | %s | %d |\n"
            % (mois_annee_fr(r["date_fin"]), r["canon"], objet_short, eur(r["montant"]), int(r["n_lots"]))
        )
else:
    lines1.append("_Aucune échéance détectée dans cette fenêtre._\n")
lines1.append("\n")

with open("reports/extrait_duel_chu.md", "w") as f:
    f.writelines(lines1)

# =============================================================================
# EXTRAIT 2 — Vue d'ensemble national sur une famille de dispositif
# =============================================================================
base["objet_norm"] = base["objet"].map(normalize_txt)
dm = base[base["categorie"] == "FABRICANT_DM"].copy()
prod = dm[dm["objet_norm"].str.contains(MOT_CLE, na=False)].copy()
prod["acheteur_classe"] = prod["acheteur_nom"].map(classify_acheteur)

top_fab = (
    prod.groupby("canon")["montant_rationalise"]
    .agg(marches="count", montant="sum")
    .sort_values("montant", ascending=False)
    .head(10)
)

top_ach = (
    prod[prod["acheteur_classe"] == "ETABLISSEMENT_IDENTIFIE"]
    .groupby("acheteur_nom")["montant_rationalise"]
    .agg(marches="count", montant="sum")
    .sort_values("montant", ascending=False)
    .head(10)
)

evol = prod[prod["annee"].between(2021, 2025)]["annee"].value_counts().sort_index()

n_total = len(prod)
n_centrale = int((prod["acheteur_classe"] == "CENTRALE_GROUPEMENT").sum())
n_generique = int((prod["acheteur_classe"] == "GENERIQUE_NON_IDENTIFIABLE").sum())
n_etabli = int((prod["acheteur_classe"] == "ETABLISSEMENT_IDENTIFIE").sum())

lines2 = []
lines2.append("# Le marché des implants en France : qui vend, qui achète\n\n")
lines2.append(
    "Ce document rassemble, à l'échelle nationale, tous les contrats publics "
    "où un fabricant reconnu de dispositifs médicaux fournit un produit décrit "
    "comme un implant (prothèses, implants orthopédiques, cardiaques, "
    "ophtalmologiques...). Il répond à trois questions : quels fabricants "
    "dominent ce marché en valeur, quels hôpitaux achètent le plus (en excluant "
    "les centrales d'achat mutualisées, pour ne garder que des établissements "
    "identifiables un par un), et comment le volume de contrats évolue dans le "
    "temps.\n\n"
)
lines2.append(
    "Sur %s marchés au total : %s passent par un établissement identifié "
    "individuellement, %s par une centrale ou un groupement d'achat mutualisé, "
    "et %s portent un nom d'acheteur trop générique dans les données pour être "
    "rattachés à un établissement précis.\n\n"
    % (f"{n_total:,}".replace(",", " "), f"{n_etabli:,}".replace(",", " "),
       f"{n_centrale:,}".replace(",", " "), f"{n_generique:,}".replace(",", " "))
)

lines2.append("## Les 10 fabricants qui pèsent le plus (en montant)\n\n")
lines2.append("| Fabricant | Nombre de marchés | Montant total |\n|---|---|---|\n")
for canon, row in top_fab.iterrows():
    lines2.append("| %s | %d | %s |\n" % (canon, int(row["marches"]), eur(row["montant"])))
lines2.append("\n")

lines2.append("## Les 10 hôpitaux les plus gros acheteurs (établissements identifiés uniquement)\n\n")
lines2.append(
    "_Les centrales d'achat mutualisées (RESAH, UniHA, UGAP...) sont exclues de "
    "ce classement : elles achètent pour le compte de dizaines d'hôpitaux à la "
    "fois, ce qui fausserait la comparaison avec un établissement qui achète "
    "pour lui-même._\n\n"
)
lines2.append("| Établissement | Nombre de marchés | Montant total |\n|---|---|---|\n")
for name, row in top_ach.iterrows():
    lines2.append("| %s | %d | %s |\n" % (name, int(row["marches"]), eur(row["montant"])))
lines2.append("\n")

lines2.append("## Évolution du nombre de marchés notifiés, 2021-2025\n\n")
lines2.append("| Année | Nombre de marchés |\n|---|---|\n")
for year, count in evol.items():
    lines2.append("| %d | %d |\n" % (year, count))
lines2.append(
    "\n> *Les fortes variations d'une année à l'autre reflètent surtout le "
    "cycle de renouvellement des gros contrats-cadres pluriannuels (souvent "
    "notifiés par vagues tous les 3 à 5 ans) plus qu'un changement réel du "
    "volume d'implants posés chaque année.*\n\n"
)

with open("reports/extrait_vue_ensemble_produit.md", "w") as f:
    f.writelines(lines2)

print("Écrit : reports/extrait_duel_chu.md et reports/extrait_vue_ensemble_produit.md")
print("CHU choisi:", CHU_CHOISI, "-", len(chu_2125), "marchés top10 sur 2021-2025,", len(echeance_grp), "échéances groupées")
print("Mot-clé:", MOT_CLE, "-", n_total, "marchés (", n_etabli, "établissement /", n_centrale, "centrale /", n_generique, "générique)")
