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
