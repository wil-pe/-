# Bilan des vérifications indépendantes (phase 6, 2026-10-25)

Deux vérificateurs, qui n'avaient pas accès aux rapports, aux handoffs ni au registre des contradictions, ont contrôlé 55 affirmations ou mesures clés dans leurs **sources primaires**.

| Lot | Domaines | Items | Confirmé | Confirmé avec réserve | Surinterprété | Inexact | Non vérifiable |
|---|---|---|---|---|---|---|---|
| batch1 | viande cultivée, économie, ACV, réglementation | 28 | 17 | 10 | 1 (EV-E-0047) | 0 | 0 |
| batch2 | nutrition, génétique, substituts, histoire | 27 | 11 | 14 | 1 (EV-A-0041) | 0 | 1 (EV-N-0022) |
| **Total** | | **55** | **28 (51 %)** | **24 (44 %)** | **2 (4 %)** | **0** | **1 (2 %)** |

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
