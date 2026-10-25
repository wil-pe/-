# Substituts du poulet : qualité protéique, énergie, coûts, ACV et arôme (voie C — approfondissement)

*Agent S — Chicken Muscle Research Lab — phase 4, mission A2 — 2026-10-25.*
*Prolonge l'agent A (`reports/alternative_proteins.md`). Identifiants : `SRC-S-…`, `EV-S-…`, `Q-S-…` (tables `research/agents/S/`). Les identifiants d'autres agents (`EV-A-…`, `EV-E-…`, `Q-E-…`) sont cités quand ils complètent l'analyse. Tout calcul fait par l'agent est signalé « calcul de l'agent » et détaillé dans le champ `notes` de la mesure correspondante.*

---

## 1. Périmètre, méthode et limites

**Lacunes visées.** KG-C01 (DIAAS mesurés), KG-C02 (énergie et débit de l'extrusion humide et de la cellule de cisaillement), KG-C04 (arôme poulet des analogues), KG-C06 (TEA de la mycoprotéine et des SCP), et marginalement KG-C05 (zinc) ; contradiction CT-11 (ACV de la mycoprotéine). KG-C03 (fibrosité) n'a pas été traité, sauf pour l'argument énergétique d'INN-09.

**Bases et outils.** Europe PMC (texte intégral libre), PubMed, Crossref, HAL et theses.fr, J-STAGE, dépôts institutionnels (HAL INRAE, Spiral/Imperial, Universidad de Chile, theses.fr), WebSearch/WebFetch (Google Patents, KCI, sites d'agences et d'entreprises, presse spécialisée et financière), base RIVM téléchargée (xlsx). Le journal (`agents/S/search_log.md`) compte 62 requêtes en 9 langues (en, fr, zh, es, ja, de, nl, fi, ko), dont des recherches explicites d'échecs et de résultats contraires.

**Bilan.** 36 sources nouvelles (25 lues en texte intégral, 5 par sections, 6 au niveau du résumé), 47 affirmations, 97 mesures. **14 sources sur 36 (39 %) ne sont pas en anglais** : zh 4, de 3, ja 2, fr 1, es 1, nl 1, fi 1, ko 1. Aucune source déjà enregistrée en `abstract_only` n'a pu être lue en texte intégral (Hodgkinson 2025, Smetana 2015, Shahid 2024, Krintiras 2016 restent inaccessibles) : aucun `access_level` d'autres agents n'a donc été modifié.

**Limites d'accès décisives.** Upcraft et al. 2021 (TEA/ACV de la mycoprotéine, Green Chem, CC-BY) : pubs.rsc.org 403, dépôt ILRI 429, absent de Spiral. Shahid et al. 2024 (Future Foods, CC-BY) : ScienceDirect 403. Järviö et al. 2021 (ACV de Solein) : dépôt Luke 503. Sillman et al. 2020 : page anti-robot de Springer. Thèse Krintiras 2016 : 404. Prospectus HKEX de Shougang LanzaTech : non lu (deux reprises seulement).

**Conventions.** Base protéine = protéine brute (N × 6,25) sauf mention ; « base produit » = kg de produit tel que vendu (humide) ; DIAAS in vitro (ivDIAAS) et in vivo ne sont pas interchangeables. Les conflits d'intérêts sont notés dans `conditions` (ENOUGH, Tereos, Quorn/Marlow, Calysta, Solar Foods, DSM, Ajinomoto, Pulmuone).

---

## 2. Qualité protéique : premiers DIAAS chiffrés pour le poulet, la mycoprotéine et une bactérie (KG-C01)

### 2.1 Ce qui est désormais mesuré

| Aliment | Méthode | DIAAS enfant / adulte | AA limitant | Réf. |
|---|---|---|---|---|
| Repas filet de poulet + quinoa | miniporc canulé (in vivo) | 101 / 110 (Lys totale) ; 91 / 110 (Lys réactive) | Lys (enfant, Lys réactive) | EV-S-0012, Q-S-0012 |
| Repas soja texturé + quinoa | miniporc (in vivo) | 102 / 111 (Lys totale) ; 58 / 83 (Lys réactive) | Lys | EV-S-0012, Q-S-0013, Q-S-0014 |
| Filet de poulet cuit au four / fumé | INFOGEST (in vitro) | AA le plus bas 125 / 116 (enfant) | Leu / Val (pas limitant) | EV-S-0010, Q-S-0008, Q-S-0009 |
| Poulet (filet et cuisse) | INFOGEST | ≥ 100 | — | EV-S-0013, Q-S-0036 |
| 5 analogues végétaux de poulet du commerce | INFOGEST | 52–65 | non précisé (résumé) | EV-S-0013, Q-S-0015 |
| Biomasse de mycoprotéine ABUNDA | INFOGEST | 83 / 97 | soufrés (Met+Cys) | EV-S-0001, Q-S-0001, Q-S-0002 |
| Analogues de filet de poulet à la mycoprotéine (2) | INFOGEST | 85–89 / 106–111 | histidine | EV-S-0002, Q-S-0004 à Q-S-0007 |
| Solein (émulsion) | digestion statique | 51 (> 3 ans) | isoleucine | EV-S-0003, Q-S-0017 |
| Rappel ingrédients : soja / pois / blé | porc | 91 / 70 / 48 | Met+Cys / Met+Cys / Lys | EV-A-0043 |

**Lecture.**
1. **Poulet.** La seule mesure in vivo trouvée porte sur un *repas* (filet + quinoa) : DIAAS adulte 110, inchangé quand on remplace la lysine totale par la lysine réactive (EV-S-0012). La valeur « 108 » souvent citée pour le poulet dans les revues provient d'une revue (Kaur 2022) et non d'une mesure primaire retrouvée (journal, PMC13402606) ; elle n'a pas été enregistrée.
2. **La chaleur de texturation coûte de la lysine.** Le soja texturé a une TID globale non différente de celle du poulet (93,8 vs 96,4 %, NS ; EV-S-0011), ce qui confirme EV-A-0012 ; mais calculé avec la lysine réactive, son DIAAS adulte tombe de 111 à 83 et celui de l'enfant de 102 à 58 (EV-S-0012). **C'est un mécanisme nouveau pour la base** : la HME (130–170 °C) peut dégrader la qualité protéique même quand la digestibilité totale reste bonne. Les auteurs estiment que la vraie valeur se situe entre les deux calculs.
3. **Mycoprotéine.** La biomasse est limitée par les acides aminés soufrés (83 % chez l'enfant), et les analogues de poulet par l'histidine (85–89 %) : ils satisfont le seuil adulte mais pas celui de l'enfant de 3 à 10 ans (EV-S-0001, EV-S-0002). C'est cohérent avec la Corée, où les analogues végétaux contiennent 34 % d'histidine et 38 % de méthionine de moins que les produits carnés (EV-S-0042). Le « PDCAAS de 0,99 » souvent cité pour la mycoprotéine (Ariëns 2026, introduction ; Imperial 2025) ne se retrouve donc pas en DIAAS in vitro pour l'enfant.
4. **Protéines bactériennes.** Le profil brut de Solein couvre les besoins FAO (> 3 ans), mais son ivDIAAS n'est que de ~51 % (EV-S-0003). C'est l'écart le plus fort trouvé entre profil et qualité digestible ; la lyse cellulaire et la matrice en sont des causes plausibles, non testées.

### 2.2 Ce qui reste incertain
- Toutes les valeurs « analogue » sont **in vitro**, avec duplicats (Ariëns) ou connues par résumé seulement (Alotaibi, Caliskan). Aucun DIAAS in vivo de mycoprotéine ou de SCP n'a été trouvé.
- La digestibilité in vitro des analogues végétaux (81–93 %, EV-S-0013) est plus basse que les TID in vivo publiées (> 0,90, EV-A-0012 ; 93,8 %, EV-S-0011) : **nouvelle contradiction de méthode** (§7).

---

## 3. Énergie et coûts industriels (KG-C02, KG-C06)

### 3.1 Extrusion humide et cellule de cisaillement

| Grandeur | Valeur | Échelle | Nature | Réf. |
|---|---|---|---|---|
| SME, HME gluten/arachide | 699–759 kJ/kg (≈ 0,19–0,21 kWh/kg) | pilote, 6 kg/h | mesurée (mécanique seule) | EV-S-0007, Q-S-0032 |
| SME, HME soja/tournesol | 41,6–84,5 Wh/kg | laboratoire, 0,5 kg/h | mesurée (mécanique seule) | EV-S-0008, Q-S-0033 |
| Débits des études publiées | 0,45–30 kg/h de poudre | labo/pilote | compilation | EV-S-0046, Q-S-0095 |
| Débit d'une filière industrielle (PolyCool 1000) | > 1 000 kg/h | industrielle | allégation du fabricant | EV-S-0043, Q-S-0093 |
| Cellule de Couette vs extrusion | 18,5–32,6 vs 200–1 200 kJ/kg | pilote (7 L) | déclaration presse | EV-S-0009, Q-S-0034, Q-S-0035 |

**Constat.** On dispose désormais de mesures d'énergie *mécanique* au laboratoire et au pilote, qui varient d'un facteur 5 selon la formulation, l'humidité et l'échelle (EV-S-0007, EV-S-0008), et d'une allégation de débit industriel (EV-S-0043). La SME diminue proportionnellement au débit à vitesse constante (EV-S-0046), ce qui interdit d'extrapoler les SME de laboratoire à une ligne industrielle. **Aucune donnée publique d'énergie totale** (mécanique + chauffage du fourreau + refroidissement de la filière) par kg d'extrudat industriel n'a été trouvée en anglais, coréen ou français (résultat négatif documenté) : KG-C02 n'est que partiellement réduit. Le chiffre de la cellule de Couette (≥ 10 fois moins d'énergie) reste une déclaration orale non vérifiée (EV-S-0009, confiance très faible).

### 3.2 Mycoprotéine : procédé et énergie

- **Procédé vérifié.** Deux fermenteurs *airlift* de 155 m3 en culture continue (« glucose-stat »), D = 0,17–0,20 h⁻¹, 10–15 g/L de biomasse, 30 t/h de culture récoltée chacun, 10 000–14 000 t/an (EV-S-0033, EV-S-0034 ; Q-S-0067 à Q-S-0071). La productivité volumique est d'environ 1,7–3,0 g/L/h et le débit de 300–450 kg de matière sèche/h par fermenteur avant réduction de l'ARN (calcul de l'agent). Cela confirme EV-A-0040, que l'audit n'avait vérifiée que sur résumé (demande du coordinateur).
- **Pénalité de la réduction de l'ARN.** Chauffage à 68 °C pendant 20–30 min, avec une perte de matière sèche pouvant atteindre 30 % (EV-S-0035, Q-S-0074).
- **Seul inventaire énergétique public.** Il s'agit des données d'usine de 2010 (Finnigan), reprises par ESU/BAFU : 1,66 kWh d'électricité et 13 MJ de vapeur (gaz naturel) par kg de mycoprotéine. En 2015, la vapeur provenait de chaleur fatale d'une usine voisine, et l'énergie représentait 46 % de l'empreinte (EV-S-0037 ; Q-S-0078, Q-S-0079). À 11–13 g de protéines/100 g (Q-A-0020 ; Moore et al. : 30 % de MS × 44 % de protéines), cela fait environ 13–15 kWh d'électricité et 98–118 MJ de chaleur par kg de protéine pour la seule étape de fermentation (calcul de l'agent).
- **Coût.** Aucune TEA publique lue (Upcraft 2021 inaccessible ; les 3,55 USD/kg de Q-E-0066 restent sans source primaire). L'industriel déclare que le sucre et les utilités déterminent le prix au kg, que ces deux postes sont volatils et que la hausse des coûts a freiné les ventes (EV-S-0045).

### 3.3 Protéines bactériennes

| Indicateur | H2-SCP (modèle) | Solein (annonces) | Méthanotrophe (FeedKind) | Gaz sidérurgiques (C. autoethanogenum) |
|---|---|---|---|---|
| Énergie | 37,8 kWh/kg SCP sèche, soit ≈ 47–76 kWh/kg de protéine (EV-S-0005) ; 70–73 MWh/t de protéine (Q-E-0042) | ≈ 47 kWh/kg de Solein, soit ≈ 65–70 kWh/kg de protéine à 68–73 % de protéines (EV-A-0020) (calcul de l'agent, EV-S-0031, Q-S-0064) | gaz naturel = 4,4 t CO2e/t de produit (EV-S-0027) | n.d. |
| Coût | 4,04–16,24 USD/kg SCP au détail (EV-S-0006) ; 5 500–6 100 €/t de protéine en 2028 (EV-E-0046) | n.d. ; « l'électricité, une part importante des coûts » (EV-S-0032) | n.d. | perte brute de 24,4 % en 2025 (EV-S-0029) |
| CAPEX | 3 800–8 500 USD/(t/an) (Q-S-0031) ; 14 567 €/t de protéine (Q-E-0043) | ≈ 18 000 €/(t/an) annoncés (calcul de l'agent, Q-S-0066) | n.d. | n.d. |
| Échelle réelle | modèle | 160 t/an (Factory 01, EV-E-0054) ; 50 000 t/an en projet | usine de Chongqing à l'arrêt (EV-S-0044) | 23 200 t/an de capacité (EV-S-0029) |

**Lecture.**
- *Cohérence des ordres de grandeur.* Les trois estimations énergétiques indépendantes de la SCP à l'hydrogène convergent vers 50–75 kWh d'électricité par kg de protéine : modèle García Martínez, modèle Fasihi, et chiffre implicite de l'annonce de Solar Foods. C'est 3 à 6 fois l'électricité de la fermentation de la mycoprotéine (≈ 13–15 kWh/kg de protéine, §3.2 ; calcul de l'agent). Cette dernière consomme en revanche aussi de la chaleur et du sucre.
- *Le CAPEX annoncé par Solar Foods dépasse les modèles.* Environ 18 000 €/(t/an), contre 3 800–8 500 USD/(t/an) et 14 567 €/t de protéine (calculs indicatifs).
- *Le réel est déficitaire.* Les deux seuls producteurs industriels de SCP pour l'aliment animal documentés ici sont soit en perte brute (Shougang LanzaTech, dépendant du prix de son coproduit éthanol et de l'approvisionnement en gaz ; EV-S-0029, EV-S-0030), soit à l'arrêt pour « difficultés de montée en échelle plus grandes que prévu » (Calysseo/FeedKind ; EV-S-0044). Avec la cession d'actifs de Meati pour environ 4 M USD (EV-A-0041), ce sont trois échecs ou difficultés économiques majeurs en voie C microbienne.

---

## 4. ACV primaires, base produit et base protéine (CT-11)

### 4.1 Les chiffres primaires trouvés

| Produit | kg CO2e/kg de produit | Périmètre / année | Nature | Réf. |
|---|---|---|---|---|
| Mycoprotéine (Finnigan) | 2,4 | usine, 2010 | données d'usine | Q-S-0080 |
| Mycoprotéine (Quorn/Carbon Trust) | 1,6 | cradle-to-gate, 2015 | industriel | Q-S-0081 |
| Mycoprotéine (ESU indépendant) | 2,44 | sortie d'usine, 2016 | ACV | Q-S-0082 |
| Mycoprotéine (Carbon Trust) | 1,137 | cradle-to-processor gate, 2018 | industriel | Q-S-0019 |
| Mycoprotéine (page Quorn, rapport 2023) | 0,5 | farm-to-factory gate | industriel | Q-S-0023 |
| Mycoprotéine (mémoire, procédé modélisé) | 74,27 | modèle | modèle non calibré | Q-S-0096 |
| Quorn haché | 6,8 (2010) ; 2,4 (2015) ; 4,99 au supermarché suisse (2016) ; 3,08 au supermarché néerlandais (2024) | variables | ACV | Q-S-0083, Q-S-0084, Q-S-0086 |
| Quorn Pieces | 1,72 | 2018 | industriel | Q-S-0020 |
| Quorn (compilation UBA) | 4,1–4,6 | littérature | compilation | Q-S-0075 |
| Poulet UK/Europe (Carbon Trust) | 5,93 (4,4–9,0) | viande comestible | littérature | Q-S-0021 |
| Poulet (UBA) | 3,8–4,3 | comestible | compilation | Q-S-0076 |
| Filet de poulet (RIVM 2024) | 3,94 | supermarché NL | base officielle | Q-S-0085 |
| FeedKind (gaz fossile) | 5,82 | usine modélisée | modèle | Q-S-0050 |
| Tofu / hamburger végétarien (RIVM) | 2,29 / 2,03 | supermarché NL | base officielle | Q-S-0087, Q-S-0088 |

### 4.2 Passage à la base protéine (calculs de l'agent)

Hypothèses : mycoprotéine 11–13 g de protéines/100 g ; filet de poulet cru 23,6 g/100 g (Q-A-0008) ; FeedKind et SPC directement par kg de protéine (source).

| Produit | kg CO2e/kg de protéine |
|---|---|
| Mycoprotéine, valeur Quorn 2023 (0,5) | ≈ 3,8–4,5 |
| Mycoprotéine, Carbon Trust 2018 (1,137) | ≈ 8,6–10,3 |
| Mycoprotéine, Quorn 2015 (1,6) | ≈ 12–15 |
| Mycoprotéine, ESU 2016 (2,44) | ≈ 18–22 |
| L-mycoprotéine de résidus agricoles (Upcraft 2021, cité par Smetana 2023, SRC-E-0005) | 23,66 (valeur publiée, secondaire) |
| Poulet, RIVM 2024 (3,94) / UBA (3,8–4,3) / Carbon Trust (5,93) | ≈ 16,7 / 16–18 / 25 |
| FeedKind : gaz fossile → biogaz → biogaz + renouvelable | 7,99 → 2,99 → 2,23 (Q-S-0051 à Q-S-0053) |
| Concentré protéique de soja / farine de poisson | 0,79 / 2,6–2,8 (Q-S-0054, Q-S-0055) |

Pour le Quorn haché, le RIVM ne donne pas de teneur en protéines, et NEVO n'a pas pu être téléchargé. Le seuil de parité avec le filet de poulet par kg de protéine serait d'environ 18 g de protéines/100 g (3,08 / 16,7 ; calcul de l'agent). En dessous de ce seuil, le Quorn haché émet plus que le filet par kg de protéine.

### 4.3 Résolution proposée de CT-11

La contradiction oppose « la mycoprotéine figure parmi les plus impactants » (EV-A-0049) à « 0,73 kg CO2e/kg » (EV-A-0050). Elle s'explique par quatre facteurs cumulés, tous documentés :
1. **L'année et la source d'énergie.** La valeur publiée par l'industriel est passée de 2,4 (2010) à 0,5 kg CO2e/kg (2023) (EV-S-0038, EV-S-0004). La vapeur au gaz naturel (13 MJ/kg) a été remplacée par de la chaleur fatale, et l'énergie pesait 46 % de l'empreinte (EV-S-0037). Les ACV fondées sur des inventaires anciens ou génériques (Smetana 2015 : 5,55–6,15, cité dans la Tab. 4.5 de SRC-S-0028 ; UBA : 4,1–4,6, EV-S-0036) décrivent donc un procédé antérieur ou générique, pas l'usine actuelle.
2. **Le mode de calcul.** Données d'usine vs procédé modélisé. Un modèle qui suppose une stérilisation à la vapeur donne 74 kg CO2e/kg (EV-S-0047), hors de toute mesure.
3. **La base.** Avec 11–13 % de protéines contre 23,6 % pour le filet cru, la mycoprotéine perd un facteur ~2 en passant à la base protéine. Avec la valeur indépendante de 2016 (ESU), elle rejoint le poulet (18–22 vs 16–25 kg CO2e/kg de protéine). Elle ne reste nettement meilleure qu'avec les valeurs récentes de l'industriel, invérifiables faute d'inventaire publié (EV-S-0038, §4.4.2.4).
4. **Le périmètre et la recette.** Sortie d'usine vs supermarché ; blanc d'œuf dans le Quorn haché (2,5–4 %). La base RIVM 2024, indépendante et cohérente, donne Quorn haché 3,08 contre filet 3,94 kg CO2e/kg par kg de produit, soit seulement −22 % (EV-S-0040). Le RIVM interdit pourtant explicitement de comparer des aliments individuels avec ces données (EV-S-0041).

**Arbitrage.** Par kg de produit, la mycoprotéine actuelle émet moins que le poulet : de −22 % (RIVM, indépendant) à −90 % (Quorn). Par kg de protéine, l'avantage est incertain : de « nul » (inventaire indépendant de 2016) à « ×4 » (valeur 2023 de l'industriel). Ajusté de la digestibilité (ivTD ~0,8 contre TID ~0,96 pour le poulet, méthodes différentes) et du DIAAS de l'enfant (histidine), l'avantage se réduit encore. **CT-11 passe de « non tranché » à « expliqué ; dépend de l'année, de la base et du périmètre ».** La donnée qui trancherait est l'inventaire Carbon Trust 2023 de Quorn, ou une ACV indépendante avec données d'usine récentes et unité fonctionnelle « kg de protéine digestible ».

**Extension aux SCP.** Pour l'aliment animal, FeedKind n'est pas moins émetteur que la farine de poisson par kg de protéine sans énergie renouvelable. Il émet 3 à 10 fois plus que le concentré de soja quel que soit le scénario (EV-S-0028). Le rapport présente en outre une incohérence interne entre le texte (7,99) et sa Table B (2,23–2,65 sans scénario indiqué), signalée en EV-S-0027.

---

## 5. Arôme du poulet et des analogues (KG-C04)

### 5.1 Odorants clés du poulet (AEDA/GC-O)
- **Bouillon.** FD 128 pour la méthylpyrazine, le méthional et le (E,E)-2,4-décadiénal, et FD 64 pour le 2-éthyl-4-méthylthiazole. Ces quatre composés reconstituent l'essentiel de la note grasse et animale (1,0 → 4,4–4,6 sur un maximum de 5,0) (EV-S-0015, EV-S-0016 ; Q-S-0037 à Q-S-0041).
- **Bouillon (Chine).** Le 2-méthyl-3-furanthiol, le méthional et le 2,4-décadiénal sont confirmés par recombinaison-omission. La meilleure saveur est associée à davantage d'AGPI et de précurseurs hydrosolubles : ribose, cystéine, thiamine (EV-S-0020).
- **Poulet rôti.** S'y ajoutent les aldéhydes lipidiques, les pyrazines et la furanone HDMF (OAV 12,9) (EV-S-0021).
- **Fractionnement (Japon, 1978).** La fraction hydrosoluble donne le meilleur arôme de poulet ; le dégraissage supprime le caractère « poulet » (EV-S-0017).

### 5.2 Analogues : la seule comparaison trouvée
Sur trois nuggets de « poulet » végétaux chinois (SPME-GC-O-MS, ROAV), les sept odorants clés sont tous des aldéhydes. Aucun thiol ni thiazole carné n'y figure. Le seul soufré odorant vient des alliacées, avec un ROAV de 0,24. Les auteurs attribuent le déficit de note spécifique aux arômes de synthèse (EV-S-0018, EV-S-0019). La méthode (SPME, sans AEDA) capte mal les thiols : l'absence de MFT est un indice, pas une preuve. Aucune comparaison AEDA analogue–poulet n'existe en anglais (résultat négatif).

### 5.3 Brevets d'arômes de réaction
- **Brevet fondateur (priorité 1955).** Ribose + cystéine donne une note « proche du porc », pas du poulet (EV-S-0024).
- **Brevet DSM EP3054792B1 (priorité 2013, « actif » jusqu'en 2034 selon Google).** L'acide arachidonique ajouté à sucre + cystéine, extrudé à 80–140 °C, donne un « authentic boiled fatty chicken ». Sans lui, la note de poulet reste faible (EV-S-0023). C'est **l'antériorité la plus directe d'INN-10** : le lipide spécifique n'est pas un phospholipide quelconque mais un AGPI n-6 en C20, et l'extrudeuse peut servir de réacteur.
- **Recettes industrielles chinoises.** Cystéine + pentoses + thiamine + graisse de poulet (EV-S-0025). La note spécifique y vient de la graisse animale.
- **Ajinomoto.** Extrait de levure riche en γ-glutamylcystéine comme précurseur soufré non animal (EV-S-0026, confiance très faible).
- **Hydrolysats de poulet.** La cystéine libre est le précurseur efficace du MFT ; l'oignon et le djenkol ne la remplacent pas (EV-S-0022).

---

## 6. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Fonctionne.**
- Mycoprotéine en continu à grande échelle depuis 30 ans, avec une productivité volumique de 1,7–3 g/L/h (EV-S-0034).
- Empreinte par kg de produit en baisse grâce à la chaleur fatale (EV-S-0037).
- Digestibilité totale du soja texturé proche de celle du poulet in vivo (EV-S-0011).
- Lignes HME annoncées à ~1 t/h (EV-S-0043).
- Arôme « poulet bouilli » reproductible sans viande par sucre + cystéine + ARA (brevet, EV-S-0023).

**Échoue ou déçoit.**
- DIAAS enfant des analogues < 100 : 52–65 pour les végétaux, 85–89 pour la mycoprotéine (EV-S-0013, EV-S-0002).
- ivDIAAS de Solein ≈ 51 (EV-S-0003).
- Lysine réactive dégradée par la texturation (EV-S-0012).
- SCP industrielles en perte ou à l'arrêt (EV-S-0029, EV-S-0044).
- Analogues de poulet du commerce sans odorants soufrés carnés (EV-S-0018).
- Avantage climatique par kg de protéine non démontré de façon indépendante (§4.3).

**Reste à inventer.**
1. Des analogues de poulet à DIAAS enfant ≥ 100 sans perte de lysine réactive.
2. Une génération in situ des odorants soufrés et lipidiques pendant la HME.
3. Des procédés microbiens couplés à de la chaleur fatale ou à de l'électricité bon marché, avec inventaire publié.
4. Une mesure de l'énergie totale par kg d'extrudat industriel.

---

## 7. Contradictions

| ID proposé | Sujet | Côté 1 | Côté 2 | Explication | Statut |
|---|---|---|---|---|---|
| CT-11 (précisée) | ACV de la mycoprotéine | 4,1–6,15 kg CO2e/kg, voire 74 en modèle (EV-A-0049, EV-S-0036, EV-S-0047) | 0,5–1,6 kg CO2e/kg (EV-A-0050, EV-S-0004, EV-S-0014) | Année et énergie (chaleur fatale), modèle vs usine, base produit vs protéine, périmètre (EV-S-0037, EV-S-0038, EV-S-0040) | Expliquée ; dépend de la base |
| nouvelle | Digestibilité des analogues végétaux | In vitro 81–93 %, DIAAS 52–65 (EV-S-0013) | TID in vivo > 0,90 (EV-A-0012) ; soja texturé 93,8 % NS vs poulet (EV-S-0011) | INFOGEST sous-estime peut-être la digestion de matrices fibreuses ; produits différents | Ouverte : comparer les deux méthodes sur les mêmes produits |
| nouvelle | Qualité des protéines bactériennes | Profil d'AA complet, « haute qualité » (EV-A-0020 ; revues) | ivDIAAS de Solein ≈ 51 (EV-S-0003) | Digestibilité cellulaire faible (paroi, matrice) | Ouverte : DIAAS in vivo nécessaire |
| nouvelle | Qualité protéique de la mycoprotéine | PDCAAS 0,99 (cité par Ariëns 2026 et Imperial 2025) | ivDIAAS enfant 83 (soufrés ; EV-S-0001) | Indice et méthode différents (PDCAAS tronqué, profil 2–5 ans) | Expliquée par la méthode |
| interne | Rapport FeedKind | 7,99 t CO2e/t de protéine (scénario 1, texte) | 2,229–2,648 (Table B, scénario non indiqué) (EV-S-0027) | La Table B correspond au scénario renouvelable | Signalée |
| mineure | Marge de Shougang LanzaTech | −24,4 % (EV-S-0029) | −24,5 % (EV-S-0030) | Arrondis de deux reprises | Sans conséquence |

---

## 8. Lacunes : réduites, persistantes

- **KG-C01 (réduite).** Premiers DIAAS chiffrés pour le poulet (in vivo sur un repas, in vitro), la mycoprotéine, des analogues et Solein. *Reste* : DIAAS in vivo de la mycoprotéine et des SCP ; texte intégral de Hodgkinson 2025 ; DIAAS de C. glutamicum (Park 2024, 403).
- **KG-C02 (partiellement réduite).** SME mesurées au labo et au pilote, débit industriel annoncé, déclaration pour la cellule de Couette. *Reste* : kWh/kg total d'une ligne industrielle (aucune source) ; vérification du chiffre de Krintiras (thèse inaccessible).
- **KG-C04 (réduite).** Odorants clés du poulet (3 AEDA), une comparaison analogue/poulet (SPME), brevets. *Reste* : AEDA tête-à-tête analogue vs poulet, avec quantification du MFT.
- **KG-C05 (marginale).** Zinc −57 % dans les analogues coréens (EV-S-0042) ; aucune donnée de biodisponibilité nouvelle.
- **KG-C06 (partiellement réduite).** Inventaire énergétique de la mycoprotéine (2010), postes de coût déclarés, TEA H2-SCP, CAPEX annoncé de Solar Foods, données financières réelles d'un producteur de SCP. *Reste* : TEA publique de la mycoprotéine (Upcraft 2021 bloqué), coût unitaire réel de la protéine de Shougang LanzaTech (prospectus HKEX à lire).

---

## 9. Pistes d'innovation

### Piste S-1 (révision d'INN-10) — Arôme de poulet généré in situ dans l'extrudeuse
- **Problème.** Les analogues de poulet manquent d'odorants soufrés carnés (EV-S-0018, EV-S-0019). Leurs arômes de surface n'ont pas de note « poulet ».
- **Solutions actuelles.** Arômes de réaction ajoutés (EV-S-0025), à base de graisse animale. Brevet DSM : sucre + cystéine + ARA extrudés séparément (EV-S-0023).
- **Insuffisances.** Ajout après cuisson, volatils perdus. La spécificité « poulet » dépend de la graisse animale ou de l'ARA.
- **Preuves d'une approche nouvelle.**
  - Les températures de la HME mesurées ou compilées (99–177 °C ; EV-S-0046, EV-S-0007) recouvrent celles revendiquées par DSM (80–140 °C, ~3 min ; EV-S-0023).
  - La cystéine libre est le précurseur efficace du MFT (EV-S-0022).
  - Le caractère « poulet » exige précurseurs hydrosolubles + lipides (EV-S-0017).
- **Hypothèse.** Ajouter 0,2–1 % de cystéine, un pentose et 0,1–0,5 % d'huile riche en ARA dans le pré-mélange HME ; un extrait de levure pourrait remplacer une partie de la cystéine (EV-S-0026). L'analogue obtiendrait, après cuisson, des FD ≥ 64 pour le méthional, le 2,4-décadiénal et le MFT, et une note « poulet » supérieure à celle d'un arôme de surface.
- **Expérience.**
  - Plan 3 × 3 (dose de précurseurs × dose d'ARA) sur une extrudeuse pilote.
  - SAFE-AEDA face au bouillon et au filet rôti (protocoles SRC-S-0011 et SRC-S-0015).
  - Recombinaison-omission ; panel de 30 personnes (tests triangulaires et descriptifs).
  - Dosage de la lysine réactive : les précurseurs Maillard pourraient aggraver EV-S-0012.
- **Critères.** *Succès* : MFT détecté (FD ≥ 16), note « poulet » +2 points sur 9, perte de lysine réactive ≤ 10 %. *Échec* : notes soufrées « œuf/oignon », chute du DIAAS, oxydation de l'ARA.
- **Coûts et risques.** Coût modeste, plusieurs mois de pilote. **Risque de liberté d'exploitation** : la revendication 1 d'EP3054792B1 couvre « heated and extruded » un mélange sucre réducteur + cystéine + ARA. Il faut une analyse juridique (→P) ou un lipide alternatif, par exemple des phospholipides riches en ARA.

### Piste S-2 — Analogue de poulet « DIAAS enfant ≥ 100 » : correction histidine + soufrés et texturation douce
- **Problème.** Les DIAAS enfant restent inférieurs à 100 : histidine pour la mycoprotéine (EV-S-0002), soufrés pour la biomasse (EV-S-0001), Met et His en Corée (EV-S-0042). La lysine réactive est dégradée par la texturation (EV-S-0012).
- **Hypothèse.** Un mélange mycoprotéine + 15–25 % d'une protéine riche en His et en soufrés, texturé à ≤ 140 °C ou en cellule de cisaillement (EV-S-0009), atteint un ivDIAAS enfant ≥ 100 avec une perte de lysine réactive ≤ 10 %. La protéine de pomme de terre, qui « amène la plupart des mélanges à 100 » (EV-A-0044), est un candidat à tester.
- **Expérience.** INFOGEST (protocole d'Ariëns, SRC-S-0001) puis confirmation sur miniporc (protocole SRC-S-0002), avec dosage de la lysine réactive. Comparer HME 160 °C, HME 130 °C et cellule de cisaillement.
- **Critères.** *Succès* : ivDIAAS enfant ≥ 100 et DIAAS in vivo ≥ 100 (lysine réactive). *Échec* : texture non fibreuse aux basses températures.
- **Coûts et risques.** Un essai sur miniporcs (6 animaux, environ 6 mois) ; allergénicité selon la protéine ajoutée.

### Piste S-3 — Fermentation protéique couplée à de la chaleur fatale (mycoprotéine) ou à une électricité très bon marché (SCP à l'hydrogène)
- **Fondement.**
  - L'énergie pèse 46 % de l'empreinte de la mycoprotéine ; la vapeur de chaleur fatale a contribué à diviser par ~2 à 4 l'empreinte publiée (EV-S-0037, EV-S-0038).
  - La SCP à l'hydrogène demande 50–75 kWh/kg de protéine (EV-S-0005, EV-S-0031).
  - Les SCP déficitaires dépendent d'un intrant ou d'un coproduit volatil (EV-S-0030).
- **Hypothèse.** Une unité de mycoprotéine adossée à une source de chaleur fatale à ≥ 70 °C, qui couvre stérilisation et réduction de l'ARN (68 °C, EV-S-0035), descend sous 10 kg CO2e/kg de protéine avec un inventaire publié et vérifié. C'est plus de 40 % sous le filet de poulet (16,7, Q-S-0085).
- **Validation.** ACV attributionnelle avec données d'usine, unité fonctionnelle « kg de protéine digestible », revue critique ISO 14040 (la lacune signalée par le RIVM, EV-S-0041).
- **Critères.** *Succès* : ≤ 10 kg CO2e/kg de protéine, quel que soit le choix d'allocation de la chaleur fatale. *Échec* : résultat qui dépend entièrement de la règle d'allocation.
- **Risques.** Dépendance au site industriel voisin, comme pour Shougang LanzaTech avec son gaz (EV-S-0030).

**Pistes existantes.**
- **INN-09** (yuba laminé) : renforcée par l'écart d'énergie mécanique entre la cellule de Couette (déclaration, ≤ 33 kJ/kg) et la HME mesurée (150–760 kJ/kg). La mesure de l'énergie totale reste à faire.
- **INN-15** : inchangée, aucune donnée nouvelle sur la biodisponibilité.

---

## 10. Recherches restantes (prioritaires)

1. **Prospectus HKEX de Shougang LanzaTech** (anglais/chinois) : volume et prix unitaire de la protéine microbienne, coût de revient. C'est le seul coût industriel réel de SCP accessible.
2. **Inventaire de la mycoprotéine.** Rapport Carbon Trust 2023 de Quorn, Upcraft 2021 (autre miroir), Finnigan 2010 (original).
3. **DIAAS in vivo** de la mycoprotéine et d'une SCP bactérienne ; texte intégral de Hodgkinson 2025 ; Park 2024.
4. **AEDA tête-à-tête** d'un analogue de poulet du commerce et du filet rôti, avec dosage du MFT par dilution isotopique.
5. **Énergie totale d'une ligne HME industrielle** (fabricants, ACV d'usine, thèse Krintiras pour la cellule de Couette) ; protéine du Quorn haché (NEVO) pour fermer la comparaison RIVM par kg de protéine.
