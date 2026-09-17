# Rapport DECP — segment CPV `33`

- Fichier source : `data/decp_consolide.parquet`
- Lignes totales (tous CPV) : 3 278 751
- Lignes filtrées (CPV commence par `33`) : 124 396 (3.79% du total)

## Taux de remplissage par colonne (%)

| Colonne | Taux de remplissage |
|---|---|
| uid | 100.00% |
| id | 100.00% |
| acheteur_id | 100.00% |
| type | 100.00% |
| codeCPV | 100.00% |
| sourceDataset | 100.00% |
| sourceFile | 100.00% |
| objet | 99.98% |
| lieuExecution_code | 99.81% |
| lieuExecution_typeCode | 99.81% |
| donneesActuelles | 99.26% |
| modification_id | 99.26% |
| dateNotification | 99.26% |
| acheteur_departement_nom | 99.23% |
| acheteur_commune_code | 99.23% |
| acheteur_commune_nom | 99.23% |
| acheteur_departement_code | 99.23% |
| acheteur_nom | 99.23% |
| acheteur_region_code | 99.23% |
| acheteur_region_nom | 99.23% |
| datePublicationDonnees | 99.07% |
| dureeMois | 98.91% |
| nature | 98.78% |
| dureeRestanteMois | 98.65% |
| titulaire_typeIdentifiant | 97.45% |
| titulaire_id | 97.29% |
| montant | 97.06% |
| montant_rationalise | 97.06% |
| formePrix | 96.77% |
| procedure | 94.94% |
| titulaire_activite_code | 94.76% |
| titulaire_nom | 94.76% |
| titulaire_activite_libelle | 94.62% |
| titulaire_commune_nom | 93.86% |
| titulaire_region_code | 93.86% |
| titulaire_region_nom | 93.86% |
| titulaire_departement_nom | 93.86% |
| titulaire_departement_code | 93.86% |
| titulaire_commune_code | 93.86% |
| titulaire_categorie | 93.58% |
| acheteur_latitude | 92.09% |
| acheteur_longitude | 92.09% |
| titulaire_latitude | 87.51% |
| titulaire_longitude | 87.51% |
| titulaire_distance | 80.49% |
| acheteur_labels | 79.56% |
| acheteur_categorie | 79.03% |
| ccag | 49.70% |
| typeGroupementOperateurs | 49.61% |
| considerationsSociales | 48.66% |
| considerationsEnvironnementales | 48.66% |
| modalitesExecution | 48.23% |
| techniques | 48.23% |
| typesPrix | 44.13% |
| marcheInnovant | 32.41% |
| attributionAvance | 32.06% |
| sousTraitanceDeclaree | 30.10% |
| offresRecues | 23.46% |
| tauxAvance | 20.72% |
| origineUE | 15.85% |
| origineFrance | 15.83% |
| titulaire_labels | 10.86% |
| idAccordCadre | 6.32% |
| montant_anomalie_raisons | 1.57% |
| montant_anomalie | 1.57% |
| acheteur_population | 0.00% |

## Répartition par année (dateNotification)

| Année | Nombre de marchés |
|---|---|
| 5 | 2 |
| 22 | 1 |
| 23 | 2 |
| 26 | 1 |
| 205 | 1 |
| 226 | 1 |
| 2005 | 2 |
| 2013 | 1 |
| 2015 | 1 |
| 2016 | 8 |
| 2017 | 74 |
| 2018 | 1 001 |
| 2019 | 6 343 |
| 2020 | 9 155 |
| 2021 | 17 849 |
| 2022 | 18 048 |
| 2023 | 20 050 |
| 2024 | 17 763 |
| 2025 | 18 676 |
| 2026 | 14 498 |
| inconnue | 919 |

> ⚠️ 10 ligne(s) portent une année aberrante (< 2013 : 5, 22, 23, 26, 205, 226…) — erreurs de saisie dans la donnée source (ex. `0026-06-17` au lieu de `2026-06-17`), pas des marchés réellement anciens. Négligeable (~0.008% du segment), non corrigé automatiquement pour éviter de deviner la vraie date.

## Échantillon de 50 objets de marché (texte libre)

