# Brief — Agent C : Biotechnologies et viande cultivée de poulet (voie B)

**Lettre** : C · **Rapport** : `research/reports/cultivated_chicken.md` · **Questions** : RQ-C1 à RQ-C8 (+ contribution à RQ-X1–X3).

## Mission
Établir l'état réel de la production de muscle de poulet à partir de cellules : types cellulaires, prolifération, différenciation, milieux, facteurs de croissance, supports, bioréacteurs, densité, oxygénation, maturation, texture, nutrition, sécurité, coûts. **Distinguer systématiquement** ce qui est démontré **avec des cellules de poulet** de ce qui est extrapolé d'autres espèces (bovin, porc, souris C2C12, canard, caille). Identifier précisément les obstacles à une production rentable à grande échelle.

## Livrables spécifiques
- Tableau « **performances démontrées en cellules de poulet** » : type cellulaire / lignée, milieu (sérum ? sans sérum ? composition connue ?), système (plaque, microporteurs, suspension, perfusion), temps de doublement, doublements cumulés, densité max (cellules/mL et g/L avec base de calcul), durée, différenciation (marqueurs, % fusion), échelle (volume), source.
- Tableau « **produits et dossiers réglementaires** » (UPSIDE, GOOD Meat, autres) : ce que contient réellement le produit (cellules de quelle nature, % de cellules dans le produit fini, autres ingrédients) d'après les **documents officiels** (mémos FDA, SFA, FSANZ) — non la presse.
- Liste hiérarchisée des **obstacles** (milieu, facteurs de croissance, densité/transfert d'O₂, différenciation sans sérum, structuration, contamination/aseptie, recyclage, coût du capital), chacun avec les preuves et l'ordre de grandeur de l'écart à combler.

## Pistes et références à retrouver (à vérifier)
- Pasitka et al. 2023 *Nature Food* (immortalisation spontanée de fibroblastes de poulet, lignées sans sérum) ; Pasitka et al. 2024 *Nature Food* (perfusion par filtration tangentielle, jusqu'à 130 × 10⁶ cellules/mL, milieu sans composant animal à 0,63 USD/L, TEA 50 000 L) — déjà enregistrée par le coordinateur : `SRC-X-0001`.
- FDA : consultations pré-commercialisation « cell-cultured chicken » UPSIDE Foods (2022) et GOOD Meat (2023) — mémos scientifiques en ligne (fda.gov, « Human Food Made with Cultured Animal Cells Inventory ») ; USDA-FSIS ; SFA Singapour (GOOD Meat 2020, sans sérum 2023).
- Cellules satellites de poulet (isolement, prolifération, sans sérum) ; lignées immortalisées (TERT/CDK4) de poulet ; ESC/iPSC/PGC aviaires ; préadipocytes de poulet (graisse cultivée).
- Équipes : Hebrew University/Nahmias (Believer Meats), Jiangnan University (江南大学, 周景文/陈坚), Nanjing Agricultural University (南京农业大学, 周光宏/丁世杰), équipes coréennes (Konkuk, Seoul National University), Japon (IntegriCulture CulNet, cellules de foie de poulet), Israël (SuperMeat), France (Vital Meat, Gourmey — canard), Pays-Bas.
- Milieux : O'Neill et al. 2021 ; Stout et al. (Beefy-9/Beefy-R, bovin → extrapolation) ; production recombinante de FGF2/IGF/insuline/transferrine à bas coût ; hydrolysats végétaux/levures/algues ; recyclage du milieu (élimination ammoniac/lactate).
- Bioprocédés : Allan, De Bank & Ellis 2019 ; transfert d'oxygène et densités limites ; Humbird 2021 (analyse technico-économique, l'agent E détaille l'économie).
- Supports : protéine de soja texturée (Ben-Arye 2020, bovin), microporteurs comestibles, matrices végétales décellularisées.
- Résultats négatifs : difficultés de différenciation sans sérum, sénescence des cellules primaires de poulet, faibles densités en adhérent.

## Langues
en, zh (细胞培养肉, 培养肉, 鸡肌肉卫星细胞, 无血清培养基), ja (培養肉, 鶏, 筋芽細胞), ko (배양육, 닭 근육 줄기세포), he/en (Israël), nl, fr (viande cultivée, viande in vitro), es (carne cultivada), de (kultiviertes Fleisch).

## Conseils
- Convertis les densités cellulaires en masse seulement si la source donne le facteur (ou cite une source pour le volume/poids cellulaire) ; sinon laisse `value_normalized` vide.
- Une densité obtenue en perfusion à 1 L n'est pas une densité démontrée à 10 000 L : `scale` exact.
- Les annonces d'entreprises (coût, capacité) → `company_claim`.
