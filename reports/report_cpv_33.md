# Rapport DECP — segment CPV `33`

- Fichier source : `data/decp_consolide.parquet`
> ℹ️ Le fichier consolidé contient une ligne par version successive de chaque marché (historique de modifications) ; ~43,75% des lignes brutes du fichier complet sont des doublons de version. Les chiffres ci-dessous sont dédupliqués : un marché (`uid`) = une ligne, la plus récente (`modification_id` maximum). Voir `scripts/decp_utils.py`.

- Marchés distincts, tous CPV confondus : 1 844 381
- Marchés filtrés (CPV commence par `33`) : 75 784 (4.11% du total)

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
| objet | 99.97% |
| dureeMois | 99.89% |
| dateNotification | 99.82% |
| donneesActuelles | 99.82% |
| modification_id | 99.82% |
| dureeRestanteMois | 99.71% |
| lieuExecution_typeCode | 99.69% |
| lieuExecution_code | 99.69% |
| datePublicationDonnees | 99.19% |
| acheteur_nom | 98.76% |
| acheteur_commune_code | 98.76% |
| acheteur_departement_code | 98.75% |
| acheteur_commune_nom | 98.75% |
| acheteur_departement_nom | 98.75% |
| acheteur_region_nom | 98.75% |
| acheteur_region_code | 98.75% |
| nature | 98.23% |
| titulaire_typeIdentifiant | 97.51% |
| titulaire_id | 97.25% |
| montant | 96.58% |
| montant_rationalise | 96.58% |
| formePrix | 94.77% |
| titulaire_nom | 94.18% |
| titulaire_activite_code | 94.18% |
| titulaire_activite_libelle | 94.02% |
| titulaire_commune_nom | 93.30% |
| titulaire_commune_code | 93.30% |
| titulaire_region_code | 93.30% |
| titulaire_region_nom | 93.30% |
| titulaire_departement_nom | 93.30% |
| titulaire_departement_code | 93.30% |
| acheteur_longitude | 92.78% |
| acheteur_latitude | 92.78% |
| titulaire_categorie | 92.76% |
| procedure | 91.96% |
| titulaire_latitude | 86.66% |
| titulaire_longitude | 86.66% |
| acheteur_labels | 82.90% |
| titulaire_distance | 80.21% |
| acheteur_categorie | 78.43% |
| ccag | 51.93% |
| typeGroupementOperateurs | 51.79% |
| considerationsSociales | 50.22% |
| considerationsEnvironnementales | 50.22% |
| modalitesExecution | 49.56% |
| techniques | 49.56% |
| typesPrix | 42.89% |
| marcheInnovant | 40.61% |
| attributionAvance | 40.26% |
| sousTraitanceDeclaree | 38.65% |
| offresRecues | 34.48% |
| tauxAvance | 30.61% |
| origineUE | 23.74% |
| origineFrance | 23.71% |
| titulaire_labels | 10.99% |
| idAccordCadre | 7.96% |
| montant_anomalie_raisons | 1.55% |
| montant_anomalie | 1.55% |
| acheteur_population | 0.00% |

## Répartition par année (dateNotification)

| Année | Nombre de marchés |
|---|---|
| 22 | 1 |
| 23 | 2 |
| 26 | 1 |
| 226 | 1 |
| 2005 | 1 |
| 2013 | 1 |
| 2015 | 1 |
| 2016 | 6 |
| 2017 | 72 |
| 2018 | 978 |
| 2019 | 5 829 |
| 2020 | 7 327 |
| 2021 | 8 666 |
| 2022 | 8 497 |
| 2023 | 11 892 |
| 2024 | 10 690 |
| 2025 | 11 477 |
| 2026 | 10 209 |
| inconnue | 133 |

> ⚠️ 6 ligne(s) portent une année aberrante (< 2013 : 5, 22, 23, 26, 205, 226…) — erreurs de saisie dans la donnée source (ex. `0026-06-17` au lieu de `2026-06-17`), pas des marchés réellement anciens. Négligeable (~0.008% du segment), non corrigé automatiquement pour éviter de deviner la vraie date.

