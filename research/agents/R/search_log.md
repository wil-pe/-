# Journal de recherche — Agent R (réglementation, phase 4) — 2026-10-25

Périmètre : textes officiels datés par juridiction (UE, France, Italie, Hongrie et autres projets d'interdiction, Royaume-Uni, Suisse, Israël, Singapour, Corée, Japon, Chine, Australie/NZ, États-Unis fédéral et États, Brésil). Prolonge l'agent E (KG-COV-07, KG-COV-12, CT-19).

Langues utilisées et justification : en (textes UE, FDA, FSA, FSANZ, États américains), fr (France, Suisse romande), it (Italie), de (canton de Zurich), hu (Hongrie, loi et presse), ko (MFDS), ja (CAA), zh (NHC, MARA), pt (ANVISA, CTNBio), he (ministère israélien de la Santé, presse). L'espagnol n'a pas été utilisé : aucune juridiction hispanophone n'est dans le périmètre de la mission R.

Contournements : EUR-Lex (HTTP 202 vide) remplacé par CELLAR (`publications.europa.eu/resource/celex/<CELEX>.ENG`, et requête SPARQL pour les actes 2026 non encore indexés par CELEX) ; Fedlex via son point SPARQL ; OpenEFSA via l'API JSON publique du portail ; TRIS via les PDF de messages ; Federal Register (texte intégral bloqué par captcha) via govinfo.gov.

| date | base | langue | requête exacte | résultats | retenus | remarque |
|---|---|---|---|---|---|---|
| 2026-10-25 | WebSearch | en | EFSA Journal 2024 guidance scientific requirements application authorisation novel food cell culture-derived food | 9 | 0 | pistes secondaires (ACNFP, presse) ; guide primaire retrouvé via Crossref |
| 2026-10-25 | Crossref | en | Guidance on the scientific requirements for an application for authorisation of a novel food in the context of Regulation (EU) 2015/2283 | 10 | 1 | DOI 10.2903/j.efsa.2024.8961 vérifié |
| 2026-10-25 | Europe PMC | en | DOI:"10.2903/j.efsa.2024.8961" + epmc-full PMC11440143 | 1 | 1 | texte intégral du guide EFSA 2024 (SRC-R-0001) |
| 2026-10-25 | WebSearch | en | open.efsa.europa.eu novel food application cultivated "cell culture" Gourmey foie gras EFSA-Q-2024 | 9 | 0 | communiqués Gourmey ; numéro EFSA-Q non trouvé par le moteur |
| 2026-10-25 | OpenEFSA API | en | searchAdvanced search= cell culture / cultivated / cultured / biomass / Gallus / chicken / pork / Bos taurus / Anas / fibroblast / myoblast | 105+ | 3 | Supreme SAS (canard), Mosa Meat (graisse bovine), Solar Foods (Xanthobacter) ; **aucune demande de poulet cultivé** |
| 2026-10-25 | OpenEFSA API | en | searchAdvanced search= Aleph / Meatable / Vital Meat / Gourmey / PARIMA / Cultivated B / Mewery / BlueNalu / Supreme / Mosa | 0-1 | 2 | résultat négatif pour Aleph, Meatable, Gourmey (marque) : le canard est enregistré sous « Supreme SAS » |
| 2026-10-25 | OpenEFSA API | en | searchAdvanced search= Methylococcus / Fusarium venenatum / bacterial biomass / Xanthobacter / insect / Hermetia / Tenebrio | 1-39 | 1 | BioProtein (Norferm, aliment animal, 2004) ; dossiers Hermetia en alimentation humaine non valides ou retirés |
| 2026-10-25 | CELLAR | en | celex 32022R1104.ENG (catalogue des matières premières) | 1 | 1 | contournement d'EUR-Lex |
| 2026-10-25 | CELLAR | en | celex 32021R0882.ENG (Tenebrio molitor séché) | 1 | 1 | exemple d'autorisation de produit avec protection des données |
| 2026-10-25 | WebSearch | en | new genomic techniques regulation adopted Official Journal 2026 plants Council Parliament NGT final adoption | 10 | 0 | règlement 2026/1388 identifié ; dates contradictoires dans la presse, vérifiées sur le texte |
| 2026-10-25 | WebFetch | en | food.ec.europa.eu/plants/new-genomic-techniques (+ legislation-plants) | 2 | 0 | page Commission : animaux et micro-organismes exclus |
| 2026-10-25 | WebSearch | en | EU CMO regulation meat-related terms plant-based ban "steak" "burger" agreement Council Parliament 2026 adopted cell-cultured | 9 | 0 | règlement adopté ; numéro fourni par une note d'avocats |
| 2026-10-25 | CELLAR SPARQL | en | resource_legal_id_celex IN (32026R1739, 32026R1388) | 2 | 2 | identifiants cellar ; textes intégraux EN récupérés |
| 2026-10-25 | WebSearch | fr | Conseil d'État décret n° 2024-144 dénominations protéines végétales annulation 2025 décision | 10 | 1 | décision n° 492839 (PDF officiel) |
| 2026-10-25 | WebSearch | fr | proposition de loi interdiction viande cellulaire France 2025 2026 Sénat adoptée "viande de synthèse" | 9 | 0 | **négatif** : aucune loi adoptée |
| 2026-10-25 | curl | fr | assemblee-nationale.fr/dyn/17/amendements/2765/AN/949.rtf | 1 | 0 | amendement au projet de loi n° 2765 déclaré irrecevable (cavalier, art. 98) le 15/05/2026 |
| 2026-10-25 | TRIS (WebFetch + curl) | en/it | notification 25152 = 2023/0675/IT ; message 009 | 2 | 1 | clôture anticipée : loi adoptée avant la fin du statu quo |
| 2026-10-25 | WebSearch | hu | Magyarország törvény laboratóriumban előállított hús tilalma 2025 elfogadta Országgyűlés sejttenyésztett | 9 | 0 | presse : vote du 18/11/2025 |
| 2026-10-25 | WebSearch | hu | "2025. évi" törvény "laboratóriumi hús" előállításának forgalomba hozatalának tilalmáról njt.hu OR magyarkozlony.hu | 9 | 2 | loi 2025. évi LXXXIX ; notification 2024/0394/HU |
| 2026-10-25 | NJT (njt.jog.gov.hu) | hu | jogszabaly/2025-89-00-00 et 2025-89-K0-00 | 2 | 1 | texte officiel et exposé des motifs |
| 2026-10-25 | TRIS (curl) | en | notification 26066 = 2024/0394/HU ; messages 109734, 114041 | 3 | 1 | avis circonstancié C(2024) 7100 final |
| 2026-10-25 | WebSearch | en | technical-regulation-information-system notification prohibition "cell-cultured" OR "laboratory meat" OR "cultivated meat" Romania OR Poland OR Czechia OR Slovakia 2025 draft | 10 | 0 | **négatif** : pas de notification 2025 pour RO/PL/CZ/SK ; Roumanie connue par la presse seulement |
| 2026-10-25 | WebSearch | de | OSAV BLV kultiviertes Fleisch Gesuch Bewilligung neuartige Lebensmittel Aleph Farms Schweiz 2025 2026 | 9 | 1 | aucune décision OSAV ; communiqué du canton de Zurich |
| 2026-10-25 | Fedlex SPARQL | fr | notation 817.022.2 et 817.02, consolidation FRA html | 2 | 2 | ordonnance du DFI ; ODAlOUs |
| 2026-10-25 | WebSearch | en | Meatly cultivated chicken pet food UK approval APHA Defra registration official 2024 "animal by-products" | 10 | 1 | aucune décision officielle APHA/Defra ; presse seulement |
| 2026-10-25 | legislation.gov.uk | en | title=precision breeding | 3 | 1 | SI 2025/581 (plantes) |
| 2026-10-25 | WebSearch | en | FSA ACNFP cell-cultivated product safety assessment 2026 Vow Gourmey Hoxton Farms Mosa Meat outcome authorisation Great Britain | 10 | 1 | **négatif** : aucune autorisation britannique ; guide FSA du 30/09/2026 |
| 2026-10-25 | WebSearch | he | משרד הבריאות מזון חדש אישור בשר מתורבת אלף פארמס gov.il שירות המזון הארצי | 9 | 1 | presse israélienne |
| 2026-10-25 | WebSearch (gov.il) | he | מזון חדש רשימת מזונות חדשים שאושרו משרד הבריאות תרבית תאים | 10 | 0 | page gov.il du 17/01/2024 inaccessible (403) ; archive.org bloqué |
| 2026-10-25 | WebSearch | en | Singapore Food Safety and Security Act 2025 novel food pre-market approval provisions commencement sso.agc.gov.sg | 9 | 0 | sso.agc.gov.sg en 403 |
| 2026-10-25 | curl sfa.gov.sg | en | food-information/novel-food + 2026-08-14-sfa-list-of-approved-novel-foods.pdf | 2 | 2 | **liste officielle de 18 approbations** |
| 2026-10-25 | WebSearch | ko | 식약처 세포배양식품 한시적 기준 및 규격 인정 신청 2026 행정예고 식품의 기준 및 규격 개정 세포배양 원료 | 9 | 1 | presse Food Today ; projet de Food Code |
| 2026-10-25 | WebSearch (mfds.go.kr, law.go.kr, korea.kr) | ko | mfds.go.kr 보도자료 세포배양가공식품 식품의 기준 및 규격 행정예고 2026 | 10 | 1 | avis n° 2026-311 (curl réinitialisé ; WebFetch OK) |
| 2026-10-25 | WebSearch (mfds.go.kr, law.go.kr) | ko | 식품등의 한시적 기준 및 규격 인정 기준 일부개정고시 세포배양 미생물 배양 2024 270일 식약처 보도자료 | 10 | 1 | avis n° 2024-13 ; law.go.kr chargé dynamiquement |
| 2026-10-25 | WebFetch | ko | foodtoday.or.kr no=208732 | 1 | 1 | 2 demandes, 0 reconnaissance |
| 2026-10-25 | WebSearch | ja | 細胞培養食品 消費者庁 食品衛生基準審議会 新開発食品調査部会 2025 2026 安全性確保 方針 | 9 | 1 | séances CAA déc. 2025 – mai 2026 |
| 2026-10-25 | curl caa.go.jp | ja | fscc_cms105_260528_06 / 260527_07 / 260528_08 / 260715_01 | 4 | 1 | projet de guide ; cadre non arrêté |
| 2026-10-25 | WebSearch (caa.go.jp, mhlw.go.jp) | ja | 消費者庁 ゲノム編集技術応用食品 届出 一覧 マダイ トラフグ ヒラメ 2025 | 10 | 1 | liste officielle des 13 notifications |
| 2026-10-25 | WebSearch | zh | 细胞培养肉 新食品原料 申报 受理 国家卫生健康委 2025 2026 首个 | 10 | 0 | **négatif** |
| 2026-10-25 | WebSearch (nhc.gov.cn, gov.cn) | zh | 国家卫生健康委员会 公告 新食品原料 微生物蛋白 2025 镰刀菌 OR 丝状真菌 OR 甲烷氧化菌 批准 | 10 | 1 | avis 2025 n° 7 (Fusarium venenatum) ; rien sur les méthanotrophes |
| 2026-10-25 | WebSearch (zwfw.nhc.gov.cn) | zh | zwfw.nhc.gov.cn 新食品原料受理情况公告 细胞培养 2026 | 10 | 1 | index des avis de recevabilité |
| 2026-10-25 | curl zwfw.nhc.gov.cn | zh | index xspylsp + 118 avis (déc. 2022 – oct. 2026) ; grep 细胞 / 培养肉 / 动物细胞 | 118 | 1 | **négatif documenté** : 0 cellule animale ; 3 cultures végétales |
| 2026-10-25 | WebSearch (gov.cn) | zh | 新食品原料安全性审查管理办法 国家卫生和计划生育委员会令第1号 2017年修正 全文 第二条 新食品原料是指 | 10 | 1 | texte intégral (plateforme NHC) |
| 2026-10-25 | WebSearch (moa.gov.cn) | zh | 农业农村部公告 乙醇梭菌蛋白 新饲料证书 饲料原料目录 2021 首祥 | 10 | 1 | avis n° 692 (2023) ; demandeur « 首朗 » (et non « 首祥 ») |
| 2026-10-25 | WebSearch (foodstandards.gov.au) | en | FSANZ A1341 cultured duck application approval 2026 gazettal; A1269 cultured quail gazetted Food Standards Gazette 2025 | 10 | 2 | A1269 publié le 18/06/2025 ; A1341 approuvé le 6/10/2026 |
| 2026-10-25 | curl | en | hfpappexternal.fda.gov inventaire AnimalCellCultureFoods | 1 | 0 | toujours 5 entrées |
| 2026-10-25 | WebSearch (fsis.usda.gov, usda.gov, federalregister.gov) | en | FSIS directive cell-cultured meat poultry inspection "grant of inspection" label approval | 10 | 0 | directive 7800.1 identifiée ; fsis.usda.gov et usda.gov en 403 |
| 2026-10-25 | API federalregister.gov | en | term "cultured animal cells" (agence FSIS) ; term "cell-cultured" | 8 | 2 | ANPR 2021 (pas de règle finale) ; colorant myoglobine 2025 ; textes via govinfo.gov |
| 2026-10-25 | WebSearch | en | Alabama SB23 2024 cultivated meat prohibition Act 2024 alison legislature enrolled text | 10 | 1 | texte « enrolled » officiel |
| 2026-10-25 | WebSearch | en | Mississippi House Bill 1006 2025 cell-cultured food products prohibit sale billstatus.ls.state.ms.us | 10 | 1 | site officiel : TLS invalide puis 503 ; copie officielle via PSU |
| 2026-10-25 | WebSearch | en | Montana HB 401 2025 cell-cultured edible product prohibit chaptered law signed legmt.gov | 10 | 2 | chapitre 276 ; communiqué du gouverneur |
| 2026-10-25 | WebSearch | en | Indiana House Enrolled Act 1425 2025 cultivated meat moratorium July 1 2025 June 30 2027 iga.in.gov | 10 | 0 | iga.in.gov rendu en JavaScript : texte non lu |
| 2026-10-25 | curl | en | nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB246.pdf | 1 | 1 | approuvé le 20/05/2025 |
| 2026-10-25 | WebSearch + API sdlegislature.gov | en | South Dakota 2025 OR 2026 bill cell-cultured protein lab-grown meat prohibit OR label sdlegislature.gov signed | 10 | 1 | titres des 7 projets via l'API ; textes non lus |
| 2026-10-25 | WebFetch | en | nationalaglawcenter.org/alternative-proteins-2025-legislative-update | 1 | 1 | compilation secondaire |
| 2026-10-25 | WebSearch | en | UPSIDE Foods v. Florida cultivated meat ban lawsuit ruling 2025 2026 preemption dormant commerce clause Eleventh Circuit; Wildtype UPSIDE Texas SB 261 lawsuit ruling | 10 | 1 | arrêt du 23/03/2026 ; **négatif** sur le contentieux texan |
| 2026-10-25 | WebSearch (ca11.uscourts.gov, courtlistener) | en | media.ca11.uscourts.gov opinions pub UPSIDE Foods Inc v. Commissioner Florida Department of Agriculture 2026 opinion pdf | 5 | 1 | arrêt n° 24-13640 |
| 2026-10-25 | WebSearch (fda.gov) | en | FDA intentional genomic alterations animals list of approvals low-risk determinations PRLR-SLICK gene edited chicken | 9 | 1 | aucune volaille éditée à usage alimentaire |
| 2026-10-25 | WebSearch | pt | ANVISA instrução normativa novos alimentos lista 2024 RDC 839 carne cultivada pedido avaliação 2025 2026 MAPA carne cultivada regulamentação | 9 | 1 | bibliothèque ANVISA 2026 ; article KindEco (« autorisation commerciale ») écarté faute de source officielle |
| 2026-10-25 | WebSearch (gov.br, in.gov.br) | pt | CTNBio Resolução Normativa nº 16 de 15 de janeiro de 2018 Técnicas Inovadoras de Melhoramento de Precisão consulta animais edição gênica | 10 | 1 | RN 16/2018 (MCTI) |
| 2026-10-25 | API dadosabertos.camara.leg.br | pt | proposicoes keywords=carne,cultivada / laboratório / células (2022-2026) | 0 | 0 | **négatif** (API sans résultat) : projets de loi brésiliens non vérifiés |
| 2026-10-25 | WebSearch | it | decreto attuativo legge 172/2023 elenco denominazioni carne prodotti a base di proteine vegetali MASAF 2024 2025 Gazzetta Ufficiale | 10 | 1 | décret d'application de l'art. 3 non trouvé (**négatif**) ; fiche de la Chambre des députés |
| 2026-10-25 | curl sfa.gov.sg | en | contre-vérification : la SFA publie-t-elle ses approbations ? | 1 | 1 | oui depuis le 17/03/2026 : la réserve de la vérification indépendante est caduque |

**Total : 61 requêtes, 10 langues (en, fr, it, de, hu, ko, ja, zh, pt, he).**

Recherches de résultats contraires ou négatifs explicites : demande de poulet cultivé dans OpenEFSA (aucune) ; loi française adoptée (aucune) ; notifications TRIS d'autres États membres (aucune trouvée) ; autorisation britannique d'un produit cellulaire pour l'humain (aucune) ; demande chinoise de viande cultivée (aucune sur 110) ; décision de l'OSAV (aucune) ; contentieux texan (rien trouvé) ; volaille éditée autorisée aux États-Unis ou au Japon (aucune) ; « autorisation commerciale » brésilienne (article non fiable écarté).
