# Matrice de couverture

Mise à jour par le coordinateur à partir des journaux `agents/<X>/search_log.md`, des tables et des handoffs.
Légende état : ⬜ non commencé · 🟨 exploratoire · 🟧 approfondi · 🟩 critères de fin atteints · ⛔ bloqué (accès).

## 1. Domaines × sources prévues

| Domaine | Bases scientifiques | Organismes / données | Brevets | Historique / autres | Langues prioritaires |
|---|---|---|---|---|---|
| H Histoire | Europe PMC, Crossref, HAL, J-STAGE (archéozoologie, histoire agricole) | FAO (systèmes traditionnels), musées | — | archive.org (traités 1600–1925), textes classiques (Columelle, Varron, Palladius), 齐民要术, Ibn al-ʿAwwām | en, fr, zh, la, ar, es, pt, ja, hi |
| N Nutrition | PubMed, Europe PMC, Crossref, Consensus, HAL/theses.fr, J-STAGE | NRC, INRAE/CVB, Aviagen/Cobb (guides), FAO, EFSA (additifs), USDA | brevets additifs (échantillon) | — | en, fr, zh, pt, es, de, ja, ko, ru, th, id, vi, tr |
| C Viande cultivée | PubMed, Europe PMC (dont bioRxiv), Crossref, Consensus, J-STAGE | FDA/USDA, SFA, FSANZ, EFSA, GFI | Google Patents (pages) | presse spécialisée (à vérifier) | en, zh, ja, ko, he, nl, fr, es, de |
| A Substituts | PubMed, Europe PMC, Crossref, Consensus | EFSA (nouveaux aliments), FAO | Google Patents | traditions culinaires | en, zh, ja, id, fr, de, nl, es, ko, th, vi |
| E Économie/industrie | Europe PMC, Crossref, OSTI, Consensus | FAOSTAT, USDA ERS, agri benchmark, ITAVI, Eurostat, CE Delft, GFI ; EUR-Lex, FDA, SFA… | — | rapports industriels (marqués company_claim) | en, fr, pt, es, zh, de, nl |
| P Brevets/innovation | Crossref, Europe PMC | registres d'entreprises, rapports GFI | Google Patents (WebFetch), WebSearch ciblé | presse (faillites, abandons — à vérifier) | en, zh, ja, ko, he, fr, de, nl |

## 2. Questions × état de couverture (état au 2026-10-25, fin de phase 3)

Chiffres agrégés par agent : `coordination/coverage_auto.md` (généré). Légende : ⬜ non commencé · 🟨 exploratoire · 🟧 approfondi · 🟩 critères de fin atteints · ⛔ bloqué.

