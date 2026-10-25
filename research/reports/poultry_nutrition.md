# Nutrition et production de muscle chez le poulet de chair (voie A) — rapport de domaine, brouillon v1

Agent N · 2026-10-25 · Questions RQ-N1 à RQ-N8 (+ contributions RQ-X1, X2, X3, X4).
Base de connaissances : 51 sources propres (SRC-N-0001 à 0051) + 2 sources réutilisées d'autres agents (SRC-E-0012, SRC-A-0021) ; 74 affirmations (EV-N-…) ; 81 mesures (Q-N-…).

---

## 1. Périmètre et méthode

**Objet.** Relations alimentation – métabolisme – génétique – croissance musculaire – rendement chez le poulet de chair, avec un objectif opérationnel : réduire l'aliment (et surtout la part d'aliment consommable par l'humain) par kg de muscle comestible sans dégrader santé et bien-être.

**Bases interrogées (107 requêtes journalisées, `research/agents/N/search_log.md`).** Europe PMC (dont texte intégral libre), PubMed (E-utilities et MCP), Crossref, HAL, theses.fr (dont API), J-STAGE, Consensus (5 appels), WebSearch/WebFetch (sites institutionnels : NCC, Aviagen, ITAVI, ministère chinois de l'Agriculture, Embrapa via presse, legislation.gov.uk, Cambridge Core).

**Langues.** en (75 requêtes), fr (7), zh (7), ja (5), es (5), pt (7). Le japonais est justifié par la politique nationale du riz fourrager (飼料用米) comme substitut du maïs importé ; le chinois par la politique de « réduction-substitution du tourteau de soja » (豆粕减量替代) et la sélection de souches nationales (圣泽901) ; le portugais par le poids du Brésil (Embrapa) ; l'espagnol par les normes FEDNA.

**Accès réel.** 12 articles évalués par les pairs lus en texte intégral (Zuidhof 2014, de Rauglaudre 2023, Belloir 2017, van Harn 2019, Laisse 2018, Mottet 2017, Nuamah 2024, Irawan 2022, Lee 2024, Yimiletey 2026, Tallentire 2018, Wangui 2025), 7 lus partiellement (Torrey 2021, Brink 2022, McCafferty 2022, Che 2022, Barbut 2024, Bilal 2026, Biteau 2026), plus des documents techniques lus en entier (guide Ross 308 2022, statistiques NCC, ITAVI PTCP 2023, page MOA, synthèse Nutreco/FEDNA, Honda 2018). Les autres sources ne sont connues que par leur résumé (`abstract_only`) et sont traitées avec une confiance réduite.

**Limites d'accès.** ScienceDirect (403), SciELO (403), EUR-Lex (réponse vide), CNKI (bloqué), PDF de thèses équatoriennes (503). Conséquences : Havenstein 2003 lu en résumé seulement ; texte du règlement (UE) 2021/1372 non lu (connu par communiqué IPIFF) ; littérature primaire chinoise et brésilienne quasi absente.

**Conventions.** IC = kg d'aliment / kg de poids vif (PV). Chaque chiffre est accompagné de la souche, de l'âge et du poids quand la source les donne. Nature des données : *mesuré* (essai), *statistique* (enquête nationale), *objectif commercial* (guide de sélectionneur), *modèle* (sortie de modèle), *calcul agent N* (dérivation explicite à partir de valeurs enregistrées).

---

## 2. État des connaissances par question

### RQ-N1 — Évolution de l'IC, de la croissance et du rendement ; part génétique / nutrition

- **Gains mesurés en conditions contrôlées.** À régime moderne identique, l'IC cumulé 0-42 j passe de 2,88 (souche témoin AMC-1957) à 1,90 (AMC-1978) puis 1,67 (Ross 308, 2005) ; la croissance augmente de plus de 400 % ; l'IC baisse de 2,55 %/an (EV-N-0001 ; Q-N-0001 à 0004). L'indice « aliment par kg de filet » (22-56 j) passe de 28,2 à 9,4 kg/kg (EV-N-0002, Q-N-0005/0006) et le rendement en grand pectoral augmente de 79-85 % (EV-N-0003). Réserve : la souche 1957 gaspille de l'aliment, ce qui gonfle son IC.
- **Génétique vs nutrition.** Dans le plan souche × régime de Havenstein 2003 (résumé), la Ross 308 a un IC à 42 j de 1,62 avec le régime 2001 contre 1,92 avec le régime 1957 ; la souche 1957 passe de 2,34 à 2,14 (EV-N-0006). À poids égal (1,815 kg), l'écart est de 1,47 contre 4,42 (EV-N-0007). Zuidhof rapporte, d'après Havenstein, que **85 à 90 %** du progrès est attribué à la génétique (EV-N-0005, citation de seconde main ; confiance modérée). La part « nutrition » est donc minoritaire mais pas nulle (≈ 0,2-0,3 point d'IC à 42 j), et confondue avec la forme physique de l'aliment (farine vs granulé).
- **Terrain.** Aux États-Unis, le ratio aliment/gain moyen est passé de 4,7 (1925, 112 j, 1,1 kg) à 1,95 (2000) puis 1,70 (2025, 47,5 j, 3,01 kg) (EV-N-0010, Q-N-0016/0017) ; il a stagné autour de 1,95 de 1985 à 2005 avant de reprendre sa baisse. **La mortalité est remontée de 3,7 % (2012-2013) à 5,95 % (2025)** (Q-N-0018), signal possible d'un compromis santé/performance non expliqué par les données consultées. En France, le poulet standard 2022 : IC 1,612 à 35,7 j et 1,93 kg, mortalité 3,9 % (EV-N-0064, Q-N-0069).
- **Objectifs commerciaux.** Ross 308 (2022, mixte, conditions optimales) : 2 998 g à 42 j, IC 1,531, IC non corrigé de la mortalité (EV-N-0008, Q-N-0011/0012). Une souche chinoise (Shengze 901plus) revendique 1,423 au sol à 2,5 kg/37 j (EV-N-0070, allégation non vérifiable).

### RQ-N2 — Besoins (protéine idéale, énergie) et limites des régimes à basse protéine

- **Spécifications pratiques.** Les normes FEDNA 2018 (reproduites par une synthèse industrielle, seconde main) visent 21,2 → 17,5 % de PB et 1,22 → 0,92 % de lysine digestible sur quatre phases ; les nutritionnistes formulent désormais sur des minima d'AA et non de PB, intègrent la glycine équivalente et attribuent aux enzymes 47-55 kcal EMA/kg de plus que FEDNA (EV-N-0068, Q-N-0075). La référence américaine NRC date de 1994 et n'a pas été révisée à notre connaissance (SRC-N-0045, métadonnées seulement).
- **Basse protéine : ce qui est établi.** Méta-analyse de 106 essais (mâles, croissance rapide) : chaque point de PB retiré dégrade l'IC de 1,9 % ; quand tous les AA indispensables respectent les ratios recommandés, la pénalité tombe à 1,2-1,3 %/point sans effet sur le gain (EV-N-0011, Q-N-0019) ; l'excrétion d'azote baisse de 11-14 %/point (EV-N-0012, Q-N-0020) ; chaque point remplace ~39 g/kg de tourteau de soja par des céréales et ~5 g/kg d'AA libres (Q-N-0021). Essai INRA : PB 19 → 17 % sans perte entre 21 et 35 j ; à 16 % et 15 %, IC +2,4 % et +3,6 % (EV-N-0014, Q-N-0023) ; +3,5 points d'efficacité azotée par point de PB (EV-N-0015).
- **Limites.** (i) Gras abdominal : +8,8 %/point (EV-N-0013), +0,5 point de % PV à 15-16 % PB (Q-N-0024), presque doublé de 210 à 165 g/kg (EV-N-0019) ; (ii) glycine + sérine deviennent limitantes (besoin 11-20 g/kg jusqu'à 21 j ; plancher ~15-16 % PB en démarrage si on les prend en compte) (EV-N-0020, Q-N-0030) ; l'acide urique coûte ≥ 60,7 kJ et une glycine par unité excrétée (EV-N-0021) ; (iii) la baisse du soja réduit le potassium et le bilan électrolytique (~−19 mEq/kg par point de PB ; SRC-N-0005, §3.2 du texte) ; (iv) barrière réglementaire : la glycine libre a nécessité une dérogation aux Pays-Bas (EV-N-0017) ; (v) interaction avec la forme : en granulé, la PB la plus basse (175/165 g/kg) n'a pas maintenu les performances (EV-N-0035).
- **Échelle nationale.** La Chine affiche −1,5 point de tourteau de soja dans les aliments en 2023, −4,44 Mt de tourteau consommé par les usines (11 mois) et −9,1 Mt de soja fourrager, en promouvant les régimes à basse protéine (EV-N-0067, Q-N-0074).

### RQ-N3 — Digestibilité et additifs ; procédés

- **Phytase.** Sur 41 études, la phytase restaure gain, IC et minéralisation osseuse dans des régimes carencés en P/Ca ; l'effet dépend de l'âge, de la souche et de la source de P plus que de la dose ; hétérogénéité extrême (I² 93-99,8 %) et biais de publication détecté (EV-N-0029). Le **superdosage** (> 2 500 FTU/kg) est défendu par une revue co-écrite par un fabricant d'enzymes, sans chiffre accessible (EV-N-0030, Q-N-0048) : gain au-delà d'un régime équilibré **non démontré** dans les sources lues.
- **Xylanase.** Méta-analyse (53 articles) favorable mais ampleur non disponible (EV-N-0031, confiance faible).
- **Protéase.** Résultat négatif instructif : −5,6 points d'IC dans un régime à AA digestibles réduits, **+5,8 points** dans un régime standard (EV-N-0032, Q-N-0043) ; −0,22 MJ/kg d'extra-chaleur (EV-N-0033). Une protéase ne « crée » pas de valeur si aucun déficit n'est à combler.
- **Énergie nette.** EN/EMA mesurée : 55-60 % (colza, son), 79 % (céréales), 86 % (huile de palmiste) ; le classement des matières premières change entre EMA et EN (EV-N-0073) — argument pour formuler en EN dès qu'on introduit des coproduits fibreux.
- **Granulation.** 0-39 j : IC 1,48-1,51 en granulé contre 1,60-1,69 en farine (Ross 308 mâles) ; la farine améliore litière et pododermatites (EV-N-0035, Q-N-0045/0046).
- **Fermentation.** Le tourteau de soja fermenté augmente le poids final mais pas l'IC (méta-analyse, 16 études ; EV-N-0034, Q-N-0047).

### RQ-N4 — Microbiote, probiotiques, alternatives aux AGP

- **Réglementation.** UE : antibiotiques autres que coccidiostatiques/histomonostatiques autorisés comme additifs seulement jusqu'au 31/12/2005 (EV-N-0038).
- **Valeur des AGP dans un système moderne.** Essai industriel non randomisé (~7 M de poulets) : gain de production inférieur au coût des AGP (−0,0093 USD/poulet) (EV-N-0037, Q-N-0049).
- **Probiotiques.** Effet moyen sur l'IC de −0,058 (106 essais), plus net avec Bacillus et dans les pays en développement (EV-N-0040, Q-N-0050) ; mais une méta-analyse d'essais randomisés sur oiseaux sains montre que l'effet sur le gain disparaît après correction du biais de publication (EV-N-0039, Q-N-0051). Thèse Jansseune 2025 : bénéfices limités aux régimes « challenge » et **non reproduits** dans un second essai (EV-N-0041). Conclusion de travail : les probiotiques sont une assurance sanitaire conditionnelle, pas un levier d'IC en conditions optimales.

### RQ-N5 — Biologie du muscle

- **Fenêtre critique.** Nombre de fibres fixé à l'éclosion ; croissance post-éclosion par hypertrophie alimentée par les cellules satellites, actives à l'éclosion et quiescentes vers 2 semaines (EV-N-0047, confiance élevée).
- **Effets de la sélection.** Les cellules satellites d'une lignée moderne prolifèrent et se différencient moins (MyoD, MyoG, mTOR plus faibles) que celles de lignées anciennes ; leur dysfonction est impliquée dans le woody breast (EV-N-0048). L'inactivation de la myostatine chez le poulet n'augmente pas le filet (contrairement à la caille) (EV-N-0049) ; MSTN n'explique pas la différence chair/ponte (EV-N-0050).
- **Alimentation in ovo.** Glucides + HMB à J17,5 : +5-6 % de poids à l'éclosion, +6-8 % de filet relatif jusqu'à 25 j (EV-N-0051, résumé, équipe d'origine) ; créatine in ovo : aucun effet sur poids, composition ni fibres à 42 j (EV-N-0071) ; vitamines : effets modestes et conditionnels (EV-N-0072). Effet à l'âge d'abattage **non démontré**.
- **Myopathies comme limite physiologique.** Ontario (Ross 708, 9 250 filets) : white striping léger-modéré 96,0 %, viande spaghetti 36,3 %, woody breast sévère 11,8 % ; 85 % des filets cumulent plusieurs défauts (EV-N-0042, Q-N-0052 à 0054) ; risque accru avec le poids vif, la chaleur et l'absence de vaccination coccidiose (EV-N-0043). Les myopathies augmentent avec le rendement filet mais les valeurs génétiques ne sont pas parfaitement corrélées (EV-N-0045) ; formes sévères plus fréquentes à 9 qu'à 6 semaines (EV-N-0046). Coût estimé > 1 Md USD/an en Amérique du Nord (EV-N-0044, estimation de seconde main).

### RQ-N6 — Limites physiologiques et compromis bien-être (voir aussi §4)

- **Entretien.** 196 kcal EM/kg^0,7543/j (EV-N-0004, Q-N-0007) ; la baisse historique de l'IC vient en grande partie de la dilution de l'entretien par une croissance plus rapide.
- **Plafond modélisé.** Même aux limites biologiques d'ingestion, de digestion et d'adiposité, 2,2 kg ne serait atteint que 1,2 j plus tôt (−8 % d'énergie alimentaire) (EV-N-0052, Q-N-0057).
- **Souches lentes.** Mesuré sur 16 souches en conditions identiques : IC corrigé jusqu'à ~3,2 kg de 1,54 (conventionnelles) à 1,76 / 1,89 / 1,97 (lentes) (EV-N-0054, Q-N-0060/0061) ; mortalité 2,52 % sans différence entre catégories en laboratoire (EV-N-0055). Modèle : une souche atteignant 2,2 kg à 56 j consommerait +27 % d'énergie, avec +27 % de GES/surface et +64 % d'azote excrété (EV-N-0053, Q-N-0058/0059). Label Rouge (France 2022) : IC 3,04 à 87,7 j et 2,26 kg (Q-N-0070).

### RQ-N7 — Ressources alimentaires alternatives (tableau §3.3)

Synthèse : aucune alternative unique au soja (EV-N-0056) ; les PAT et protéines aquatiques ont les meilleures pentes d'IC, les protéines microbiennes, graines et feuilles les pires ; la digestibilité baisse aux forts taux pour toutes. Côté environnement, la microalgue augmente presque tous les impacts et les PAT les réduisent (EV-N-0057) ; la plupart des ACV donnent à la farine d'insectes un impact climatique **supérieur** au soja hors vrais déchets (EV-N-0058). Données d'essais : méthanotrophe jusqu'à 120 g/kg sans perte de gain (EV-N-0059 ; cohérent avec EV-A-0014) ; levure C. jadinii plafonnée à ~10 % des protéines (EV-N-0060) ; féverole sans tanins jusqu'à 40 % en finition (EV-N-0061) ; pois/féverole en remplacement partiel (EV-N-0062) ; anciennes denrées jusqu'à 25 % (EV-N-0063, petit essai) ; riz fourrager en remplacement total du maïs (EV-N-0069, n = 6).

### RQ-N8 — Rendements et protéine comestible par kg d'aliment

- Rendements Ross 308 (objectifs, mâle à 3,0 kg) : carcasse éviscérée 73,4 %, filet 25,9 %, viande totale sans peau ni os 43,1 % du PV (femelle : 74,1 / 28,1 / 44,5 %) (EV-N-0009, Q-N-0013 à 0015).
- Composition (Laisse 2018) : 181 g de protéines/kg PV ; viande = 47 % du PV et 54 % des protéines corporelles ; total consommable 62 % du PV et 64 % des protéines (EV-N-0024, Q-N-0034/0035).
- Efficience protéique : brute 0,54, nette (consommable) 0,88 pour un poulet standard français (EV-N-0022, Q-N-0032/0033) ; modifiable de 0,8 à 2 par la formulation (EV-N-0023). Le modèle FAO-GLEAM donne pour les poulets OCDE 5,1 kg de protéines consommables par kg de protéines produites (EV-N-0026, Q-N-0039) : écart majeur expliqué au §5.

---

## 3. Tableaux quantitatifs

### 3.1 Performances par génotype et système (IC = kg aliment / kg PV)

| Système / souche | Âge, poids | IC | Nature | ID |
|---|---|---|---|---|
| AMC-1957 (témoin non sélectionné), régime moderne | 0-42 j | 2,88 | mesuré | Q-N-0001 |
| AMC-1978, régime moderne | 0-42 j | 1,90 | mesuré | Q-N-0002 |
| Ross 308 (2005), régime moderne | 0-42 j | 1,67 | mesuré | Q-N-0003 |
| Ross 308 (2001) régime 2001 / régime 1957 | 42 j ; 2,67 / 2,13 kg | 1,62 / 1,92 | mesuré (résumé) | Q-N-0009 |
| Ross 308 objectif 2022 (mixte) | 42 j ; 3,00 kg | 1,531 | objectif commercial | Q-N-0011 |
| Conventionnelles, 16 souches (Torrey) | ~3,2 kg | 1,54 (corrigé mortalité) | mesuré | Q-N-0060 |
| Lentes « SLOW » (Torrey) | ~2,8 kg | 1,97 | mesuré | Q-N-0061 |
| Ross 308 mâles granulé / farine | 0-39 j | 1,48 / 1,69 | mesuré | Q-N-0045/0046 |
| France poulet standard 2022 | 35,7 j ; 1,93 kg | 1,612 | statistique | Q-N-0069 |
| France Label Rouge 2022 | 87,7 j ; 2,26 kg | 3,04 | statistique | Q-N-0070 |
| États-Unis 2025 | 47,5 j ; 3,01 kg | 1,70 | statistique | Q-N-0016 |
| États-Unis 1925 | 112 j ; 1,13 kg | 4,7 | historique | Q-N-0017 |

### 3.2 Efficacité de conversion vers le muscle et la protéine comestible (calcul agent N)

Hypothèses : rendements Ross 308 à 3,0 kg (moyenne mâle-femelle : carcasse 73,7 %, filet 27,0 %, viande sans peau ni os 43,8 %) appliqués à tous les systèmes ; protéines de viande = 0,181 × 0,54 = 0,0977 kg/kg PV, protéines consommables = 0,181 × 0,64 = 0,116 kg/kg PV (Laisse 2018) ; PB moyenne de l'aliment 20 % ; aliment des reproducteurs **non inclus**. Ces hypothèses avantagent les souches lentes et le Label Rouge (rendements réels plus faibles) : leurs valeurs sont donc optimistes.

| Système | IC | kg aliment/kg carcasse | kg aliment/kg filet | kg aliment/kg viande | g protéine viande/kg aliment | g protéine consommable/kg aliment | kg aliment/kg protéine viande | protéine viande / protéine ingérée |
|---|---|---|---|---|---|---|---|---|
| Ross 308 objectif (42 j) | 1,531 | 2,08 | 5,68 | 3,50 | 63,8 | 75,7 | 15,7 | 0,32 |
| Conventionnel Torrey (~3,2 kg) | 1,54 | 2,09 | 5,71 | 3,52 | 63,5 | 75,2 | 15,8 | 0,32 |
| France standard 2022 | 1,612 | 2,19 | 5,98 | 3,68 | 60,6 | 71,9 | 16,5 | 0,30 |
| États-Unis 2025 | 1,70 | 2,31 | 6,31 | 3,88 | 57,5 | 68,1 | 17,4 | 0,29 |
| Lentes Torrey (~2,8 kg) | 1,97 | 2,67 | 7,31 | 4,50 | 49,6 | 58,8 | 20,2 | 0,25 |
| Label Rouge 2022 | 3,04 | 4,12 | 11,3 | 6,94 | 32,2 | 38,1 | 31,1 | 0,16 |
| AMC-1957 (0-42 j) | 2,88 | 3,91 | 10,7 | 6,58 | 33,9 | 40,2 | 29,5 | 0,17 |

Valeurs enregistrées : Q-N-0076 à Q-N-0081. Contrôle de cohérence : protéine corporelle totale / protéine ingérée = 0,59 pour l'objectif Ross, contre 0,54 chez Laisse (qui inclut les reproducteurs) : ordre de grandeur cohérent. Le rendement de la conversion « protéine alimentaire → protéine de viande » plafonne donc vers **0,30-0,32** : deux tiers de l'azote ingéré ne finissent pas dans la viande (entretien, os, plumes, abats, excrétion). En **protéines consommables** (et non totales), l'efficience peut dépasser 1 si la ration est faite de coproduits (EV-N-0023).

### 3.3 Ressources alimentaires alternatives

| Ingrédient | Taux testé | Effet croissance / IC / rendement | Base de preuve | Statut UE / US | Coût / ACV |
|---|---|---|---|---|---|
| PB réduite + AA libres | −1 à −4 points | IC +1,2-1,9 %/point ; gras ↑ ; N −11-14 %/point | méta-analyse 106 essais (EV-N-0011) + essais (EV-N-0014, 0016, 0018) | AA autorisés ; glycine : dérogation NL (EV-N-0017) | coût non chiffré (lacune) |
| Farine de larves de mouche soldat | 5-28 % | pas d'effet global (15 essais) ; dégradation à 10 % au Costa Rica | EV-A-0024 ; EV-A-0032 | UE : PAT d'insectes autorisées pour volailles (règlement 2021/1372, connu par communiqué, SRC-N-0026) ; US : non vérifié | plus cher que la farine de poisson ; GES > soja hors déchets (EV-N-0058) |
| Protéine bactérienne méthanotrophe | ≤ 120 g/kg ; ≤ 12,5 % | gain maintenu, G:F ↑ ; autolysat négatif | EV-N-0059 ; EV-A-0014 | non vérifié | catégorie « microbien » : pente IC +0,448 (EV-N-0056) |
| Levure C. jadinii | 10-30 % des protéines | pertes linéaires au-delà de 10 % | 1 essai (EV-N-0060) | non vérifié | — |
| Microalgues | 10-15 % | catégorie aquatique : pente IC −0,123 | méta-analyse (EV-N-0056) | — | impacts environnementaux ↑ (EV-N-0057) |
| PAT (hors insectes) | variable | pente IC −0,003 (≈ soja) | méta-analyse (EV-N-0056) | réautorisation partielle UE 2021 (secondaire) | impacts ↓ sauf acidification +8 % |
| DDGS | 15-20 % | pente IC +0,139 | méta-analyse (EV-N-0056) | autorisé | impacts/UF ↓ ; fumier ↑ |
| Colza | variable | pente IC +0,313 | méta-analyse (EV-N-0056) | autorisé | — |
| Féverole sans tanins | 15/30/40 % | ≈ témoin ; carcasse −0,6 pt au taux élevé | 1 essai (EV-N-0061) | autorisé | — |
| Pois + féverole | 55-100 % du soja selon phase | partiel OK ; total dès 10 j → pertes | 1 essai (EV-N-0062) | autorisé | — |
| Anciennes denrées | 6-25 % | pas de perte, G:F ↑ | 1 petit essai (EV-N-0063) | — | — |
| Riz fourrager (Japon) | 100 % du maïs | pas d'effet (n = 6) | EV-N-0069 | — | plus cher que le maïs importé |
| Soja fermenté | 3-15 % | PV ↑, IC NS | méta-analyse 16 études (EV-N-0034) | — | — |
| Lentille d'eau, manioc, tournesol | — | **non couverts** (lacune) | — | — | — |

### 3.4 Coût alimentaire

| Pays, année | Part de l'aliment dans le coût de production | ID |
|---|---|---|
| France, poulet standard 2022 | 0,755 / 1,264 €/kg vif ≈ 60 % (62 % hors rémunération ; aliment + poussin ≈ 79 %) | EV-N-0065, Q-N-0071 |
| France, Label Rouge 2022 | 1,436 / 2,485 €/kg vif ≈ 58 % | Q-N-0072 |
| Brésil (Paraná), juillet 2025 | 64 % (4,60 R$/kg vif) | EV-N-0066, Q-N-0073 |
| Amérique du Nord (affirmation générale) | ≈ 2/3 | EV-N-0074 |

---

## 4. Limites physiologiques (section demandée)

1. **Entretien.** 196 kcal EM/kg^0,75/j (EV-N-0004). Chaque jour d'élevage en plus coûte de l'entretien sans muscle : c'est le mécanisme par lequel les souches lentes et les abattages tardifs dégradent l'IC (EV-N-0053, EV-N-0054).
2. **Efficacité de dépôt protéique.** Le passage protéine ingérée → protéine de viande plafonne à ~0,32 (§3.2) ; l'excès d'AA est catabolisé à un coût de ≥ 60,7 kJ/g N et consomme de la glycine (EV-N-0021). La voie la plus sûre pour progresser n'est pas la sélection mais la **réduction de l'excès d'AA** (basse PB équilibrée).
3. **Plafond de l'IC.** Le modèle de Tallentire situe le gain restant à ~8 % d'énergie (EV-N-0052). Les statistiques américaines montrent pourtant une baisse de l'IC moyen de 1,89 (2015) à 1,70 (2025) à âge constant et poids croissant (EV-N-0010) : soit le modèle est trop pessimiste, soit l'écart terrain/potentiel se comble (gestion, santé, granulation, enzymes) sans que le potentiel génétique bouge beaucoup. Les données ne permettent pas de trancher.
4. **Myopathies.** Elles touchent la majorité des filets des souches à fort rendement (EV-N-0042) et augmentent avec le poids et le rendement (EV-N-0045, EV-N-0046) : le rendement filet est limité par la capacité vasculaire/régénérative du muscle (hypoxie, dysfonction des cellules satellites, EV-N-0048).
5. **Compromis bien-être.** Souches lentes (type BCC/ECC) : +14 à +28 % d'aliment par kg de PV aux poids cibles de l'essai (~3,2 kg ; la catégorie la plus lente n'atteint que 2,8 kg) (Torrey ; calcul : 1,76/1,54 et 1,97/1,54) et +27 % d'énergie dans le modèle Tallentire ; mortalité non différente en laboratoire (EV-N-0055), mais en hausse dans le système conventionnel américain (EV-N-0010). Le texte du BCC n'a pas été lu (lacune).

---

## 5. Contradictions repérées

| Sujet | Côté A | Côté B | Explication probable |
|---|---|---|---|
| Efficience protéique nette du poulet | ECpc 0,88 (France ; EV-N-0022) et 0,8-2 selon formule (EV-N-0023) | 5,1 kg de protéines consommables par kg produit (≈ 0,2) pour les poulets OCDE (EV-N-0026) | Mottet compte céréales, légumineuses et soja comme 100 % consommables ; Laisse applique des parts partielles (maïs 15 %). Le désaccord est **définitionnel**, pas expérimental. |
| Basse PB et rendement filet | aucun effet (EV-N-0014) | baisse à −3 points (EV-N-0016) / hausse à −3 points (EV-N-0018) | Base de calcul différente (% PV vs % carcasse), Gly ajoutée ou non, profils d'AA différents. |
| Basse PB et IC | +1,2-1,9 %/point (méta-analyse, EV-N-0011) | IC amélioré à −2/−3 points (EV-N-0016) ou inchangé (EV-N-0018) | Essais récents avec AA (dont Gly) très bien ajustés ; témoins peut-être en excès de protéine (fermentation caecale). |
| Probiotiques | IC −0,058, effet renforcé après correction de biais (EV-N-0040) | gain non significatif après correction (EV-N-0039) ; non-réplication (EV-N-0041) | Méthodes de correction, essais en conditions sanitaires différentes. |
| Limites de la sélection | gain restant ~8 % (modèle, EV-N-0052) | IC terrain toujours en baisse (EV-N-0010) ; allégations chinoises 1,42 (EV-N-0070) | Écart potentiel/terrain ; définition des IC (mortalité, pesée). |
| Alimentation in ovo | +6-8 % de filet relatif à 25 j (EV-N-0051) | aucun effet de la créatine à 42 j (EV-N-0071) | Molécule, moment d'injection, durée de suivi ; équipe d'origine vs équipe indépendante. |
| Insectes (avec l'agent A) | pas d'effet global, taux recommandé 28 % (EV-A-0024) | dégradation dès 10 % (EV-A-0032) | Mes données ajoutent un argument environnemental défavorable (EV-N-0058) et une pente d'IC neutre des PAT (EV-N-0056) : **elles ne tranchent pas** sur la performance mais contredisent l'intérêt environnemental hors déchets. |
| Méthanotrophe (avec l'agent A) | jusqu'à 12,5 % sans perte (EV-A-0014) | — | Mes données (EV-N-0059, ≤ 120 g/kg) **confirment** ; mais la catégorie « microbien » de la méta-analyse a une pente d'IC défavorable (EV-N-0056) et la levure plafonne à 10 % des protéines (EV-N-0060). |

---

## 6. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Fonctionne (preuves convergentes).** Sélection génétique (85-90 % du progrès) ; granulation (−0,1 à −0,2 d'IC) ; basse PB à −2 points avec AA indispensables + glycine (N excrété −22 à −28 %, IC ±1-2 %) ; phytase aux doses usuelles pour remplacer le phosphate ; remplacement partiel du soja par féverole/pois, PAT, DDGS dans des limites connues.

**Échoue ou déçoit.** Très basse PB (≤ 16 %) : IC et gras se dégradent ; protéase sur régime déjà équilibré (IC +5,8 points) ; soja fermenté sur l'IC ; probiotiques en conditions sanitaires optimales ; MSTN-KO pour le filet ; in ovo pour l'hyperplasie (non démontré à l'abattage) ; insectes et microalgues pour l'environnement quand le substrat n'est pas un déchet ; levure au-delà de 10 % des protéines.

**Reste à inventer.** (i) Formuler pour l'**efficience nette** (protéines consommables) et en **énergie nette**, pas seulement pour l'IC et le coût ; (ii) lever le plancher de PB (glycine, potassium/électrolytes, amidon/protéine) ; (iii) agir sur la fenêtre péri-éclosion pour augmenter la capacité musculaire sans myopathie ; (iv) des souches « à bien-être » dont la pénalité d'aliment est compensée par une nutrition dédiée ; (v) des protéines microbiennes à cellules intactes produites avec de l'énergie bas carbone.

---

## 7. Lacunes (cherché sans succès ou non couvert)

- Besoins en vitamines et minéraux : non traités (hors phosphore).
- Tables INRAE-CVB, Rostagno 2017 (existence signalée mais notice non vérifiée), NRC 1994 (non lu) ; aucune table de besoins primaires lue.
- Méta-analyse chiffrée du superdosage de phytase et de la xylanase (ampleur en points d'IC).
- Coût des régimes basse PB (prix des AA vs soja) : non trouvé.
- Lentille d'eau, manioc, tournesol, colza (essais spécifiques), anciennes denrées à grande échelle.
- Littérature primaire chinoise (CNKI bloqué) sur basse protéine et 黑水虻 ; littérature brésilienne (SciELO 403).
- Texte du règlement (UE) 2021/1372, statut UE de la glycine et des SCP, statut américain (AAFCO/FDA) des farines d'insectes et des SCP.
- Texte du Better Chicken Commitment ; études de souches lentes en conditions commerciales (mortalité, myopathies).
- Composition protéique de la viande (tables Ciqual/USDA) et part de l'aliment des reproducteurs, pour affiner le §3.2.
- Résultats négatifs de l'alimentation in ovo en recherche dédiée : aucune revue critique trouvée.

---

## 8. Pistes d'innovation

### Piste N-1 — Formulation « efficience nette + énergie nette »
- **Problème.** Le poulet consomme plus de protéines consommables qu'il n'en produit (ECpc 0,88, EV-N-0022) et dépend du soja importé.
- **Solutions actuelles.** Formulation au moindre coût en EMA et AA digestibles ; contraintes de PB.
- **Insuffisances.** L'EMA surévalue les matières fibreuses et protéiques (EV-N-0073) ; aucune contrainte sur la part consommable ; le passage à des coproduits dégrade souvent l'IC (EV-N-0056).
- **Preuves d'une nouvelle approche.** ECpc modifiable de 0,8 à 2 par la seule formule, gain « très supérieur » à celui d'un meilleur IC (EV-N-0023) ; AA libres + basse PB maintiennent l'IC (EV-N-0011) ; féverole, DDGS, PAT, anciennes denrées utilisables (EV-N-0061 à 0063).
- **Hypothèse.** Une formulation multi-objectif (coût, EN, AA digestibles + Gly équivalente, part consommable ≤ 25 %) atteint ECpc ≥ 1,3 avec une pénalité d'IC ≤ 3 %.
- **Expérience de validation.** Ross 308 mixtes, 0-42 j, 3 régimes × 12 parquets : (A) moindre coût EMA, (B) moindre coût EN + basse PB, (C) B + contrainte ECpc ; mesures : IC corrigé, rendement filet, gras, N excrété, myopathies ; calcul ECpc avec deux jeux de parts consommables (Laisse et Mottet).
- **Succès / échec.** Succès : ECpc ≥ 1,3 (définition Laisse) et ≥ 0,5 (définition Mottet), IC ≤ +3 %, filet ≥ −0,5 point. Échec : IC > +5 % ou WB sévère ↑.
- **Coûts / risques.** Essai ≈ 1 500 oiseaux, faisable en station ; risques : variabilité des coproduits, mycotoxines, disponibilité locale.

### Piste N-2 — Lever le plancher de protéine brute
- **Problème.** Sous ~17 % de PB, IC et gras se dégradent (EV-N-0014, EV-N-0019).
- **Solutions actuelles.** Ajout des AA indispensables jusqu'à Val/Ile/Arg.
- **Insuffisances.** Gly+Ser, potassium/électrolytes et rapport amidon/protéine ne sont pas formulés ; glycine soumise à dérogation (EV-N-0017).
- **Preuves.** Gly équivalente premier limitant (EV-N-0020), coût en glycine de l'acide urique (EV-N-0021), baisse du K et du bilan électrolytique avec le soja (SRC-N-0005), gras lié au déséquilibre amidon/protéine (EV-N-0019).
- **Hypothèse.** Ajuster Gly équivalente + K (bilan électrolytique) + source d'amidon lente permet 15 % de PB en croissance-finition sans pénalité d'IC > 2 %.
- **Expérience.** Dose-réponse 19/17/15 % PB × (± Gly) × (± K₂CO₃), Ross 308 mâles 10-42 j, 8 parquets/traitement.
- **Succès / échec.** IC ≤ +2 %, gras ≤ +0,2 point, N excrété −25 % ; échec si gras > +0,5 point.
- **Coûts / risques.** Prix des AA libres ; statut réglementaire de la glycine à vérifier.

### Piste N-3 — Programmer la capacité musculaire en péri-éclosion pour réduire les myopathies
- **Problème.** Myopathies chez la majorité des filets (EV-N-0042) ; rendement filet limité par la capacité régénérative.
- **Solutions actuelles.** Ralentir la croissance, sélection conjointe WB/rendement (EV-N-0045).
- **Insuffisances.** La sélection est lente ; l'in ovo n'a pas d'effet démontré à l'abattage (EV-N-0071) ; MSTN-KO inefficace sur le filet (EV-N-0049).
- **Preuves.** Fibres fixées à l'éclosion, fenêtre des cellules satellites (EV-N-0047) ; dysfonction des cellules satellites dans le WB (EV-N-0048) ; filet relatif +6-8 % à 25 j avec in ovo glucides+HMB (EV-N-0051).
- **Hypothèse.** Un apport énergétique péri-éclosion (in ovo + alimentation dès l'éclosion) augmente le nombre de noyaux/fibre et réduit l'incidence du WB sévère à poids d'abattage égal.
- **Expérience.** 2 × 2 (in ovo glucides+HMB oui/non × accès précoce à l'aliment oui/non), Ross 308, abattage 42 et 49 j ; histologie (fibres, noyaux Pax7+), notation WB/WS.
- **Succès / échec.** WB sévère −30 % relatif sans perte de rendement ; échec si aucun effet à 42 j.
- **Coûts / risques.** Matériel d'injection, couvoir ; risque d'effet transitoire. Lien direct avec l'agent C (biologie des cellules satellites).

### Piste N-4 — Souches « bien-être » nourries pour leur courbe de croissance
- **Problème.** Pénalité alimentaire des souches lentes (+14 à +28 % d'aliment aux poids cibles ; EV-N-0054) et environnementale (EV-N-0053).
- **Insuffisances.** Les aliments restent conçus pour les souches rapides.
- **Preuves.** Un aliment à 19,6 % de PB réduit l'écart GES de +27 % à +16 % dans le modèle (EV-N-0053).
- **Hypothèse.** Un programme basse PB + EN dédié aux souches lentes réduit l'écart d'azote excrété de moitié et l'écart d'IC d'un tiers.
- **Expérience.** Deux souches (conventionnelle, lente), deux programmes (standard, dédié), jusqu'à 2,5 kg.
- **Critères.** Écart d'IC ≤ 0,15 ; N excrété −30 % pour la souche lente.

---

## 9. Contributions aux questions transversales

- **RQ-X1 (coût mesuré).** Coût de production mesuré France 2022 : 1,264 €/kg vif (standard) et 2,485 €/kg vif (Label Rouge) ; Brésil 2025 : 4,60 R$/kg vif ; aliment ≈ 58-64 % (§3.4).
- **RQ-X2 (ressources/kg de protéine comestible).** ≈ 13-15 kg d'aliment (frais) par kg de protéine consommable et 15,7-17,4 kg par kg de protéine de viande en système rapide (calcul §3.2) ; 20-31 kg en souches lentes / Label Rouge ; GWP ferme 3,23 kg CO₂-éq/kg carcasse (UK, périmètre élevage, Q-N-0064).
- **RQ-X3 (goulets partagés).** Les acides aminés (lysine, méthionine, thréonine, valine, glycine) sont le goulet commun entre aliment volaille à basse PB et milieux de culture (voie B) ; les protéines microbiennes (méthanotrophe, levure) sont un candidat commun aux trois voies mais avec des plafonds d'incorporation (EV-N-0059, EV-N-0060).
- **RQ-X4 (réglementation alimentation animale).** AGP interdits UE 2006 (EV-N-0038) ; PAT d'insectes autorisées pour volailles UE 2021 (secondaire) ; glycine libre sous dérogation NL en 2019 (EV-N-0017) ; politique chinoise de réduction du soja (EV-N-0067).

---

## 10. Recherches restantes prioritaires

1. Textes officiels : règlement (UE) 2021/1372, registre UE des additifs (glycine, SCP), statut AAFCO/FDA des farines d'insectes et protéines bactériennes.
2. Havenstein 2003 et 1994 en texte intégral (part génétique/nutrition, mortalité, rendements).
3. Prix des AA de synthèse vs tourteau de soja et coût marginal d'un point de PB en moins (avec l'agent E).
4. Tables de composition de la viande (Ciqual, USDA FoodData Central) et part de l'aliment des reproducteurs, pour consolider le §3.2.
5. Texte du Better Chicken Commitment et études de terrain sur souches lentes (mortalité, myopathies, IC).
6. Méta-analyses chiffrées du superdosage de phytase et des xylanases ; adoption de l'énergie nette en formulation.
7. Littérature chinoise (basse protéine, 黑水虻, souches nationales) et brésilienne (Rostagno, Embrapa) via sources accessibles.

## 11. Notes sur les outils et errata

- Défaut kb.py (corrigé par le coordinateur en cours de session) : titres CJK normalisés en chaîne vide → faux doublons. Trois titres (SRC-N-0046/0047/0048) ont été saisis avec une romanisation puis restaurés via `kb.py set`.
- Errata corrigés par l'agent avant la commande `set` (avec les fonctions de kb.py, traces dans `notes`) : liste d'auteurs erronée de SRC-N-0018 (corrigée d'après PubMed/Crossref) ; `contradicts` d'EV-N-0022 (EV-N-0026) ; mentions d'affiliation ou de nom commercial non vérifiées retirées (SRC-N-0028, 0032, 0038, 0051, EV-N-0059) ; unité de Q-N-0074.
