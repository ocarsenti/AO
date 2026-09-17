# Rapport de granularité — segment CPV `33`
Analyse approfondie du champ `objet` (texte libre) sur l'ensemble des **75 784** marchés du segment (pas un échantillon).
> ℹ️ Dédupliqué par `uid` (dernière version par `modification_id`) — voir `scripts/decp_utils.py` et la note en tête de `report_cpv_33.md`.

## 1. Recherche par mots-clés dans `objet`
Recherche en sous-chaîne, insensible à la casse et aux accents (ex. `stent` matche aussi `stents`, `implant` matche aussi `implantable`/`implantation`).
| Mot-clé | Lignes | % du segment |
|---|---|---|
| stent | 158 | 0.21% |
| prothese / prothèse | 2 725 | 3.60% |
| catheter / cathéter | 1 946 | 2.57% |
| implant | 6 450 | 8.51% |
| defibrillateur / défibrillateur | 813 | 1.07% |
| pacemaker / stimulateur cardiaque | 182 | 0.24% |

### stent (158 lignes)
1. FOURNITURES DE DISPOSITIFS MEDICAUX POUR LA NEURORADIOLOGIE INTERVENTIONNELLE POUR LE CHU ROUEN NORMANDIE - Lot 27: Dispositif de thrombectomie mécanique: stent en nitinol auto-expansible avec des motifs à 3 cellules fermées de D jusqu’à 6,5mm et L jusqu’à 57mm
2. Dispositifs médicaux à usage unique de cardiologie pour le groupement de commandes coordonné par le CHU Caen Normandie - STENT CORONAIRE ACTIF
3. FOURNITURES DE DISPOSITIFS MEDICAUX POUR LA NEURORADIOLOGIE INTERVENTIONNELLE POUR LE CHU ROUEN NORMANDIE - Lot 15: Stent intracrânien auto-expansible tressé en nitinol platine à mailles fermées avec des extremitées évasées de diamètre D de 2,5 à 5,5 mm
4. Le présent marché négocié a pour objet la fourniture et livraison de dispositif médicaux spécifiques de stents et de micro cathéters désignés comme suit : - DERIVO 2 ; - ACCLINO ; - NeuroSpeed ; - NeuroSlider DLC.
5. STENT AUTOEXPANSIBLE DE REDIRECTION DU FLUX SANGUIN INTRACRANIEN - Fourniture de dispositifs médicaux pour neuroradiologie interventionnelle (2023/2026)

### prothese / prothèse (2 725 lignes)
1. PROTHESE TOTALE DE GENOU A GLISSEMENT SYMETRIQUE - GAPSCA - Fourniture de dispositifs médicaux pour orthopédie et traumatologie (2023/2027)
2. Fourniture de prothèses chirurgicales et dispositifs médicaux - AO 2018-56 - **ELECTRODE ENDOCAV TEMPORAIRE INTRACARD
3. Fourniture de prothèses chirurgicales et dispositifs médicaux AO 2019-60LOT N° 5 STIMULATEUR CARDIAQUE DOUBLE CHAMBRE
4. FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - PROTHÈSE HANCHE IMPLANTS
5. Prestation de fabrication et de fourniture de prothèses dentaires pour trois établissements parties membres du GHT NORMANDIE CENTRE _ CH Argentan, CHU Caen et EPSM CAEN - Prothèses dentaires amovibles pour le CHU de Caen et l’EPSM Caen

### catheter / cathéter (1 946 lignes)
1. Les Hospices Civils de Lyon sont pouvoir adjudicateur et coordonnateur du groupement de commandes pour la "Fourniture d’objets de pansements". - BANDELETTE ADHESIVE POUR MAINTIEN DE CATHETERS
2. DM CARDIO-1823-19	Catheters  à ballonnet pour Traitement des occlusions chroniques
3. Fourniture de dispositifs médicaux pour l’épuration extra-rénale, au CHRU de Tours - AC - Cathéter longue durée simple branche bilumière + kit de pose
4. Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - AAT- CATHETER D’ABLATION PER OPERATOIRE
5. Fourniture de dispositifs médicaux stériles (DMS) de chirurgie générale (viscérale/urologie/gynécologie/obstétrique) et cathétérisme central (RESAH / ACCHG 2018-004) INTEGRA LIFESCIENCES

### implant (6 450 lignes)
1. Fourniture de Dispositifs Médicaux Implantables: Prothèse totale de genou première intention
2. FOURNITURE DE DISPOSITIFS MEDICAUX IMPLANTABLES - AO CARDIO - ICA25 (2025-2028)
3. DMS 2024-02 AO 092 fourniture de Dispositifs Médicaux Stériles à usage unique  *Casaque, drapage opératoire, compresse, instrument, cupule, tampon, set, pansement tous types, thérapie par pression négative, brosse chirurgicale, immobilisation, contention / compression, maintien. *Dialyse, aphérèse, immunophérèse *Biberon, lacs suspenseurs, dispositifs médicaux non implantables : médecine, chirurgie, électrophysiologie, radiologie, angioplastie, coronarographie. *Dispositifs médicaux implantables toutes spécialités  - MECHE FIBRE
4. Fourniture de dispositifs médicaux stériles, implantables ou non, consommables stériles associés et ancillaires de pose nécessaires à l’activité des établissements membres du GHT Vendée. - ELECTRODE RESTERILISABLE POUR RHIZOLYSE
5. DMS 2024-02 AO 092 fourniture de Dispositifs Médicaux Stériles à usage unique  *Casaque, drapage opératoire, compresse, instrument, cupule, tampon, set, pansement tous types, thérapie par pression négative, brosse chirurgicale, immobilisation, contention / compression, maintien. *Dialyse, aphérèse, immunophérèse *Biberon, lacs suspenseurs, dispositifs médicaux non implantables : médecine, chirurgie, électrophysiologie, radiologie, angioplastie, coronarographie. *Dispositifs médicaux implantables toutes spécialités  - TROUSSE OPERATOIRE EXTREMITE RENFORCEE STANDARD

