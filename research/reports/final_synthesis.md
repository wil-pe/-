# Synthèse — Chicken Muscle Research Lab

> **Version intermédiaire v0.1 (2026-10-25), fin des phases 3, 5 et 6.** Elle sera révisée après les approfondissements de la phase 4 (agents B, M, S, R, K en cours) et la comparaison de la phase 7.
> Chaque affirmation renvoie aux identifiants de la base (`EV-…` affirmation, `Q-…` mesure, `SRC-…` source, `CT-…` contradiction, `KG-…` lacune, `INN-…` piste). La nature de chaque chiffre est indiquée : **mesuré**, **statistique**, **déclaration d'entreprise**, **sortie de modèle**.

## 1. Sur quoi repose cette synthèse

- **Corpus** : 308 sources uniques (dont 44 brevets), 394 affirmations, 434 mesures. Lecture réelle : 150 sources en texte intégral (49 %), 83 par sections (27 %), 59 en résumé seulement (19 %), 16 en métadonnées ou par une source secondaire (5 %).
  - Bases réellement consultées : PubMed, Europe PMC, Crossref, Consensus, J-STAGE, HAL, theses.fr, archive.org, OSTI, Google Patents, sites officiels FDA/SFA/FSANZ/UE/Italie/États américains.
  - Bases bloquées : OpenAlex, Semantic Scholar, Google Scholar, Espacenet, PATENTSCOPE, CAB, CNKI, SciELO.
- **Contrôle** :
  - toutes les références ont été résolues automatiquement (DOI/PMID) : aucune n'est inventée ;
  - 55 affirmations clés ont été contre-vérifiées par des vérificateurs indépendants : aucun chiffre faux, mais 44 % de réserves sur la portée ou l'attribution, toutes corrigées (`coordination/verification/summary.md`).
- **Biais connus** :
  - 85 % des sources sont en anglais ;
  - les articles clés de la voie B (Pasitka 2023–2025, *Nature Food*) ne sont lus qu'en résumé ;
  - les brevets ne sont qu'un échantillon.
- **Ce n'est pas** une revue exhaustive mondiale.

## 2. Réponses provisoires aux questions transversales

