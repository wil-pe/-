# Viande cultivée de poulet (voie B) — état réel des connaissances, obstacles et pistes

*Brouillon v1 — agent C (Biotechnologies et viande cultivée), 2026-10-25. Toutes les affirmations renvoient aux tables `research/agents/C/` (`EV-C-…`, `Q-C-…`, `SRC-C-…`) ou à des sources enregistrées par d'autres agents (`SRC-E-…`, `SRC-X-…`).*

**Légende de la nature des preuves**, utilisée dans tout le texte :
**[P]** démontré avec des cellules de poulet ; **[Av]** démontré chez un autre oiseau (caille) ; **[X]** extrapolé d'une autre espèce (bovin, ovin, souris) ; **[M]** modèle ou analyse technico-économique ; **[E]** annonce d'entreprise ou presse ; **[R]** texte réglementaire officiel.
**Bases de calcul** : *biomasse humide* (cellules récoltées, eau comprise) ≠ *matière sèche* ≠ *protéine* ≠ *tissu musculaire* ≠ *produit fini* (mélange cellules + ingrédients). Une densité obtenue à l'échelle du laboratoire n'est pas une densité démontrée industriellement.

---

## Résumé

1. **Les trois poulets cultivés évalués par la FDA sont surtout des fibroblastes, pas du muscle.** GOOD Meat (lignée DF-1) et Believer Meats livrent une biomasse de fibroblastes en suspension, sans aucune phase de différenciation musculaire ; UPSIDE livre des feuillets de cellules « ayant des caractéristiques de myocytes et de fibroblastes », dans des proportions non publiées [R] (EV-C-0001, EV-C-0006, EV-C-0009). La caille de Vow, dont la sécurité a été évaluée favorablement par FSANZ (Australie et Nouvelle-Zélande, avril 2025), est elle aussi faite uniquement de fibroblastes [Av][R] (EV-C-0022).
2. **Le point fort propre au poulet, c'est l'immortalisation spontanée des fibroblastes.** Elle donne des lignées non génétiquement modifiées, stables sur 100 à 500 doublements de population (DF-1 ; Believer) [P][R] (EV-C-0008, EV-C-0010). Chez le bovin, l'équivalent demande environ 400 jours de culture [X] (EV-C-0019). Le phénomène n'est pourtant pas trivial : une crise réplicative longue précède l'émergence des lignées (EV-C-0066), et la littérature académique le jugeait « très rare » (EV-C-0036, EV-C-0067).
3. **Les densités les plus élevées publiées pour des cellules animales alimentaires viennent du poulet**, et d'une seule équipe liée à une entreprise : 108 × 10⁶ cellules/mL en continu sans sérum, et 130 × 10⁶ cellules/mL (43 % p/v) en perfusion par filtration tangentielle pendant plus de 20 jours, à l'échelle du laboratoire [P] (Q-C-0001, Q-C-0003). Ces valeurs dépassent la limite pratique de 86 × 10⁶ cellules/mL (258 g/L humides) du modèle de Humbird [M] (EV-C-0040).
4. **Production sans sérum ni facteurs de croissance : démontrée à petite échelle, mais pas pour les produits vendus.** Believer a déclaré à la FDA une production en milieu sans composant animal et sans insuline ni FGF2 recombinants [R] (EV-C-0011). En revanche, le poulet vendu par UPSIDE en 2023 était produit avec du sérum [R] (EV-C-0004), et le dossier FDA de GOOD Meat mentionne du FBS (EV-C-0007). Vow utilise encore deux facteurs de croissance recombinants [Av] (EV-C-0023).
5. **La biomasse récoltée contient environ moitié moins de protéines que le filet.** C'est mesuré chez la caille : 9 g/100 g contre 18,5 g/100 g, avec au moins 80 % d'eau [Av][R] (EV-C-0020, EV-C-0021). Le mémo FDA de Believer va dans le même sens, sans chiffres (EV-C-0013). Un coût exprimé par kg de biomasse humide sous-estime donc d'un facteur ~2 le coût par kg de protéine (EV-C-0074, Q-C-0083).
6. **Pour le muscle de poulet *différencié*, rien d'industrialisable n'est publié.** Les cellules satellites restent primaires, cultivées avec du sérum et envahies par des fibroblastes (EV-C-0029, EV-C-0032). L'unique lignée immortalisée par un oncogène (SV40-LT) a échoué (EV-C-0044). Le meilleur indice de fusion publié (30 %) exige un transgène MyoD (EV-C-0027). Aucun milieu de différenciation sans sérum n'est publié pour le poulet (journal, requête n° 46).
7. **L'économie projetée contredit les faits industriels.** La TEA de Believer annonçait 6,2 USD/lb [M] (EV-C-0018), mais l'entreprise a fermé en décembre 2025 faute de fonds, après avoir levé 390 M USD [E] (EV-C-0065). En avril 2024, le Bundestag constatait l'absence de production commerciale (EV-C-0068). Les produits vendus au détail que nous avons repérés sont des hybrides très dilués : 3 % de poulet cultivé dans GOOD Meat 3 (Singapour, 2024), 4 % dans une friandise pour chiens (Royaume-Uni, 2025) [E] (EV-C-0075, Q-C-0084, Q-C-0069).

---

## 1. Périmètre et méthode