1. MN DM SPE 2024-2028 STERLAB (LABO MXM)
2. LOT 2 FOURNITURE DE VACCINS ACWY NIMENRIX
3. Acquisition de consommables de filtration pour le Laboratoire Départemental d’Analyses de la Mayenne (LDA53)
4. Fourniture de kit pour analyse de l’ADN tumoral circulant avec solution de bio informatique intégrée
5. AO BM-Mix Taq polym+ tampon
6. GHT Nièvre : Fourniture de réactifs et consommables pour les laboratoires du Centre de Biologie du Nivernais - Milieux liquides prêts à l’emploi (en tubes)
7. Fourniture lots 66.1/3;90.2/6;91.2;95.1;96.3;103.2;105.1;109.3;110.1;111.5;112.3/4;116.2;117.1;121.2;123.5;124.1/4125.3;135.1/7;135.10;136.1/8;137.1/4;138.1/2;138.4;150.1/2;15.2;20.1/5;201.1/3;202.1/4;204.1/5;205.1/2;206.1/10;207.11;208.1/5;221.1;221.3
8. Fourniture ENDO BLOC lots 28.1/2;54.1/4;170.1/2;251.1-3-7-9/13;252.3;253.1-4/7;254;257.1;258;259;260.7;261;262;263;264;266;267.1/3-5;271.1-3-4-6-8-10;272.1/4;274.1/2;275.1;279.1/9;282.2/3;286.1;288.1/6;291.1/2;292.1/9;293.2-4/5-7-9/10;295.1-3;321.1/3;324.1
9. Fourniture de couches jetables nourrissons pour les structures de la petite enfance: Lot 1 : Fourniture de couches jetables nourrissons pour les structures de la petite enfance
10. Fourniture spécial. pharm GAPLCA lots 74.1,76.4,170.1/2,346.1/3,407.1,679.1,680.1/2,683.1/2,687.1/4,687.1/4,696.1,739.1/2,742.1/3,747.1/2,756.1/2,760.1/6,770.3/4,867.1,867.4,868.4,969.1/2,1019.3,1022.1,1033.1/2,1047.1/3,1059.1,1066.1,1079.2,1103.1,1104.1/3
11. Fourniture de dispositifs médicaux de perfusion, de prélèvement et d’exploration, d’abord urogénital, digestif, nerveux et respiratoire au profit du GAPLCA lots 86.1-3
12. Soins du corps _ Lot 85_25-01DMN
13. FOURNITURES DE DISPOSITIFS MEDICAUX POUR LA NEURORADIOLOGIE INTERVENTIONNELLE POUR LE CHU ROUEN NORMANDIE - Lot 53: Cathéter d’angiographie de diamètre 5 et 6F à tressage renforcé toutes courbures  adaptées pour la neuroradiologie de longueur inférieure ou égale à 130cm.
14. Fourniture de spécialités pharmaceutiques au profit du GAPLCA lots 909.1/2,910.1/5,950.2/3,982.2
15. Fourniture de réactifs et de consommables de laboratoire pour le Centre hospitalier Bretagne Atlantique
16. Fourniture de spécialités pharmaceutiques au profit du GAPLCA lots 597.1,605.2,607.1,611.1
17. Fourniture de spécialités pharmaceutiques au profit du GAPLCA lots 1137.1/7,1140.1/3
18. PANSG PANSEMENT ET MATERIELS DE STERILISATION - 89 LOTS VOIR DETAIL DANS CAHIER DES CHARGES
19. AOO-2020-2158 à 2164 Dispositifs pour ablation de fibrilation atriale - INTRODUCTEUR type SLO
20. Fourniture, installation, mise en services de moniteurs de neuromonitoring, des consommables et prestations de maintenance associées
21. AO MEDICAMENTS ANTINEOPLASIQUES ET IMMUNOMODULATEURS (Classe ATC L)
22. Fourniture de spécialités pharmaceutiques GAPLCA lots 840.2,841.1/6,843.3,852.1/3,854.1,867.2/3,868.1/3,877.4/6,879.5,895.1,900.1,915.4/7,917.1/4,922.2/4,572.1,573.1,922.8/9,928.3,932.1/4,933.1,933.4,937.1/3,941.3,942.2,943.1,944.2/4,960.3,962.1,962.5
23. 23M01 GAULOYS LABORATOIRE XO_ALLOGA
24. Fourniture lots 66.1/3;90.2/6;91.2;95.1;96.3;103.2;105.1;109.3;110.1;111.5;112.3/4;116.2;117.1;121.2;123.5;124.1/4125.3;135.1/7;135.10;136.1/8;137.1/4;138.1/2;138.4;150.1/2;15.2;20.1/5;201.1/3;202.1/4;204.1/5;205.1/2;206.1/10;207.11;208.1/5;221.1;221.3
25. Maintenance et fourniture des pièces détachées, accessoires et consommables des équipements exclusivement entretenus par la société CRYO BIO SYSTEMS
26. Acquisition de matériels de réanimation cardiaque et de ventilation médicale avec exécution de prestations associées - Massage cardiaque automatisé pour pompiers
27. Fourniture de produits de santé du système nerveux - GAC-2023-048_2024-SNMS1_SAD M_2630- MEDIC2021
28. MEDICAMENTS ET PRODUITS PHARMACEUTIQUES - SECTEUR EST HERAULT
29. MN SIEMENS REACTIFS MAINTENANCE
30. Fourniture de consommables pour filtration, pour anatomie-cytopathologie, pour graveur de cassettes, pour sytème d’impression et filmeuse de lames
31. Pousse TIVA
32. Fourniture de prothèses chirurgicales et dispositifs médicaux  2022chro0014 - DISPOSITIF DE REINSERTION MENISCALE - Marché n° 232-047
33. DMNS 2023-010 _ Lot_75
34. AGUETTANT GAO29 2023/SLM
35. Fourniture de médicaments 2023 - 2024 - L04AC03 ANAKINRA
36. La présente consultation porte sur la conclusion d’un accord-cadre ayant pour objet l’acquisition et la location d’équipements lourds de bloc opératoire et l’exécution de prestations associées. La description technique des équipements et prestations est d
37. Fourniture de dispositifs médicaux relatifs aux pansements, compresses hémostatiques stériles et couvertures à usage opérationnel - couverture chaufferette type ready-heat II ou équivalent
38. FOURNITURE DE DISPOSITIFS MEDICAUX NON IMPLANTABLES STERILES (Digestif, Urologie/Gynécologie, Chirurgie, Respiratoire, ORL, Stomatologie, Dialyse, Cardiovasculaire, Perfusion, Biopsie et Consommables d’équipement) Lot 24 DM non implantables Système Digestif et métabolique GAMIDA ou équivalent
39. Fourniture de prothèses cervicales à noyau fixe pour le CHRU de Tours
40. FOURNITURE DE PRODUITS D?INCONTINENCE, AUTRES CONSOMMABLES ET SERVICES ASSOCIES LOT 6 CARRES ET GANTS
41. RH MSP16 DELBERT 22-25
42. Identification des anticorps anti-HLA sur bille à antigène HLA unique (single antigen) avec mise à disposition d un automate de technologie LUMINEX
43. Fourniture de dispositifs médicaux endoscopie digestive, équipements de protection individuelle, drapage opératoire, désinfection - stérilisation et d’instrumentation chirurgicale lots 70.1/5;72.1/5;73.1/5;76.1/8;77.1/3;82.1/3;223.7;239.1;386.1
44. AO DISPOSITIFS MEDICAUX  2024/2028
45. Fourniture de dispositifs médicaux non implantables de Dialyse, Cathétérisme central et périphérique (MIDLINE), Système cardiovasculaire, Kits de surveillance de pression, Consommables haute pression pour injecteur, Système nerveux et Ophtalmologie - Lots 101 à 177 - Lot 137: Solution oculaire tamponnée électrolytes, stérile flacon en verre
46. Fourniture spécial. pharm GAPLCA lots 74.1,76.4,170.1/2,346.1/3,407.1,679.1,680.1/2,683.1/2,687.1/4,687.1/4,696.1,739.1/2,742.1/3,747.1/2,756.1/2,760.1/6,770.3/4,867.1,867.4,868.4,969.1/2,1019.3,1022.1,1033.1/2,1047.1/3,1059.1,1066.1,1079.2,1103.1,1104.1/3
47. Fourniture de médicaments un an 2022 - J05AG01 NEVIRAPIN
48. Fourniture de dispositifs médicaux de perfusion, de prélèvement et d’exploration, d’abord urogénital, digestif, nerveux et respiratoire lots 1.1;8.1/4;9.1/2;10.1/11;11.1/7;19.1/6-17;66.1/7;67.1;139.1;140.1;193.1/2;203.1/4;218.4/5
49. Fourniture spécial. pharm GAPLCA lots 74.1,76.4,170.1/2,346.1/3,407.1,679.1,680.1/2,683.1/2,687.1/4,687.1/4,696.1,739.1/2,742.1/3,747.1/2,756.1/2,760.1/6,770.3/4,867.1,867.4,868.4,969.1/2,1019.3,1022.1,1033.1/2,1047.1/3,1059.1,1066.1,1079.2,1103.1,1104.1/3
50. Fourniture de dispositifs médicaux ENDO BLOC lots 99.1/2;100.1;101.1;243.1/4;401.1;401.3;403.1;404.1/2;405.1/2;406.1/3;407.1/2;408.1/3;410.1/412.1/3;413.1;414.1/4;415.1/2;416.1;416.3;418.1;419.1;420.1;424.1;427.1
