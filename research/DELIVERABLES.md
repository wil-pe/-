# Livrables — correspondance avec la mission (section 14)

État au 2026-10-25 (fin de phase 4, phase 8 en cours). Légende : ✅ présent · 🟧 présent, à compléter · ⬜ non commencé.

| # | Livrable demandé | Fichier(s) | État |
|---|---|---|---|
| 1 | Cartographie scientifique | `research_questions.md` + `coordination/coverage_matrix.md` + `coordination/coverage_auto.md` | ✅ |
| 2 | Chronologie historique de l'alimentation des poules | `reports/history.md` (§3 Chronologie) | ✅ |
| 3 | Catalogue des ingrédients et ressources alternatives | `reports/poultry_nutrition.md` (§3.3) + `reports/alternative_proteins.md` (§3) | ✅ |
| 4 | Base bibliographique dédupliquée | `source_registry.csv` + `reports/bibliography.md` (456 sources uniques, 17 langues) + `coordination/dedup_report.md` | ✅ |
| 5 | Base de données quantitative | `quantitative_data.csv` (898 mesures, base/échelle/nature typées) | ✅ |
| 6 | Synthèse de la production de muscle de poulet | `reports/poultry_nutrition.md` | ✅ |
| 7 | Analyse approfondie de la viande cultivée | `reports/cultivated_chicken.md` (niveau coûts/obstacles/réglementation ; procédés non détaillés, cf. note B) | 🟧 |
| 8 | Comparaison des substituts | `reports/alternative_proteins.md` + `reports/deep/S_substituts_nutrition_energie.md` | ✅ |
| 9 | Cartographie des brevets, chercheurs et entreprises | `reports/patents_and_innovation.md` + `agents/P/patent_map.csv` + `agents/P/actors.csv` | ✅ (échantillon) |
| 10 | Analyse économique et environnementale | `reports/industrialization.md` + `reports/deep/K_comparaison_voies.md` + `agents/{E,K}/models/` | ✅ |
| 11 | Inventaire des questions scientifiques non résolues | `knowledge_gaps.md` | ✅ |
| 12 | Liste hiérarchisée d'opportunités d'innovation | `innovation_opportunities.md` (21 pistes classées) | ✅ |
| 13 | Rapport final avec recommandations | `reports/final_synthesis.md` (v0.2 ; v1 après la 2e vérification) | 🟧 |

## Bases de données (section 7)
- `source_registry.csv` — registre des sources (déduplication par DOI, PMID, titre normalisé, URL).
- `evidence_database.csv` — 647 affirmations sourcées, avec citation, niveau de preuve, contradictions.
- `quantitative_data.csv` — 898 mesures, chacune avec sa base (`quantity_basis`), son échelle et sa nature (`data_nature`).

## Rapports d'approfondissement (phase 4)
- `reports/deep/M_economie_nutrition.md`, `reports/deep/S_substituts_nutrition_energie.md`, `reports/deep/R_reglementation.md`, `reports/deep/K_comparaison_voies.md`.
- (L'approfondissement « données de procédé des cellules aviaires » a été interrompu par la politique d'usage ; voir `agents/B/handoff.md`.)

## Traçabilité et contrôle
- `coordination/verification/summary.md` + `batch1/2/3_results.md` — vérifications indépendantes.
- `coordination/audit_*.md` — audits automatiques (références, cohérence, couverture).
- `coordination/dedup_report.md`, `coordination/deletions.log`.
- `progress.md` — journal de reprise.

## Reste à faire
- Phase 8 : second échantillon de vérification **aléatoire** (en cours, batch3) ; puis `final_synthesis.md` v1.
- Livrable 7 : les lacunes de procédé de la voie B (KG-B01, B04, B05, B06) restent ouvertes et signalées comme telles.
- En attente d'un humain : PDF HAL hal-01995110 ; clé OpenAlex ; textes intégraux *Nature Food* (Pasitka).
