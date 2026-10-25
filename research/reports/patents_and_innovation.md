# Brevets, recherche industrielle et innovation — muscle de poulet (voies A, B, C)

*Agent P — brouillon de phase 3–4, 2026-10-25. Questions couvertes : RQ-P1 à RQ-P5 et RQ-X5 (responsable principal). Toutes les affirmations renvoient à `research/agents/P/{sources,evidence,quant}.csv` (identifiants `SRC-`, `EV-`, `Q-`), à `patent_map.csv` (44 brevets) et à `actors.csv` (49 acteurs).*

> **Règle de lecture.** Une revendication de brevet décrit ce que le déposant veut protéger, pas ce qui fonctionne. Les lignes `patent_claim` ont une confiance « low » au plus ; quand une valeur de brevet est citée ici, c'est pour situer ce qui est *tenté*, jamais comme preuve de faisabilité. Les chiffres d'entreprise sont marqués `company_claim` et les sorties de modèles `model_output`.

---

## 1. Périmètre et méthode

**Objet.** Cartographier brevets, acteurs, prototypes, échecs et problèmes non résolus pour les trois voies de production de muscle de poulet : A (élevage, aliment, génétique), B (viande cultivée), C (substituts végétaux, fongiques, microbiens, fermentation de précision) ; en déduire des pistes de recherche testables.

**Bases et outils.** Google Patents (recherche via WebSearch restreint à `patents.google.com`, lecture page par page), Europe PMC (texte intégral libre), Crossref (vérification), J-STAGE, HAL, theses.fr, registre Companies House (UK), communiqués d'entreprises et presse spécialisée. Journal complet : `research/agents/P/search_log.md` (72 lignes, 9 langues : en, zh, ja, ko, fr, es, nl, pt, sv).

**Échantillon de brevets.** 44 documents (27 voie B, 12 voie C, 5 voie A), juridictions de publication WO 21, US 13, CN 5, EP 2, AU 1, JP 1, KR 1 ; dates de priorité de 1995 à 2024 (pic 2017–2021). Il s'agit d'un **échantillon raisonné**, pas d'une analyse de familles exhaustive : la sélection a privilégié (i) les déposants les plus actifs selon GFI APAC (EV-P-0053), (ii) les brevets explicitement « poulet/aviaire », (iii) au moins un document par sous-domaine et par grande juridiction asiatique.

