# Handoff — Agent E (ingénierie, économie, industrialisation, réglementation) — 2026-10-25

Rapport : `research/reports/industrialization.md` · Modèle : `research/agents/E/models/pathway_cost_model.py` (+ `results.md`, `results.json`) · Journal : `search_log.md` (81 requêtes, 8 langues) · Terminologie : `terminology.md` (39 entrées).
Bilan : 42 sources E (SRC-E-0001…0042) + 4 réutilisées (SRC-X-0001, SRC-A-0024, SRC-A-0011, SRC-P-0004) ; 59 affirmations (EV-E-0001…0059) ; 72 mesures (Q-E-0001…0072).

## 1. Résultats clés
- **Le poulet conventionnel est la seule voie avec des coûts statistiques.** En 2017 : 63-65 c€/kg vif au Brésil et aux États-Unis, 78,6-86,5 c€ dans l'UE ; l'aliment représente environ 60-65 % (EV-E-0015, EV-E-0016, Q-E-0022…0026). En France en 2022 : standard 1,26 €, Label Rouge 2,49 €, bio 3,37 €/kg vif (EV-E-0019, Q-E-0029…0031).
- **Les TEA de la viande cultivée divergent de cinq ordres de grandeur** (Humbird 37/51 $/kg ; Risner 437 000 → 1,95 $/kg ; CE Delft 22 421 → 6,43 $/kg ; Negulescu 17-35 $/kg). Le milieu représente 40-99 % du coût selon les études (EV-E-0001, EV-E-0005, EV-E-0022, EV-E-0012, EV-E-0042).
- **Les chiffres de presse remontent aux mêmes TEA et sont parfois déformés.** CE Delft 5,66 $/kg (avant corrigendum) devient 6,43 $/kg après, et « 2,50 $/kg » dans la presse espagnole (EV-E-0022, EV-E-0058).
- **Modèle E (calibré sur Humbird à ±1 $/kg)** : 36 / 97 / 287 $/kg de protéine cultivée (optimiste / intermédiaire / prudent), contre 8,3-14,1 €2017 (9,3-15,9 $2017) par kg de protéine pour le poulet standard UE. La parité exige une biomasse humide à 3,3 $/kg ou moins, alors que milieu + autres OPEX seuls font 6 $/kg dans le scénario optimiste (EV-E-0059, Q-E-0067…0072).
- **ACV** : la viande cultivée rejoint au mieux le poulet « ambitieux » 2030 (2,8 contre 2,7 kg CO2-eq/kg) avec 100 % d'énergie renouvelable ; 14,3 avec le mix mondial ; 246-1 508 avec des intrants purifiés (EV-E-0024, EV-E-0006). Pour le poulet, le LUC du soja domine et inverse le classement des systèmes (EV-E-0008, EV-E-0009).
- **Industrialisation** : l'usine Believer (≈ 150 M$, environ 12 kt/an annoncées, approuvée par l'USDA) n'a jamais produit ; l'entreprise a fermé en décembre 2025 (EV-E-0047). Vague de fermetures en 2024-2025 (EV-E-0048). Échelle réelle ≈ 10³ L (EV-E-0050, EV-E-0055).
- **Réglementation** : textes officiels lus pour l'UE, l'Italie, la Floride, le Texas, la FDA, Singapour, FSANZ, le Brésil et le bac à sable britannique (EV-E-0027…0038, EV-E-0052). À Singapour, toute modification du milieu ou de la lignée impose une nouvelle approbation (EV-E-0035) ; FSANZ crée une catégorie dédiée (EV-E-0036).

## 2. Contradictions repérées
- Pasitka : 6,2 $/lb dans le résumé (EV-E-0014) contre 23,26-27,24 $/kg selon la revue (EV-E-0042, Q-E-0045). Base probablement différente (hybride ou cellules).
- Pasitka : 43 % m/v (EV-E-0013) contre plafond physique de 258 g/L chez Humbird (EV-E-0003).
- CE Delft (EV-E-0022) contre Humbird (EV-E-0001) : qualité d'hygiène et coût du capital.
- Sinke (EV-E-0024) contre Risner (EV-E-0006) : pureté des intrants et énergie.
- Mostert : l'ordre des systèmes de poulet dépend du LUC (EV-E-0008 contre EV-E-0009).
- Consultation FDA (EV-E-0034) contre interdictions d'États (EV-E-0032, EV-E-0033).
- Poulet ≈ 4,6 $/kg de protéine sèche (EV-A-0042, animal entier, prix départ ferme) contre 8,3-14,1 €2017/kg de protéine pour la viande désossée (Q-E-0070) : base de calcul à harmoniser.
- Mycoprotéine : EV-A-0050 contre EV-A-0049 (agent A).
- *Erratum* : le champ `contradicts` de EV-E-0058 a été corrigé en EV-E-0022 via `kb.py set`.

