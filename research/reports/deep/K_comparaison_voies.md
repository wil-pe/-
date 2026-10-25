# Comparaison homogène des trois voies par kg de protéine comestible (mission X2, agent K)

*Rapport d'approfondissement de phase 4 — 2026-10-25. Toutes les valeurs comparatives sont des **sorties de modèle** (`research/agents/K/models/comparison.py`, SRC-K-0019) calculées à partir de lignes `Q-…` sourcées ; aucune n'est une mesure de production. Lacunes visées : KG-X01, KG-X02 (RQ-X1, RQ-X2) ; contradictions : CT-10 (résolue), CT-01, CT-09, CT-15, CT-20 (précisées).*

## 1. Périmètre, méthode et limites

**Question.** Que coûtent et qu'émettent les trois voies — A élevage (standard, certifié, Label Rouge, bio), B viande cultivée, C substituts — pour **un kg de protéine comestible**, lorsque chaque chiffre passe par une chaîne de conversion explicite (`comparison_framework.md`) ?

**Sources.** 22 sources nouvelles (SRC-K-0001 à SRC-K-0022), dont 21 externes (la 22e est le modèle lui-même, SRC-K-0019) et 7 non anglophones (33 % des externes : fr ×3, pt ×2, ja, de) ; 19 externes lues en texte intégral et 2 par sections. Elles complètent les lignes existantes des agents E, N, A, C, X et, pour les DIAAS et quelques ACV de la voie C, celles que l'agent S enregistrait en parallèle (Q-S-…, non encore fusionnées). 56 affirmations (EV-K-0001 à EV-K-0056) et 189 mesures (Q-K-0001 à Q-K-0189) : 124 sorties de modèle (dont 57 du modèle K et 67 issues des ACV/TEA lues), 15 hypothèses `model_assumption` (dont 8 de l'agent K), 19 estimations publiées, 14 mesures, 8 statistiques, 8 déclarations d'entreprises.

**Modèle.** Le script lit toutes les tables `agents/*/quant.csv` ; il ne contient aucune donnée en dur hormis des constantes d'unités (1 lb = 0,4536 kg ; 1 kWh = 3,6 MJ). Chaque hypothèse est elle-même une ligne Q (Q-K-0122 à Q-K-0128, Q-K-0186). Trois scénarios (prudent / intermédiaire / optimiste) bornent l'étendue des sources, pas une probabilité. Une analyse de sensibilité un-facteur-à-la-fois identifie les facteurs déterminants.

**Limites d'accès.** CIQUAL (ANSES) en maintenance : teneurs françaises en protéines remplacées par USDA, TACO et la table japonaise. Leinonen 2012 (Royaume-Uni, standard/plein air/bio), Prudêncio da Silva 2014 (France/Brésil, Label Rouge), Upcraft 2021 (mycoprotéine) et Sauveur 1997 (Label Rouge) : identifiés mais PDF bloqués (403 ou dépôt fermé). Série ICPFrango de l'Embrapa : page dynamique illisible. Aucune source primaire chinoise ou hispanophone exploitable (11 requêtes, journal). L'étude AVEC/Wageningen 2026 n'a pas été trouvée.

