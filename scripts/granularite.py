#!/usr/bin/env python3
"""Analyse de granularité sur un segment CPV déjà extrait du fichier DECP consolidé.

Usage: python3 scripts/granularite.py [cpv_prefix]

Produit reports/report_cpv_<prefix>_granularite.md avec 4 sections :
  1. Recherche par mots-clés produit dans `objet`
  2. Mesure de la "généricité" de l'objet (lots sans descripteur, renvois au
     CCTP, objets très courts)
  3. Filtrage par titulaire (fabricants connus) : volumes, montants, top
     acheteurs, répartition annuelle
  4. Croisement mot-clé produit x titulaire connu
"""
import re
import sys
import unicodedata

import pandas as pd

from decp_utils import load_cpv_segment

CPV_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "33"
PARQUET_PATH = "data/decp_consolide.parquet"
SAMPLE_SEED = 42


def normalize(s):
    """lowercase + strip accents, for accent-insensitive substring matching."""
    if s is None or (isinstance(s, float) and pd.isna(s)):
        return ""
    s = unicodedata.normalize("NFKD", str(s).lower())
    return "".join(c for c in s if not unicodedata.combining(c))


# ---------------------------------------------------------------------------
# Load & filter segment (recomputed from source parquet, independent of the
# earlier report_cpv_33.md so this script can be re-run for any CPV prefix)
# ---------------------------------------------------------------------------
seg, _total_all_cpv = load_cpv_segment(CPV_PREFIX, PARQUET_PATH)
n_total = len(seg)

seg["objet_norm"] = seg["objet"].map(normalize)
seg["titulaire_norm"] = seg["titulaire_nom"].map(normalize)
seg["annee"] = pd.to_datetime(seg["dateNotification"], errors="coerce").dt.year

lines = []
lines.append("# Rapport de granularité — segment CPV `%s`\n" % CPV_PREFIX)
lines.append("Analyse approfondie du champ `objet` (texte libre) sur l'ensemble "
              "des **%s** marchés du segment (pas un échantillon).\n" % f"{n_total:,}".replace(",", " "))
lines.append("> ℹ️ Dédupliqué par `uid` (dernière version par `modification_id`) — "
              "voir `scripts/decp_utils.py` et la note en tête de `report_cpv_%s.md`.\n\n"
              % CPV_PREFIX)

# ===========================================================================
# 1) Recherche par mots-clés produit
# ===========================================================================
lines.append("## 1. Recherche par mots-clés dans `objet`\n")
lines.append("Recherche en sous-chaîne, insensible à la casse et aux accents "
              "(ex. `stent` matche aussi `stents`, `implant` matche aussi "
              "`implantable`/`implantation`).\n")

keywords = [
    ("stent", ["stent"]),
    ("prothese / prothèse", ["prothes"]),
    ("catheter / cathéter", ["catheter"]),
    ("implant", ["implant"]),
    ("defibrillateur / défibrillateur", ["defibrillateur"]),
    ("pacemaker / stimulateur cardiaque", ["pacemaker", "stimulateur cardiaque"]),
]

lines.append("| Mot-clé | Lignes | % du segment |\n|---|---|---|\n")
keyword_masks = {}
for label, substrings in keywords:
    mask = pd.Series(False, index=seg.index)
    for sub in substrings:
        mask = mask | seg["objet_norm"].str.contains(sub, regex=False, na=False)
    keyword_masks[label] = mask
    cnt = int(mask.sum())
    lines.append("| %s | %s | %.2f%% |\n" % (label, f"{cnt:,}".replace(",", " "), cnt / n_total * 100))
lines.append("\n")

for label, substrings in keywords:
    mask = keyword_masks[label]
    cnt = int(mask.sum())
    lines.append("### %s (%s lignes)\n" % (label, f"{cnt:,}".replace(",", " ")))
    if cnt == 0:
        lines.append("_Aucune ligne trouvée._\n\n")
        continue
    sample_n = min(5, cnt)
    sample = seg.loc[mask, "objet"].dropna().sample(
        n=min(sample_n, mask.sum()), random_state=SAMPLE_SEED
    ) if seg.loc[mask, "objet"].notna().any() else pd.Series(dtype="object")
    for i, obj in enumerate(sample, 1):
        obj_clean = str(obj).replace("\n", " ").replace("|", "/").strip()
        lines.append("%d. %s\n" % (i, obj_clean))
    lines.append("\n")

