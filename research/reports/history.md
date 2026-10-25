# Histoire de l'alimentation des poules : de la domestication à l'industrie, et ce que le passé peut encore apprendre

**Agent H — rapport de domaine (brouillon de phase 3–4), 2026-10-25**
Questions traitées : RQ-H1 à RQ-H5. Identifiants : sources `SRC-H-…` (et sources d'autres agents réutilisées), affirmations `EV-H-…`, mesures `Q-H-…`.

---

## 1. Périmètre et méthode

**Objet.** Retracer ce que les poules ont mangé et comment on les a nourries ou engraissées, depuis leur domestication jusqu'à la fin du XXe siècle, en séparant strictement :
- les **preuves historiques documentées** (textes d'époque lus, mesures archéologiques) ;
- les **reconstitutions** (synthèses modernes à partir de données indirectes) ;
- les **hypothèses**.
Le but est aussi de repérer des pratiques abandonnées qui mériteraient d'être testées à nouveau.

**Bases et outils.** J'ai interrogé :
- Europe PMC (texte intégral libre), PubMed et Crossref (avec un client local, car `search.py crossref` renvoie une erreur 400) ;
- archive.org (recherche et texte OCR intégral), LacusCurtius et remacle.org pour les agronomes latins ;
- Wikisource chinois pour le 齊民要術, et legislation.gov.uk pour les textes européens (EUR-Lex inaccessible pendant la session) ;
- J-STAGE et HAL, Google Patents (page de brevet), WebSearch et WebFetch.

Le journal (`research/agents/H/search_log.md`) compte 86 lignes et plus de 100 requêtes en 11 langues : en, fr, la, zh, es, pt, ja, de, hi, ar et el (via la traduction des Géoponiques). Il inclut des recherches ciblées de résultats négatifs ou contraires : risques des verminières, effets négatifs des aliments fermentés et du lactosérum, faible effet résiduel des antibiotiques facteurs de croissance, controverses de datation.

**Bilan d'enregistrement.**

| Élément | Nombre | Détail |
|---|---|---|
| Sources | 53 | 20 lues en texte intégral, 18 en partie, 9 en résumé seul, 6 en métadonnées seules |
| Affirmations | 66 | 36 `historical_documented`, 8 reconstitutions, 1 hypothèse explicite, plus essais modernes, textes réglementaires, modèles |
| Mesures | 63 | Surtout `scale=historical`, `data_nature=historical_record` ; aussi mesures isotopiques archéologiques et quelques données modernes |

**Limites d'accès.**
- Pages bloquées (403) : JBC (Hart et al. 1922–1925 ; Moore et al. 1946), ScienceDirect (Castanon 2007), conférence Nobel d'Eijkman, PDF japonais (SBJ). Pour ces documents, je n'ai que les métadonnées ou le résumé.
- EUR-Lex répond par une page vide (défi JavaScript).
- Pas d'accès à CNKI : la littérature savante chinoise sur l'histoire de l'aviculture n'a pas été trouvée. Seul le texte primaire a été lu.
- Columelle VIII n'est pas en ligne sur LacusCurtius ; je l'ai lu dans l'édition bilingue Du Bois (1846).
- Les textes anciens ont été lus en traduction, sauf Caton, Columelle et le 齊民要術, lus aussi dans la langue originale.
- La recherche archive.org ne porte que sur les métadonnées. Le repérage des verminières a donc demandé de télécharger puis d'explorer le texte de chaque traité.

---

## 2. État des connaissances par question

### RQ-H1 — Que mangeaient les premières volailles domestiques ?

**Ce qui est établi.**

*Date et lieu des premiers poulets.*
- La synthèse archéozoologique la plus complète réexamine environ 600 sites. Elle place les premiers os de poulets domestiques non ambigus à Ban Non Wat (Thaïlande), vers 1650–1250 av. J.-C. (EV-H-0001, SRC-H-0001).
- Les poulets n'arrivent en Chine centrale, en Asie du Sud et en Mésopotamie qu'à la fin du IIe millénaire av. J.-C.
- Les « poulets » néolithiques de Chine du Nord (Dadiwan, 7900–5900 cal BP) sont en réalité des faisans (identification par ADN mitochondrial). Ils étaient nourris en partie de millets cultivés : δ13C de −17,6 à −14,2 ‰ (EV-H-0004, Q-H-0053). Ce résultat renverse l'ancienne hypothèse d'une domestication précoce en Chine du Nord.

*Statut des premiers poulets d'Europe.*
- Les datations radiocarbone directes repoussent leur arrivée au Ier millénaire av. J.-C.
- Ils étaient d'abord des « exotica » non consommés : squelettes complets, sans traces de découpe. On ne les mange que plusieurs siècles plus tard (EV-H-0003, SRC-H-0007).
- Conséquence : l'alimentation des premières volailles n'était pas organisée pour produire de la viande.

**Hypothèse (non démontrée).**
- La culture et le stockage du riz et du millet auraient attiré le coq bankiva dans la niche humaine. La domestication aurait donc été commensale, fondée sur les grains et déchets agricoles (EV-H-0002).
- La diffusion ultérieure du poulet suit celle des céréales : en Éthiopie vers 800–600 av. J.-C., puis en Afrique de l'Est avec le riz et le haricot mungo, et dans le bassin du Niger entre 300 et 900 ap. J.-C. (EV-H-0066).
- C'est une corrélation spatio-temporelle. Il n'existe **aucune donnée isotopique** sur les premiers poulets d'Asie du Sud-Est (lacune majeure).

**Isotopes du collagène : une alimentation régionalement diverse.** Ces mesures sont directes (`data_nature=measured`).

| Site et période | δ13C | δ15N | Interprétation |
|---|---|---|---|
| Pompéi, avant 79 ap. J.-C. (n = 5 ; EV-H-0005, Q-H-0048/0049) | −16,8 ‰ en moyenne (porcs −20,4 ‰) | — | Signal enrichi, régime distinct, compatible avec le millet que recommandent Columelle et les Géoponiques (EV-H-0012, EV-H-0023) |
| Catalogne ibère et romaine (EV-H-0006, Q-H-0050/0051) | −19,8 ‰ (C3) | 8,0 ‰ | Régime d'omnivores : végétaux C3 plus protéines animales (restes, invertébrés) |
| Aqaba ottomane, XVIe–XIXe s. (SRC-H-0006, Q-H-0052) | −16,5 ‰ | 8,9 ‰ | δ2H bas, compatible avec un abreuvement par eau de puits |
| Old Bara, empire d'Oyo (EV-H-0007) | — | — | Céréales C4 (sorgho, millet ou maïs), comme les humains et les chevaux |

**Amériques précolombiennes : question ouverte.**
- L'os d'El Arenal-1 (Chili) a été présenté comme une preuve d'introduction polynésienne (SRC-H-0008).
- Il a été contesté : contamination de l'ADN, possible effet réservoir marin (SRC-H-0009), absence d'haplotypes polynésiens dans les échantillons sud-américains (SRC-H-0010).
- La défense invoque un δ13C de −20,9 à −19,45 ‰ et un δ34S terrestre : régime terrestre pauvre en protéines, avec peut-être un peu de maïs (EV-H-0008, Q-H-0054).
- Côté alimentation, les rares données disponibles décrivent donc un oiseau nourri de grains terrestres.

### RQ-H2 — Pratiques documentées dans les textes anciens

**Rome.** Les trois agronomes latins décrivent un système cohérent. Les textes ont été lus.

*Caton (~160 av. J.-C.)* : gavage de jeunes poules enfermées, avec des boulettes de farine ou de farine d'orge trempées, deux fois par jour (EV-H-0009).

*Varron (~37 av. J.-C.)*
- Poulailler commercial de 200 poules.
- Poussins nourris 15 jours d'orge et de graine de cresson pré-humidifiées (EV-H-0011, Q-H-0003).
- Engraissement dans un local chaud, étroit et obscur, car « le mouvement et la lumière » empêchent d'engraisser.
- Boulettes d'orge (± ivraie ou lin) pendant 25 jours, ou pain de froment trempé dans l'eau et le vin pendant 20 jours (EV-H-0010, Q-H-0001/0002).

*Columelle (~60 ap. J.-C.)*
- Il hiérarchise les aliments selon le prix (*vilitas annonae*) : orge concassée, vesce, cicérole, millet, panic. À défaut : criblures de blé, ivraie cuite, son, cytise, marc de raisin hors ponte (EV-H-0012).
- C'est une **formulation au moindre coût qualitative**, dix-neuf siècles avant la programmation linéaire.
- Il fixe des rations : 4 cyathes par jour pour une poule enfermée, 2–3 pour une poule en liberté (EV-H-0013, Q-H-0005/0006).
- Il décrit l'épinette : cage ou panier suspendu où l'oiseau ne peut se retourner, local chaud et sombre, 20 jours, jamais plus de 25 (EV-H-0014, Q-H-0007).

*Pline* rapporte deux faits (EV-H-0015) :
- la loi Fannia (161 av. J.-C.) interdisait de servir des poules engraissées ;
- on la contournait en engraissant de jeunes coqs avec des aliments trempés dans le lait : **première attestation retrouvée de la finition lactée**.

**Méditerranée orientale, monde byzantin et arabo-andalou.**

*Géoponiques (Xe s., livre XIV)*
- Elles reprennent l'engraissement à l'obscurité, mais disent que « la plupart » nourrissent au millet.
- Elles limitent l'effectif à 40 poules par poulailler (EV-H-0023, Q-H-0009).
- Surtout, elles décrivent une **production de vers pour les poussins** : levain d'orge, son et eau, avec du crottin d'âne ou de cheval ; des vers apparaissent en trois jours (EV-H-0022, Q-H-0010).

*Ibn al-ʿAwwām (Séville, fin XIIe s.)*
- Il recopie cette « vermière » (EV-H-0024) et l'incubation dans le crottin.
- Il élargit la gamme des aliments d'engraissement : légumes cuits, sorgho (*doura*) avec son, riz, oignon et poireau (EV-H-0025).
- Il note que les fèves données en continu rendent les pondeuses stériles (EV-H-0026). Ce savoir empirique serait à confronter aux effets connus des facteurs antinutritionnels de la féverole (question pour l'agent N).

**Chine.** Le 齊民要術 (Jia Sixie, ~544) a été lu en chinois classique (EV-H-0027 à EV-H-0029).
- Engraissement rapide en enclos, ailes rognées, avec grains vides, panic et fèves.
- Pour la table : blé cuit à la vapeur, 21 jours (Q-H-0012).
- Cages au sol à plancher à claire-voie (棧), qui rendent les oiseaux calmes et faciles à engraisser.
- Pondeuses séparées des coqs, gavées de grain : « plus de cent œufs » (Q-H-0013).
- Poussins nourris de grain cuit **sec**, l'humide étant réputé causer des infections ombilicales.
- Le texte cite le 《家政法》, plus ancien : on laboure un mou de terre, on l'arrose de bouillie de millet glutineux et on le couvre d'herbe coupée ; des « vers blancs » y naissent, puis on y installe dix poules et un coq (Q-H-0015). C'est une **verminière de plein champ**, apparemment indépendante de la tradition gréco-arabe.

**Égypte : l'incubation industrielle avant l'industrie.**
- Pline mentionne l'éclosion dans les fumiers d'Égypte (EV-H-0065).
- Réaumur (1749) rapporte, d'après le P. Sicard (EV-H-0016) :
  - 386 fours (*mamals*) conduits par des spécialistes du village de Bermé (Q-H-0016) ;
  - fours chauffés à la bouse ou à la fiente séchée ;
  - environ 8 couvées par saison de 40 000 à 50 000 œufs (Q-H-0017/0018) ;
  - un contrat de deux tiers d'éclosion (Q-H-0019).
- Réaumur en déduit plus de 92 millions de poussins par an. C'est une estimation par calcul, pas un recensement (Q-H-0020).

### RQ-H3 — Systèmes traditionnels (Afrique, Amériques, Asie, Moyen-Orient)

**La divagation est la norme pré-industrielle.** Jusqu'au XXe siècle, les volailles vivaient surtout de la ressource de divagation. On n'y ajoutait du grain que lorsque l'effectif la dépassait (EV-H-0054). Les rares mesures montrent que :
- **Sri Lanka** : un troupeau villageois ingère environ 550 g de matière sèche par jour, à 9,4 % de protéines brutes. Plus de 70 % viennent de **déchets ménagers** (riz cuit, résidu de noix de coco, brisures) ; les petits invertébrés ne font que 8 % (EV-H-0049, Q-H-0040 à Q-H-0042). Les poussins pèsent 313 g à 70 jours et la mortalité atteint 65 % (Q-H-0043).
- **Mexique (Michoacán)** : sur 36,4 g de contenu du jabot, le maïs et le sorgho comptent pour 13,9 g, l'aliment commercial pour 8,1 g et les insectes pour seulement 0,3 g. Les régimes ne couvrent pas les besoins (EV-H-0050, Q-H-0044 à Q-H-0046).
- **Kenya** : la ponte passe d'environ 40 œufs par an en divagation à 120 en élevage intensif (EV-H-0053, Q-H-0047). L'alimentation, la génétique et la santé y sont confondues.

**Les insectes d'appoint, pratique vivante en Afrique.**
- Nourrir les poussins de termites est très répandu en Afrique subsaharienne (EV-H-0051).
- La « semi-domestication » des termites consiste à retourner sur une galerie de termitière un canari (jarre d'argile) contenant des résidus de culture humidifiés. On récolte après 3–4 semaines (Q-H-0037).
- Au Ghana, 23 % des éleveurs donnent « toujours » des termites, 19 % « souvent », 11 % jamais. L'usage baisse avec la scolarisation (EV-H-0052, Q-H-0038/0039). Environ 78 % des éleveurs du Burkina Faso en donnent au moins occasionnellement (chiffre cité).
- Une méthode du même type (pot à termites) est signalée en Inde (Tamil Nadu), mais seulement par la presse (journal).

**Lacunes de cette question.**
- Je n'ai trouvé **aucune source historique** sur l'usage traditionnel de l'azolla ou des lentilles d'eau pour les poulets (Vietnam, Chine). Les études modernes relèvent de l'agent N.
- Rien non plus sur l'intégration poulet-pisciculture, ni sur la galinha caipira coloniale : seulement de la vulgarisation de l'Embrapa.

### RQ-H4 — Chronologie de l'industrialisation (1890–2006)

Voir le tableau chronologique (§ 3). Points saillants :

1. **Vitamines.** La poule a servi de modèle à la première carence découverte : la polynévrite des poules nourries au riz poli, observée par Eijkman à Batavia (EV-H-0037). La vitamine D (huile de foie de morue) a ensuite supprimé la faiblesse des pattes et permis l'élevage en bâtiment (EV-H-0038). Ce dernier point n'est vérifié ici que par une source secondaire ; les articles du Wisconsin (SRC-H-0025) n'ont pas pu être lus.
2. **Protéines végétales.** L'effet du chauffage sur le tourteau de soja est étudié dès 1936 (EV-H-0064, métadonnées). Le passage au soja révèle de nouvelles contraintes minérales : il faut ajouter 25 ppm de zinc à un régime de soja dans les années 1950 (EV-H-0062). Les premiers essais de phytase fongique datent de 1968–1971 (EV-H-0063). La date de la première phytase **commerciale** (souvent citée : 1991) **n'a pas été vérifiée**.
3. **Génétique.** Le concours « Chicken of Tomorrow » (1948) marque le début de la sélection spécialisée chair (EV-H-0039, source secondaire). L'agent N quantifie ses effets :
   - indice de consommation (IC) des États-Unis : 4,7 en 1925, 1,70 en 2025 (EV-N-0010, Q-N-0016/0017) ;
   - croissance multipliée par plus de 4 entre une souche de 1957 et une Ross 308 de 2005 recevant le même régime (EV-N-0001).
4. **Antibiotiques facteurs de croissance (AGP).**
   - 1946 : la streptomycine stimule la croissance du poussin (EV-H-0040).
   - Retraits : Suède 1986, UE 1995–1999 pour cinq molécules, interdiction totale le 1er janvier 2006 (EV-H-0041).
   - Résultat négatif instructif : au Danemark, l'arrêt de 1998 n'a changé ni la production par m² ni la mortalité, et l'IC n'a augmenté que de 0,016 (EV-H-0042, Q-H-0055).
5. **Acides aminés de synthèse.**
   - DL-méthionine (Degussa) : synthèse en 1946/47, autorisation en alimentation animale en Allemagne en 1953 (EV-H-0043, communication d'entreprise).
   - L-lysine par fermentation : brevet Kyowa Hakko de 1958, 6–20 g/L (EV-H-0044, Q-H-0057), après la découverte de la fermentation du glutamate en 1956.
   - Cette microbiologie industrielle est la même que celle mobilisée pour les milieux de culture (voie B).
6. **Formulation au moindre coût.** La programmation linéaire est appliquée pour la première fois par Waugh (1951) à un aliment pour **vaches laitières** (EV-H-0045). La date de la première formulation publiée pour volailles n'a pas été retrouvée.
7. **Réglementation européenne.**
   - Farines animales interdites pour tous les animaux d'élevage au 1er janvier 2001 (EV-H-0046).
   - Eaux grasses et recyclage intra-espèce interdits en 2002, maintenus en 2009 (EV-H-0047).
   - Réautorisation des protéines d'insectes pour volailles en 2021 (EV-E-0029, SRC-E-0017, agent E).

### RQ-H5 — Innovations oubliées ou abandonnées

**1. La verminière, production délibérée de larves pour les volailles.** C'est la découverte majeure de la mission. Elle est documentée dans trois traditions au moins :
- gréco-byzantine : Géoponiques, EV-H-0022 ;
- reprise arabo-andalouse : Ibn al-ʿAwwām, EV-H-0024 (source dépendante) ;
- chinoise, apparemment indépendante : 《家政法》 dans le 齊民要術, EV-H-0027.

En France, elle est recommandée au XVIIIe siècle et industrialisée en fosse au XIXe :
- Réaumur conseille de verser du sang de bœuf sur les fumiers, d'y jeter des chairs corrompues, de collecter les larves de scarabées des couches maraîchères (EV-H-0020) ;
- Gobin (1882) décrit une fosse d'un mètre garnie de sang d'abattoir, de marc et de viande d'équarrissage, avec des larves au bout d'un mois (EV-H-0030, Q-H-0036).

Elle est **abandonnée pour des raisons documentées** :
- coût, odeur, insalubrité, goût de la chair et des œufs ;
- picage lorsqu'on supprime la nourriture animale (EV-H-0032) ;
- inadaptée à l'élevage et à l'engraissement, seulement utile à la ponte (EV-H-0031).

Un risque sanitaire non nommé à l'époque est plausible : le cycle cadavre–mouche–asticot du botulisme aviaire (EV-H-0059 ; extrapolation, confiance faible). Le droit européen interdit aujourd'hui de nourrir les animaux d'élevage avec des déchets de cuisine. Il tolère des asticots nourris de sous-produits animaux… pour la pêche (EV-H-0047).

**2. La finition lactée.** Elle est attestée de Rome (EV-H-0015) aux XIXe et XXe siècles :
- La Flèche : environ 40 jours, 30 litres de mouture par tête (moitié sarrasin), délayée au lait écrémé ou au petit-lait (EV-H-0034, Q-H-0033/0034) ;
- Sussex : gavage mécanique au lait écrémé, surplus des laiteries (EV-H-0055) ;
- Bresse : préférence pour le petit-lait (EV-H-0056).

Données d'époque :
- un poulet de 750 g double en 18 jours avec environ 11 kg d'aliment frais (lait compris) par kg de viande (EV-H-0033, Q-H-0029/0030) ;
- un avertissement empirique : pas plus de moitié de lait (EV-H-0035).

Un essai moderne confirme une **réponse dose-dépendante** : 25 g/kg de lactosérum acide de yaourt sont sans effet négatif sur la croissance et améliorent la stabilité oxydative du filet ; 50–100 g/kg réduisent la croissance (EV-H-0057, Q-H-0061).

**3. Les grains cuits, pré-humidifiés ou fermentés.**
- Constants dans les textes : pâtée humide de Varron, blé à la vapeur du 齊民要術.
- Réaumur mesure une baisse d'ingéré (en équivalent grain sec) de 2/5 pour l'orge cuite, de 1/5 pour le froment, de plus de la moitié pour le maïs. L'avoine et le sarrasin n'en profitent pas (EV-H-0018, Q-H-0023 à Q-H-0025). Ce sont des mesures de satiété, pas de performance.
- Les aliments fermentés modernes donnent des **résultats contradictoires** : moindre ingestion et moindre croissance au démarrage, perte de lysine libre (EV-H-0058).

**4. Les eaux grasses.**
- Interdites dans l'UE en 2002 après la fièvre aphteuse de 2001.
- Le Japon, la Corée du Sud et Taïwan en ont fait une filière réglementée avec traitement thermique.
- Le gain de surface modélisé pour le porc européen est de 21,5 % (EV-H-0048, Q-H-0056). C'est une extrapolation au poulet, non démontrée.

**5. Les grains germés.** Aucune source historique n'a été trouvée. Un seul essai moderne, de qualité faible, existe : 10 % d'orge hydroponique (EV-H-0060).

---

## 3. Chronologie

| Date / période | Lieu | Pratique ou innovation | Source | Type de preuve |
|---|---|---|---|---|
| 7900–5900 cal BP | Dadiwan (Gansu) | Faisans « appâtés » au millet par les premiers agriculteurs (pas des poulets) | SRC-H-0002 | expérimental (ADN + isotopes) |
| ~1650–1250 av. J.-C. | Ban Non Wat (Thaïlande) | Premiers poulets domestiques non ambigus ; lien supposé avec riz et millet | SRC-H-0001 | reconstitution / hypothèse |
| fin IIe mill. av. J.-C. | Chine centrale, Asie du Sud, Mésopotamie | Arrivée du poulet, liée aux millets et au riz irrigué | SRC-H-0001 | reconstitution |
| ~800–600 av. J.-C. | Éthiopie ; Méditerranée | Arrivée du poulet ; en Europe, d'abord « exotica » non consommés | SRC-H-0001, SRC-H-0007 | datation directe |
| ~160 av. J.-C. | Italie | Gavage de jeunes poules (Caton, chap. 89) | SRC-H-0013 | historique documenté |
| 161 av. J.-C. | Rome | Loi Fannia ; finition au lait pour la contourner | SRC-H-0015 | historique documenté (rapporté) |
| ~37 av. J.-C. | Italie | Poulailler de 200 poules ; engraissement à l'obscurité 20–25 j (Varron) | SRC-H-0012 | historique documenté |
| ~60 ap. J.-C. | Italie | Hiérarchie des aliments selon le prix ; rations ; épinette (Columelle) | SRC-H-0014 | historique documenté |
| avant 79 ap. J.-C. | Pompéi | Poulets à signal isotopique C4 (millet ?) distinct des autres animaux | SRC-H-0003 | mesure archéologique |
| ~77 ap. J.-C. | Égypte (selon Pline) | Éclosion dans les fumiers | SRC-H-0015 | historique documenté |
| ~544 | Chine du Nord | 齊民要術 : cages, blé à la vapeur 21 j ; 家政法 : production de « vers blancs » | SRC-H-0023 | historique documenté |
| VIIIe–IXe s. | Afrique de l'Est, Madagascar | Poulets diffusés avec le riz et le haricot mungo | SRC-H-0001 | reconstitution |
| Xe s. (sources antérieures) | Byzance | Géoponiques : millet, ≤ 40 poules/poulailler, vers pour poussins, incubation dans la fiente | SRC-H-0018 | historique documenté |
| fin XIIe s. | Séville | Ibn al-ʿAwwām : vermière, sorgho, effets des fèves | SRC-H-0019 | historique documenté (dépendant) |
| XVIIe–XIXe s. | Oyo (Nigeria) ; Aqaba | Poulets nourris de céréales C4 ; abreuvés à l'eau de puits | SRC-H-0005, SRC-H-0006 | mesure archéologique |
| ~1700–1749 | Égypte (selon Sicard) | 386 fours d'éclosion, ~8 couvées de 40 000–50 000 œufs | SRC-H-0016 | historique documenté (rapporté) |
| 1749–1750 | France | Réaumur : mesures d'ingéré, grains cuits, insectes, incubation au fumier | SRC-H-0016, SRC-H-0017 | historique documenté (expérimental d'époque) |
| 1858–1882 | France | Verminières en fosse ; critiques (odeur, goût, picage) ; ration de 80 g/j | SRC-H-0020 à SRC-H-0022 | historique documenté |
| 1864–1895 | France, Angleterre | Finition lactée (La Flèche, Bresse, Sussex) ; gavage mécanique | SRC-H-0021, SRC-H-0046 | historique documenté |
| fin années 1880–1890 | Java | Eijkman : polynévrite des poules au riz poli | SRC-H-0024 | reconstitution (biographie) |
| 1922–1925 | Wisconsin | Série sur les besoins des poussins (vitamine D, lumière) | SRC-H-0025 (métadonnées), SRC-H-0035 | reconstitution |
| 1936 | États-Unis | Effet du chauffage sur le tourteau de soja | SRC-H-0053 (métadonnées) | historique documenté (titre) |
| 1946 | Wisconsin | Streptomycine et croissance du poussin | SRC-H-0026, SRC-H-0028 | reconstitution |
| 1946–1953 | Allemagne | DL-méthionine : synthèse, puis autorisation fourragère (1953) | SRC-H-0031 | communication d'entreprise |
| 1948 | États-Unis | Concours « Chicken of Tomorrow » | SRC-H-0035 | reconstitution |
| 1950 | États-Unis | « Animal protein factor », auréomycine | SRC-H-0027 (métadonnées) | historique documenté (titre) |
| 1951 | États-Unis | Programmation linéaire pour un aliment laitier (Waugh) | SRC-H-0034 | historique documenté (titre) |
| 1956–1958 | Japon | Fermentation du glutamate ; brevet lysine (Kyowa Hakko) | SRC-H-0033, SRC-H-0032 | brevet |
| 1957–2005 | Amérique du Nord | Gains génétiques mesurés sur souches d'époque | SRC-N-0001, SRC-N-0002 | expérimental (agent N) |
| 1968–1971 | États-Unis | Premiers essais de phytase fongique chez le poussin | SRC-H-0051, SRC-H-0052 | reconstitution |
| 1986 ; 1995–1999 ; 2006 | Suède ; UE | Retraits puis interdiction totale des AGP | SRC-H-0028, SRC-H-0029, SRC-N-0025 | réglementaire |
| 1998 | Danemark | Arrêt volontaire des AGP : IC +0,016 seulement | SRC-H-0030 | statistique |
| 1er janvier 2001 | UE | Interdiction des protéines animales transformées pour les animaux d'élevage | SRC-H-0036 | réglementaire |
| 2002 (2009) | UE | Interdiction des eaux grasses et du recyclage intra-espèce | SRC-H-0037, SRC-H-0038 | réglementaire |
| 1997 ; 2003 ; 2009 | Corée du Sud ; Taïwan ; Japon | Filières réglementées de recyclage des déchets alimentaires en aliment | SRC-H-0039 ; terminologie (エコフィード) | reconstitution |
| 2021 | UE | Protéines d'insectes réautorisées pour volailles et porcs | SRC-E-0017 (agent E) | réglementaire |

---

## 4. Tableaux quantitatifs

### 4.1 Rations, durées et rendements historiques

Toutes ces valeurs sont `scale=historical`, `data_nature=historical_record`, sauf mention contraire.

| Paramètre | Valeur | Contexte | ID |
|---|---|---|---|
| Ration, poule enfermée / en liberté | 4 / 2–3 cyathes par jour | Columelle | Q-H-0005, Q-H-0006 |
| Durée d'engraissement | 20–25 j | Varron, Columelle | Q-H-0001, Q-H-0002, Q-H-0007 |
| Durée d'engraissement | 21 j (blé à la vapeur) | 齊民要術 | Q-H-0012 |
| Durée d'engraissement | ~40 j | La Flèche | Q-H-0033 |
| Durée d'engraissement | ~21 j | Sussex | Q-H-0063 |
| Ingéré volontaire d'hiver | 1/4 litron/j (orge, avoine, sarrasin) | Réaumur | Q-H-0021 |
| Orge annuelle d'une poule confinée | 6 boisseaux (≈ 3 livres 15 sous) ; rentable au-delà de 75 œufs | Réaumur | Q-H-0026, Q-H-0027 |
| Orge pour une basse-cour divagante | 1 boisseau d'orge cuite par jour pour ~300 volailles | Réaumur | Q-H-0028 |
| Économie de grain par cuisson | orge 0,4 ; froment 0,2 ; maïs > 0,5 | Réaumur | Q-H-0023 à Q-H-0025 |
| Ration pondeuse en liberté limitée | 80 g de grain sec/j | France ~1880 | Q-H-0035 |
| Gain à l'engraissement lacté | 750 → 1 500 g en 18 j ; ~11 kg d'aliment frais par kg | ~1860 | Q-H-0029, Q-H-0030 |
| Rapport os/viande | 17 % (maigre) / 9 % (gras) | Gayot | Q-H-0031, Q-H-0032 |
| Poids moyen à l'engraissement | 4,97 → 6,91 lb en 14 j (24 oiseaux) | 1894 | Q-H-0059, Q-H-0060 |
| Délais de production d'insectes | vers : 3 j (vermière) ; larves : 30 j (fosse) ; termites : 21–28 j (canari) | Géoponiques ; Gobin ; Afrique | Q-H-0010, Q-H-0036, Q-H-0037 |
| Fours d'Égypte | 386 fours ; 8 couvées ; 40 000–50 000 œufs ; 2/3 d'éclosion ; 92,6 millions (estimation) | Réaumur | Q-H-0016 à Q-H-0020 |

Mise en perspective : l'IC national des États-Unis est de 4,7 en 1925 et de 1,70 en 2025 (agent N, Q-N-0016/0017). Les **≈ 11 kg/kg** de 1860 ne sont pas comparables : ils sont exprimés en masse fraîche avec du lait, sur une finition seule.

### 4.2 Régimes réels mesurés

| Système | Mesure | Valeur | ID |
|---|---|---|---|
| Pompéi | δ13C / δ15N | −16,8 / 5,9 ‰ | Q-H-0048, Q-H-0049 |
| Catalogne ibère et romaine | δ13C / δ15N | −19,8 / 8,0 ‰ | Q-H-0050, Q-H-0051 |
| Aqaba ottomane | δ13C | −16,5 ‰ | Q-H-0052 |
| Village, Sri Lanka | MS ingérée par troupeau | 550 g/j ; 9,4 % PB ; > 70 % déchets | Q-H-0040 à Q-H-0042 |
| Traspatio, Mexique | jabot | 36,4 g, dont insectes 0,3 g | Q-H-0044 à Q-H-0046 |
| Kenya, divagation | ponte | 40 œufs/an | Q-H-0047 |
| Ghana | éleveurs donnant « toujours » des termites | 23 % | Q-H-0038 |

---

## 5. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Ce qui a fonctionné de façon répétée** (convergence de traditions indépendantes) :
- **Claustration, obscurité et repos pour la finition.** Ces principes reviennent à Rome, à Byzance, en al-Andalus, en Chine et en France. La durée efficace est de 2–3 semaines, et le rendement décroît après environ 14 jours (EV-H-0061).
- **Céréales cuites ou pré-humidifiées.** Elles étaient utilisées pour les poussins et pour la finition.
- **Substitution des aliments selon le prix.** Columelle et Réaumur raisonnent déjà ainsi.
- **Valorisation de coproduits.** Son, criblures, marc, lait écrémé et petit-lait, déchets ménagers étaient tous mobilisés.

**Ce qui a échoué ou a été abandonné :**
- **Verminières.** Hygiène, odeur, goût, travail et picage les ont condamnées (EV-H-0032). C'est la technologie qui manquait (contrôle du substrat, de l'hygiène et de la récolte), pas le principe.
- **Eaux grasses.** Elles sont abandonnées pour le risque d'épizootie, non pour des raisons nutritionnelles (EV-H-0048).
- **Farines animales.** Leur abandon est dû au risque d'ESB (EV-H-0046).
- **AGP.** Leur abandon tient à l'antibiorésistance. Leur bénéfice était devenu marginal dans un élevage moderne (EV-H-0042).

**Ce qui reste à inventer :**
- une bioconversion des déchets en insectes qui soit sûre et auditable : substrats aujourd'hui interdits, comme les déchets de cuisine ;
- une finition à base de coproduits laitiers à dose optimale pour les souches modernes ;
- une transformation des céréales (cuisson ou fermentation) qui n'entraîne pas de perte d'acides aminés.

---

## 6. Contradictions repérées

- **Régime des poulets romains.** Pompéi présente un signal C4 (millet ?) (EV-H-0005) ; la Catalogne, un signal C3 avec omnivorie (EV-H-0006). Il ne s'agit pas d'une contradiction stricte, mais d'une **diversité régionale**. Le lien `contradicts` saisi au départ entre ces deux lignes a été supprimé avec `kb.py set`.
- **El Arenal.** Les uns invoquent un régime marin qui vieillirait la date et une contamination de l'ADN (SRC-H-0009, SRC-H-0010) ; les autres un régime terrestre et l'absence de contamination (SRC-H-0011). La question n'est pas résolue (EV-H-0008).
- **Verminière.** Réaumur et Gobin la recommandent (EV-H-0020, EV-H-0030) ; Jacque et Gayot la rejettent (EV-H-0032).
- **Termites.** Trinervitermes est réputé tuer les poussins par certains informateurs du Togo et du Burkina (EV-H-0051), alors qu'il est le genre le plus utilisé au Ghana (EV-H-0052).
- **Densité maximale par poulailler.** Les Géoponiques consultées donnent 40 poules ; Ibn al-ʿAwwām, qui les cite, en donne 50 (Q-H-0009 contre Q-H-0011).
- **Gains attribués aux AGP.** Ils sont spectaculaires dans les années 1950 (Hao 2014), mais quasi nuls au Danemark en 1998 (EV-H-0042). L'explication probable tient à des souches, des régimes et une hygiène différents.

---

## 7. Lacunes (cherché sans succès)

- Données isotopiques sur les premiers poulets d'Asie du Sud-Est et de Chine (EPMC sans résultat ; CNKI inaccessible).
- Littérature savante chinoise et japonaise sur l'histoire de l'alimentation des poules. J-STAGE ne renvoyait rien aux requêtes japonaises à plusieurs mots ; après correction de l'outil par le coordinateur, une série historique a été repérée mais pas lue (« わが国畜産研究・技術開発の黎明 », LIVESTOCK TECHNOLOGY 2011–2014).
- Date de la première phytase commerciale, et contexte réglementaire du phosphore.
- Première formulation par programmation linéaire publiée pour les volailles.
- Date de généralisation du tourteau de soja dans les aliments composés.
- Usage historique de l'azolla et des lentilles d'eau pour les poulets.
- Intégration poulet-pisciculture.
- Histoire coloniale de la galinha caipira et des gallinas criollas.
- Grains germés pour volailles dans les traités anciens : aucune occurrence trouvée.
- Lien explicite verminières–botulisme (« limberneck ») dans la littérature avicole de 1900 à 1930.
- Textes originaux non lus : Eijkman, Hart/Steenbock, Moore 1946, Stokstad & Jukes, Farina et al. 1991 (Tropicultura).

---

## 8. Innovations historiques à réévaluer

| Pratique | Période | Pourquoi abandonnée (si documenté) | Intérêt moderne potentiel | Ce qu'il faudrait tester |
|---|---|---|---|---|
| Verminière à poussins (levain d'orge, son, crottin) | Byzance Xe s., al-Andalus XIIe s. (EV-H-0022, EV-H-0024) | Non documenté pour ces périodes | Production locale de larves vivantes pour les premiers jours ; enrichissement comportemental | Rendement en larves par kg de substrat ; charge microbienne ; croissance et picage des poussins à 0–14 j |
| Parcelle à « vers blancs » (bouillie de millet + herbe coupée) | Chine, ≤ VIe s. (EV-H-0027) | Non documenté | Production d'insectes au champ, intégrée aux cultures | Identité des larves ; production par m² ; apport protéique pour 10 poules |
| Verminière en fosse (sang, marc, équarrissage) | France XVIIIe–XIXe s. (EV-H-0020, EV-H-0030) | Odeur, insalubrité, goût, picage, travail (EV-H-0032) ; botulisme probable (EV-H-0059) | Bioconversion par mouche soldat noire de coproduits **autorisés** (voir EV-A-0024, SRC-A-0021) | Analyse comparée historique et moderne : substrats, pathogènes, profil en acides aminés |
| Termites au canari | Afrique, actuelle (EV-H-0051) | Recul avec la scolarisation (EV-H-0052) | Protéines gratuites pour poussins villageois, sans intrant | Production par canari ; toxicité par genre (Trinervitermes) ; mortalité des poussins |
| Finition au petit-lait ou au lait écrémé | Rome → XXe s. (EV-H-0015, EV-H-0034, EV-H-0055) | Spécialisation et coût du travail (gavage) ; non documenté précisément | Valorisation du lactosérum acide (polluant laitier) ; qualité du filet | Dose-réponse 0–50 g/kg en finition (21–35 j) sur souches à croissance lente et rapide (EV-H-0057) |
| Céréales cuites ou vapeur pour économiser le grain | Rome, Chine VIe s., Réaumur 1749 (EV-H-0018, EV-H-0028) | Remplacées par la granulation et l'extrusion industrielles (supposé) | Transformation à la ferme de céréales locales (orge, maïs) | Digestibilité et IC selon le type de cuisson et la céréale ; vérifier l'absence de gain pour l'avoine |
| Pâtée pré-humidifiée ou fermentée | Varron, Columelle | Non documenté | Aliments fermentés, réduction des pathogènes | Fermentation sans perte de lysine (EV-H-0058) |
| Eaux grasses traitées | Universel jusqu'en 2002 | Fièvre aphteuse de 2001 (EV-H-0048) | Réduction de surface (−21,5 % modélisé chez le porc) | Bilan sanitaire et zootechnique pour poulets (Japon, Corée) |
| Hiérarchie des aliments selon le prix (*vilitas annonae*) | Columelle | Remplacée par la programmation linéaire (EV-H-0045) | — (déjà généralisé) | — |

---

## 9. Pistes d'innovation

### Piste H-1 — « Verminière moderne » : larves vivantes produites sur place pour le démarrage des poussins

- **Problème.** Les premiers jours de vie conditionnent la croissance et le comportement. Les aliments de démarrage sont chers et riches en soja. Le picage reste un problème de bien-être.
- **Solutions actuelles.** Farine de larves de mouche soldat noire (BSF) produite en usine. Ses effets globaux sur les performances sont neutres (EV-A-0024).
- **Insuffisances.**
  - La transformation (séchage, broyage) a un coût énergétique.
  - L'impact climatique est élevé si le substrat n'est pas un vrai déchet (EV-N-0058).
  - Le bénéfice comportemental des larves **vivantes** est perdu.
- **Preuves en faveur d'une nouvelle approche.**
  - Trois traditions anciennes produisaient spécifiquement des larves pour poussins (EV-H-0022, EV-H-0024, EV-H-0027).
  - La pratique africaine des termites est vivante (EV-H-0051, EV-H-0052).
  - Réaumur observait déjà l'avidité des poussins pour les insectes vivants (EV-H-0021).
  - Les verminières ont été abandonnées pour des raisons d'hygiène, aujourd'hui maîtrisables (EV-H-0032, EV-H-0059).
- **Hypothèse.** Fournir 5–10 % de la matière sèche en larves vivantes de BSF, élevées sur un substrat végétal autorisé (son, drêches) pendant 0–14 jours :
  - réduit le picage et la mortalité ;
  - sans dégrader l'IC ;
  - et réduit l'énergie de transformation par rapport à la farine.
- **Expérience de validation.** Essai factoriel en 2 × 3 :
  - souche à croissance rapide ou lente ;
  - témoin, 5 % ou 10 % de larves vivantes ;
  - 6 répétitions par traitement, 0–35 jours.
  - Mesures : poids, IC, mortalité, picage (score de plumage), *Salmonella* et *Clostridium* dans les larves et les caeca.
- **Critères de succès.** Score de plumage amélioré d'au moins 20 %, IC non dégradé (± 2 %), pathogènes indétectables dans les larves.
- **Critères d'échec.** IC dégradé de plus de 3 %, ou pathogènes détectés malgré le contrôle du substrat.
- **Coûts et risques.**
  - Faible coût expérimental.
  - Risque réglementaire : larves vivantes = « animaux d'élevage » nourris de substrats limités ; à vérifier avec l'agent E.
  - Risque de biosécurité.

### Piste H-2 — Finition au lactosérum acide pour poulets à croissance lente (et labels)

- **Problème.** Le lactosérum acide de yaourt est un polluant laitier difficile à valoriser. Les filières label cherchent à se différencier sur la qualité.
- **Solutions actuelles.** Épandage et méthanisation du lactosérum ; finition au maïs ou aux céréales pour les labels.
- **Insuffisances.** Aucune valorisation protéique ou fonctionnelle en volaille. La seule donnée moderne porte sur une souche à croissance rapide (EV-H-0057).
- **Preuves.**
  - Deux millénaires de finition lactée (EV-H-0015, EV-H-0034, EV-H-0055, EV-H-0056).
  - Un seuil empirique (pas plus de moitié de lait ; EV-H-0035), concordant avec la réponse dose-dépendante moderne (25 g/kg toléré, 50–100 g/kg pénalisants ; Q-H-0061).
  - Une meilleure stabilité oxydative du filet.
- **Hypothèse.** En finition seulement (21 derniers jours), 20–30 g/kg de lactosérum acide :
  - améliorent la stabilité oxydative et l'acceptabilité sensorielle du filet de poulets à croissance lente ;
  - sans perte de croissance ;
  - avec un coût alimentaire inférieur ou égal.
- **Expérience.** Quatre doses (0, 15, 30, 45 g/kg) en finition, deux souches, 6 répétitions. Mesures : croissance, IC, TBARS du filet à 1, 3, 6 et 9 jours, panel sensoriel, coût par kg.
- **Succès / échec.** Succès : TBARS au 6e jour réduit d'au moins 15 % sans baisse du gain. Échec : baisse du gain dès 15 g/kg.
- **Coûts et risques.** Faibles. Variabilité du lactosérum (acidité, minéraux) ; logistique de séchage.

### Piste H-3 — Cuisson à la ferme des céréales locales : retester Réaumur avec des méthodes modernes

- **Problème.** La dépendance au soja et aux aliments granulés industriels pèse sur les petits élevages et les élevages en autonomie.
- **Solutions actuelles.** Granulation et extrusion industrielles ; enzymes (agent N).
- **Insuffisances.** Peu accessibles à la ferme. Aucun test moderne de la cuisson simple par céréale n'a été retrouvé.
- **Preuves.**
  - Réaumur mesure des baisses d'ingéré différentes selon la céréale : orge −40 %, maïs plus de −50 %, avoine et sarrasin sans effet (EV-H-0018).
  - Le blé à la vapeur était utilisé pour la finition en Chine (EV-H-0028).
  - L'humide est réputé nuisible au poussin (EV-H-0029) ; la fermentation peut faire perdre de la lysine (EV-H-0058).
- **Hypothèse.** La cuisson à la vapeur de l'orge et du maïs améliore leur énergie métabolisable apparente (AMEn) et l'IC des poulets en finition, mais pas celle de l'avoine ou du sarrasin. L'effet mesuré par Réaumur refléterait donc la gélatinisation de l'amidon, pas seulement la satiété.
- **Expérience.** Mesure de l'AMEn et de la digestibilité iléale de chaque céréale, crue ou cuite à la vapeur, chez le poulet de 21 à 35 jours, puis essai de performance.
- **Succès / échec.** Succès : AMEn augmentée d'au moins 5 % pour l'orge ou le maïs cuits. Échec : aucune différence, ce qui indiquerait un effet de satiété seulement.
- **Coûts et risques.** Faibles. Énergie de cuisson à comptabiliser (agent E).

---

## 10. Recherches restantes prioritaires

1. Lire les publications primaires du Wisconsin (1922–1925) et de Moore et al. (1946) par une autre voie (bibliothèque, Internet Archive Scholar) pour confirmer les dates de la vitamine D et des AGP.
2. Dater la première phytase commerciale et la première formulation par programmation linéaire pour volailles (revues de Poultry Science des années 1950–1990, archives d'entreprises).
3. Chercher les études isotopiques chinoises sur des poulets (Shang, Zhou, Han) en chinois (鸡骨 稳定同位素 食性), via Wanfang ou WebSearch étendu.
4. Retrouver et lire Farina et al. 1991 (Tropicultura) ainsi que les données de rendement de la production de termites et de larves en Afrique de l'Ouest (Bénin, Togo : « production d'asticots aviculture villageoise »).
5. Chercher dans la littérature avicole de 1900 à 1930 (archive.org : « limberneck », « maggots », « meat scraps », « animal food for poultry » — Jackson 1915) le lien botulisme–larves et la transition vers les farines de viande. Il faudrait aussi documenter les « grains germés » (« sprouted oats ») des stations agronomiques américaines.
