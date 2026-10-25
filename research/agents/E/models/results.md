# Résultats du modèle économique (agent E) — sorties de modèle, pas des coûts démontrés

## Voie A — coût par kg de viande désossée et par kg de protéine

| Système | Coût élevage /kg PV | Monnaie | Réf. | Coût /kg viande désossée | Coût /kg protéine | idem en USD (même année) |
|---|---|---|---|---|---|---|
| UE moyenne, standard (2017) | 0.825 | EUR2017 | Q-E-0022 | 2.07–2.53 | 8.3–14.1 | 9.3–15.9 |
| Pologne, standard (2017) | 0.786 | EUR2017 | Q-E-0026 | 1.99–2.44 | 7.9–13.6 | 9.0–15.3 |
| Brésil, standard (2017) | 0.632 | EUR2017 | Q-E-0023 | 1.66–2.08 | 6.6–11.6 | 7.5–13.1 |
| États-Unis, standard (2017) | 0.645 | EUR2017 | Q-E-0024 | 1.69–2.11 | 6.7–11.7 | 7.6–13.3 |
| France, standard (2022) | 1.264 | EUR2022 | Q-E-0029 | 3.0–3.55 | 12.0–19.7 | 12.6–20.8 |
| France, Label Rouge (2022) | 2.485 | EUR2022 | Q-E-0030 | 5.6–6.38 | 22.4–35.5 | 23.6–37.3 |
| France, biologique (2022) | 3.366 | EUR2022 | Q-E-0031 | 7.47–8.43 | 29.9–46.8 | 31.5–49.3 |

Hypothèses : abattage 0,21-0,38 €/kg carcasse (UE 2017, Q-E-0027) appliqué à tous les systèmes ; rendement carcasse 0,70 (Q-E-0049) ; viande désossée 43,1-47 % du PV (Q-N-0014, Q-N-0035 ; probablement surestimé pour Label Rouge/bio) ; protéine 18-25 % (Q-E-0052) ; 100 % des coûts imputés à la viande ; découpe, emballage, distribution exclus.

## Voie B — modèle ascendant par kg de masse cellulaire humide (USD ≈ 2018-2020)

Contrôle de calibration (Humbird 2021, tableau 2) : fed-batch modèle 36.4 $/kg vs 37 ; perfusion modèle 51.7 $/kg vs 51.

| Scénario | Capital + frais fixes | Milieu | Autres OPEX | Total $/kg humide | Total $/kg protéine | Total €2020/kg protéine |
|---|---|---|---|---|---|---|
| prudent | 30.3 | 22.0 | 8.0 | 60.3 | 287 | 251 |
| intermediate | 10.3 | 7.0 | 3.0 | 20.3 | 97 | 85 |
| optimistic | 1.7 | 4.0 | 2.0 | 7.7 | 36 | 32 |

Paramètres et références :

| Paramètre | Prudent | Intermédiaire | Optimiste | Unité | Référence |
|---|---|---|---|---|---|
| tci_usd_per_kg_yr | 96.1 | 48.2 | 12.7 | USD par (kg/an) de capacité | Q-E-0004 ; Q-E-0003 ; Q-E-0048/Q-E-0047 |
| capital_recovery_factor | 0.146 | 0.102 | 0.0333 | fraction du TCI par an | dérivé Q-E-0003 ; model_assumption ; model_assumption (CE Delft) |
| fixed_om_fraction | 0.09 | 0.09 | 0.09 | fraction du TCI par an | SRC-E-0001 (section 2.5) |
| utilization | 0.75 | 0.9 | 0.95 | fraction de la capacité nominale | model_assumption |
| medium_usd_per_kg | 22 | 7 | 4 | USD/kg masse cellulaire humide | Q-E-0005 ; dérivé Q-E-0001/Q-E-0006 ; model_assumption |
| other_opex_usd_per_kg | 8 | 3 | 2 | USD/kg masse cellulaire humide | SRC-E-0001 tableau 2 ; model_assumption |

### Sensibilité (tornade) autour du scénario intermédiaire (20.3 $/kg humide)

| Paramètre | Coût si valeur optimiste | Coût si valeur prudente | Amplitude | Réf. |
|---|---|---|---|---|
| medium_usd_per_kg | 17.3 | 35.3 | 18.0 | Q-E-0005 ; dérivé Q-E-0001/Q-E-0006 ; model_assumption |
| tci_usd_per_kg_yr | 12.7 | 30.5 | 17.8 | Q-E-0004 ; Q-E-0003 ; Q-E-0048/Q-E-0047 |
| capital_recovery_factor | 16.6 | 22.7 | 6.1 | dérivé Q-E-0003 ; model_assumption ; model_assumption (CE Delft) |
| other_opex_usd_per_kg | 19.3 | 25.3 | 6.0 | SRC-E-0001 tableau 2 ; model_assumption |
| utilization | 19.7 | 22.3 | 2.6 | model_assumption |
| fixed_om_fraction | 20.3 | 20.3 | 0.0 | SRC-E-0001 (section 2.5) |