### defibrillateur / défibrillateur (813 lignes)
1. ACQUISITION DE DEFIBRILLATEURS
2. Fourniture de dispositifs médicaux implantables de cardiologie et d’orthopédie ao2021chro0027  - DEFIBRILLATEUR IMPLANTABLE SIMPLE CHAMBRE Marché n° 222-001 Marché n° 222-011
3. Maintenance et acquisition de défibrillateurs automatisés externes pour la ville de Saint-Herblain.
4. SA3-ACBC- DEFIBRILLATEURS – SUD ET EST DE PARIS - LOT 2
5. Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie et mise à disposition des équipements associés. - JAA- DEFIBRILLATEUR CARDIAQUE IMPLANTABLE

### pacemaker / stimulateur cardiaque (182 lignes)
1. Fourniture de Dispositifs Médicaux Implantables - pour Stimulation & Défibrillation Cardiaque -  - STIMULATEUR CARDIAQUE SANS SONDE AVEC SYSTEME DE POSE
2. Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie et mise à disposition des équipements associés - JAB- STIMULATEUR CARDIAQUE IMPLANTABLE
3. FOURNITURE DE DEFIBRILLATEURS CARDIAQUES IMPLANTABLES, SONDES DE DEFIBRILLATION, STIMULATEURS CARDIAQUES, SONDES DE STIMULATION et SONDES D’ELECTROPHYSIOLOGIE  - STIMULATEUR CARDIAQUE DOUBLE CHAMBRE DDDR AVEC POSSIBILITE D’AUTOCAPTURE VENTRICULAIRE C
4. Fourniture de dispositifs médicaux implantables de cardiologie et d’orthopédie ao2021chro0027  - STIMULATEUR CARDIAQUE SIMPLE CHAMBRE marché n° 222-001 marché n° 222-005 marché n° 222-011
5. Fourniture de stimulateurs cardiaques internes – sondes pour stimulateur et moniteurs ECG implantables pour le Centre Hospitalier de Mâcon.  - Stimulateur cardiaque simple chambre

## 2. Généricité de l'objet
> ⚠️ Mesures heuristiques (regex + liste de mots), pas une vérité absolue — utiles pour estimer un ordre de grandeur, pas pour un décompte exact.

| Critère | Lignes | % du segment |
|---|---|---|
| Référence à un n° de lot sans descripteur produit à proximité | 3 701 | 4.88% |
| Renvoi "voir cahier des charges / CCTP / bordereau" (ou équivalent) | 30 | 0.04% |
| Objet de moins de 5 mots | 10 418 | 13.75% |

### Exemples — Lot sans descripteur produit (3 701 lignes)
1. 22_2437_2_01 Acquisition de préservatifs et lubrifiant pour le CD 91 Lot 1 Préservatifs masculins
2. AGP835-Lot 46
3. 2019-079-006-072 CH Bourg-en-Bresse  LOT 6 - Automate coup par coup avec au minimum le panel syndromique entérique, extraction incorporée avec une seule technologie, fonctionnant sur un seul automate
4. 202208-Lot 7 - Collier cervical adulte, collier cervical enfant
5. Fourniture spécial. pharm GAPLCA lots 74.1,76.4,170.1/2,346.1/3,407.1,679.1,680.1/2,683.1/2,687.1/4,687.1/4,696.1,739.1/2,742.1/3,747.1/2,756.1/2,760.1/6,770.3/4,867.1,867.4,868.4,969.1/2,1019.3,1022.1,1033.1/2,1047.1/3,1059.1,1066.1,1079.2,1103.1,1104.1/3

### Exemples — Renvoi cahier des charges / CCTP / bordereau (30 lignes)
1. PANSG PANSEMENT ET MATERIELS DE STERILISATION - 89 LOTS VOIR DETAIL DANS CAHIER DES CHARGES
2. PANSG PANSEMENT ET MATERIELS DE STERILISATION - 89 LOTS VOIR DETAIL DANS CAHIER DES CHARGES
3. PANSG PANSEMENT ET MATERIELS DE STERILISATION - 89 LOTS VOIR DETAIL DANS CAHIER DES CHARGES
4. PANSG PANSEMENT ET MATERIELS DE STERILISATION - 89 LOTS VOIR DETAIL DANS CAHIER DES CHARGES
5. PANSG PANSEMENT ET MATERIELS DE STERILISATION - 89 LOTS VOIR DETAIL DANS CAHIER DES CHARGES

### Exemples — Objet de moins de 5 mots (10 418 lignes)
1. FILTRATION - SIGMA ALDRICH
2. 23DMS - MEDTRONIC
3. Achat de défibrillateurs
4. MEDICAMENTS NON SUBSTITUABLES
5. KIT DRAINAGE LONG TERME

## 3. Filtrage par titulaire connu (fabricants)
> Montants calculés sur `montant_rationalise`, **en excluant les lignes flaguées `montant_anomalie` ("suspect"/"aberrant") par data.gouv.fr** — sur l'ensemble du segment, 1 177 lignes (1.55%) portent un tel flag mais pèsent à elles seules 37% de la somme brute des montants (ex. montant total d'un accord-cadre recopié sur un seul lot). Lignes sans montant fiable également exclues des moyennes/totaux ; le nombre de marchés reste inchangé (compte sur tous les marchés, montant fiable ou non).