| Question | Sources principales trouvées | Langues explorées | Résultats disponibles | Contradictions | Lacunes | Recherches restantes | État |
|---|---|---|---|---|---|---|---|
| RQ-X1 coût mesuré vs projeté | statistiques UE/FR/BR/US (2017, 2022), 6 TEA, modèle E | en, fr, pt, es, it | A : coûts statistiques ; B : sorties de modèles uniquement ; C : prix d'ingrédients | CT-02, CT-08, CT-10 | coûts du poulet après 2017 ; TEA de la mycoprotéine et des SCP | Pasitka 2024 texte intégral ; TEA des substituts | 🟧 |
| RQ-X2 ressources par kg de protéine | ACV Sinke, Risner, Mostert, Smetana, Shahid ; modèle E | en, fr | GES par kg de protéine pour A et B ; C partiel | CT-09, CT-11, CT-15 | eau, terres, énergie sur base homogène ; ACV du poulet cultivé | ACV primaires (GLEAM, Quorn, Solein) | 🟨 |
| RQ-X3 goulets partagés | E-3, P-3, A-4, EV-A-0014, EV-P-0060 | en | soja/SCP communs à A, B, C ; plasma d'abattoir (A+B) | — | prix des acides aminés de synthèse vs soja | prix des AA ; hydrolysats « qualité milieu » | 🟨 |
| RQ-X4 réglementation | textes officiels UE, IT, US (fédéral, FL, TX), SG, FSANZ | en, it, ja, ko, pt | autorisations et interdictions datées | CT-19 | MFDS, NHC, OSAV, Israël, 6 États US ; règlement 2021/1372 (aliment animal) | textes primaires restants | 🟧 |
| RQ-X5 espaces d'innovation | 29 pistes → 21 consolidées | — | `innovation_opportunities.md` | — | expériences non réalisées | vérification des preuves de base | 🟨 |
| RQ-H1 premiers régimes | Ban Non Wat, isotopes (Pompéi, Catalogne, Oyo), faisans nourris au millet en Chine | en, zh | régimes régionaux documentés | CT-16 | isotopes des premiers poulets d'Asie | 鸡骨 稳定同位素 食性 (Wanfang) | 🟧 |
| RQ-H2 textes anciens | Varron, Columelle, Pline, Géoponiques, Ibn al-ʿAwwām, 齊民要術 | la, el, ar, zh, fr, en | protocole de finition stable sur 2 000 ans | CT-17 | traductions critiques non consultées | ctext.org (authentification) | 🟧 |
| RQ-H3 systèmes traditionnels | études villageoises (Sri Lanka, Mexique), termites (Afrique de l'Ouest) | en, fr, es, hi | composition de jabots, pratiques | CT-18 | rendements des termitières et des asticots ; azolla, intégration poulet-poisson | Farina et al. 1991 | 🟨 |
| RQ-H4 industrialisation | Eijkman, vitamine D, AGP, lysine, Danemark (arrêt des AGP) | en, fr, ja, de | chronologie datée | — | JBC 1922–1925 (403) ; 1ʳᵉ phytase commerciale ; 1ʳᵉ programmation linéaire pour volailles | archive.org 1900–1930 | 🟧 |
| RQ-H5 innovations oubliées | verminières, finition lactée, cuisson des grains (Réaumur) | fr, la, ar, zh, en | 3 pistes (INN-18 à INN-20) | CT-17 | essais modernes | — | 🟧 |
| RQ-N1 IC, génétique | Zuidhof 2014, guides Ross, données de terrain FR/US | en, fr, pt, zh | IC 2,88 → 1,67 à régime identique | — | Havenstein en texte intégral | ScienceDirect (403) | 🟧 |
| RQ-N2 besoins, basse protéine | Belloir, méta-analyses basse protéine | en, fr, zh | −1,2 à −1,9 % d'IC par point de PB ; plancher ~17 % | CT-21 | INRAE-CVB, Rostagno, NRC 1994 | tables | 🟧 |
| RQ-N3 additifs | protéases, phytase | en | effets conditionnels | — | méta-analyses chiffrées phytase/xylanase | — | 🟨 |
| RQ-N4 microbiote | probiotiques, Jansseune 2025 | en, fr | effets fragiles | CT-22 | — | — | 🟨 |
| RQ-N5 biologie du muscle | myopathies (Ontario), in ovo | en | prévalence des myopathies | CT-23 | mécanismes (KG-A02) | — | 🟨 |
| RQ-N6 limites physiologiques | modèle (~8 % d'énergie récupérable), souches lentes | en | +14 à 28 % d'aliment pour les souches lentes | — | texte du BCC ; souches lentes en conditions commerciales | — | 🟨 |
| RQ-N7 ressources alternatives | insectes, SCP, colza, féverole… | en, zh, pt, es | pas d'alternative unique au soja | CT-12 | lentille d'eau, manioc, tournesol ; littérature chinoise et brésilienne | CNKI, SciELO | 🟨 |
| RQ-N8 rendements, protéine comestible | guides Ross, études FR | en, fr | 61–64 g de protéine de viande par kg d'aliment (rapide), 32 g (Label Rouge) | CT-20 | composition de la viande (CIQUAL) | — | 🟧 |
| RQ-C1 types cellulaires | FDA (3 dossiers), FSANZ, Pasitka 2023, DF-1 | en, zh, ja, ko, he | fibroblastes immortalisés spontanément = base industrielle | CT-07 | lignées de cellules satellites immortalisées | — | 🟧 |
| RQ-C2 prolifération, densité | Pasitka 2023/2024 (résumés), DF-1 | en | 130 × 10⁶ cellules/mL au laboratoire | CT-03 | données industrielles | Pasitka 2024 texte intégral | 🟨 ⛔ (paywall) |
| RQ-C3 différenciation | SV40, MyoD, inhibiteur ERK | en, zh | indice de fusion ≤ 30 % (transgène) | — | milieu de différenciation sans sérum | — | 🟧 |
| RQ-C4 milieux | Believer, Vow, brevet WO2021148955 | en | sans sérum déclaré ; facteurs recombinants chez Vow | CT-05, CT-06 | composition complète publiée | *safety narratives* FDA | 🟨 |
| RQ-C5 bioréacteurs | Humbird, Pasitka | en | — | CT-04 | O₂, contamination, recyclage chez le poulet | — | 🟨 |
| RQ-C6 supports | — | en | — | — | Ben-Arye 2020 non retrouvé | — | ⬜/🟨 |
| RQ-C7 composition, sécurité | FSANZ (caille), mémos FDA | en | 9 g de protéines/100 g (caille) | CT-01 | composition du poulet cultivé | *safety narratives* FDA | 🟨 |
| RQ-C8 coûts, obstacles | TEA, fermetures | en | obstacles hiérarchisés | CT-04, CT-08 | — | — | 🟧 |
| RQ-A1 analogues végétaux | HME, micro-impression, analogues suédois | en, zh, ko, ja | indice LMA 0,20 vs viande | CT-14 | énergie de la HME | — | 🟧 |
| RQ-A2 fongiques/microbiennes | Quorn, Solein, FeedKind | en, zh | mycoprotéine industrielle ; SCP à 68–73 % de protéines | CT-11 | TEA publique | — | 🟨 |
| RQ-A3 fermentation de précision | — | en | — | — | peu couvert | — | 🟨 |
| RQ-A4 insectes, algues, lentilles d'eau | — | en | — | CT-12 | essai Wolffia (Kaplan) | — | 🟨 |
| RQ-A5 traditions | yuba, su ji, tempeh | zh, ja, id | savoir-faire de laminage | — | analogues modernes laminés | CNKI, J-STAGE (PDF image) | 🟨 |
| RQ-A6 hybrides | GOOD Meat 3 (3 %), SuperMeat, SCiFi | en | produits très dilués | — | dose-réponse sensorielle | INN-07 | 🟨 |
| RQ-A7 écart nutritionnel et sensoriel | DIAAS soja/pois/porc, fer, arôme | en | qualité protéique limitée par le profil en AA | CT-13 | DIAAS du poulet, de la mycoprotéine, des SCP ; olfactométrie | Hodgkinson 2025 | 🟨 |
| RQ-E1 coûts du poulet | van Horne 2017/2018, ITAVI 2022, Embrapa | en, fr, pt | coûts par pays et par système | CT-10 | après 2017 (international) | AVEC 2026, USDA ERS | 🟧 |
| RQ-E2 TEA | 6 TEA + revue de cadrage + modèle E | en, es | divergence de 5 ordres de grandeur | CT-02, CT-08 | Garrison, Negulescu en texte intégral | — | 🟧 |
| RQ-E3 substituts | prix du soja et du pois, e-SCP | en | prix d'ingrédients seulement | — | TEA HME et mycoprotéine | — | 🟨 |
| RQ-E4 ACV | Sinke, Risner, Mostert | en | voir RQ-X2 | CT-09 | — | — | 🟨 |
| RQ-E5 installations | Believer, UPSIDE, GOOD Meat | en | échelle réelle ~10³ L | — | statut de Glenview, ABEC | — | 🟧 |
| RQ-E6 réglementation | voir RQ-X4 | — | — | — | — | — | 🟧 |
| RQ-P1 brevets | 44 brevets (échantillon) | en, zh, ja, ko | dépôts concentrés sur les milieux et facteurs de croissance | CT-24 | revendications non lues pour 38/44 ; comptage de familles | EPO OPS (clé requise) | 🟨 ⛔ |
| RQ-P2 acteurs | 49 acteurs | en, zh, ja, ko, nl, sv | `agents/P/actors.csv` | — | statuts 2026 de SuperMeat, Aleph, Mosa, Vital Meat | — | 🟨 |
| RQ-P3 échecs | 7 échecs confirmés | en | causes partielles | — | causes techniques détaillées | — | 🟧 |
| RQ-P4 problèmes non résolus | inventaire U1–U9 | — | — | — | — | — | 🟧 |
| RQ-P5 pistes | 10 pistes | — | intégrées dans INN-01 à INN-21 | — | — | — | 🟧 |

Aucune question n'atteint encore les critères de fin (🟩). Les principaux manques transversaux sont : les textes intégraux sous paywall (Pasitka, Havenstein), les sources non anglophones primaires (85 % des sources sont en anglais), les textes réglementaires restants et les données industrielles de la voie B, qui ne sont pas publiques.

## 3. Biais de couverture connus (dès la phase 1)

- Bases bloquées : OpenAlex, Semantic Scholar, Google Scholar, Espacenet, PATENTSCOPE, CAB Abstracts, CNKI, SciELO, Gallica → la littérature chinoise, latino-américaine et la littérature agronomique grise sont sous-représentées.
- Paywalls : beaucoup d'articles de zootechnie (Poultry Science est en accès libre depuis 2020, mais pas British Poultry Science, Animal Feed Science and Technology…) ne sont lisibles qu'en résumé.
- WebSearch est indexé depuis les États-Unis : biais anglophone et commercial.
