# Substituts du muscle de poulet et nouvelles sources de protéines (voie C)

*Agent A — Chicken Muscle Research Lab — brouillon de phase 3–4, 2026-10-25.*
*Toutes les affirmations renvoient aux tables `research/agents/A/{sources,evidence,quant}.csv` (identifiants `SRC-A-…`, `EV-A-…`, `Q-A-…`). Les identifiants d'autres agents (`EV-N-…`, `EV-E-…`, `EV-C-…`) sont cités quand ils complètent l'analyse.*

---

## 1. Périmètre et méthode

**Question générale.** Quelles technologies produisent un aliment qui ressemble au poulet sans (ou avec peu de) cellules musculaires animales, et lesquelles peuvent (1) remplacer directement la viande de poulet, (2) remplacer une partie de l'aliment volaille, (3) alimenter la viande cultivée (voie B) ?

**Bases et outils réellement utilisés.** Europe PMC (dont texte intégral libre), PubMed, Crossref (requêtes directes, l'outil interne étant en erreur), HAL et theses.fr, J-STAGE, Consensus (2 requêtes), WebSearch/WebFetch (presse spécialisée, sites d'entreprises, Google Patents, KoreaScience, Soyinfo Center, Science and Technology Daily), téléchargement direct de la base officielle USDA FoodData Central SR Legacy. Le journal complet (116 requêtes distinctes en 7 langues : en, fr, zh, es, ja, ko, id) est dans `research/agents/A/search_log.md` ; la terminologie multilingue (44 entrées) dans `terminology.md`.

**Bilan d'enregistrement.** 46 sources : 11 articles ou revues scientifiques lus en texte intégral et 4 documents lus par sections (avis EFSA, revue de Leber, ouvrage de Shurtleff, article coréen), plus 9 documents non académiques lus en entier (base USDA, brevet, communiqués, presse, communication de congrès) ; 22 sources lues au niveau du résumé. 51 affirmations, 67 mesures.

**Règles de lecture appliquées.**
- Base de calcul toujours précisée : protéine brute (N × 6,25) vs protéine « vraie » (facteurs spécifiques) vs protéine digestible (DIAAS) ; poids humide (produit) vs matière sèche.
- Nature des chiffres : mesure, estimation publiée, sortie de modèle, annonce d'entreprise.
- Référence « poulet » : filet de poulet cuit rôti sans peau, USDA SR Legacy fdc_id 171477 (SRC-A-0004). La table française CIQUAL n'a pas pu être téléchargée (erreur 503).

