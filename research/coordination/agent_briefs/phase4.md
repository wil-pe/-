# Phase 4 — approfondissements ciblés (consignes communes + 5 missions)

Les consignes de `_common.md` et `protocol.md` restent applicables (outils, enregistrement via `kb.py`, honnêteté sur l'accès, journal, terminologie, handoff). Différences pour la phase 4 :

- Tu **prolonges** le travail d'un agent de phase 3 : lis d'abord son handoff et son rapport (indiqués ci-dessous), puis `research/knowledge_gaps.md`, `research/contradictions.md` et `research/innovation_opportunities.md`. Ne refais pas ce qui est déjà enregistré (`kb.py find`).
- Tu écris sous **ta propre lettre** (dossier `research/agents/<lettre>/`) et tu rédiges un rapport d'approfondissement `research/reports/deep/<lettre>_<thème>.md` (≈ 2 000–4 000 mots), qui cite ses identifiants et indique explicitement quelles lacunes (`KG-…`) et contradictions (`CT-…`) il réduit ou résout.
- **Langues** : au moins **30 % de sources non anglophones** quand une communauté existe (chinois, portugais, espagnol, japonais, coréen, allemand, français…). Ce biais (85 % de sources en anglais en phase 3) est la première faiblesse du corpus.
- **Leçons de l'audit de phase 3** : ne mets jamais `confidence=high` sur une déclaration d'entreprise, un brevet ou un modèle ; un document lu en métadonnées seules ne peut pas porter une confiance `moderate` ; si tu lis le texte intégral d'une source déjà enregistrée en `abstract_only`, mets à jour son `access_level` avec `kb.py set` et note-le ; vérifie qu'un chiffre cité « d'après une revue » existe bien dans la source primaire, et sinon dis-le.
- Objectif : **20 à 40 sources nouvelles**, dont la majorité lue en texte intégral ou par sections pertinentes ; 30 à 60 affirmations ; autant de mesures que pertinent.
- Réponse finale (≤ 400 mots) : lacunes réduites (`KG-…`), contradictions résolues ou précisées (`CT-…`), chiffres nouveaux clés, limites d'accès, recherches restantes.

---

## Mission B2 (lettre **B**) — Données de procédé pour cellules aviaires : FDA, brevets, industrie vaccinale
Prolonge l'agent C (`research/agents/C/handoff.md`, `research/reports/cultivated_chicken.md`). Lacunes visées : KG-B01, KG-B04, KG-B05, KG-B06, KG-COV-05, KG-COV-06 ; contradictions CT-01 à CT-06.
1. **FDA** : lis les documents publics de pré-commercialisation (*Scientific Memo*, *Disclosable safety narrative*, *Response letter*) pour UPSIDE (CCC 000002), GOOD Meat (CCC 000001 ?) et Believer (CCC 000039 ?) sur fda.gov (inventaire « Human Food Made with Cultured Animal Cells »). Extrais : lignée, milieu (sérum, facteurs, antibiotiques), procédé, échelle, composition chiffrée (protéines, lipides, eau, minéraux), contaminants, spécifications.
2. **Pasitka 2023/2024/2025 et Future Meat/Believer** : cherche les données que les articles payants contiennent via des routes légales — prépublications bioRxiv/Research Square, manuscrits auteur (PMC, dépôt de l'Université hébraïque), **données et méthodes supplémentaires** (souvent en accès libre chez Nature), **brevets** de la même équipe (les exemples reprennent souvent les données). Objectif : la base du « 43 % p/v », les litres de milieu par kg, la composition du milieu à 0,63 USD/L et la base du coût de 6,2 USD/lb (CT-02, CT-03).
3. **Industrie vaccinale** (source sous-exploitée) : la bioproduction de vaccins utilise depuis des décennies des cellules aviaires en bioréacteur (fibroblastes d'embryon de poulet, DF-1, EB66/EBx de Valneva, AGE1.CR/canard, QT6/QM7 de caille). Cherche les densités atteintes, les débits spécifiques de consommation d'O₂ (qO₂), de glucose et de glutamine, la production d'ammoniac et de lactate, les milieux sans sérum, les modes (fed-batch, perfusion, ATF/TFF), les volumes (jusqu'à quelle échelle ?). Indique clairement l'extrapolation de cellules vaccinales vers l'alimentaire.
4. Langues : en, zh (鸡胚成纤维细胞 生物反应器, DF-1 细胞 悬浮培养, 无血清), ja, ko, de, fr.

## Mission N2 (lettre **M**) — Économie de la nutrition et littérature non anglophone (voie A)
Prolonge l'agent N (`research/agents/N/handoff.md`, `research/reports/poultry_nutrition.md`). Lacunes : KG-A01, KG-A03, KG-A04, KG-COV-08, KG-COV-09, KG-COV-11 ; RQ-X3 ; CT-12, CT-20, CT-21.
1. **Prix** des acides aminés de synthèse (L-lysine HCl/sulfate, DL-méthionine, L-thréonine, L-valine, L-isoleucine, glycine) et du tourteau de soja, séries 2015–2026 (sources statistiques, rapports d'entreprises cotées — étiqueter), coût d'un point de PB en moins ; **qualité alimentation animale vs qualité milieu de culture** (pureté, métaux lourds, endotoxines) — pont avec INN-01.
2. Littérature **chinoise** (低蛋白日粮 肉鸡, 黑水虻 肉鸡, 饲料转化率 遗传进展) et **brésilienne** (frango de corte proteína bruta reduzida, larvas de mosca soldado negra, Embrapa custo de produção) : priorité aux revues en accès libre (Revista Brasileira de Zootecnia, Ciência Rural, Pesquisa Agropecuária Brasileira, 动物营养学报, 中国畜牧杂志, 饲料工业…).
3. **Insectes** : méta-analyses dose-réponse chez le poulet de chair (fraction entière/dégraissée, âge) → CT-12.
4. **Tables** : INRAE-CVB, Rostagno 2017/2024, NRC 1994 (ce qui est accessible), composition de la viande de poulet (CIQUAL, USDA FoodData Central) pour consolider la chaîne aliment → protéine comestible.
5. Souches à croissance lente en conditions commerciales et texte du Better Chicken Commitment.

## Mission A2 (lettre **S**) — Substituts : nutrition, énergie, coûts, arôme (voie C)
Prolonge l'agent A (`research/agents/A/handoff.md`, `research/reports/alternative_proteins.md`). Lacunes : KG-C01 à KG-C06 ; CT-11.
1. **DIAAS mesurés** : filet de poulet, mycoprotéine, protéines bactériennes, analogues commerciaux (Hodgkinson 2025 et autres).
2. **Énergie et coûts industriels** : extrusion humide (kWh/kg, débit), cellule de cisaillement, mycoprotéine (TEA : Upcraft 2021 et autres), SCP hydrogénotrophes et méthanotrophes (énergie par kg de protéine, coûts).
3. **ACV primaires** : Quorn, Solein, FeedKind, analogues végétaux, sur base produit **et** base protéine → CT-11.
4. **Arôme poulet** : composés clés (GC-O, AEDA) du poulet cuit et des analogues ; brevets d'arômes de réaction.
5. Langues : en, zh (高水分挤压 能耗, 菌体蛋白 成本), ja, de, nl, fi (Solar Foods), id, ko.

## Mission R (lettre **R**) — Réglementation (section 12 de la mission)
Prolonge l'agent E (`research/agents/E/handoff.md`, section 8 de `research/reports/industrialization.md`). Lacune : KG-COV-12 ; CT-19.
Pour chaque juridiction — UE (règlement 2015/2283, guide EFSA 2024 sur les aliments issus de cultures cellulaires, demandes déposées dans OpenEFSA/registre de la Commission, règlement 2021/1372 et statut des SCP/insectes en alimentation animale), France, Italie, Hongrie et autres projets d'interdiction, Royaume-Uni (FSA, bac à sable, aliments pour animaux de compagnie), Suisse (OSAV), Israël, Singapour, Corée (MFDS), Japon (MHLW), Chine (NHC, nouveaux aliments, 新食品原料), Australie/NZ (FSANZ), États-Unis (FDA/USDA, AAFCO, lois des États : Alabama, Mississippi, Montana, Indiana, Nebraska, Dakota du Sud, Floride, Texas…), Brésil (ANVISA, MAPA) — établis un tableau **texte officiel daté** (titre, numéro, date, URL officielle) et distingue autorisation d'**ingrédient**, de **procédé** et de **produit**, alimentation humaine vs animale, statut OGM. Contourne EUR-Lex (page vide) par publications.europa.eu, data.europa.eu ou les journaux officiels nationaux. Langues : en, fr, it, de, ko, ja, zh, pt, he, hu.

## Mission X2 (lettre **K**) — Comparaison homogène des trois voies (phase 7, collecte des données)
Utilise les tables existantes (`research/quantitative_data.csv`) et `research/coordination/comparison_framework.md`. Lacunes : KG-X01, KG-X02, RQ-X2 ; CT-10.
1. Complète les facteurs de conversion manquants avec des **sources primaires** : rendement en viande désossée selon les systèmes (standard, Label Rouge, bio), composition de la viande (protéines crue/cuite), eau, énergie et surface par kg de poulet (FAO GLEAM, ACV européennes et brésiliennes), et les mêmes grandeurs pour les procédés de la voie C et pour les scénarios de la voie B (Sinke, Risner, Humbird).
2. Coûts du poulet après 2017 (étude AVEC/Wageningen 2026 si elle existe, ITAVI, USDA ERS, Embrapa CIAS, agri benchmark).
3. Construis `research/agents/K/models/comparison.py` (lecture des `Q-…` réels, aucune valeur inventée ; hypothèses marquées) et un tableau final : coût, GES, énergie, eau, surface **par kg de protéine comestible**, pour A (standard, certifié, bio), B (scénarios publiés et recalcul à 9 % de protéines, EV-X-0001) et C (ingrédients et produits disponibles), avec la nature de chaque chiffre.
