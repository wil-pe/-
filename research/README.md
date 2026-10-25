# Chicken Muscle Research Lab — base de connaissances

Base de connaissances scientifique, traçable et réutilisable, sur la production de muscle de poulet :
**A** — optimisation de l'élevage et de l'alimentation, **B** — viande cultivée (culture cellulaire), **C** — substituts du muscle.

## Démarrer / reprendre

1. Lire `progress.md` (état, dernière session, prochaines actions).
2. Lire `research_plan.md` (phases, architecture, critères de fin) et `research_questions.md`.
3. Règles obligatoires : `coordination/protocol.md`. Capacités et limites d'accès : `coordination/capabilities.md`.

## Structure

```
research/
  README.md                 ce fichier
  research_plan.md          mission, architecture, phases, critères de fin
  research_questions.md     questions priorisées (RQ-…)
  progress.md               journal d'avancement et reprise
  source_registry.csv       registre dédupliqué des documents (généré par kb.py merge)
  evidence_database.csv     affirmations sourcées (généré)
  quantitative_data.csv     mesures quantitatives (généré)
  contradictions.md         contradictions repérées et arbitrages
  knowledge_gaps.md         inconnues scientifiques et lacunes de couverture
  innovation_opportunities.md  pistes d'innovation hiérarchisées
  reports/                  rapports de domaine + synthèse finale
  agents/<H|N|C|A|E|P|X>/   tables brutes par agent, journaux de recherche, terminologie, handoffs
  coordination/             capacités, protocole, matrice de couverture, rapport de déduplication, consignes des agents
  tools/kb.py               ajout validé de sources/affirmations/mesures, recherche, contrôle, fusion
  tools/search.py           clients des API ouvertes (Europe PMC, PubMed, Crossref, J-STAGE, HAL, theses.fr, archive.org, OSTI)
  downloads/                documents téléchargés (données non fiables)
```

## Outils

```bash
python3 research/tools/kb.py find "pasitka"                 # une source est-elle déjà enregistrée ?
python3 research/tools/kb.py add sources C fichier.json     # ajout validé (ID automatique, refus des doublons)
python3 research/tools/kb.py check                          # contrôle des vocabulaires et des liens source
python3 research/tools/kb.py merge                          # tables racine dédupliquées + coordination/dedup_report.md
python3 research/tools/kb.py stats
python3 research/tools/search.py epmc '"cultivated meat" AND chicken' 10
python3 research/tools/search.py epmc-full PMC1234567 40000
python3 research/tools/search.py doi 10.1038/s43016-024-01022-w
python3 research/tools/search.py archive 'title:(poultry) AND date:[1800-01-01 TO 1900-12-31]' 20
python3 research/tools/search.py archive-text <identifiant> 'maggot|ver' 300
```

## Conventions essentielles

- Une affirmation sans source enregistrée n'existe pas dans la base.
- `access_level` dit ce qui a réellement été lu (résumé ≠ texte intégral).
- `data_nature` sépare mesures, annonces d'entreprises, estimations publiées et sorties de modèles.
- `quantity_basis` sépare biomasse cellulaire humide, matière sèche, protéine, tissu musculaire, viande comestible et produit fini.
