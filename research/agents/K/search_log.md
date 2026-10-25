# Journal de recherche — agent K (phase 4, mission X2 : comparaison homogène des trois voies)

Session du 2026-10-25. Bases : Europe PMC (`search.py epmc`, `epmc-full`), Crossref, HAL (API), J-STAGE, WebSearch (standard et étendu), WebFetch, API ouvertes (ADEME data-fair, Recherche Data Gouv, USDA FoodData Central, BCE, Helda, CGSpace, ALICE/Embrapa), téléchargements directs (FAO, waterfootprint.org, CE Delft/GFI Europe, edepot WUR, MEXT, CFN/TACO, ifeu).
Langues : en, fr, pt, es, zh, ja, de. Justification des langues ajoutées : **pt** (Brésil = premier exportateur de poulet, Embrapa, TACO), **ja** (table officielle japonaise distinguant protéine N×facteur et protéine en acides aminés), **de** (ACV de référence de l'ifeu pour les pouvoirs publics allemands). Les recherches **zh** et **es** n'ont donné aucune source primaire exploitable (voir lignes « sans résultat »).

| date | base | langue | requête exacte | résultats | retenus | remarque |
|---|---|---|---|---|---|---|
| 2026-10-25 | Europe PMC | en | broiler life cycle assessment organic free range standard energy land | 171 | 1 (Alves 2026, SRC-K-0013) | Résultats surtout génériques |
| 2026-10-25 | Europe PMC | en | Leinonen Predicting the environmental impacts of chicken systems in the United Kingdom broiler | 5 | 0 | Leinonen 2012 identifié (SRC-E-0010) mais PDF bloqué (OUP, ScienceDirect 403) malgré licence CC BY-NC-ND |
| 2026-10-25 | Europe PMC | en | Prudencio da Silva environmental impacts French Brazilian broiler chicken production scenarios | 2 | 0 | Article identifié ; pas de texte libre |
| 2026-10-25 | HAL | en | Environmental impacts of French and Brazilian broiler chicken production scenarios | 1 | 0 | Notice HAL sans fichier (lien ISTEX fermé) |
| 2026-10-25 | HAL | fr | analyse du cycle de vie poulet label rouge standard biologique | 0 | 0 | Sans résultat |
| 2026-10-25 | curl FAO | en | i3460e.pdf (Greenhouse gas emissions from pig and chicken supply chains) | 1 | 1 (SRC-K-0001) | Texte intégral lu |
| 2026-10-25 | WebSearch | en | FAO "Pathways towards lower emissions" 2023 chicken meat emission intensity kg CO2eq per kg protein GLEAM 3 | 9 | 1 (SRC-K-0022) | Valeurs du poulet uniquement graphiques |
| 2026-10-25 | WebSearch | en | Mekonnen Hoekstra 2012 "A Global Assessment of the Water Footprint of Farm Animal Products" pdf chicken meat 4325 | 9 | 1 (SRC-K-0002, rapport 48) | Article Ecosystems non téléchargeable ; rapport UNESCO-IHE lu |
| 2026-10-25 | lecture fichiers agent E | en | Sinke 2023 (téléchargement de l'agent E) — énergie, sols, eau | 1 | 0 | Valeurs seulement en figures → recherche du rapport CE Delft 2021 |
| 2026-10-25 | WebSearch | en | CE Delft "LCA of cultivated meat" "Future projections for different scenarios" 2021 pdf land use water cumulative energy demand chicken | 9 | 1 (SRC-K-0003) | Rapport lu (copie GFI Europe) |
| 2026-10-25 | API ADEME data-fair | fr | datasets?q=agribalyse | 6 | 2 jeux | AGRIBALYSE 4 = données v3.2 |
| 2026-10-25 | API ADEME | fr | lines?q=poulet / Nuggets / végétal | 46 / 7 / 55 | 6 produits (SRC-K-0005) | Base par kg de produit |
| 2026-10-25 | Recherche Data Gouv | fr | dataset doi:10.57745/XTENSJ (fichiers AGRIBALYSE 3.2) | 14 fichiers | 3 (tableurs conv./bio, note soja) | Méthodologie EN (6 Mo) : connexion coupée (2 essais) |
| 2026-10-25 | data.gouv API | fr | datasets?q=ciqual | 1 | 0 | Site CIQUAL en maintenance (XLS et XML renvoient une page HTML) |
| 2026-10-25 | API USDA FDC | en | Chicken, broilers or fryers, meat only, raw (SR Legacy) | 12 | 1 (SRC-K-0006) | Entrées crues relevées |
| 2026-10-25 | API USDA FDC | en | chicken breast raw (Foundation) | 6 | idem | Filet 22,5 g |
| 2026-10-25 | WebSearch | pt | Tabela Brasileira de Composição de Alimentos TACO 4ª edição pdf frango peito sem pele cru proteína | 10 | 1 (SRC-K-0007) | PDF sur cfn.org.br |
| 2026-10-25 | WebSearch | ja | 日本食品標準成分表 八訂 増補2023年 エクセル 本表 mext.go.jp content xlsx | 9 | 1 (SRC-K-0008) | Excel trouvé sur la page MEXT |
| 2026-10-25 | WebSearch | zh | 白羽肉鸡 生命周期评价 碳足迹 kg CO2-eq 每千克 鸡肉 研究 | 10 | 0 | Aucune ACV chinoise ; renvoie vers Turquie, Corée, Thaïlande, Australie |
| 2026-10-25 | Crossref | zh | 肉鸡 碳足迹 生命周期 | 10 | 0 | Sans résultat pertinent |
| 2026-10-25 | WebSearch | zh | 全国农产品成本收益资料汇编 肉鸡 每50公斤主产品 总成本 2023 规模养殖 | 9 | 0 | Compilation officielle non accessible en ligne |
| 2026-10-25 | WebSearch | zh | 中国食物成分表 标准版 第6版 鸡胸脯肉 蛋白质 每100克 可食部 查询平台 chinanutri | 10 | 0 | Aucune page officielle ; sites tiers écartés |
| 2026-10-25 | WebSearch | en | van Horne "Competitiveness of the EU poultry meat sector" base year 2021 OR 2022 OR 2023 Wageningen Economic Research production costs | 9 | 0 | Pas d'édition postérieure à 2017 |
| 2026-10-25 | WebSearch (étendu) | en | AVEC Wageningen 2025 OR 2026 study production costs broiler EU Brazil Ukraine Thailand "base year" new edition | 9 | 1 (SRC-K-0009) | Étude AVEC 2026 **non trouvée** ; mémo WUR 2022 (données 2021) |
| 2026-10-25 | WebSearch | fr | ITAVI "coûts de production" volailles de chair résultats 2023 OR 2024 poulet standard label rouge biologique €/kg vif | 9 | 0 | Seulement résultats 2022 (déjà SRC-E-0012) et notes FranceAgriMer |
| 2026-10-25 | HAL | fr | rendement filet poulet label rouge croissance lente carcasse | 0 | 0 | Sans résultat |
| 2026-10-25 | HAL | fr | poulet label rouge rendement | 1 | 0 | Sauveur 1997 : PDF bloqué (HAL « Access denied », productions-animales.org 503 / connexion coupée) |
| 2026-10-25 | Europe PMC | en | slow-growing broiler carcass yield breast yield fast-growing comparison organic Label Rouge | 14 | 2 (SRC-K-0011, SRC-K-0012) | Textes intégraux lus |
| 2026-10-25 | WebSearch | en | Mostert 2022 Wageningen Livestock Research Report 1397 "Environmental impact of broiler production systems in the Netherlands" edepot pdf | 9 | 1 (SRC-K-0010) | Composition, GES, sols |
| 2026-10-25 | Europe PMC | en | (texte intégral) PMC13352374 Alves 2026 | 1 | 1 | Budgets d'entreprise États-Unis 2023 |
| 2026-10-25 | Crossref | en | Upcraft protein from renewable resources mycoprotein production from agricultural residues | 3 | 0 | Article RSC (CC BY) mais pubs.rsc.org 403 ; chiffres seulement via résumé de moteur (non retenus) |
| 2026-10-25 | WebSearch | en | Upcraft Tu Johnson Finnigan Hallett 2021 mycoprotein agricultural residues spiral.imperial.ac.uk OR europepmc cost per kg protein | 10 | 1 (Risner 2023, SRC-K-0014) | Découverte de la TEA de Risner 2023 |
| 2026-10-25 | Crossref | en | Järviö attributional life cycle assessment of microbial protein production hydrogen-oxidizing bacteria | 3 | 1 (SRC-K-0015) | PDF via Helda |
| 2026-10-25 | Crossref | en | Sillman life cycle environmental sustainability analysis microbial protein production power-to-food | 3 | 0 | Identifiée (Int J LCA 2020) ; non lue faute de temps |
| 2026-10-25 | WebSearch | en | Järviö 2021 "attributional life cycle assessment of microbial protein production" helda.helsinki.fi pdf | 9 | 0 | Puis API Helda : 3 documents (Järviö 2021, thèse 2022, Mazac 2022) |
| 2026-10-25 | Europe PMC | en | mycoprotein life cycle assessment Fusarium venenatum greenhouse gas per kg protein | 27 | 0 | Revues seulement (sources primaires suivies par l'agent S) |
| 2026-10-25 | ORA (Oxford) | en | Poore & Nemecek 2018, manuscrit accepté | 1 | (SRC-E-0030 réutilisée) | Fig. 1 lue ; mise à jour de l'accès demandée au coordinateur |
| 2026-10-25 | WebSearch | de | ifeu 2020 "Ökologische Fußabdrücke von Lebensmitteln und Gerichten in Deutschland" pdf Hähnchenfleisch Tofu kg CO2-Äquivalente | 9 | 1 (SRC-K-0016) | PDF ifeu (copie UBA bloquée) |
| 2026-10-25 | WebSearch | es | MAPA "estudio de costes" pollo de engorde España 2021 OR 2022 OR 2023 euros por kg peso vivo explotación avícola | 9 | 0 | Article aviNews (403) ; pas d'étude officielle récente |
| 2026-10-25 | Crossref | es | huella de carbono producción pollo de engorde análisis de ciclo de vida | 10 | 0 | « Huella hídrica del pollo de engorde… Lima » (2018) identifiée ; PDF inaccessible |
| 2026-10-25 | Crossref | pt | pegada de carbono frango de corte avaliação do ciclo de vida Brasil | 10 | 0 | Sans ACV primaire |
| 2026-10-25 | WebSearch | pt | Embrapa Suínos e Aves pegada de carbono frango de corte kg CO2 eq por kg de frango vivo estudo publicado | 9 | 1 (SRC-K-0017) | Chapitre Talamini 2021 (IC, maïs, soja) |
| 2026-10-25 | WebFetch | pt | embrapa.br/suinos-e-aves/cias/custos/icpfrango | 1 | 0 | Série ICPFrango chargée dynamiquement (non lisible) |
| 2026-10-25 | WebSearch | en | GFI 2024 U.S. retail market plant-based meat average price per pound compared to conventional meat SPINS chicken | 9 | 1 (SRC-K-0018) | Prix relatifs seulement |
| 2026-10-25 | API BCE | — | EXR.A.USD.EUR.SP00.A 2017-2025 | 9 | 3 (Q-K-0107 à 0109) | Taux 2021, 2023, 2025 |
| 2026-10-25 | Europe PMC | en | cultured meat life cycle assessment higher global warming than chicken (**contraire**) | 152 | 0 | Revues seulement ; résultat contraire déjà couvert par Risner 2025 (SRC-E-0003) |
| 2026-10-25 | Europe PMC | en | organic broiler life cycle assessment emissions per kg higher than conventional (**contraire**) | 159 | 0 | Aucune ACV bio primaire nouvelle ; AGRIBALYSE bio utilisée |
| 2026-10-25 | Europe PMC | en | high moisture extrusion meat analogue specific mechanical energy kWh per kg (**lacune KG-C02**) | 2 | 0 | Sans résultat |
| 2026-10-25 | J-STAGE | ja | 培養肉 コスト | 82 | 0 | Articles de vulgarisation, pas de TEA |
| 2026-10-25 | HAL | fr | coût de production poulet biologique | 2 | 0 | Communication INRAE 2017 sur l'autonomie protéique (hors périmètre coût) |
| 2026-10-25 | Crossref | es | carne cultivada costo de producción | 5 | 0 | Sans TEA hispanophone |
| 2026-10-25 | Crossref | zh | 肉鸡 生产成本 收益 分析 | 5 | 0 | Sans résultat pertinent |
| 2026-10-25 | Crossref | zh | 细胞培养肉 生命周期评价 碳排放 | 6 | 0 | Sans résultat pertinent |
| 2026-10-25 | Crossref | es | emisiones gases efecto invernadero pollo de engorda ciclo de vida México | 6 | 0 | Sans résultat pertinent |
| 2026-10-25 | Crossref | pt | custo de produção frango de corte série histórica Embrapa ICPFrango | 6 | 0 | Mémoires seulement |
| 2026-10-25 | lecture tables agent S | — | agents/S/quant.csv (DIAAS, FeedKind, Quorn, RIVM) | 97 lignes | 13 utilisées dans le modèle | Valeurs non encore fusionnées par le coordinateur |

Bilan : 56 requêtes journalisées, 7 langues (en, fr, pt, ja, de, zh, es) ; 2 recherches explicitement orientées vers des résultats contraires et 1 vers une lacune connue (lignes marquées), plus 11 recherches restées sans résultat exploitable (zh, es, fr, pt), qui documentent la couverture.