**Limites d'accès (importantes pour l'interprétation).**
- Espacenet, PATENTSCOPE, CNIPA, KIPRIS, J-PlatPat : bloqués ou inutilisables ; Lens.org : application JavaScript non exploitable ; USPTO ppubs : PDF images sans couche texte (pas d'OCR disponible).
- Google Patents par `curl` : 6 pages complètes obtenues puis blocage HTTP 503 (« Sorry ») continu pendant plus de 30 minutes, probablement dû à l'IP partagée. Les 38 autres brevets ont été lus par WebFetch, qui tronque à 100 000 caractères : bibliographie, résumé et début de description lus, **revendications non lues** (accès noté `abstract_only` dans `patent_map.csv`, `partial_text_read` dans les sources).
- Les statuts juridiques (« Active », « Ceased », « Abandoned », « Expired ») sont **des estimations de Google Patents**, pas des certificats de registres officiels. « Ceased » sur un WO signifie la fin de la phase internationale PCT, pas l'abandon des phases nationales.
- Articles clés payants : Pasitka et al. 2023 et 2024 (Nature Food) lus en résumé seulement ; deux analyses de brevets de 2026 (Li, *Future Foods* ; Sperlova et al., *Innovation*) inaccessibles (403), enregistrées en `metadata_only` (SRC-P-0070, SRC-P-0071).
- Bug d'outil signalé puis corrigé par le coordinateur : les titres CJK étaient vus comme des doublons ; les trois sources concernées ont été réenregistrées puis corrigées (SRC-P-0065 à 0067).

**Textes intégraux lus (hors brevets).** Humbird 2021 (SRC-E-0001), Hwang et al. 2025 (SRC-P-0054), Kostrakiewicz-Gierałt 2024 (SRC-P-0055), Hoek et al. 2026 (SRC-P-0056), Riquelme-Guzmán et al. 2024 (SRC-P-0057), Shima 2023 en japonais (SRC-P-0066), Ferdous et al. 2026 (SRC-A-0012), revue sur la stabilité génomique 2026 (SRC-P-0068), Mia et al. 2026 (SRC-P-0069), plus 19 articles de presse, communiqués et fiches de registre.

---

## 2. RQ-P1 — Cartographie des brevets

### 2.1 Qui dépose ?

La seule source quantitative globale trouvée est l'analyse de GFI APAC (SRC-P-0058), dont la base et la requête ne sont pas publiées (confiance faible, EV-P-0053) : UPSIDE Foods domine (143 demandes, 43 familles ; Q-P-0029), suivie d'Aleph Farms (83/14), Mosa Meat (54/13), Joes Future Food (30/25), Believer Meats (28/5) et Yissum (26/5). **Huit des vingt premiers déposants sont chinois** (Q-P-0030), dont cinq organismes publics (Jiangnan, Zhejiang, China Meat Research Centre, Ocean University of China, Nanjing Agricultural University). Une revue de 2025 reprend ce constat : les universités et organismes publics chinois ont déposé plus de brevets de viande cultivée que leurs homologues américains et européens réunis (EV-P-0054, source en partie dépendante de GFI).

Pour les analogues végétaux, une revue PRISMA de 183 brevets anglophones (2014–2023 ; Q-P-0031) montre une hausse en 2020–2022, des déposants surtout américains, Nestlé en tête et le soja comme matière première la plus fréquente (EV-P-0055). Le biais linguistique de cette revue (brevets CN/JP/KR non anglophones exclus) est probablement important vu le poids asiatique observé pour la viande cultivée.

### 2.2 Ce que l'échantillon de 44 brevets révèle

**Tableau 1 — Répartition de l'échantillon par domaine (patent_map.csv).**

| Domaine | n | Exemples (déposant) |
|---|---|---|
| B-media | 9 | homologues végétaux du sérum (Future Meat/Yissum), activateurs de FGF (Yissum), albumine recombinante (Tufts), sans ammoniac (Mosa), sérum d'abattage (Chung-Ang), FGF-2 thermostable (BTL), inhibiteur ERK (Yeda), milieu pour cellules de poulet avec SVF (Shantou Debao) |
| B-cell-line | 7 | HIPPO/YAP et GS/TERT (UPSIDE), lignées sans facteurs de croissance (UPSIDE), CEF immortalisés (Intervet), EBx (Valneva → Vital Meat), cellules productrices de phytoène (Tufts) |
| B-scaffold | 5 | soja texturé (Aleph/Technion), gel de plasma (U. Tokyo/Nissin), microporteurs et hydrogels (CMRC), fibres microfluidiques (NJAU) |
| B-product | 4 | poulet in vitro DF-1 (JUST/GOOD Meat), hybride (SuperMeat), viande 3D pionnière (van Eelen), viande à extraits naturels (KR) |
| B-bioreactor | 2 | fibres creuses comestibles (Merck), cuves en parallèle à milieu conditionné (Fork & Goode) |
| C-myco | 5 | souche polyploïde (Marlow/Quorn), continu avec recyclage (3F Bio/ENOUGH), Neurospora (Better Meat Co ; Emergy/Meati), tapis de surface (Fynder) |
| C-SCP | 4 | Xanthobacter H2/CO2 (Solar Foods), chimiolithotrophes (Kiverdi), boucle verticale méthane (Calysta), U-loop (Unibio) |
| C-plant / C-precision-fermentation | 3 | fibres alignées (Beyond Meat), extrusion + déchiquetage type poulet (Mars), hème (Impossible) |
| A-feed / A-genetics | 5 | alimentation in ovo (NCSU/Yissum), acide guanidinoacétique (Degussa/Alzchem), phytase thermotolérante (Syngenta/Diversa → AB Enzymes), aliment à farine de larves, puce 50k SNP (CAAS) |

**Statuts (estimation Google) :** 21 PCT éteints, 10 actifs, 6 expirés, 5 en cours, 2 abandonnés.

**Six constats principaux.**

1. **Le poulet cultivé commercialisé repose sur une lignée vaccinale publique.** Le brevet JUST/GOOD Meat décrit des cellules « C1F » dérivées de la lignée UMNSAH/DF-1 (ATCC CRL-12203, déposée en 1996), spontanément immortalisée (EV-P-0005). Valneva a breveté l'usage alimentaire de ses lignées EBx en suspension sans sérum, cédées à Vital Meat (EV-P-0008), et Intervet protège des CEF immortalisés par SV40T + cTERT (EV-P-0007). Trois familles indépendantes montrent donc le **transfert de lignées aviaires de l'industrie vaccinale vers l'alimentation** (EV-P-0062). Ce transfert explique en partie l'avance du poulet sur les autres espèces : les lignées vaccinales sont déjà adaptées à la suspension et au sans-sérum. Il ne résout pas la question du muscle : ce sont des fibroblastes ou des cellules souches, pas des myocytes matures.

2. **Les revendications débordent la physique.** UPSIDE revendique des densités « d'environ 10^5 à 10^10 cellules/mL » ou « 1 à 1000 g/L » (EV-P-0002). Avec 3000 pg par cellule (hypothèse de Humbird), 10^10 cellules/mL représenteraient environ 30 kg par litre, alors que la limite de viscosité est estimée à ~86×10^6 cellules/mL (EV-P-0040, Q-P-0004). Ces plages sont un choix de rédaction juridique : elles confirment qu'il ne faut pas lire un brevet comme un résultat.

3. **Le portefeuille vise surtout le coût du milieu.** Neuf brevets sur 27 en voie B portent sur le milieu, avec trois stratégies : remplacer les protéines sériques par des homologues végétaux (EV-P-0009) ou de l'albumine recombinante (EV-P-0011) ; remplacer les facteurs de croissance par des petites molécules (EV-P-0010), par des variants thermostables (EV-P-0016) ou par l'expression autocrine dans des lignées modifiées (EV-P-0004, gain ×1,42 seulement, Q-P-0043) ; supprimer la glutamine pour éviter l'ammoniac (EV-P-0012, EV-P-0003). Une revue de 2026 déplace le problème : à grande échelle, **les acides aminés représenteraient 76 % du coût du milieu** contre 24 % pour les facteurs de croissance (EV-P-0056, Q-P-0032). Or presque aucun brevet de l'échantillon ne porte sur l'approvisionnement en acides aminés de qualité culture cellulaire. **C'est un angle mort du portefeuille.**

4. **La Chine dépose beaucoup mais pas toujours « sans sérum ».** Un brevet chinois délivré en 2023 pour les cellules souches musculaires de poulet repose encore sur 15–25 % de SVF (EV-P-0014). Une demande du CMRC sur les microporteurs a été rejetée (EV-P-0020). Le portefeuille public chinois se concentre sur la structuration (microporteurs, hydrogels, fibres microfluidiques ; EV-P-0020 à EV-P-0022). Selon l'Académie chinoise d'ingénierie, plus de 80 % des bioréacteurs du marché chinois sont importés et moins de 10 % des microporteurs sont nationaux (EV-P-0058, Q-P-0035). Les brevets servent aussi une stratégie d'autonomie industrielle (voir aussi la puce SNP nationale, EV-P-0036).

5. **Une partie du socle est dans le domaine public.** Le brevet pionnier de van Eelen (priorité 1997) a expiré en 2019 (EV-P-0026). Sont aussi expirés le brevet de souche Quorn (2018), l'extrusion humide avec déchiquetage en flocons type poulet de Mars (2020), l'alimentation in ovo (2021) et la phytase thermotolérante (2024) (EV-P-0061). Plusieurs demandes ont été abandonnées ou rejetées (Emergy et Vital Meat aux États-Unis, CMRC en Chine, U. Tokyo/Nissin au Japon). Une analyse de liberté d'exploitation (non faite ici, voir piste 9) pourrait montrer qu'un produit hybride simple est réalisable presque entièrement sans licence.

6. **Les verrous de structuration sont physiques.** Merck revendique qu'une fibre creuse comestible de 1 mm ne supporte que 0,3–0,5 mm de tissu (EV-P-0023, Q-P-0037). C'est cohérent avec le principe rappelé par l'Université de Tokyo : sans vascularisation, un tissu de plus de quelques centaines de µm nécrose au centre (EV-P-0059, Q-P-0036). Les brevets d'échafaudages (soja texturé, gels de plasma, fibres) ne donnent aucune épaisseur de tissu fonctionnel au-delà de cette limite (EV-P-0018, EV-P-0019, EV-P-0022).

### 2.3 Voies A et C dans les brevets

Les brevets de nutrition avicole de l'échantillon sont anciens et souvent expirés. Ils portent des gains revendiqués modestes : alimentation in ovo +3 à 8 % de poids à l'éclosion (EV-P-0033, Q-P-0052) ; acide guanidinoacétique à 0,92 g/kg, +7 % de poids final (EV-P-0034, Q-P-0053) ; phosphate réduit à 0,225 % grâce à la phytase (EV-P-0035, Q-P-0054). En voie C, les brevets fongiques et microbiens revendiquent des densités de biomasse bien supérieures à celles des cellules animales : 18 g/L de matière sèche en continu (EV-P-0028), 41 g/L en submergé (EV-P-0030), jusqu'à 180 g/L en tapis de surface (EV-P-0029), et des taux de croissance bactériens de 0,04 à 0,12 h⁻¹ (EV-P-0031, Q-P-0050). Le transfert de gaz reste le verrou des SCP gazeuses (EV-P-0032, Q-P-0051). Le brevet de souche polyploïde de Marlow rappelle que **l'instabilité des souches en fermentation continue longue a été un verrou industriel**, résolu par la génétique de la souche (durée de campagne au moins quadruplée ; EV-P-0027). C'est une leçon directe pour la culture continue de cellules animales (piste 7).

---

## 3. RQ-P2 — Acteurs, laboratoires, prototypes

`actors.csv` liste 49 acteurs sourcés. Points saillants :

- **États-Unis** : UPSIDE (poulet ; usine EPIC annoncée à 50 000 lb/an, Q-P-0023 ; usine de Glenview suspendue, EV-P-0046), GOOD Meat (poulet DF-1, produit de détail à 3 % de cellules), Tufts (milieux, ingénierie cellulaire), Fork & Goode ; en voie C, Beyond Meat, Impossible, Better Meat Co, Fynder, Kiverdi, Calysta ; Emergy (Meati) en cession pour le bénéfice des créanciers.
- **Israël** : Believer/Future Meat et Yissum (laboratoire Nahmias), Aleph Farms/Technion, SuperMeat (hybrides de poulet), Yeda/Weizmann (différenciation).
- **Europe** : Mosa Meat (NL), Meatable (NL, dissoute), Vital Meat et Valneva (FR), Intervet (NL/US), Merck KGaA (DE), Marlow Foods et 3F Bio/ENOUGH (UK/NL), Solar Foods (FI), Unibio (DK), Mycorena (SE, faillite), Deep Branch (UK, liquidation).
- **Asie** : Jiangnan, Zhejiang, NJAU, CMRC, Tianjin USTech, Joes Future Food, Shantou Debao, IAS-CAAS (CN) ; Chung-Ang, Yonsei, DaNAgreen, CJ CheilJedang (KR) ; Université de Tokyo et Nissin (JP).
- **Prototypes et échelles démontrées** (déclaratifs) : suspension sans sérum à 500 L chez SCiFi Foods (Q-P-0016) ; bioréacteur de 700 L (500 L utiles) décrit par GOOD Meat (EV-P-0006) ; biomasse hybride à 2 000 L et filets en flacons de 2 L chez UPSIDE (Q-P-0024, Q-P-0025) ; densités de 108–130×10^6 cellules/mL rapportées par Future Meat à l'échelle de paillasse (Q-P-0006, Q-P-0008).

---

## 4. RQ-P3 — Échecs, abandons et résultats négatifs

**Tableau 2 — Échecs et abandons confirmés (source primaire ou deux médias).**

| Acteur / projet | Date | Ce qui a échoué | Preuve | Leçon |
|---|---|---|---|---|
| New Age Eats (porc cultivé) | 03/2023 | Financement ; usine pilote d'Alameda finie à 90 %, jamais ouverte ; « la science n'était pas prête pour le passage à l'échelle » (fondateur) | SRC-P-0003, SRC-P-0072 ; EV-P-0045 ; Q-P-0017 | Construire l'infrastructure avant d'avoir figé le procédé détruit le capital |
| GOOD Meat – contrat ABEC | 2021–2025 | Bioréacteurs de 250 000 L abandonnés de fait, réduits à 5×125 000 L pour « obstacles de financement » ; litige ; jugement de 4,4 M USD | SRC-P-0007, SRC-P-0008 ; EV-P-0047 ; Q-P-0018, Q-P-0019 | Le saut d'échelle géant n'a jamais été financé ; pas de preuve publique de faisabilité biologique à cette échelle |
| GOOD Meat 3 | 05/2024 | Pivot : 3 % de cellules contre ~70 % auparavant, pour baisser les coûts | SRC-A-0034, SRC-P-0059 ; EV-P-0048 ; Q-P-0020, Q-P-0021 | Le modèle économique réel actuel est l'hybride à très faible teneur cellulaire |
| UPSIDE – usine de Glenview | 02/2024 | Usine de >140 M USD (>30 M lb/an prévues) suspendue ; filets encore en flacons de 2 L | SRC-P-0009, SRC-P-0073 ; EV-P-0046 ; Q-P-0056, Q-P-0057 | « Preuves clés » à apporter à petite échelle avant l'usine |
| SCiFi Foods (bœuf hybride) | 06/2024 | Fermeture faute de financement malgré une suspension sans sérum à 500 L | SRC-P-0001, SRC-P-0002 ; EV-P-0044 ; Q-P-0015 | Une avance technique (suspension, CRISPR) ne suffit pas sans débouché autorisé |
| Mycorena (mycoprotéine) | 07/2024 | Faillite, échec de la série B | SRC-P-0006 (communiqué) ; EV-P-0050 | Les brevets deviennent des actifs de liquidation |
| Emergy / Meati (Neurospora) | 02–10/2025 | Saisie de trésorerie par le prêteur, 150 licenciements, cession pour le bénéfice des créanciers ; ~6,7 M USD de dépenses par mois selon le repreneur | SRC-P-0063 (primaire), SRC-P-0064 ; EV-P-0051 (même événement que EV-A-0041) ; Q-P-0027, Q-P-0028 | Le CAPEX et le rythme de dépense ont dépassé la croissance des ventes |
| Deep Branch (SCP CO2/H2 pour aliments) | ≤2026 | Liquidation (registre) ; causes non publiées | SRC-P-0062 ; EV-P-0052 | Un SCP fourrager doit concurrencer le prix du soja |
| Believer Meats (poulet, ex-Future Meat) | 12/2025 | Arrêt un mois après l'étiquetage USDA et après la lettre FDA ; >34 M USD de factures de construction impayées ; >390 M USD levés | SRC-P-0004, SRC-P-0005 ; EV-P-0043 ; Q-P-0012 à Q-P-0014 | **L'approbation réglementaire ne garantit pas la viabilité** : l'usine de 12 000 t/an (capacité déclarée) n'a pas trouvé de financement d'exploitation |
| Meatable (porc) | 12/2025 | Dissolution volontaire faute de nouveaux financements (~139 M USD levés) | SRC-P-0060, SRC-P-0061 ; EV-P-0049 ; Q-P-0026 | Sans marché européen ouvert, la plateforme technologique n'a pas suffi |
| Brevets abandonnés ou rejetés | 2019–2026 | Demandes US d'Emergy et de Vital Meat abandonnées ; rejet en Chine (CMRC) ; décision de rejet au Japon (U. Tokyo/Nissin) | EV-P-0061, EV-P-0020, EV-P-0019 | La propriété intellectuelle est fragile et souvent peu défendue |

**Non confirmés (recherches négatives).** Aucune insolvabilité d'ENOUGH/Abunda n'a été trouvée (deux recherches, dont une en néerlandais). Aucun arrêt documenté du chantier BioTech Foods/JBS de Saint-Sébastien (les articles trouvés datent de 2023). Ces deux cas **ne doivent pas** être classés en échec.

**Lecture transversale.** Aucun des échecs documentés n'est publiquement attribué à une impossibilité biologique précise. Les causes déclarées sont financières (levée de fonds, dette de construction, trésorerie). Mais trois signaux techniques convergent :
- l'abandon de fait des bioréacteurs géants (EV-P-0047) ;
- la persistance de la culture en flacons pour les produits structurés (EV-P-0046) ;
- la dilution à 3 % de cellules dans le produit de détail (EV-P-0048).

Ensemble, ils indiquent que le **coût et l'échelle du procédé cellulaire** restent le facteur limitant, conformément au modèle de Humbird (EV-P-0039, EV-P-0065). Les déclarations de fondateurs (« la science n'était pas prête », EV-P-0045) restent des opinions.