# ===========================================================================
# 2) Mesure de la "généricité" de l'objet
# ===========================================================================
lines.append("## 2. Généricité de l'objet\n")
lines.append("> ⚠️ Mesures heuristiques (regex + liste de mots), pas une "
              "vérité absolue — utiles pour estimer un ordre de grandeur, "
              "pas pour un décompte exact.\n\n")

# 2a) lot number pattern without any product-descriptive word nearby
lot_pattern = re.compile(r"\blots?\b.{0,20}?\d")
descriptor_words = [
    "dispositif", "dispositifs", "medicament", "medicaments", "materiel", "materiels",
    "consommable", "consommables", "reactif", "reactifs", "prothes", "catheter",
    "implant", "stent", "pansement", "pansements", "vaccin", "vaccins", "produit",
    "produits", "chirurgical", "chirurgicaux", "chirurgicale", "medical", "medicale",
    "medicaux", "medicales", "appareil", "appareils", "equipement", "equipements",
    "seringue", "seringues", "gant", "gants", "masque", "masques", "aiguille",
    "aiguilles", "sonde", "sondes", "tubulure", "tubulures", "compresse", "compresses",
    "perfusion", "oxygene", "laboratoire", "biologie", "analyse", "analyses",
    "pharmaceutique", "pharmaceutiques", "specialite", "specialites", "defibrillateur",
    "pacemaker", "stimulateur", "orthese", "ortheses", "ancillaire", "ancillaires",
    "instrumentation", "ligature", "suture", "sutures", "drainage", "endoscopie",
    "radiologie", "imagerie", "biopsie", "filtration", "filtre", "filtres",
]

def has_lot_no_descriptor(text_norm):
    if not lot_pattern.search(text_norm):
        return False
    return not any(w in text_norm for w in descriptor_words)

seg["lot_sans_descripteur"] = seg["objet_norm"].map(has_lot_no_descriptor)
n_lot = int(seg["lot_sans_descripteur"].sum())

# 2b) "voir cahier des charges / CCTP / bordereau" or equivalent
cctp_pattern = re.compile(
    r"(voir|cf\.?|detail(?:e|ee)?\s+dans)\s+.{0,20}"
    r"(cahier des charges|cctp|bordereau|dce|dpgf)"
)
seg["renvoi_cctp"] = seg["objet_norm"].map(lambda t: bool(cctp_pattern.search(t)))
n_cctp = int(seg["renvoi_cctp"].sum())

# 2c) objet < 5 words
seg["n_mots_objet"] = seg["objet"].fillna("").map(lambda s: len(str(s).split()))
seg["objet_court"] = (seg["n_mots_objet"] > 0) & (seg["n_mots_objet"] < 5)
n_court = int(seg["objet_court"].sum())

lines.append("| Critère | Lignes | % du segment |\n|---|---|---|\n")
lines.append("| Référence à un n° de lot sans descripteur produit à proximité | %s | %.2f%% |\n"
             % (f"{n_lot:,}".replace(",", " "), n_lot / n_total * 100))
lines.append("| Renvoi \"voir cahier des charges / CCTP / bordereau\" (ou équivalent) | %s | %.2f%% |\n"
             % (f"{n_cctp:,}".replace(",", " "), n_cctp / n_total * 100))
lines.append("| Objet de moins de 5 mots | %s | %.2f%% |\n"
             % (f"{n_court:,}".replace(",", " "), n_court / n_total * 100))
lines.append("\n")

