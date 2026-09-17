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
