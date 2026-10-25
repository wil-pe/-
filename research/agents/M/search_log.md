# Journal de recherche — Agent M (phase 4 : économie de la nutrition avicole, littérature non anglophone, voie A)

Période : 2026-10-25. Prolonge l'agent N. Outils : `search.py` (epmc, epmc-full, pubmed, crossref), Consensus (MCP), WebSearch, WebFetch, curl + pypdf/pdftotext/openpyxl.
Colonnes : date | base | langue | requête exacte | résultats | retenus | remarque.
« retenus » = références jugées pertinentes, lues et/ou enregistrées (ID SRC-M dans la remarque).

| date | base | langue | requête exacte | résultats | retenus | remarque |
|---|---|---|---|---|---|---|
| 2026-10-25 | curl (URL stable Banque mondiale) | en | CMO-Historical-Data-Monthly.xlsx | 1 fichier | 1 | Version datée du 3 janv. 2025 (données jusqu'à déc. 2024) → SRC-M-0005 |
| 2026-10-25 | WebSearch | en | World Bank Pink Sheet CMO-Historical-Data-Monthly.xlsx 2026 | 10 | 0 | Aucune version 2025-2026 trouvée par URL stable (limite documentée) |
| 2026-10-25 | WebSearch | zh | 赖氨酸 价格 2025 年均价 元/吨 苏氨酸 蛋氨酸 饲料添加剂 | 9 | 0 | Rapports de cabinets payants (IMARC, 智研) : non retenus ; pistes Boyar/卓创 |
| 2026-10-25 | WebSearch | zh | 梅花生物 2024年年度报告 赖氨酸 苏氨酸 销量 营业收入 平均售价 | 9 | 0 | PDF du rapport Meihua repéré (qq.com), non lu faute de temps ; Fufeng préféré (ASP explicites) |
| 2026-10-25 | WebSearch | en | Fufeng Group annual report 2024 amino acids average selling price threonine lysine sales volume | 9 | 1 | Rapport annuel 2025 (HKEX) → SRC-M-0001 |
| 2026-10-25 | WebFetch | en | fufeng-group.com/en/investor/announcements.php | 0 | 0 | HTTP 503 |
| 2026-10-25 | WebSearch | en | hkexnews Fufeng Group annual report 2021 OR 2019 OR 2017 "average selling price of threonine" "98% lysine" | 9 | 3 | Rapports 2019, 2022, 2023 → SRC-M-0002 à 0004 ; résultats 2014 téléchargés (ASP en % seulement, non retenu) |
| 2026-10-25 | WebSearch | zh | 安迪苏 2025年年度报告 蛋氨酸 市场价格 元/公斤 均价 | 9 | 0 | Pas de prix annuel de la méthionine dans les extraits ; seulement 21-23 RMB/kg S1 2024 via un article de presse (non vérifié, non retenu) |
| 2026-10-25 | WebSearch | zh | 2024年全国饲料工业发展概况 农业农村部 饲料添加剂 氨基酸 产量 豆粕用量占比 | 9 | 0 | Sites de rapports commerciaux (观研) : non retenus |
| 2026-10-25 | WebSearch (moa.gov.cn, chinafeed.org.cn) | zh | 全国饲料工业发展概况 2024年 饲料添加剂总产量 氨基酸 | 10 | 2 | Pages officielles 2024 et 2025 → SRC-M-0006, 0007 |
| 2026-10-25 | crossref | pt | redução proteína bruta frangos de corte aminoácidos industriais viabilidade econômica | 12 | 0 | Articles RBZ/Ciência Rural (SciELO 403) ; dissertations USP repérées |
| 2026-10-25 | curl | pt | scielo.br, rbz.org.br, seer.sct.embrapa.br, alice.cnptia.embrapa.br | — | — | SciELO 403 (article et DOI) ; rbz.org.br 200 ; Alice Embrapa 200 ; PAB 302 |
| 2026-10-25 | crossref | zh | 低蛋白日粮 肉鸡 生长性能 | 20 | 0 | Crossref indexe mal les revues chinoises d'alimentation animale |
| 2026-10-25 | crossref | zh | 低蛋白低豆粕 肉鸡 氨基酸 饲料成本 | 10 | 0 | idem |
| 2026-10-25 | WebSearch | zh | 动物营养学报 低蛋白日粮 白羽肉鸡 生长性能 胸肌率 氮排放 补充甘氨酸 | 9 | 0 | Yang 2016 (动物营养学报, Gly) repéré : résumé sur opaj.napstic.cn, texte intégral sur Wanfang (payant) |
| 2026-10-25 | WebFetch | zh | opaj.napstic.cn/periodicalArticle/0120160600061902 | 1 | 0 | Métadonnées Yang 2016 ; pas de PDF |
| 2026-10-25 | curl | zh | chinajan.com (动物营养学报), xmsyxb.com (畜牧兽医学报), zgxmzz.com (中国畜牧杂志) | — | — | chinajan : connexion réinitialisée ; xmsyxb : 200 (PDF libres) ; zgxmzz : 403 |
| 2026-10-25 | WebSearch (xmsyxb, chinaagrisci, casb, sciengine) | zh | 肉鸡 低蛋白 饲粮 氨基酸 生长性能 屠宰性能 | 9 | 1 | → SRC-M-0008 ; WOD188 Arg (2025.11.021) repéré |
| 2026-10-25 | WebSearch (xmsyxb, chinaagrisci, casb, sciengine, feedindustry) | zh | 黑水虻幼虫粉 肉鸡 生长性能 替代豆粕 添加水平 | 10 | 0 | **Aucun essai chinois BSF × poulet de chair en accès libre trouvé** ; revue d'entomologie (2019) sans données poulet |
| 2026-10-25 | epmc | en | ("black soldier fly" OR "Hermetia illucens" OR "insect meal") AND broiler* AND ("meta-analysis" OR "meta-regression" OR "dose-response") | 25 | 2 | Okon 2026 désormais en PMC (SRC-A-0021 → texte intégral) ; Njeri 2026 (N excrété) |
| 2026-10-25 | pubmed | en | (insect meal OR black soldier fly OR Hermetia OR Tenebrio OR mealworm) AND broiler* AND (meta-analysis OR meta-regression) [TiAb] | 3 | 1 | Malematja 2024 |
| 2026-10-25 | epmc | en | TITLE:(meta-analysis OR meta-regression) AND (insect OR … ) AND (poultry OR broiler OR chicken) | 25 | 0 | surtout pondeuses, aquaculture, ruminants |
| 2026-10-25 | Consensus | en | meta-analysis insect meal inclusion level broiler growth performance feed conversion defatted full-fat Hermetia Tenebrio | 3 | 1 | Malematja 2024 ; Tóth 2026 (essai 2-4 %) |
| 2026-10-25 | epmc-full | en | PMC13382029 (Okon 2026) | 1 | 1 | Texte intégral : « 28 % » = inclusion moyenne (intercept centré) → SRC-A-0021 mis à jour |
| 2026-10-25 | crossref | en | Martínez Marín black soldier fly meta-analysis broiler metabolizable energy / Hayat 2024 … / Chhetri 2025 … | 15 | 1 | Martínez Marín 2023, Hayat 2024 (Anim Prod Sci, corrigendum), Chhetri 2025 (Kafkas) repérés |
| 2026-10-25 | WebFetch / curl | en | tandfonline.com/doi/full/10.1080/1828051X.2023.2194909 | 0 | 0 | 403 |
| 2026-10-25 | WebSearch | en | "Meta-analysis of the effect of black soldier fly larvae meal in diet on broiler performance…" pdf | 10 | 1 | PDF IRIS Turin → SRC-M-0009 |
| 2026-10-25 | pubmed / epmc-full | en | Moula N[Author] AND Detilleux J[Author] AND meta-analysis[Title] ; PMC6562956 | 1 | 1 | → SRC-M-0010 |
| 2026-10-25 | epmc | en | TITLE:("L-lysine" AND (safety OR efficacy)) AND JOURNAL:"EFSA J" AND endotoxin | 5 | 1 | → SRC-M-0011 (Metex 2022) |
| 2026-10-25 | epmc | en | TITLE:("L-valine" OR "L-isoleucine" OR glycine OR "DL-methionine" OR "L-threonine") AND JOURNAL:"EFSA J" AND endotoxin AND poultry | 3 | 1 | → SRC-M-0012 (thréonine 2017) ; isoleucine 2020 repérée |
| 2026-10-25 | epmc | en | ("feed grade" OR "food grade") AND ("amino acid*") AND ("cultured meat" OR "cultivated meat") AND (medium OR media) | 15 | 1 | Leber 2026 = SRC-A-0032 (déjà enregistré) |
| 2026-10-25 | WebSearch | en | L-Lysine monohydrochloride cell culture grade specification endotoxin EU/mg heavy metals ppm certificate | 10 | 1 | Thermo (pas de limite affichée), Wako CultureSure (< 10 UE/g) |
| 2026-10-25 | WebFetch | ja | labchem-wako.fujifilm.com/jp/product/detail/W01W0103-2379.html | 1 | 1 | → SRC-M-0013 ; prix sur devis |
| 2026-10-25 | epmc-full | en | PMC8362201 (Humbird 2021) — section Amino acids | 1 | 1 | SRC-E-0001 réutilisé (EV-M-0015) |
| 2026-10-25 | API USDA FDC (DEMO_KEY) | en | foods/search chicken breast raw | 0 | 0 | 429 (quota partagé) → fichiers SR Legacy de l'agent A relus |
| 2026-10-25 | curl | fr | ciqual.anses.fr Table Ciqual 2020 XLS ; data.gouv.fr API | 0 | 0 | 503 ; data.gouv : connexion réinitialisée → **CIQUAL toujours inaccessible** (KG-COV-10) |
| 2026-10-25 | curl | pt | TACO 4ª edição (cfn.org.br) | 1 | 1 | Déjà enregistré par K (SRC-K-0007) |
| 2026-10-25 | WebFetch | en | nap.nationalacademies.org/read/2114/chapter/5 (NRC 1994) | 0 | 0 | 301 → 404 |
| 2026-10-25 | WebSearch | en | Nutrient Requirements of Poultry Ninth Revised Edition 1994 read online "Table 2-6" broilers | 9 | 0 | Piste : 10e édition NASEM |
| 2026-10-25 | WebSearch / WebFetch | en | National Academies "Nutrient Requirements of Poultry" tenth revised edition ; read/25395 | 9 | 1 | → SRC-M-0015 (2026) ; chapitre 14 non lisible |
| 2026-10-25 | WebSearch | pt | Tabelas Brasileiras para Aves e Suínos Rostagno 5ª edição 2024 … | 9 | 1 | → SRC-M-0016 (presse) ; avinews 403 |
| 2026-10-25 | WebFetch | en | feedtables.com/content/soybean-meal-46/48/50 | 0 | 0 | 404 (tables INRAE-CVB non accessibles) |
| 2026-10-25 | WebSearch | en | site:feedtables.com soybean meal 48 crude protein lysine broiler AMEn INRAE CIRAD AFZ | 9 | 1 | Feedipedia → SRC-M-0014 |
| 2026-10-25 | WebFetch | en | betterchickencommitment.com/policy/ | 1 | 1 | → SRC-M-0017 |
| 2026-10-25 | WebSearch | fr | "European Chicken Commitment" texte français critères densité 30 kg/m² souches croissance lente | 9 | 1 | Texte officiel FR non trouvé ; Réussir 2025 → SRC-M-0018 |
| 2026-10-25 | epmc | en | ("slow-growing" OR "slower-growing") AND broiler* AND (commercial farm* OR "commercial conditions" OR "commercial flocks") AND (mortality OR welfare OR "feed conversion") | 20 | 2 | → SRC-M-0019 (Danemark) ; Thaïlande 2025 repéré |
| 2026-10-25 | epmc | en | Nicol 2024 … / Forseth 2024 broiler mortality Ross 308 Hubbard JA787 Norway ; TITLE:"Mortality risk on farm and during transport" | 6 | 1 | → SRC-M-0020 ; Nicol 2024 non retrouvé |
| 2026-10-25 | WebSearch | nl | kostprijs vleeskuikens trager groeiend ras Beter Leven voederconversie Wageningen Economic Research rapport | 9 | 2 | edepot 591335, 644754 → SRC-M-0021, 0022 ; 631066 (qualité d'abattage) non retenu |
| 2026-10-25 | epmc | en | ("reduced crude protein" OR "low crude protein" OR "low-protein") AND broiler* AND ("feed cost" OR economic …) | 15 | 0 | Aucune estimation chiffrée du coût d'un point de PB → calcul agent (Q-M-0080 à 0082) |
| 2026-10-25 | teses.usp.br | pt | Caetano 2013 (DOI 10.11606/d.74.2013.tde-23092013-133127) | 1 | 1 | → SRC-M-0024 (pas de prix) |
| 2026-10-25 | WebSearch | zh | 农业农村部 畜产品和饲料集贸市场价格情况 2025年12月 豆粕 玉米 全国平均价格 元/公斤 | 10 | 1 | → SRC-M-0026 |
| 2026-10-25 | curl | pt | alice.cnptia.embrapa.br simple-search "mosca soldado negra frangos" | 0 | 0 | 403 (recherche Alice bloquée) |
| 2026-10-25 | WebSearch | pt | farinha de larvas de mosca soldado negra (Hermetia illucens) frangos de corte desempenho Embrapa OR RBZ OR Ciência Rural OR PAB | 9 | 0 | **Aucun essai brésilien BSF × poulet de chair publié trouvé** ; résumés de congrès (sang) ; thèse tilapia |
| 2026-10-25 | teses.usp.br | pt | Tavares 2020 Tenebrio molitor viabilidade econômica frangos | 1 | 1 | → SRC-M-0025 (prix des AA au Brésil) |
| 2026-10-25 | HAL API / curl | fr | halId_s:hal-01995110 (Laisse 2018) | 1 | 1 | /document = page anti-robot ; /file/…pdf = PDF → tableau 6 contre-vérifié (SRC-N-0012) |
| 2026-10-25 | WebFetch | zh | xmsyxb.com 2025.11.021 (WOD 188, Arg) | 1 | 1 | → SRC-M-0027 (résumé) |
| 2026-10-25 | WebSearch | zh | 白羽肉鸡 自主培育品种 广明2号 圣泽901 沃德188 料重比 42日龄 体重 国家家禽生产性能测定站 测定结果 | 9 | 1 | Aucun rapport officiel de test de performance ; 人民日报 2026 → SRC-M-0028 |
| 2026-10-25 | WebSearch | zh | 安迪苏 2025年年度报告 蛋氨酸 销量 营业收入 功能性产品 sse.com.cn pdf | 9 | 0 | Aucun prix ni volume de méthionine publié trouvé (lacune méthionine/valine/isoleucine/glycine) |
| 2026-10-25 | WebSearch | zh | 团体标准 肉鸡 低蛋白低豆粕多元化日粮 生产技术规范 粗蛋白质 T/CFIAS 中国饲料工业协会 | 9 | 0 | Norme CFIAS seulement pour le canard (T/CFIAS 8006-2024) ; projet de norme de Pékin (DB11) : téléchargement réinitialisé |
| 2026-10-25 | curl | zh | beijing.gov.cn / nyncj.beijing.gov.cn (projet DB11 家禽低豆粕饲料) ; ttbz.org.cn | 0 | 0 | Connexions réinitialisées ; ttbz 404 |
| 2026-10-25 | WebFetch | pt | embrapa.br/suinos-e-aves/cias/custos/icpfrango | 0 | 0 | Graphiques dynamiques non lisibles (même constat que N) |
| 2026-10-25 | WebSearch (extended) | zh | "黑水虻" 幼虫粉 对 肉鸡 生长性能 屠宰性能 的影响 中国畜牧杂志 OR 饲料工业 OR 动物营养学报 OR 中国家禽 | 9 | 1 | Revue 环境昆虫学报 2025 → SRC-M-0029 ; thèse NJAU (4 % BSF en basse PB) : page vide |
| 2026-10-25 | curl | en | doi 10.1093/ps/82.10.1500 → sciencedirect / poultryscience.org (Havenstein 2003) | 0 | 0 | 403 / page sans texte : KG-COV-08 toujours ouvert |
| 2026-10-25 | Recherche de résultats contraires | en | (synthèse) mortalité des souches lentes en conditions commerciales | — | 2 | Norvège (Forseth 2024 : ×2) vs Danemark (Al-Saeedi 2026 : NS) : contradiction documentée |
| 2026-10-25 | Recherche de résultats contraires | en | (synthèse) qualité alimentation animale « impropre » aux milieux | — | 2 | Lysine EFSA ≈ spécification culture cellulaire ; thréonine ×30 000 : résultat mitigé |
| 2026-10-25 | WebSearch | es | harina de larvas de mosca soldado negra pollos de engorde nivel de inclusión rendimiento conversión alimenticia costo tesis | 9 | 1 | Thèses équatoriennes (UTC 30-40 % de remplacement ; ESPOL 10-30 %, bénéfice net maximal à 0 % selon l'extrait) ; article colombien (Musca domestica) → SRC-M-0030 |
| 2026-10-25 | WebSearch | es | dietas bajas en proteína pollos de engorde aminoácidos sintéticos valina isoleucina glicina costo de la dieta FEDNA | 9 | 0 | Engormix, USSEC, Evonik (contenus commerciaux, non retenus) ; essai UNAM (PB −2 %, Trop Subtrop Agroecosyst) repéré, non lu |
| 2026-10-25 | curl | es | dspace.espol.edu.ec T-113320 Mindiola Mendoza.pdf | 0 | 0 | Connexion réinitialisée (comme pour l'agent N) |
| 2026-10-25 | WebFetch | es | repositorio.utc.edu.ec (Del Hierro Escobar 2022) | 1 | 0 | Notice seule : 96 oiseaux, 30/40 % de remplacement du soja, NS ; non enregistré (mémoire de licence, résumé incohérent) |
| 2026-10-25 | WebFetch | es | revistasojs.ucaldas.edu.co … download/8663/7049 | 1 | 1 | PDF lu → SRC-M-0030 (Musca domestica, Colombie) |

Bilan : 70 requêtes journalisées ; langues : en 32, zh 19, pt 9, es 5, fr 3, nl 1, ja 1. Recherches explicites de résultats contraires ou négatifs : mortalité des souches lentes, qualité « impropre » des AA de qualité alimentation animale, effets négatifs des insectes (Moula 2019, revue chinoise, Costa Rica), pénalité de la basse PB (Caetano 2013), économie négative des insectes (Tavares 2020).
