> **Note du coordinateur (2026-10-25)** : passages sur l'usine Believer corrigés après vérification indépendante (`coordination/verification/batch1_results.md`) — la source ne dit pas que l'usine « n'a jamais produit » ni qu'elle est « vacante ».

# Ingénierie, économie, industrialisation et réglementation des trois voies de production de muscle de poulet

**Agent E — Chicken Muscle Research Lab — brouillon de phase 3-4 (2026-10-25)**
Questions couvertes : RQ-E1 à RQ-E6 ; responsable principal de RQ-X1 (coûts), RQ-X2 (ressources par kg de protéine), RQ-X4 (réglementation).

> Règle de lecture : chaque chiffre est suivi de sa nature. **Mesuré** = observé sur une installation ou une expérience ; **statistique** = enquête/série officielle ; **estimation publiée** = modèle d'exploitation type ; **sortie de modèle** = TEA/ACV/modèle de l'agent E ; **déclaration d'entreprise** = non vérifiable. Une sortie de modèle n'est jamais un coût industriel démontré. Les monnaies sont conservées avec leur année ; aucune correction d'inflation n'a été appliquée.

---

## 1. Périmètre et méthode

**Bases et outils.** Europe PMC (recherche et texte intégral libre), PubMed, Crossref (API directe après erreur de l'outil local, réparé depuis), J-STAGE, HAL, theses.fr, WebSearch/WebFetch, téléchargement direct (curl + pdftotext) de rapports et de textes officiels, API de la BCE pour les taux de change. Les textes européens ont été obtenus par l'Office des publications (`publications.europa.eu/resource/celex/…`) car EUR-Lex renvoie une page vide (HTTP 202) aux robots.

**Couverture.** 81 requêtes journalisées (`research/agents/E/search_log.md`) en anglais, français, chinois, espagnol, portugais, italien, japonais et coréen (le portugais pour l'Embrapa et l'ANVISA, l'italien pour la loi 172/2023, le japonais et le coréen pour les cadres réglementaires). 42 sources enregistrées par l'agent E (SRC-E-0001 à SRC-E-0042) et 4 sources d'autres agents réutilisées (SRC-X-0001, SRC-A-0024, SRC-A-0011, SRC-P-0004) ; 32 sources E lues en texte intégral (29, dont 22 articles, rapports ou textes officiels, 6 articles de presse ou communiqués et le modèle interne) ou en partie (3), plus SRC-A-0024 lue intégralement ; 59 affirmations (EV-E-0001 à 0059) ; 72 mesures (Q-E-0001 à 0072). Modèle économique : `research/agents/E/models/pathway_cost_model.py` (résultats dans `results.md`).

**Limites d'accès.** Pasitka et al. 2024 (Nature Food), Goodwin et al. 2024, Negulescu et al. 2023, Mattick 2015, Tuomisto 2011, Poore & Nemecek 2018 et Garrison 2022 sont payants ou non indexés : résumé ou métadonnées seulement. Bloqués : rapport USDA-FAS/GAIN (403), PDF de l'ANVISA (copie municipale utilisée), pages Embrapa (contenu masqué pour cause de restrictions électorales 2026), Meat+Poultry et Wilson Times (403), page dynamique des statuts de Floride (site législatif alternatif utilisé). Aucune donnée de coût **mesurée** dans une usine de viande cultivée n'est publique.

---

## 2. RQ-E1 / RQ-X1 (voie A) — Coût de production du poulet conventionnel

### 2.1 Tableau des coûts par pays et par système

| Pays / système | Année | Coût d'élevage | Base | Aliment | Poussin | Main-d'œuvre | Logement / structure | Nature | Réf. |
|---|---|---|---|---|---|---|---|---|---|
| UE (moyenne 9 pays), standard | 2017 | 82,5 c€ | /kg vif | 50,7 | 14,9 | 3,1 | 5,5 | estimation publiée (modèle d'exploitation type) | Q-E-0022, EV-E-0015 |
| Pologne (min. UE) – R.-U. (max. UE) | 2017 | 78,6 – 86,5 c€ | /kg vif | 47,7-55,6 (plage UE) | 12,9-18,7 | 1,5-5,2 | 4,7-6,2 | estimation publiée | Q-E-0026, EV-E-0015 |
| Brésil | 2017 | 63,2 c€ | /kg vif | 43,7 | 8,9 | 2,0 | 4,9 | estimation publiée | Q-E-0023, EV-E-0016 |
| États-Unis | 2017 | 64,5 c€ | /kg vif | 44,1 | 10,5 | 1,9 | 2,9 | estimation publiée | Q-E-0024 |
| Ukraine | 2017 | 67,2 c€ | /kg vif | 42,0 | 13,6 | 0,4 | 5,6 | estimation publiée | Q-E-0025 |
| UE, après abattage | 2017 | 134-155 c€ | /kg carcasse | — | — | abattage 21-38 c€/kg carcasse | — | estimation publiée | Q-E-0027, EV-E-0018 |
| France, standard | 2022 | 1,264 € (1,212 hors rémunération) | /kg vif | 0,755 | 0,239 | 0,052 (forfait) | 0,125 | statistique (enquête OP) | Q-E-0029, EV-E-0019 |
| France, Label Rouge | 2022 | 2,485 € | /kg vif | 1,436 | 0,187 | 0,256 | 0,418 | statistique | Q-E-0030 |
| France, biologique | 2022 | 3,366 € | /kg vif | 2,161 | 0,230 | 0,268 | 0,463 | statistique (échantillon fragile) | Q-E-0031 |
| Brésil (Paraná, ICPFrango) | juil. 2025 | R$ 4,60 (≈ 0,73 € au taux BCE 2025) | /kg vif | 64 % du coût | — | — | — | statistique (via presse) | Q-E-0032, Q-E-0064, EV-E-0021 |

Sources : van Horne 2018, Wageningen Economic Research, rapport commandé par l'AVEC (SRC-E-0011, texte intégral lu) ; ITAVI/Chambres d'agriculture, résultats 2022 (SRC-E-0012, texte intégral lu) ; Embrapa/CIAS via Notícias Agrícolas (SRC-E-0013).

### 2.2 Ce que montrent ces chiffres

- **L'aliment est le poste dominant** : environ 60 à 65 % du coût d'élevage en Europe en 2017 (EV-E-0015), 64 % au Paraná en 2025 (EV-E-0021). C'est la seule voie pour laquelle on dispose de coûts **statistiques** répétés.
- **L'écart entre pays** (Brésil/États-Unis ≈ 77 % du coût UE en 2017) vient surtout du prix de l'aliment (24 €/100 kg contre 31 €/100 kg) (EV-E-0016). Les surcoûts réglementaires européens ne pèsent que 5,0 c€/kg vif, soit 6,1 % (EV-E-0017).
- **Volatilité.** Le coût standard français a augmenté de 23,5 % en 2022 (aliment +27 %, poussin +27,2 %) pour atteindre un niveau record sur 30 ans (EV-E-0020). Tout comparateur « poulet » doit donc être daté.
- **Systèmes différenciés.** Pour la même année et la même méthode, Label Rouge ≈ 2,0 × et bio ≈ 2,7 × le standard par kg vif (EV-E-0019). L'indice de consommation (IC) passe de 1,61 à 3,04-3,08 et l'âge d'abattage de 36 à 84-88 jours.
- **Lacune.** Il n'existe pas d'édition plus récente de l'étude internationale Wageningen/AVEC : l'AVEC annonçait une nouvelle étude « début 2026 » sur des données 2024, que je n'ai pas trouvée. Les sources agri benchmark (Thünen) et USDA ERS n'ont pas fourni de série exploitable pendant cette session.

### 2.3 Conversion en coût par kg de viande et par kg de protéine (modèle E)

Le modèle convertit le coût par kg vif en coût par kg de viande désossée. Il ajoute l'abattage (0,21-0,38 €/kg carcasse, Q-E-0027), suppose un rendement carcasse de 0,70 (Q-E-0049) et un rendement en viande désossée de 43,1-47 % du poids vif (Q-N-0014, déclaration Aviagen ; Q-N-0035, revue). La teneur en protéines retenue est de 18-25 % (Q-E-0052). **Tous les coûts sont imputés à la viande**, ce qui surestime son coût puisque la valeur des coproduits est ignorée. La découpe est exclue, ce qui le sous-estime.

| Système | €/kg viande désossée | €/kg protéine | idem en USD de la même année |
|---|---|---|---|
| UE standard 2017 | 2,07-2,53 | 8,3-14,1 | 9,3-15,9 |
| Brésil 2017 | 1,66-2,08 | 6,6-11,6 | 7,5-13,1 |
| France standard 2022 | 3,00-3,55 | 12,0-19,7 | 12,6-20,8 |
| France Label Rouge 2022 | 5,60-6,38 | 22,4-35,5 | 23,6-37,3 |
| France bio 2022 | 7,47-8,43 | 29,9-46,8 | 31,5-49,3 |

(Sorties de modèle, Q-E-0070 et `results.md`.) **Point de méthode.** L'agent A rapporte environ 4,6 USD/kg de protéine sèche pour le poulet **départ ferme**, sur la base de l'animal entier (EV-A-0042). Mon calcul, rapporté à la seule viande désossée, donne 2 à 3 fois plus. Ce n'est pas une contradiction mais une différence de base de calcul, qui doit être fixée avant toute comparaison entre voies (voir § 9).

---

## 3. RQ-E2 / RQ-X1 (voie B) — TEA de la viande cultivée

### 3.1 Tableau comparatif des TEA

| Étude | Espèce | Financement / conflit | Échelle modélisée | Densité supposée | Milieu | Cycle | Coût résultant | Leviers principaux | Nature | Réf. |
|---|---|---|---|---|---|---|---|---|---|---|
| Humbird 2021 | cellules animales génériques | Open Philanthropy | 24 × 20 m³ fed-batch, 6,8 kt/an ; 96 × 2 m³ perfusion, 6,9 kt/an | limite NH3 110 g/L ; perfusion 195 g/L ; max. physique 258 g/L | acides aminés purifiés (19 $/kg) + facteurs de croissance (3 $/kg) à 100 kt/an mondial | fed-batch / continu | **37 $/kg** (fed-batch), **51 $/kg** (perfusion), ~22 $/kg avec hydrolysat ; TCI 328 / 663 M$ | acides aminés, CAPEX (salles blanches), métabolisme | sortie de modèle, base masse humide | EV-E-0001-0004, Q-E-0001-0009 |
| Risner et al. 2021 | bœuf | UC Davis, fonds publics | 1 % du bœuf US (121 kt) ; CAPEX des seuls bioréacteurs | 10⁷ à 2 × 10⁸ cellules/mL | E8 (2019) → facteurs de croissance gratuits | doublement 24 → 8 h ; maturation 240 → 24 h | **437 000 → 1,95 $/kg** (scénarios 1 à 4) | prix du FGF-2, densité, temps de doublement | sortie de modèle (coût minimal) | EV-E-0005, Q-E-0010-0012 |
| CE Delft (Vergeer et al.) 2021, corrigendum | générique | commandé par le GFI ; données d'environ 15 entreprises | 10 kt/an : 130 STR de 10 m³ + 430 réacteurs de perfusion de 2 m³ ; 450 M$ | 50 × 10⁶ cellules/mL (scénario « densité élevée » supprimé car physiquement impossible) | prix actuels → protéines recombinantes et facteurs de croissance bon marché | 42 j | **22 421 → 6,43 $/kg** (5,66 $/kg dans la version de février 2021) | milieu puis CAPEX ; délai de retour de 4 → 30 ans | sortie de modèle | EV-E-0022-0023, Q-E-0033-0036 |
| Negulescu et al. 2023 | bœuf | fonds publics US | 100 kt/an au total ; STR 42 kL / STR 211 kL / airlift 262 kL | non lue | non lue | non lue | **35 / 25 / 17 $/kg** (COGS) | taille des réacteurs, airlift | sortie de modèle (résumé seul) | EV-E-0012, Q-E-0021 |
| Pasitka et al. 2024 | **poulet** (fibroblastes) | équipe Believer Meats | usine théorique de 50 000 L | **mesurée** : jusqu'à 130 × 10⁶ cellules/mL, 43 % m/v, plus de 20 j | 0,63 $/L, sans composant animal (déclaration) | perfusion continue TFF | **6,2 $/lb (≈ 13,7 $/kg)** dans le résumé ; 23,26-27,24 $/kg selon une revue | perfusion, densité | mesure (densité) + sortie de modèle (coût) | EV-E-0013-0014, Q-E-0018-0020, Q-E-0045 |
| Garrison et al. 2022 | générique | Oklahoma State | non lue | — | — | — | ≥ 63 $/kg (d'après la revue Bry-Chevalier) | — | sortie de modèle (métadonnées seules) | SRC-E-0029, Q-E-0046 |
| Goodwin et al. 2024 (revue de cadrage) | — | — | — | les TEA supposent des STR ≥ 20 000 L et des lignées en suspension | — | — | la viande cultivée a « peu de chances » d'être compétitive dans le paradigme actuel | milieux végétaux, aseptie de qualité alimentaire | revue (résumé) | EV-E-0011 |
| Sun et al. 2024 (Chine) | — | Institut du MARA | capacités déclarées de 500-1 000 L en Chine | — | — | — | pas de TEA chinoise ; prix déclarés (Future Meat volaille 17 $/kg, 2021) | — | revue + déclarations | EV-E-0049-0050, Q-E-0053-0054 |

Aucune TEA **japonaise** ou **coréenne** n'a été trouvée (J-STAGE : 10 résultats pour 培養肉, aucun TEA). La revue de Bry-Chevalier 2026 recense six TEA académiques. Le milieu y représente 40 à 99 % des coûts selon les études (EV-E-0042). Le CAPEX nécessaire pour remplacer 1 % du bœuf américain est estimé entre 1,58 et 5,45 Md$ (EV-E-0043).

### 3.2 Lecture critique

1. **Mesuré vs supposé.** Seule la densité de Pasitka (130 × 10⁶ cellules/mL, plus de 20 jours) est une mesure (EV-E-0013), réalisée par l'équipe d'une entreprise et non répliquée. Tous les coûts sont des sorties de modèle. Le prix du milieu de 0,63 $/L est une déclaration.
2. **La dispersion des résultats est de cinq ordres de grandeur.** Elle vient de quatre hypothèses : (i) le prix et la quantité de milieu ; (ii) la qualité d'hygiène, salles blanches selon Humbird ou « qualité alimentaire » sans salle blanche selon CE Delft ; (iii) le coût du capital, de 14,6 %/an pour Humbird à un délai « social » de 30 ans pour CE Delft ; (iv) la densité et la productivité.
3. **Les chiffres de presse remontent à une même TEA.** Les « 5,66 $/kg » (ou « 2,57 $/lb ») de 2021 viennent de CE Delft/GFI avant corrigendum (6,43 $/kg après). Un article espagnol les transforme en « 2,50 $ par kilo » (EV-E-0058). Les « 6,2 $/lb » de 2024 proviennent du seul résumé de Pasitka et al. (EV-E-0014).
4. **Échec industriel de l'auteur de la TEA la plus optimiste sur le poulet.** Believer Meats, dont l'équipe a publié Pasitka et al., a cessé ses activités en décembre 2025. Son usine de Caroline du Nord (~150 M$ selon la presse), approuvée par l'USDA en novembre 2025, était en administration judiciaire et sans repreneur en août 2026 ; aucune source consultée ne documente de production commerciale (EV-E-0047, EV-E-0055, corrigés après vérification indépendante). Cela ne réfute pas les données de laboratoire, mais montre qu'une projection de TEA n'a pas suffi à financer l'exploitation.

---

## 4. Modèle économique transparent (agent E)

**Construction.** Le coût par kg de masse cellulaire humide en sortie de bioréacteur s'écrit : intensité capitalistique × (facteur de recouvrement + 9 % de frais fixes) / taux d'utilisation + milieu + autres OPEX. Le modèle reproduit Humbird 2021 : 36,4 $/kg contre 37 en fed-batch, 51,7 $/kg contre 51 en perfusion (calibration). Pour la conversion en protéine, la masse humide est supposée contenir 30 % de matière sèche, elle-même à 70 % de protéines, soit 21 % (Q-E-0050, Q-E-0051).

| Paramètre | Prudent | Intermédiaire | Optimiste | Référence |
|---|---|---|---|---|
| TCI, $ par (kg/an) de capacité | 96,1 (Humbird perfusion) | 48,2 (Humbird fed-batch) | 12,7 (Believer, capacité jamais démontrée) | Q-E-0004 ; Q-E-0003 ; Q-E-0048/0047 |
| Recouvrement du capital (/an) | 0,146 (implicite Humbird) | 0,102 | 0,033 (délai 30 ans) | dérivé Q-E-0003 ; model_assumption ; model_assumption (CE Delft) |
| Frais fixes (/an du TCI) | 0,09 | 0,09 | 0,09 | SRC-E-0001 |
| Utilisation | 0,75 | 0,90 | 0,95 | model_assumption |
| Milieu ($/kg humide) | 22 | 7 (hydrolysat) | 4 (facteurs de croissance gratuits) | Q-E-0005 ; dérivé Q-E-0001/0006 ; model_assumption |
| Autres OPEX ($/kg) | 8 | 3 | 2 | SRC-E-0001 ; model_assumption |

**Résultats (sorties de modèle, USD ≈ 2018-2020).**

| Scénario | $/kg masse humide | $/kg protéine | €2020/kg protéine |
|---|---|---|---|
| Prudent | 60,3 | 287 | 251 |
| Intermédiaire | 20,3 | 97 | 85 |
| Optimiste | 7,7 | 36 | 32 |

**Sensibilité.** Autour du scénario intermédiaire, le coût du milieu (amplitude 18,0 $/kg) et l'intensité capitalistique (17,8 $/kg) dominent. Viennent ensuite le recouvrement du capital (6,1), les autres OPEX (6,0) et l'utilisation (2,6) (Q-E-0072). Le tirage Monte-Carlo illustratif (lois triangulaires) donne P5/P50/P95 = 17,6/26,2/36,3 $/kg humide. Aucun tirage n'atteint le coût protéique du poulet standard UE, ni même le haut de plage Label Rouge ou bio. Cela traduit la position des hypothèses publiées, pas une probabilité réelle.

**Seuils de parité.** Pour égaler le poulet standard UE 2017 en coût par kg de protéine, la masse cellulaire humide devrait coûter au plus 3,3 $/kg (7,8 $/kg pour le Label Rouge, 10,4 $/kg pour le bio ; Q-E-0071). Or, même avec un capital gratuit, milieu et autres OPEX du scénario optimiste font déjà 6 $/kg (EV-E-0059). **Conclusion modélisée** : la parité avec le poulet standard n'apparaît dans aucune combinaison d'hypothèses publiées. Un recouvrement avec les segments label/bio n'apparaît que si toutes les hypothèses optimistes se réalisent ensemble. Ce résultat rejoint la formulation de Pasitka (« within the range of organic chicken ») et la revue de Goodwin (EV-E-0011).

**Paramètre caché.** Au prix déclaré de 0,63 $/L, le coût du milieu varie de 1,5 $/kg (2,3 L/kg, minimum physique à 43 % m/v sans renouvellement) à 31,5 $/kg (50 L/kg). Aucune source lue ne publie la consommation réelle de milieu par kg en perfusion (lacune critique).

---

## 5. RQ-E3 (voie C) — Coûts et capacités des substituts

| Produit | Valeur | Base | Nature | Réf. |
|---|---|---|---|---|
| Protéine de bactéries oxydant l'hydrogène (Power-to-SCP), 2028, meilleurs sites | 5,5-6,1 €/kg | protéine | sortie de modèle, co-auteurs de Solar Foods | EV-E-0046, Q-E-0041 |
| idem, Finlande | > 7,3 €/kg | protéine | sortie de modèle | Q-E-0041 |
| Électricité Power-to-SCP 2030 | 70-73 kWh/kg | protéine | sortie de modèle | Q-E-0042 |
| CAPEX première usine e-SCP (16,4 kt/an) | 14 567 € par t de protéine et par an | installation | sortie de modèle | Q-E-0043 |
| Solar Foods Factory 01 | 160 t/an nominales, 1 g/L/h ; objectif 230 t en 2026 | installation | déclaration d'entreprise | EV-E-0054, Q-E-0055-0056 |
| Isolat de soja / de pois | 1,8-8,1 / 3,5-9,3 €/kg | protéine | prix de marché (pas un coût) | Q-E-0065 |
| Mycoprotéine (TEA citée) | 3,55 $/kg | base inconnue | sortie de modèle, source primaire non retrouvée | EV-E-0045, Q-E-0066 |

**Constat.** Il n'existe pas de TEA publique d'extrusion humide (requête EPMC : 148 résultats, aucun TEA). L'agent A confirme l'absence de TEA publique de mycoprotéine et de données énergétiques industrielles d'extrusion. Les substituts se comparent donc au poulet au niveau de l'**ingrédient protéique**, pas du produit fini. L'électricité nécessaire à l'e-SCP (environ 70 kWh/kg de protéine) relie directement sa compétitivité au prix de l'électricité renouvelable, comme pour la viande cultivée (Sinke : énergie du site = premier poste GES).

---

## 6. RQ-E4 / RQ-X2 — ACV des trois voies, par kg de produit et par kg de protéine

| Système | kg CO2-eq par kg de produit (base) | kg CO2-eq par kg de protéine (conversion E) | Nature | Réf. |
|---|---|---|---|---|
| Poulet conventionnel NL, avec LUC | 3,65 / kg vif | 31-47 (100 % imputé à la viande) | ACV (sortie de modèle) | EV-E-0008, Q-E-0015 |
| Poulet croissance lente BLS NL, avec LUC | 3,55 / kg vif | 30-46 | ACV | Q-E-0016 |
| Poulet conventionnel NL, soja à faible LUC | 1,37 / kg vif | 12-18 | ACV | EV-E-0009, Q-E-0017 |
| Poulet « ambitieux » 2030 / actuel / moyenne mondiale 2018 | 2,7 / 6,0 / 9,0 par kg de viande | 11-15 / 24-33 / 36-50 | ACV | Q-E-0039 |
| Viande cultivée 2030 : renouvelable total / sur site / mix mondial | 2,8 / 4,0 / 14,3 par kg | 11-16 / 16-22 / 57-79 | ACV ex ante (GFI) | EV-E-0024, Q-E-0037-0038 |
| Viande cultivée, pire cas Sinke | 24,8 par kg | — | ACV ex ante | EV-E-0025 |
| Viande cultivée, Risner 2025 (intrants purifiés) | 246-1 508 par kg (12-1 508 tous scénarios) | 57-7 181 | ACV ex ante | EV-E-0006, Q-E-0013-0014 |
| Extrudés végétaux (intermédiaires) | 7,7-7,9 par kg (revue) | — | revue | EV-E-0010 |
| Mycoprotéine | 0,73 par kg (revue de 5 ACV) — contredit par une ACV 2015 qui la classe parmi les plus impactants | — | revue / ACV | EV-A-0050 vs EV-A-0049 |

**Lecture.**
- **Énergie et pureté des intrants décident du résultat pour la viande cultivée.** Avec un mix renouvelable et des intrants de qualité alimentaire, elle rejoint au mieux le poulet « ambitieux » (2,8 contre 2,7, EV-E-0024). Avec le mix mondial, elle le dépasse de plus de cinq fois. Avec des intrants de qualité pharmaceutique, l'écart atteint deux à trois ordres de grandeur (EV-E-0006).
- **Pour le poulet, le changement d'affectation des sols (LUC) du soja domine** (plus de 50 % des émissions). Il inverse même le classement entre systèmes conventionnel et à croissance lente (EV-E-0009).
- **Terres.** Sinke estime l'IC biotique de la viande cultivée environ trois fois meilleur que celui du poulet (1,0 contre 2,8 kg MS/kg de viande, EV-E-0026). Mais l'énergie métabolique de l'animal y est remplacée par de l'énergie externe.
- **Les chiffres fondateurs les plus cités sont obsolètes.** Les 1,9-2,2 kg CO2-eq/kg de Tuomisto 2011 reposent sur un milieu à base d'hydrolysat de cyanobactéries qui n'existe pas (EV-E-0007).

---

## 7. RQ-E5 — Infrastructures, CAPEX, passage à l'échelle et installations réelles

| Entreprise / site | Voie | Volume / équipement | Statut (date) | Nature | Réf. |
|---|---|---|---|---|---|
| Believer Meats, Wilson (Caroline du Nord, États-Unis) | B (poulet) | 200 000 pieds², ~150 M$, 26 Mlb/an (≈ 11,8 kt) annoncées | **construite**, approuvée par l'USDA (nov. 2025) ; entreprise fermée (déc. 2025) ; usine en administration judiciaire, sort non réglé (août 2026) ; offre de rachat d'UPSIDE de 50 M$ retirée ; aucune production commerciale documentée | presse ; capacité = déclaration | EV-E-0047, SRC-E-0031, SRC-P-0004 |
| UPSIDE Foods, Glenview (Illinois) | B (poulet) | grande usine prévue | **suspendue** (févr. 2024) ; filets produits en flacons de 2 L (2023) | presse (relevée par l'agent P) | SRC-P-0009 |
| UPSIDE Foods, Emeryville (Californie) | B | 22 680 kg/an annoncés | en fonctionnement (pilote) | déclaration compilée | SRC-E-0034 |
| GOOD Meat / Eat Just + ABEC | B (poulet) | 10 × 250 000 L prévus → 5 × 125 000 L (nov. 2022) | **abandonné** ; litige réglé pour 4,4 M$ | presse (agent P) | SRC-P-0007, SRC-P-0008 |
| GOOD Meat, Singapour | B (poulet) | hybride à 3 % de cellules au détail | vendu (2024) | communication d'entreprise (agent A) | SRC-A-0034 |
| Eat Just | B | 6 000 L | déclaré | déclaration compilée | SRC-E-0034 |
| Mosa Meat ; Aleph Farms ; Future Meat | B | 1 000 L ; 180 t/an annoncées chacune | annoncé | déclarations compilées | SRC-E-0034 |
| Joes Future Food ; CellX ; 佰鸿 (Chine) | B | 500 L (2019) ; 1 000 L (2020) ; 1 000 L (2023) | pilote | déclarations compilées | EV-E-0050 |
| Meatable (Pays-Bas) ; SCiFi Foods (États-Unis) ; Upstream Foods ; CellRev | B | — | **fermées** (2024-2025) faute de financement | presse | EV-E-0048 |
| Solar Foods Factory 01, Vantaa (Finlande) | C (SCP) | 160 t/an nominales → 230 t (2026) ; Factory 02 prévue en 2028 | en fonctionnement (paramètres nominaux atteints, production non publiée) | déclaration d'entreprise | EV-E-0054 |

**Synthèse.** Les TEA dimensionnent des usines de 6,8 à 10 kt/an (EV-E-0001, EV-E-0022). Or les capacités réellement opérées en viande cultivée restent de l'ordre de 10³ L, et 20 à 180 t/an sont annoncées (EV-E-0050). Aucune production commerciale n'est documentée dans la seule grande usine construite pour le poulet (EV-E-0055). Le coût de construction de Believer, environ 12,7 $ par kg de capacité annuelle déclarée, est très inférieur aux 45-48 $ des TEA. Mais cette capacité n'a pas été démontrée : c'est la valeur « optimiste » du modèle, à ne pas lire comme un CAPEX prouvé. Côté contraintes sanitaires, FSANZ juge qu'une approche HACCP complète, surtout pendant l'expansion cellulaire, est indispensable (EV-E-0037). Humbird chiffre le coût des salles blanches (40 M$ sur 178 M$ de coûts directs en fed-batch, tableau 2). CE Delft suppose au contraire une hygiène « qualité alimentaire » sans salle blanche (EV-E-0023). C'est l'hypothèse non testée la plus coûteuse du secteur.

---

## 8. RQ-E6 / RQ-X4 — Réglementation par juridiction (textes officiels datés)

Légende : **ING** = autorisation d'un ingrédient ; **PROC** = exigences liées au procédé ou à l'installation ; **PROD** = autorisation d'un produit précis.

| Juridiction | Texte / acte (date) | Ce qui est autorisé ou interdit | Type | Réf. |
|---|---|---|---|---|
| UE | Règlement (UE) 2015/2283 (25/11/2015, applicable au 1/1/2018) : art. 3(2)(a)(vi) culture cellulaire/tissulaire ; (ii) micro-organismes, champignons, algues ; avis EFSA en 9 mois, acte de la Commission en 7 mois ; protection des données 5 ans | autorisation préalable par inscription sur la liste de l'Union (générique, avec spécifications) ; au début 2025, une seule demande de viande cultivée (Gourmey, 2024) | PROD (+ spécifications de procédé) | EV-E-0027, EV-E-0028, EV-E-0039 |
| UE (aliment animal) | Règlement (UE) 2021/1372 (17/08/2021) | protéines animales transformées d'insectes autorisées pour volailles et porcs | ING | EV-E-0029 |
| Italie | Loi n° 172 du 1/12/2023 (en vigueur au 16/12/2023) | interdiction de produire, vendre, importer, **produire pour l'export** des aliments et aliments pour animaux issus de cultures cellulaires de vertébrés ; amendes de 10 000 à 150 000 € ; interdiction des dénominations « viande » pour les produits végétaux | interdiction PROD + PROC | EV-E-0030, EV-E-0031 |
| France | Rapport du Sénat n° 504 (avril 2023) ; propositions de loi AN n° 1965 (5/12/2023) et n° 2172 (13/02/2024) | recommandations : interdiction avant autorisation UE, taxation des bioréacteurs de plus de 25 000 L, interdiction des mélanges cellules/viande ; pas de loi adoptée trouvée | — (politique) | EV-E-0056 |
| États-Unis (fédéral) | Accord FDA–USDA-FSIS (mars 2019) ; inventaire des consultations FDA | UPSIDE (poulet, 16/11/2022), GOOD Meat (poulet, 20/03/2023), Mission Barns (graisse de porc, 07/03/2025), Wildtype (saumon, 28/05/2025), Believer (poulet, 24/07/2025) | PROD + PROC (par entreprise) + inspection de l'établissement | EV-E-0034 |
| Floride | Fla. Stat. § 500.452 (ch. 2024-137) | interdiction de fabriquer pour la vente, vendre, distribuer ; délit de 2e degré | interdiction | EV-E-0032 |
| Texas | SB 261 (effet du 1/9/2025 au 1/9/2027) | interdiction temporaire de l'offre et de la vente ; étiquetage « cell-cultured »/« lab-grown » | moratoire | EV-E-0033 |
| Autres États américains | Alabama, Mississippi, Montana, Indiana (moratoire 2025-2027), Nebraska, Dakota du Sud | **non vérifié sur textes officiels** (sources secondaires contradictoires) | — | journal de recherche |
| Singapour | SFA, *Requirements for the Safety Assessment of Novel Foods* (1re version 22/11/2019, révision 17/03/2025) | nouvel aliment = moins de 20 ans d'usage ; dossier sur lignées, milieux, échafaudages, asepsie ; **toute modification des lignées ou du milieu exige une nouvelle approbation** ; étiquetage « cultured »/« cell-based » | PROD + PROC | EV-E-0035 |
| Royaume-Uni | FSA, bac à sable des produits cellulaires (mars 2025-février 2027) | 2 demandes en évaluation des risques (févr. 2026) ; objectif de délai d'environ 2,5 ans ; aliment pour animaux de compagnie (Meatly, 2024) autorisé selon la presse | PROD | EV-E-0038 |
| Israël | Ministère de la Santé, janvier 2024 | lettre « no questions » pour le bœuf d'Aleph Farms ; audit BPF requis | PROD + PROC (presse seulement) | EV-E-0041 |
| Australie / Nouvelle-Zélande | FSANZ A1269, rapport d'approbation du 7/04/2025 ; normes 1.5.4 et 3.4.1, annexe 25A | caille cultivée (Vow) ; catégorie dédiée « cell-cultured food » ; A1341 (canard de Gourmey) en consultation (2026) | PROD (annexe) + PROC (norme 3.4.1) | EV-E-0036, EV-E-0037, EV-E-0057 |
| Corée du Sud | MFDS : normes temporaires (révision 2024) ; projet d'amendement du Food Code (30/06/2026) | reconnaissance d'ingrédient (environ 270 jours ouvrés, presse) + catégorie « aliments transformés à base de cellules cultivées » ; aucune approbation trouvée | ING + catégorie | EV-E-0040, EV-E-0053, EV-E-0057 |
| Chine | Plan du MARA (2021, 14e plan quinquennal) ; procédure 新食品原料 (NHC) | soutien de planification ; aucune approbation ; aucun texte spécifique trouvé | — | EV-E-0049 |
| Japon | — | pas de cadre spécifique (2024) ; question d'interprétation du droit existant (細胞性食品) | — | EV-E-0051 |
| Brésil | ANVISA RDC n° 839 (14/12/2023, en vigueur au 16/03/2024) | cultures de cellules ou de tissus et produits de fermentation = nouveaux aliments ; autorisation préalable ; dossier avec milieux, pureté, stabilité génétique | PROD/ING + PROC | EV-E-0052 |
| Suisse | demande d'Aleph Farms (presse) | non vérifié sur source officielle | — | SRC-E-0032 (notes) |

**Conséquences économiques de la réglementation.**
1. **Optimiser le procédé coûte une nouvelle autorisation.** Les leviers de coût les plus puissants des TEA (changer de milieu, d'hydrolysat, de lignée) déclenchent à Singapour une nouvelle approbation (EV-E-0035). Aux États-Unis, la consultation et l'inspection sont également propres à l'entreprise et à son procédé.
2. **Les délais réglementaires sont longs.** Le minimum légal est de 16 mois dans l'UE hors suspensions (EV-E-0028). Il a fallu environ 26 mois chez FSANZ (Q-E-0060), et l'objectif britannique est d'environ 2,5 ans (Q-E-0057).
3. **Le risque politique est distinct du risque scientifique** : interdictions italienne et texanes, vote des États membres en comité PAFF (EV-E-0039), recommandation française d'interdire les hybrides cellules/viande (EV-E-0056).
4. **Pour la voie A**, l'autorisation des insectes en aliment volaille (EV-E-0029) est une autorisation d'**ingrédient**, beaucoup plus légère.

---

## 9. Contradictions repérées

| # | Côté 1 | Côté 2 | Explication probable / à vérifier |
|---|---|---|---|
| 1 | Pasitka (résumé) : 6,2 $/lb ≈ 13,7 $/kg (EV-E-0014) | revue Bry-Chevalier : Pasitka 23,26-27,24 $/kg (EV-E-0042) | base différente (produit hybride contre biomasse) ; texte intégral nécessaire |
| 2 | Pasitka : 43 % m/v de biomasse (EV-E-0013) | Humbird : plafond de 258 g/L (fraction volumique 0,25) (EV-E-0003) | cellules de poulet plus petites et/ou définition de « m/v » (biomasse tassée) ; à vérifier |
| 3 | CE Delft : 6,43 $/kg en 2030 (EV-E-0022) | Humbird : 22-51 $/kg (EV-E-0001-0002) | hygiène qualité alimentaire contre salles blanches ; coût du capital sur 30 ans contre 14,6 %/an |
| 4 | Sinke : 2,8-14,3 kg CO2-eq/kg (EV-E-0024) | Risner : 246-1 508 kg pour des intrants purifiés (EV-E-0006) | pureté des intrants (facteur de purification 20×) et mix énergétique |
| 5 | Poulet à croissance lente moins émetteur avec LUC (EV-E-0008) | plus émetteur avec un soja à faible LUC (EV-E-0009) | choix méthodologique (LUC) |
| 6 | Presse : « 2,50 $/kg » (EV-E-0058) | rapport CE Delft : 6,43 $/kg (EV-E-0022) | déformation (confusion livre/kilo probable) |
| 7 | Consultation FDA favorable (EV-E-0034) | interdictions en Floride et au Texas (EV-E-0032, EV-E-0033) | conflit entre niveaux fédéral et étatique |
| 8 | Mycoprotéine : 0,73 kg CO2e/kg (EV-A-0050) | mycoprotéine parmi les plus impactants (EV-A-0049) | unité fonctionnelle et énergie de fermentation (agent A) |
| 9 | Poulet ≈ 4,6 $/kg de protéine (animal entier, départ ferme ; EV-A-0042) | 9,3-15,9 $2017 (8,3-14,1 €2017) par kg de protéine pour la viande désossée (modèle E, Q-E-0070) | base de calcul (animal entier contre viande désossée, prix contre coût) |

---

## 10. Ce qui fonctionne, ce qui échoue, ce qui reste à inventer

**Fonctionne (démontré).**
- Voie A : coûts statistiques stables et faibles (0,63-0,86 €/kg vif standard en 2017 ; 1,26 € en France en 2022), dominés par l'aliment.
- Voie B : densités élevées en perfusion à l'échelle laboratoire/pilote (EV-E-0013) ; autorisations de produits dans 5 juridictions (États-Unis, Singapour, Israël, Australie/Nouvelle-Zélande, plus le Royaume-Uni pour l'aliment pour animaux de compagnie).
- Voie C : fermentation gazeuse à l'échelle de 160 t/an (déclarée).

**Échoue (documenté).**
- Passage à l'échelle des usines de viande cultivée : Believer (usine construite et approuvée, exploitant fermé en décembre 2025, aucune production commerciale documentée), Glenview (suspendue), projet de bioréacteurs ABEC (abandonné), vague de fermetures en 2024-2025 (EV-E-0047, EV-E-0048).
- Les TEA ne convergent pas : aucune ne prévoit la parité avec le poulet standard hors scénarios où toutes les limites sont levées.

**Reste à inventer.**
- Un milieu à moins de 10 L par kg de masse humide à moins de 1 $/L, validé sur plus de 20 jours.
- Une aseptie de qualité alimentaire validée à plus de 10 m³.
- Des données de procédé publiques (consommation de milieu, taux de contamination, utilisation réelle).
- Une TEA publique de l'extrusion et de la mycoprotéine.
- Un cadre réglementaire permettant de modifier un milieu sans réautorisation complète.

---

## 11. Lacunes (cherché sans succès)

- Étude internationale des coûts du poulet postérieure à 2017 (AVEC/Wageningen 2026 annoncée, non trouvée) ; séries USDA ERS et agri benchmark non obtenues ; aucune série argentine ou mexicaine récente.
- Texte intégral de Pasitka 2024, Negulescu 2023, Garrison 2022 et Goodwin 2024 (paywall).
- TEA primaire de la mycoprotéine (réf. 102 de Bry-Chevalier introuvable) et de l'extrusion humide (aucune) ; capacités de Quorn (Billingham) et de Calysseo (Chongqing) non retrouvées.
- ACV de la viande cultivée **spécifique au poulet** : aucune (EPMC, 39 résultats).
- TEA de viande cultivée chinoise, japonaise ou coréenne : aucune trouvée.
- Textes primaires du MFDS (Corée), de la NHC (Chine), de l'OSAV (Suisse), du ministère de la Santé israélien ; registre OpenEFSA (statut des dossiers Gourmey et Mosa Meat).
- Volumes de milieu par kg et taux de contamination à l'échelle industrielle (aucune donnée publique).

---

## 12. Pistes d'innovation

### Piste E-1 — Mesurer et réduire le « litre de milieu par kg », paramètre caché des TEA
- **Problème** : le milieu représente 40 à 99 % du coût (EV-E-0042). Au prix déclaré de 0,63 $/L, son coût varie d'un facteur 20 selon la consommation (2,3 à 50 L/kg, modèle E). Aucune source ne publie cette consommation.
- **Solutions actuelles** : perfusion TFF (EV-E-0013) ; récupération du lactate (Wimble et al. 2026, sortie de modèle) ; hydrolysats (Humbird).
- **Insuffisances** : bilans matière non publiés ; recyclage limité par l'ammoniac et le lactate (Humbird : limite NH3).
- **Preuves en faveur** : densités élevées de 130 × 10⁶ cellules/mL sur plus de 20 jours (EV-E-0013) ; récupération du lactate jugée rentable en modèle.
- **Hypothèse** : une perfusion couplée à l'élimination continue de NH3 (échange d'ions ou membrane) et au recyclage de plus de 50 % du milieu réduit la consommation à 10 L/kg ou moins sans réduire la croissance.
- **Expérience** : bioréacteurs de 2-10 L avec fibroblastes de poulet, 3 conditions (perfusion simple ; perfusion avec recyclage ; recyclage avec élimination de NH3), 21 jours, triplicats. Mesures : L/kg, densité, viabilité, NH3, lactate, stabilité génétique.
- **Critères** : succès = 10 L/kg ou moins avec une productivité d'au moins 80 % du témoin ; échec = plus de 25 L/kg ou dérive génétique.
- **Coûts et risques** : environ 6-12 mois de travail d'équipe en laboratoire ; risque d'accumulation de métabolites non identifiés ; un changement de milieu implique une réautorisation à Singapour (EV-E-0035).

### Piste E-2 — Tester l'hypothèse « qualité alimentaire sans salle blanche »
- **Problème** : la qualité d'hygiène sépare Humbird (salles blanches de classe 8, TCI de 48 $ par kg/an) de CE Delft (qualité alimentaire). Ce choix pèse environ 17,8 $/kg dans la tornade.
- **Solutions actuelles** : CIP/SIP, cuves pressurisées, stérilisation HTST (modèle CE Delft).
- **Insuffisances** : aucune statistique publique de taux de contamination des cultures de cellules animales en environnement alimentaire ; FSANZ insiste sur la phase d'expansion (EV-E-0037).
- **Preuves** : les fermentations alimentaires aseptiques (enzymes, acides aminés) fonctionnent sans salle blanche (argument de CE Delft, non quantifié).
- **Hypothèse** : avec une conception CIP/SIP de type fermentation alimentaire et un milieu contenant un antimicrobien autorisé (ou sans), le taux de lots contaminés reste sous 2 % à 200-1 000 L.
- **Expérience** : campagne de 50 lots ou plus sur une ligne pilote de qualité alimentaire, avec surveillance microbiologique et analyse des causes ; comparaison au coût d'une salle blanche équivalente.
- **Critères** : succès = moins de 2 % de lots perdus, et le TCI estimé baisse d'au moins 25 % ; échec = plus de 5 %.
- **Coûts et risques** : CAPEX pilote élevé (dizaines de milliers à millions d'euros selon l'échelle) ; acceptabilité réglementaire à discuter avec la SFA/FSANZ en amont.

### Piste E-3 — Hydrolysats de tourteau de soja « qualité milieu » : un goulet commun aux voies A et B (RQ-X3)
- **Problème** : les acides aminés purifiés coûtent 19 $/kg de biomasse (EV-E-0004). Le tourteau de soja, base de l'aliment volaille, coûte 0,33 $/kg selon Humbird.
- **Solutions actuelles** : hydrolysats végétaux en complément (Humbird : hydrolysat supposé à 2 $/kg) ; algues et levures (littérature de l'agent C).
- **Insuffisances** : aucun hydrolysat ne constitue à ce jour un milieu complet (Humbird) ; endotoxines et variabilité des lots.
- **Hypothèse** : un hydrolysat enzymatique de tourteau de soja, purifié par ultrafiltration et complété en glutamine, couvre au moins 70 % des acides aminés d'un milieu pour fibroblastes de poulet pendant 10 passages, pour un coût inférieur à 3 $/kg d'acides aminés.
- **Expérience** : hydrolyse à 3 niveaux (protéase, durée), ultrafiltration, formulation, croissance sur 10 passages contre milieu de référence, coût de procédé estimé par mini-TEA.
- **Critères** : succès = au moins 80 % du taux de croissance du témoin, endotoxines sous le seuil fixé, coût inférieur à 3 $/kg ; échec = croissance inférieure à 60 % ou variabilité entre lots supérieure à 20 %.
- **Coûts et risques** : faible (laboratoire) ; risque de LUC du soja (EV-E-0009) qui transfère l'impact de la voie A à la voie B.

### Piste E-4 — Hybrides à faible taux de cellules : modèle économique et réglementaire
- **Problème** : la parité de coût est hors d'atteinte pour un produit 100 % cellules (modèle E). Les hybrides sont la voie de marché observée (3 % de cellules à Singapour, SRC-A-0034), mais la France envisage de les restreindre (EV-E-0056).
- **Hypothèse** : un hybride contenant 10-20 % de cellules de poulet apporte la note aromatique « poulet » perçue par les consommateurs, pour un surcoût de matière inférieur à 2-3 €/kg de produit dans le scénario intermédiaire.
- **Expérience (avec l'agent A)** : tests sensoriels triangulaires sur des matrices végétales texturées avec 0, 3, 10 et 20 % de biomasse cellulaire, plus un calcul de coût de mélange à partir du modèle E.
- **Critères** : succès = différence perçue à 10 % ou moins de cellules et surcoût sous le seuil ; échec = pas de différence perçue à 20 %.
- **Risques** : interdictions de mélange (France, recommandation 10), étiquetage.

---

## 13. Recherches restantes prioritaires

1. Obtenir le texte intégral de Pasitka 2024 : base du coût de 6,2 $/lb (produit hybride ou cellules), consommation de milieu par kg, définition de « 43 % m/v ».
2. Lire en intégralité Negulescu 2023, Garrison 2022 et Goodwin 2024 (tableau des hypothèses des TEA) ; retrouver la TEA primaire de la mycoprotéine et Upcraft 2021.
3. Actualiser les coûts du poulet (2023-2025) : étude AVEC/Wageningen 2026, ITAVI 2024-2025, USDA ERS/ARMS, agri benchmark ; série Embrapa officielle dès la levée des restrictions électorales.
4. Consulter directement le registre OpenEFSA (dossiers Gourmey, Mosa Meat, Solein), les textes de l'OSAV suisse, du MFDS coréen (projet du 30/06/2026), de la NHC chinoise et du ministère de la Santé israélien ; vérifier les lois des autres États américains sur les textes officiels.
5. ACV primaires : mycoprotéine (Quorn), Solein (Järviö 2021), FAO GLEAM pour le poulet par kg de protéine ; harmoniser la base « kg de protéine comestible » avec les agents N et A.