for label, mask_col in [
    ("Lot sans descripteur produit", "lot_sans_descripteur"),
    ("Renvoi cahier des charges / CCTP / bordereau", "renvoi_cctp"),
    ("Objet de moins de 5 mots", "objet_court"),
]:
    mask = seg[mask_col]
    cnt = int(mask.sum())
    lines.append("### Exemples — %s (%s lignes)\n" % (label, f"{cnt:,}".replace(",", " ")))
    if cnt == 0:
        lines.append("_Aucune ligne trouvée._\n\n")
        continue
    sample = seg.loc[mask, "objet"].dropna().sample(
        n=min(5, mask.sum()), random_state=SAMPLE_SEED
    )
    for i, obj in enumerate(sample, 1):
        obj_clean = str(obj).replace("\n", " ").replace("|", "/").strip()
        lines.append("%d. %s\n" % (i, obj_clean))
    lines.append("\n")

# ===========================================================================
# 3) Filtrage par titulaire connu
# ===========================================================================
lines.append("## 3. Filtrage par titulaire connu (fabricants)\n")

# `montant_rationalise` ne corrige PAS les lignes que data.gouv.fr flague lui-même
# comme "suspect"/"aberrant" dans `montant_anomalie` (ex. montant d'accord-cadre
# entier recopié sur un seul lot) : sur ce segment, 1.55% des lignes portent un tel
# flag mais pèsent 37% de la somme totale des montants. On les exclut des
# totaux/moyennes et on affiche leur nombre pour transparence.
seg["montant_fiable"] = seg["montant_rationalise"].where(seg["montant_anomalie"].isna())
n_anomalie_total = int(seg["montant_anomalie"].notna().sum())

lines.append("> Montants calculés sur `montant_rationalise`, **en excluant les lignes "
              "flaguées `montant_anomalie` (\"suspect\"/\"aberrant\") par data.gouv.fr** "
              "— sur l'ensemble du segment, %s lignes (%.2f%%) portent un tel flag mais "
              "pèsent à elles seules %.0f%% de la somme brute des montants (ex. montant "
              "total d'un accord-cadre recopié sur un seul lot). Lignes sans montant "
              "fiable également exclues des moyennes/totaux ; le nombre de marchés reste "
              "inchangé (compte sur tous les marchés, montant fiable ou non).\n\n"
              % (f"{n_anomalie_total:,}".replace(",", " "), n_anomalie_total / n_total * 100,
                 seg.loc[seg["montant_anomalie"].notna(), "montant_rationalise"].dropna().sum()
                 / seg["montant_rationalise"].dropna().sum() * 100))

manufacturers = [
    ("Medtronic", ["medtronic"]),
    ("Abbott", ["abbott"]),
    ("Boston Scientific", ["boston scientific"]),
    ("Biotronik", ["biotronik"]),
    ("Stryker", ["stryker"]),
    ("Zimmer Biomet", ["zimmer biomet", "zimmer", "biomet"]),
    ("Johnson & Johnson / DePuy Synthes", ["johnson", "depuy", "synthes"]),
    ("Getinge", ["getinge"]),
]

manuf_masks = {}
summary_rows = []
for name, aliases in manufacturers:
    mask = pd.Series(False, index=seg.index)
    for alias in aliases:
        mask = mask | seg["titulaire_norm"].str.contains(alias, regex=False, na=False)
    manuf_masks[name] = mask
    cnt = int(mask.sum())
    n_excl = int(seg.loc[mask, "montant_anomalie"].notna().sum())
    montants = seg.loc[mask, "montant_fiable"].dropna()
    summary_rows.append((name, cnt, n_excl, montants.sum(), montants.mean() if len(montants) else float("nan")))

lines.append("| Fabricant | Marchés | dont montant exclu (anomalie) | Montant total (€) | Montant moyen (€) |\n|---|---|---|---|---|\n")
for name, cnt, n_excl, total, mean in summary_rows:
    total_s = f"{total:,.0f}".replace(",", " ") if cnt else "—"
    mean_s = f"{mean:,.0f}".replace(",", " ") if cnt and not pd.isna(mean) else "—"
    lines.append("| %s | %s | %s | %s | %s |\n" % (
        name, f"{cnt:,}".replace(",", " "), n_excl, total_s, mean_s
    ))
lines.append("\n")

