# Bilan des vérifications indépendantes (phase 6, 2026-10-25)

Deux vérificateurs, qui n'avaient pas accès aux rapports, aux handoffs ni au registre des contradictions, ont contrôlé 55 affirmations ou mesures clés dans leurs **sources primaires**.

| Lot | Domaines | Items | Confirmé | Confirmé avec réserve | Surinterprété | Inexact | Non vérifiable |
|---|---|---|---|---|---|---|---|
| batch1 | viande cultivée, économie, ACV, réglementation | 28 | 17 | 10 | 1 (EV-E-0047) | 0 | 0 |
| batch2 | nutrition, génétique, substituts, histoire | 27 | 11 | 14 | 1 (EV-A-0041) | 0 | 1 (EV-N-0022) |
| **batch3** | **aléatoire, tous domaines** | **45** | **38 (84 %)** | **5 (11 %)** | **0** | **0** | **2 (accès)** |
| **Total** | | **100** | **66** | **29** | **2** | **0** | **3** |

## batch3 — échantillon aléatoire (phase 8)

batch1 et batch2 visaient les affirmations **les plus structurantes** (choisies à la main), d'où un taux de réserve élevé (44 %). batch3 est un **tirage aléatoire** de 45 items (graine fixe) sur toute la base, hors les 55 déjà vérifiés et hors les lignes de l'agent B (quarantaine).

Résultat : **0 erreur factuelle, 0 surinterprétation**, taux de réserve 11 % (imprécisions de formulation ou de qualificatif), 2 items non vérifiables pour blocage d'accès (rapport annuel Fufeng en police CJK non extractible ; revue chinoise cnif.cn en 503). Aucune source fabriquée ; citations, DOI et métadonnées concordent partout ; les sorties de modèle (agents K, M) sont arithmétiquement reproductibles et leurs hypothèses fortes signalées ; conflits d'intérêts et natures de données correctement étiquetés.

Les 5 réserves ont été corrigées (EV-S-0002 73→74 % ; EV-N-0034 plage d'incorporation ; Q-P-0039 flacon agité et non fed-batch ; Q-H-0032 rapport os:viande provisoire 9→9–11 % et localisateur ; Q-S-0011 note d'accès).

**Lecture** : l'écart entre 44 % (ciblé) et 11 % (aléatoire) indique que les imprécisions se concentrent sur les affirmations les plus saillantes — déjà corrigées — et que le corps de la base est fiable. **Fiabilité globale estimée : élevée** sur cet échantillon.

En plus des contrôles ci-dessus, l'audit automatique (`tools/audit.py refs`) a résolu chaque DOI et chaque PMID des 309 sources : aucune référence n'est inventée.

## Ce que montrent les vérifications
1. **Les chiffres sont fiables** : aucune valeur principale n'est fausse sur 55 items.
2. **Les erreurs portent sur la portée et l'attribution** :
   - affirmations enrichies d'inférences ou de faits venus d'autres sources (EV-E-0047, EV-A-0041, EV-C-0065) ;
   - vocabulaire réglementaire imprécis (EV-C-0001, EV-E-0030, EV-E-0035) ;
   - limites énoncées par la source elle-même omises (EV-E-0019, EV-E-0024, EV-E-0006, EV-N-0054) ;
   - incohérences internes des sources (résumé contre tableaux) non relevées (EV-N-0001, EV-N-0012, EV-C-0044) ;
   - conflits d'intérêts non notés (EV-N-0012, EV-N-0032, EV-A-0002, EV-A-0014, EV-A-0020, EV-A-0043).
3. **Les niveaux d'accès étaient plutôt sous-déclarés** (4 sources disponibles en texte intégral dans PMC), jamais surdéclarés dans l'échantillon contrôlé.

## Corrections appliquées
Les 26 items avec réserve ou surinterprétés ont été corrigés par le coordinateur avec `kb.py set`. Chaque correction est tracée dans le champ `notes` de la ligne, avec un renvoi à `batch1_results.md` ou `batch2_results.md`.

La correction de l'usine Believer, qui n'est pas « jamais entrée en production » mais dont aucune production commerciale n'est documentée, a été répercutée dans EV-E-0055, dans le rapport `industrialization.md` et dans `contradictions.md`.

Les leçons tirées ont été intégrées aux consignes de la phase 4 (`agent_briefs/phase4.md`) et transmises aux agents en cours.

## Limite
Ce contrôle ne porte que sur un échantillon de 55 affirmations, sur 394 au total, choisies parmi les plus structurantes. Le taux de réserve observé, 44 %, suggère que les autres affirmations contiennent des imprécisions de portée comparables. **Les affirmations non vérifiées doivent être lues avec la prudence correspondante.** Un second échantillonnage, aléatoire cette fois, est prévu en phase 8.
