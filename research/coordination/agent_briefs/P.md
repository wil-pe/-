# Brief — Agent P : Brevets, recherche industrielle et innovation

**Lettre** : P · **Rapport** : `research/reports/patents_and_innovation.md` · **Questions** : RQ-P1 à RQ-P5, responsable principal de RQ-X5.

## Mission
Cartographier publications, brevets, laboratoires, entreprises, prototypes, procédés expérimentaux, **projets abandonnés et résultats négatifs**, technologies insuffisamment explorées. Identifier les problèmes techniques **sans solution satisfaisante**, puis proposer de nouvelles pistes de recherche avec leurs fondements, risques, coûts potentiels et expériences de validation.

## Livrables spécifiques
- `research/agents/P/patent_map.csv` (créé avec Python/csv, colonnes : `patent_number, title, assignee_original, assignee_current, priority_date, publication_date, jurisdiction, family_hint, domain (B-cell-line|B-media|B-bioreactor|B-scaffold|B-product|C-plant|C-myco|C-SCP|C-precision-fermentation|A-feed|A-genetics|other), key_claim_summary_fr, source_id, access (page_read|abstract_only|secondary)`). Chaque brevet consulté est aussi enregistré comme source (`source_type=patent`). Objectif : ≥ 40 brevets représentatifs, avec répartition par déposant et par pays — **échantillon, pas exhaustivité** (Espacenet/PATENTSCOPE bloqués ; utiliser Google Patents via `WebFetch` et `WebSearch` avec `allowed_domains=["patents.google.com"]`).
- `research/agents/P/actors.csv` (entreprises, laboratoires, chercheurs : nom, pays, voie, technologie, statut, financements si sourcés, source_id).
- Tableau « **échecs et abandons** » : acteur/projet, date, ce qui a échoué (technique, économique, réglementaire, financement), preuve (source primaire si possible), leçon.
- Inventaire « **problèmes non résolus** » (lien avec `knowledge_gaps.md` que le coordinateur consolidera).
- **Pistes de recherche** (≥ 8), chacune répondant aux 10 questions : problème précis ; solutions actuelles ; insuffisances ; preuves suggérant une nouvelle approche ; technologies à combiner ; hypothèses ; expérience de test ; coûts et difficultés ; critères succès/échec ; étape suivante. Classer : **amélioration réalisable** / **innovation à développer** / **hypothèse spéculative**.

## Pistes à explorer (à vérifier)
- Brevets viande cultivée : Memphis Meats/UPSIDE (ex. WO2018208628A1, voie HIPPO/YAP pour densité — page consultable), Future Meat/Believer (fibroblastes de poulet immortalisés spontanément, perfusion), JUST/GOOD Meat, SuperMeat, Aleph Farms, Mosa Meat (milieux), Integriculture (CulNet), Vital Meat, Gourmey, Meatable, Wildtype ; universités chinoises (CNIPA : 江南大学, 南京农业大学) et coréennes.
- Brevets substituts : extrusion humide/cellule de cisaillement, mycoprotéine (Marlow Foods, Emergy/Meati, Nature's Fynd, Enough), SCP (Solar Foods, Calysta, Unibio).
- Brevets nutrition avicole (échantillon) : acides aminés, phytases, procédés de protéines d'insectes pour aliment.
- Abandons/faillites et réductions d'activité (à confirmer par sources primaires : communiqués, registres, presse fiable) : New Age Eats (2023), SCiFi Foods (2024), suspension de projets d'usines (UPSIDE, GOOD Meat), autres ; pivots vers l'alimentation animale de compagnie ou les cosmétiques ; échecs dans les SCP (ex. Deep Branch ?).
- Résultats négatifs publiés (différenciation, densité, coût des milieux, contamination, purification de l'endotoxine des facteurs recombinants).
- Domaines connexes sous-exploités : biofabrication pharmaceutique (perfusion intensifiée), bioréacteurs à lit fixe, co-culture, ingénierie métabolique des cellules (auxotrophies, glutamine synthétase, cycle de l'urée), production autocrine de facteurs de croissance, hybrides fermentation microbienne + cellules animales, valorisation des coproduits d'abattoir/couvoir, aliment volaille issu de SCP.

## Langues
en, zh (专利 细胞培养肉, 培育肉), ja (特許 培養肉), ko (특허 배양육), he/en, fr, de, nl, es, pt.

## Conseils
- Une revendication de brevet n'est **pas** une preuve que la technique fonctionne : `evidence_type=patent_claim`, confiance au plus `low` sauf données expérimentales.
- Date de priorité ≠ date de publication ; déposant d'origine ≠ titulaire actuel.
- Les annonces de faillite doivent être confirmées par au moins une source primaire ou deux médias indépendants.