- **Questions couvertes** : RQ-C1 à RQ-C8, avec des apports à RQ-X1–X3.
- **Bases consultées** : Europe PMC (prépublications incluses), PubMed, Crossref, J-STAGE, HAL, theses.fr et Consensus (un seul appel), ainsi que WebSearch/WebFetch pour les sites officiels (FDA, SFA, FSANZ, Bundestag) et la presse spécialisée, toujours identifiée comme telle. Le détail des 53 requêtes est dans `research/agents/C/search_log.md`.
- **Langues** : en, fr, zh, es, pt, ja, ko, de, nl, he. La production non anglophone sur le poulet est mince : un article chinois (SRC-C-0021) et des documents d'entreprise ou de presse en japonais, coréen et chinois (SRC-C-0022, 0025, 0026). La recherche coréenne et brésilienne (Embrapa) paraît en anglais.
- **Corpus** : 43 sources enregistrées par C, plus 5 réutilisées (SRC-X-0001, SRC-E-0001, SRC-E-0002, et, après vérification dans le document primaire, SRC-A-0034 et SRC-P-0018).
  - Ont été lus intégralement : 5 documents FDA, les sections utiles du dossier FSANZ, 2 documents SFA, le rapport du Bundestag et 26 textes intégraux Europe PMC.
  - Seuls les résumés étaient accessibles pour Pasitka 2023, 2024 et 2025 (*Nature Food*, payant), Contreras 2026 et Li 2025.
- **Limites d'accès** :
  - *Nature Food* est payant ; Ben-Arye 2020 n'a pas été retrouvé dans les bases et n'est donc pas enregistré.
  - La SFA ne publie pas les dossiers d'autorisation.
  - 中国食品学报 renvoyait une erreur HTTP 503 ; CNKI est bloqué.
  - Les compositions de milieux, les volumes de bioréacteurs et les rendements industriels restent confidentiels, y compris dans les mémos FDA, qui renvoient à des « annexes confidentielles ».

---

## 2. État des connaissances par question

### RQ-C1 — Types cellulaires, lignées, stabilité génétique

**Fibroblastes embryonnaires : la seule voie déjà autorisée.**

- GOOD Meat utilise la lignée commerciale DF-1 (UMNSAH/DF1, ATCC CRL-12203). Elle provient d'embryons de 10 jours et s'est immortalisée spontanément ; elle a été adaptée à la suspension et à un milieu pauvre en sérum [R] (EV-C-0006).
- Believer isole des fibroblastes d'œufs de poulet Baladi israélien, attend leur immortalisation spontanée, puis les adapte à la suspension [R] (EV-C-0009).
- UPSIDE combine deux lignées : des myoblastes de poulets adultes et des fibroblastes de peau d'embryon. Elles sont immortalisées soit spontanément, soit par un **cisgène TERT de poulet** [R] (EV-C-0002).
- Chez la caille (Vow), l'immortalisation est survenue spontanément en sérum réduit et en suspension ; le séquençage du génome montre que les variants apparaissent surtout à ce moment-là, puis restent stables [Av][R] (EV-C-0022).

**Stabilité génétique : surtout des données d'entreprise.**

