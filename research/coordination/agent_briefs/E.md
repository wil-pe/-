# Brief — Agent E : Ingénierie, économie, industrialisation et réglementation

**Lettre** : E · **Rapport** : `research/reports/industrialization.md` · **Questions** : RQ-E1 à RQ-E6, responsable principal de RQ-X1, RQ-X2, RQ-X4.

## Mission
Comparer les procédés existants et émergents des trois voies sur leurs **performances réelles** : matières premières, coûts, rendements, énergie, eau, terres, GES, équipements, infrastructures, pertes, transformation, contraintes sanitaires, passage à l'échelle, CAPEX/OPEX. Construire des comparaisons **quantitatives** sans jamais mélanger résultats expérimentaux, estimations d'entreprises et modèles théoriques. Couvrir la **réglementation** (textes officiels datés).

## Livrables spécifiques
- Tableau « **coût de production du poulet conventionnel** » par pays/système (standard, certifié, bio) et postes de coût (aliment, poussin, main-d'œuvre, énergie, bâtiment) — sources : agri benchmark (Thünen), USDA ERS, ITAVI, Embrapa (CIAS), Eurostat/Commission européenne, FAOSTAT.
- Tableau « **TEA de la viande cultivée** » : auteur/année, espèce, financement, échelle, densité supposée, coût du milieu, durée de cycle, coût résultant, principaux leviers de sensibilité, nature (modèle vs données empiriques). Inclure au minimum : Humbird 2021, Risner et al. 2021, CE Delft 2021, Negulescu et al. 2023, Pasitka et al. 2024 (`SRC-X-0001`), Goodwin et al. 2024 (revue de cadrage des TEA), et toute TEA chinoise/japonaise/coréenne trouvée.
- Tableau « **ACV** » des trois voies (GES, énergie, eau, terres par kg de produit **et** par kg de protéine) : Sinke et al. 2023, Tuomisto ; Mattick et al. 2015 ; Lynch & Pierrehumbert 2019 ; Risner et al. 2023 (pré-publication, purification de qualité pharmaceutique) ; ACV du poulet (FAO GLEAM, Leinonen et al. 2012) ; ACV mycoprotéine/SCP/analogues ; Poore & Nemecek 2018.
- **Modèle économique transparent** (script Python dans `research/agents/E/models/`) comparant les voies avec scénarios prudent/intermédiaire/optimiste quand les données le permettent ; chaque paramètre rattaché à un `Q-…` ou marqué `model_assumption`. Analyse de sensibilité : quels paramètres déterminent réellement la rentabilité.
- Tableau « **installations industrielles** » : entreprise, site, volume annoncé, statut (annoncé, construit, en production, suspendu, abandonné), date, source (primaire de préférence).
- Section **réglementation** par juridiction (UE : règlement 2015/2283 nouveaux aliments, guide EFSA sur aliments issus de cultures cellulaires, dossiers déposés ; Italie loi d'interdiction 2023 ; autres interdictions nationales ; États-Unis : accord FDA–USDA 2019, consultations FDA, lois d'États interdisant la viande cultivée ; Singapour SFA ; Royaume-Uni FSA (bac à sable, aliments pour animaux de compagnie) ; Israël ; Australie/NZ FSANZ ; Corée MFDS ; Chine ; Japon ; Suisse ; Brésil). Distinguer autorisation d'**ingrédient**, de **procédé** et de **produit**. Inclure aliment animal (insectes, SCP) en lien avec l'agent N et nouveaux aliments fongiques/microbiens en lien avec l'agent A.

## Langues
en, fr (ITAVI, coûts de revient), pt (Embrapa, « custo de produção de frango »), es, zh (培养肉 成本 技术经济), de/nl (CE Delft, Thünen), ko/ja (cadres réglementaires).

## Conseils
- Monnaie et année d'origine toujours conservées ; conversion seulement avec source du taux/de l'indice.
- Le « coût » d'une TEA est une `model_output` ; un prix de vente au détail n'est pas un coût de production.
- Signale explicitement quand plusieurs chiffres circulant dans la presse remontent à une même TEA.