**Résultats négatifs publiés.** La recherche active de publications primaires sur la perte de capacité myogénique des cellules de poulet au fil des passages n'a renvoyé que des revues (journal). Deux revues de 2026 documentent toutefois des risques non résolus :
- l'instabilité génomique observée chez des lignées spontanément immortalisées, dont des fibroblastes de poulet (EV-P-0063) ;
- l'absence de normes harmonisées pour qualifier les lignées et les banques de cellules (EV-P-0064).

---

## 5. RQ-P4 — Problèmes techniques sans solution satisfaisante

**Tableau 3 — Inventaire des problèmes non résolus (à intégrer à `knowledge_gaps.md`).**

| # | Problème | Pourquoi les solutions actuelles sont insuffisantes | Preuves |
|---|---|---|---|
| U1 | Coût des acides aminés de qualité culture cellulaire | 76 % du coût d'un milieu à grande échelle ; les hydrolysats manquent de Gln, Cys, Ser, Arg et sont coûteux à purifier ; presque aucun brevet sur ce poste | EV-P-0056, EV-P-0066, EV-P-0039, Q-P-0032 |
| U2 | Plafond de densité et inhibition métabolique (NH3, CO2, O2) | Limite physique ~86×10^6 cellules/mL et limite NH3 de 110 g/L dans le modèle, contre 108–130×10^6 cellules/mL déclarés pour le poulet (cellules plus petites ?), non reproduits indépendamment | EV-P-0040, EV-P-0041, EV-P-0042 |
| U3 | Montée en échelle des bioréacteurs | Aucun réacteur >2 000 L documenté pour un produit vendu ; projets de 100 000–250 000 L abandonnés ou suspendus | EV-P-0046, EV-P-0047 |
| U4 | Muscle vrai à partir de lignées immortalisées | Les lignées approuvées sont des fibroblastes (DF-1) ; la différenciation myogénique reste démontrée surtout sur cellules primaires (inhibiteur ERK) | EV-P-0005, EV-P-0017 |
| U5 | Épaisseur et structure (morceaux entiers) | Diffusion de l'O2 limitée à quelques centaines de µm ; fibres creuses : 0,3–0,5 mm par fibre ; filets en flacons | EV-P-0059, EV-P-0023, EV-P-0046 |
| U6 | Stabilité génomique et sûreté des lignées | Instabilité génomique des lignées spontanément immortalisées ; pas de normes alimentaires harmonisées | EV-P-0063, EV-P-0064 |
| U7 | Facteurs de croissance bon marché et acceptables | Petites molécules d'origine médicamenteuse (FK-506) ; expression autocrine au gain modeste ; variants thermostables testés sur cellules de souris | EV-P-0010, EV-P-0004, EV-P-0016 |
| U8 | Viabilité économique après autorisation | Believer fermé après les approbations FDA/USDA ; GOOD Meat à 3 % de cellules | EV-P-0043, EV-P-0048 |
| U9 | Stabilité des souches en fermentation continue (voie C, et B par analogie) | Résolu chez Quorn par une souche polyploïde ; non traité pour les cellules animales en continu | EV-P-0027, EV-P-0042 |
| U10 | Transfert gaz-liquide des SCP gazeuses | Airlifts : 20–40 % d'utilisation de l'O2 ; la conception des réacteurs en boucle reste propriétaire | EV-P-0032, Q-P-0051 |

