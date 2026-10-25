# Réglementation des trois voies de production de muscle de poulet : textes officiels datés par juridiction (agent R, phase 4)

*Rédigé le 25/10/2026. Prolonge la section 8 de `research/reports/industrialization.md` (agent E). Réduit les lacunes **KG-COV-07** et **KG-COV-12** et précise la contradiction **CT-19**.*

---

## 1. Périmètre, méthode et limites d'accès

**Question.** Pour chaque juridiction, quels textes officiels encadrent (i) le poulet d'élevage amélioré (voie A : aliments des animaux, édition du génome), (ii) la viande cultivée (voie B) et (iii) les substituts (voie C : protéines unicellulaires, mycoprotéines, analogues végétaux) ? Il faut distinguer à chaque fois l'autorisation d'un **ingrédient** (ING), les exigences de **procédé** ou d'établissement (PROC) et l'autorisation d'un **produit** précis (PROD).

**Méthode.** Tous les textes ont été lus sur une source officielle le 25/10/2026, sauf mention contraire. Quand la source officielle était inaccessible, la source utilisée est citée et typée `press_report` ou `secondary_only`. Contournements utilisés :
- **EUR-Lex** (page vide, HTTP 202) : CELLAR (`publications.europa.eu/resource/celex/<CELEX>.ENG`). Pour les actes de 2026 pas encore indexés par CELEX, une requête SPARQL a retrouvé l'identifiant CELLAR. Cette méthode règle l'accès visé par **KG-COV-07**.
- **OpenEFSA** : API JSON publique du portail.
- **TRIS** : PDF des messages de la Commission.
- **Fedlex** : point SPARQL.
- **Federal Register** (texte intégral bloqué par captcha) : govinfo.gov.
- **NHC (Chine)** : téléchargement des 118 avis de recevabilité.

**Bilan.** 44 sources nouvelles (SRC-R-0001…0044), dont 17 non anglophones (39 %) en fr, it, de, hu, ko, ja, zh, pt et he ; 31 lues en texte intégral et 13 en partie. Ont été enregistrées 62 affirmations (EV-R-0001…0062) et 29 mesures (Q-R-0001…0029). Journal : 61 requêtes en 10 langues.

**Accès bloqués.**
- **Israël** : gov.il en 403, archive.org interdit par la politique réseau.
- **Singapour** : texte de la loi FSSA sur sso.agc.gov.sg en 403. La page de l'autorité (SFA) et sa liste officielle ont en revanche été lues.
- **États-Unis (fédéral)** : fsis.usda.gov et usda.gov en 403. La directive FSIS 7800.1 n'a donc pas été lue.
- **États américains** : Mississippi (certificat TLS invalide, puis 503 ; une copie officielle hébergée par Penn State a été utilisée) ; Indiana et Dakota du Sud (pages rendues en JavaScript).
- **Corée** : law.go.kr est chargé dynamiquement, les fiches MFDS ont été lues via WebFetch.
- **Brésil** : l'API de la Chambre n'a renvoyé aucun résultat.

---

## 2. Tableau par juridiction : textes officiels datés

Légende : **ING** = autorisation d'ingrédient ; **PROC** = exigences de procédé ou d'établissement ; **PROD** = autorisation d'un produit d'un demandeur donné ; **H/A** = alimentation humaine / animale. Statut au 25/10/2026.

### 2.1 Union européenne

