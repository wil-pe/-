# Contradictions

Registre consolidé par le coordinateur à partir des handoffs et des tables. Chaque entrée : affirmations opposées (`EV-…`/`Q-…`), explication possible, arbitrage **provisoire**, vérification à faire.
Types : **S** = désaccord scientifique / de mesure · **M** = désaccord de modèle (hypothèses) · **B** = différence de base de calcul (pas une vraie contradiction) · **D** = documentaire (déclaration vs document) · **R** = réglementaire / juridique.

Dernière mise à jour : 2026-10-25 (agents A, C, E, H, N, P).

## Voie B — viande cultivée

| ID | Type | Sujet | Côté 1 | Côté 2 | Explication possible | Arbitrage provisoire | Vérification à faire |
|---|---|---|---|---|---|---|---|
| CT-01 | B/S | Teneur en protéines de la biomasse cultivée | 21 % de la masse humide : hypothèse de Humbird, reprise dans le modèle de l'agent E (Q-E-0050, Q-E-0051, EV-E-0059) | 9 g/100 g mesurés sur la biomasse de caille récoltée, ≥ 80 % d'eau (dossier FSANZ, EV-C-0020, EV-C-0074) | Hypothèse générique vs mesure réelle, mais sur une espèce voisine (caille) et chez une seule entreprise | **9 % retenu comme valeur centrale, 21 % comme borne optimiste.** Recalcul du coordinateur : 85/225/670 USD/kg de protéine (EV-X-0001, Q-X-0001 à Q-X-0004) | Composition de la biomasse de poulet dans les *safety narratives* de la FDA (CCC 000002, CCC 000039) ; mesures Kjeldahl + humidité sur DF-1 |
| CT-02 | B/D | Coût du poulet cultivé, Pasitka et al. 2024 | 6,2 USD/lb, soit ≈ 13,7 USD/kg (résumé, EV-E-0014, SRC-X-0001) | 23,26–27,24 USD/kg selon la revue de Bry-Chevalier 2026 (EV-E-0042, Q-E-0045) | Base différente : produit hybride vs biomasse 100 % cellulaire ? scénario différent ? | **Non tranché** : texte intégral non accessible (paywall) | Lire Pasitka 2024 (méthodes et données supplémentaires) : base du coût, L de milieu par kg, sens de « % p/v » |
| CT-03 | S/M | Densité cellulaire maximale | 108 puis 130 × 10⁶ cellules/mL, « 43 % p/v », en perfusion TFF de laboratoire (Q-C-0001, Q-C-0003, EV-C-0017, EV-E-0013) | Limite pratique modélisée de 86 × 10⁶ cellules/mL ; plafond physique de 258 g/L (Humbird, EV-C-0040, EV-E-0003) | Le modèle vise des cuves industrielles (transfert d'O₂, mélange) ; volume cellulaire supposé (3 000 pg) ; « p/v » peut désigner un culot humide avec liquide interstitiel | Démontré **au laboratoire par une seule équipe** (aussi relevé par l'agent P : EV-P-0040 vs EV-P-0041/0042), non démontré à l'échelle ; les deux chiffres ne portent pas sur la même échelle. Une revendication de brevet UPSIDE jusqu'à 10¹⁰ cellules/mL est physiquement impossible (EV-P-0002) | Méthodes de Pasitka 2024 ; réplication indépendante ; mesures d'O₂ par cellule de poulet |
| CT-04 | M | Rentabilité de la perfusion | Perfusion rentable dans la TEA Believer/Pasitka (EV-C-0018) | Perfusion plus chère que le fed-batch selon Humbird (EV-C-0039) ; fermeture de Believer en décembre 2025 (EV-C-0065, EV-E-0047) | Hypothèses de coût du milieu et de recyclage ; la fermeture peut avoir des causes financières, non techniques | Le modèle Believer n'est **pas validé** à l'échelle industrielle (usine jamais exploitée) ; la fermeture ne prouve pas l'échec technique | Causes documentées de la fermeture (agent P) ; TEA indépendante de la perfusion avec recyclage |
| CT-05 | D | Production sans sérum | SFA : approbation « sans sérum » de GOOD Meat en janvier 2023 (EV-C-0063) | Sérum de veau fœtal (FBS) dans le dossier FDA de GOOD Meat, mars 2023 (EV-C-0007) ; produit UPSIDE avec sérum (EV-C-0004) | Dossiers et versions de procédé différents ; approuver un procédé ≠ produire commercialement avec ce procédé | Les deux sont vrais pour des dossiers différents ; **aucune preuve d'un poulet cultivé sans sérum vendu aux États-Unis** | Dossiers SFA (non publiés) ; étiquetage FSIS |
| CT-06 | D | Facteurs de croissance | Believer déclare à la FDA une production sans facteurs de croissance (EV-C-0011) | FGF-2 + insuline dans le milieu Believer de 2023 (EV-C-0071) ; deux facteurs recombinants chez Vow (EV-C-0023) | Versions successives du milieu ; adaptation de la lignée | Possible pour une lignée adaptée, mais **non démontré dans une publication évaluée par les pairs avec composition complète** | Composition du milieu dans le mémo FDA/Believer et dans Pasitka 2024 |
| CT-07 | S | Facilité de l'immortalisation spontanée des fibroblastes de poulet | « Très rare » chez l'oiseau : DF-1 est un événement unique (EV-C-0036, EV-C-0067) | Reproductible selon Pasitka 2023 (EV-C-0015, EV-C-0019) | Protocoles différents (passages longs, sélection) ; biais de publication | Reproductible **dans un seul laboratoire** ; la stabilité génétique est affirmée par Future Meat (EV-P-0041) mais mise en doute par une revue de 2026 (EV-P-0063) | Réplication indépendante ; caryotype, séquençage longitudinal (INN-14) |
| CT-08 | M | Coût de la viande cultivée selon les TEA | Humbird : 37–51 USD/kg (EV-E-0001) | Risner : 437 000 → 1,95 USD/kg ; CE Delft : 22 421 → 6,43 USD/kg (EV-E-0005, EV-E-0022) | Hypothèses : qualité d'hygiène (pharmaceutique vs alimentaire), coût du capital, densité, prix du milieu | Les écarts viennent des hypothèses, **pas de mesures** ; aucune TEA n'est validée par une production réelle | Tableau des hypothèses par TEA (agent E) ; données réelles d'installation |
| CT-09 | M | ACV de la viande cultivée | Sinke : 2,8 (énergie 100 % renouvelable) à 14,3 (mix mondial) kg CO₂-éq/kg (EV-E-0024) | Risner : 246–1 508 kg CO₂-éq/kg avec intrants purifiés de qualité pharmaceutique (EV-E-0006) | Purification des intrants (élimination de l'endotoxine) et énergie | **Dépend du niveau de purification réellement exigé**, inconnu à ce jour | Spécifications réelles des intrants dans les dossiers réglementaires |

## Voies A et C — élevage et substituts

| ID | Type | Sujet | Côté 1 | Côté 2 | Explication possible | Arbitrage provisoire | Vérification à faire |
|---|---|---|---|---|---|---|---|
| CT-10 | B | Coût du poulet par kg de protéine | ≈ 4,6 USD/kg de protéine (animal entier, prix départ ferme, EV-A-0042) | 8,3–14,1 €2017/kg de protéine (viande désossée, modèle de l'agent E, Q-E-0070) | Base « animal entier » vs « viande désossée comestible » | **Viande désossée comestible** pour comparer des produits ; base animal entier seulement pour comparer des aliments du bétail | Harmonisation dans `comparison_framework.md` |
| CT-11 | B/M | ACV de la mycoprotéine | Parmi les plus impactantes (Smetana 2015, EV-A-0049) | 0,73 kg CO₂-éq/kg de produit (Shahid 2024, co-auteur industriel, EV-A-0050) | Bases de calcul (produit vs protéine), énergie, année, conflit d'intérêts | Non tranché | ACV primaires Quorn ; conversion sur base protéine |
| CT-12 | S | Taux d'insectes dans l'aliment du poulet | 28 % « recommandé » (EV-A-0024, Q-A-0041) | Dégradation des performances dès 10 % (EV-A-0032, Costa Rica) | Espèce d'insecte, dégraissage, âge, durée de l'essai, formulation | L'agent N ne tranche pas sur la performance, mais ajoute un argument environnemental défavorable : l'ACV des insectes est mauvaise quand le substrat n'est pas un vrai déchet (EV-N-0058) | Méta-analyse dose-réponse BSF par fraction (entière/dégraissée) et par âge |
| CT-13 | S | Aliments ultra-transformés végétaux et santé | Défavorables (Rauber 2024, EV-A-0022) | Bénéfice indépendant de l'ultra-transformation (Thompson 2026, EV-A-0023) | Même cohorte (UK Biobank), définitions et ajustements différents | Observationnel des deux côtés ; **aucune causalité établie** | Comparaison des modèles statistiques |
| CT-14 | S | Acceptabilité sensorielle des nuggets végétaux | Quasi-parité (NECTAR, EV-A-0026 ; rapport lu via la presse) | Nugget vegan le moins apprécié au Pérou (EV-A-0047) | Populations, produits et protocoles différents | Dépend du produit et du marché | Rapport NECTAR primaire |
| CT-20 | B | Efficience protéique nette du poulet (protéines consommables par l'humain produites / ingérées) | 0,88 pour le poulet standard français (Laisse et al., EV-N-0022) | ≈ 0,2 (Mottet et al., EV-N-0026) | **Définition** de la fraction « consommable par l'humain » des matières premières et pays différents ; la seule formulation de l'aliment fait varier l'indicateur de 0,8 à 2 (EV-N-0023) | Indicateur très sensible à la définition ; **toujours afficher la définition** | Recalcul des deux méthodes sur un même aliment |
| CT-21 | S | Régimes à basse protéine et rendement en filet | Aucun effet / baisse / hausse selon les essais (EV-N-0014, EV-N-0016, EV-N-0018) | — | Niveaux de réduction, acides aminés supplémentés (glycine+sérine), âge, souche | Effet **non généralisable** ; plancher vers 17 % de protéine brute en finition (EV-N-0019, EV-N-0020) | Méta-analyse avec ajustement glycine+sérine |
| CT-22 | S | Probiotiques et performances | Effet positif rapporté (EV-N-0039) | Effet fragile, non reproduit (EV-N-0040, EV-N-0041) | Souches microbiennes, conditions sanitaires, biais de publication | **Faible confiance** dans un gain généralisable d'IC | Essais multicentriques préenregistrés |
| CT-23 | S | Alimentation in ovo | Gains rapportés (EV-N-0051) | Absence d'effet durable (EV-N-0071) | Nutriments injectés, âge de mesure | Non tranché | Méta-analyse in ovo |
| CT-15 | M | Classement des systèmes avicoles en ACV | Ordre dépendant de la prise en compte du changement d'usage des sols (Mostert, EV-E-0008) | idem sans LUC (EV-E-0009) | Le LUC lié au soja domine | Toujours présenter les résultats **avec et sans LUC** | — |

## Histoire

| ID | Type | Sujet | Côté 1 | Côté 2 | Explication possible | Arbitrage provisoire | Vérification à faire |
|---|---|---|---|---|---|---|---|
| CT-16 | S | Poulets précolombiens (El Arenal, Chili) | Datation précolombienne (EV-H-0008) | Datation contestée (même entrée) | Contamination du radiocarbone par l'alimentation marine | Controversé ; **ne pas utiliser comme preuve** | Datations récentes |
| CT-17 | S | Verminières (production délibérée de larves) | Recommandées dans les textes anciens et au XIXᵉ s. (EV-H-0020, EV-H-0030) | Rejetées ensuite : odeur, goût de la viande, picage (EV-H-0032) | Problèmes d'hygiène et de goût, pas d'inefficacité nutritionnelle | Abandon pour **acceptabilité et hygiène**, pas pour inefficacité | Essais modernes de larves vivantes (piste H-1) |
| CT-18 | S | Termites *Trinervitermes* | Dites toxiques par des informateurs (EV-H-0051) | Genre le plus utilisé au Ghana (EV-H-0052) | Savoir local hétérogène | Non tranché | Analyses de composition et de toxicité |

## Brevets

| ID | Type | Sujet | Côté 1 | Côté 2 | Remarque |
|---|---|---|---|---|---|
| CT-24 | D | Statut juridique des brevets | Statuts affichés par Google Patents (EV-P-0019, EV-P-0020) | Statuts incohérents entre pages et familles | Google Patents n'est pas un registre officiel : vérifier les statuts sur les registres EPO/USPTO/CNIPA avant toute conclusion de liberté d'exploitation (INN-07) |

## Réglementaire

| ID | Type | Sujet | Côté 1 | Côté 2 | Remarque |
|---|---|---|---|---|---|
| CT-19 | R | États-Unis | Consultations de la FDA terminées pour du poulet cultivé (EV-E-0034) | Interdictions en Floride, permanente (EV-E-0032), et au Texas, 2025–2027 (EV-E-0033) | Divergence juridique fédéral/États, pas une contradiction scientifique |

## Corrections déjà appliquées par le coordinateur (traçabilité)

- EV-H-0044 : `patent_claim` + confiance `high` → `historical_documented` + `moderate` (fait historique daté ; rendements du brevet non vérifiés).
- EV-H-0045 : confiance `moderate` → `low` (source lue en métadonnées seulement).
- EV-E-0058 : `commercial_claim` → `documentary_verification` (comparaison directe d'un article de presse et du rapport primaire).
- SRC-A-0024 : `abstract_only` → `full_text_read` (texte intégral lu par l'agent E).
- EV-A-0036 : note ajoutée — « 2 mg/mL de BSA » absent du brevet primaire (vérification de l'agent C, EV-C-0076).
- EV-A-0034, Q-A-0009 : erreurs signalées par l'agent A corrigées.
- SRC-C-0021 : DOI imprimé par la revue mais déposé nulle part (ni Crossref, ni DataCite, ni Handle) ; métadonnées confirmées sur la page de la revue.