---

## 6. Tableaux quantitatifs clés

**Tableau 4 — Viande cultivée : modèle et déclarations.**

| Grandeur | Valeur | Nature | ID |
|---|---|---|---|
| Coût de masse cellulaire humide, fed-batch | 37 USD/kg | model_output | Q-P-0001 |
| Idem, perfusion | 51 USD/kg | model_output | Q-P-0002 |
| Idem, fed-batch avec hydrolysats à 2 USD/kg | 22 USD/kg | model_output | Q-P-0003 |
| Densité maximale absolue (cellules de 17,7 µm) | 86×10^6 cellules/mL | model_assumption | Q-P-0004 |
| Densité limitée par NH3 (≤20 m³) | 110 g/L | model_output | Q-P-0005 |
| Fibroblastes de poulet, culture continue | 108×10^6 cellules/mL ; 36 % p/v | measured (résumé, auteurs = entreprise) | Q-P-0006, Q-P-0007 |
| Perfusion TFF, poulet | 130×10^6 cellules/mL ; 43 % p/v | measured (résumé) | Q-P-0008, Q-P-0009 |
| Milieu sans composant animal | 0,63 USD/L | company_claim | Q-P-0010 |
| Coût projeté (usine théorique de 50 000 L) | 6,2 USD/lb | model_output | Q-P-0011 |
| Milieu avec SVF / Beefy-9 (paillasse) | 290 / 217 USD/L | measured_reported_by_review | Q-P-0033, Q-P-0034 |
| Part des acides aminés dans le coût du milieu (grande échelle) | 76 % | model_output | Q-P-0032 |

