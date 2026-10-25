# Journal d'avancement

## Reprendre le travail (lire en premier)

1. `git checkout claude/chicken-muscle-research-lab && git pull origin claude/chicken-muscle-research-lab`
2. Lire ce fichier, puis `research_plan.md` et `coordination/protocol.md`.
3. `python3 research/tools/kb.py stats` puis `python3 research/tools/kb.py check` pour l'état de la base.
4. Lire les `agents/<X>/handoff.md` : chaque handoff liste les recherches prioritaires restantes.
5. Pour relancer un agent : lui donner `coordination/agent_briefs/_common.md` + `coordination/agent_briefs/<X>.md` + son handoff, en précisant la phase.

## État courant

| Phase | État |
|---|---|
| 1 Inspection des outils, périmètre | ✅ fait (`coordination/capabilities.md`) |
| 2 Questions, matrice, architecture, structure | ✅ fait |
| 3 Recherches exploratoires parallèles | 🟨 en cours (6 agents lancés) |
| 4–8 | ⬜ |

## Session 1 — 2026-10-25

- Inspection des capacités : WebSearch, WebFetch, PubMed (MCP + E-utilities), Europe PMC, Crossref, Consensus (3 résultats), J-STAGE, HAL, theses.fr, archive.org, OSTI, Google Patents (pages via WebFetch) opérationnels ; OpenAlex, Semantic Scholar, Google Scholar, Espacenet, PATENTSCOPE, CAB, CNKI, SciELO, Gallica bloqués ou limités.
- Création de la structure, du protocole, des outils `tools/kb.py` (validation, ID, déduplication) et `tools/search.py` (clients API).
- Rédaction des 33 questions de recherche priorisées et des consignes des 6 agents.
- Première source de contrôle enregistrée par le coordinateur : `SRC-X-0001` (Pasitka et al. 2024, *Nature Food*, métadonnées vérifiées via Crossref, résumé seul).
- Lancement en parallèle des agents H, N, C, A, E, P (phase 3 exploratoire + premier approfondissement).

## Prochaines actions du coordinateur

- À la fin des agents : `kb.py check`, `kb.py merge`, lecture des handoffs, consolidation de `contradictions.md`, `knowledge_gaps.md`, `innovation_opportunities.md`, mise à jour de la matrice de couverture.
- Vérifications indépendantes croisées des chiffres clés (coût, densité, IC) par un agent différent de celui qui les a enregistrés.
- Décider de la phase 4 (approfondissements ciblés) et d'éventuels agents supplémentaires.
