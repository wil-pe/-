# Résultats du modèle de comparaison (agent K) — sorties de modèle, pas des mesures

Base : **kg de protéine comestible** (N × facteur). Scénarios notés *prudent / intermédiaire / optimiste*. Aucune correction d'inflation ; USD au change BCE de l'année de la donnée. Nature des intrants indiquée ligne par ligne (statistical, published_estimate, model_output, company_claim, model_assumption…).

## 0. Tableau final — par kg de protéine comestible (plages toutes sources et scénarios confondus)

| Ligne | Coût (USD de l'année de la donnée) | GES (kg CO2-eq) | Énergie (MJ) | Eau bleue (L) | Surface (m2·an) |
|---|---|---|---|---|---|
| A standard (porte d'abattoir) | 7.6–19.0 | 11.1–44.0 | 94–137 | 200–1654 | 20.0–46.9 |
| A standard (produit au détail, toutes étapes) | n.d. | 17.5–57.0 | 168–306 | n.d. | 18.7–71.0 |
| A certifié (ECC / Beter Leven) | 19.1–25.5 | 18.8–55.4 | n.d. | 2740 | 46.4–65.7 |
| A Label Rouge | 40.9–46.5 | 30.1–39.0 | 234–303 | 2740 | n.d. |
| A biologique / pâturage | 53.9–67.9 | 38.1–73.3 | 305–396 | 5780 | n.d. |
| B, base publiée (21 % ; 18-25 % pour les ACV) | 9–287 | 10.0–79.4 (intrants purifiés : 984–8378) | 588–1467 | 168–311 | 6.8–10.0 |
| B, recalcul à 9 % de protéines (caille mesurée) | 22–670 | 28–159 (intrants purifiés : 2733–16756) | 1633–2933 | 467–622 | 18.9–20.0 |
| C ingrédients (soja, pois, tofu, mycoprotéine, SCP ; porte d'usine ou détail selon la source) | 1.9–29.6 | 0.8–20.8 | 98–370 | 246 | 8.7–34.0 (SCP photovoltaïque modélisée : < 0.83) |
| C produits (analogues végétaux AGRIBALYSE, toutes étapes) | n.d. | 7.7–11.4 | 284–344 | n.d. | n.d. |

Nature des chiffres par ligne :

- **A standard (porte d'abattoir)** — coût : published_estimate + statistical (UE moyenne 2017, standard; UE six pays 2021, standard; France 2022, standard (ITAVI); États-Unis 2023, standard (grande échelle, hors abattage); Brésil (Paraná) 2025, standard (hors abattage)) ; GES : model_output ; énergie : company_claim + model_output ; eau : model_assumption + model_output + published_estimate ; surface : model_output + published_estimate.
- **A standard (produit au détail, toutes étapes)** — coût : — (—) ; GES : measured + model_assumption + model_output + statistical ; énergie : measured + model_output ; eau : — ; surface : measured + model_output + statistical.
- **A certifié (ECC / Beter Leven)** — coût : published_estimate (Pays-Bas 2021, certifié ECC; France 2021, certifié ECC) ; GES : model_output ; énergie : — ; eau : model_assumption + model_output + published_estimate ; surface : model_output.
- **A Label Rouge** — coût : model_assumption + statistical (France 2022, Label Rouge (ITAVI)) ; GES : model_output ; énergie : company_claim + model_output ; eau : model_assumption + model_output + published_estimate ; surface : —.
- **A biologique / pâturage** — coût : model_assumption + published_estimate + statistical (États-Unis 2023, pâturage (hors abattage); France 2022, biologique (ITAVI)) ; GES : model_output ; énergie : company_claim + model_output ; eau : model_assumption + model_output + published_estimate ; surface : —.
- **B, base publiée (21 % ; 18-25 % pour les ACV)** — coût : model_output (+ model_assumption) (Humbird 2021, fed-batch (masse humide); Humbird 2021, perfusion; Humbird 2021, fed-batch + hydrolysat 2 $/kg; CE Delft 2021, 2030 tous leviers (produit CM); Risner 2021, limites levées (scénario 4); Pasitka 2024, résumé (6,2 $/lb, base non vérifiée); Pasitka 2024 selon la revue Bry-Chevalier; Modèle E/X, scénario optimiste (biomasse humide); Modèle E/X, scénario intermédiaire; Modèle E/X, scénario prudent) ; GES : model_output + model_assumption ; énergie : model_output + model_assumption ; eau : model_output + model_assumption ; surface : model_output + model_assumption.
- **B, recalcul à 9 % de protéines (caille mesurée)** — coût : model_output (+ model_assumption) (Humbird 2021, fed-batch (masse humide); Humbird 2021, perfusion; Humbird 2021, fed-batch + hydrolysat 2 $/kg; CE Delft 2021, 2030 tous leviers (produit CM); Risner 2021, limites levées (scénario 4); Pasitka 2024, résumé (6,2 $/lb, base non vérifiée); Pasitka 2024 selon la revue Bry-Chevalier; Modèle E/X, scénario optimiste (biomasse humide); Modèle E/X, scénario intermédiaire; Modèle E/X, scénario prudent) ; GES : model_output + model_assumption ; énergie : model_output + model_assumption ; eau : model_output + model_assumption ; surface : model_output + model_assumption.
- **C ingrédients (soja, pois, tofu, mycoprotéine, SCP ; porte d'usine ou détail selon la source)** — coût : measured_reported_by_review + model_output (Isolat de soja, prix de marché 2019-2023; e-SCP (bactéries H2), sites les moins chers 2028; Mycoprotéine, TEA (Risner 2023)) ; GES : company_claim + model_output + published_estimate + statistical ; énergie : company_claim + model_output + published_estimate ; eau : model_output + published_estimate ; surface : model_output + published_estimate.
- **C produits (analogues végétaux AGRIBALYSE, toutes étapes)** — coût : — (aucun coût de produit trouvé) ; GES : model_assumption + model_output ; énergie : model_assumption + model_output ; eau : — ; surface : —.

Avertissements : (1) les indicateurs d'énergie ne sont pas homogènes (A : MJ non renouvelables EF ou énergie primaire ; B : demande d'énergie CE Delft ; C : CED ou électricité) ; (2) l'eau bleue de la voie A selon Mekonnen & Hoekstra (1 654-5 780 L) et selon CE Delft (200 L) diffère d'un facteur 8 à 30 à cause des périmètres et de l'irrigation supposée ; (3) les coûts mélangent des années 2017-2025 sans inflation ; (4) les coûts de B sont des sorties de TEA, ceux de A des estimations publiées ou statistiques ; (5) les plages ne sont pas des intervalles de confiance.

## 1. Facteurs de conversion de la voie A

| Facteur | Prudent | Intermédiaire | Optimiste | Réf. |
|---|---|---|---|---|
| Protéine de la viande désossée crue (kg/kg) | 0.206 | 0.214 | 0.232 | Q-K-0049 ; Q-K-0046 ; Q-K-0123 |
| Viande désossée / poids vif — standard | 0.414 | 0.431 | 0.470 | Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| Viande désossée / poids vif — certifie | 0.319 | 0.325 | 0.353 | Q-K-0066 ; Q-K-0077 + Q-K-0122 (hypothèse) |
| Viande désossée / poids vif — label_rouge_bio | 0.302 | 0.306 | 0.306 | Q-K-0076 + Q-K-0122 (hypothèse) |
| Allocation des impacts à la viande | 1.0 | 0.88 | 0.88 | Q-K-0124 ; Q-K-0006 |
| Rapport protéine acides aminés / N×facteur (filet) | 0.824 | | | Q-K-0053 / Q-K-0052 |

Protéine comestible par kg de poids vif (rendement × protéine) :

- standard : 0.085 / 0.092 / 0.109 kg/kg PV
- certifie : 0.066 / 0.070 / 0.082 kg/kg PV
- label_rouge_bio : 0.062 / 0.065 / 0.071 kg/kg PV

## 2. Voie A — coût par kg de protéine comestible (100 % des coûts imputés à la viande désossée)

| Cas | Monnaie | Coût par kg PV (ferme + abattage) | Coût / kg protéine (monnaie d'origine) | idem en USD de l'année | Nature des intrants | Réf. |
|---|---|---|---|---|---|---|
| UE moyenne 2017, standard | EUR2017 | 1.091 / 1.032 / 0.972 | 12.79 / 11.18 / 8.91 | 14.45 / 12.63 / 10.07 | published_estimate | Q-E-0022 ; Q-K-0110 ; Q-E-0049 ; rendement Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| UE six pays 2021, standard | EUR2021 | 1.247 / 1.171 / 1.094 | 14.62 / 12.69 / 10.03 | 17.29 / 15.01 / 11.87 | published_estimate | Q-K-0059 ; Q-K-0060 ; Q-K-0061 ; rendement Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| France 2022, standard (ITAVI) | EUR2022 | 1.541 / 1.541 / 1.541 | 18.07 / 16.71 / 14.14 | 19.03 / 17.6 / 14.89 | published_estimate + statistical | Q-E-0029 ; Q-K-0112 (abattage 2021) ; Q-K-0061 ; rendement Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| États-Unis 2023, standard (grande échelle, hors abattage) | USD2023 | 1.146 / 1.146 / 1.146 | 13.43 / 12.42 / 10.51 | 13.43 / 12.42 / 10.51 | published_estimate | Q-K-0080 ; rendement Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| Brésil (Paraná) 2025, standard (hors abattage) | BRL2025 | 4.6 / 4.6 / 4.6 | 53.94 / 49.87 / 42.19 | 9.66 / 8.94 / 7.56 | statistical | Q-E-0032 ; rendement Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| Pays-Bas 2021, certifié ECC | EUR2021 | 1.418 / 1.371 / 1.325 | 21.57 / 19.71 / 16.17 | 25.51 / 23.32 / 19.13 | published_estimate | Q-K-0056 ; Q-K-0111 ; Q-K-0114 ; rendement Q-K-0066 ; Q-K-0077 + Q-K-0122 (hypothèse) |
| France 2021, certifié ECC | EUR2021 | 1.362 / 1.362 / 1.362 | 20.73 / 19.59 / 16.63 | 24.52 / 23.17 / 19.67 | published_estimate | Q-K-0058 ; Q-K-0113 ; Q-K-0114 ; rendement Q-K-0066 ; Q-K-0077 + Q-K-0122 (hypothèse) |
| États-Unis 2023, pâturage (hors abattage) | USD2023 | 4.224 / 4.224 / 4.224 | 67.9 / 64.5 / 59.5 | 67.9 / 64.5 / 59.5 | published_estimate | Q-K-0082 ; rendement Q-K-0076 + Q-K-0122 (hypothèse) |
| France 2022, Label Rouge (ITAVI) | EUR2022 | 2.75 / 2.753 / 2.755 | 44.2 / 42.04 / 38.81 | 46.55 / 44.26 / 40.87 | model_assumption + statistical | Q-E-0030 ; Q-K-0128 (hyp.) ; Q-K-0121 ; rendement Q-K-0076 + Q-K-0122 (hypothèse) |
| France 2022, biologique (ITAVI) | EUR2022 | 3.631 / 3.634 / 3.636 | 58.36 / 55.49 / 51.22 | 61.46 / 58.43 / 53.94 | model_assumption + statistical | Q-E-0031 ; Q-K-0128 (hyp.) ; Q-K-0121 ; rendement Q-K-0076 + Q-K-0122 (hypothèse) |

## 3. Voie A — environnement par kg de protéine comestible

| Indicateur | Cas | Système | Périmètre | Prudent / Intermédiaire / Optimiste | Unité | Nature | Réf. | Remarque |
|---|---|---|---|---|---|---|---|---|
| GES | France standard, AGRIBALYSE sortie ferme + abattoir | standard | porte | 22.9 / 18.6 / 15.8 | kg CO2-eq/kg protéine | model_output | Q-K-0027 ; Q-K-0115 |  |
| GES | Pays-Bas standard avec LUC (WUR 1397) | standard | porte | 44.0 / 35.8 / 30.3 | kg CO2-eq/kg protéine | model_output | Q-K-0069 |  |
| GES | Pays-Bas standard sans LUC (WUR 1397) | standard | porte | 16.2 / 13.2 / 11.1 | kg CO2-eq/kg protéine | model_output | Q-K-0070 |  |
| GES | Pays-Bas Beter Leven 1 étoile avec LUC (WUR 1397) | certifie | porte | 55.4 / 46.1 / 39.1 | kg CO2-eq/kg protéine | model_output | Q-K-0071 |  |
| GES | Pays-Bas Beter Leven 1 étoile sans LUC (WUR 1397) | certifie | porte | 26.6 / 22.1 / 18.8 | kg CO2-eq/kg protéine | model_output | Q-K-0071 |  |
| GES | France Label Rouge, AGRIBALYSE + abattoir | label_rouge_bio | porte | 39.0 / 32.6 / 30.1 | kg CO2-eq/kg protéine | model_output | Q-K-0031 ; Q-K-0115 |  |
| GES | France biologique, AGRIBALYSE (moyenne → systèmes 1-2) + abattoir | label_rouge_bio | porte | 73.3 / 51.3 / 38.1 | kg CO2-eq/kg protéine | model_output | Q-K-0035 ; Q-K-0039 ; Q-K-0115 |  |
| GES | Monde, FAO GLEAM 2013 (berceau-détail) | standard | détail | 44.4 / 37.6 / 34.7 | kg CO2-eq/kg protéine | model_assumption + model_output | Q-K-0001 ; Q-K-0005 ; protéine Q-K-0049 ; Q-K-0046 ; Q-K-0123 | conversion carcasse → viande de la FAO elle-même |
| GES | Royaume-Uni, FAO GLEAM (déjà par kg de protéine) | standard | détail | 43.5 / 43.5 / 43.5 | kg CO2-eq/kg protéine | model_output | Q-K-0004 | PAS 2050 : 32,9 (notes) |
| GES | Monde, Poore & Nemecek (moyenne, par kg de protéine) | standard | détail | 57.0 / 57.0 / 57.0 | kg CO2-eq/kg protéine | model_output | Q-K-0102 | base protéine des auteurs (volaille, produit de détail) |
| GES | France, viande de poulet crue, AGRIBALYSE toutes étapes (produit) | standard | détail | 19.2 / 19.2 / 19.2 | kg CO2-eq/kg protéine | measured + model_output | Q-K-0045 ; Q-K-0046 | même base que les analogues végétaux AGRIBALYSE (voie C) |
| GES | France, filet de poulet cru, AGRIBALYSE toutes étapes (produit) | standard | détail | 24.0 / 24.0 / 24.0 | kg CO2-eq/kg protéine | measured + model_output | Q-K-0040 ; Q-K-0047 |  |
| Énergie | France, filet de poulet cru, AGRIBALYSE toutes étapes (MJ non renouvelables) | standard | détail | 305.8 / 305.8 / 305.8 | MJ/kg protéine | measured + model_output | Q-K-0041 ; Q-K-0047 | transformation = 47 % ; comparable à l'escalope végétale (voie C) |
| GES | Allemagne, Hähnchen (moyenne), ifeu (produit) | standard | détail | 25.7 / 25.7 / 25.7 | kg CO2-eq/kg protéine | measured + model_output | Q-K-0091 ; Q-K-0046 | base produit non précisée (os éventuels) : protéine 21,4 % supposée |
| Énergie | Allemagne, Hähnchen (moyenne), ifeu (énergie primaire) | standard | détail | 168.2 / 168.2 / 168.2 | MJ/kg protéine | measured + model_output | Q-K-0093 ; Q-K-0046 | base produit non précisée |
| Surface | Allemagne, Hähnchen (moyenne), ifeu | standard | détail | 18.7 / 18.7 / 18.7 | m2·an/kg protéine | measured + model_output | Q-K-0092 ; Q-K-0046 | base produit non précisée |
| GES | Pays-Bas, filet de poulet au supermarché, RIVM 2024 (agent S) | standard | détail | 17.5 / 17.5 / 17.5 | kg CO2-eq/kg protéine | measured + statistical | Q-S-0085 ; Q-K-0047 | allocation économique |
| Surface | Pays-Bas, filet de poulet, RIVM 2024 (agent S) | standard | détail | 24.4 / 24.4 / 24.4 | m2·an/kg protéine | measured + statistical | Q-S-0089 ; Q-K-0047 |  |
| Énergie | France standard, AGRIBALYSE (MJ non renouvelables) + électricité d'abattoir | standard | porte | 137.0 / 111.5 / 94.3 | MJ/kg protéine | company_claim + model_output | Q-K-0028 ; Q-K-0074 |  |
| Énergie | France Label Rouge, AGRIBALYSE (MJ non renouvelables) + électricité d'abattoir | label_rouge_bio | porte | 302.9 / 253.2 / 233.6 | MJ/kg protéine | company_claim + model_output | Q-K-0032 ; Q-K-0074 |  |
| Énergie | France biologique, AGRIBALYSE (MJ non renouvelables) + électricité d'abattoir | label_rouge_bio | porte | 395.5 / 330.6 / 305.0 | MJ/kg protéine | company_claim + model_output | Q-K-0036 ; Q-K-0074 |  |
| Eau bleue | Monde, standard ↔ classe industrielle (Mekonnen & Hoekstra) | standard | porte | 1654 / 1654 / 1654 | L/kg protéine | model_assumption + model_output + published_estimate | Q-K-0012 ; Q-K-0010 ; Q-K-0127 (hyp.) | base protéine de la source (127 g/kg), indépendante du rendement désossé |
| Eau bleue | Monde, certifié et Label Rouge ↔ classe mixte (Mekonnen & Hoekstra) | certifie | porte | 2740 / 2740 / 2740 | L/kg protéine | model_assumption + model_output + published_estimate | Q-K-0120 ; Q-K-0010 ; Q-K-0127 (hyp.) | base protéine de la source (127 g/kg), indépendante du rendement désossé |
| Eau bleue | Monde, biologique ↔ classe pâturage (Mekonnen & Hoekstra) | label_rouge_bio | porte | 5780 / 5780 / 5780 | L/kg protéine | model_assumption + model_output + published_estimate | Q-K-0013 ; Q-K-0010 ; Q-K-0127 (hyp.) | base protéine de la source (127 g/kg), indépendante du rendement désossé |
| Eau bleue | Référence ambitieuse 2030 (CE Delft) | standard | porte | 200 / 200 / 200 | L/kg protéine | model_output + published_estimate | Q-K-0018 ; Q-K-0024 | même méthode que la voie B (CE Delft) |
| Eau (rareté) | France standard, AGRIBALYSE (m3 privés AWARE) | standard | porte | 8.4 / 6.9 / 5.8 | m3 éq. privés/kg protéine | model_output | Q-K-0030 | indicateur pondéré par la rareté, pas un volume |
| Eau (rareté) | France Label Rouge, AGRIBALYSE (m3 privés AWARE) | label_rouge_bio | porte | 21.0 / 17.6 / 16.2 | m3 éq. privés/kg protéine | model_output | Q-K-0034 | indicateur pondéré par la rareté, pas un volume |
| Eau (rareté) | France biologique, AGRIBALYSE (m3 privés AWARE) | label_rouge_bio | porte | 53.0 / 44.3 / 40.9 | m3 éq. privés/kg protéine | model_output | Q-K-0038 | indicateur pondéré par la rareté, pas un volume |
| Surface | Pays-Bas standard (WUR 1397) | standard | porte | 42.1 / 34.3 / 29.0 | m2·an/kg protéine | model_output | Q-K-0072 |  |
| Surface | Pays-Bas Beter Leven 1 étoile (WUR 1397) | certifie | porte | 65.7 / 54.7 / 46.4 | m2·an/kg protéine | model_output | Q-K-0073 |  |
| Surface | Brésil 2020, maïs + soja sans allocation (calcul K, Embrapa) | standard | porte | 46.9 / 38.2 / 32.3 | m2·an/kg protéine | model_output | Q-K-0100 | surestimé : surface du soja non partagée avec l'huile |
| Surface | Monde, Poore & Nemecek (moyenne) | standard | détail | 71.0 / 71.0 / 71.0 | m2·an/kg protéine | model_output | Q-K-0103 |  |
| Surface | Référence ambitieuse 2030 (CE Delft) | standard | porte | 20.0 / 20.0 / 20.0 | m2·an/kg protéine | model_output + published_estimate | Q-K-0016 ; Q-K-0024 | même méthode que la voie B (CE Delft) |

Utilisation du sol AGRIBALYSE (points, non convertibles en m2) : rapport Label Rouge/conventionnel = 1.3, bio/conventionnel = 2.57 (Q-K-0029, Q-K-0033, Q-K-0037).

## 4. Voie B — coût par kg de protéine (scénarios publiés ; USD de l'étude, ≈ 2018-2024)

| Scénario | Coût publié $/kg (biomasse humide ou produit) | $/kg protéine à 21 % | à 9 % | à 8,8 % | Nature | Réf. |
|---|---|---|---|---|---|---|
| Humbird 2021, fed-batch (masse humide) | 37.0 | 176.2 | 411.1 | 420.5 | model_output | Q-E-0001 |
| Humbird 2021, perfusion | 51.0 | 242.9 | 566.7 | 579.5 | model_output | Q-E-0002 |
| Humbird 2021, fed-batch + hydrolysat 2 $/kg | 22.0 | 104.8 | 244.4 | 250.0 | model_output | Q-E-0006 |
| CE Delft 2021, 2030 tous leviers (produit CM) | 6.43 | 30.6 | 71.4 | 73.1 | model_output | Q-E-0034 |
| CE Delft 2021, scénario actuel le plus coûteux | 22421.0 | 106766.7 | 249122.2 | 254784.1 | model_output | Q-E-0033 |
| Risner 2021, limites levées (scénario 4) | 1.95 | 9.3 | 21.7 | 22.2 | model_output | Q-E-0011 |
| Risner 2021, référence 2019 | 437000.0 | 2080952.4 | 4855555.6 | 4965909.1 | model_output | Q-E-0010 |
| Pasitka 2024, résumé (6,2 $/lb, base non vérifiée) | 13.67 | 65.1 | 151.9 | 155.3 | model_output | Q-E-0020 |
| Pasitka 2024 selon la revue Bry-Chevalier | 25.25 | 120.2 | 280.6 | 286.9 | model_output | Q-E-0045 |
| Modèle E/X, scénario optimiste (biomasse humide) | 7.65 | 36.4 | 85.0 | 86.9 | model_assumption + model_output | Q-X-0001 ; Q-K-0126 |
| Modèle E/X, scénario intermédiaire | 20.25 | 96.4 | 225.0 | 230.1 | model_assumption + model_output | Q-X-0002 ; Q-K-0126 |
| Modèle E/X, scénario prudent | 60.3 | 287.1 | 670.0 | 685.2 | model_assumption + model_output | Q-X-0003 ; Q-K-0126 |

## 5. Voie B — environnement par kg de protéine

| Indicateur | Cas | Base publiée (25 %→18 % de protéines) | Recalcul à 9 % | Unité | Nature | Réf. |
|---|---|---|---|---|---|---|
| GES | Sinke 2023, 2030 énergie renouvelable (scopes 1-2 + partie du scope 3) | 11.2–15.6 | 31.1–31.1 | kg CO2-eq/kg protéine | model_assumption + model_output | Q-E-0037 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |
| GES | Sinke 2023, 2030 mix électrique mondial | 57.2–79.4 | 158.9–158.9 | kg CO2-eq/kg protéine | model_assumption + model_output | Q-E-0038 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |
| GES | CE Delft 2021, plage des scénarios 2030 | 10.0–75.0 | 27.8–150.0 | kg CO2-eq/kg protéine | model_assumption + model_output | Q-K-0022 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |
| GES | Risner 2025, intrants purifiés (qualité pharmaceutique) | 984.0–8377.8 | 2733.3–16755.6 | kg CO2-eq/kg protéine | model_assumption + model_output | Q-E-0014 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |
| Énergie | CE Delft 2021, demande d'énergie 2030 | 588.0–1466.7 | 1633.3–2933.3 | MJ/kg protéine | model_assumption + model_output | Q-K-0021 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |
| Eau bleue | CE Delft 2021, eau bleue 2030 | 168.0–311.1 | 466.7–622.2 | L/kg protéine | model_assumption + model_output | Q-K-0017 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |
| Surface | CE Delft 2021, occupation des sols 2030 | 6.8–10.0 | 18.9–20.0 | m2·an/kg protéine | model_assumption + model_output | Q-K-0015 ; Q-K-0126 (hyp. protéine) ; Q-C-0021 |

Hypothèse forte (Q-K-0126) : l'impact par kg de produit est gardé constant quand la teneur en protéines passe de 18-25 % à 9 %. Une biomasse plus aqueuse pourrait réduire l'impact par kg de produit ; aucune ACV ne l'a modélisé.

## 6. Voie C — ingrédients et produits par kg de protéine

| Indicateur | Cas | Valeurs | Unité | idem USD | Nature | Réf. | Remarque |
|---|---|---|---|---|---|---|---|
| Coût | Isolat de soja, prix de marché 2019-2023 | 1.8–8.1 | EUR/kg protéine | 1.9–8.53 | measured_reported_by_review | Q-E-0065 | prix, pas un coût ; USD au change 2022 (indicatif) |
| Coût | e-SCP (bactéries H2), sites les moins chers 2028 | 5.5–6.1 | EUR/kg protéine | 6.21–6.89 | model_output | Q-E-0041 | sortie de modèle ; co-auteurs Solar Foods (SRC-E-0028) |
| Coût | Mycoprotéine, TEA (Risner 2023) | 29.56 | USD/kg protéine | 29.56 | model_output | Q-K-0085 | 3,55 $/kg de mycoprotéine humide à 11-12 % de protéines |
| GES | Protéine microbienne H2 (Järviö 2021, mix finlandais) | 11.6–13.0 | kg CO2-eq/kg protéine |  | model_output | Q-K-0089 | hydroélectricité : ~8 fois moins (par kg de produit) |
| GES | Mycoprotéine (Shahid 2024 ÷ 11 % de protéines) | 6.6 | kg CO2-eq/kg protéine |  | company_claim + published_estimate | Q-A-0064 ; Q-A-0019 | co-auteur industriel (CT-11) |
| GES | Tofu, Poore & Nemecek (moyenne) | 20.0 | kg CO2-eq/kg protéine |  | model_output | Q-K-0104 |  |
| GES | Tofu, ifeu 2020 (÷ 11 % de protéines CE Delft) | 9.1 | kg CO2-eq/kg protéine |  | model_output + published_estimate | Q-K-0094 ; Q-K-0025 | deux sources combinées (Allemagne / Pays-Bas) |
| GES | Pois (graine), Poore & Nemecek (moyenne) | 4.0 | kg CO2-eq/kg protéine |  | model_output | Q-K-0106 | ingrédient brut |
| GES | Escalope végétale soja, AGRIBALYSE (produit, toutes étapes) | 9.4–11.4 | kg CO2-eq/kg protéine |  | model_assumption + model_output | Q-K-0042 ; Q-K-0125 (hyp.) | inclut emballage, distribution, consommation |
| GES | Nuggets de soja, AGRIBALYSE (produit) | 7.7–9.3 | kg CO2-eq/kg protéine |  | model_assumption + model_output | Q-K-0044 ; Q-K-0125 (hyp.) |  |
| GES | Protéine bactérienne FeedKind (méthanotrophe, aliment), biogaz+renouvelable → gaz fossile | 2.23–7.99 | kg CO2-eq/kg protéine |  | model_output | Q-S-0053 ; Q-S-0051 | t/t = kg/kg ; ingrédient pour l'alimentation animale |
| GES | Concentré protéique de soja (référence du rapport FeedKind) | 0.791 | kg CO2-eq/kg protéine |  | published_estimate | Q-S-0054 | ingrédient |
| GES | Mycoprotéine Quorn 2018 (Carbon Trust) ÷ 11 % de protéines | 10.3 | kg CO2-eq/kg protéine |  | company_claim | Q-S-0019 ; Q-A-0019 | déclaration d'entreprise |
| GES | Tofu au supermarché, RIVM 2024 (÷ 11 % de protéines) | 20.8 | kg CO2-eq/kg protéine |  | published_estimate + statistical | Q-S-0087 ; Q-K-0025 | Pays-Bas |
| Énergie | Protéine microbienne H2 (Järviö 2021), hydro → mix finlandais | 156–370 | MJ/kg protéine |  | company_claim + model_output | Q-K-0116 ; Q-K-0087 ; Q-K-0090 | demande cumulée d'énergie (CED) |
| Énergie | e-SCP 2030, électricité seule (Fasihi 2025) | 252–263 | MJ/kg protéine |  | model_output | Q-E-0042 | MWh/t = kWh/kg ; électricité finale |
| Énergie | Escalope végétale soja, AGRIBALYSE (MJ non renouvelables, toutes étapes) | 283.9–343.7 | MJ/kg protéine |  | model_assumption + model_output | Q-K-0043 ; Q-K-0125 (hyp.) | transformation = 61 % du total |
| Énergie | Tofu, ifeu 2020 (énergie primaire ÷ 11 %) | 98.2 | MJ/kg protéine |  | model_output + published_estimate | Q-K-0118 ; Q-K-0025 |  |
| Eau bleue | Tofu, CE Delft 2021 | 245.5 | L/kg protéine |  | model_output + published_estimate | Q-K-0019 ; Q-K-0025 | même méthode que B et la référence poulet CE Delft |
| Surface | Tofu, Poore & Nemecek (moyenne) | 22.0 | m2·an/kg protéine |  | model_output | Q-K-0105 |  |
| Surface | Tofu, CE Delft 2021 | 16.4 | m2·an/kg protéine |  | model_output + published_estimate | Q-K-0020 ; Q-K-0025 |  |
| Surface | Pois (graine), Poore & Nemecek (moyenne) | 34.0 | m2·an/kg protéine |  | model_output | Q-K-0119 |  |
| Surface | Soja (graine), rendement protéique mondial | 8.7 | m2·an/kg protéine |  | published_estimate | Q-A-0023 | 1/rendement |
| Surface | SCP photovoltaïque (modèle, borne) | 0.0–0.83 | m2·an/kg protéine |  | model_output | Q-A-0024 | « >1 200 g/m2/an » → < 0,83 |

Aucun coût de **produit fini** de la voie C n'a été trouvé ; seul un prix relatif existe (viandes végétales +77 % au poids vs viande conventionnelle aux États-Unis en 2023, Q-K-0101).

## 6 bis. Base 3 — kg de protéine de qualité équivalente (DIAAS tronqué à 100 %, Q-K-0186)

Facteurs (min(DIAAS ; 100)/100) : poulet (filet et cuisse, in vitro) 1.00–1.00 (Q-S-0036) ; analogues végétaux de poulet du commerce (in vitro, 5 produits) 0.52–0.65 (Q-S-0015) ; biomasse de mycoprotéine (enfant → adulte) 0.83–0.97 (Q-S-0001 ; Q-S-0002) ; poudre Solein (protéine bactérienne H2) 0.51–0.51 (Q-S-0017).

| Cas | Par kg de protéine | Facteur DIAAS | Par kg de protéine de qualité équivalente | Unité | Réf. |
|---|---|---|---|---|---|
| Poulet cru, AGRIBALYSE toutes étapes (GES) | 19.2–24.0 | 1.00 | 19.2–24.0 | kg CO2-eq/kg protéine de qualité équivalente | Q-K-0045 ; Q-K-0040 ; Q-S-0036 |
| Analogues végétaux de soja, AGRIBALYSE (GES) | 7.7–11.4 | 0.52–0.65 | 11.8–21.9 | kg CO2-eq/kg protéine de qualité équivalente | Q-K-0042 ; Q-K-0044 ; Q-K-0125 ; Q-S-0015 |
| Mycoprotéine, coût TEA | 29.56 | 0.83–0.97 | 30.5–35.6 | USD/kg protéine de qualité équivalente | Q-K-0085 ; Q-S-0001 ; Q-S-0002 |
| Mycoprotéine, GES (Shahid 2024 ; Quorn 2018) | 6.6–10.3 | 0.83–0.97 | 6.8–12.4 | kg CO2-eq/kg protéine de qualité équivalente | Q-A-0064 ; Q-S-0019 ; Q-S-0001 ; Q-S-0002 |
| Protéine bactérienne H2, coût e-SCP 2028 (USD) | 6.21–6.89 | 0.51 | 12.2–13.5 | USD/kg protéine de qualité équivalente | Q-E-0041 ; Q-S-0017 |
| Protéine bactérienne H2, GES (Järviö 2021) | 11.6–13.0 | 0.51 | 22.7–25.5 | kg CO2-eq/kg protéine de qualité équivalente | Q-K-0089 ; Q-S-0017 |

DIAAS de la biomasse de poulet cultivée : inconnu (aucune mesure) ; la voie B n'est pas ajustée.

## 7. Analyse de sensibilité (un facteur à la fois, autour du scénario intermédiaire)

### A_cost_standard_EU6_2021 (base 12.7)

| Facteur | Valeur basse → haute | Résultat bas | Résultat haut | Rapport max/min | Réf. |
|---|---|---|---|---|---|
| protein_definition | 0.824 → 1.0 | 15.4 | 12.7 | 1.21 | Q-K-0053/Q-K-0052 (acides aminés vs N×facteur) |
| yield | 0.414 → 0.47 | 13.2 | 11.6 | 1.14 | Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| protein | 0.206 → 0.232 | 13.2 | 11.7 | 1.13 | Q-K-0049 ; Q-K-0046 ; Q-K-0123 |
| slaughter | 0.27 → 0.4 | 12.2 | 13.2 | 1.08 | Q-K-0060 |
| farm | 0.897 → 0.955 | 12.4 | 13.0 | 1.05 | Q-K-0059 |

### A_cost_system_choice_FR2022

standard 16.7 ; Label Rouge 42.1 ; bio 55.5 EUR2022/kg protéine comestible (Q-E-0029/0030/0031 ; Q-K-0112 ; Q-K-0128 ; Q-K-0121 ; rendements)

### B_cost_E_model (base 225.0)

| Facteur | Valeur basse → haute | Résultat bas | Résultat haut | Rapport max/min | Réf. |
|---|---|---|---|---|---|
| biomass_cost | 7.65 → 60.3 | 85.0 | 670.0 | 7.88 | Q-X-0001 / Q-X-0003 (× 0,09) |
| protein | 0.088 → 0.25 | 230.1 | 81.0 | 2.84 | Q-C-0021 ; Q-K-0126 (8,8-25 %) |

### A_GHG_standard_NL (base 35.8)

| Facteur | Valeur basse → haute | Résultat bas | Résultat haut | Rapport max/min | Réf. |
|---|---|---|---|---|---|
| LUC | 1.38 → 3.75 | 13.2 | 35.8 | 2.72 | Q-K-0070 (sans) / Q-K-0069 (avec) |
| allocation | 0.88 → 1.0 | 35.8 | 40.7 | 1.14 | Q-K-0124 |
| yield | 0.414 → 0.47 | 37.2 | 32.8 | 1.14 | Q-N-0035 ; Q-N-0014 ; Q-K-0064+Q-K-0065 |
| protein | 0.206 → 0.232 | 37.2 | 33.0 | 1.13 | Q-K-0049 ; Q-K-0046 ; Q-K-0123 |

### B_GHG (base 158.9)

| Facteur | Valeur basse → haute | Résultat bas | Résultat haut | Rapport max/min | Réf. |
|---|---|---|---|---|---|
| energy_and_purity | 2.8 → 1508.0 | 31.1 | 16755.6 | 538.57 | Q-E-0037 (renouvelable) → Q-E-0014 (intrants purifiés, Risner) |
| protein | 0.088 → 0.25 | 162.5 | 57.2 | 2.84 | Q-C-0021 ; Q-K-0126 |

## 8. Seuils de parité (coût maximal de la biomasse humide pour égaler le haut de plage de la voie A standard)

| Comparateur A | A, USD/kg protéine (prudent) | Biomasse max. à 9 % | à 21 % |
|---|---|---|---|
| UE moyenne 2017, standard | 14.45 | 1.3 | 3.03 |
| UE six pays 2021, standard | 17.29 | 1.56 | 3.63 |
| France 2022, standard (ITAVI) | 19.03 | 1.71 | 4.0 |
| États-Unis 2023, standard (grande échelle, hors abattage) | 13.43 | 1.21 | 2.82 |
| Brésil (Paraná) 2025, standard (hors abattage) | 9.66 | 0.87 | 2.03 |

## 9. CT-10 — base « animal entier » vs « protéine comestible »

Protéine de l'animal entier 0.181 kg/kg PV contre 0.0922 kg/kg PV de protéine comestible (rapport 1.96). Le prix de 4,6 USD/kg de protéine (animal entier, EV-A-0042) équivaut à 9.0 USD/kg de protéine comestible (Q-N-0034 ; Q-A-0053 ; rendement Q-N-0014 ; protéine Q-K-0046).

## 10. Lignes Q utilisées

| Q | Paramètre | Valeur | Unité | Nature | Source |
|---|---|---|---|---|---|
| Q-A-0019 | Protéines, mycoprotéine (ingrédient, poids humide) | 11 | g/100 g | company_claim | SRC-A-0005 |
| Q-A-0023 | Rendement protéique du soja (moyenne mondiale pondérée) | 115 | g protéine/m²/an | published_estimate | SRC-A-0011 |
| Q-A-0024 | Rendement protéique modélisé de la SCP photovoltaïque (H2, méthanol, formiate) | >1200 | g protéine/m²/an | model_output | SRC-A-0011 |
| Q-A-0053 | Prix par kg de protéine sèche, poulet | 4.6 | USD/kg protéine MS | statistical | SRC-A-0037 |
| Q-A-0064 | Émissions GES de la mycoprotéine (ingrédient) | 0.73 | kg CO2e/kg | published_estimate | SRC-A-0045 |
| Q-C-0021 | Protéines dans la biomasse cellulaire récoltée (caille cultivée) | 8.8-9.5 | g protein per 100 g | measured | SRC-C-0008 |
| Q-C-0082 | Teneur en protéines de la biomasse humide implicite dans l'hypothèse de Humbird | 21 | % (0.30 dry fraction × 0.70 protein in dry mass) | model_assumption | SRC-E-0001 |
| Q-E-0001 | Coût de production, masse cellulaire humide, fed-batch | 37 | $/kg | model_output | SRC-E-0001 |
| Q-E-0002 | Coût de production, masse cellulaire humide, perfusion | 51 | $/kg | model_output | SRC-E-0001 |
| Q-E-0006 | Coût fed-batch avec hydrolysat végétal à 2 $/kg | 22 | $/kg | model_output | SRC-E-0001 |
| Q-E-0010 | Coût minimal de la viande cultivée, scénario 1 (référence 2019) | 437000 | USD/kg | model_output | SRC-E-0002 |
| Q-E-0011 | Coût minimal de la viande cultivée, scénario 4 (limites levées) | 1.95 | USD/kg | model_output | SRC-E-0002 |
| Q-E-0014 | PRG viande cultivée, scénarios à intrants purifiés | 246-1508 | kg CO2e/kg cultured meat | model_output | SRC-E-0003 |
| Q-E-0020 | Coût projeté du poulet cultivé, usine 50 000 L | 6.2 | US$/lb | model_output | SRC-X-0001 |
| Q-E-0022 | Coût de production poulet en élevage, moyenne UE | 82.5 | eurocent per kg live weight | published_estimate | SRC-E-0011 |
| Q-E-0029 | Coût de production poulet standard France (rémunération éleveur incluse) | 1.264 | €/kg vif | statistical | SRC-E-0012 |
| Q-E-0030 | Coût de production poulet Label Rouge France | 2.485 | €/kg vif | statistical | SRC-E-0012 |
| Q-E-0031 | Coût de production poulet biologique France | 3.366 | €/kg vif | statistical | SRC-E-0012 |
| Q-E-0032 | Coût de production poulet de chair Paraná (ICPFrango) | 4.60 | R$/kg | statistical | SRC-E-0013 |
| Q-E-0033 | COGS viande cultivée, scénario actuel (1) | 22421 | $/kg CM | model_output | SRC-E-0014 |
| Q-E-0034 | COGS viande cultivée, scénario 2030 tous leviers (8) | 6.43 | $/kg CM | model_output | SRC-E-0014 |
| Q-E-0037 | Empreinte carbone viande cultivée 2030, benchmark ambitieux (renouvelable scopes 1-3) | 2.8 | kg CO2-eq./kg meat | model_output | SRC-E-0015 |
| Q-E-0038 | Empreinte carbone viande cultivée 2030, mix énergétique mondial | 14.3 | kg CO2-eq./kg meat | model_output | SRC-E-0015 |
| Q-E-0041 | Coût de la protéine e-SCP 2028, sites les moins chers | 5500-6100 | € t−1 protein | model_output | SRC-E-0028 |
| Q-E-0042 | Consommation d'électricité Power-to-SCP 2030 | 70-73 | MWh t−1 protein | model_output | SRC-E-0028 |
| Q-E-0045 | Coût TEA Pasitka et al. selon revue | 23.26-27.24 | $/kg | model_output | SRC-A-0024 |
| Q-E-0049 | Rendement carcasse supposé (carcasse/poids vif) | 70 | % of live weight | model_assumption | SRC-E-0011 |
| Q-E-0061 | Taux de change annuel moyen USD/EUR 2017 | 1.1297 | US dollar/Euro | statistical | SRC-E-0038 |
| Q-E-0063 | Taux de change annuel moyen USD/EUR 2022 | 1.0530 | US dollar/Euro | statistical | SRC-E-0038 |
| Q-E-0064 | Taux de change annuel moyen BRL/EUR 2025 | 6.3072 | Brazilian real/Euro | statistical | SRC-E-0038 |
| Q-E-0065 | Prix de marché des isolats de protéine de soja | 1.8-8.1 | €/kg protein | measured_reported_by_review | SRC-A-0024 |
| Q-K-0001 | GES moyens mondiaux de la viande de poulet de chair (berceau-détail, GLEAM) | 5.4 | kg CO2-eq/kg CW | model_output | SRC-K-0001 |
| Q-K-0004 | GES de la viande de poulet britannique par kg de protéine (méthode GLEAM) | 43.5 | kg CO2-eq/kg meat protein | model_output | SRC-K-0001 |
| Q-K-0005 | Rendement en viande sans gras ni os supposé dans les comparaisons de la FAO | 59 | % of carcass weight | model_assumption | SRC-K-0001 |
| Q-K-0006 | Part des émissions allouée aux coproduits d'abattage (convention Kool et al. 2009 reprise  | 12 | % | model_assumption | SRC-K-0001 |
| Q-K-0010 | Teneur en protéines de la viande de poulet utilisée par Mekonnen & Hoekstra | 127 | g/kg | published_estimate | SRC-K-0002 |
| Q-K-0012 | Empreinte eau bleue de la viande de poulet, système industriel (moyenne mondiale) | 210 | m3/ton | model_output | SRC-K-0002 |
| Q-K-0013 | Empreinte eau bleue de la viande de poulet, système de pâturage (moyenne mondiale) | 734 | m3/ton | model_output | SRC-K-0002 |
| Q-K-0015 | Occupation des sols de la viande cultivée 2030 (énergie renouvelable / conventionnelle) | 1.7-1.8 | m2a crop-eq./kg product | model_output | SRC-K-0003 |
| Q-K-0016 | Occupation des sols du poulet, référence ambitieuse 2030 (CE Delft) | 4.6 | m2a crop-eq./kg product | model_output | SRC-K-0003 |
| Q-K-0017 | Eau bleue de la viande cultivée 2030 (énergie conventionnelle / renouvelable) | 42-56 | litre/kg product | model_output | SRC-K-0003 |
| Q-K-0018 | Eau bleue du poulet, référence ambitieuse 2030 (CE Delft) | 46 | litre/kg product | model_output | SRC-K-0003 |
| Q-K-0019 | Eau bleue du tofu (CE Delft) | 27 | litre/kg product | model_output | SRC-K-0003 |
| Q-K-0020 | Occupation des sols du tofu (CE Delft) | 1.8 | m2a crop-eq./kg product | model_output | SRC-K-0003 |
| Q-K-0021 | Demande d'énergie de la viande cultivée 2030 (plage des scénarios) | 147-264 | MJ/kg product | model_output | SRC-K-0003 |
| Q-K-0022 | Empreinte carbone de la viande cultivée 2030 (plage des scénarios) | 2.5-13.5 | kg CO2-eq./kg product | model_output | SRC-K-0003 |
| Q-K-0023 | Teneur en protéines supposée du produit de viande cultivée (CE Delft) | 18-25 | % of total weight | model_assumption | SRC-K-0003 |
| Q-K-0024 | Teneur en protéines du poulet retenue par CE Delft | 23 | % of total weight | published_estimate | SRC-K-0003 |
| Q-K-0025 | Teneur en protéines du tofu retenue par CE Delft | 11 | % of total weight | published_estimate | SRC-K-0003 |
| Q-K-0027 | Changement climatique, poulet conventionnel, sortie ferme (France) | 1.864 | kg CO2 eq/kg | model_output | SRC-K-0004 |
| Q-K-0028 | Épuisement des ressources énergétiques, poulet conventionnel, sortie ferme | 11.34 | MJ/kg | model_output | SRC-K-0004 |
| Q-K-0029 | Utilisation du sol, poulet conventionnel, sortie ferme | 161.6 | Pt/kg | model_output | SRC-K-0004 |
| Q-K-0030 | Épuisement des ressources en eau, poulet conventionnel, sortie ferme | 0.72 | m3 depriv./kg | model_output | SRC-K-0004 |
| Q-K-0031 | Changement climatique, poulet Label Rouge, sortie ferme (France) | 2.335 | kg CO2 eq/kg | model_output | SRC-K-0004 |
| Q-K-0032 | Épuisement des ressources énergétiques, poulet Label Rouge, sortie ferme | 18.5 | MJ/kg | model_output | SRC-K-0004 |
| Q-K-0033 | Utilisation du sol, poulet Label Rouge, sortie ferme | 210.1 | Pt/kg | model_output | SRC-K-0004 |
| Q-K-0034 | Épuisement des ressources en eau, poulet Label Rouge, sortie ferme | 1.306 | m3 depriv./kg | model_output | SRC-K-0004 |
| Q-K-0035 | Changement climatique, poulet biologique (moyenne), sortie ferme (France) | 2.985 | kg CO2 eq/kg | model_output | SRC-K-0004 |
| Q-K-0036 | Épuisement des ressources énergétiques, poulet biologique (moyenne), sortie ferme | 24.26 | MJ/kg | model_output | SRC-K-0004 |
| Q-K-0037 | Utilisation du sol, poulet biologique (moyenne), sortie ferme | 416.0 | Pt/kg | model_output | SRC-K-0004 |
| Q-K-0038 | Épuisement des ressources en eau, poulet biologique (moyenne), sortie ferme | 3.296 | m3 depriv./kg | model_output | SRC-K-0004 |
| Q-K-0039 | Changement climatique, poulet biologique systèmes n° 1 et 2, sortie ferme | 4.23-4.47 | kg CO2 eq/kg | model_output | SRC-K-0004 |
| Q-K-0040 | Changement climatique, filet de poulet sans peau cru (France, toutes étapes) | 5.404 | kg CO2 eq/kg | model_output | SRC-K-0005 |
| Q-K-0041 | Épuisement des ressources énergétiques, filet de poulet cru (toutes étapes) | 68.8 | MJ/kg | model_output | SRC-K-0005 |
| Q-K-0042 | Changement climatique, escalope végétale ou steak à base de soja (France, toutes étapes) | 2.168 | kg CO2 eq/kg | model_output | SRC-K-0005 |
| Q-K-0043 | Épuisement des ressources énergétiques, escalope végétale à base de soja (toutes étapes) | 65.3 | MJ/kg | model_output | SRC-K-0005 |
| Q-K-0044 | Changement climatique, nuggets de soja (France, toutes étapes) | 1.76 | kg CO2 eq/kg | model_output | SRC-K-0005 |
| Q-K-0045 | Changement climatique, viande de poulet crue (France, toutes étapes) | 4.113 | kg CO2 eq/kg | model_output | SRC-K-0005 |
| Q-K-0046 | Protéines, viande de poulet crue sans peau (viande seule) | 21.4 | g/100 g | measured | SRC-K-0006 |
| Q-K-0047 | Protéines, filet de poulet cru sans peau ni os | 22.5 | g/100 g | measured | SRC-K-0006 |
| Q-K-0049 | Proteína, frango inteiro sem pele cru | 20.6 | g/100 g | measured | SRC-K-0007 |
| Q-K-0052 | たんぱく質（N×係数）, 若どり むね 皮なし 生 | 23.3 | g/100 g | measured | SRC-K-0008 |
| Q-K-0053 | アミノ酸組成によるたんぱく質, 若どり むね 皮なし 生 | 19.2 | g/100 g | measured | SRC-K-0008 |
| Q-K-0056 | Coût de production sortie ferme, poulet ECC sans éclaircie, Pays-Bas 2021 | 112.3 | cents per kg live weight | published_estimate | SRC-K-0009 |
| Q-K-0058 | Coût de production sortie ferme, poulet ECC, France 2021 | 108.2 | cents per kg live weight | published_estimate | SRC-K-0009 |
| Q-K-0059 | Coût de production sortie ferme, poulet conventionnel, six pays de l'UE 2021 (PL-DE) | 89.7-95.5 | cents per kg live weight | published_estimate | SRC-K-0009 |
| Q-K-0060 | Coût d'abattage, poulet conventionnel, six pays de l'UE 2021 | 27-40 | cents per kg carcass weight | published_estimate | SRC-K-0009 |
| Q-K-0061 | Rendement d'abattage retenu (carcasse / poids vif) | 73 | % | model_assumption | SRC-K-0009 |
| Q-K-0064 | Filet en % du poids vif : conventionnel / DRB / Beter Leven 1 étoile | 25.0 | % of live weight | company_claim | SRC-K-0010 |
| Q-K-0065 | Viande de cuisse en % du poids vif : conventionnel / DRB / BLS | 16.4 | % of live weight | company_claim | SRC-K-0010 |
| Q-K-0066 | Viande désossée totale (filet + viande de cuisse) en % du poids vif, poulet Beter Leven 1  | 35.3 | % of live weight | company_claim | SRC-K-0010 |
| Q-K-0069 | GES par kg de poids vif abattu, avec LUC : conventionnel / DRB / BLS | 3.75 | kg CO2-eq/kg live weight | model_output | SRC-K-0010 |
| Q-K-0070 | GES par kg de poids vif abattu, sans LUC : conventionnel / DRB / BLS | 1.38 | kg CO2-eq/kg live weight | model_output | SRC-K-0010 |
| Q-K-0071 | GES par kg de poids vif abattu, poulet Beter Leven 1 étoile (avec / sans LUC) | 1.75-3.64 | kg CO2-eq/kg live weight | model_output | SRC-K-0010 |
| Q-K-0072 | Occupation des sols par kg de poids vif abattu : conventionnel | 3.59 | m2a crop eq/kg live weight | model_output | SRC-K-0010 |
| Q-K-0073 | Occupation des sols par kg de poids vif abattu : Beter Leven 1 étoile | 4.32 | m2a crop eq/kg live weight | model_output | SRC-K-0010 |
| Q-K-0074 | Électricité d'abattoir par tonne de poids vif | 95 | kWh/ton live weight | company_claim | SRC-K-0010 |
| Q-K-0076 | Rendement en filet, souche S757N (type Label Rouge) bio à 85 j, mâles peu/très utilisateur | 14.1-14.5 | % of BW | measured | SRC-K-0011 |
| Q-K-0077 | Rendement en filet, souche JA757 (poulet certifié) bio à 71 j | 15.8-16.4 | % of BW | measured | SRC-K-0011 |
| Q-K-0080 | Coût total de production, poulet conventionnel grande échelle, États-Unis (prix S1 2023) | 0.5197 | USD/lb live weight | published_estimate | SRC-K-0013 |
| Q-K-0082 | Coût total de production, poulet en pâturage (parcs mobiles), États-Unis (2023) | 1.916 | USD/lb live weight | published_estimate | SRC-K-0013 |
| Q-K-0085 | Coût de production de la protéine de mycoprotéine (TEA, base) | 29.56 | $/kg protein | model_output | SRC-K-0014 |
| Q-K-0087 | Demande cumulée d'énergie de la protéine microbienne (poudre, mix électrique finlandais) | 240.2 | MJ/kg product | model_output | SRC-K-0015 |
| Q-K-0089 | GES de la protéine microbienne par 100 g de protéine (mix électrique finlandais) | 1.16-1.3 | kg CO2-eq per 100 g protein | model_output | SRC-K-0015 |
| Q-K-0090 | Teneur en protéines de la poudre de protéine microbienne (mesures nutritionnelles du produ | 65 | % | company_claim | SRC-K-0015 |
| Q-K-0091 | CO2-Fußabdruck, Hähnchen (Durchschnitt), an der Supermarktkasse | 5.5 | kg CO2-Äq./kg Lebensmittel | model_output | SRC-K-0016 |
| Q-K-0092 | Flächen-Fußabdruck, Hähnchen (Durchschnitt) | 4 | m2·a Naturflächenbelegung/kg LM | model_output | SRC-K-0016 |
| Q-K-0093 | Primärenergiebedarf, Hähnchen (Durchschnitt) | 10 | kWh Primärenergie-Äq./kg LM | model_output | SRC-K-0016 |
| Q-K-0094 | CO2-Fußabdruck, Tofu | 1.0 | kg CO2-Äq./kg Lebensmittel | model_output | SRC-K-0016 |
| Q-K-0100 | Surface de maïs et de soja mobilisée par kg de poids vif, Brésil 2020 (sans allocation hui | 4.0 | m2/kg live weight | model_output | SRC-K-0017 |
| Q-K-0102 | GES de la viande de volaille par 100 g de protéine (moyenne ; 10e centile) | 5.7 | kg CO2eq per 100 g protein | model_output | SRC-E-0030 |
| Q-K-0103 | Occupation des sols de la viande de volaille par 100 g de protéine (moyenne ; 10e centile) | 7.1 | m2·year per 100 g protein | model_output | SRC-E-0030 |
| Q-K-0104 | GES du tofu par 100 g de protéine (moyenne) | 2.0 | kg CO2eq per 100 g protein | model_output | SRC-E-0030 |
| Q-K-0105 | Occupation des sols du tofu par 100 g de protéine (moyenne) | 2.2 | m2·year per 100 g protein | model_output | SRC-E-0030 |
| Q-K-0106 | GES des pois par 100 g de protéine (moyenne) | 0.4 | kg CO2eq per 100 g protein | model_output | SRC-E-0030 |
| Q-K-0107 | Taux de change annuel moyen USD/EUR 2021 | 1.1827 | US dollar/Euro | statistical | SRC-E-0038 |
| Q-K-0108 | Taux de change annuel moyen USD/EUR 2023 | 1.0813 | US dollar/Euro | statistical | SRC-E-0038 |
| Q-K-0109 | Taux de change annuel moyen USD/EUR 2025 | 1.1300 | US dollar/Euro | statistical | SRC-E-0038 |
| Q-K-0110 | Coût d'abattage du poulet, neuf pays de l'UE 2017 | 21-38 | eurocents per kg carcass weight | published_estimate | SRC-E-0011 |
| Q-K-0111 | Coût d'abattage, poulet ECC, six pays de l'UE 2021 | 28.2-41.2 | cents per kg carcass weight | published_estimate | SRC-K-0009 |
| Q-K-0112 | Coût d'abattage, France 2021 : conventionnel | 38 | cents per kg carcass weight | published_estimate | SRC-K-0009 |
| Q-K-0113 | Coût d'abattage, France 2021 : poulet ECC | 39.2 | cents per kg carcass weight | published_estimate | SRC-K-0009 |
| Q-K-0114 | Rendement d'abattage supposé du poulet ECC | 71.5 | % | model_assumption | SRC-K-0009 |
| Q-K-0115 | GES de l'énergie d'abattoir et du transport vers l'abattoir, par kg de poids vif | 0.09 | kg CO2-eq/kg live weight | model_output | SRC-K-0010 |
| Q-K-0116 | Demande cumulée d'énergie de la protéine microbienne, scénario hydroélectrique (FHE) | 101.2 | MJ/kg product | model_output | SRC-K-0015 |
| Q-K-0118 | Primärenergiebedarf, Tofu | 3 | kWh Primärenergie-Äq./kg LM | model_output | SRC-K-0016 |
| Q-K-0119 | Occupation des sols des pois par 100 g de protéine (moyenne) | 3.4 | m2·year per 100 g protein | model_output | SRC-E-0030 |
| Q-K-0120 | Empreinte eau bleue de la viande de poulet, système mixte (moyenne mondiale) | 348 | m3/ton | model_output | SRC-K-0002 |
| Q-K-0121 | Rendement carcasse, souche S757N (type Label Rouge) bio à 85 j | 67.6-69.0 | % of BW | measured | SRC-K-0011 |
| Q-K-0122 | Hypothèse : viande de cuisse désossée des souches Label Rouge / bio = valeur du poulet Bet | 16.1 | % of live weight | model_assumption | SRC-K-0019 |
| Q-K-0123 | Hypothèse : teneur en protéines de la viande désossée identique pour les systèmes standard | 20.6-23.2 | g/100 g | model_assumption | SRC-K-0019 |
| Q-K-0124 | Hypothèse : allocation de 100 % (prudent) ou 88 % (intermédiaire, optimiste) des impacts e | 0.88-1.0 | fraction | model_assumption | SRC-K-0019 |
| Q-K-0125 | Hypothèse : teneur en protéines de l'escalope végétale à base de soja d'AGRIBALYSE = plage | 19-23 | g/100 g | model_assumption | SRC-K-0019 |
| Q-K-0126 | Hypothèse : teneur en protéines du produit de viande cultivée de Sinke et al. 2023 = compo | 9-25 | % of total weight | model_assumption | SRC-K-0019 |
| Q-K-0128 | Hypothèse : coût d'abattage des poulets Label Rouge et bio français = coût ECC France 2021 | 39.2 | cents per kg carcass weight | model_assumption | SRC-K-0019 |
| Q-K-0186 | Hypothèse : ajustement à la qualité protéique par le DIAAS tronqué à 100 % (kg de protéine | 100 | % (plafond de troncature) | model_assumption | SRC-K-0019 |
| Q-N-0014 | Viande totale désossée (filet + cuisse sans peau ni os), mâle Ross 308 à 3,0 kg | 43.10 | % of live weight | company_claim | SRC-N-0003 |
| Q-N-0034 | Teneur en protéines de l'animal entier (carcasse + cinquième quartier), poulet de chair | 181 | g/kg | measured_reported_by_review | SRC-N-0012 |
| Q-N-0035 | Part de la viande dans le poids vif, poulet de chair | 47 | % du PV | measured_reported_by_review | SRC-N-0012 |
| Q-S-0001 | ivDIAAS biomasse de mycoprotéine ABUNDA, profil enfant 3–10 ans (AA limitant : soufrés) | 83 | % | measured | SRC-S-0001 |
| Q-S-0002 | ivDIAAS biomasse de mycoprotéine ABUNDA, profil adulte (AA limitant : soufrés) | 97 | % | measured | SRC-S-0001 |
| Q-S-0015 | DIAAS in vitro de cinq analogues végétaux de poulet du commerce | 52-65 | % | measured | SRC-S-0003 |
| Q-S-0017 | ivDIAAS de la poudre Solein (émulsion non fermentée), AA limitant Ile | 51.0 | % | measured | SRC-S-0004 |
| Q-S-0019 | Empreinte carbone de la mycoprotéine Quorn (cradle-to-processor gate), 2018 | 1.137 | kg CO2e/kg | company_claim | SRC-S-0005 |
| Q-S-0036 | DIAAS in vitro du poulet (filet et cuisse) | 100 | % | measured | SRC-S-0003 |
| Q-S-0051 | Empreinte carbone de FeedKind par tonne de protéine, scénario 1 (gaz fossile) | 7.99 | tCO2e/t protein | model_output | SRC-S-0021 |
| Q-S-0053 | Empreinte carbone de FeedKind par tonne de protéine, biogaz + électricité renouvelable | 2.23 | tCO2e/t protein | model_output | SRC-S-0021 |
| Q-S-0054 | Empreinte carbone du concentré protéique de soja par kg de protéine (référence du rapport  | 0.791 | kgCO2e/kg protein | published_estimate | SRC-S-0021 |
| Q-S-0085 | Potentiel de réchauffement du filet de poulet au supermarché (RIVM 2024) | 3.943 | kg CO2 eq/kg | statistical | SRC-S-0030 |
| Q-S-0087 | Potentiel de réchauffement du tofu au supermarché (RIVM 2024) | 2.293 | kg CO2 eq/kg | statistical | SRC-S-0030 |
| Q-S-0089 | Occupation des sols du filet de poulet (RIVM 2024) | 5.48 | m2a crop eq/kg | statistical | SRC-S-0030 |
| Q-X-0001 | Coût de la protéine cultivée, recalcul avec 9 % de protéines (scénario optimiste) | 85 | USD/kg protein | model_output | SRC-E-0042;SRC-C-0008 |
| Q-X-0002 | Coût de la protéine cultivée, recalcul avec 9 % de protéines (scénario intermédiaire) | 225 | USD/kg protein | model_output | SRC-E-0042;SRC-C-0008 |
| Q-X-0003 | Coût de la protéine cultivée, recalcul avec 9 % de protéines (scénario prudent) | 670 | USD/kg protein | model_output | SRC-E-0042;SRC-C-0008 |