**Tableau 5 — Échelles et chiffres industriels (déclaratifs).**

| Grandeur | Valeur | Nature | ID |
|---|---|---|---|
| Teneur en cellules, GOOD Meat 3 (détail) | 3 % | company_claim | Q-P-0020 |
| Teneur antérieure (restauration) | ~70 % | company_claim (1 média) | Q-P-0021 |
| Prix GOOD Meat 3 | 7,20 SGD / 120 g (≈60 SGD/kg) | statistical | Q-P-0022 |
| Bioréacteurs prévus (ABEC) | 250 000 L | company_claim | Q-P-0018 |
| Bioréacteurs utilisés (hybrides UPSIDE) | 2 000 L | company_claim | Q-P-0025 |
| Capacité de conception, usine Believer | 12 000 t/an | company_claim | Q-P-0012 |
| Capacité annoncée d'EPIC (UPSIDE) | 50 000 lb/an (≈22,7 t) | company_claim | Q-P-0023 |
| Financements levés : Believer / Meatable / SCiFi / New Age | >390 / ~139 / ~40 / ~32 M USD | statistical | Q-P-0014, Q-P-0026, Q-P-0015, Q-P-0017 |

**Tableau 6 — Biomasses revendiquées (voie C) et effets revendiqués (voie A), données de déposants.**

| Système | Valeur | ID |
|---|---|---|
| Tapis fongiques MK7 | jusqu'à 180 g/L (base non précisée) | Q-P-0047 |
| Neurospora submergé | 41 g/L de matière sèche | Q-P-0048 |
| Mycoprotéine en continu avec recyclage | 18 g/L de matière sèche | Q-P-0049 |
| Xanthobacter sur H2/CO2 | µ = 0,04–0,12 h⁻¹ | Q-P-0050 |
| FeedKind chez le poulet de chair (essai publié) | jusqu'à 12,5 % du régime sans perte de croissance | Q-P-0038 |
| Alimentation in ovo | +3–8 % de poids à l'éclosion | Q-P-0052 |
| Acide guanidinoacétique | 0,92 g/kg → +7 % de poids final | Q-P-0053 |

---

## 7. Ce qui fonctionne / ce qui échoue / ce qui reste à inventer

**Fonctionne (démontré ou autorisé, à petite échelle).**
- Lignées aviaires spontanément immortalisées en suspension sans sérum, issues du savoir-faire vaccinal (EV-P-0005, EV-P-0008, EV-P-0057).
- Produits hybrides à faible teneur cellulaire, effectivement vendus (EV-P-0048).
- Mycoprotéine industrielle stabilisée par la génétique de la souche (EV-P-0027).
- SCP méthanotrophe en aliment pour poulet jusqu'à 12,5 % (EV-P-0060, essai contrôlé).

**Échoue ou stagne.**
- Usines dédiées de grande capacité : Believer arrêté, Glenview suspendue, bioréacteurs ABEC abandonnés (EV-P-0043, EV-P-0046, EV-P-0047).
- Produits structurés au-delà de l'échelle du flacon (EV-P-0046).
- Modèles d'affaires des start-up de mycélium et de SCP fourragère à fort CAPEX (EV-P-0050 à EV-P-0052).

**Reste à inventer.**
- Une source d'acides aminés de qualité culture à bas coût (U1).
- La différenciation musculaire de lignées immortalisées en suspension (U4).
- Une structuration épaisse sans vascularisation (U5).
- Un contrôle qualité génomique adapté à la production continue (U6, U9).
- Un modèle économique où la fraction cellulaire apporte une valeur mesurable (piste 6).

---

## 8. Contradictions

1. **Densité maximale.** Humbird : 86×10^6 cellules/mL et 258 g/L comme plafond absolu (EV-P-0040). Future Meat : 108–130×10^6 cellules/mL et 36–43 % p/v pour le poulet (EV-P-0041, EV-P-0042). Explications possibles : cellules de poulet plus petites que l'hypothèse de 17,7 µm (Humbird note lui-même que des cellules plus petites permettent davantage), définition différente du « % p/v », ou culot cellulaire compacté. **Non tranché** : les articles de Future Meat n'ont été lus qu'en résumé.
2. **Économie.** Humbird : 37–51 USD/kg de masse cellulaire, « exclurait » l'accessibilité (EV-P-0039, EV-P-0065). Pasitka 2024 : 6,2 USD/lb dans une usine théorique en perfusion (EV-P-0042). La société auteure de cette projection optimiste a cessé ses activités 16 mois plus tard (EV-P-0043). C'est une tension, pas une réfutation : la fermeture est financière et documentée comme telle.
3. **Sûreté des lignées spontanées.** Future Meat affirme la stabilité génétique de ses lignées (EV-P-0041). Une revue de 2026 rapporte une instabilité génomique chez des fibroblastes de poulet spontanément immortalisés (EV-P-0063).
4. **Statut juridique.** Pour CN113684177A, Google Patents affiche « Pending » mais aussi un événement de rejet en 2024 (EV-P-0020). Pour JP2023047559A, « Pending » coexiste avec une décision de rejet en 2026 (EV-P-0019). Seuls les registres officiels peuvent trancher.
5. **Attributions erronées des résumés WebSearch** (corrigées sur les pages) : US11432574B2 appartient à Better Meat Co, pas à Emergy ; US10669524B2 appartient à Fork & Goode, pas à Integriculture ; US20160227831A1 n'a pas été vérifié et a été exclu de l'échantillon.

---

## 9. Lacunes

- Pas de comptage de familles reproductible (Espacenet/PATENTSCOPE/Lens bloqués) ; pas de données CNIPA, KIPRIS ou J-PlatPat directes ; aucun brevet de Joes Future Food, Jiangnan ou Zhejiang lu.
- Revendications non lues pour 38 des 44 brevets.
- Pasitka 2023/2024 (Nature Food) et les deux analyses de brevets de 2026 non lus en texte intégral.
- Aucun brevet de modification génétique du muscle du poulet (myostatine) trouvé : résultat négatif à confirmer (voir journal).
- Aucun brevet chinois, japonais ou coréen sur l'approvisionnement en acides aminés pour milieux de culture trouvé (non recherché spécifiquement : à faire).
- Causes techniques internes des échecs non publiques ; date et type de liquidation de Deep Branch non lus.
- Statut 2026 non vérifié pour SuperMeat, Aleph Farms, Mosa Meat, Vital Meat, Fork & Goode et Kiverdi.