### RQ-X1 — Coût mesuré vs projeté
| Voie | Ce qui est connu | Nature | Réf. |
|---|---|---|---|
| A — poulet standard | 0,63 (Brésil) – 0,65 (États-Unis) – 0,825 (moyenne UE) €/kg vif en 2017 ; 1,264 €/kg vif en France en 2022 (Label Rouge 2,485 ; bio 3,366). L'aliment représente ≈ 57–66 % du coût en élevage (UE 2017). | estimations publiées / statistique | Q-E-0022 à Q-E-0024, Q-E-0029 à Q-E-0031, EV-E-0015, EV-E-0019 |
| A — par kg de protéine | 8,3–14,1 €2017/kg de protéine de viande désossée (UE standard) | sortie du modèle E sur données statistiques | Q-E-0070 |
| B — viande cultivée | **Aucun coût industriel mesuré.** Les TEA vont de 6 USD/kg à plus de 400 000 USD/kg de biomasse humide selon les hypothèses (Humbird 37–51 ; CE Delft 6,43 ; Risner jusqu'à 437 000). Le modèle E, recalculé avec la composition mesurée (9 % de protéines), donne **85 / 225 / 670 USD par kg de protéine** (optimiste / intermédiaire / prudent). | sorties de modèles | EV-E-0001, EV-E-0005, EV-E-0022, EV-X-0001, Q-X-0001 à Q-X-0003 |
| C — substituts | Ingrédients : isolat de soja 1,8–8,1 €/kg de protéine (prix de marché) ; protéine bactérienne (e-SCP) 5,5–6,1 €/kg de protéine en 2028 (modèle, avec conflit d'intérêts). Aucune TEA publique des produits finis (extrusion, mycoprotéine). | prix / sortie de modèle | Q-E-0065, Q-E-0041, KG-C06 |

**Conclusion provisoire** (confiance modérée sur le sens, faible sur les valeurs) :
- Sous les hypothèses démontrées à ce jour, **la protéine de poulet cultivée coûte un à deux ordres de grandeur de plus que celle du poulet standard**.
- La parité exigerait une biomasse humide à ≤ 1,4 USD/kg (≤ 3,3 USD/kg si l'on retient 21 % de protéines) (Q-X-0004). Or le seul plancher « milieu + autres frais d'exploitation » du scénario optimiste atteint déjà 6 USD/kg (EV-E-0059).
- Ce constat dépend surtout de deux inconnues : la composition réelle de la biomasse de poulet (KG-B01) et les litres de milieu par kg (KG-B04).

### RQ-X2 — Ressources par kg de protéine
- **GES** :
  - La viande cultivée en 2030 n'égale le poulet « ambitieux » (2,8 contre 2,7 kg CO₂-éq/kg de viande) que si l'énergie est renouvelable pour les scopes 1–2 et une partie du scope 3. Elle monte à 14,3 avec le mix électrique mondial (Q-E-0037 à Q-E-0039, EV-E-0024).
  - Avec des intrants purifiés de qualité pharmaceutique, elle atteint 246–1 508 kg CO₂-éq/kg (EV-E-0006, CT-09).
  - Pour le poulet, le changement d'usage des sols lié au soja domine le bilan (EV-E-0009, CT-15).
- **Énergie, eau, surface** sur base homogène : **non encore consolidées** (mission K en cours).

### RQ-X3 — Goulets partagés
La **protéine** est l'intrant commun des trois voies :
- tourteau de soja et SCP pour le poulet : une SCP méthanotrophe remplace le soja jusqu'à 12,5 % de la ration (EV-A-0014, EV-P-0060) ;
- acides aminés pour le milieu de culture, qui pèseraient ~76 % du coût du milieu selon un modèle sur milieu bovin (Q-P-0032) ;
- protéines texturées pour les substituts.

Trois ponts sont identifiés comme les moins explorés : hydrolysats « qualité milieu » issus de matières de l'alimentation animale (INN-01), plasma d'abattoir (INN-08), hybrides cellules + végétal (INN-07).

### RQ-X4 — Réglementation (état provisoire)
- **États-Unis** : 5 consultations FDA closes par une lettre *no questions*, dont 3 pour du poulet (UPSIDE 2022, GOOD Meat 2023, Believer 2025) (EV-E-0034). Ce ne sont pas des autorisations : l'USDA-FSIS intervient ensuite (EV-C-0001).
- **Interdictions** : Italie (loi 172/2023, y compris la production pour l'export, avec sanctions automatiques et extension aux financeurs, EV-E-0030), Floride (EV-E-0032), Texas 2025–2027 (EV-E-0033).
- **Singapour** : toute modification susceptible d'affecter l'évaluation (lignée, milieu) doit être soumise à la SFA (EV-E-0035), ce qui freine l'optimisation du milieu, principal levier de coût.
- **Analyse complète** : mission R en cours.

### RQ-X5 — Espaces d'innovation
Voir `innovation_opportunities.md`. Les 21 pistes y sont classées selon une grille explicite (impact, preuves, testabilité).

## 3. Voie A — optimiser l'élevage

**Ce qui fonctionne (preuves convergentes)**
- **La génétique domine** : à régime identique, l'IC 0–42 j passe de 2,88 (souche témoin de 1957) à 1,67 (Ross 308, 2005), soit −42 % d'après le tableau de Zuidhof 2014. Le résumé des auteurs, incohérent avec ce tableau, annonce −50 % (EV-N-0001).
- **Performances de terrain** : IC de 1,612 en France (2022, Q-N-0069) et de 1,70 lb/lb aux États-Unis (2025, Q-N-0016), contre un objectif commercial Ross de 1,531 (`company_claim`, Q-N-0011). La mortalité américaine atteint 5,95 % (Q-N-0018).
- **Conversion en protéine** : environ 61–64 g de protéine de viande par kg d'aliment en souche rapide, 32 g en Label Rouge (Q-N-0076, Q-N-0079 ; calculs de l'agent N). Le rapport protéine de viande / protéine ingérée plafonne vers 0,32 (Q-N-0081).
- **Régimes à basse protéine** : chaque point de protéine brute retiré coûte 1,2–1,9 % d'IC mais réduit l'azote excrété de 11–14 % (EV-N-0011, EV-N-0012). Le plancher se situe vers 17 % de PB en finition (EV-N-0019, EV-N-0020).

**Ce qui échoue ou déçoit**
- Protéase sur un régime déjà équilibré : effet limité à une phase, nul sur l'IC cumulé (EV-N-0032).
- Probiotiques en conditions sanitaires optimales : effet non reproduit (CT-22).
- Alimentation in ovo : pas de gain démontré à l'abattage (CT-23).
- Insectes et microalgues : bilan environnemental défavorable quand le substrat n'est pas un vrai déchet (EV-N-0058).

**Limites physiologiques**
- Selon un modèle, il ne resterait qu'environ 8 % d'énergie récupérable par la sélection (EV-N-0052).
- Les myopathies sont très répandues en Ontario : white striping 96 %, spaghetti meat 36 %, woody breast sévère 12 % (EV-N-0042).
- Les souches lentes consomment 14 à 28 % d'aliment en plus, à des poids et âges non identiques (EV-N-0054).

**Leviers prioritaires**
- INN-05 (efficience protéique nette) et INN-06 (plancher de PB) : preuves solides, testables en station expérimentale.
- INN-11 (nutrition des souches lentes) et INN-16 (fenêtre péri-éclosion).

## 4. Voie B — viande cultivée

**État réel (documents réglementaires primaires)**
- **Ce qui est vendu** : les trois poulets cultivés passés en consultation FDA sont des **biomasses de fibroblastes, pas du muscle** (EV-C-0001, EV-C-0006, EV-C-0009). Les produits vendus au détail contiennent 3 % (GOOD Meat 3, déclaration d'entreprise) ou 4 % de cellules (Chick Bites, aliment pour chien) (Q-C-0084, Q-C-0069).
- **Atout propre au poulet** : l'immortalisation spontanée de fibroblastes (lignées DF-1, Believer) permet la suspension sans sérum (EV-C-0008, EV-C-0010, EV-C-0015).
  - Cette facilité est disputée (CT-07).
  - DF-1, la lignée de GOOD Meat, est une lignée vaccinale publique (EV-P-0005).
- **Densités record** : 108 puis 130 × 10⁶ cellules/mL, au laboratoire, par une seule équipe, connues par le résumé seulement (Q-C-0001, Q-C-0003, CT-03).
- **Composition** : la seule biomasse aviaire analysée publiquement (caille) contient 9 g de protéines/100 g, contre 18,5 g pour le filet (EV-C-0020).

**Obstacles hiérarchisés** (du plus déterminant au moins déterminant pour le coût par kg de protéine)
1. Coût et consommation du milieu : litres/kg inconnus (KG-B04), acides aminés (Q-P-0032).
2. Coût du capital et aseptie : salle blanche vs qualité alimentaire, hypothèse non testée et la plus coûteuse (EV-E-0023, INN-12).
3. Faible densité protéique de la biomasse (KG-B01, INN-02).
4. Absence de différenciation musculaire industrialisable : indice de fusion ≤ 30 % avec transgène (EV-C-0027), aucun milieu de différenciation sans sérum publié (KG-B02, KG-B03).
5. Structuration au-delà de quelques centaines de µm, faute de vascularisation (EV-P-0059).

**Signaux industriels**
- Believer Meats, l'équipe aux meilleures données publiées, a fermé en décembre 2025, quelques semaines après l'approbation USDA de son usine. Aucune production commerciale n'y est documentée (EV-C-0065, EV-E-0047, EV-P-0043).
- Les capacités réellement opérées restent de l'ordre de 10³ L (EV-E-0055).
- Les filets UPSIDE sont encore produits en flacons de 2 L (EV-P-0046).
- Des cuves de 250 000 L ont été abandonnées (EV-P-0047).

## 5. Voie C — substituts

- **Texture** : l'extrusion humide ne reproduit pas la fibrosité du filet (indice LMA de 0,20, inférieur à la longe de porc, EV-A-0002). Une micro-impression post-extrusion multiplie la séparation fibreuse par 5 (EV-A-0003).
- **Nutrition** :
  - l'écart de qualité protéique vient du profil en acides aminés plutôt que de la digestibilité (EV-A-0012) ; DIAAS : soja 91, pois 70, porc 117 — compilation d'auteurs industriels (EV-A-0043) ;
  - les substituts sont pauvres en fer biodisponible (rapport phytate:fer de 2,5 à 45, EV-A-0004).
- **Arôme** : l'arôme de poulet repose sur des précurseurs soufrés et des phospholipides, pas sur l'hème (EV-A-0017, EV-A-0019) → piste INN-10.
- **Production** :
  - la mycoprotéine est produite en continu à l'échelle industrielle (EV-A-0040) ;
  - les protéines bactériennes hydrogénotrophes en sont au démonstrateur (160 t/an annoncées, Q-E-0055) ;
  - plusieurs entreprises ont échoué (Meati, Mycorena, Deep Branch : EV-A-0041, EV-P-0043 à EV-P-0052).
- **Lacunes majeures** : DIAAS du poulet et des nouvelles protéines, énergie de l'extrusion, TEA publiques (KG-C01, C02, C06).

## 6. Ce que l'histoire apprend

- Le protocole de finition est resté le même pendant 2 000 ans, de Rome au Sussex : confinement, obscurité, pâtée d'orge ou de blé cuit, 20–25 jours (EV-H-0010, EV-H-0014, EV-H-0028, EV-H-0055).
- **La production délibérée de larves pour les poules** (verminière) apparaît dans trois traditions : byzantine (Géoponiques, EV-H-0022), arabo-andalouse (Ibn al-ʿAwwām, qui les recopie, EV-H-0024) et chinoise, apparemment indépendante (EV-H-0027). Elle a été abandonnée pour l'odeur, le goût et le picage, pas pour inefficacité (EV-H-0032, CT-17) → INN-18.
- Réaumur mesure en 1749–1750 l'économie de grain apportée par la cuisson : orge −40 %, maïs plus de −50 % (Q-H-0021 à Q-H-0028) → INN-20, utile surtout pour les élevages sans granulation.
- L'arrêt des antibiotiques facteurs de croissance au Danemark n'a fait monter l'IC que de 0,016 (EV-H-0042).

## 7. Recommandations provisoires

1. **Pour réduire le coût du muscle de poulet à court terme**, les leviers démontrés restent ceux de la voie A : génétique, formulation à efficience nette, basse protéine raisonnée, gestion des myopathies. Le gain restant est probablement modeste (KG-A01).
2. **Pour la voie B**, il faut d'abord **mesurer** ce que les TEA supposent, avant d'investir dans l'échelle. Trois expériences peu coûteuses le permettraient : protéines par kg de biomasse (INN-02), litres de milieu par kg (INN-03), remplacement des acides aminés par des hydrolysats de qualité alimentation animale (INN-01).
3. **Les produits hybrides** (B+C) sont la seule forme commerciale actuelle. La dose-réponse sensorielle de la fraction cellulaire (INN-07) conditionne leur intérêt économique.
4. **Pour la voie C**, les verrous sont la fibrosité, l'arôme et la densité nutritionnelle (fer, B12). Les pistes INN-09, INN-10 et INN-15 sont testables rapidement.
5. **La protéine est le goulet commun** : une filière partagée (soja, SCP) entre aliment volaille, milieux de culture et substituts est le principal espace d'innovation transversal identifié.

## 8. Incertitudes majeures (voir `knowledge_gaps.md`, `contradictions.md`)

- Composition et consommation de milieu réelles de la biomasse de poulet cultivée (KG-B01, KG-B04).
- Pureté réellement exigée des intrants : elle fait varier l'ACV d'un facteur 100 (KG-B06, CT-09).
- Base du coût de 6,2 USD/lb de Pasitka 2024 (CT-02).
- DIAAS mesurés des substituts (KG-C01).
- Coûts du poulet après 2017 à l'échelle internationale (KG-X02).