## Échantillon de 50 objets de marché (texte libre)

1. AOMED1 / V03AF04 - LEVOFOLINATE DE CALCIUM
2. SPECIALITES EN ACCES PRECOCE FOURNIES PAR RHYTHM PHARMACEUTICALS
3. PharmacoTox- Médicaments Toxiques- Biochimie UPLC et CQI spécifiques - Kit de dosage HPLC Catecholamines urinaires
4. Fourniture de dispositifs médicaux stériles et non stériles : d’abord digestif, genito-urinaire, respiratoire et ORL » pour les établissements adhérant au GCS Achats du Centre
5. Fourniture de produits de nutrition entérale adulte et pédiatrique, CNO, de DADFMS pour la prise en charge des MMH et de laits spécifiques au profit des établissements membres du GCS GRAPS Grand Est - lot 01: Mélange polymérique - Produit adulte normocalorique normoprotidique
6. AO23DMS_Lot 512
7. Matériels d’endoscopie médicale avec exécution des prestations associées et prestations de gestion de parc  - Endomicroscopie
8. Fourniture de produits de nutrition entérale par sonde, adulte et pédiatrique et de produits diététiques pour le compte du gpt de commandes coordonné par le CH de Verdun/St-Mihiel: Lot 6: Boisson lactée HP HC enrichie en AA
9. Médicament sous Autorisation d’Accès Compassionnel (AAC) et Autorisation d’Accès Précoce Pré-AMM (AP1) 2025
10. DMS Orthopédie et traumatologie lot 49
11. LOT 2201113 - DISPOSITIF DE FIXATION 18G POUR CATHÉTER PÉRIDURAL - GHT 11 - Fourniture de dispositifs médicaux, médico-techniques non stériles et produits non tissés
12. Fourniture de dispositifs médicaux de soins dentaires AO-2025-006
13. DISPOSITIF DE FERMETURE VASCULAIRE BIORESORBABLE
14. DISPOSITIFS MEDICAUX DE REHABILITATION APRES LARYNGECTOMIE TOTALE
15. GHT - Fourniture de dispositifs médicaux implantables - AO Cardio - ICA22<br />Familles Vasculaire, Cardiologie Interventionnelle, Chirurgie Cardiaque, Embolisation, Rythmologie
16. Fourniture de médicaments radiopharmaceutiques diagnostiques TEP pour l’Oncopole Claudius Regaud: Lot 3 : 18F - DOPA
17. DMS 2024-02 AO 092 fourniture de Dispositifs Médicaux Stériles à usage unique  *Casaque, drapage opératoire, compresse, instrument, cupule, tampon, set, pansement tous types, thérapie par pression négative, brosse chirurgicale, immobilisation, contention / compression, maintien. *Dialyse, aphérèse, immunophérèse *Biberon, lacs suspenseurs, dispositifs médicaux non implantables : médecine, chirurgie, électrophysiologie, radiologie, angioplastie, coronarographie. *Dispositifs médicaux implantables toutes spécialités  - IMPLANT POLYPROPYLENE
18. BRENTUXIMAB VEDOTINE FORME INJECTABLE
19. Fourniture de produits d’hygiène pour le groupement de commande de Sète agglôpole méditerranée
20. TLS01-2026 - M_3339 - AMOXICILLINE + ACIDE CLAVULANIQUE INJECTABLE
21. DISPOSITIFS MEDICAUX STERILES : ANESTHESIE ET REANIMATION - Cathéter veineux central insertion périphérique Picc 4F 60CM, 5F 60CM
22. AGP835-Lot 133
23. Fourniture de dispositifs médicaux de cardiologie interventionnelle - Relance 1
24. FOURNITURE DE SPECIALITES PHARMACEUTIQUES DES CLASSES ATC : A-B-C-D-G-M-N-P-R-V pour le CH du Mans, le CH de la Ferté Bernard, le PSSL, le CH de St Calais, le CH de Château du Loir, le CH du Lude, le CH de Bonnétable, le CH de Beaumont sur Sarthe, le CH d
25. Accord-Cadre multi-attributaires à marchés subséquents relatif à la fourniture de produits pharmaceutiques (médicaments et dispositifs médicaux) par grossiste répartiteur - centre hospitalier spécialisé Auxerre
26. 210288-Lot 2 : Bandelette non résorbable de soutènement sous urétral par voie transobturatrice
27. Acquisition de chariots brancards pour ambulances et d’équipements associés, d’accessoires, de consommables, de pièces détachées pour les membres du GCS UniHA - Chaise portoir mécanique
28. Implants d’ophtalmologie à usage unique pour le CH Argentan, le CH Aunay-Bayeux, le CH Falaise, le CH Lisieux et le CHU de Caen - IMPLANT CATARACTE TORIQUE
29. DIAGNOSTIC AMONT ET PLAN D ACTION POUR LA REDUCTION DES MICROPOLLUANTS SUR 3M
30. Fourniture de dispositifs médicaux non stériles et autres consommables non stériles - Circuits pour respirateurs et accessoire associés
31. BRIVARACETAM
32. Fournitures et livraison de spécialités pharmaceutiques pour le GHT du Limousin - ARTICAINE ET ADRENALINE
33. Lot 41 : SYSTEME DE DRAINAGE THORACIQUE POUR PNEUMOLOGIE - GAPSCA - Fourniture de dispositifs médicaux d’aspiration et drainage (2025/2028)
34. Le marché porte sur l’achat d’un automate permettant de multiplexer les anticorps et ainsi mettre en évidence plusieurs protéines d’intérêt sur la même coupe de tissu. Cet achat s’inscrit dans le cadre du projet IHU EVEREST, premier et seul IHU sur le site lyonnais, spécialisé dans les maladies chroniques du foie.
35. FOURNITURE DE REACTIFS DE BACTERIOLOGIE - Lot 14 : Gélose chromogène pour Carbapénémase (type OXA 48) et détection combinée
36. Dispositifs médicaux stériles non implantables :  -	Anesthésie réanimation ; chirurgie ; circulation extracorporelle ; cardiologie ; médecine ; endoscopie ; gynécologie – obstétrique ; prélèvement biopsie -	Autotransfusion         -	Dispositif diagnost
37. Fourniture de dispositifs médicaux - Abord Respiratoire RES22 au profit des adhérents du GCS UniHa M_2620 - NÉBULISEUR AVEC MASQUE ET TUBULURE POUR PATIENT ADULTE TRACHÉOTOMISÉ
38. 21DMS- AUBIN - GROUPEMENT GAULOYS
39. PA MED NEOMERCAZOLE
40. Fourniture de dispositifs médicaux pour valves  cardiaques, prothèses vasculaires et système d’assistance ventriculaire (18 lots)
41. YM811-Lot 271
42. Ght_MED_2025-019_AC_Fourniture De Médicaments [2025-2027] - racecadotril forme orale indication pédiatrique
43. FOURNITURE DE DISPOSITIFS MEDICAUX
44. FOURNITURE DE DISPOSITIFS MEDICAUX
45. FOURNITURE DE MEDICAMENTS ANTI-INFECTIEUX
46. FOURNITURE DE DISPOSITIFS MEDICAUX STERILES DE CHIRURGIE 2024 LOT 141
47. PROTHESE FIXE  ASSISTEE OU NON PAR CFAO
48. Fourniture d’un système de lecture et d’interprétation des PLA2RI et THSD7A : Matériels, réactifs, consommables et maintenance pour le laboratoire d’immunologie du CHU de Nice
49. 2025-0589 FOURNITURE DE DISPOSITIFS MEDICAUX IMPLANTABLES : CARDIOLOGIE - MN SPICA25 (2025-2028)
50. MASQUES CHIRURGICAUX
