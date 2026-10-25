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
| 3 Recherches exploratoires parallèles | ✅ 6 agents terminés (H, N, C, A, E, P) |
| 4 Approfondissements ciblés | 🟨 5 agents lancés (B procédé aviaire, M économie nutrition, S substituts, R réglementation, K comparaison) — consignes `coordination/agent_briefs/phase4.md` |
| 5 Extraction, déduplication | ✅ fusion `kb.py merge` (308 sources uniques, 1 doublon), audit des références (0 référence inventée) |
| 6 Vérification, contradictions | ✅ 55 affirmations contre-vérifiées (0 inexact, 24 réserves, 2 surinterprétations, 1 non vérifiable — corrigées) ; `contradictions.md` (24), `knowledge_gaps.md`, matrice de couverture |
| 7 Comparaison, innovation | 🟨 `innovation_opportunities.md` v1 (21 pistes classées) ; comparaison homogène en cours (agent K) |
| 8 Synthèse, audit | 🟨 `reports/final_synthesis.md` v0.1 (intermédiaire) |

## Session 1 — 2026-10-25

- Inspection des capacités : WebSearch, WebFetch, PubMed (MCP + E-utilities), Europe PMC, Crossref, Consensus (3 résultats), J-STAGE, HAL, theses.fr, archive.org, OSTI, Google Patents (pages via WebFetch) opérationnels ; OpenAlex, Semantic Scholar, Google Scholar, Espacenet, PATENTSCOPE, CAB, CNKI, SciELO, Gallica bloqués ou limités.
- Création de la structure, du protocole, des outils `tools/kb.py` (validation, ID, déduplication) et `tools/search.py` (clients API).
- Rédaction des 33 questions de recherche priorisées et des consignes des 6 agents.
- Première source de contrôle enregistrée par le coordinateur : `SRC-X-0001` (Pasitka et al. 2024, *Nature Food*, métadonnées vérifiées via Crossref, résumé seul).
- Lancement en parallèle des agents H, N, C, A, E, P (phase 3 exploratoire + premier approfondissement).

### Résultats de la phase 3 (agents terminés)
- H : 53 sources, 66 affirmations, 63 mesures ; N : 51/74/81 ; C : 43/76/86 ; A : 46/51/67 ; E : 42/59/72 (+ modèle `agents/E/models/`).
- Audit `tools/audit.py refs` : tous les DOI/PMID de H, N, C, A, E se résolvent et les titres concordent (4 DOI non-Crossref, dont 1 DOI chinois imprimé mais non déposé).
- Corrections du coordinateur tracées dans les champs `notes` et listées en fin de `contradictions.md`.
- Recalcul du coordinateur (EV-X-0001) : avec la composition mesurée (9 % de protéines), la protéine cultivée coûte 85/225/670 USD/kg dans le modèle de l'agent E.
- Outils : correctif des titres non latins dans `kb.py` (faux doublons), commande `kb.py set`, client Crossref/J-STAGE réparés, type `documentary_verification` ajouté.

### Phases 5–6 (même session)
- Agent P terminé (73 sources, 44 brevets, `agents/P/patent_map.csv`, `actors.csv`).
- Vérification indépendante de 55 affirmations clés : `coordination/verification/summary.md` ; corrections appliquées et tracées.
- Corrections notables : usine Believer (« jamais en production » non soutenu → « aucune production commerciale documentée ») ; vocabulaire FDA (« no questions » ≠ autorisation) ; incohérences résumé/tableaux (Zuidhof 2014 : −42 % d'IC, pas −50 %).
- Nouveaux types de preuve : `documentary_verification`, `press_report`, `data_compilation`, `archaeometric_measurement`.

## Prochaines actions du coordinateur

- À la fin des agents de phase 4 : `kb.py check`, `audit.py refs <lettre>`, `audit.py consistency`, `kb.py merge`, lecture des handoffs ; mise à jour de `contradictions.md` (CT-01 à CT-06 en particulier), `knowledge_gaps.md`, matrice de couverture.
- Intégrer la comparaison homogène de l'agent K dans la synthèse (phase 7) et réviser le classement `innovation_opportunities.md`.
- Phase 8 : second échantillonnage de vérification, **aléatoire** (≈ 40 affirmations), puis synthèse finale v1.
- Points en attente d'un humain : PDF HAL hal-01995110 (Laisse et al. 2018, anti-bot) ; clé API OpenAlex éventuelle ; textes intégraux *Nature Food* (Pasitka 2023/2024/2025).