---

## 10. RQ-P5 / RQ-X5 — Pistes de recherche

Chaque piste répond aux dix questions du brief. Classement : **[A] amélioration réalisable**, **[I] innovation à développer**, **[S] hypothèse spéculative**. Les coûts sont des **ordres de grandeur estimés par P** (en mois-personne et en équipement), non sourcés.

### Piste 1 [A] — Qualifier les lignées aviaires d'origine vaccinale pour l'alimentation

1. **Problème** : pas de lignées de poulet ouvertes, caractérisées et à la fois proliférantes et myogéniques (U4, U6).
2. **Solutions actuelles** : DF-1 (GOOD Meat), EBx (Valneva/Vital Meat), CEF immortalisés (Intervet), lignées propriétaires de Future Meat (EV-P-0005, EV-P-0008, EV-P-0007).
3. **Insuffisances** : fibroblastes peu myogéniques ; instabilité génomique possible (EV-P-0063) ; données de banque peu publiées (EV-P-0064).
4. **Preuves d'une nouvelle approche** : précédent réglementaire pour les lignées spontanées et cisgéniques (EV-P-0057) ; lignées commerciales déjà adaptées à la suspension sans sérum (EV-P-0062).
5. **Technologies à combiner** : banques de cellules de type pharmaceutique, caryotype/CNV/séquençage complet, criblage de milieux alimentaires.
6. **Hypothèse** : au moins une lignée vaccinale aviaire existante conserve un caryotype stable sur 50 doublements dans un milieu de qualité alimentaire, avec un temps de doublement inférieur à 24 h.
7. **Expérience** : 3 à 4 lignées accessibles × 2 milieux, 50 doublements ; séquençage complet aux doublements 0, 25 et 50 ; mesure du temps de doublement, de la densité maximale en flacon agité et de la composition (protéines, lipides).
8. **Coûts/difficultés** : environ 12 mois-personne, séquençage, licences et conditions d'usage des lignées (accords de transfert de matériel ATCC/Valneva à vérifier).
9. **Succès/échec** : succès = au moins une lignée stable (aucune variation de nombre de copies majeure) et doublement <24 h ; échec = dérive génomique systématique.
10. **Étape suivante** : test de différenciation (piste 2) sur les lignées retenues.

### Piste 2 [I] — Différencier en muscle des lignées immortalisées par petites molécules, en suspension

1. **Problème** : la biomasse vendue est fibroblastique ; le muscle structuré reste à petite échelle (U4).
2. **Solutions actuelles** : différenciation de myoblastes primaires ; inhibiteur ERK (indice de fusion 62 % contre 15 %, Q-P-0042) ; activateurs de FGF (EV-P-0010).
3. **Insuffisances** : données obtenues sur cellules primaires adhérentes, sans test sur lignées immortalisées ni en suspension.
4. **Preuves** : EV-P-0017 ; agrégats en suspension déjà maîtrisés pour les lignées aviaires (EV-P-0008).
5. **Technologies** : inhibiteurs ERK1/2, agents élevant le Ca²⁺ intracellulaire, agrégats ou microporteurs comestibles (EV-P-0020).
6. **Hypothèse** : un inhibiteur ERK induit l'expression de MyHC dans une fraction notable (≥20 %) de cellules issues de lignées aviaires immortalisées à potentiel myogénique résiduel.
7. **Expérience** : courbe dose-réponse sur 3 lignées (en plaque puis en agrégats), mesure de MyHC/MyoG par immunofluorescence et qPCR, protéines myofibrillaires, analyse du profil de texture après cuisson.
8. **Coûts** : 6 à 9 mois-personne ; résidus de petites molécules à évaluer sur le plan réglementaire.
9. **Succès** : ≥20 % de noyaux MyHC+ et augmentation des protéines myofibrillaires ; échec : <5 %.
10. **Étape suivante** : combiner avec la piste 5 (milieu) puis tester sensoriellement en hybride (piste 6).

### Piste 3 [I] — Milieux à base d'hydrolysats de SCP, complétés en acides aminés limitants (pont A+B+C)

1. **Problème** : les acides aminés pèsent ~76 % du coût du milieu à grande échelle (U1).
2. **Solutions actuelles** : acides aminés purifiés ; hydrolysats végétaux ou de levure (EV-P-0056) ; homologues végétaux des protéines sériques (EV-P-0009).
3. **Insuffisances** : déficits en Gln, Cys, Ser et Arg ; purification coûteuse (EV-P-0066) ; selon Humbird, condition « nécessaire mais insuffisante » (EV-P-0065).
4. **Preuves** : des SCP (méthanotrophes, hydrogénotrophes) sont produites industriellement et déjà validées comme aliment pour poulet jusqu'à 12,5 % (EV-P-0060) ; le scénario hydrolysat à 2 USD/kg ramène le coût modélisé de 37 à 22 USD/kg (Q-P-0003).
5. **Technologies** : hydrolyse enzymatique de SCP, ultrafiltration et retrait des endotoxines, complémentation ciblée en acides aminés limitants, cellules modifiées par glutamine synthétase (EV-P-0003).
6. **Hypothèse** : un hydrolysat de SCP, purifié et complété en 4 acides aminés, remplace au moins 75 % des acides aminés d'un DMEM/F12 sans réduire de plus de 20 % la croissance des fibroblastes de poulet sur 10 passages.
7. **Expérience** : plan factoriel (taux de remplacement 0/25/50/75/100 % × avec/sans complémentation), dosage des endotoxines, croissance, viabilité, métabolites, puis TEA du milieu.
8. **Coûts** : 6 à 12 mois-personne ; accès à une SCP de qualité alimentaire ; endotoxines (bactéries Gram négatives).
9. **Succès** : critère de l'hypothèse atteint + coût calculé du milieu < coût de référence ; échec : toxicité ou endotoxines non éliminables.
10. **Étape suivante** : partager la même matière première entre aliment pour volaille et milieu de culture (approvisionnement commun, RQ-X3).

### Piste 4 [A] — Valoriser le plasma d'abattoir de poulet comme supplément de milieu (pont A+B)

