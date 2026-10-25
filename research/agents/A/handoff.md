# Handoff — Agent A (substituts du muscle et nouvelles protéines, voie C)

Date : 2026-10-25. Rapport : `research/reports/alternative_proteins.md`. Base : 46 sources (SRC-A-0001 à SRC-A-0046), 51 affirmations (EV-A-0001 à EV-A-0051), 67 mesures (Q-A-0001 à Q-A-0067).

## 1. Résultats clés

- **Texture.** La HME reproduit la compression globale mais pas la fibrosité à l'échelle du faisceau. L'indice LMA des HMMA de soja est de 0,20, inférieur à celui des viandes ; une micro-impression perforante post-extrusion augmente jusqu'à 5× la séparation fibreuse (EV-A-0002, EV-A-0003 ; Q-A-0011, Q-A-0012). Les analogues de poulet sont moins élastiques que le poulet cuit et presque insensibles à la cuisson (EV-A-0001). Un mélange pois–gluten structuré en cellule de cisaillement atteint la résistance du poulet, 50–100 kPa (EV-A-0015 ; Q-A-0028).
- **Fer.** Aucun des 44 substituts suédois n'est une bonne source de fer biodisponible (phytate:fer de 2,5 à 45). La mycoprotéine est riche en zinc (6,7 mg/100 g) et quasi dépourvue de phytates (EV-A-0004, EV-A-0005). Le poulet cuit n'apporte que 1,04 mg de fer, 1,0 mg de zinc et 0,34 µg de B12 pour 100 g (Q-A-0003–Q-A-0005).
- **Qualité protéique.** L'écart avec la viande tient au profil en acides aminés, pas à la digestibilité : la TID des burgers végétaux et des isolats dépasse 0,90 (EV-A-0012). Les DIAAS d'ingrédients sont de 91 pour le soja, 70 pour le pois et 48 pour le blé, contre 117 pour le porc ; un mélange pois/riz plafonne à 84 (EV-A-0043, EV-A-0044).
- **Arôme.** L'arôme de poulet dépend des précurseurs soufrés (ribose/IMP + cystéine, thiamine) et des phospholipides, pas de l'hème. La léghémoglobine est dosée sur la viande rouge (≤0,8 %) ; l'EFSA a rendu en 2024 un avis favorable mais provisoire (EV-A-0017, EV-A-0018, EV-A-0019).
- **Mycoprotéine.** Production industrielle continue : 2 × 150 m³, environ 300 kg/h (EV-A-0040). Effets démontrés sur le muscle humain, dans des essais petits et liés à l'industriel (EV-A-0008, EV-A-0009). La Chine l'a autorisée en 2025 et une ligne de 20 000 t/an est annoncée (EV-A-0048). Échec économique de Meati (EV-A-0041).
- **Bactéries H2.** Solein contient 73,1 % de protéines en N × 6,25 contre 68 % avec le facteur spécifique (EV-A-0020). Un pilote de 300 L atteint 90 g/L de matière sèche (EV-A-0051). Le modèle de SCP photovoltaïque donne environ 15 t de protéines/ha/an, soit à peu près 10 fois le soja (EV-A-0013).
- **Aliment volaille.** La SCP de méthanotrophe est utilisable jusqu'à 12,5 % chez le Ross 308 (EV-A-0014) ; les larves de mouche soldat n'ont pas d'effet global (EV-A-0024). Le frein reste le prix du tourteau de soja, environ 1,1 USD/kg de protéine contre 4,6 USD pour le poulet (EV-A-0042).
- **Hybrides.** Le seul poulet cultivé vendu au détail contient 3 % de cellules dans une matrice végétale (EV-A-0039). Des protéines de pois/soja à 0,1 mg/mL remplacent 2 mg/mL de BSA pour des fibroblastes de poulet (donnée de brevet, court terme, EV-A-0036).
- **Marché.** Ventes US de viandes végétales : −7 % en valeur et −11 % en volume en 2024 (EV-A-0025). Taux d'appréciation de 30 % contre 68 % pour la viande, les nuggets et filets de poulet étant les catégories les plus proches de la parité (EV-A-0026).

