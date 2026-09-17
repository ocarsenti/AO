# AO — analyse DECP par segment CPV

Analyse du fichier consolidé des Données Essentielles de la Commande Publique
(DECP), filtré par préfixe de code CPV, avec rapport de qualité et
d'échantillonnage.

## Source

Fichier consolidé (format Parquet) de data.gouv.fr :
https://www.data.gouv.fr/datasets/donnees-essentielles-de-la-commande-publique-consolidees-format-tabulaire

Téléchargé le 2026-09-17 (~236 Mo, 3 278 751 lignes, 66 colonnes). Ce jeu de
données est régénéré quasi quotidiennement par data.gouv.fr ; relancer le
téléchargement pour une version à jour.

## Utilisation

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas pyarrow

# télécharger le fichier source (pas versionné dans git, voir .gitignore)
curl -L -o data/decp_consolide.parquet \
  https://www.data.gouv.fr/api/1/datasets/r/11cea8e8-df3e-4ed1-932b-781e2635e432

# générer le rapport pour un préfixe CPV donné (ex: 33 = santé/pharma)
python3 scripts/analyze.py 33
```

Le rapport est écrit dans `reports/report_cpv_<prefix>.md` et contient :
- nombre de lignes filtrées vs. total
- taux de remplissage par colonne
- répartition par année (`dateNotification`)
- échantillon aléatoire de 50 objets de marché (texte libre)

## Segments déjà générés

- `reports/report_cpv_33.md` — Santé / pharma (CPV 33xxxxxx), 124 396 marchés