| Texte (n°, date) | URL officielle | Statut | Portée | Réf. |
|---|---|---|---|---|
| Règlement (UE) 2015/2283, 25/11/2015 | eur-lex.europa.eu/eli/reg/2015/2283/oj (lu via CELLAR) | en vigueur depuis le 1/1/2018 | H. Les cultures cellulaires forment la catégorie (vi). L'autorisation **PROD** se fait par inscription sur la liste de l'Union, avec spécifications ; protection des données de 5 ans | EV-E-0027, EV-E-0028 |
| Guide scientifique EFSA NDA, EFSA J 2024;22:e8961 (DOI 10.2903/j.efsa.2024.8961) | doi.org/10.2903/j.efsa.2024.8961 | applicable au 1/2/2025 | **PROC** très détaillé : lignée, banques, stabilité génétique, virus et prions, facteurs de croissance d'origine microbienne. Il n'existe pas de stratégie de génotoxicité arrêtée | EV-R-0001…0004 |
| Registre OpenEFSA | open.efsa.europa.eu | consulté le 25/10/2026 | 2 demandes de culture cellulaire animale : canard de Supreme SAS (EFSA-Q-2024-00582, en évaluation, horloge suspendue depuis le 15/10/2026) et graisse bovine de Mosa Meat (EFSA-Q-2026-00100, phase de réception). **Aucune demande de poulet** | EV-R-0005, Q-R-0021 |
| Idem : Solein (Xanthobacter sp. SoF1), EFSA-Q-2022-00140 | idem | avis adopté, en publication (31/08/2026) | H, **PROD** à venir. L'avis de l'EFSA n'est pas l'autorisation, qui viendra d'un acte de la Commission | EV-R-0006 |
| Règlement d'exécution 2021/882, 1/6/2021 (Tenebrio molitor séché) | publications.europa.eu, cellar 898daec1… | en vigueur | H, **PROD**. Le premier insecte autorisé a demandé environ 39,5 mois du dépôt à l'acte (calcul de l'agent) ; le demandeur dispose de 5 ans d'exclusivité | EV-R-0010, Q-R-0014, Q-R-0017 |
| Règlement 2021/1372, 17/8/2021 | eur-lex eli 2021/1372 | en vigueur | A, **ING** : protéines animales transformées d'insectes autorisées pour volailles et porcs | EV-E-0029 |
| Règlement 2022/1104, 1/7/2022 (catalogue des matières premières) | cellar 41bf1c2f… | en vigueur | A. Entrée 12.1.13 : protéines unicellulaires bactériennes (dont Methylococcus capsulatus sur gaz naturel). Catalogue **volontaire**, qui n'autorise rien ; les micro-organismes GM restent soumis au règlement 1829/2003 | EV-R-0008, EV-R-0009 |
| Dossiers Hermetia illucens en alimentation humaine | OpenEFSA | non valides, retirés ou en évaluation | La mouche soldat noire est autorisée en aliment pour volailles, pas en alimentation humaine | EV-R-0007 |
| Règlement (UE) 2026/1388, 17/6/2026 (plantes NGT) | cellar c0b375d4… | en vigueur le 16/7/2026, applicable le 17/7/2028 | Le régime allégé ne vise **que les plantes** : animaux et micro-organismes édités restent OGM | EV-R-0011, Q-R-0029 |
| Règlement (UE) 2026/1739, 8/7/2026 (OCM, dénominations carnées) | cellar 1b055a6f… | applicable au 19/8/2029, stocks jusqu'au 19/8/2032 | « meat », « chicken », « poultry », « breast », « wing », « thigh », « drumstick »… sont réservés aux produits carnés et **interdits pour les aliments de culture cellulaire**. « Burger », « sausage » et « nuggets » ne figurent pas dans la liste | EV-R-0012, EV-R-0013, Q-R-0015 |

### 2.2 États membres et Europe hors UE

| Juridiction | Texte (n°, date) | URL officielle | Statut | Portée | Réf. |
|---|---|---|---|---|---|
| France | Conseil d'État, n° 492839, 28/1/2025 | conseil-etat.fr/…/492839.pdf | décision définitive | Annulation du décret n° 2024-144 sur les dénominations des produits végétaux. Aucune loi d'interdiction de la viande cellulaire adoptée ; un amendement de mai 2026 a été déclaré irrecevable (cavalier) | EV-R-0014 ; SRC-E-0039 |
| Italie | Loi n. 172, 1/12/2023 | normattiva.it (ELI 2023/12/01/23G00188) | en vigueur au 16/12/2023 | Interdiction H **et A** des cultures cellulaires de **vertébrés**, fondée sur la précaution (art. 7 du règlement 178/2002). Sanctions automatiques, étendues aux financeurs (vérification indépendante). Art. 3 : interdiction des dénominations carnées pour les produits végétaux | EV-E-0030, EV-R-0062 |
| Italie (UE) | TRIS 2023/0675/IT, message 009 du 29/1/2024 | technical-regulation-information-system.ec.europa.eu, notification 25152 | close | La Commission clôt la procédure : texte adopté **pendant le statu quo** de la directive 2015/1535 | EV-R-0015 |
| Hongrie | Loi 2025. évi LXXXIX (adoptée le 18/11/2025, promulguée le 28/11/2025) | njt.jog.gov.hu/jogszabaly/2025-89-00-00 | en vigueur le lendemain de la promulgation | Interdiction de produire et de mettre sur le marché la « viande de laboratoire » et les produits qui en contiennent, sauf usages médical et vétérinaire | EV-R-0016 |
| Hongrie (UE) | TRIS 2024/0394/HU ; avis circonstancié C(2024) 7100 final du 9/10/2024 | notification 26066 | close ; texte définitif reçu le 5/12/2025 | La Commission juge l'interdiction **inutile et injustifiée** et non conforme aux chapitres II à VI du règlement 2015/2283. La Lituanie et l'Autriche ont aussi émis un avis circonstancié | EV-R-0017 |
| Autres projets | Roumanie (vote du Sénat en 2023, presse) | — | non vérifié | Aucune notification TRIS 2025 trouvée pour RO, PL, CZ ou SK | journal |
| Suisse | ODAlOUs (RS 817.02), art. 15-19, état au 1/7/2025 ; ordonnance du DFI (RS 817.022.2), état au 1/2/2024 | fedlex.data.admin.ch/eli/cc/2017/63 et …/2017/159 | en vigueur | H. Catégorie f (cultures cellulaires). Autorisation **PROD** de l'OSAV pour **5 ans non renouvelables**, puis désignation générique par le DFI. Le dossier inclut le procédé | EV-R-0018, EV-R-0019, Q-R-0016 |
| Suisse | Demande d'Aleph Farms (juillet 2023) | communiqué du canton de Zurich, 11/9/2025 | pas d'autorisation au 11/9/2025 | — | EV-R-0020 |
| Royaume-Uni | Bac à sable FSA (2025-2027) ; guide « toxicology and growth media », 30/9/2026 | gov.uk | 2 dossiers en évaluation, aucune autorisation pour l'alimentation humaine | **PROC** : inventaire de chaque composant du milieu (qualité alimentaire ou pharmaceutique, résidus) ; composants recombinants | EV-E-0038, EV-R-0022, EV-R-0023 |
| Royaume-Uni (A) | Meatly, aliment pour chiens (juillet 2024) | aucune décision officielle trouvée | presse | Agrément d'établissement ou inspection APHA selon la presse | EV-R-0024 |
| Angleterre (OGM) | Precision Breeding Regulations 2025 (SI 2025/581), 13/5/2025 | legislation.gov.uk/uksi/2025/581 | en vigueur le 13/11/2025 (calcul) | **Plantes seulement** | EV-R-0021 |

### 2.3 Moyen-Orient et Asie-Pacifique

| Juridiction | Texte (n°, date) | URL officielle | Statut | Portée | Réf. |
|---|---|---|---|---|---|
| Israël | Communiqué du ministère de la Santé, 17/1/2024 (bœuf d'Aleph Farms) | gov.il/he/pages/17012024-02 (403) | presse seulement | **PROD**, plus une licence de la ligne de production. La nature exacte de l'acte n'est pas établie : « lettre no questions » selon une source, « approbation de commercialisation » selon une autre | EV-E-0041, EV-R-0025 |
| Singapour | Food Safety and Security Act 2025 ; page SFA « Overview of Pre-Market Approval Framework » | sfa.gov.sg/food-information/novel-food | infractions en vigueur depuis le 28/11/2025 | H, **PROD**. Annulation possible en cas de **changement matériel** du mode de fabrication (section 112) | EV-R-0026, EV-R-0027 |
| Singapour | **SFA List of Approved Novel Foods**, version du 14/8/2026 (1re édition le 17/3/2026) | sfa.gov.sg/docs/…/2026-08-14-sfa-list-of-approved-novel-foods.pdf | officielle | 18 approbations, dont 6 de cellules animales. Poulet : Eat Just (26/11/2020 avec sérum fœtal bovin ; 11/1/2023 sans sérum), Vital Meat (17/10/2025). Caille Vow (22/3/2024), canard Suprême SAS (10/4/2026), bœuf Aleph (22/7/2026), Solein (29/9/2022) | EV-R-0028…0034, Q-R-0001…0012, Q-R-0023 |
| Corée du Sud | Avis MFDS n° 2024-13, 21/2/2024 | mfds.go.kr/brd/m_207/view.do?seq=14965 | en vigueur | **ING** : reconnaissance provisoire des matières obtenues par culture de cellules ou de micro-organismes | EV-R-0035 |
| Corée du Sud | Avis MFDS n° 2026-311, 30/6/2026 (projet de Food Code) | mfds.go.kr/brd/m_209/view.do?seq=44261 | projet ; consultation jusqu'au 31/8/2026 | Catégorie de produit « 세포배양가공식품 », réservée aux ingrédients reconnus | EV-R-0036 |
| Corée du Sud | Données MFDS (audit parlementaire, presse du 13/10/2026) | foodtoday.or.kr | presse | 2 demandes, 0 reconnaissance ; 869 jours écoulés pour la première ; frais de 45 M KRW | EV-R-0037, Q-R-0018…0020 |
| Japon | Projet de guide de la CAA (sous-comité des nouveaux aliments, 28/5/2026) | caa.go.jp/…/fscc_cms105_260528_06.pdf | projet ; choix entre examen et notification non arrêté | **PROC** : revalidation proportionnée en cas de changement de procédé. Lignée GM : examen OGM ; édition du génome : confirmation par la CAA | EV-R-0038…0040 |
| Japon (A) | Liste CAA des aliments édités notifiés | caa.go.jp/…/genome_edited_food/list | 13 entrées | Daurade, fugu, cardeau et tilapia à muscle ou croissance accrus commercialisés **par simple notification** ; aucune volaille | EV-R-0060 |
| Chine | Mesures sur les 新食品原料 (2013, modifiées en 2017) | zwfw.nhc.gov.cn/kzx/zcfg/xspylsp_237/202107/t20210707_2132.html | en vigueur | **ING** publié de façon générique. Inspection du site possible ; « évaluation du risque pour la stabilité sociale » ; aliments GM exclus | EV-R-0041 |
| Chine | 118 avis de recevabilité de la NHC (déc. 2022 – oct. 2026) | zwfw.nhc.gov.cn/kzx/slgs/xspylsp/ | — | 110 demandes, **aucune de cellules animales** | EV-R-0042, Q-R-0022 |
| Chine (C) | Avis NHC 2025 n° 7 (protéine de Fusarium venenatum) | zwfw.nhc.gov.cn/…/t20251210_3206.html | approuvée en novembre 2025 | **ING** ; au moins 50 g de protéines pour 100 g de matière sèche | EV-R-0043, Q-R-0027 |
| Chine (A) | Avis MARA n° 692, 21/7/2023 | moa.gov.cn/govpublic/xmsyj/202307/t20230727_6433063.htm | en vigueur | A, **ING** : protéine de Clostridium autoethanogenum autorisée pour les volailles de chair, à 1-4 % recommandé et 9 % au maximum | EV-R-0044, Q-R-0026 |
| Australie / Nouvelle-Zélande | A1269 (caille Vow), publication au Journal officiel le 18/6/2025 ; normes 1.5.4 et 3.4.1, annexe 25A | foodstandards.gov.au/…/A1269-… | en vigueur | **PROD** (annexe 25A) et **PROC** (norme 3.4.1). Mention « cell-cultured » obligatoire | EV-R-0045, EV-E-0036 |
| Australie / Nouvelle-Zélande | A1341 (canard de Suprême SAS = Gourmey), reçue en août 2025, approuvée par FSANZ le 6/10/2026 | foodstandards.gov.au (rapport du 24/6/2026, circulaire 415-26) | notifiée aux ministres (60 jours) | **PROD** comme ingrédient | EV-R-0046, Q-R-0025 |

### 2.4 Amériques

| Juridiction | Texte (n°, date) | URL officielle | Statut | Portée | Réf. |
|---|---|---|---|---|---|
| États-Unis (FDA) | Inventaire des consultations sur les aliments issus de cellules animales | hfpappexternal.fda.gov/scripts/fdcc/?set=AnimalCellCultureFoods | 5 entrées (dont 3 de poulet), aucune depuis juillet 2025 | La FDA **clôt une consultation volontaire** par une lettre « no questions » ; ce n'est pas une autorisation. Le dossier est propre à l'entreprise et à son procédé | EV-R-0047, Q-R-0024 |
| États-Unis (USDA-FSIS) | ANPR 86 FR 49491, 3/9/2021 | govinfo.gov/…/FR-2021-09-03/pdf/2021-19057.pdf | aucune règle finale | Transfert de la FDA au FSIS à la récolte. Pas d'approbation générique des étiquettes | EV-R-0048 |
| États-Unis (C) | 90 FR 5590, 17/1/2025 (myoglobine) | govinfo.gov/…/FR-2025-01-17/pdf/2025-01239.pdf | en vigueur au 19/2/2025 | **ING** (colorant produit par Komagataella phaffii GM) pour les analogues de viande et de volaille hachées | EV-R-0049 |
| États-Unis (A) | FDA CVM, IGA « low risk » ; guides GFI #187A (mai 2024) et #187B (janvier 2025) | fda.gov/…/low-risk-igas | — | Pour l'usage alimentaire, seuls 3 bovins figurent sur la liste, **aucune volaille** | EV-R-0061 |
| Floride | Fla. Stat. § 500.452 (ch. 2024-137) | leg.state.fl.us | en vigueur | Interdiction | EV-E-0032 |
| Floride (contentieux) | 11e circuit, n° 24-13640, 23/3/2026 | media.ca11.uscourts.gov/opinions/pub/files/202413640.pdf | injonction refusée en appel | Le PPIA **ne préempte pas** l'interdiction. Le grief tiré de la clause de commerce dormante reste pendant | EV-R-0057 |
| Texas | SB 261 (1/9/2025 – 1/9/2027) | capitol.texas.gov | en vigueur ; contestée en justice (secondaire) | Moratoire et étiquetage | EV-E-0033 |
| Alabama | SB23 « enrolled », en vigueur au 1/10/2024 | legislature.state.al.us/pdf/SearchableInstruments/2024RS/SB23-enr.pdf | en vigueur | Interdiction ; délit de classe C ; exception pour la recherche publique | EV-R-0050 |
| Mississippi | HB 1006 (version envoyée au gouverneur), 1/7/2025 | copie officielle (aglaw.psu.edu) | en vigueur | Interdiction ; amende ≤ 500 USD ; produits végétaux et d'insectes non étiquetables comme viande | EV-R-0051, Q-R-0028 |
| Montana | HB 401, chapitre 276 de 2025 ; application au 1/10/2025 | archive.legmt.gov/…/CH0276.pdf ; news.mt.gov | en vigueur | Interdiction ; produits exclus de la définition de la viande | EV-R-0052, EV-R-0053 |
| Nebraska | LB 246, approuvé le 20/5/2025 | nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB246.pdf | en vigueur | Le produit est réputé « adultéré », donc interdit | EV-R-0054 |
| Dakota du Sud | SB 124 (2026, moratoire de 5 ans) ; HB 1022 et HB 1118 (2025) | sdlegislature.gov (titres via l'API) | presse | Moratoire ; étiquetage ; pas de fonds publics | EV-R-0055 |
| Indiana et 7 États « étiquetage » | HB 1425 (1/7/2025 – 30/6/2027) ; SC, TN, CO, OK, UT, WY | non lus sur source officielle | secondaire | Moratoire ou étiquetage | EV-R-0056 |
| Brésil | RDC ANVISA n° 839, 14/12/2023 (en vigueur au 16/3/2024, modifiée par la RDC 976/2025) ; agenda 2026-2027, thème 3.3 | copie municipale (SRC-E-0033) ; bibliothèque ANVISA du 20/3/2026 | en vigueur ; listes d'aliments autorisés à réglementer | **PROD/ING** et **PROC** ; aucun dossier de viande cultivée connu | EV-E-0052, EV-R-0058 |
| Brésil (A) | Résolution normative CTNBio n° 16, 15/1/2018 | antigo.mctic.gov.br/…/Resolucao_Normativa_CTNBio_n_16_de_15012018.html | en vigueur | Un produit édité sans ADN recombinant peut ne pas être un OGM, après consultation au cas par cas, **y compris pour les animaux** | EV-R-0059 |

---

## 3. Ce que le corpus établit désormais

1. **Aucune demande de poulet cultivé n'est déposée à l'EFSA**, ni en Chine, ni en Corée à notre connaissance. Les deux dossiers européens concernent le canard (Supreme SAS) et la graisse bovine (Mosa Meat) (EV-R-0005, EV-R-0042, EV-R-0037). Le poulet cultivé n'est autorisé qu'à **Singapour** (Eat Just, Vital Meat ; EV-R-0028) et fait l'objet de consultations closes par la FDA aux **États-Unis** (EV-R-0047).
2. **Singapour publie désormais ses approbations.** La réserve de la vérification indépendante (EV-C-0063 : « la SFA ne publie pas ses décisions ») reposait sur le document de 2025. Elle est caduque depuis la liste du 17/3/2026 (EV-R-0028). L'approbation du milieu sans sérum de GOOD Meat, connue jusqu'ici par la presse (SRC-C-0038), est confirmée par la source primaire (EV-R-0029).
3. **Les spécifications officielles donnent la composition de la biomasse autorisée.**
   - Poulet Eat Just : 5 à 10 % de protéines pour 85 à 95 % d'eau (Q-R-0001, Q-R-0002).
   - Vital Meat : plus de 6 % de protéines (Q-R-0004).
   - Caille Vow : plus de 4 % de protéines (Q-R-0006).
   - Canard Suprême : plus de 7 % de protéines, et plus de 60 % sur matière sèche (Q-R-0009, Q-R-0010).

   Ce sont des **limites** réglementaires, pas des mesures. Elles valident l'ordre de grandeur de 9 % de protéines retenu pour recalculer les TEA (EV-X-0001) : la biomasse cellulaire autorisée contient environ deux à trois fois moins de protéines que le filet de poulet (rapprochement fait par l'agent, à confirmer par l'agent K).
4. **Le procédé autorisé fixe des bornes.** L'approbation de Vow à Singapour décrit des bioréacteurs de 200 à 20 000 L et une densité minimale de récolte de 30 g/L (EV-R-0031, Q-R-0007, Q-R-0008). C'est un périmètre déclaré par l'entreprise, pas la preuve d'une production à 20 000 L.
5. **L'UE réserve « chicken » et ses morceaux à la viande à partir de 2029** et l'interdit explicitement pour les produits cellulaires (EV-R-0012). Cette harmonisation européenne rend sans objet les décrets français annulés (EV-R-0014) ; c'est une conclusion de l'agent.
6. **L'Union désapprouve les interdictions nationales.** Elle a clos la procédure italienne parce que la loi a été adoptée pendant le statu quo (EV-R-0015). Pour la Hongrie, elle a émis un avis circonstancié jugeant l'interdiction « inutile et injustifiée » (EV-R-0017). La Hongrie a pourtant promulgué sa loi le 28/11/2025 (EV-R-0016).
7. **Aucune juridiction étudiée n'offre de voie allégée pour un poulet édité.**
   - UE : les animaux sont exclus du régime NGT (EV-R-0011).
   - Angleterre : les règlements de 2025 visent les plantes (EV-R-0021).
   - États-Unis : aucune volaille dans la liste des IGA à faible risque (EV-R-0061).
   - Japon : la notification a suffi pour quatre poissons à croissance ou muscle accrus (EV-R-0060).
   - Brésil : la consultation CTNBio est ouverte aux animaux (EV-R-0059).

---

## 4. Contradictions réduites ou précisées

- **CT-19 (FDA contre interdictions d'États) : précisée, en partie résolue.** L'arrêt du 11e circuit (EV-R-0057) juge que le Poultry Products Inspection Act ne préempte pas une interdiction d'État, qui ne régit « ni les ingrédients, ni les installations ». L'achèvement d'une consultation FDA (EV-R-0047) et l'inspection fédérale ne donnent donc pas le droit de vendre dans tous les États. Il ne s'agit pas d'une contradiction de faits mais de deux niveaux juridiques compatibles à ce stade. Reste ouvert : le grief tiré de la clause de commerce dormante (Floride) et le contentieux texan, non retrouvé. Le nombre d'États dont l'interdiction ou le moratoire est vérifié sur texte officiel passe de 2 (FL, TX) à **6** : s'ajoutent AL, MT et NE, ainsi que MS par une copie du texte officiel (EV-R-0050…0054).
- **EV-E-0035 (Singapour, « toute modification ») : confirmé et nuancé.** Sous la loi FSSA, un « changement matériel » de procédé est un motif possible d'annulation (EV-R-0027). La formulation reste conditionnelle (« may be cancelled »).
- **EV-E-0041 (Israël, lettre « no questions ») contre EV-R-0025 (« approbation de commercialisation »).** Deux journaux décrivent l'acte différemment. Le texte officiel est inaccessible : la nature juridique reste **non vérifiée**.
- **Corée : date limite de la consultation.** La presse donnait le 31/7/2026, l'avis officiel dit le 31/8/2026 (EV-R-0036). La source officielle prévaut.
- **Section 8 du rapport E : mises à jour.**
  - Japon : il existe désormais un projet de guide, mais pas de cadre arrêté (EV-R-0038).
  - Corée : les deux textes officiels sont lus (EV-R-0035, EV-R-0036).
  - Suisse : le régime est lu sur Fedlex (EV-R-0018).
  - FSANZ : un deuxième produit (canard) est approuvé (EV-R-0046).

---

## 5. Ce que change chaque régime pour les voies A, B et C

### Voie A (élevage optimisé)
- **Aliments des animaux : la voie de l'ingrédient est la plus légère.**
  - UE : insectes (2021/1372) ; protéines unicellulaires (SCP) méthanotrophes au catalogue, d'usage volontaire.
  - Chine : protéine de Clostridium jusqu'à 9 % de l'aliment des poulets de chair (EV-E-0029, EV-R-0008, EV-R-0044).

  C'est l'opportunité la plus proche du marché pour les SCP : en aliment volaille, elles évitent l'autorisation de produit exigée en alimentation humaine.
- **Mouche soldat noire** : autorisée en aliment volaille, mais pas en alimentation humaine dans l'UE (EV-R-0007). Pour un éleveur, cela limite toute valorisation croisée vers l'alimentation humaine.
- **Génétique par édition du génome** (poulet à muscle accru, résistance aux maladies) :
  - le régime OGM complet s'applique dans l'UE ;
  - aux États-Unis, une approbation ou une décision de faible risque au cas par cas est nécessaire ;
  - au Japon, la notification a suffi pour des poissons comparables ;
  - au Brésil, une consultation CTNBio au cas par cas est ouverte aux animaux.

  Le **Japon et le Brésil** sont les premiers marchés plausibles (EV-R-0011, EV-R-0061, EV-R-0060, EV-R-0059).
- **Dénominations.** Le règlement 2026/1739 réserve « chicken », « breast », « wing » à la viande issue de l'animal (EV-R-0012) : c'est un avantage commercial réglementé pour la voie A.

### Voie B (viande cultivée)
- **La nature de l'autorisation diffère selon les pays.**
  - **Produit** d'un demandeur donné : UE (avec 5 ans d'exclusivité), Suisse (5 ans puis liste générique), Singapour, Australie/NZ, Brésil, Israël.
  - **Ingrédient**, puis catégorie de produit : Corée, Chine.
  - **Consultation volontaire et inspection de l'établissement** : États-Unis.

  Dans les régimes « produit », chaque concurrent doit déposer son propre dossier. Dans les régimes « ingrédient » (Chine), une annonce publique peut profiter à des tiers substantiellement équivalents (EV-R-0041).
- **Optimiser coûte une procédure.**
  - Singapour : un changement matériel peut entraîner l'annulation (EV-R-0027) ; le passage au milieu sans sérum a fait l'objet d'une seconde approbation, plus de deux ans après la première (Q-R-0013).
  - Japon (projet) : la revalidation serait proportionnée au changement (EV-R-0038).
  - Royaume-Uni : chaque composant du milieu doit être inventorié avec sa qualité et ses résidus (EV-R-0022).

  Les leviers de coût identifiés par les TEA (milieu, hydrolysats, facteurs recombinants) sont donc des **variables réglementées**.
- **Délais observés** (calculs de l'agent sur dates officielles) :
  - environ 14 mois pour A1341 chez FSANZ (Q-R-0025), contre environ 26 mois pour A1269 ;
  - plus de 28 mois et toujours sans reconnaissance pour le premier dossier coréen (Q-R-0020) ;
  - environ 39,5 mois pour le premier insecte dans l'UE (Q-R-0014).
- **Risque politique.** L'interdiction couvre aussi l'**aliment pour animaux** en Italie (EV-R-0062) et les hybrides en Hongrie (EV-R-0016). Aux États-Unis, au moins cinq États interdisent (FL, AL, MS, MT, NE) et trois imposent un moratoire (TX ; IN et SD, ces deux derniers connus par sources secondaires) ; la préemption fédérale ne protège pas (EV-R-0057).
- **Étiquetage.** « Chicken » sera interdit pour le poulet cultivé dans l'UE en 2029 (EV-R-0012). L'Australie/NZ impose « cell-cultured » ou « cell-cultivated » (EV-R-0045) ; le Texas impose « cell-cultured » ou « lab-grown » (EV-E-0033).

### Voie C (substituts)
- **Les SCP et mycoprotéines avancent par autorisation d'ingrédient ou de produit.**
  - Solein : approuvée à Singapour en 2022 ; avis de l'EFSA adopté en 2026, en attente de l'acte de la Commission (EV-R-0034, EV-R-0006).
  - Mycoprotéine de Fusarium : approuvée en Chine en 2025 (EV-R-0043).
  - Myoglobine produite par une levure GM : autorisée comme colorant aux États-Unis (EV-R-0049).
- **Les dénominations sont le principal frein commercial.**
  - UE : interdiction de « chicken », « breast », « wing » à partir de 2029 ; « nuggets », « burger » et « sausage » restent utilisables (EV-R-0012).
  - Italie : interdiction nationale des termes carnés pour les produits végétaux (EV-R-0062).
  - Mississippi : interdiction de l'étiquetage « meat » pour les produits végétaux et à base d'insectes (EV-R-0051).
  - France : le décret a été annulé (EV-R-0014).
- **Microbes GM** : ils restent soumis aux règles OGM dans l'UE (EV-R-0011, EV-R-0008). En Chine, les aliments GM sont exclus du régime des nouveaux ingrédients (EV-R-0041).

---

## 6. Lacunes restantes

- **Israël** : texte officiel inaccessible (403, archive.org bloqué).
- **Singapour** : texte de la loi FSSA non lu (403).
- **États-Unis** :
  - directive FSIS 7800.1 et accord FDA–FSIS de 2019 non lus (403) ;
  - textes officiels de l'Indiana, du Dakota du Sud et des 7 lois d'étiquetage non lus ;
  - contentieux texan non retrouvé.
- **Roumanie et autres projets européens** : presse seulement.
- **Royaume-Uni** : aucun acte officiel de l'APHA ou de la Defra sur l'aliment pour animaux de compagnie.
- **Brésil** : projets de loi d'interdiction et compétence du MAPA non vérifiés.
- **Corée** : annexe 2 de l'avis 2024-13 (données exigées) non lue.
- **UE** : liste de l'Union consolidée (2017/2470) et avis EFSA sur Solein non lus (non publiés).

---

## 7. Pistes d'innovation (d'origine réglementaire)

- **R-1 « Procédé à plage autorisée ».**
  - *Problème* : toute optimisation du milieu ou de l'échelle peut exiger une nouvelle approbation (EV-R-0027, Q-R-0013).
  - *Fondement* : l'approbation de Vow fixe une **plage** de 200 à 20 000 L et une densité minimale (EV-R-0031) au lieu de valeurs ponctuelles.
  - *Hypothèse* : des dossiers rédigés en plages validées (volume, densité, gamme de composants équivalents) réduisent les redépôts.
  - *Validation* : comparer les approbations SFA, FSANZ et FDA (plages contre points fixes) et relever le nombre de compléments ou de nouvelles demandes.
  - *Succès* : au moins une modification de milieu acceptée sans nouveau dossier.
- **R-2 « SCP en aliment volaille d'abord ».**
  - *Fondement* : statut d'ingrédient d'aliment pour animaux dans l'UE et en Chine (EV-R-0008, EV-R-0044), contre une autorisation de produit lente en alimentation humaine (EV-R-0006).
  - *Hypothèse* : une SCP peut atteindre plus vite une échelle industrielle en remplaçant 5 à 9 % du soja des poulets de chair.
  - *Validation* : essai zootechnique au taux maximal chinois de 9 %. Pont avec l'agent M sur les coûts.
- **R-3 « Poulet édité dans les juridictions à notification ».**
  - *Fondement* : poissons à muscle accru notifiés au Japon (EV-R-0060) ; consultation CTNBio au Brésil (EV-R-0059).
  - *Risque* : régime OGM complet dans l'UE (EV-R-0011).
  - *Validation* : dossier de pré-consultation CAA ou CTNBio pour une délétion sans transgène.

---

## 8. Recherches restantes prioritaires

1. Textes officiels de l'Indiana HB 1425 et du Dakota du Sud SB 124 (accès hors JavaScript) ; état du contentieux texan et de la suite de l'affaire floridienne (clause de commerce dormante).
2. Avis EFSA sur Solein dès sa publication, puis acte d'exécution de la Commission.
3. Directive FSIS 7800.1 (miroir officiel) et accord FDA–FSIS de 2019.
4. Annexe 2 de l'avis MFDS 2024-13 et adoption finale du Food Code coréen (avis 2026-311).
5. Israël : liste officielle des nouveaux aliments du ministère de la Santé (accès réseau à rouvrir).
6. Brésil : projets de loi (PL et PDL contre la RDC 839) et rôle du MAPA ; Roumanie et autres États membres (TRIS).
