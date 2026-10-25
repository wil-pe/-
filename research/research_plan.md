# Plan de recherche — Chicken Muscle Research Lab

## Objet

Constituer une base de connaissances traçable pour découvrir comment produire du muscle de poulet (ou un équivalent) plus efficacement, selon trois voies comparées séparément :

- **Voie A — Optimisation de l'élevage** : maximiser le muscle comestible par unité de ressources.
- **Voie B — Viande cultivée** : produire du tissu musculaire de poulet sans élever d'animal jusqu'à l'abattage.
- **Voie C — Substituts** : produire un aliment aussi proche que possible du poulet sans (ou avec peu de) cellules animales.

Hors périmètre : œufs (sauf comme source de cellules ou de protéines), autres espèces (sauf comme points de comparaison explicitement marqués « extrapolation »).

## Architecture

| Agent | Domaine | Rapport | Préfixe ID |
|---|---|---|---|
| H | Histoire de l'alimentation des poules | `reports/history.md` | `SRC-H`, `EV-H`, `Q-H` |
| N | Nutrition et production de muscle (voie A) | `reports/poultry_nutrition.md` | `…-N-…` |
| C | Biotechnologies et viande cultivée (voie B) | `reports/cultivated_chicken.md` | `…-C-…` |
| A | Substituts et nouvelles protéines (voie C) | `reports/alternative_proteins.md` | `…-A-…` |
| E | Ingénierie, économie, industrialisation, réglementation | `reports/industrialization.md` | `…-E-…` |
| P | Brevets, recherche industrielle, innovation | `reports/patents_and_innovation.md` | `…-P-…` |
| X | Coordinateur : priorités, contrôle, déduplication, contradictions, synthèse | `reports/final_synthesis.md` | `…-X-…` |

Les agents ne communiquent pas directement : chaque agent publie `agents/<X>/handoff.md` ; le coordinateur lit les handoffs, consolide (`kb.py merge`), relance des vérifications indépendantes et redistribue les questions.

Le nombre d'agents n'augmente que si un domaine dépasse la capacité d'un agent (candidats identifiés : réglementation, ACV, Chine/Corée/Japon en langue originale).

## Phases

| Phase | Contenu | Livrable | État |
|---|---|---|---|
| 1 | Inspection des outils, périmètre | `coordination/capabilities.md` | fait |
| 2 | Questions, matrice domaines × sources, architecture, structure documentaire | `research_questions.md`, `coordination/coverage_matrix.md`, `coordination/protocol.md`, outils `tools/` | fait |
| 3 | Recherches exploratoires parallèles (6 agents) | premiers enregistrements, journaux, handoffs, brouillons de rapports | en cours |
| 4 | Recherches approfondies et collecte (texte intégral, sources primaires, langues) | registres enrichis | à venir |
| 5 | Extraction des données, déduplication | tables racine dédupliquées | à venir |
| 6 | Vérification scientifique, contradictions, vérifications croisées indépendantes | `contradictions.md`, statuts de vérification | à venir |
| 7 | Comparaison économique et environnementale, innovation | modèles, `innovation_opportunities.md` | à venir |
| 8 | Synthèse finale et audit qualité | `reports/final_synthesis.md`, audit | à venir |

## Critères de fin par domaine

Un domaine est « suffisamment couvert » lorsque, pour chacune de ses questions P1 :

1. les travaux fondateurs et les revues récentes (≤ 3 ans) ont été identifiés et au moins une revue lue en texte intégral ;
2. les principales approches concurrentes ont été examinées ;
3. des recherches explicites de **résultats contraires et négatifs** ont été menées et journalisées ;
4. au moins deux langues autres que l'anglais ont été explorées lorsque des communautés pertinentes existent ;
5. les chiffres clés sont rattachés à une source primaire (`verified_primary`) ou explicitement marqués comme non vérifiés ;
6. les incertitudes restantes sont documentées dans `knowledge_gaps.md`.

Si les nouveaux résultats se raréfient, avant de conclure : changer de termes, de langue, suivre les références (amont) et les citations (aval), explorer les domaines connexes (pharmacie biologique, fermentation industrielle, agronomie tropicale, génie des procédés alimentaires).

## Règles de comparaison (section 9 de la mission)

- Ne jamais additionner ni comparer des grandeurs de bases différentes : biomasse cellulaire humide ≠ matière sèche ≠ protéine ≠ tissu musculaire ≠ viande comestible ≠ produit fini.
- Pour les comparaisons inter-voies, la base de référence est **le kg de protéine comestible** et **le kg de produit comestible**, avec facteurs de conversion sourcés.
- Les coûts sont toujours étiquetés : mesuré / annoncé par une entreprise / estimé dans une publication / hypothèse de modèle / inconnu.
- Scénarios prudent / intermédiaire / optimiste seulement quand les données le permettent.