| Fabricant | Marchés | dont montant exclu (anomalie) | Montant total (€) | Montant moyen (€) |
|---|---|---|---|---|
| Medtronic | 1 738 | 34 | 2 228 303 650 | 1 349 669 |
| Abbott | 1 098 | 15 | 2 043 529 739 | 1 920 611 |
| Boston Scientific | 1 216 | 16 | 967 002 883 | 822 981 |
| Biotronik | 281 | 4 | 231 408 599 | 841 486 |
| Stryker | 941 | 27 | 1 315 131 730 | 1 459 636 |
| Zimmer Biomet | 373 | 7 | 283 862 694 | 804 144 |
| Johnson & Johnson / DePuy Synthes | 1 015 | 21 | 925 654 714 | 960 223 |
| Getinge | 259 | 4 | 182 189 034 | 717 280 |

### Medtronic (1 738 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 150 | 58 518 013 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 134 | 218 309 023 |
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 126 | 450 607 345 |
| RESEAU DES ACHETEURS HOSPITALIERS | 123 | 445 766 827 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE CAEN NORMANDIE | 85 | 64 040 363 |
| CENTRE HOSPITALIER DE COLMAR (CENTRE HOSPITALIER LOUIS PASTEUR) | 80 | 8 088 075 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 70 | 104 457 216 |
| CENTRE HOSPITALIER UNIVERSITAIRE | 64 | 14 211 718 |
| CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | 63 | 24 233 053 |
| CENTRE HOSPITALIER UNIVERSITAIRE D ORLEANS (HOPITAL MADELEINE ORLEANS) | 47 | 7 131 258 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2016 | 1 |
| 2017 | 6 |
| 2018 | 26 |
| 2019 | 185 |
| 2020 | 166 |
| 2021 | 199 |
| 2022 | 221 |
| 2023 | 301 |
| 2024 | 150 |
| 2025 | 297 |
| 2026 | 185 |
| inconnue | 1 |

### Abbott (1 098 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 81 | 49 070 812 |
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 80 | 182 195 362 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 79 | 189 459 802 |
| CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | 52 | 30 744 391 |
| CENTRE HOSPITALIER DE VALENCIENNES | 52 | 54 534 109 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE CAEN NORMANDIE | 44 | 75 495 187 |
| RESEAU DES ACHETEURS HOSPITALIERS | 44 | 316 365 660 |
| CENTRE HOSPITALIER UNIVERSITAIRE D ORLEANS (HOPITAL MADELEINE ORLEANS) | 42 | 5 372 700 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 41 | 189 918 918 |
| CENTRE HOSPITALIER UNIVERSITAIRE | 41 | 51 817 200 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2017 | 1 |
| 2018 | 11 |
| 2019 | 63 |
| 2020 | 116 |
| 2021 | 138 |
| 2022 | 168 |
| 2023 | 176 |
| 2024 | 87 |
| 2025 | 175 |
| 2026 | 158 |
| inconnue | 5 |

### Boston Scientific (1 216 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 123 | 170 585 326 |
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 105 | 17 931 566 |
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 65 | 147 749 866 |
| CENTRE HOSPITALIER DE COLMAR (CENTRE HOSPITALIER LOUIS PASTEUR) | 60 | 4 520 368 |
| CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | 54 | 9 195 709 |
| RESEAU DES ACHETEURS HOSPITALIERS | 52 | 163 547 247 |
| CENTRE HOSPITALIER UNIVERSITAIRE D ORLEANS (HOPITAL MADELEINE ORLEANS) | 48 | 5 673 386 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE CAEN NORMANDIE | 44 | 41 604 493 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 44 | 39 533 500 |
| CENTRE HOSPITALIER DE VALENCIENNES | 41 | 30 935 187 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2017 | 2 |
| 2018 | 11 |
| 2019 | 116 |
| 2020 | 123 |
| 2021 | 156 |
| 2022 | 181 |
| 2023 | 217 |
| 2024 | 103 |
| 2025 | 168 |
| 2026 | 137 |
| inconnue | 2 |

### Biotronik (281 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 30 | 7 895 383 |
| CENTRE HOSPITALIER UNIVERSITAIRE D ORLEANS (HOPITAL MADELEINE ORLEANS) | 28 | 4 024 471 |
| CENTRE HOSPITALIER DE COLMAR (CENTRE HOSPITALIER LOUIS PASTEUR) | 22 | 2 121 762 |
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 15 | 43 156 721 |
| CHD LA ROCHE SUR YON LUCON MONTAIGU (CHD-VENDEE) | 14 | 1 577 764 |
| CENTRE HOSPITALIER D AUXERRE | 13 | 0 |
| CENTRE HOSPITALIER LES CHANAUX | 13 | 1 221 866 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 12 | 11 592 550 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 12 | 11 302 495 |
| CENTRE HOSPITALIER DE PAU | 11 | 2 744 709 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2017 | 1 |
| 2018 | 1 |
| 2019 | 33 |
| 2020 | 36 |
| 2021 | 27 |
| 2022 | 48 |
| 2023 | 62 |
| 2024 | 18 |
| 2025 | 31 |
| 2026 | 24 |