**Avertissement transversal.** Les coûts mélangent des années 2017-2025 sans correction d'inflation ; les indicateurs d'énergie ne sont pas homogènes (ressources fossiles EF pour A, demande d'énergie totale pour B, CED ou électricité pour C) ; les périmètres diffèrent (porte de ferme ou d'abattoir, porte d'usine, détail) et sont signalés ligne par ligne dans `results.md`.

## 2. Facteurs de conversion de la voie A (lacune « chaîne aliment → protéine comestible »)

### 2.1 Teneur en protéines de la viande crue
Les tables officielles donnent 21,4 g/100 g pour la viande de poulet crue sans peau (USDA, EV-K-0018, Q-K-0046), 20,6 g pour le poulet entier sans peau cru (TACO, EV-K-0019, Q-K-0049), 22,5 g pour le filet (USDA, Q-K-0047) et 23,2 g pour la viande blanche (Q-K-0123). La table japonaise montre un point méthodologique décisif : le même filet contient 23,3 g de protéines « N × facteur » mais 19,2 g en somme d'acides aminés (EV-K-0020, Q-K-0052, Q-K-0053), soit un rapport de 0,82 (Q-K-0182). **Changer de définition de la protéine déplace tous les résultats « par kg de protéine » de 18 %**, davantage que l'écart de rendement entre souches standard (EV-K-0049).
Aucune donnée crue par système n'existe ; la TACO montre seulement qu'un poulet fermier « caipira » cuit est plus riche en protéines (29,6 contre 25,0 g/100 g) par moindre humidité (Q-K-0051). L'hypothèse d'une teneur identique entre systèmes est donc marquée (Q-K-0123).

### 2.2 Rendement en viande désossée
| Système | Prudent | Intermédiaire | Optimiste | Base |
|---|---|---|---|---|
| Standard | 41,4 % | 43,1 % | 47 % | WUR 1397 (objectifs sélectionneurs, Q-K-0064 + Q-K-0065) ; Ross 308 (Q-N-0014) ; Laisse 2018 (Q-N-0035) |
| Certifié (ECC, Beter Leven, certifié) | 31,9 % | 32,5 % | 35,3 % | BLS (Q-K-0066) ; filet JA757 mesuré (Q-K-0077) + cuisse BLS (hypothèse Q-K-0122) |
| Label Rouge / bio | 30,2 % | 30,6 % | 30,6 % | filet S757N mesuré (Q-K-0076) + cuisse BLS (hypothèse) |

Les mesures directes montrent l'ampleur de l'écart : le filet représente 25,0 % du poids vif d'un Ross 308 contre 19,2 % d'un Beter Leven (EV-K-0026), et 14,1-14,5 % d'une souche Label Rouge S757N à 85 jours (EV-K-0027) ; dans un essai américain, il fait 28 % de la carcasse en conventionnel contre 15 % en croissance lente, dont l'ossature est plus lourde (EV-K-0028). **Aucune donnée publiée de viande désossée totale n'a été trouvée pour les souches Label Rouge ou bio** : le rendement de cuisse est emprunté au BLS (lacune).
Il en résulte 0,085-0,109 kg de protéine comestible par kg de poids vif en standard, 0,066-0,082 en certifié et 0,062-0,071 en Label Rouge/bio (`results.md` §1).

### 2.3 CT-10 résolue (type B)
La protéine de l'animal entier (181 g/kg PV, Q-N-0034) vaut 1,96 fois la protéine comestible (92 g/kg PV) ; le prix de 4,6 USD/kg de protéine « animal entier » (EV-A-0042) correspond ainsi à ≈ 9,0 USD/kg de protéine comestible, dans la plage du modèle (EV-K-0051, Q-K-0181). L'écart de CT-10 n'est pas une contradiction mais une **différence de base** ; la base « protéine comestible » est retenue pour comparer des produits.

## 3. Coûts du poulet après 2017 (KG-X02)

Nouveaux points (tous convertis au kg de protéine comestible, `results.md` §2) :
- **UE, six pays, 2021** (Wageningen, exploitation type) : 89,7-95,5 c€/kg vif en conventionnel et 106,6-114,0 en ECC (EV-K-0022) ; abattage 27-40 c€/kg carcasse ; 166,5 c€/kg carcasse après abattage aux Pays-Bas (EV-K-0023). L'étude est commandée par une ONG favorable à l'ECC et repose sur des prix 2021, avant la flambée de 2022.
- **France 2022** (ITAVI, déjà enregistré par l'agent E) : 1,26 / 2,49 / 3,37 €/kg vif (standard / Label Rouge / bio) ; représentativité limitée (5 organisations en standard, petit échantillon bio).
- **États-Unis 2023** (budget d'entreprise) : 0,52 USD/lb vif en conventionnel grande échelle, 0,64 en moyenne échelle, 1,92 en pâturage (EV-K-0024) ; modèle « éleveur acheteur d'aliment », éloigné de l'intégration réelle.
- **Brésil 2025** (Embrapa) : 4,60 R$/kg vif (Q-E-0032) ; IC national 1,7 en 2020 (EV-K-0025).
Aucune série chinoise, espagnole ou de l'agri benchmark n'a été obtenue.

| Cas (coûts imputés à 100 % à la viande désossée) | Coût / kg de protéine comestible | USD de l'année |
|---|---|---|
| UE 2017, standard (Q-K-0129) | 8,9-12,8 €2017 | 10,1-14,5 |
| UE six pays 2021, standard (Q-K-0130) | 10,0-14,6 €2021 | 11,9-17,3 |
| France 2022, standard (Q-K-0131) | 14,1-18,1 €2022 | 14,9-19,0 |
| États-Unis 2023, standard, hors abattage (Q-K-0132) | 10,5-13,4 USD2023 | 10,5-13,4 |
| Brésil 2025, hors abattage (Q-K-0133) | 42-54 BRL2025 | 7,6-9,7 |
| Pays-Bas 2021, ECC (Q-K-0134) | 16,2-21,6 €2021 | 19,1-25,5 |
| France 2022, Label Rouge (Q-K-0137) | 38,8-44,2 €2022 | 40,9-46,5 |
| France 2022, bio (Q-K-0138) | 51,2-58,4 €2022 | 53,9-61,5 |
| États-Unis 2023, pâturage, hors abattage (Q-K-0136) | 59,5-67,9 USD2023 | 59,5-67,9 |

Deux résultats se dégagent. D'abord, la plage UE 2017 de l'agent K (8,9-12,8 €) recoupe celle de l'agent E (8,3-14,1 €, Q-E-0070) obtenue avec d'autres combinaisons d'hypothèses : la référence est robuste. Ensuite, **le surcoût du bien-être est multiplié par la conversion** : +22 % par kg vif pour l'ECC aux Pays-Bas, mais ≈ +50 % par kg de protéine comestible, parce que le rendement désossé baisse (EV-K-0040) ; en France, Label Rouge et bio coûtent 2,5 et 3,3 fois le standard par kg de protéine (EV-K-0041, Q-K-0180).

## 4. Tableau final par kg de protéine comestible (KG-X01, RQ-X1/RQ-X2)

Plages toutes sources et scénarios confondus (`results.md` §0 ; Q-K-0139 à Q-K-0170).

| Ligne | Coût (USD de l'année) | GES (kg CO2-eq) | Énergie (MJ) | Eau bleue (L) | Surface (m2·an) | Nature dominante |
|---|---|---|---|---|---|---|
| A standard, porte d'abattoir | 7,6-19,0 | 11-44 | 94-137 (fossile) | 200-1 654 | 20-47 | estimations publiées, statistiques ; ACV (sorties de modèle) |
| A standard, produit au détail | — | 17,5-57 | 168-306 | — | 19-71 | ACV, méta-analyse |
| A certifié (ECC, Beter Leven) | 19,1-25,5 | 19-55 | n.d. | 2 740* | 46-66 | estimations publiées ; ACV |
| A Label Rouge | 40,9-46,5 | 30-39 | 234-303 | 2 740* | n.d. | statistiques + hypothèses |
| A bio / pâturage | 53,9-67,9 | 38-73 | 305-396 | 5 780* | n.d. | statistiques, modèle ; ACV |
| B, base publiée (21 % de protéines ; 18-25 % dans les ACV) | 9-287 | 10-79 (intrants purifiés : 984-8 378) | 588-1 467 | 168-311 | 6,8-10 | sorties de TEA/ACV |
| B, recalcul à 9 % de protéines | 22-670 | 28-159 (2 733-16 756) | 1 633-2 933 | 467-622 | 19-20 | sorties de modèle + hypothèse de proportionnalité |
| C ingrédients | 1,9-29,6 | 0,8-21 | 98-370 | 246 (tofu) | 8,7-34 (SCP PV < 0,83) | prix de marché, TEA, ACV, déclarations |
| C produits (analogues de soja) | n.d. | 7,7-11,4 | 284-344 | n.d. | n.d. | ACV + hypothèse de composition |

\* classe de système de Mekonnen & Hoekstra associée par hypothèse (Q-K-0127).

### 4.1 Coût
- **Voie A** : 7,6-19 USD/kg de protéine pour le standard, 19-26 pour le certifié, 41-47 pour le Label Rouge, 54-68 pour le bio ou le pâturage.
- **Voie B** : 9-287 USD avec l'hypothèse de 21 % de protéines, 22-670 USD avec la mesure de 9 % (EV-K-0042). Seuls deux scénarios restent à moins de cinq fois le poulet standard : Risner « limites levées » (21,7 USD à 9 %) et CE Delft 2030 « tous leviers » (71 USD). Le scénario intermédiaire du modèle E/X (225 USD) vaut 13 à 18 fois le standard, mais **5 fois le Label Rouge et 4 fois le bio** : la cible de parité réaliste de la voie B est la viande sous signe de qualité, pas le poulet standard. Pour égaler le standard, la biomasse humide devrait coûter au plus 0,87-1,71 USD/kg à 9 % (2,0-4,0 à 21 %), sous le plancher de 6 USD/kg du scénario optimiste (EV-K-0043, Q-K-0171 à Q-K-0175).
- **Voie C** : l'isolat de soja (prix de marché 1,9-8,5 USD/kg de protéine) et l'e-SCP modélisée (6,2-6,9 USD) sont sous le poulet standard ; la mycoprotéine (29,6 USD/kg de protéine, TEA Risner 2023) le dépasse (EV-K-0031, EV-K-0033). **Le chiffre de 3,55 USD/kg de mycoprotéine (Q-E-0066) est retrouvé dans sa source primaire : il porte sur le kg de mycoprotéine humide (~73 % d'eau)** (EV-K-0032), ce qui réduit KG-C06. Aucun coût de produit fini n'existe ; le seul indicateur est une prime de prix de +77 % au poids des viandes végétales sur la viande conventionnelle aux États-Unis en 2023 (EV-K-0037).

### 4.2 GES
Avec LUC, le poulet standard émet 30-44 kg CO2-eq/kg de protéine à la porte de l'abattoir aux Pays-Bas, 16-23 en France (AGRIBALYSE, soja ecoinvent 3.9) et 35-44 dans GLEAM (EV-K-0001, EV-K-0004) ; sans LUC, 11-16. Label Rouge 30-39, bio 38-73 (EV-K-0013). La viande cultivée se situe à 10-79 kg sur la base publiée et **28-159 à 9 % de protéines** ; avec des intrants de qualité pharmaceutique, 984-16 756 (EV-K-0044). Concrètement, la viande cultivée à énergie renouvelable (≈ 31 kg à 9 %) ne bat le poulet que si l'on compte le LUC du soja ; avec le mix électrique mondial (≈ 159), elle dépasse tous les systèmes A.
Côté C, les ingrédients émettent 0,8-21 kg CO2-eq/kg de protéine (concentré de soja 0,8 ; pois 4 ; FeedKind 2,2-8,0 ; protéine microbienne H2 11,6-13 ; tofu 9-21) et les analogues de soja 7,7-11,4, contre 17,5-24 pour le poulet de détail sur la même base AGRIBALYSE/RIVM (EV-K-0046).

### 4.3 Énergie, eau, surface
- **Énergie** : la viande cultivée demande 4 à 30 fois l'énergie fossile du poulet standard par kg de protéine (EV-K-0045). Résultat moins attendu : **les analogues végétaux de soja consomment autant d'énergie non renouvelable par kg de protéine que le filet de poulet** (284-344 contre 306 MJ, toutes étapes), la transformation représentant ~60 % de leur total (EV-K-0017, EV-K-0046).
- **Eau bleue** : les sources divergent d'un facteur 8 pour le poulet (1 654 L/kg de protéine selon Mekonnen & Hoekstra, classe industrielle ; 200 L selon CE Delft), si bien que l'ordre A/B est **indécidable** (EV-K-0047, nouvelle contradiction proposée). Les indicateurs pondérés par la rareté (AGRIBALYSE, ifeu) ne sont pas des volumes et sont présentés à part.
- **Surface** : B (6,8-20 m2·an/kg de protéine) et C (tofu 16-22, soja 8,7) restent sous A standard (20-47) même à 9 % de protéines ; le Beter Leven en demande 46-66 (EV-K-0048). Pour le Label Rouge et le bio, seules des surfaces en points AGRIBALYSE existent (×1,3 et ×2,6 le conventionnel) : pas de m2 comparables.

### 4.4 Troisième base : protéine de qualité équivalente
En divisant par le DIAAS in vitro tronqué à 100 % (hypothèse Q-K-0186 ; DIAAS de l'agent S), les analogues de soja passent à 11,8-21,9 kg CO2-eq par kg de protéine de qualité équivalente, rejoignant le bas de la plage du poulet (19-24). La protéine bactérienne H2 voit son coût (12-14 USD) et ses GES (23-26) presque doubler (DIAAS 51 %), alors que la mycoprotéine est peu affectée (DIAAS 83-97 %) (EV-K-0056, Q-K-0187 à Q-K-0189). Le DIAAS de la biomasse de poulet cultivée est inconnu.

## 5. Ce qui détermine réellement le résultat (sensibilité)

| Grandeur | Facteur | Rapport max/min | Réf. |
|---|---|---|---|
| Coût A standard (UE 2021) | définition de la protéine (acides aminés vs N×facteur) | 1,21 | Q-K-0176 |
| | rendement en viande désossée | 1,14 | |
| | teneur en protéines de la viande | 1,13 | |
| | coût d'abattage (27-40 c€) | 1,08 | |
| | coût d'élevage entre pays de l'UE | 1,05 | |
| Coût A, choix du système (standard → bio) | | 3,3 | Q-K-0180 |
| Coût B (modèle E/X) | coût de la biomasse (scénario) | 7,9 | Q-K-0177 |
| | teneur en protéines (8,8-25 %) | 2,8 | |
| GES A standard (Pays-Bas) | inclusion du LUC | 2,7 | Q-K-0178 |
| | allocation (88-100 %) | 1,14 | |
| GES B | énergie et pureté des intrants | 539 | Q-K-0179 |

**Lecture.** (1) Pour A, les écarts de coût entre pays européens comptent moins que les conventions de conversion ; seul le changement de système multiplie le coût. (2) Pour B, le coût de la biomasse (donc milieu et capital, EV-E-0059) domine, suivi de la composition, une donnée qui n'a jamais été mesurée pour le poulet (KG-B01). (3) Pour les GES de A, le LUC du soja domine : la même graine brésilienne vaut 1,6, 2,6 ou 4,5 kg CO2-eq/kg selon la base de données (EV-K-0053), ce qui suffit à expliquer CT-15 et l'écart entre AGRIBALYSE et Wageningen. (4) Pour les GES de B, la pureté des intrants et l'énergie dominent de deux ordres de grandeur (CT-09).

## 6. Contradictions

- **CT-10** — résolue : différence de base (animal entier vs protéine comestible, rapport 1,96 ; EV-K-0051).
- **CT-01** — étendue : trois études de la voie B supposent environ 20 % de protéines (Humbird 21 %, CE Delft 18-25 %, Mazac 19 % ; EV-K-0011, EV-K-0054) contre 9 g/100 g mesurés sur la caille ; à impact par kg inchangé, les GES, l'énergie, l'eau et la surface de B par kg de protéine sont multipliés par 2 à 2,8 (EV-K-0052). Cette proportionnalité reste une borne : une biomasse plus aqueuse pourrait réduire l'impact par kg.
- **CT-09** — précisée : à 9 % de protéines, la viande cultivée de Sinke (énergie renouvelable sur les scopes 1-2 et une partie du scope 3) émet ≈ 31 kg CO2-eq/kg de protéine contre 11-16 pour le poulet sans LUC ; l'écart avec Risner (intrants purifiés) atteint un facteur 539. L'asymétrie de périmètre de Risner (berceau-porte vs comparateur au détail) est maintenue.
- **CT-15** — précisée : le classement des systèmes s'inverse avec ou sans LUC aux Pays-Bas (EV-K-0029). En France, AGRIBALYSE place le Label Rouge au-dessus du standard malgré une part LUC plus faible (0,41 contre 0,57 kg CO2-eq/kg vif, EV-K-0013). La variation des facteurs du soja entre bases (×2,8, EV-K-0053) en est le premier déterminant.
- **CT-20** — non traitée sur le fond, mais la base « protéine comestible » (92 g/kg PV) et la base « animal entier » (181 g/kg PV) diffèrent d'un facteur 2, ce qui contribue aux écarts d'efficience protéique entre Laisse et Mottet.
- **Nouvelle (proposée)** — eau bleue de la voie A : 1 654-5 780 L/kg de protéine (Mekonnen & Hoekstra) contre 200 L (référence CE Delft), soit l'ordre A/B qui s'inverse selon la source (EV-K-0006, EV-K-0009, EV-K-0047).
- **Interne à AGRIBALYSE** : la moyenne bio (2,98 kg CO2-eq/kg vif) est inférieure aux deux systèmes bio détaillés (4,23-4,47), sans explication dans le tableur (Q-K-0039).

## 7. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Fonctionne.** Le poulet standard reste la protéine animale la moins chère par kg de protéine comestible (7,6-19 USD) et, sans LUC, l'une des moins émettrices (11-16 kg CO2-eq). Les ingrédients végétaux bruts (soja, pois) dominent toutes les voies en coût, GES et surface.
**Échoue.** Aucun scénario publié de viande cultivée n'approche le poulet standard une fois corrigé à 9 % de protéines, hors Risner « limites levées ». Pour l'énergie, B est la voie la plus intensive.
**Reste à inventer ou à mesurer.** (a) La composition de la biomasse de poulet cultivée (KG-B01) ; (b) le rendement en viande désossée des souches Label Rouge/bio ; (c) des coûts de produits finis de la voie C ; (d) une ACV de la viande cultivée qui tienne compte de la teneur réelle en protéines ; (e) une eau bleue harmonisée pour le poulet.

## 8. Pistes d'innovation

**K-1. Viande cultivée « premium » plutôt que « commodité ».**
*Problème* : la parité de coût avec le poulet standard exige une biomasse ≤ 0,9-1,7 USD/kg (9 % de protéines). *Solutions actuelles* : les TEA visent le standard. *Insuffisance* : le plancher OPEX optimiste est de 6 USD/kg. *Preuves d'une autre approche* : le Label Rouge et le bio coûtent 41-68 USD/kg de protéine comestible (Q-K-0137, Q-K-0138), soit la zone du scénario CE Delft 2030 (71) et du modèle E/X optimiste (85). *Hypothèse* : un produit cultivé positionné face au poulet sous signe de qualité (ou hybride avec ces viandes) atteindrait la parité avec ≤ 4-6 USD/kg de biomasse humide. *Validation* : TEA paramétrée sur la composition mesurée (Kjeldahl + humidité) d'une biomasse de poulet en suspension. *Succès* : coût ≤ 45 USD/kg de protéine avec des hypothèses démontrées en pilote. *Échec* : > 100 USD. *Risques* : interdictions réglementaires (Italie, Floride, Texas) et acceptabilité.

**K-2. Mesurer avant de modéliser la composition de la biomasse.**
*Problème* : ±2,8 sur tous les indicateurs de B par kg de protéine (EV-K-0052). *Hypothèse* : la protéine de biomasse de fibroblastes de poulet en culture dense est < 12 % de la masse humide. *Expérience* : Kjeldahl/Dumas, humidité, lipides et acides aminés (somme) sur 3 lots × 2 milieux. *Succès* : coefficient de variation < 10 %. *Coût* : faible (≈ 10-20 k€). Effet attendu : réduction directe de KG-B01 et de CT-01.

**K-3. Protéine de qualité équivalente comme unité de comparaison.**
*Problème* : les analogues végétaux perdent la moitié de leur avantage GES une fois ajustés au DIAAS (EV-K-0056). *Hypothèse* : des formulations complémentaires (pois + riz, ajout de mycoprotéine) portent le DIAAS des analogues au-delà de 80 % et rétablissent un avantage d'un facteur 2. *Validation* : DIAAS in vivo (porc) de trois formulations, combiné à leur ACV AGRIBALYSE. *Succès* : ≤ 12 kg CO2-eq/kg de protéine de qualité équivalente.

**K-4. Soja à faible LUC : levier commun aux voies A et B.**
*Fondement* : le LUC fait varier les GES du poulet d'un facteur 2,7 (Q-K-0178) et le soja brésilien de 1,6 à 4,5 kg CO2-eq/kg selon la base (EV-K-0053) ; les milieux de la voie B à base d'hydrolysat de soja (CE Delft : 75 % des acides aminés) héritent du même facteur. *Hypothèse* : exiger un soja « cut-off 2008 » réduit davantage les GES par kg de protéine du poulet standard que le passage au Label Rouge. *Validation* : ACV AGRIBALYSE avec les jeux « non associés à la déforestation » (déjà disponibles, SRC-K-0020).

## 9. Lacunes réduites et restantes

- **KG-X01** — largement réduite : tableau homogène coût, GES, énergie, eau et surface par kg de protéine comestible pour A (4 systèmes), B (12 scénarios publiés, bases 21 % et 9 %) et C (ingrédients et produits), avec la nature de chaque chiffre ; restent les coûts de produits de la voie C et l'énergie et la surface du Label Rouge et du bio en unités physiques.
- **KG-X02** — réduite : coûts 2021 (six pays de l'UE, conventionnel et ECC), 2022 (France), 2023 (États-Unis), 2025 (Brésil) ; restent la Chine, l'Amérique latine hors Brésil et l'étude AVEC 2026 (non trouvée).
- **KG-C06** — réduite : base du chiffre de 3,55 USD/kg identifiée (Risner 2023, kg humide) ; TEA indépendante de la SCP H2 encore manquante.
- **KG-C01** (côté usage) — les DIAAS in vitro de l'agent S sont intégrés comme troisième base.

## 10. Recherches restantes prioritaires

1. Composition chimique (protéines, eau, lipides) d'une biomasse de **poulet** cultivée : dossiers FDA (CCC 000002, CCC 000039 ; agent B).
2. Rendement en viande désossée totale des souches Label Rouge/bio (ITAVI, SYSAAF, INRAE) et coûts ITAVI 2023-2024.
3. Table CIQUAL (à la réouverture) pour remplacer les teneurs USDA dans la chaîne française, et composition des analogues AGRIBALYSE.
4. Leinonen 2012 et Prudêncio da Silva 2014 (énergie et surface par système standard / plein air / bio / Label Rouge) via une bibliothèque.
5. Valeurs numériques GLEAM 3 (tableau de bord FAO) par kg de protéine et par région.
6. Coûts de produits finis de la voie C (TEA d'extrusion humide, KG-C02) et prix au détail du poulet pour convertir la prime GFI en valeur absolue.