## 2. Contradictions repérées

- **ACV de la mycoprotéine.** EV-A-0049 (Smetana 2015 : parmi les plus impactants) ↔ EV-A-0050 (Shahid 2024 : 0,73 kg CO2e/kg, base produit, co-auteur industriel). Les bases de calcul diffèrent.
- **Ultra-transformation.** EV-A-0022 (Rauber 2024 : UPF végétaux défavorables) ↔ EV-A-0023 (Thompson 2026 : bénéfice indépendant des UPF). Même cohorte UK Biobank.
- **Insectes en aliment volaille.** EV-A-0024 / Q-A-0041 (28 % « recommandé ») ↔ EV-A-0032 (dégradation à 10 %, Costa Rica). Le champ `contradicts` n'a pas été rempli pour cette paire.
- **Nuggets végétaux.** EV-A-0026 (quasi-parité, NECTAR) ↔ EV-A-0047 (nugget vegan le moins aimé, Pérou).
- **Protéines des burgers.** EV-A-0011 (DIAAS inférieur) ↔ EV-A-0012 (TID élevée) : compatibles, voir EV-A-0043.
- **Correction d'erreurs dans la base (champs `notes`).** Dans EV-A-0034, la note « cohérent avec EV-A-0029 » doit se lire EV-A-0031. Q-A-0009 porte `scale=commercial_farm` alors qu'il s'agit de produits de détail : il faudrait `not_applicable`. Ces lignes n'ont pas pu être modifiées via `kb.py`.

## 3. Lacunes (cherché sans succès)

- DIAAS mesuré du filet de poulet, de la mycoprotéine et des SCP.
- Énergie et productivité industrielles de la HME et de la cellule de cisaillement.
- Analyse technico-économique publique de la mycoprotéine (Upcraft 2021 : erreur 403).
- Olfactométrie d'analogues de poulet.
- Analogues laminés de yuba ou de kōya-dōfu (aucune étude moderne ; PDF J-STAGE en image).
- Rapports NECTAR et GFI primaires ; texte de la NHC (Chine) ; avis ACNFP/EFSA sur Solein.
- Essai original de Kaplan et al. sur Wolffia.
- Biodisponibilité du fer de Solein.
- Table CIQUAL (erreur 503).

## 4. Questions pour d'autres agents

- **→C** Données multi-passages sur les fractions protéiques végétales (pois/soja, fraction <10 kDa retirée) comme substitut d'albumine pour fibroblastes ou cellules satellites de poulet (brevet WO2021/148955A1 cité par SRC-A-0032) ? Composition exacte de la matrice végétale de GOOD Meat 3 dans le dossier SFA ?
- **→N** Coût et digestibilité des SCP bactériennes (méthanotrophes, hydrogénotrophes) et des larves de mouche soldat face au tourteau de soja dans les formules poulet de chair ; dosages effectivement utilisés en Europe. Comment expliquer l'écart entre 28 % et 10 % (EV-A-0024 vs EV-A-0032) ?
- **→E** Énergie et coût par kg des lignes HME ; analyse technico-économique de la mycoprotéine et des SCP hydrogénotrophes ; texte de l'annonce NHC 2025 n° 7 ; état de l'avis EFSA sur Solein après février 2025. ACV par kg de protéine digestible du poulet face à la mycoprotéine et aux extrudés (voir EV-E-0010).
- **→P** Brevets sur les films laminés et le yuba pour pièces entières (antériorité de la piste 1) ; brevets d'arômes de réaction « poulet » ; titulaire et revendications de WO2021/148955A1 ; causes techniques de l'échec de Meati.
- **→H** Sources primaires chinoises (Qingyilu, Suiyuan shidan) sur les techniques d'imitation de la volaille, si accessibles.

## 5. Pistes d'innovation (détail au §7 du rapport)