### Stryker (941 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| RESEAU DES ACHETEURS HOSPITALIERS | 128 | 517 969 102 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 74 | 117 549 070 |
| HOPITAL LE MANS | 60 | 5 819 243 |
| CENTRE HOSPITALIER DE BOULOGNE SUR MER | 44 | 2 792 890 |
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 44 | 81 854 846 |
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 40 | 15 521 336 |
| CENTRE HOSPITALIER DE VALENCIENNES | 37 | 14 824 981 |
| CTRE HOSPITALIER VILLEFRANCHE S SAONE | 36 | 6 389 418 |
| CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | 34 | 20 329 356 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 34 | 31 977 873 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2017 | 1 |
| 2018 | 11 |
| 2019 | 70 |
| 2020 | 60 |
| 2021 | 166 |
| 2022 | 110 |
| 2023 | 115 |
| 2024 | 111 |
| 2025 | 163 |
| 2026 | 133 |
| inconnue | 1 |

### Zimmer Biomet (373 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| RESEAU DES ACHETEURS HOSPITALIERS | 43 | 96 669 383 |
| CENTRE HOSPITALIER DE BOULOGNE SUR MER | 32 | 1 800 916 |
| CENTRE HOSPITALIER DE VALENCIENNES | 27 | 28 049 461 |
| CENTRE HOSPITALIER DE DUNKERQUE | 24 | 1 675 216 |
| HOPITAL LE MANS | 21 | 3 181 303 |
| CENTRE HOSPITALIER DE COLMAR (CENTRE HOSPITALIER LOUIS PASTEUR) | 21 | 1 123 777 |
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 16 | 3 652 978 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 16 | 56 667 035 |
| CHD LA ROCHE SUR YON LUCON MONTAIGU (CHD-VENDEE) | 13 | 14 303 827 |
| CENTRE HOSPITALIER UNIVERSITAIRE GRENOBLE ALPES (HOPITAL NORD) | 11 | 5 185 086 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2018 | 1 |
| 2019 | 30 |
| 2020 | 23 |
| 2021 | 91 |
| 2022 | 62 |
| 2023 | 56 |
| 2024 | 27 |
| 2025 | 32 |
| 2026 | 51 |

### Johnson & Johnson / DePuy Synthes (1 015 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| CENTRE HOSPITALIER DE COLMAR (CENTRE HOSPITALIER LOUIS PASTEUR) | 109 | 3 579 564 |
| RESEAU DES ACHETEURS HOSPITALIERS | 96 | 243 021 763 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 87 | 139 466 136 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 55 | 56 541 786 |
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 48 | 12 667 458 |
| CENTRE HOSPITALIER DE VALENCIENNES | 37 | 24 356 391 |
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 37 | 31 159 696 |
| CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | 34 | 10 429 059 |
| CENTRE HOSPITALIER DE BOULOGNE SUR MER | 33 | 2 994 826 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE CAEN NORMANDIE | 31 | 10 674 201 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2018 | 16 |
| 2019 | 85 |
| 2020 | 104 |
| 2021 | 137 |
| 2022 | 120 |
| 2023 | 175 |
| 2024 | 113 |
| 2025 | 128 |
| 2026 | 137 |

### Getinge (259 marchés)
**Top 10 acheteurs (par nombre de marchés) :**

| Acheteur | Marchés | Montant total fiable (€) |
|---|---|---|
| CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | 31 | 35 262 796 |
| CTRE HOSPITALIER UNIVERS PONTCHAILLOU | 21 | 1 434 053 |
| GROUPEMENT COOPERATION SANITAIRE - UNION DES HOPITAUX POUR LES ACHATS | 15 | 36 619 676 |
| HOSPICES CIVILS DE LYON (SIEGE ADMINISTRATIF) | 12 | 42 126 179 |
| CHU NANTES (DIRECTION GENERALE) | 11 | 6 263 288 |
| CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | 11 | 1 311 223 |
| CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | 11 | 12 605 955 |
| HOPITAL LE MANS | 10 | 392 911 |
| CENTRE HOSPITALIER DE SAINT-BRIEUC, PAIMPOL ET TREGUIER | 8 | 607 233 |
| CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | 8 | 5 909 221 |

**Répartition par année :**

| Année | Marchés |
|---|---|
| 2018 | 2 |
| 2019 | 28 |
| 2020 | 36 |
| 2021 | 30 |
| 2022 | 30 |
| 2023 | 51 |
| 2024 | 14 |
| 2025 | 41 |
| 2026 | 27 |

## 4. Croisement mot-clé produit × titulaire connu
**2 664 lignes** matchent à la fois un mot-clé produit (section 1) et un titulaire connu (section 3) — 3.515% du segment.

Détail complet (2 664 lignes) exporté dans [`report_cpv_33_croisement.csv`](report_cpv_33_croisement.csv), avec la colonne `montant_anomalie` pour repérer les montants flagués suspect/aberrant par data.gouv.fr. Aperçu des 100 marchés les plus récents ci-dessous :

