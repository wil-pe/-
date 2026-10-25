# Handoff — Agent K (phase 4, mission X2 : comparaison homogène des trois voies) — 2026-10-25

Rapport : `research/reports/deep/K_comparaison_voies.md` · Modèle : `research/agents/K/models/comparison.py` (+ `results.md`, `results.json`) · Journal : `search_log.md` (56 requêtes, 7 langues) · Terminologie : `terminology.md` (42 entrées).
Bilan : 22 sources (SRC-K-0001 à 0022, dont 21 externes, 7 non anglophones = 33 %) ; 56 affirmations (EV-K-0001 à 0056) ; 189 mesures (Q-K-0001 à 0189, dont 57 sorties du modèle K et 8 hypothèses K).

## 1. Résultats clés
- **Coût par kg de protéine comestible, voie A** (100 % des coûts imputés à la viande désossée) : standard 7,6-19 USD (UE 2017 : 8,9-12,8 €, cohérent avec Q-E-0070 ; UE 2021 : 10,0-14,6 € ; France 2022 : 14,1-18,1 €) ; ECC 16-22 €2021 ; Label Rouge 39-44 €2022 ; bio 51-58 €2022 (Q-K-0129 à Q-K-0138, EV-K-0039 à EV-K-0041).
- **Le bien-être est surcoûté deux fois** : +22 % par kg vif pour l'ECC, ≈ +50 % par kg de protéine, à cause du rendement désossé (43 → 32-35 % du PV) (EV-K-0040, EV-K-0026, EV-K-0027).
- **Voie B** : 9-287 USD/kg de protéine à 21 %, 22-670 à 9 % (EV-K-0042) ; parité avec le standard seulement si la biomasse humide coûte ≤ 0,87-1,71 USD/kg (EV-K-0043) ; la zone de parité réaliste est le Label Rouge/bio (41-68 USD).
- **GES par kg de protéine** : A standard 11-44 (LUC ×2,7), Label Rouge 30-39, bio 38-73 ; B 10-79 (base publiée), 28-159 (9 %), 984-16 756 (intrants purifiés) ; analogues de soja 7,7-11,4 ; ingrédients 0,8-21 (EV-K-0044, EV-K-0046).
- **Énergie** : B 4-30 fois A ; les analogues de soja consomment autant d'énergie fossile par kg de protéine que le filet de poulet (284-344 vs 306 MJ) (EV-K-0045, EV-K-0046).
- **Définition de la protéine** (acides aminés vs N × facteur) : facteur 1,21, premier facteur de sensibilité du coût de A (EV-K-0020, EV-K-0049).
- **DIAAS** : ajustés à la qualité, les analogues de soja (11,8-21,9 kg CO2-eq/kg) rejoignent le poulet (19-24) ; la protéine bactérienne H2 double son coût et ses GES (EV-K-0056).
- **Q-E-0066 (3,55 USD/kg de mycoprotéine)** : source primaire = Risner et al. 2023 ; base = kg de mycoprotéine humide (~73 % d'eau), soit 29,56 USD/kg de protéine (EV-K-0031, EV-K-0032).

## 2. Contradictions repérées
- **CT-10 résolue** (base) : animal entier 181 g vs comestible 92 g de protéine/kg PV (EV-K-0051 vs EV-A-0042).
- **CT-01 étendue aux ACV** : Humbird 21 %, CE Delft 18-25 %, Mazac 19 % (EV-K-0011, EV-K-0054) vs caille 9 % (EV-C-0020) → ×2-2,8 sur tous les indicateurs B par kg de protéine (EV-K-0052).
- **CT-15** : facteur du soja brésilien 1,6 (ecoinvent 3.9) / 2,6 (3.8) / 4,5 (GFLI) (EV-K-0053) ; inversion des systèmes avec ou sans LUC (EV-K-0029).
- **Nouvelle — eau bleue de A** : 1 654-5 780 L/kg de protéine (Mekonnen & Hoekstra, EV-K-0006) vs 200 L (CE Delft, EV-K-0009) ; ordre A/B indécidable (EV-K-0047).
- **Interne AGRIBALYSE** : bio « moyenne » 2,98 < systèmes bio 1-2 (4,23-4,47 kg CO2-eq/kg vif) (Q-K-0035, Q-K-0039).

## 3. Lacunes (cherché sans succès)
- Étude AVEC/Wageningen 2026 ; coûts ITAVI 2023-2024 ; série ICPFrango (page dynamique) ; coûts chinois (全国农产品成本收益资料汇编 non en ligne) ; coûts espagnols récents (aviNews 403).
- Rendement en viande désossée totale des souches Label Rouge/bio (seul le filet est mesuré ; cuisse empruntée au BLS, Q-K-0122).
- CIQUAL (en maintenance) ; ACV primaires chinoises et hispanophones ; Leinonen 2012, Prudêncio da Silva 2014, Upcraft 2021 (PDF bloqués).
- Énergie et surface physiques (m2) du Label Rouge et du bio ; coûts de produits finis de la voie C ; valeurs GLEAM 3 par kg de protéine (graphiques seulement, EV-K-0055).

## 4. Questions pour d'autres agents
- **→C/B** : composition (protéines, eau, lipides, acides aminés) de la biomasse de poulet dans les mémos FDA (CCC 000002, 000039) — elle fixe ×2-2,8 sur toute la voie B.
- **→N/M** : rendement en viande désossée (filet + cuisse sans os) des souches S757N, JA757 et des poulets bio ; teneur en protéines crue par système ; CIQUAL dès réouverture.
- **→A/S** : composition (protéines) des analogues AGRIBALYSE (escalope végétale soja, nuggets de soja) pour remplacer l'hypothèse Q-K-0125 ; coûts de produits finis (TEA d'extrusion).
- **→E** : la base du coût Pasitka 2024 (6,2 $/lb) reste non vérifiée (CT-02) ; elle entre dans la plage B.
- **→X (coordinateur)** : (1) passer **SRC-E-0030** (Poore & Nemecek) de `metadata_only` à `partial_text_read` (manuscrit accepté lu sur ORA, Fig. 1 ; URL https://ora.ox.ac.uk/objects/uuid:b0b53649-5e93-4415-bf07-6b0b1227172f) — ma tentative de `kb.py set` sur une ligne de l'agent E a été refusée par le contrôle d'accès, je ne l'ai pas contournée ; (2) ajouter la contradiction « eau bleue A » ; (3) le modèle lit des lignes Q-S-… non encore fusionnées (DIAAS, FeedKind, Quorn, RIVM) : relancer `comparison.py` après fusion.

## 5. Pistes d'innovation
- **K-1** Viande cultivée « premium » : parité avec le Label Rouge/bio (41-68 USD/kg de protéine) à ≤ 4-6 USD/kg de biomasse ; TEA sur composition mesurée.
- **K-2** Mesurer la composition de biomasse de poulet (Kjeldahl/Dumas + humidité + acides aminés, 3 lots × 2 milieux) : coût faible, effet ×2-2,8.
- **K-3** Protéine de qualité équivalente : formulations d'analogues à DIAAS > 80 % pour rétablir un avantage GES ×2.
- **K-4** Soja à faible LUC, levier commun A et B : comparer « cut-off 2008 » vs passage au Label Rouge dans AGRIBALYSE.

## 6. Recherches restantes prioritaires
1. Composition de la biomasse de poulet cultivée (FDA, agent B). 2. Viande désossée des souches Label Rouge/bio (ITAVI, SYSAAF, INRAE). 3. CIQUAL et composition des analogues. 4. Leinonen 2012 / Prudêncio da Silva 2014 par bibliothèque. 5. Tableau de bord GLEAM 3 (valeurs par kg de protéine). 6. TEA d'extrusion humide et prix de détail du poulet.

## 7. Limites d'accès rencontrées
- HAL (« Access denied » sur fichiers), productions-animales.org (503 / connexion coupée), pubs.rsc.org (403), ScienceDirect/OUP (403 malgré licence ouverte), avinews.com (403), umweltbundesamt.de (page HTML au lieu du PDF), dataverse Recherche Data Gouv (méthodologie de 6 Mo : connexion coupée), jukuri.luke.fi (connexion coupée), CIQUAL (maintenance), Embrapa ICPFrango (contenu dynamique).
- Contournements : copies institutionnelles (GFI Europe pour CE Delft, Helda pour Järviö/Mazac, CFN pour TACO, ifeu.de pour ifeu, ORA pour Poore & Nemecek), API ouvertes (ADEME, USDA, BCE).