1. **Filet laminé par films protéiques (« yuba 2.0 ») avec perforation contrôlée.**
   - Fondement : EV-A-0029, EV-A-0030, EV-A-0003, EV-A-0002.
   - Hypothèse : un empilement de films de 0,5–1 mm perforés et liés à la transglutaminase atteint l'indice LMA du poulet avec moins d'énergie que la HME.
   - Validation : plan factoriel ; mesures LMA, traction, LAOS, panel de 60 personnes, kWh/kg.
2. **Système aromatique « poulet » sans hème.**
   - Fondement : EV-A-0017, EV-A-0019.
   - Hypothèse : des précurseurs (ribose/IMP, cystéine, thiamine) et une émulsion de phospholipides incorporés avant cuisson rapprochent le profil d'odorants de celui du poulet.
   - Validation : GC-O/AEDA face au poulet rôti, tests triangulaires.
3. **Matrice fermentée « dé-phytatée » et productrice de B12.**
   - Fondement : EV-A-0004, EV-A-0005, EV-A-0033, EV-A-0046.
   - Hypothèse : Rhizopus associé à une bactérie propionique abaisse le rapport phytate:fer sous 1 et produit au moins 0,34 µg de B12/100 g.
   - Validation : dosage InsP6, LC-MS/MS de la B12, absorption sur Caco-2, texture.
4. **Fractions végétales comme albumine des milieux pour cellules de poulet.**
   - Fondement : EV-A-0036, EV-A-0037.
   - Hypothèse : on atteint au moins 90 % de la productivité obtenue avec l'albumine sur 10 passages ou plus, pour un coût inférieur à 0,1 USD/L.

## 6. Recherches restantes prioritaires

1. DIAAS mesurés : poulet, mycoprotéine, Solein, C. necator (texte intégral de Hodgkinson 2025, laboratoire Stein).
2. Énergie et coût de la HME et de la cellule de cisaillement industrielles ; analyse technico-économique de la mycoprotéine.
3. Arôme des analogues de poulet (GC-O, brevets d'arômes de réaction).
4. Analogues laminés (yuba/腐竹) et congelés (高野豆腐) : CNKI/Wanfang, J-STAGE avec OCR.
5. SCP pour l'aliment volaille : essais avec bactéries hydrogénotrophes, autorisations UE, prix par kg de protéine.

## 7. Limites d'accès rencontrées

- **Outils internes.**
  - `search.py crossref` renvoie une erreur HTTP 400 : le paramètre `select` contient `language`, champ non accepté par Crossref. Contournement : requêtes directes `api.crossref.org/works?query.bibliographic=…&select=DOI,title,author,issued,container-title,type`.
  - `search.py jstage` échoue sur les requêtes à plusieurs mots.
  - `search.py hal` lève `KeyError: 'response'` sur certains titres longs.
  - **Bogue `kb.py`** : les titres en caractères non latins (zh, ko, ja) sont normalisés en chaîne vide, et toute nouvelle source CJK est déclarée doublon de SRC-C-0021. Contournement : ajouter une référence en caractères latins au titre (SRC-A-0028 à SRC-A-0030). À corriger par le coordinateur, par exemple en normalisant avec conservation des caractères Unicode.
- **Sites bloqués.**
  - USDA FDC API : DEMO_KEY limitée (429), d'où le téléchargement du CSV SR Legacy dans `research/downloads/A/usda_sr_legacy/`.
  - CIQUAL (503), pubs.rsc.org, doaj.org, revistas.udea.edu.co (403), acnfp.food.gov.uk (404/410), nhc.gov.cn (connexion réinitialisée).
  - PDF J-STAGE en image et pas d'OCR disponible.
- **Paywalls.** Elsevier et Springer : résumés seulement (Schreuders 2019, Krintiras 2016, Smetana 2015, Shahid 2024, Novak 2025, Fanelli 2022, Wiebe 2002).
- **Quota Consensus.** 2 requêtes utilisées sur le quota partagé.