**Limites d'accès.** Articles Elsevier/Springer/RSC le plus souvent lus au niveau du résumé (Schreuders 2019, Krintiras 2016, Smetana 2015, Shahid 2024, Novak 2025…). Rapports NECTAR et GFI non consultés directement (presse spécialisée seulement). Pages ACNFP (Royaume-Uni) et texte officiel de la NHC chinoise inaccessibles. PDF japonais sur le yuba sous forme d'image (pas d'OCR). Couverture hispanophone d'Europe PMC quasi nulle pour ce thème.

---

## 2. État des connaissances par question

### RQ-A1 — Analogues végétaux du poulet : matières, procédés, propriétés

**Matières.** Les analogues commerciaux de morceaux de poulet vendus aux Pays-Bas reposent sur la protéine de soja texturée, le pois (concentré texturé) ou des mélanges soja-blé ; ils affichent 19–23 g de protéines/100 g, mais 1,1–1,9 g de sel/100 g contre 0,1 g pour le filet cru (SRC-A-0001 ; Q-A-0008, Q-A-0009, Q-A-0010). En Corée, l'isolat de soja domine ; sa forte stabilité thermique (renforcée par le sel) rend impossible la structuration aux températures de la charcuterie (75–90 °C) et impose l'extrusion à 130–160 °C (EV-A-0034).

**Procédés et ce qu'ils obtiennent.**
- *Extrusion à haute humidité (HME).* C'est le procédé industriel dominant. Il reproduit correctement les propriétés globales de compression (TPA), mais la structure obtenue est feuilletée : les feuillets de HMMA de soja ont un indice d'anisotropie mécanique à longue distance (LMA) moyen de 0,20, significativement inférieur à celui des viandes cuites ; ils se déchirent par décollement de couches et se déforment de façon isotrope, alors que le filet de poulet se sépare en faisceaux millimétriques (EV-A-0002 ; Q-A-0011). Une revue chinoise récente arrive au même diagnostic : fibres « trop faibles et sans hiérarchie » (EV-A-0031).
- *Post-traitement.* Une micro-impression perforante de feuillets de 1 mm, recollés à la transglutaminase, multiplie jusqu'à 5 fois la séparation fibreuse anisotrope et améliore la perception de fibrosité face au filet de poulet. Le panel était toutefois très petit (n = 15) et la démonstration n'a été faite qu'au banc (EV-A-0003 ; Q-A-0012).
- *Cellule de cisaillement (Couette, Wageningen).* À 110–120 °C, les mélanges pois–gluten atteignent la résistance à la traction d'une référence de poulet (50–100 kPa) ; les mélanges soja–gluten sont plus résistants (220–300 kPa) (EV-A-0015 ; Q-A-0028). Une cellule de 7 L produit des pièces fibreuses de 30 mm d'épaisseur ; selon les auteurs, aucune barrière à la montée en échelle n'apparaît, ce qui reste une opinion (EV-A-0016 ; Q-A-0029).
- *Rhéologie fine.* À petite déformation, des analogues commerciaux de poulet tombent dans la même zone que le poulet cuit. Ils sont en revanche moins élastiques, présentent moins de durcissement sous déformation, et la cuisson ne change presque rien à leur texture, contrairement à la viande qui durcit et devient plus élastique (EV-A-0001).

**Sensoriel et marché.** Dans le test hédonique NECTAR 2025 (122 produits), 30 % des participants aiment le produit végétal moyen contre 68 % pour la viande. Les filets et nuggets de poulet font partie des catégories les plus proches de la parité, et la texture reste le premier axe d'amélioration (EV-A-0026 ; Q-A-0040, source secondaire). Au Pérou, le nugget vegan commercial est le moins apprécié (sec, peu juteux) face au nugget de poulet (EV-A-0047). Aux États-Unis, les ventes au détail de viandes végétales ont baissé de 7 % en valeur et de 11 % en volume en 2024, après −12 %/−19 % en 2023. Sur la même période, la viande conventionnelle progressait (EV-A-0025 ; Q-A-0037–Q-A-0039).

### RQ-A2 — Protéines fongiques et microbiennes

**Mycoprotéine (Fusarium venenatum).** C'est la seule biomasse microbienne alimentaire produite en masse depuis des décennies. Le procédé est continu, dans deux fermenteurs airlift « pressure-cycle » de 150 000 L, pour environ 300 kg de biomasse/h. Les campagnes durent environ 1 000 h et sont limitées par l'apparition de mutants très ramifiés (EV-A-0040 ; Q-A-0049–Q-A-0051 ; la base humide ou sèche du débit n'est pas précisée). L'ARN est réduit par traitement thermique. L'ingrédient contient environ 45 % de protéines et 25 % de fibres sur matière sèche, soit environ 11 g de protéines/100 g en poids humide (données de l'entreprise, EV-A-0006 ; Q-A-0019, Q-A-0020).
- *Nutrition humaine.* Avec un apport protéique élevé, un régime vegan riche en mycoprotéine soutient une synthèse protéique myofibrillaire équivalente à un régime omnivore chez des personnes âgées (EV-A-0008). Il produit aussi des gains de masse maigre comparables sur 10 semaines d'entraînement (EV-A-0009 ; Q-A-0022). Ces essais sont petits et liés à l'industriel.
- *Sécurité.* Les réactions allergiques déclarées sont rares (≈1 cas possiblement IgE-médié pour 24 millions de portions selon l'entreprise), mais un recueil indépendant (CSPI) compte autant de signalements britanniques (EV-A-0007 ; Q-A-0021).
- *Nouvelles capacités.* La Chine a autorisé fin 2025 la protéine de F. venenatum comme « nouvel ingrédient alimentaire » ; une ligne de 20 000 t/an est annoncée (EV-A-0048 ; Q-A-0063, annonce non vérifiée sur le texte officiel).
- *Échecs.* Meati (mycélium de Neurospora) a cédé ses actifs pour environ 4 M USD en 2025 après environ 450 M USD levés (EV-A-0041 ; Q-A-0052).

**Bactéries hydrogénotrophes (HOB).**
- *Composition.* La poudre Solein (Xanthobacter sp. SoF1) contient 73,1 % de protéines en N × 6,25, mais 68 % avec le facteur spécifique N × 5,83. C'est un exemple chiffré de l'écart entre protéine brute et protéine vraie. Elle contient aussi 1 240 mg/kg de fer, de biodisponibilité inconnue (EV-A-0020 ; Q-A-0030–Q-A-0032).
- *Statut réglementaire.* Solein est autorisée à Singapour (2022) et a obtenu un GRAS auto-affirmé aux États-Unis (2024) ; l'évaluation EFSA restait ouverte début 2025 (EV-A-0021).
- *Mesures pilotes.* Un réacteur gazeux pressurisé de 300 L atteint 90 g/L de biomasse sèche de Cupriavidus necator à 80 % de protéines brutes (EV-A-0051 ; Q-A-0065–Q-A-0067).
- *Modèle.* Une SCP alimentée par photovoltaïque pourrait fournir plus de 1 200 g de protéines/m²/an, soit environ 10 fois le soja (≈115 g/m²/an), ou 15 t de protéines/ha/an (EV-A-0013 ; Q-A-0023–Q-A-0026). Ce chiffre est une sortie de modèle : il n'intègre ni le coût, ni l'énergie de construction, ni les limites de transfert de H2.

**Repères économiques.** Rapporté au kilogramme de protéine sèche, le poulet coûtait environ 4,6 USD contre 1,1 USD pour le soja (données d'environ 2014–2016, EV-A-0042 ; Q-A-0053, Q-A-0054). Les teneurs en protéines brutes sont de 50–83 % de la matière sèche pour les bactéries, 30–70 % pour les champignons et 40–60 % pour les algues (Q-A-0055).

### RQ-A3 — Fermentation de précision

- *Hème.* La léghémoglobine de soja produite par Komagataella phaffii a reçu un avis EFSA favorable (provisoire, en attente de l'avis OGM). Elle est autorisée aux États-Unis comme colorant depuis 2019, au Canada et en Australie–Nouvelle-Zélande depuis 2020 (EV-A-0018 ; Q-A-0035, Q-A-0036). FSANZ l'a plafonnée à 0,8 % du produit cru par analogie avec la myoglobine de la viande rouge (0,8–1,8 %) (EV-A-0019 ; Q-A-0034). **Pour le poulet, l'hème n'est pas l'enjeu principal** : l'arôme du blanc de poulet dépend surtout des précurseurs soufrés et des phospholipides (RQ-A7).
- *Intrants pour la viande cultivée.* Les ingrédients de la voie C peuvent remplacer des composants coûteux des milieux. Des protéines hydrosolubles de soja, de pois ou de pois chiche à 0,1 mg/mL remplacent 2 mg/mL de BSA pour des fibroblastes de poulet à court terme (donnée de brevet, EV-A-0036 ; Q-A-0043). Méthylcellulose et amidon de maïs, à environ 0,054 USD/L, se comparent aux ~24,56 USD/L d'albumine recombinante. Un isolat de colza coûterait ~0,002 USD/L (estimations, cellules bovines, EV-A-0037 ; Q-A-0045, Q-A-0046). Le milieu pèse 50–90 % du coût matière de la viande cultivée (Q-A-0044). Ces chiffres complètent ceux de l'agent E : même avec un hydrolysat végétal à 2 USD/kg, le coût fed-batch du modèle de Humbird reste à ~22 USD/kg humide (EV-E-0002).

### RQ-A4 — Insectes, algues, lentilles d'eau, coproduits

- *Insectes dans l'aliment volaille.* Une méta-analyse de 15 essais ne trouve aucun effet global de la farine de larves de mouche soldat noire sur l'ingestion, le GMQ ou l'IC du poulet de chair (EV-A-0024). Un essai costaricien montre en revanche une dégradation à 10 % d'incorporation (EV-A-0032), ce qui contredit le taux de 28 % « recommandé » par la méta-analyse (Q-A-0041). Une revue multicritère classe les insectes derniers des alternatives pour l'alimentation humaine (EV-A-0027).
- *Protéines bactériennes dans l'aliment volaille.* La SCP de méthanotrophe (Methylococcus capsulatus) remplace le tourteau de soja jusqu'à 12,5 % chez le Ross 308 sans perte de croissance globale, à condition d'une phase d'adaptation (EV-A-0014 ; Q-A-0027). Le frein principal est économique : le tourteau de soja reste très bon marché (EV-A-0042).
- *Microalgues.* 25 g de protéines de spiruline ou de chlorelle stimulent la synthèse protéique musculaire humaine autant que 25 g de mycoprotéine (EV-A-0010).
- *Lentilles d'eau.* Jusqu'à 45 % de protéines sur matière sèche ; plantes fraîches de Wolffia autorisées dans l'UE depuis 2021 et concentré protéique de Lemna depuis 2024, avec une vigilance sur le manganèse (EV-A-0035 ; Q-A-0042). L'essai clinique original sur la biodisponibilité des protéines de Wolffia n'a pas été retrouvé (lacune).

### RQ-A5 — Traditions d'analogues

La Chine documente des analogues de viande depuis le Xe siècle : tofu en « côtelettes d'agneau » (965), recettes au gluten de blé (1301), yuba dans le *Bencao gangmu* (1596). Le premier analogue de volaille connu est une « oie rôtie » enveloppée de yuba (1790, *Suiyuan shidan*) ; le tempeh apparaît en 1815 (EV-A-0028). La cuisine bouddhiste fabrique le « Buddha's chicken » en pressant des feuilles de yuba fraîches dans des moules, puis en les cuisant à la vapeur (EV-A-0029). La structure est ainsi obtenue par **laminage de films protéino-lipidiques**, à basse température. Le su ji industriel (素鸡) reste un procédé à ≤99 °C (trempage alcalin, pressage, ficelage, vapeur), mais sa version artisanale est lente : environ 6 000 pièces de 100 g par équipe de 20 personnes en 8 h, selon un brevet chinois retiré (EV-A-0030). Le tempeh peut contenir peu de phytates (24 mg/100 g mesurés), mais sa vitamine B12 dépend des bactéries associées : un tempeh fait avec du Rhizopus pur n'en contient pas (EV-A-0005, EV-A-0033 ; Q-A-0007 : 0,08 µg/100 g).

Aucune étude instrumentale moderne n'a été trouvée sur des analogues de poulet en pièces entières fabriqués par laminage de yuba (recherche explicite, 1 seul résultat, une revue). Cette absence est une lacune et, potentiellement, une piste (§7).

### RQ-A6 — Produits hybrides

- *Seul produit de viande cultivée vendu au détail.* C'est un hybride : GOOD Meat 3 (Singapour, mai 2024) contient 3 % de poulet cultivé dans une matrice de protéines végétales, vendu 7,20 SGD les 120 g (≈60 SGD/kg). La faible part cellulaire est justifiée par le coût (EV-A-0039 ; Q-A-0048).
- *Hybride poulet–végétal en laboratoire.* Remplacer 20 % de filet par un isolat de soja + transglutaminase donne la meilleure texture parmi les isolats testés, avec 20,9 % de protéines brutes après cuisson. Le témoin à base d'émulsion de poulet n'en contient que 13,9 %, car la formulation ajoute de l'eau (EV-A-0038 ; Q-A-0047).
- *Côté voie B.* Des adipocytes de poulet cultivés, mélangés à des protéines de soja extrudées, ont reçu une note sensorielle de 4,5/5 (EV-C-0016, agent C).

### RQ-A7 — Écart nutritionnel et sensoriel avec le poulet

**Qualité protéique.**
- *Ingrédients.* Les DIAAS (profil de référence 0,5–3 ans, digestibilité mesurée chez le porc) sont de 91 pour le soja (limitant : Met+Cys), 70 pour le pois, 55 pour la féverole, 48 pour le blé et 47 pour le riz (lysine limitante). La viande de porc atteint 117 ; aucune valeur pour le poulet n'a été trouvée dans cette source (EV-A-0043 ; Q-A-0056–Q-A-0059).
- *Mélanges.* Ils réduisent l'écart (pois/riz : DIAAS maximal de 84) et la protéine de pomme de terre peut amener la plupart des mélanges à 100 (EV-A-0044 ; Q-A-0060).
- *Produits finis.* Chez le porc, le DIAAS des burgers animaux dépasse celui des burgers végétaux. Pour les plus de 3 ans, l'Impossible Burger (soja) rejoint le bœuf 80 % maigre (EV-A-0011). La digestibilité iléale vraie des burgers végétaux et des isolats dépasse 0,90, comme celle de la viande (EV-A-0012) : **l'écart tient surtout au profil en acides aminés, pas à la digestibilité.**
- *Profils comparés (USDA).* Le filet de poulet cuit apporte environ 85 mg de lysine et 40 mg de Met+Cys par gramme de protéine, contre environ 45 et 18 mg/g pour le tempeh (calculés à partir de Q-A-0006 et Q-A-0007).

**Micronutriments.**
- *Fer.* Le filet de poulet cuit n'apporte qu'environ 1 mg de fer, 1 mg de zinc et 0,34 µg de B12 pour 100 g (Q-A-0003–Q-A-0005). L'écart sur le fer porte donc moins sur la quantité que sur la forme et la biodisponibilité. Parmi 44 substituts suédois, les rapports phytate:fer vont de 2,5 à 45, et aucun produit ne passe sous le seuil de 1 ; aucun n'est une bonne source de fer biodisponible (EV-A-0004 ; Q-A-0013–Q-A-0015).
- *Zinc et sel.* La mycoprotéine apporte 6,7 mg de zinc/100 g mesurés, avec presque pas de phytates (EV-A-0005 ; Q-A-0016). Le sel médian des substituts est de 1,3 g/100 g, contre 74 mg de sodium/100 g pour le poulet cuit, soit environ 0,19 g de sel (Q-A-0018 ; Q-A-0005, notes).
- *Modèles français (INCA3).* Les substituts à base de soja améliorent légèrement le score PANDiet ; ceux à base de céréales le dégradent (moins de vitamines B et de minéraux) (EV-A-0045 ; Q-A-0061). L'enrichissement en fer et en zinc faciliterait la réduction de la viande (EV-A-0046).
- *Santé à long terme.* Les données sont contradictoires (§5).

**Arôme.** L'arôme carné du poulet dépend du 2-méthyl-3-furanthiol (réaction de Maillard entre ribose issu de l'IMP et cystéine, ou dégradation de la thiamine) et d'aldéhydes issus des phospholipides polyinsaturés, comme le (E,E)-2,4-décadiénal ; l'oxydation des lipides produit aussi le défaut de « réchauffé » (EV-A-0017). Aucune étude d'olfactométrie comparant un analogue végétal de poulet au poulet n'a été trouvée (lacune).

---

## 3. Tableaux quantitatifs

### 3.1 Substituts vs filet de poulet (pour 100 g de produit sauf mention)

| Produit | Protéines (base) | DIAAS / AA limitant | Lipides | Fer | Zinc | B12 | Sel/Na | Texture mesurée | Sources |
|---|---|---|---|---|---|---|---|---|---|
| **Filet de poulet cuit rôti** (référence) | 31,0 g (N×6,25, cuit) | pas de valeur poulet trouvée ; porc 117 (proxy) ; Lys 85 mg/g prot. | 3,6 g | 1,04 mg | 1,0 mg | 0,34 µg | Na 74 mg | traction 50–100 kPa (cru/réf.) ; LMA élevé | Q-A-0001–0006, Q-A-0028, Q-A-0059 |
| Filet de poulet cru (étiquette NL) | 23,6 g | — | 1,6 g | — | — | — | sel 0,1 g | durcit et gagne en élasticité à la cuisson | Q-A-0008, EV-A-0001 |
| Analogues commerciaux de poulet (NL, 5) | 19–23 g (étiquette) | non mesuré | 0,5–7,0 g | — | — | enrichis B12 pour certains | sel 1,1–1,9 g | moins élastiques, insensibles à la cuisson | Q-A-0009, Q-A-0010, EV-A-0001 |
| Substituts de viande (Suède, 44) | 5,5–23,8 g (N×5,4–5,85) | — | 2–22 g | 0,4–4,7 mg (phy:Fe 2,5–45) | 0,8–2,2 mg (hors mycoprotéine) | — | sel médian 1,3 g | — | Q-A-0013–0018 |
| HMMA soja (40 % SPC) | n.d. | soja ingrédient 91 (Met+Cys) | — | — | — | — | — | LMA 0,20 < viande ; TPA « proche » | Q-A-0011, Q-A-0056 |
| Pois–gluten (cellule de cisaillement) | n.d. | pois 70 (Met+Cys) ; blé 48 (Lys) | — | — | — | — | — | traction ≈ poulet à 110–120 °C | EV-A-0015, Q-A-0057, Q-A-0058 |
| Mycoprotéine (ingrédient) | 11 g (humide) ; 45 % MS (entreprise) | pas de DIAAS mesuré trouvé | 2,9 g | 0,5 mg | 9 mg (entreprise) ; 6,7 mg (produits mesurés) | 0 | Na 5 mg | « microstructure proche du filet » (affirmation) | Q-A-0016, Q-A-0019, Q-A-0020 |
| Tempeh (USDA) | 20,3 g | Lys 45 mg/g prot. | 10,8 g | 2,7 mg | 1,14 mg | 0,08 µg | Na 9 mg | — | Q-A-0007 |
| Solein (poudre) | 73,1 % (N×6,25) / 68 % (N×5,83) | non publié | 7,8 % | 124 mg (biodisponibilité inconnue) | — | — | — | — | Q-A-0030–0032 |
| C. necator (pilote) | 80 % prot. brute (MS) | — | — | — | — | — | — | — | Q-A-0066 |
| Hybride poulet + 20 % isolat de soja (cuit) | 20,9 % | — | 0,2 % | — | — | — | — | meilleure cohésion/cisaillement que riz/pois | Q-A-0047 |
| Nugget végétal optimisé (Pérou) | 12,0 % | — | 4,5 % | — | — | — | — | dureté 6,1 N | Q-A-0062 |

*Lecture.* Les colonnes « protéines » ne sont pas directement comparables : poids cuit vs cru vs poudre, et facteurs N différents. Seul le DIAAS, quand il existe, compare des protéines digestibles.

### 3.2 Procédés

| Procédé | Matière première | Rendement / productivité | Échelle atteinte | Coût / impact (nature) | Sources |
|---|---|---|---|---|---|
| Extrusion humide (HME) | concentrés/isolats soja, pois, gluten | **non trouvé** (kWh/kg, kg/h : lacune) | industrielle (produits commerciaux) | GES des extrudés 7,7–7,9 kg CO2e/kg (revue, agent E) | EV-A-0002, EV-E-0010 |
| Micro-impression post-HME | feuillets HMMA de 1 mm + TG | jusqu'à 5× de séparation fibreuse | banc (rouleau) | non évalué | EV-A-0003 |
| Cellule de Couette | SPI/PPI + gluten | 7 L par lot, 30 min à 120 °C | pilote | non évalué | EV-A-0016, Q-A-0029 |
| Su ji / yuba (traditionnel) | feuilles de tofu/yuba | ≈6 000 × 100 g / 20 personnes / 8 h (méthode manuelle) | artisanal → semi-industriel | ≤99 °C (faible énergie, non mesurée) | EV-A-0030, EV-A-0029 |
| Mycoprotéine (Quorn) | glucose (amidon) + NH3 | ≈300 kg biomasse/h dans 2 × 150 m³ ; campagnes ~1 000 h | industrielle | 0,73 kg CO2e/kg ingrédient (revue liée à l'industriel) vs « impact le plus élevé » (ACV 2015) | EV-A-0040, EV-A-0050, EV-A-0049 |
| Mycoprotéine (Chine) | n.d. | ligne pilote « kt » ; 20 000 t/an en construction | industrielle (annonce) | n.d. | EV-A-0048, Q-A-0063 |
| Bactéries H2 (PV-SCP) | H2 électrolytique + CO2 | modèle : 15 t protéines/ha/an ; efficacité soleil→aliment ≤0,4–0,8 % | modèle | non chiffré | EV-A-0013, Q-A-0025, Q-A-0026 |
| Bactéries H2 (pilote) | H2/O2/CO2 | 90 g/L MS ; 300 g/L humide en 35 h | pilote 300 L | n.d. | EV-A-0051 |
| Méthanotrophes | méthane | n.d. ici | industrielle (aliment animal) | concurrence du tourteau de soja (~1,1 USD/kg protéine) | EV-A-0014, EV-A-0042 |
| Larves de mouche soldat | coproduits | n.d. ici | industrielle (aliment animal) | n.d. | EV-A-0024, EV-A-0032 |
| Fermentation de précision (léghémoglobine) | glucose, levure GM | n.d. | industrielle | autorisée US/CA/ANZ ; UE provisoire | EV-A-0018 |

### 3.3 Matrice des rôles possibles

Légende : ✔ démontré (mesure ou produit commercialisé) · ◐ démontré partiellement ou en laboratoire · ○ hypothèse ou modèle · — non pertinent.

| Technologie | Alimentation humaine directe | Aliment volaille | Intrant pour la viande cultivée | Produit hybride |
|---|---|---|---|---|
| Protéines végétales texturées (HME, cisaillement) | ✔ (déclin des ventes US) | ✔ (tourteaux, base actuelle) | ◐ (protéines de pois/soja comme substitut d'albumine, EV-A-0036 ; supports) | ✔ (GOOD Meat 3 ; hybride 20 %, EV-A-0038) |
| Films de yuba / su ji | ✔ (traditionnel) | — | ○ (support laminé pour cellules) | ○ |
| Mycoprotéine | ✔ | ○ | ○ | ◐ |
| Bactéries H2 (Solein, C. necator) | ◐ (Singapour, GRAS US) | ○ (profil comparé à la farine de poisson) | ○ (hydrolysat ou source d'AA) | ○ |
| Méthanotrophes | — | ✔ (≤12,5 %, EV-A-0014) | ○ | — |
| Insectes (BSF) | ◐ (rejet consommateur) | ✔/◐ (résultats contradictoires) | ○ | ○ |
| Microalgues (spiruline, chlorelle) | ✔ (MyoPS, EV-A-0010) | ◐ (non approfondi) | ○ (hydrolysats : revues seulement) | — |
| Lentilles d'eau | ✔ (UE 2021/2024) | ○ | ○ | — |
| Fermentation de précision (hème, protéines) | ✔ (hème, viande rouge) | — | ◐ (facteurs de croissance recombinants : voie B) | ○ |
| Stabilisants végétaux (méthylcellulose, amidon, isolat de colza) | ✔ (additifs) | — | ◐ (estimations de coût, cellules bovines, EV-A-0037) | — |

---

## 4. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Ce qui fonctionne.**
- *Produits transformés.* Les nuggets et filets panés végétaux approchent la parité sensorielle (EV-A-0026). La HME et la cellule de cisaillement reproduisent la résistance globale du poulet (EV-A-0015, EV-A-0001).
- *Mycoprotéine.* Elle est produite en continu à l'échelle industrielle depuis des décennies (EV-A-0040), et son effet sur le muscle humain est démontré (EV-A-0008, EV-A-0009).
- *Aliment volaille.* La SCP de méthanotrophe (EV-A-0014) et, de façon plus discutée, les insectes (EV-A-0024) y entrent sans perte de performance à des taux modérés.
- *Hybridation.* C'est la seule voie de mise sur le marché du poulet cultivé à ce jour (EV-A-0039).

**Ce qui échoue ou déçoit.**
- *Pièces entières.* La fibrosité à l'échelle du faisceau musculaire reste absente (EV-A-0002, EV-A-0031), de même que l'élasticité acquise à la cuisson (EV-A-0001).
- *Micronutriments.* Le fer est très peu biodisponible dans les analogues à base d'isolats (EV-A-0004). Les analogues sont salés (Q-A-0010, Q-A-0018).
- *Marché.* Les ventes reculent (EV-A-0025), Meati a fait faillite et Beyond Meat est endetté (EV-A-0041). L'écart hédonique moyen reste de 30 % contre 68 % pour la viande (Q-A-0040).
- *Bilan environnemental.* Il n'est pas systématiquement meilleur que celui du poulet : selon l'unité fonctionnelle, le poulet se classe parmi les meilleurs (EV-A-0049).

**Ce qui reste à inventer.**
1. Un procédé de structuration à faible énergie qui crée une hiérarchie fibreuse à l'échelle de 0,1–1 mm.
2. Un système aromatique spécifique au poulet.
3. Des matrices dont le fer et le zinc sont biodisponibles, grâce à la fermentation et à un faible taux de phytates.
4. Une SCP qui égale le prix protéique du tourteau de soja pour l'aliment volaille.
5. Des fractions végétales standardisées, validées sur de nombreux passages, pour les milieux de culture de cellules de poulet.

---

## 5. Contradictions repérées

| Sujet | Côté A | Côté B | Lecture |
|---|---|---|---|
| ACV de la mycoprotéine | Impact le plus élevé, avec la viande cultivée (énergie de culture) — EV-A-0049 (2015) | 0,73 kg CO2e/kg, inférieur au soja et au pois — EV-A-0050 (2024, co-auteur Marlow Foods) | Les bases diffèrent (kg de produit humide à 11 % de protéines vs kg de repas ou de protéine digestible) et les inventaires aussi (2015 vs 2023) ; un calcul par kg de protéine reste à faire. |
| Ultra-transformation et santé | Aliments végétaux UPF : +5 % de MCV et +12 % de mortalité CV — EV-A-0022 | Régime végétal sain riche en UPF : −11 % de MCV — EV-A-0023 | Même cohorte (UK Biobank), définitions différentes ; aucune des deux n'isole les analogues de viande. |
| Insectes dans l'aliment du poulet | Pas d'effet global ; 28 % « recommandé » — EV-A-0024, Q-A-0041 | Dégradation à 10 % — EV-A-0032 | Hétérogénéité des substrats et des procédés ; le taux de 28 % paraît extrapolé. |
| Parité sensorielle des nuggets | Nuggets végétaux proches de la parité (NECTAR) — EV-A-0026 | Nugget vegan commercial le moins aimé (Pérou) — EV-A-0047 | Produits et panels différents ; NECTAR n'a été lu que par la presse. |
| Qualité protéique des burgers végétaux | DIAAS inférieur au bœuf — EV-A-0011 | TID > 0,90, comme la viande — EV-A-0012 | Les deux sont compatibles : la digestibilité est bonne, mais Met+Cys ou Lys limitent (EV-A-0043). |
| Texture de la HME | Profils TPA « proches de la viande » (cité dans EV-A-0002) | LMA insuffisante ; analogues moins élastiques (EV-A-0002, EV-A-0001) | La TPA ne mesure pas la fibrosité ; il faut des indicateurs dédiés (LMA, test de traction multi-pics, rhéologie LAOS). |
| Zinc de la mycoprotéine | 9 mg/100 g (ingrédient, entreprise) — Q-A-0019 (notes) | 6,7 mg/100 g (produits mesurés) — Q-A-0016 | Dilution par la formulation ; pas une vraie contradiction. |
| Allergies à la mycoprotéine | Très rares (base Marlow) — EV-A-0007 | Signalements CSPI comparables en nombre | Données de pharmacovigilance spontanée, sous-déclaration probable. |

---

## 6. Lacunes (cherché sans succès)

- **DIAAS mesuré du filet de poulet, de la mycoprotéine et des SCP bactériennes** : aucune valeur trouvée dans les sources lues (le résumé de Hodgkinson 2025 donne des médianes par catégorie).
- **Énergie et productivité industrielles de la HME et de la cellule de cisaillement** (kWh/kg, kg/h, rendement en protéine) : aucune donnée publique trouvée.
- **Analyse technico-économique publique de la mycoprotéine** : Upcraft 2021 identifié mais inaccessible (403).
- **Arôme d'analogues de poulet** (GC-O, AEDA) : aucune étude primaire.
- **Analogues laminés à base de yuba ou de kōya-dōfu** : aucune donnée mécanique moderne trouvée ; PDF J-STAGE illisible.
- **Rapports primaires NECTAR et GFI**, **texte officiel de la NHC (Chine)**, **avis ACNFP/EFSA sur Solein** : non obtenus.
- **Essai Kaplan et al. sur la biodisponibilité des protéines de Wolffia** : non retrouvé (seules des lettres de 2019).
- **Biodisponibilité du fer de Solein** (124 mg/100 g) et **acides nucléiques résiduels** des SCP alimentaires : aucune donnée trouvée.
- **Données en espagnol** : couverture quasi nulle (seules des communications de congrès et de la littérature grise ont été trouvées).

---

## 7. Pistes d'innovation

### Piste 1 — Filet de « poulet » laminé par films protéiques (yuba 2.0) avec perforation contrôlée

- **Problème.** Aucun procédé industriel ne reproduit la séparation en faisceaux millimétriques du filet de poulet (EV-A-0002, EV-A-0031).
- **Solutions actuelles.** La HME donne une structure feuilletée sans LMA. La micro-impression post-HME améliore la fibrosité, mais au prix de deux étapes énergivores (EV-A-0003). La cellule de Couette fonctionne par lots (EV-A-0016).
- **Insuffisances.** Énergie de la HME (110–160 °C), absence de hiérarchie fibreuse, pas de contrôle de l'adhésion entre couches.
- **Preuves d'une nouvelle approche.** La cuisine bouddhiste obtient des imitations de poulet par pressage de films de yuba (EV-A-0029). Le su ji industriel se fabrique à ≤99 °C (EV-A-0030). L'épaisseur de 1 mm et des liaisons faibles entre couches sont précisément ce qui restaure la fibrosité dans l'étude de Lou (EV-A-0003).
- **Hypothèse.** Un empilement de films de yuba (soja, ou soja–pois pour la diversité des matières) de 0,5–1 mm, perforés puis liés par une transglutaminase à faible dose, atteint un indice LMA et une rupture multi-pics non différents du filet de poulet cuit. L'énergie de procédé serait inférieure à celle de la HME.
- **Expérience de validation.** Films produits en bain thermostaté. Trois facteurs : épaisseur (3 niveaux), perforation (oui/non), dose de TG (3 niveaux). Mesures :
  - LMA index et traction multi-pics (méthode de SRC-A-0002) ;
  - TPA et résistance à la traction (cible 50–100 kPa, Q-A-0028) ;
  - rhéologie LAOS (SRC-A-0001), notamment l'élasticité après cuisson ;
  - panel de 60 consommateurs face au filet de poulet et à un HMMA ;
  - énergie électrique et thermique par kg (compteur).
- **Critères.** *Succès* : LMA non différent du poulet (p > 0,05, n ≥ 5), résistance dans la plage 50–100 kPa, préférence de fibrosité sur le HMMA, énergie inférieure à celle de la HME. *Échec* : délamination à la cuisson, ou productivité des films inférieure à 10 % de celle d'une ligne HME.
- **Coûts et risques.** Le principal risque est la productivité lente de la formation des films (cinétique de film, procédé discontinu). S'y ajoutent l'oxydation des lipides du yuba et l'allergène soja. Coût de laboratoire modeste (bain-marie, TG, analyseur de texture).

### Piste 2 — Système aromatique « poulet » sans hème : précurseurs soufrés et phospholipides

- **Problème.** Le goût et la texture sont les premiers freins (EV-A-0026, EV-A-0047). L'hème des analogues est calibré sur la viande rouge (EV-A-0019).
- **Insuffisances des solutions actuelles.** Les arômes sont souvent appliqués en surface, sans précurseurs réactifs à la cuisson. Aucune étude comparative d'olfactométrie n'existe (lacune).
- **Preuves.** Les odorants clés du poulet viennent de ribose/IMP + cystéine ou thiamine (2-méthyl-3-furanthiol) et de phospholipides polyinsaturés (2,4-décadiénal) (EV-A-0017).
- **Hypothèse.** Incorporer dans la matrice, avant cuisson, un système de précurseurs (ribose ou IMP, cystéine, thiamine) et une émulsion de phospholipides riches en acides gras polyinsaturés (lécithine) produit à la cuisson un profil d'odorants plus proche du poulet qu'un arôme de surface. Le choix de la lécithine fait écho à son usage dans la voie B (EV-C-0016).
- **Expérience.** Plan factoriel (précurseurs × phospholipides) sur un HMMA standard. Analyses GC-MS et GC-olfactométrie (AEDA) face au filet de poulet rôti. Tests triangulaires et descriptifs. Suivi du défaut de « réchauffé » à J+1 (EV-A-0017).
- **Critères.** *Succès* : présence du 2-méthyl-3-furanthiol et du (E,E)-2,4-décadiénal à des facteurs de dilution comparables au poulet, et score « goût de poulet » significativement accru. *Échec* : notes soufrées excessives, ou rancissement rapide.
- **Coûts et risques.** Coûts faibles. Risques : formation de composés indésirables (acrylamide, faux goûts soufrés), réglementation des arômes de réaction.

### Piste 3 — Matrice fermentée « dé-phytatée » et productrice de B12

- **Problème.** Le fer des analogues est très peu biodisponible (phytate:fer de 2,5 à 45 ; EV-A-0004). Ils contiennent peu de B12, et le tempeh n'en apporte que par sa flore bactérienne (EV-A-0033).
- **Preuves.** La fermentation (mycoprotéine, tempeh) abaisse fortement les phytates (EV-A-0005). La biomasse microbienne peut être très riche en fer (Solein : 124 mg/100 g, EV-A-0020). En France, la modélisation montre que l'enrichissement en fer et zinc est le levier nutritionnel clé (EV-A-0046).
- **Hypothèse.** Une fermentation en milieu solide de la matrice pois–soja texturée par Rhizopus, associée à une bactérie propionique productrice de B12, fait passer le rapport phytate:fer sous 1. Elle apporte au moins 0,34 µg de B12/100 g, le niveau du poulet (Q-A-0005), sans détruire la texture.
- **Expérience.** Comparer HMMA témoin et HMMA fermenté (24–48 h). Mesures : InsP6 et fer (comme SRC-A-0003), B12 active par LC-MS/MS, absorption du fer sur cellules Caco-2, TPA et LMA, analyse sensorielle.
- **Critères.** *Succès* : phytate:fer ≤ 1, B12 ≥ 0,34 µg/100 g, perte de dureté ≤ 20 %. *Échec* : pseudo-B12 inactive, perte de structure, risque microbiologique.
- **Coûts et risques.** Sécurité microbienne (Klebsiella dans les ferments traditionnels), durée de fermentation, statut de nouvel aliment selon la souche.

### Piste 4 — Fractions protéiques végétales standardisées comme « albumine » des milieux pour cellules de poulet (pont C→B)

- **Problème.** Le milieu pèse 50–90 % du coût matière de la viande cultivée (Q-A-0044). L'albumine recombinante coûte environ 24,56 USD/L (EV-A-0037).
- **Preuves.** Des protéines de soja, de pois ou de pois chiche à 0,1 mg/mL remplacent 2 mg/mL de BSA pour des fibroblastes de poulet sur 3 jours (brevet, EV-A-0036). Méthylcellulose et amidon, ou isolat de colza, coûtent de 0,002 à 0,054 USD/L (EV-A-0037).
- **Hypothèse.** Une fraction de protéine de pois, filtrée pour retirer la partie de moins de 10 kDa et produite à partir de concentrés alimentaires, maintient la croissance de fibroblastes ou de cellules satellites de poulet sur au moins 10 passages, avec une productivité au moins égale à 90 % de celle obtenue avec l'albumine.
- **Expérience.** Courbes de croissance sur 10 passages et plus. Mesures : temps de doublement, densité finale, stabilité caryotypique, coût par litre. À mener avec l'agent C.
- **Critères.** *Succès* : cible de 90 % atteinte et coût inférieur à 0,1 USD/L pour ce poste. *Échec* : cytotoxicité cumulative ou variabilité d'un lot à l'autre supérieure à 20 %.
- **Coûts et risques.** Standardisation et endotoxines des fractions végétales ; propriété intellectuelle (brevet WO2021/148955A1 à analyser par l'agent P).

---

## 8. Recherches restantes (prioritaires)

1. **DIAAS mesurés** du filet de poulet, de la mycoprotéine, de Solein et de C. necator : texte intégral de Hodgkinson 2025 (97 aliments), travaux du laboratoire Stein, dossiers réglementaires.
2. **Énergie, rendement et coût de la HME et de la cellule de cisaillement à l'échelle industrielle**, et analyse technico-économique de la mycoprotéine : rapports TEA du GFI et de Wageningen, versions auteur d'Upcraft 2021, données Marlow Foods et Fuxiang.
3. **Arôme des analogues de poulet** : études GC-O, brevets d'arômes de réaction « poulet », extraits de levure.
4. **Analogues laminés (yuba, 腐竹) et congelés (高野豆腐)** : CNKI/Wanfang, J-STAGE avec OCR, mesures mécaniques ; recherche d'antériorité de brevets (agent P).
5. **SCP pour l'aliment volaille** : essais poulet avec des bactéries hydrogénotrophes, autorisations UE (FeedKind, Uniprotein), prix réel par kg de protéine face au tourteau de soja ; à croiser avec l'agent N.