1. **Problème** : le sérum de veau fœtal est coûteux et éthiquement contesté ; les remplaçants recombinants restent chers (U7).
2. **Solutions actuelles** : sérum d'abattage bovin, porcin ou de poulet décoloré au kaolin (EV-P-0015) ; gel de plasma bovin (EV-P-0019) ; milieux recombinants (EV-P-0011).
3. **Insuffisances** : intrant animal variable ; pas de données sur cellules de poulet avec sérum de poulet ; brevet rejeté au Japon (EV-P-0019).
4. **Preuves** : sérum porcin à 30 % ≈1,4× l'effet du SVF sur cellules porcines (EV-P-0015) ; le sang est déjà collecté en abattoir de volailles (voie A).
5. **Technologies** : fractionnement du plasma (albumine, transferrine), inactivation thermique et virale, contrôle de lot.
6. **Hypothèse** : un plasma de poulet d'abattoir traité permet de réduire de ≥50 % l'apport en SVF ou en facteurs recombinants pour des cellules de poulet, à coût et variabilité acceptables.
7. **Expérience** : 5 lots de plasma de poulet × 3 traitements, sur cellules de poulet primaires et DF-1, sur 10 passages ; coefficient de variation entre lots.
8. **Coûts** : 4 à 6 mois-personne ; biosécurité (agents adventices aviaires) et statut réglementaire d'un « sous-produit animal ».
9. **Succès** : croissance ≥80 % du témoin et variabilité entre lots <15 % ; échec : variabilité ou contamination rédhibitoire.
10. **Étape suivante** : à utiliser comme solution de transition pour des produits hybrides positionnés sans exigence « sans animal ».

### Piste 5 [I] — Lignées cisgéniques autocrines de poulet (FGF2/IGF1 thermostables) sans facteurs exogènes

1. **Problème** : les facteurs de croissance restent un coût et une contrainte de chaîne d'approvisionnement (U7).
2. **Solutions actuelles** : lignées UPSIDE sécrétant du FGF2 (gain ×1,42, EV-P-0004) ; FGF-2 thermostable (EV-P-0016) ; petites molécules (EV-P-0010).
3. **Insuffisances** : gain modeste ; variants non testés sur poulet ; perception « OGM » (EV-P-0058).
4. **Preuves** : précédent FDA pour une immortalisation cisgénique par TERT (EV-P-0057) ; signal de sécrétion IL2 de poulet fonctionnel (EV-P-0004).
5. **Technologies** : édition ciblée (insertion en « locus sûr »), variants thermostables d'origine aviaire, promoteurs inductibles.
6. **Hypothèse** : l'expression autocrine d'un FGF2 aviaire thermostabilisé, combinée à IGF1, rend une lignée de poulet indépendante des facteurs exogènes avec une croissance ≥80 % du témoin supplémenté.
7. **Expérience** : 4 constructions × 2 lignées ; 30 doublements sans facteurs ; mesure de la croissance, du FGF2 sécrété (ELISA), du caryotype et de tests de transformation (croissance en agar mou).
8. **Coûts** : 12 mois-personne ; propriété intellectuelle (famille UPSIDE, EV-P-0004) et réglementation UE/Chine.
9. **Succès** : ≥80 % de croissance sans facteurs, sans signal de transformation ; échec : gain <1,5× ou instabilité.
10. **Étape suivante** : analyse de liberté d'exploitation face aux revendications UPSIDE, puis dossier réglementaire comparé US/SG/UE.

### Piste 6 [A] — Dose-réponse sensorielle de la fraction cellulaire dans les hybrides de poulet

1. **Problème** : on ne sait pas quelle fraction minimale de cellules justifie le surcoût (U8) ; le marché vend 3 % de cellules (EV-P-0048).
2. **Solutions actuelles** : hybrides à 0,5–18 % (SuperMeat, EV-P-0025), 3 % (GOOD Meat), ~10 % (SCiFi, EV-P-0044), bandes de poulet à adipocytes cultivés (EV-P-0041).
3. **Insuffisances** : aucune courbe dose-réponse sensorielle publique trouvée ; restrictions possibles de liberté d'exploitation par les revendications hybrides (EV-P-0025).
4. **Preuves** : l'extrusion humide type poulet est dans le domaine public (EV-P-0038) ; les auteurs de Future Meat attribuent l'arôme à la graisse cultivée (EV-P-0041, résumé).
5. **Technologies** : extrusion humide, biomasse ou graisse de poulet cultivée, analyse sensorielle (tests triangulaires, profils descriptifs), chromatographie gazeuse et olfactométrie.
6. **Hypothèse** : en dessous d'environ 5 % de biomasse cellulaire, la différence n'est pas perçue face à un témoin végétal aromatisé ; la graisse cultivée apporte un effet détectable à plus faible dose que la biomasse fibroblastique.
7. **Expérience** : matrice extrudée × {0, 1, 3, 5, 10, 20 %} × {biomasse, graisse} ; tests triangulaires (n ≥ 60), profils aromatiques, profil de texture.
8. **Coûts** : 3 à 6 mois-personne ; disponibilité de biomasse de poulet cultivée (quelques kg).
9. **Succès** : identification d'un seuil de détection et d'une dose à valeur ajoutée ; échec : aucune différence jusqu'à 20 % (ce qui remettrait en cause l'intérêt de l'hybride).
10. **Étape suivante** : coupler à une TEA du coût par point de préférence.

### Piste 7 [S] — Dérive clonale en culture continue de cellules aviaires : appliquer la leçon de Quorn