for name, aliases in manufacturers:
    mask = manuf_masks[name]
    cnt = int(mask.sum())
    lines.append("### %s (%s marchés)\n" % (name, f"{cnt:,}".replace(",", " ")))
    if cnt == 0:
        lines.append("_Aucun marché trouvé pour ce fabricant sur ce segment._\n\n")
        continue
    sub = seg.loc[mask]

    lines.append("**Top 10 acheteurs (par nombre de marchés) :**\n\n")
    lines.append("| Acheteur | Marchés | Montant total fiable (€) |\n|---|---|---|\n")
    top_acheteurs = (
        sub.groupby("acheteur_nom", dropna=True)
        .agg(marches=("uid", "count"), montant=("montant_fiable", "sum"))
        .sort_values("marches", ascending=False)
        .head(10)
    )
    for acheteur, row in top_acheteurs.iterrows():
        lines.append("| %s | %d | %s |\n" % (
            acheteur, int(row["marches"]), f"{row['montant']:,.0f}".replace(",", " ")
        ))
    lines.append("\n")

    lines.append("**Répartition par année :**\n\n")
    lines.append("| Année | Marchés |\n|---|---|\n")
    year_counts = sub["annee"].value_counts(dropna=False).sort_index()
    for year, count in year_counts.items():
        label = "inconnue" if pd.isna(year) else int(year)
        lines.append("| %s | %d |\n" % (label, count))
    lines.append("\n")

# ===========================================================================
# 4) Croisement mot-clé produit x titulaire connu
# ===========================================================================
lines.append("## 4. Croisement mot-clé produit × titulaire connu\n")

any_keyword = pd.Series(False, index=seg.index)
for label in keyword_masks:
    any_keyword = any_keyword | keyword_masks[label]

any_manuf = pd.Series(False, index=seg.index)
for name in manuf_masks:
    any_manuf = any_manuf | manuf_masks[name]

cross_mask = any_keyword & any_manuf
n_cross = int(cross_mask.sum())
lines.append("**%s lignes** matchent à la fois un mot-clé produit (section 1) "
             "et un titulaire connu (section 3) — %.3f%% du segment.\n\n"
             % (f"{n_cross:,}".replace(",", " "), n_cross / n_total * 100))

if n_cross:
    cross = seg.loc[cross_mask, [
        "objet", "acheteur_nom", "titulaire_nom", "montant_rationalise", "montant_anomalie", "dateNotification"
    ]].sort_values("dateNotification", ascending=False)

    csv_path = "reports/report_cpv_%s_croisement.csv" % CPV_PREFIX
    cross.to_csv(csv_path, index=False)

    INLINE_LIMIT = 100
    lines.append("Détail complet (%s lignes) exporté dans [`%s`](%s), avec la colonne "
                 "`montant_anomalie` pour repérer les montants flagués suspect/aberrant "
                 "par data.gouv.fr. Aperçu des %d marchés les plus récents ci-dessous :\n\n"
                 % (f"{n_cross:,}".replace(",", " "), csv_path.split("/")[-1], csv_path.split("/")[-1],
                    min(INLINE_LIMIT, n_cross)))
    lines.append("| Objet | Acheteur | Titulaire | Montant (€) | Anomalie | Date notification |\n|---|---|---|---|---|---|\n")
    for _, row in cross.head(INLINE_LIMIT).iterrows():
        obj_clean = str(row["objet"]).replace("\n", " ").replace("|", "/").strip()
        montant = "—" if pd.isna(row["montant_rationalise"]) else f"{row['montant_rationalise']:,.0f}".replace(",", " ")
        anomalie = row["montant_anomalie"] if pd.notna(row["montant_anomalie"]) else ""
        lines.append("| %s | %s | %s | %s | %s | %s |\n" % (
            obj_clean, row["acheteur_nom"], row["titulaire_nom"], montant, anomalie, row["dateNotification"]
        ))
    lines.append("\n")
else:
    lines.append("_Aucune ligne ne matche à la fois un mot-clé produit et un "
                 "titulaire connu — les fabricants listés répondent probablement "
                 "sous des libellés d'objet trop génériques (accords-cadres, "
                 "numéros de lot) pour que le mot-clé produit apparaisse.\n\n")

out_path = "reports/report_cpv_%s_granularite.md" % CPV_PREFIX
with open(out_path, "w") as f:
    f.writelines(lines)

print("Report written to", out_path)