| Objet | Acheteur | Titulaire | Montant (€) | Anomalie | Date notification |
|---|---|---|---|---|---|
| DM implantables. Lot 106 | RESEAU DES ACHETEURS HOSPITALIERS | BOSTON SCIENTIFIC | 199 485 |  | 2026-09-08 |
| DM implantables. Lot 30: Système cardiovasculaire ABBOTT MEDICAL (Vascular) ou équivalent | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 368 000 |  | 2026-08-28 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTCONC - OSTÉOSYNTHÈSE : FRACTURE PÉRI PROTHÉTIQUE | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 2 139 209 |  | 2026-08-26 |
| Prothèse pariétale en polyester non résorbable auto-fixante pour le traitement des hernies ventrales | CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | MEDTRONIC FRANCE | 99 528 |  | 2026-08-25 |
| Prothèse pariétale non résorbable biface en polyéthylène avec film hydrogel de collagène pour le traitement des hernies ventrales, pose en intra péritonéal par colioscopie | CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | MEDTRONIC FRANCE | 138 328 |  | 2026-08-25 |
| Prothèse pariétale biologique pour le traitement des hernies ventrales | CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | MEDTRONIC FRANCE | 305 428 |  | 2026-08-25 |
| Prothèse pariétale préformée en polypropylène monofilament anatomique en 3D pour le traitement des hernies inguinales par coelioscopie | CENTRE HOSPITALIER UNIVERSITAIRE ROUEN (HOPITAL CHARLES NICOLLE CHU ROUEN) | MEDTRONIC FRANCE | 58 608 |  | 2026-08-25 |
| RYT 24 - HOLTER ECG IMPLANTABLE | CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | BOSTON SCIENTIFIC | 858 000 |  | 2026-08-20 |
| RYT 24 - DEFIBRILLATEUR ENDOCAVITAIRE AVEC SONDE SOUS-STERNALE | CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | MEDTRONIC FRANCE | 320 000 |  | 2026-08-20 |
| RYT 24 - STIMULATEUR CARDIAQUE SANS SONDE | CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | MEDTRONIC FRANCE | 3 200 000 |  | 2026-08-20 |
| Fourniture d¿implants d¿orthopédie, pour prothèses articulaires, pour ostéosynthèse, pour ligamentoplastie, de ciment orthopédique et prêt des ancillaires associés | CTRE HOSPITALIER VILLEFRANCHE S SAONE | ZIMMER BIOMET FRANCE | 63 466 |  | 2026-08-19 |
| XSTIM - Stimulateur cardiaque double chambre asservi | CENTRE HOSPITALIER DE VALENCIENNES | ABBOTT MEDICAL FRANCE SAS | 5 768 124 |  | 2026-08-17 |
| XSTIM - Stimulateur cardiaque double chambre asservi | CENTRE HOSPITALIER DE VALENCIENNES | MEDTRONIC FRANCE | 882 482 |  | 2026-08-14 |
| XCARD - IMPLANT POUR OCCLUSION D’UN FORAMEN OVALE PERMEABLE | CENTRE HOSPITALIER DE VALENCIENNES | ABBOTT MEDICAL FRANCE SAS | 2 124 168 |  | 2026-08-14 |
| DM ORTHO.Lot 14:Prothèse Epaule ZIMMER BIOMET ou équivalent | RESEAU DES ACHETEURS HOSPITALIERS | ZIMMER BIOMET FRANCE | 102 333 |  | 2026-08-11 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - OSTÉOSYNTHÈSE: PLAQUE ET VIS | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 742 654 |  | 2026-08-06 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - IMPLANT FIXATION LIGAMENTAIRE | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 71 614 |  | 2026-08-06 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - PROTHÈSE GENOU | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 103 167 |  | 2026-08-06 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - PROTHÈSE HANCHE | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 52 872 |  | 2026-08-06 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - PROTHÈSE COUDE | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 193 893 |  | 2026-08-06 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTCONC - GENOU : PROTHÈSE TOTALE GENOU À PLATEAU FIXE ET ROTATOIRE | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | ZIMMER BIOMET FRANCE | 1 532 251 |  | 2026-08-06 |
| Fourniture de dispositifs médicaux de cardiologie, chirurgie vasculaire et neuroradiologie  (Relance des lots 67-68-112-113-114-123, suite radiation codes LPPR)   - GAA- ENDOPROTHESE CORONAIRE A PRINCIPE ACTIF | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | MEDTRONIC FRANCE | 1 129 144 |  | 2026-08-04 |
| Fourniture de dispositifs médicaux de cardiologie, chirurgie vasculaire et neuroradiologie  (Relance des lots 67-68-112-113-114-123, suite radiation codes LPPR)   - GAA- ENDOPROTHESE CORONAIRE A PRINCIPE ACTIF | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | BOSTON SCIENTIFIC | 546 840 |  | 2026-08-04 |
| Fourniture de dispositifs médicaux de cardiologie, chirurgie vasculaire et neuroradiologie  (Relance des lots 67-68-112-113-114-123, suite radiation codes LPPR)   - GAA- ENDOPROTHESE CORONAIRE A PRINCIPE ACTIF | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 585 330 |  | 2026-08-04 |
| XORTO - PROTHESE TOTALE DE GENOU POUR CHIRURGIE ROBOTISEE | CENTRE HOSPITALIER DE VALENCIENNES | ZIMMER BIOMET FRANCE | 22 341 176 |  | 2026-08-04 |
| Fourniture de dispositifs médicaux de cardiologie, chirurgie vasculaire et neuroradiologie  (Relance des lots 67-68-112-113-114-123, suite radiation codes LPPR)   - DAU- CATHETER ANGIOPLASTIE PERIPHERIQUE AVEC PRINCIPE ACTIF | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | MEDTRONIC FRANCE | 45 572 |  | 2026-08-04 |
| Fourniture de dispositifs médicaux de cardiologie, chirurgie vasculaire et neuroradiologie  (Relance des lots 67-68-112-113-114-123, suite radiation codes LPPR)   - FBH- ENDOPROTHESE CAROTIDIENNE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | BOSTON SCIENTIFIC | 75 000 |  | 2026-08-04 |
| Fourniture de dispositifs stériles pour coronarographie et angioplastie coronaire - Cathéter d’aspiration | GROUPE HOSPITALIER RANCE EMERAUDE | MEDTRONIC FRANCE | 27 000 |  | 2026-08-01 |
| Fourniture de dispositifs stériles pour coronarographie et angioplastie coronaire - Endoprothèse coronaire coatée à polymère bioresorbable | GROUPE HOSPITALIER RANCE EMERAUDE | BOSTON SCIENTIFIC | 133 742 |  | 2026-08-01 |
| Fourniture de dispositifs stériles pour coronarographie et angioplastie coronaire - Endoprothèse coronaire coatée à polymère durable avec diametre compris entre 2mm et 5mm | GROUPE HOSPITALIER RANCE EMERAUDE | MEDTRONIC FRANCE | 357 956 |  | 2026-08-01 |
| Fourniture de dispositifs stériles pour coronarographie et angioplastie coronaire - Endoprothèse coronaire coatée à polymère durable | GROUPE HOSPITALIER RANCE EMERAUDE | ABBOTT MEDICAL FRANCE SAS | 664 778 |  | 2026-08-01 |
| Fourniture de dispositifs stériles pour coronarographie et angioplastie coronaire - Cathéter guide | GROUPE HOSPITALIER RANCE EMERAUDE | MEDTRONIC FRANCE | 152 514 |  | 2026-08-01 |
| 2026-0219 - FOURNITURE DE DISPOSITIFS MEDICAUX PROTHETIQUES IMPLANTABLES : FAMILLES ORL. UROLOGIE - SOFAMAO2 (2026-2029) | CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | BOSTON SCIENTIFIC | 525 300 |  | 2026-07-29 |
| 2026-0219 - FOURNITURE DE DISPOSITIFS MEDICAUX PROTHETIQUES IMPLANTABLES : FAMILLES ORL. UROLOGIE - SOFAMAO2 (2026-2029) | CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | BOSTON SCIENTIFIC | 525 300 |  | 2026-07-29 |
| XCARD - CATHETER ABLATION  FA | CENTRE HOSPITALIER DE VALENCIENNES | ABBOTT MEDICAL FRANCE SAS | 2 048 280 |  | 2026-07-29 |
| 2025-0785 - FOURNITURE DE DISPOSITIFS MEDICAUX PROTHETIQUES IMPLANTABLES : FAMILLES ENDOSCOPIE DIGESTIVE, CHIRURGIE PLASTIQUE ET REPARATRICE, ORL, PNEUMOLOGIE, UROLOGIE, GYNECOLOGIE - FAMDIVAO2 (2025-2029) | CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | MEDTRONIC FRANCE | 12 600 |  | 2026-07-28 |
| 2025-0785 - FOURNITURE DE DISPOSITIFS MEDICAUX PROTHETIQUES IMPLANTABLES : FAMILLES ENDOSCOPIE DIGESTIVE, CHIRURGIE PLASTIQUE ET REPARATRICE, ORL, PNEUMOLOGIE, UROLOGIE, GYNECOLOGIE - FAMDIVAO2 (2025-2029) | CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | BOSTON SCIENTIFIC | 53 835 |  | 2026-07-28 |
| LGS25 FOURNITURE  DE LIGATURES ¿ AUTOSUTURES ¿ PROTHESES VISCERALES | CTRE HOSPITALIER INTERCOM ALPES DU SUD (SITE HOSPITALIER DE GAP) | JOHNSON & JOHNSON MEDICAL SAS | 422 998 |  | 2026-07-28 |
| LGS25 FOURNITURE  DE LIGATURES ¿ AUTOSUTURES ¿ PROTHESES VISCERALES | CTRE HOSPITALIER INTERCOM ALPES DU SUD (SITE HOSPITALIER DE GAP) | MEDTRONIC FRANCE | 446 712 |  | 2026-07-28 |
| 2025-0785 - FOURNITURE DE DISPOSITIFS MEDICAUX PROTHETIQUES IMPLANTABLES : FAMILLES ENDOSCOPIE DIGESTIVE, CHIRURGIE PLASTIQUE ET REPARATRICE, ORL, PNEUMOLOGIE, UROLOGIE, GYNECOLOGIE - FAMDIVAO2 (2025-2029) | CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | BOSTON SCIENTIFIC | 53 835 |  | 2026-07-28 |
| 2025-0785 - FOURNITURE DE DISPOSITIFS MEDICAUX PROTHETIQUES IMPLANTABLES : FAMILLES ENDOSCOPIE DIGESTIVE, CHIRURGIE PLASTIQUE ET REPARATRICE, ORL, PNEUMOLOGIE, UROLOGIE, GYNECOLOGIE - FAMDIVAO2 (2025-2029) | CENTRE HOSPITALIER REGIONAL DE MARSEILLE (ASSISTANCE PUBLIQUE-HOPITAUX MARSEILLE) | MEDTRONIC FRANCE | 12 600 |  | 2026-07-28 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - OSTÉOSYNTHÈSE: PLAQUE ET VIS | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | STRYKER FRANCE SA | 1 171 594 |  | 2026-07-23 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 57 : Cathéter ballonnet angioplastie coronaire, monorail, semi-compliant | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 16 296 680 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 48 : Système fermeture point de ponction artérielle chirurgical | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 19 044 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 55 : Cathéter ballonnet angioplastie coronaire, monorail, non compliant, revêtement hydrophile | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 8 659 800 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 22 : Concentré acide, vrac | RESEAU DES ACHETEURS HOSPITALIERS | MEDTRONIC FRANCE | 2 340 780 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 114: Sonde transoesophagienne procédure électrophysiologie | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 8 013 200 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 98 : Guide vasculaire périphérique 0.014" à 0.018" , recanalisation | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 3 474 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 105: Cathéter électrophysiologie conventionnelle, diagnostic, courbure fixe, PEBAX, 4 pôles | RESEAU DES ACHETEURS HOSPITALIERS | BIOTRONIK FRANCE | 2 372 480 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 113: Cathéter électrophysiologie ablation RF, irriguée, mesure de la force de contact | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 14 605 200 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 111: Cathéter électrophysiologie ablation RF, courbure bidirectionnelle | RESEAU DES ACHETEURS HOSPITALIERS | BOSTON SCIENTIFIC | 9 188 176 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 106: Cathéter électrophysiologie conventionnelle, diagnostic, courbure fixe, PUR, 4 et 10 pôles | RESEAU DES ACHETEURS HOSPITALIERS | BOSTON SCIENTIFIC | 2 708 800 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 107: Cathéter électrophysiologie conventionnelle, diagnostic, courbure orientable, PEBAX, 4 et 10 pôles | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 12 899 200 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 115: Gaine et Aiguille trans-septale | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 20 502 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 91 : Cathéter ballonnet angioplastie périphérique semi-compliant, recanalisation sous-poplitée | RESEAU DES ACHETEURS HOSPITALIERS | MEDTRONIC FRANCE | 2 490 400 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 110: Cathéter électrophysiologie ablation RF, courbure unidirectionnelle | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 6 356 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 64 : Cathéter Imagerie endocoronaire, Console tomographie cohérence optique OCT | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 26 931 840 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 104: Sonde-électrode stimulation temporaire bipolaire implantation percutanée | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 914 640 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 54 : Cathéter ballonnet angioplastie coronaire, monorail, non compliant | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 13 516 880 |  | 2026-07-21 |
| DMNI1026 DM non implantables 2025-R077 LOTS 35_36_48_54_55_57_64_77_90_98_104 | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 200 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 61 : Cathéter guide angioplastie coronaire, revêtement interne silicone 5 à 8Fr | RESEAU DES ACHETEURS HOSPITALIERS | MEDTRONIC FRANCE | 25 140 752 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 62 : Extension de cathéter guide flexible | RESEAU DES ACHETEURS HOSPITALIERS | BOSTON SCIENTIFIC | 7 249 600 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 63 : Cathéter Echographie endocoronaire, Console-Module IVUS (intravascular ultrasound) | RESEAU DES ACHETEURS HOSPITALIERS | BOSTON SCIENTIFIC | 11 436 400 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 77 : Guide mesure Fraction Flux de Réserve coronaire (FFR) | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 29 274 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 80 : Système protection distale capture d’embol | RESEAU DES ACHETEURS HOSPITALIERS | MEDTRONIC FRANCE | 2 960 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 35 : Valve hémostatique mixte à vis et à poussoir | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 612 800 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 82 : Cathéter ballonnet modelage endoprothèse aortique | RESEAU DES ACHETEURS HOSPITALIERS | MEDTRONIC FRANCE | 1 736 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 36 : Kit inflation (seringue inflation, tubulure, valve, torquer..) | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 31 315 720 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 116: Aiguile de ponction trans-septale par radiofréquence | RESEAU DES ACHETEURS HOSPITALIERS | BOSTON SCIENTIFIC | 12 054 000 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lot 1 à 100 - Lot 90 : Cathéter ballonnet angioplastie périphérique semi-compliant, guide 0.035" | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 7 679 200 |  | 2026-07-21 |
| Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 109: Cathéter électrophysiologie conventionnelle, diagnostic, courbure orientable, 20 Pôles | RESEAU DES ACHETEURS HOSPITALIERS | ABBOTT MEDICAL FRANCE SAS | 3 657 200 |  | 2026-07-21 |
| CMF.IMPLANTS CRANIO-FACIAU S/M | CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | STRYKER FRANCE SA | 684 165 |  | 2026-07-09 |
| ORTCONC Epaule : Prothèse Totale Epaule Anatomique convertible et traumatologie | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | STRYKER FRANCE SA | 1 872 642 |  | 2026-07-08 |
| STM25 FOURNITURE DE DISPOSITIFS MEDICAUX STERILES ET DISPOSITIFS MEDICAUX IMPLANTABLES, DE RYTHMOLOGIE ET D¿ELECTROPHYSIOLOGIE | CTRE HOSPITALIER INTERCOM ALPES DU SUD (SITE HOSPITALIER DE GAP) | BIOTRONIK FRANCE | 330 421 |  | 2026-07-03 |
| XRADI - STENT RETRIEVER TRES PETIT DIAMETRE | CENTRE HOSPITALIER DE VALENCIENNES | STRYKER FRANCE SA | 439 085 |  | 2026-07-03 |
| XORTO - PROTHESE TOTALE DE GENOU à CHARNIERE ROTATOIRE | CENTRE HOSPITALIER DE VALENCIENNES | ZIMMER BIOMET FRANCE | 803 136 |  | 2026-07-03 |
| XRADI-2 ENDOPROTHESE VASCULAIRE CRANIENNE | CENTRE HOSPITALIER DE VALENCIENNES | STRYKER FRANCE SA | 156 682 |  | 2026-07-01 |
| Fourniture de dispositifs médicaux du domaine de la cardiologie interventionnelle, de l’abord vasculaire périphérique, de la radiologie interventionnelle, des endoprothèses, de la neuroradiologie et de la radiologie AO-2024-177 | CENTRE HOSPITALIER UNIVERSITAIRE DE LILLE | STRYKER FRANCE SA | 5 875 200 |  | 2026-07-01 |
| RYT 24 - HOLTER ECG IMPLANTABLE | CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | ABBOTT MEDICAL FRANCE SAS | 801 198 |  | 2026-06-22 |
| FOURNITURES DE DISPOSITIFS MEDICAUX IMPLANTABLES ET DISPOSITIFS MEDICAUX SPECIALISES 2025 – N°MNSP25DMISP | CENTRE HOSPITALIER UNIVERSITAIRE GRENOBLE ALPES (HOPITAL NORD) | STRYKER FRANCE SA | 1 600 000 | suspect | 2026-06-22 |
| Fourniture de prothèses orthopédiques et d’accessoires d’ostéosynthèses pour le Centre Hospitalier de la Région de Saint-Omer | CENTRE HOSPITALIER DE DUNKERQUE | STRYKER FRANCE SA | 35 386 |  | 2026-06-18 |
| Fourniture de prothèses orthopédiques et d’accessoires d’ostéosynthèses pour le Centre Hospitalier de la Région de Saint-Omer | CENTRE HOSPITALIER DE DUNKERQUE | ZIMMER BIOMET FRANCE | 148 912 |  | 2026-06-18 |
| Fourniture de prothèses orthopédiques et d’accessoires d’ostéosynthèses pour le Centre Hospitalier de la Région de Saint-Omer | CENTRE HOSPITALIER DE DUNKERQUE | JOHNSON & JOHNSON MEDICAL SAS | 35 386 |  | 2026-06-18 |
| HCL FOURNITURE DE STENTS CORONAIRES, BALLONS ACTIFS, CATHETERS DE DILATATION ET SERVICES ASSOCIES | CTRE HOSPITALIER VILLEFRANCHE S SAONE | ABBOTT MEDICAL FRANCE SAS | 213 270 |  | 2026-06-18 |
| XSTIM - Holter implantable | CENTRE HOSPITALIER DE VALENCIENNES | BIOTRONIK FRANCE | 5 154 360 |  | 2026-06-16 |
| XRADI - STENT RETRIEVER PETIT DIAMETRE | CENTRE HOSPITALIER DE VALENCIENNES | MEDTRONIC FRANCE | 961 805 |  | 2026-06-16 |
| FOURNITURE D’IMPLANTS D’ORTHOPÉDIE - ORTHOCAT - CLOU CENTRO-MÉDULLAIRE | CENTRE HOSPITALIER UNIVERSITAIRE REIMS | JOHNSON & JOHNSON MEDICAL SAS | 48 416 |  | 2026-06-11 |
| XPORA - CATHETER D’ELECTROPORATION | CENTRE HOSPITALIER DE VALENCIENNES | BOSTON SCIENTIFIC | 2 189 000 |  | 2026-06-09 |
| Fournitures de produits pharmaceutiques: Dispositifs Médicaux Stériles au Groupement GAULoYS (280 lots) - CATHETER DRAINAGE BILIAIRE - STERILE | CTRE HOSPITALIER INTERCOMMUNAL AGGLOMERATION DE NEVERS | BOSTON SCIENTIFIC | 0 |  | 2026-06-08 |
| RYT 24 - HOLTER ECG IMPLANTABLE | CENTRE HOSPITALIER UNIVERSITAIRE DE TOULOUSE (HOTEL DIEU SAINT JACQUES) | BIOTRONIK FRANCE | 801 198 |  | 2026-06-08 |
| DM ORTHO. Lot 4:Hanche : Prothèse Totale Hanche tous couples de frottements et double mobilité | RESEAU DES ACHETEURS HOSPITALIERS | STRYKER FRANCE SA | 88 479 |  | 2026-06-05 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - GAI- CATHETER ANGIOPLASTIE CORONAIRE NON COMPLIANT | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 170 000 |  | 2026-06-03 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - GAJ- CATHETER ANGIOPLASTIE CORONAIRE SEMI-COMPLIANT | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 396 000 |  | 2026-06-03 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - GAC- ENDOPROTHESE CARDIAQUE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 708 056 |  | 2026-06-03 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - GAD-  ENDOPROTHESE CARDIAQUE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 630 878 |  | 2026-06-03 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - GAE- ENDOPROTHESE CARDIAQUE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 803 614 |  | 2026-06-03 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - GAH- ENDOPROTHESE CARDIAQUE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 75 649 |  | 2026-06-03 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - KAA- CATHETER DIAGNOSTIC BIPOLAIRE OU QUADRIPOLAIRE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | ABBOTT MEDICAL FRANCE SAS | 363 168 |  | 2026-06-02 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - JAD- STIMULATEUR CARDIAQUE IMPLANTABLE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | BIOTRONIK FRANCE | 1 532 219 |  | 2026-06-02 |
| Fourniture de dispositifs médicaux de cardiologie, électrophysiologie, radiologie, chirurgie cardiaque, chirurgie vasculaire, neuroradiologie, assistance monitoring invasif  et mise à disposition des équipements associés - JAD- STIMULATEUR CARDIAQUE IMPLANTABLE | CENTRE HOSPITALIER REGIONAL UNIVERSITAIRE DE TOURS (CHRU TROUSSEAU CHAMBRAY) | BOSTON SCIENTIFIC | 1 149 164 |  | 2026-06-02 |

