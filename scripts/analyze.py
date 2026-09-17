#!/usr/bin/env python3
"""Filter DECP consolidated data by CPV prefix and produce a report.

Usage: python3 scripts/analyze.py [cpv_prefix]
"""
import sys
import pandas as pd

CPV_PREFIX = sys.argv[1] if len(sys.argv) > 1 else "33"
PARQUET_PATH = "data/decp_consolide.parquet"
SAMPLE_SEED = 42
SAMPLE_SIZE = 50

df = pd.read_parquet(PARQUET_PATH)
total_rows = len(df)

df["codeCPV"] = df["codeCPV"].astype("string")
mask = df["codeCPV"].str.startswith(CPV_PREFIX, na=False)
seg = df[mask].copy()

n = len(seg)

# fill rate per column
fill_rate = (seg.notna().sum() / n * 100).round(2).sort_values(ascending=False)

# sample of free-text objects
sample_pool = seg["objet"].dropna()
sample_n = min(SAMPLE_SIZE, len(sample_pool))
sample = sample_pool.sample(n=sample_n, random_state=SAMPLE_SEED) if sample_n else sample_pool

# year distribution, from dateNotification
seg["annee"] = pd.to_datetime(seg["dateNotification"], errors="coerce").dt.year
year_counts = seg["annee"].value_counts(dropna=False).sort_index()

# --- write report ---
out_path = "reports/report_cpv_%s.md" % CPV_PREFIX
with open(out_path, "w") as f:
    f.write("# Rapport DECP — segment CPV `%s`\n\n" % CPV_PREFIX)
    f.write("- Fichier source : `%s`\n" % PARQUET_PATH)
    f.write("- Lignes totales (tous CPV) : %s\n" % f"{total_rows:,}".replace(",", " "))
    f.write("- Lignes filtrées (CPV commence par `%s`) : %s (%.2f%% du total)\n\n"
            % (CPV_PREFIX, f"{n:,}".replace(",", " "), n / total_rows * 100))

    f.write("## Taux de remplissage par colonne (%)\n\n")
    f.write("| Colonne | Taux de remplissage |\n|---|---|\n")
    for col, rate in fill_rate.items():
        f.write("| %s | %.2f%% |\n" % (col, rate))
    f.write("\n")

    f.write("## Répartition par année (dateNotification)\n\n")
    f.write("| Année | Nombre de marchés |\n|---|---|\n")
    for year, count in year_counts.items():
        label = "inconnue" if pd.isna(year) else int(year)
        f.write("| %s | %s |\n" % (label, f"{count:,}".replace(",", " ")))
    f.write("\n")
    n_aberrant = int((seg["annee"] < 2013).sum())
    if n_aberrant:
        f.write("> ⚠️ %d ligne(s) portent une année aberrante (< 2013 : 5, 22, 23, 26, 205, 226…) — "
                "erreurs de saisie dans la donnée source (ex. `0026-06-17` au lieu de `2026-06-17`), "
                "pas des marchés réellement anciens. Négligeable (~%.3f%% du segment), non corrigé "
                "automatiquement pour éviter de deviner la vraie date.\n\n"
                % (n_aberrant, n_aberrant / n * 100))

    f.write("## Échantillon de %d objets de marché (texte libre)\n\n" % sample_n)
    for i, obj in enumerate(sample, 1):
        obj_clean = str(obj).replace("\n", " ").replace("|", "/").strip()
        f.write("%d. %s\n" % (i, obj_clean))

print("Report written to", out_path)
print("Filtered rows:", n, "/", total_rows)