### Monte-Carlo illustratif (20 000 tirages triangulaires, graine 42)

P5 / P50 / P95 = 17.6 / 26.2 / 36.3 $/kg humide.

Part des tirages dont le coût par kg de protéine est inférieur au haut de la plage de la voie A (coût de la viande désossée, même base protéine, sans correction d'inflation) :

- EU_standard_2017_high (15.9 $/kg protéine) : 0.0%
- FR_label_rouge_2022_high (37.3 $/kg protéine) : 0.0%
- FR_bio_2022_high (49.3 $/kg protéine) : 0.0%

Avertissement : ces parts mesurent la position des hypothèses publiées, pas une probabilité réelle ; le coût de la masse cellulaire humide exclut la mise en forme, l'emballage, la distribution et la marge.

### Seuils de parité (base protéine)

| Comparateur (haut de plage voie A) | $/kg protéine | Coût max. admissible de la masse humide $/kg |
|---|---|---|
| EU_standard_2017_high | 15.9 | 3.34 |
| FR_label_rouge_2022_high | 37.3 | 7.83 |
| FR_bio_2022_high | 49.3 | 10.35 |

Plancher du scénario optimiste sans aucun coût en capital (milieu + autres OPEX) : 6.0 $/kg humide.

### Sensibilité à la consommation de milieu au prix déclaré de 0,63 $/L (Q-E-0019, company_claim)

| L de milieu par kg humide | Coût du milieu $/kg |
|---|---|
| 2.3 | 1.45 |
| 5 | 3.15 |
| 10 | 6.3 |
| 20 | 12.6 |
| 50 | 31.5 |

## Voie C — coûts d'ingrédients protéiques disponibles (pas de produit fini)

| Ingrédient | Valeur | Unité | Réf. | Nature |
|---|---|---|---|---|
| e-SCP (H2-oxydantes), meilleurs sites 2028 | 5.5-6.1 | EUR/kg protéine | Q-E-0041 | model_output (COI Solar Foods) |
| e-SCP, Finlande 2028 | >7.3 | EUR/kg protéine | Q-E-0041 (notes) | model_output |
| Isolat de soja, prix de marché 2019-2023 | 1.8-8.1 | EUR/kg protéine | Q-E-0065 | prix de marché (pas un coût) |
| Isolat de pois, prix de marché 2020-2023 | 3.5-9.3 | EUR/kg protéine | Q-E-0065 (notes) | prix de marché (pas un coût) |
| Mycoprotéine (TEA citée par revue, base non précisée) | 3.55 | USD/kg | Q-E-0066 | model_output, source primaire non identifiée |

## Émissions par kg de protéine (RQ-X2)

| Système | Valeur source | kg CO2-eq/kg protéine (bas) | (haut) | Réf. | Conversion |
|---|---|---|---|---|---|
| Poulet conventionnel NL, avec LUC | 3.65 /kg PV | 31.1 | 47.0 | Q-E-0015 | 100 % imputé à la viande désossée (surestimation) |
| Poulet BLS (croissance lente) NL, avec LUC | 3.55 /kg PV | 30.2 | 45.8 | Q-E-0016 | 100 % imputé à la viande désossée (surestimation) |
| Poulet conventionnel NL, soja faible LUC | 1.37 /kg PV | 11.7 | 17.7 | Q-E-0017 | 100 % imputé à la viande désossée (surestimation) |
| Poulet 2030 « ambitieux » (Sinke) | 2.7 /kg viande | 10.8 | 15.0 | Q-E-0039 | base kg de viande |
| Poulet actuel « ambitieux » (Sinke, Agri-footprint) | 6.0 /kg viande | 24.0 | 33.3 | Q-E-0039 (notes) | base kg de viande |
| Poulet moyenne mondiale 2018 (Poore & Nemecek via Sinke) | 9.0 /kg viande | 36.0 | 50.0 | Q-E-0039 (notes) | base kg de viande |
| Viande cultivée 2030, renouvelable total (Sinke) | 2.8 /kg viande | 11.2 | 15.6 | Q-E-0037 | base kg de viande |
| Viande cultivée 2030, renouvelable sur site (Sinke) | 4.0 /kg viande | 16.0 | 22.2 | Q-E-0037 (notes) | base kg de viande |
| Viande cultivée 2030, mix mondial (Sinke) | 14.3 /kg viande | 57.2 | 79.4 | Q-E-0038 | base kg de viande |
| Viande cultivée, Risner 2025 (tous scénarios) | 12-1508 /kg | 57 | 7181 | Q-E-0013 | protéine = 21 % (Q-E-0050/0051) |