## 3. Lacunes (cherché sans succès)
- Pas d'étude internationale des coûts du poulet après 2017 (l'étude AVEC/Wageningen 2026 n'a pas été trouvée) ; USDA ERS et agri benchmark non obtenus ; pas de série latino-américaine récente.
- Pas de TEA publique d'extrusion ni de mycoprotéine (la réf. 102 de Bry-Chevalier n'a pas été identifiée) ; capacités de Quorn et de Calysseo non trouvées.
- Pas d'ACV spécifique au poulet cultivé ; pas de TEA chinoise, japonaise ou coréenne.
- Pas de données publiques de L de milieu par kg, de taux de contamination ni d'utilisation réelle.
- Textes primaires MFDS, NHC, OSAV (Suisse), ministère de la Santé israélien et registre OpenEFSA non lus ; lois de l'Alabama, du Mississippi, du Montana, de l'Indiana, du Nebraska et du Dakota du Sud non vérifiées sur sources officielles.

## 4. Questions pour d'autres agents
- **→N** : peux-tu fournir des rendements mesurés en viande désossée et des teneurs en protéines de la viande crue pour le standard, le Label Rouge et le bio ? Le modèle E applique au Label Rouge et au bio le rendement Ross 308 (Q-N-0014) faute de mieux. As-tu le coût d'un aliment « soja à faible LUC » ou à base d'insectes (règlement 2021/1372, EV-E-0029) ?
- **→C** : as-tu des données mesurées de consommation de milieu (L/kg) en perfusion pour des cellules de poulet, la définition de « 43 % m/v » (Q-C-0004) et des volumes de lots réels (UPSIDE, GOOD Meat, Vow) ? Le Meatly à 0,22 £/L (SRC-C-0039) est-il une mesure ?
- **→A** : quel est le coût ou le prix des matrices végétales pour calculer le coût d'un hybride (piste E-4) ? Disposes-tu d'une donnée d'énergie industrielle de l'extrusion (même non publique) ou d'une ACV primaire de Quorn ?
- **→P** : peux-tu confirmer le statut actuel de Glenview (SRC-P-0009) et du projet ABEC (SRC-P-0007/8), les capacités réelles de Vow et de Mosa Meat, et chercher s'il existe des brevets sur l'élimination de NH3 et le recyclage de milieu (piste E-1) ?
- **→X (coordinateur)** : le bug CJK de kb.py m'avait forcé à ajouter des titres anglais entre crochets dans SRC-E-0034, SRC-E-0035 et SRC-E-0036 ; à harmoniser si nécessaire. Faut-il fixer une base commune « kg de protéine de viande comestible » pour RQ-X1/X2 ?

## 5. Pistes d'innovation
- **E-1 Litre de milieu par kg** : la perfusion avec recyclage et élimination de NH3 ramènerait la consommation à 10 L/kg ou moins ; essai à 2-10 L sur 21 jours ; succès = au moins 80 % de la productivité du témoin.
- **E-2 Aseptie de qualité alimentaire sans salle blanche** : moins de 2 % de lots contaminés sur 50 lots ou plus à 200-1 000 L ; enjeu d'environ 18 $/kg dans la tornade.
- **E-3 Hydrolysat de tourteau de soja de qualité milieu** : goulet commun aux voies A et B ; au moins 70 % des acides aminés, 10 passages, moins de 3 $/kg.
- **E-4 Hybrides à 10-20 % de cellules** : seuil sensoriel et coût de mélange ; risque réglementaire en France et en Italie.
(Détails : rapport, § 12.)

## 6. Recherches restantes prioritaires
1. Texte intégral de Pasitka 2024 (base du coût, L/kg, m/v).
2. Textes intégraux de Negulescu 2023, Garrison 2022 et Goodwin 2024 ; TEA primaire de la mycoprotéine (Upcraft 2021, etc.).
3. Coûts du poulet 2023-2025 (étude AVEC 2026, ITAVI, USDA, agri benchmark ; Embrapa après les élections).
4. Registre OpenEFSA, OSAV, MFDS (projet du 30/06/2026), NHC, Israël ; lois des États américains sur textes officiels.
5. ACV primaires de la mycoprotéine et de Solein ; FAO GLEAM ; base protéine harmonisée avec N et A.

## 7. Limites d'accès rencontrées
- EUR-Lex : HTTP 202 vide (contourné par publications.europa.eu). Pages Springer et Nature : authentification (Sinke lu via le PDF éditeur hébergé par CE Delft ; Pasitka et Goodwin en résumé seulement).
- USDA-FAS/GAIN, Meat+Poultry, Wilson Times : 403. PDF de l'ANVISA : page HTML (copie municipale utilisée). Embrapa : contenu masqué (restrictions électorales 2026). Page statutaire de Floride : chargement dynamique (site alternatif leg.state.fl.us).
- Crossref via search.py : erreurs 400 (API directe utilisée ; outil réparé depuis). J-STAGE : requêtes à plusieurs termes sans résultat (outil corrigé depuis). Références EPMC de Bry-Chevalier incomplètes.