1. **Problème** : la perfusion continue (>20 jours, EV-P-0042) peut sélectionner des variants (U6, U9).
2. **Solutions actuelles** : banques de cellules ; contrôle ponctuel du caryotype (EV-P-0064).
3. **Insuffisances** : aucune donnée publique de suivi génomique en continu prolongé chez le poulet.
4. **Preuves** : chez Quorn, les variants morphologiques limitaient la durée des campagnes, résolu par une souche polyploïde (EV-P-0027) ; instabilité génomique des lignées spontanées (EV-P-0063).
5. **Technologies** : séquençage longitudinal des populations, cytométrie, suivi des sous-clones par code-barres génétiques, redémarrage programmé depuis une banque de cellules.
6. **Hypothèse** : en perfusion de plus de 30 jours, des sous-clones à croissance accélérée et à phénotype altéré dominent, fixant une durée de campagne optimale économiquement.
7. **Expérience** : 3 cultures continues de 60 jours (petite échelle, TFF) ; séquençage et caryotype tous les 10 jours ; croissance et composition.
8. **Coûts** : 6 mois-personne ; bioréacteurs de perfusion de laboratoire.
9. **Succès** (de l'hypothèse) : dérive détectée et quantifiée → règle de durée de campagne ; échec : stabilité sur 60 jours (résultat également utile).
10. **Étape suivante** : intégrer la durée de campagne dans les TEA de perfusion (contradiction 2).

### Piste 8 [I] — Structuration par fibres creuses comestibles espacées de moins de 1 mm

1. **Problème** : la diffusion de l'O2 limite l'épaisseur à quelques centaines de µm (U5).
2. **Solutions actuelles** : fibres creuses comestibles (0,3–0,5 mm de tissu par fibre, EV-P-0023) ; fibres microfluidiques (EV-P-0022) ; soja texturé (EV-P-0018).
3. **Insuffisances** : aucune épaisseur centimétrique documentée dans les brevets lus ; filets encore en flacons (EV-P-0046).
4. **Preuves** : cohérence entre la limite physique (EV-P-0059) et la conception des fibres (EV-P-0023).
5. **Technologies** : membranes comestibles poreuses (alginate, protéines réticulées), réseaux de fibres imprimés en 3D, perfusion interne.
6. **Hypothèse** : un réseau de fibres comestibles espacées de ≤0,8 mm permet un tissu de poulet de ≥1 cm d'épaisseur sans nécrose centrale après 14 jours.
7. **Expérience** : cartouches de 1 cm³ à 3 espacements (0,6/0,8/1,2 mm) ; mesure de l'O2 interne, coloration vivant/mort, MyHC, profil de texture.
8. **Coûts** : 9 à 12 mois-personne ; propriété intellectuelle de Merck (PCT éteint, phases nationales à vérifier).
9. **Succès** : >80 % de viabilité au cœur à 0,8 mm ; échec : nécrose au-delà de 0,6 mm.
10. **Étape suivante** : coût par kg du matériau de fibre et intégration à un produit structuré.

### Piste 9 [A] — Produit hybride « sans licence » : audit de liberté d'exploitation du domaine public

1. **Problème** : le paysage de brevets peut bloquer de nouveaux entrants, mais une partie du socle a expiré (EV-P-0061).
2. **Solutions actuelles** : licences et rachats d'actifs de faillites (brevets de Mycorena présentés comme actifs, EV-P-0050).
3. **Insuffisances** : aucune carte de liberté d'exploitation publique ; statuts Google non fiables (contradiction 4).
4. **Preuves** : brevets expirés (van Eelen, extrusion Mars, in ovo, phytase) ; nombreux PCT éteints ; lignée DF-1 commercialement disponible (EV-P-0005).
5. **Technologies** : analyse de liberté d'exploitation par conseil en propriété industrielle, registres officiels (EPO, USPTO, CNIPA).
6. **Hypothèse** : un hybride de poulet (extrusion humide + biomasse aviaire en suspension sans sérum à faible teneur) peut être produit sans licence de brevet en vigueur dans l'UE, sous réserve des conditions d'usage des lignées.
7. **Expérience** : audit documentaire sur 3 juridictions (UE, US, SG) couvrant les familles UPSIDE, SuperMeat, GOOD Meat, Believer/Yissum et Impossible.
8. **Coûts** : 1 à 2 mois-personne de conseil ; pas de laboratoire.
9. **Succès** : chaîne de procédé sans revendication bloquante identifiée ; échec : revendications hybrides ou de lignées en vigueur incontournables.
10. **Étape suivante** : prototype de la piste 6 sur cette base.

### Piste 10 [S] — Alimentation in ovo de précurseurs de créatine pour augmenter l'hyperplasie musculaire (voie A)

1. **Problème** : le nombre de fibres musculaires est fixé avant l'éclosion ; les gains post-éclosion se heurtent aux myopathies (domaine de l'agent N).
2. **Solutions actuelles** : alimentation in ovo de nutriments (+3–8 % de poids, EV-P-0033) ; acide guanidinoacétique dans l'aliment (+7 %, EV-P-0034).
3. **Insuffisances** : effets revendiqués par les déposants, variables ; combinaison in ovo + précurseur de créatine non trouvée dans l'échantillon.
4. **Preuves** : les deux brevets sont expirés, donc les technologies sont libres ; l'injection amniotique est une technique maîtrisée (EV-P-0033).
5. **Technologies** : injection automatisée d'œufs, acide guanidinoacétique ou créatine, histomorphométrie des fibres.
6. **Hypothèse** : une injection amniotique d'acide guanidinoacétique en fin d'incubation augmente le nombre de fibres du pectoral à l'éclosion et le rendement en filet à 35 jours, sans hausse du « woody breast ».
7. **Expérience** : 4 doses × 300 œufs ; éclosabilité ; nombre et aire des fibres à J0 ; rendement en filet et score de myopathie à J35.
8. **Coûts** : 6 mois-personne ; station expérimentale avicole.
9. **Succès** : +5 % de fibres et +2 points de rendement en filet sans perte d'éclosabilité ; échec : baisse de l'éclosabilité ou aucun effet.
10. **Étape suivante** : vérification par l'agent N de la littérature existante sur l'injection in ovo de créatine ou d'acide guanidinoacétique avant tout essai.

**Synthèse RQ-X5 (espaces les moins explorés).**
- L'approvisionnement en acides aminés et la mutualisation des matières premières entre aliment avicole, SCP et milieux (piste 3).
- La différenciation musculaire des lignées vaccinales (pistes 1 et 2).
- Le suivi génomique en culture continue (piste 7).
- La dose-réponse sensorielle des hybrides (piste 6).

Les pistes 4, 6 et 9 sont les tests **les plus rapides et les moins coûteux** (de quelques semaines à 6 mois, sans bioréacteur).

---

## 11. Recherches restantes (priorisées)

1. Lire Pasitka 2023/2024 en texte intégral (accès institutionnel) pour trancher la contradiction sur la densité (base du « % p/v »).
2. Obtenir les revendications des 38 brevets lus par WebFetch (reprendre `curl` sur Google Patents quand le blocage cessera, ou utiliser l'API EPO OPS avec une clé).
3. Comptage de familles reproductible (Lens.org avec clé API ou PATENTSCOPE) : viande cultivée de poulet, milieux, acides aminés pour culture cellulaire, SCP pour l'alimentation animale.
4. Brevets CNIPA de Jiangnan, Zhejiang et Joes Future Food ; brevets KIPO de Yonsei et CJ ; brevets JPO d'IntegriCulture (SRC-C-0026 côté agent C).
5. Statuts 2026 de SuperMeat, Aleph, Mosa, Vital Meat, Fork & Goode et Kiverdi ; causes de la liquidation de Deep Branch (onglet « Insolvency » de Companies House) ; lecture directe du communiqué Agronomics sur Meatable.