- DF-1 : plus de 100 doublements et 160 passages sans aberration sur 100 cellules examinées. Entre la lignée parentale et les cellules récoltées, le nombre modal de chromosomes passe de 76 à 72 (EV-C-0008, Q-C-0009). C'est une dérive, jugée acceptable par la FDA.
- Believer : caryotype normal sur 500 doublements, temps de doublement stable sur plus de 800 jours, pas de mutation de TP53 [R, données de l'entreprise] (EV-C-0010, Q-C-0013, Q-C-0014).
- La SFA exige une évaluation de la stabilité, par exemple par caryotypage [R] (SRC-C-0010).

**Comment se fait l'immortalisation spontanée.** Une étude complète sur des fibroblastes embryonnaires de poulet primaires (CEF) en décrit les étapes (EV-C-0066, Q-C-0073 à Q-C-0076) :
- les CEF primaires se divisent environ une fois par jour (1,03 doublement/jour) ;
- ils entrent en crise entre les passages 18 et 33 ;
- la lignée qui en émerge ne pousse d'abord qu'à 0,12 doublement/jour, puis accélère à 0,60 au-delà du passage 80 ;
- DF-1 atteint 1,33 doublement/jour, soit un temps de doublement d'environ 18 h [P].

Il faut donc des mois de culture, une sélection, et accepter une dérive génétique.

**Les autres types cellulaires sont nettement moins mûrs.**

- *Cellules satellites* : uniquement primaires et cultivées avec du sérum dans toutes les études lues (EV-C-0031 à EV-C-0034). Les fibroblastes contaminent les isolats (EV-C-0029) ; une culture primaire peut compter plus de 40 % de cellules non myogéniques (Q-C-0033). L'immortalisation par SV40-LT n'a pas fonctionné, avec un suivi limité au passage 12 et une dépendance au sérum (EV-C-0044). **Aucune lignée de cellules satellites de poulet immortalisée par TERT/CDK4 n'a été trouvée**, ni en anglais ni en chinois.
- *Préadipocytes* : les cellules primaires s'arrêtent vers 9 doublements ; après transduction de chTERT/chTR, elles dépassent 100 doublements [P] (EV-C-0035).
- *Cellules germinales primordiales (PGC)* : c'est le seul type cellulaire de poulet qui s'auto-renouvelle en milieu totalement défini, sans sérum ni cellules nourricières, avec FGF2 + insuline + activine A [P] (EV-C-0053). Ces cellules n'ont toutefois pas d'intérêt direct comme tissu alimentaire.
- *Cellules souches embryonnaires* : « aucun système de culture largement applicable » ; on utilise encore des cellules nourricières de rongeur [P] (EV-C-0054, EV-C-0037). Aucune donnée de production n'a été trouvée pour les iPSC de poulet.

### RQ-C2 — Prolifération et densités

- **Temps de doublement chiffrés pour le poulet** :
  - DF-1 en 2D avec sérum : ~18 h ; CEF primaires : ~23 h [P] (Q-C-0073, Q-C-0074).
  - Les études coréennes sur cellules satellites ne donnent les temps de doublement qu'en figure. Elles montrent un avantage des cellules embryonnaires sur celles de poulets de 5 semaines (EV-C-0031) et une prolifération plus forte à **41 °C**, la température corporelle du poulet, qu'à 37 °C (EV-C-0033).
  - **Aucun temps de doublement de cellules satellites de poulet en milieu sans sérum n'a été trouvé** (requêtes 6, 46, 47). La référence sans sérum reste bovine : Beefy-9, ~39 h, 18,2 doublements en 28 jours [X] (Q-C-0044, Q-C-0045).
- **Densités** :
  - 108 × 10⁶ cellules/mL en continu, sans sérum, soit 36 % p/v (Q-C-0001, Q-C-0002) ;
  - 130 × 10⁶ cellules/mL en perfusion par filtration tangentielle, 43 % p/v, sur plus de 20 jours (Q-C-0003 à Q-C-0005) [P].
  - Ces chiffres viennent d'un résumé seulement, d'une équipe liée à Believer, à l'échelle du laboratoire. À titre de comparaison, les cuves agitées de thérapie cellulaire tournent à 0,19–2 × 10⁶ cellules/mL et les fibres creuses à 10⁸–10⁹ cellules/mL [X] (Q-C-0058, Q-C-0059).
  - Les volumes industriels ne sont jamais publiés. GOOD Meat évoque un bioréacteur de 6 000 L, Meatly un pilote de 320 L [E] (Q-C-0067, EV-C-0064). En Chine, des essais de porc cultivé à 2 000 L sont annoncés [E] (Q-C-0051).
- **Conversion en masse** : on suppose 3 à 3,5 ng de biomasse humide par cellule [M] (Q-C-0042, Q-C-0057), soit environ 2,9 × 10¹¹ cellules par kg humide (EV-C-0052). Les 43 % p/v de Pasitka impliquent environ 3,3 ng par cellule (calcul de C, Q-C-0004) : c'est cohérent avec ces hypothèses, mais cela suppose une fraction volumique cellulaire supérieure à la limite de viscosité retenue par Humbird (EV-C-0040). La méthode de mesure du « % p/v » (culot humide ?) reste à vérifier.

### RQ-C3 — Différenciation, maturation et part réelle de muscle

- **Dans les produits autorisés, la part de muscle est nulle (GOOD Meat, Believer) ou inconnue (UPSIDE)** [R] (EV-C-0001, EV-C-0006, EV-C-0009).
  - UPSIDE est la seule à décrire une phase adhérente de différenciation, avec hypertrophie et formation d'un « tissu cohérent » (SRC-C-0001, p. 11), sans donner de proportion de myocytes.
  - Une équipe coréenne affirme, sans données, que les produits structurés contiennent moins de 10 % de cellules musculaires [E/opinion] (EV-C-0051).
- **Différenciation démontrée chez le poulet** :
  - Myotubes à partir de cellules satellites primaires, induits avec 2 % de sérum de cheval (SRC-C-0016, SRC-C-0013) ou avec extrait d'embryon de poulet + sérum de cheval (EV-C-0034).
  - Transdifférenciation de fibroblastes immortalisés par un MyoD inductible : indice de fusion de 30,49 % en hydrogel 3D, soit environ 70 % de noyaux hors myotubes, et cela reste une modification génétique [P] (EV-C-0027, Q-C-0028).
  - Aucun milieu de différenciation sans sérum n'est publié pour le poulet : les seuls sont bovins ou porcins (requête 46).
- **La graisse est l'étape de différenciation la plus solide.** La lécithine active PPARγ et déclenche l'adipogenèse des fibroblastes de poulet. Ce résultat a été rapporté par Believer (EV-C-0016), reproduit indépendamment par Embrapa (EV-C-0037), et le potentiel est conservé après 576 doublements (EV-C-0010). Les fibroblastes primaires se transdifférencient aussi en adipocytes jusqu'au passage 9 (EV-C-0030).
- **Écart biochimique** : des cellules satellites et des myotubes de poulet diffèrent de la viande par 66 à 69 métabolites (variation d'au moins un facteur 2) [P] (EV-C-0050). La maturation *post mortem* de la viande n'a pas d'équivalent en culture (EV-C-0047).

### RQ-C4 — Milieux de culture

- **Sérum** :
  - Les fibroblastes de poulet s'adaptent progressivement à 1,5 % de FBS ou à 1 % de sérum de poulet, au prix d'une prolifération plus lente (EV-C-0028), puis au sans-sérum (Believer, Vow).
  - Mais les produits réellement fabriqués aux États-Unis en 2023 utilisaient du sérum (UPSIDE : EV-C-0004 ; GOOD Meat, FBS à faible teneur : EV-C-0007).
  - Le procédé sans sérum d'UPSIDE donnait plus de plomb que le procédé avec sérum (47,6 contre 13,3 ppb), ce qui montre l'importance de la pureté des intrants (EV-C-0005, Q-C-0018, Q-C-0019).
- **Facteurs de croissance** :
  - Ils représentent ~98 % du coût du milieu E8 et ~60 % de Beefy-9 (EV-C-0070, Q-C-0078).
  - Le milieu sans sérum de 2023 pour fibroblastes de poulet contenait encore 10 ng/mL de FGF-2 et 3 µg/mL d'insuline, d'après la revue de Quek (EV-C-0071).
  - Selon la FDA, Believer s'en passe en production (EV-C-0011).
  - Vow ajoute deux facteurs recombinants produits dans l'orge (pureté 20–30 %) ou dans *E. coli* (EV-C-0023, Q-C-0025).
  - Un FGF-2 *aviaire* est vendu environ 136 SGD/mg, contre 990 SGD/mg pour un FGF-2 humain de référence (EV-C-0072, Q-C-0080).
- **Coût du milieu par litre**, sur quatre ordres de grandeur :
  - 376,80 USD/L dans le scénario de référence de Risner [M] (Q-C-0048) ;
  - 217 USD/L pour Beefy-9 aux prix de laboratoire [X] (Q-C-0046) ;
  - 0,63 USD/L chez Believer (estimation publiée, Q-C-0006) ;
  - 0,22 £/L annoncés par Meatly [E] (Q-C-0068) ;
  - « 1/60 » du prix d'un milieu sérique selon IntegriCulture [E] (Q-C-0050).
- **Substituts testés sur cellules aviaires** :
  - Extrait d'embryon de poulet : inférieur au FBS (EV-C-0034).
  - Extraits d'œuf : environ 5 USD par 500 mL, en conditions à faible sérum (EV-C-0056).
  - Hydrolysats d'algues : effet très dépendant de la lignée (testé sur la lignée de caille QM7) (EV-C-0055).
  - Optimisation métabolomique de 28 métabolites : +40,7 % de croissance (étude primaire non lue) (EV-C-0073).
  - Believer utilisait aussi l'hydroxypropyl-β-cyclodextrine (HPβCD), une substance nouvelle pour la FDA, et une enzyme dérivée du soja, retirée depuis (Q-C-0017, SRC-C-0005).
  - **Remplacement de l'albumine par des protéines végétales** : dans les exemples du brevet WO 2021/148955 A1 (Future Meat/Yissum), 0,1 mg/mL de protéines de soja, de pois ou de pois chiche suffisent à remplacer la BSA pour des fibroblastes de poulet en suspension, à 39 °C, sans sérum. Le chanvre et le blé échouent, et la fraction de moins de 10 kDa est toxique [P, données de brevet, jour 3 seulement] (EV-C-0076, Q-C-0085, Q-C-0086 ; SRC-P-0018). Le brevet ne chiffre pas la concentration de BSA utilisée comme comparateur.
- **Ammoniac, lactate et recyclage** :
  - Humbird retient 5 mM de NH₃ et 50 mM de lactate comme seuils d'inhibition ; l'ammoniac plafonne alors la densité à ~110 g/L en fed-batch [M] (EV-C-0038).
  - Believer avait décrit une « régénération » du milieu par filtration, mais **ne l'a pas utilisée** pour le matériau évalué [R] (EV-C-0012).
  - Ailleurs, un strippage alcalin élimine plus de 82 % de l'ammoniac, et un mélange 50 % recyclé / 50 % frais soutient la croissance [X, ovin] (EV-C-0060).
  - Les myoblastes murins ne consomment que ~26 % des acides aminés autres que glucose et glutamine (EV-C-0062).
  - **Le recyclage du milieu n'est démontré chez aucune lignée de poulet.**

### RQ-C5 — Bioréacteurs, transfert d'oxygène, contamination

- **Mode de culture** :
  - Les trois procédés FDA font proliférer les cellules en suspension, en cuves agitées.
  - Believer pratique l'échange de milieu, interprète une chute brutale de l'oxygène dissous comme signe de contamination et prévoit une montée en volume en Caroline du Nord. La FDA prend acte de cet engagement mais n'a pas évalué l'échelle (SRC-C-0003, p. 14, note 15).
  - UPSIDE ajoute une phase adhérente, plus difficile à monter en échelle que la suspension (EV-C-0001).
- **Limites physiques et métaboliques** (modèles) :
  - L'ammoniac limite la densité dans les cuves de moins de 20 m³, le CO₂ (pCO₂ > 100 mbar) au-delà [M] (EV-C-0038, Q-C-0040).
  - La perfusion (ATF) permet ~195 g/L, mais coûte 51 contre 37 USD/kg humide en fed-batch (EV-C-0039, Q-C-0041).
  - Dans un modèle de procédé complet à 20 000 L, les utilités (stérilisation du milieu, nettoyage en place, refroidissement) et l'expansion cellulaire sont les goulots d'étranglement (EV-C-0061).
- **Oxygène** : aucune donnée de transfert d'O₂ mesurée sur des cellules de poulet n'a été trouvée. La culture à 41 °C augmente la respiration mitochondriale (EV-C-0033) alors que l'oxygène est moins soluble à cette température : c'est une hypothèse de travail à vérifier (voir piste I-2). Dans des agrégats non vascularisés, des sphéroïdes de 500 µm ou plus deviennent nécrotiques (EV-C-0049).
- **Contamination** :
  - Aucune étape du procédé ne réduit la charge microbienne. Le risque principal se situe à la récolte (*Listeria monocytogenes*) et il augmente avec les soutirages et remplissages répétés, c'est-à-dire en culture continue [Av][R] (EV-C-0024).
  - **Aucun taux de contamination publié n'a été trouvé** (requête 53). Les trois procédés FDA déclarent ne pas utiliser d'antibiotiques en production.

### RQ-C6 — Supports et structuration

- La structure vient surtout de la matrice végétale. Les lanières de Believer associent cellules adipeuses et soja extrudé : la texture est attribuée aux protéines animales et végétales, l'arôme à la graisse cultivée (EV-C-0016).
- Supports comestibles testés avec des cellules de poulet :
  - cellulose bactérienne en hydrogel (EV-C-0049) ;
  - microporteurs en cellulose bactérienne revêtus de chitosane (EV-C-0058) ;
  - GelMA, un gel à base de gélatine, non optimisé pour l'alimentation (EV-C-0027).
- Les microporteurs non comestibles imposent une étape de dissociation coûteuse (EV-C-0059).
- Des cellules musculaires de poulet co-cultivées avec des fibroblastes DF-1 se différencient mieux (EV-C-0058). C'est une piste pour réduire les facteurs de croissance.
- **Aucune mesure quantitative de texture (TPA, cisaillement) d'un poulet cultivé n'a été trouvée.**

### RQ-C7 — Composition, nutrition, sécurité

- **Poulet, données FDA** [R] :
  - Les lots UPSIDE contiennent plus de fer, de potassium, de phosphore, de cholestérol et de folates que le filet (EV-C-0014).
  - La biomasse Believer est plus humide et plus pauvre en protéines, lipides et cendres que le filet, et plus salée à cause du lavage (EV-C-0013).
  - GOOD Meat : 80 µg de fer/100 g, moins que le poulet (Q-C-0010).
  - La FDA précise qu'elle n'interprète pas ces données comme une information nutritionnelle définitive.
- **Caille, données FSANZ** [Av][R] :
  - 9 g de protéines/100 g, 1,5–1,6 g de lipides, humidité d'au moins 80 % (Q-C-0021, Q-C-0023, Q-C-0024).
  - Fortes teneurs en cobalamine (jusqu'à 929 fois le besoin moyen estimé par portion), biotine, folates, fer et sodium, attribuées au milieu (EV-C-0025).
- **Sécurité** :
  - Le cisgène TERT est jugé sans danger après cuisson et digestion (SRC-C-0001, p. 7).
  - Believer n'a pas détecté de protéines d'œuf (seuil de 2,5 ppm) (SRC-C-0003).
  - Plomb : spécification de moins de 100 ppb chez UPSIDE (Q-C-0020).
  - HPβCD résiduelle inférieure à 0,009 % (Q-C-0017).
  - Les facteurs de croissance résiduels sont mesurés et réduits par la cuisson : environ 80 % de baisse pour l'un des facteurs de Vow (SRC-C-0008, § 3.1.3).
- **Produits finis** :
  - À Singapour, les cellules servaient d'ingrédient de nuggets (EV-C-0026).
  - Les friandises pour chiens Chick Bites contenaient 4 % de cellules [E] (Q-C-0069).
  - Le premier poulet cultivé vendu au détail, GOOD Meat 3 (Singapour, mai 2024), ne contient que **3 % de poulet cultivé**, le reste étant des protéines végétales. Le communiqué de l'entreprise justifie ce choix notamment par la réduction des coûts [E] (EV-C-0075, Q-C-0084 ; source primaire SRC-A-0034, déjà enregistrée par l'agent A). Le communiqué ne dit rien du milieu ni des volumes.

### RQ-C8 — Coûts, rendements, obstacles démontrés

- **Projections** :
  - Believer : 6,2 USD/lb, soit environ 13,7 USD/kg, pour une usine théorique de 50 000 L [M] (EV-C-0018, Q-C-0007).
  - Humbird : 37 USD/kg humide en fed-batch et 51 USD/kg en perfusion [M] (EV-C-0039 ; EV-E-0001 de l'agent E).
  - Risner : environ 437 000 USD/kg dans le scénario de référence, 1,95 USD/kg seulement si toutes les ruptures technologiques se produisent (EV-C-0043 ; EV-E-0005).
- **Par kg de protéine** : avec la composition mesurée de la caille, les 37 USD/kg humide de Humbird deviennent ~411 USD/kg de protéine. L'hypothèse implicite de Humbird (~21 % de protéines dans la biomasse humide) en donnerait ~176 (calcul de C, EV-C-0074, Q-C-0082, Q-C-0083).
- **Faits industriels** :
  - Fermeture de Believer, malgré un dossier FDA favorable et une usine prévue pour au moins 12 000 t/an [E] (EV-C-0065, Q-C-0071). Une autorisation USDA de l'usine en novembre 2025 n'apparaît que dans un résumé de moteur de recherche ; elle n'est pas vérifiée.
  - Aucune production commerciale en 2024 selon le Bundestag (EV-C-0068).
  - Les autorisations peuvent aussi servir à financer les entreprises (SRC-C-0042).
  - Les produits vendus au détail repérés contiennent 3 % (GOOD Meat 3, 2024) et 4 % (Chick Bites, aliment pour chiens, 2025) de cellules (Q-C-0084, Q-C-0069). Les volumes de biomasse réellement produits restent donc très faibles.

---

## 3. Tableaux quantitatifs

### Tableau A — Performances démontrées en cellules de poulet (et caille, signalée)

| Type cellulaire / lignée | Milieu | Système | Temps de doublement / croissance | Doublements cumulés | Densité max | Durée | Différenciation | Échelle | Source |
|---|---|---|---|---|---|---|---|---|---|
| Fibroblastes spontanément immortalisés (plusieurs races) | sans sérum | suspension, culture continue | n.d. (résumé) | n.d. | 108 × 10⁶ cell./mL ; 36 % p/v (humide supposée) | n.d. | adipogenèse (lécithine) | labo | EV-C-0015, Q-C-0001/0002 |
| Idem (Believer) | sans composant animal, 0,63 USD/L | perfusion par filtration tangentielle | n.d. | n.d. | 130 × 10⁶ cell./mL ; 43 % p/v | > 20 j, récoltes multiples | — | labo (volume n.d.) | EV-C-0017, Q-C-0003–0006 |
| Fibroblastes Baladi (Believer, dossier FDA) | sans composant animal ni insuline/FGF2 en production | suspension, échange de milieu | stable > 800 j | 500 (caryotype normal) | n.d. | — | adipogène après 576 doublements | pilote (Rehovot) | EV-C-0010/0011 |
| DF-1 (GOOD Meat) | FBS réduit + Pluronic | suspension | 1,33 doublement/j (~18 h, en 2D avec sérum) | > 100 (> 160 passages) | n.d. | — | aucune | pilote (JOINN) | EV-C-0006/0008, Q-C-0073 |
| CEF primaires | 20 % FBS ou sérum | 2D | 1,03 doublement/j ; crise aux passages 18–33 | ~12–17 passages | — | — | adipogène jusqu'au passage 9 | labo | Q-C-0074/0075, EV-C-0030 |
| Fibroblastes immortalisés + MyoD (transgène) | 12 → 1,5 % FBS ; 1 % sérum de poulet | 2D/3D GelMA | n.d. | n.d. | — | — | **indice de fusion 30,5 %** (3D) | labo | EV-C-0027/0028 |
| Cellules satellites primaires (embryon / broiler) | 15–20 % FBS ou sérum de poulet + sérum de cheval | 2D | figures seulement ; meilleure à 41 °C | — | — | — | myotubes avec 2 % de sérum de cheval | labo | EV-C-0031–0034 |
| Cellules satellites + SV40-LT | 0–20 % FBS | 2D | ralentissement tardif | jusqu'au passage 12 | — | — | MyoD/MyHC (qPCR) | labo | EV-C-0044 |
| Préadipocytes chTERT/chTR | FBS | 2D | — | > 100 (primaires : 9) | — | > 1 an | adipogène | labo | EV-C-0035 |
| PGC | défini, FGF2 + insuline + activine A | suspension (agrégats) | n.d. | lignées pérennes | — | — | — | labo | EV-C-0053 |
| **[Av]** Fibroblastes de caille (Vow) | sans sérum + 2 facteurs recombinants | suspension, cuves agitées | n.d. | n.d. | n.d. | — | aucune | échelle actuelle de Vow | EV-C-0022/0023 |

### Tableau B — Produits et dossiers réglementaires (documents officiels)

| Dossier | Cellules | Différenciation | Milieu déclaré | Forme à la récolte | Composition publiée | % de cellules dans le produit fini | Source |
|---|---|---|---|---|---|---|---|
| FDA CCC 000002 — UPSIDE (mémo 14/11/2022) | myoblastes (adulte) + fibroblastes (embryon) ; spontanées ou cisgène TERT | oui, adhérente (« caractéristiques de myocytes et de fibroblastes ») | acides aminés, BSA, facteurs de croissance ; une version avec sérum bovin ; **produit commercialisé avec sérum** | feuillets cellulaires, humidité ajustée | qualitatif : Fe, K, P, cholestérol, folates plus élevés ; plomb 13,3 (avec sérum) / 47,6 ppb (sans) | non publié | EV-C-0001–0005, EV-C-0014 |
| FDA CCC 000001 — GOOD Meat (17/03/2023) | DF-1 (fibroblastes) | non | basal + FBS (faible) + anti-agrégant | pâte cellulaire (centrifugation) | Fe 80 µg/100 g ; hypoxanthine 46,9 mg/100 g ; nitrate 2 mg/100 g | absent du mémo FDA ; **3 % dans GOOD Meat 3** (Singapour, communiqué de l'entreprise, mai 2024 ; EV-C-0075) | EV-C-0006–0008, Q-C-0010–0012 |
| FDA CCC 000039 — Believer (24/07/2025 ; complément 24/09/2025) | fibroblastes Baladi spontanés | non (potentiel adipogène) | sans composant animal ; sans insuline/FGF2 en production ; HPβCD ; enzyme de soja retirée | biomasse lavée (NaCl) | qualitatif : + humidité, − protéines/lipides/cendres, + sodium | non publié | EV-C-0009–0013, SRC-C-0005 |
| SFA Singapour — Eat Just/GOOD Meat (déc. 2020 ; sans sérum janv. 2023) | poulet (dossier non public) | — | sans sérum autorisé en 2023 [presse] | — | non publiée | ingrédient de nuggets | EV-C-0026, EV-C-0063 |
| FSANZ A1269 — Vow, caille (avril 2025) [Av] | fibroblastes embryonnaires 221523-Fib-Quail | non | basal sans composant animal + 2 facteurs recombinants | cellules récoltées congelées | **protéines 9 g/100 g ; lipides 1,5–1,6 ; humidité ≥ 80 %** | ingrédient principal, ≤ 300 g/portion | EV-C-0020–0025 |
| Royaume-Uni — Meatly (aliment pour animaux, 2024–2025) [E] | poulet (type non précisé) | — | sans protéine ni facteur de croissance (déclaré) | — | — | **4 %** (Chick Bites) | EV-C-0064, Q-C-0069 |

### Tableau C — Obstacles hiérarchisés et ordre de grandeur de l'écart

| Rang | Obstacle | Preuves | Écart à combler (ordre de grandeur) |
|---|---|---|---|
| 1 | **Rentabilité du capital et de l'échelle** | Believer fermé (EV-C-0065) ; 37–51 USD/kg humide modélisés (EV-C-0039) ; installation ~600 M USD (Q-C-0053, estimation non sourcée) | Projection la plus optimiste : 13,7 USD/kg, sur une base non vérifiée (Q-C-0007). Coût réel inconnu. L'écart avec le coût du poulet conventionnel est à chiffrer avec l'agent E (RQ-E1), car aucune valeur de référence n'a été enregistrée par C. |
| 2 | **Absence de muscle différencié à l'échelle** | produits = fibroblastes (EV-C-0006/0009) ; fusion 30 % avec transgène (EV-C-0027) ; aucun milieu de différenciation sans sérum chez le poulet | pas de procédé démontré : écart qualitatif |
| 3 | **Densité protéique et nutritionnelle** | 9 contre 18,5 g de protéines/100 g [Av] (EV-C-0020) | facteur ~2 sur la base protéique (EV-C-0074) |
| 4 | **Coût et définition du milieu, facteurs de croissance** | de 0,63 à 376 USD/L selon les sources (Q-C-0006, Q-C-0048) ; Vow dépend de facteurs recombinants (EV-C-0023) | 2 à 3 ordres de grandeur entre laboratoire académique et annonces industrielles ; ≤ 1 USD/L non vérifié indépendamment |
| 5 | **Métabolites, recyclage du milieu** | seuils NH₃ 5 mM et lactate 50 mM (EV-C-0038) ; régénération non utilisée (EV-C-0012) | recyclage = 0 % démontré chez le poulet |
| 6 | **Transfert d'O₂, CO₂, utilités à grande échelle** | CO₂ limitant au-delà de 20 m³ (EV-C-0038) ; utilités = goulot (EV-C-0061) | aucune donnée poulet au-delà du pilote |
| 7 | **Contamination et aseptie en culture continue** | risque accru avec soutirages répétés (EV-C-0024) ; aucun taux publié | inconnu (absence de données) |
| 8 | **Structuration** | nécrose des sphéroïdes ≥ 500 µm (EV-C-0049) ; produits = hybrides végétaux (EV-C-0016) | épaisseur viable sans perfusion interne : ~0,3 mm, à comparer à l'épaisseur d'un morceau entier |

---

## 4. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Fonctionne (chez le poulet)** :
- immortalisation spontanée de fibroblastes et adaptation à la suspension (EV-C-0006, 0009, 0015) ;
- culture sans sérum et, selon la FDA, sans facteurs de croissance en production (EV-C-0011) ;
- densités supérieures à 10⁸ cellules/mL au laboratoire (Q-C-0003) ;
- adipogenèse simple, à la lécithine (EV-C-0016, 0037) ;
- milieu totalement défini pour les PGC (EV-C-0053) ;
- remplacement à court terme de la BSA par 0,1 mg/mL de protéines de légumineuses (données de brevet, EV-C-0076) ;
- passage de l'évaluation de sécurité aux États-Unis, à Singapour, et pour la caille en Australie et Nouvelle-Zélande.

**Échoue ou reste fragile** :
- cellules satellites (sénescence, contamination par les fibroblastes, dépendance au sérum ; EV-C-0029, 0032, 0034) ;
- immortalisation par SV40-LT (EV-C-0044) ;
- cellules souches embryonnaires (EV-C-0054) ;
- substituts animaux non définis : l'extrait d'embryon de poulet reste inférieur au FBS (EV-C-0034) ;
- passage du sans-sérum au produit réellement vendu (EV-C-0004) ;
- viabilité économique (EV-C-0065).

**Reste à inventer** :
- différenciation musculaire sans sérum ni transgène, à forte densité ;
- recyclage du milieu validé chez le poulet ;
- biomasse à densité protéique proche de celle du muscle ;
- structuration épaisse sans support non comestible ;
- données publiques de contamination et de rendement à l'échelle industrielle.

---

## 5. Contradictions repérées

1. **Immortalisation spontanée « rare » ou « facile » ?** « Très rare » selon Christman et al. 2006 et Wang et al. 2017 (EV-C-0067, EV-C-0036) ; « facile » pour les fibroblastes de poulet selon Pasitka 2023/2025 (EV-C-0015, EV-C-0019). Ce qui pourrait réconcilier les deux : le type cellulaire (fibroblastes contre préadipocytes ou cellules satellites), la durée de culture, la sélection en suspension et en sérum réduit, et la taille des populations en crise. Aucune source ne donne la fréquence de succès par tentative.
2. **« Sans sérum » à Singapour (janvier 2023) contre FBS dans le dossier FDA de GOOD Meat (mars 2023)** (EV-C-0063 contre EV-C-0007). De même, UPSIDE déclare un procédé sans sérum mais un produit vendu avec sérum (EV-C-0004).
3. **Facteurs de croissance indispensables ou non ?** Believer s'en passe en production (EV-C-0011). Vow, autre fibroblaste aviaire, en utilise deux (EV-C-0023), et le milieu de 2023 de Believer contenait du FGF-2 et de l'insuline (EV-C-0071).
4. **Densité** : 130 × 10⁶ cellules/mL mesurées (EV-C-0017) contre un maximum pratique de 86 × 10⁶ modélisé par Humbird (EV-C-0040). Il faut lire les méthodes de Pasitka (volume, base du « % p/v »).
5. **Perfusion, économie modélisée et réalité** : la TEA de Believer est favorable à la perfusion (EV-C-0018) ; Humbird la juge plus chère que le fed-batch (EV-C-0039) ; et Believer a fermé (EV-C-0065).
6. **« Composition similaire au filet » contre mesures** : le résumé FDA du dossier Believer qualifie la biomasse de « similaire » au filet de poulet, alors que la section composition du même mémo indique moins de protéines et de lipides (EV-C-0013). La mesure sur la caille donne environ moitié moins de protéines (EV-C-0020).
7. **Composition cellulaire modélisée contre mesurée** : ~21 % de protéines implicites chez Humbird contre 9 % mesurés (EV-C-0074).

---

## 6. Lacunes (cherché sans succès)

- Temps de doublement chiffrés de cellules satellites de poulet, a fortiori en milieu sans sérum (requêtes 6, 46, 47).
- Lignée de cellules satellites ou de myoblastes de poulet immortalisée par TERT/CDK4 et publiée (requête 7). UPSIDE en déclare une (TERT), sans publication.
- Milieu de différenciation myogénique sans sérum pour le poulet.
- Volumes de production, densités industrielles, taux de contamination et durée de cycle réels (tous confidentiels).
- Pourcentage de cellules dans les produits vendus : on ne dispose que des déclarations des entreprises (GOOD Meat 3 : 3 % ; Chick Bites : 4 %). Aucun document réglementaire ne le donne, et la base (biomasse humide ?) n'est pas précisée.
- Mesures de texture et données sensorielles quantitatives sur du poulet cultivé.
- Données de transfert d'O₂ et de consommation d'O₂ par cellule de poulet en bioréacteur.
- Recyclage du milieu appliqué à des cellules de poulet.
- Littérature chinoise sur le poulet (CNKI bloqué) ; aucun article de Jiangnan ou de Nanjing sur le poulet n'a été repéré.

---

## 7. Pistes d'innovation

### I-1. Densifier la biomasse en protéines avant récolte
- **Problème** : la biomasse aviaire récoltée ne contient qu'environ 9 % de protéines (EV-C-0020), ce qui double le coût par kg de protéine (EV-C-0074).
- **Solutions actuelles** : déshydratation partielle (« moisture adjustment » chez UPSIDE, SRC-C-0001 p. 12) et mélange avec des protéines végétales (EV-C-0016).
- **Insuffisances** : la déshydratation n'ajoute pas de protéines ; les produits hybrides diluent les cellules jusqu'à 4 % (Q-C-0069).
- **Indices en faveur d'une autre approche** :
  - UPSIDE signale une hypertrophie cellulaire pendant sa phase de différenciation (SRC-C-0001 p. 11) ;
  - la voie mTOR est activée à 41 °C (EV-C-0033) ;
  - les fibroblastes sécrètent du collagène (1,59 µg/mg, EV-C-0027).
- **Hypothèse** : une phase de « maturation » courte (24–72 h), sans division, en milieu enrichi en acides aminés essentiels à 41 °C, augmente la teneur en protéines de la biomasse humide de fibroblastes de poulet immortalisés.
- **Expérience** : lignée DF-1 adaptée à la suspension sans sérum ; comparer récolte directe et maturation de 24, 48 et 72 h. Mesurer protéines (Kjeldahl), humidité, collagène (hydroxyproline), viabilité et taille cellulaire.
- **Critères** :
  - succès : au moins 13 g de protéines/100 g humides ;
  - échec : moins de 10 g, ou perte de masse au-delà de 10 %.
- **Coûts et risques** : faibles (paillasse, ~1 mois) ; risque que l'eau interstitielle domine la mesure.

### I-2. Exploiter la température physiologique du poulet en perfusion
- **Problème** : les protocoles hérités des mammifères (37 °C) sous-optimisent les cellules de poulet (EV-C-0033).
- **Insuffisances** : à 41 °C, la consommation d'O₂ augmente alors que la solubilité de l'O₂ diminue (hypothèse non mesurée), ce qui pourrait annuler le gain en cuve.
- **Hypothèse** : en perfusion avec oxygénation contrôlée, la productivité volumique des fibroblastes de poulet est plus élevée à 39–41 °C qu'à 37 °C.
- **Expérience** : bioréacteurs de 1–2 L en perfusion à 37, 39 et 41 °C. Mesurer le taux de croissance, la consommation spécifique d'O₂, la production d'ammoniac et de lactate, la densité maximale et le coût de milieu par kg.
- **Critères** :
  - succès : productivité au moins 20 % plus élevée, sans hausse du NH₃ produit par cellule ;
  - échec : limitation en O₂ ou perte de viabilité.
- **Coûts** : modérés.

### I-3. Recycler le milieu de cellules de poulet en boucle fermée
- **Problème** : le milieu pèse 55–95 % du coût selon une estimation citée (Q-C-0064).
- **Insuffisance actuelle** : la régénération décrite par Believer n'a jamais été utilisée en production (EV-C-0012).
- **Indices** : élimination de plus de 82 % de l'ammoniac par strippage (EV-C-0060) ; seulement ~26 % des acides aminés consommés (EV-C-0062).
- **Hypothèse** : une boucle de perfusion avec élimination en ligne de l'ammoniac et réajustement du glucose et de la glutamine permet de réutiliser au moins 50 % du milieu pendant 20 jours sans perte de croissance chez les fibroblastes de poulet sans sérum.
- **Expérience** : 2 bioréacteurs en parallèle (témoin et recyclage), suivi du métabolome du milieu, de la croissance, du caryotype et des métaux lourds (cf. EV-C-0005).
- **Critères** :
  - succès : au moins 30 % de milieu frais en moins par kg, à croissance égale (± 10 %) ;
  - échec : accumulation d'inhibiteurs non identifiés.

### I-4. Co-culture fibroblastes–cellules satellites comme source endogène de facteurs de croissance
- **Problème** : le muscle de poulet différencié dépend du sérum (EV-C-0034).
- **Insuffisances** : facteurs recombinants coûteux (EV-C-0072) ; MyoD = modification génétique (EV-C-0027).
- **Indices** : les fibroblastes DF-1 améliorent la prolifération et la différenciation des cellules musculaires sur microporteurs (EV-C-0058) ; IntegriCulture revendique une approche par co-culture d'organes (EV-C-0045, non vérifiée).
- **Hypothèse** : un milieu conditionné par des fibroblastes de poulet immortalisés, ou une co-culture 1:1, remplace au moins 80 % du sérum de cheval nécessaire à la fusion des cellules satellites de poulet.
- **Expérience** : indice de fusion à 5 jours en milieu défini + milieu conditionné, comparé à 2 % de sérum de cheval.
- **Critères** :
  - succès : indice de fusion au moins égal à 80 % de celui du témoin ;
  - échec : moins de 50 %.
- **Coûts** : faibles.

*Lien avec les autres voies (RQ-X3)* : les pistes I-1 et I-3 posent la question du coût des acides aminés de qualité alimentaire, celle que rencontre l'aliment volaille (voie A, agent N). Humbird propose un hydrolysat de soja dont le profil en acides aminés essentiels est proche des besoins cellulaires [M] (SRC-E-0001).

---

## 8. Recherches restantes (prioritaires)

1. Obtenir le texte intégral de Pasitka 2023 et 2024 (méthodes : volume, base du « % p/v », composition des milieux, temps de doublement), par prépublication, version auteur ou bibliothèque.
2. Lire les annexes non confidentielles des dossiers FDA (« disclosable safety narrative » de CCC 000039, Parts 1 à 4) pour les compositions chiffrées.
3. Rechercher dans CNKI/Wanfang les travaux chinois sur le poulet (鸡 细胞培养肉, 鸡胚成纤维细胞 永生化), notamment à Jiangnan et à Nanjing.
4. Trouver des mesures de consommation d'O₂, de NH₃ et de lactate par cellule pour les fibroblastes et cellules satellites de poulet, à défaut chez la caille (QM7).
5. Faire un suivi des produits et dossiers : composition déclarée à l'USDA-FSIS (étiquetage), dossiers déposés au Royaume-Uni et dans l'UE, statut de l'usine de Believer et d'UPSIDE.
