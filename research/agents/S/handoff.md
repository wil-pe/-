# Handoff — Agent S (phase 4, mission A2 : substituts — nutrition, énergie, coûts, arôme)

Date : 2026-10-25. Rapport : `research/reports/deep/S_substituts_nutrition_energie.md`. Base : 36 sources (SRC-S-0001 à SRC-S-0036 ; 14 non anglophones, soit 39 % : zh 4, de 3, ja 2, fr, es, nl, fi, ko), 47 affirmations (EV-S-0001 à EV-S-0047), 97 mesures (Q-S-0001 à Q-S-0097). Le contrôle `kb.py check` ne signale aucun problème.

## 1. Résultats clés

- **DIAAS du poulet.** Chez le miniporc, le repas filet de poulet + quinoa atteint un DIAAS adulte de 110, que la lysine soit comptée totale ou réactive. Le repas au soja texturé passe de 111 à 83 avec la lysine réactive : la chaleur de texturation dégrade la lysine (EV-S-0012, EV-S-0011). En in vitro, le filet de poulet dépasse 100 pour tous les acides aminés indispensables (EV-S-0010, EV-S-0013).
- **DIAAS des substituts (in vitro).**
  - Analogues végétaux de poulet du commerce : 52–65 (EV-S-0013).
  - Analogues de poulet à la mycoprotéine : 85–89 (enfant) et 106–111 (adulte), limités par l'histidine (EV-S-0002).
  - Biomasse de mycoprotéine : 83/97, limitée par les acides aminés soufrés (EV-S-0001).
  - Solein : ≈ 51, limitée par l'isoleucine (EV-S-0003).
- **Procédé Quorn vérifié.** Deux fermenteurs airlift de 155 m3 ; taux de dilution 0,17–0,20 h⁻¹ ; 10–15 g/L ; 30 t/h de culture par fermenteur ; 10 000–14 000 t/an. La réduction de l'ARN (68 °C) fait perdre jusqu'à 30 % de la matière sèche (EV-S-0033 à EV-S-0035). Cela confirme EV-A-0040.
- **Énergie.**
  - Mycoprotéine : 1,66 kWh + 13 MJ de vapeur par kg (données d'usine de 2010), l'énergie représentant 46 % de l'empreinte (EV-S-0037).
  - SCP à l'hydrogène : 37,8 kWh/kg de SCP sèche (modèle, EV-S-0005), ≈ 47 kWh/kg de Solein selon le projet de 50 000 t/an et 270 MW (EV-S-0031). Soit ≈ 50–75 kWh/kg de protéine, en accord avec Q-E-0042.
  - HME : SME mesurée de 0,04–0,21 kWh/kg (laboratoire/pilote, EV-S-0007, EV-S-0008) ; aucune énergie industrielle publiée.
- **Coûts et échecs.**
  - SCP à l'hydrogène : 4–16 USD/kg (modèle, EV-S-0006).
  - Solar Foods : CAPEX annoncé ≈ 18 000 €/(t/an) (EV-S-0032).
  - Shougang LanzaTech (23 200 t/an de protéine) en perte brute de 24,4 % (EV-S-0029).
  - Usine FeedKind de Chongqing à l'arrêt (EV-S-0044).
  - Mycoprotéine : selon Quorn, le sucre et l'énergie dominent le coût (EV-S-0045).
- **ACV, base produit et base protéine.**
  - Mycoprotéine : 2,4 (2010), 1,6 (2015), 2,44 (ESU 2016), 1,137 (2018) et 0,5 kg CO2e/kg (2023) (EV-S-0038, EV-S-0014, EV-S-0004).
  - RIVM 2024 (indépendant) : Quorn haché 3,08 contre filet de poulet 3,94 kg CO2e/kg (EV-S-0040).
  - FeedKind : 7,99 → 2,23 kg CO2e/kg de protéine selon l'énergie, contre 0,79 pour le concentré de soja (EV-S-0027, EV-S-0028).
- **Arôme.**
  - Bouillon de poulet : FD 128 pour le méthional, le (E,E)-2,4-décadiénal et la méthylpyrazine ; quatre odorants suffisent à le reconstituer (EV-S-0015, EV-S-0016) ; 2-méthyl-3-furanthiol confirmé (EV-S-0020).
  - Analogues chinois de poulet : odorants clés uniquement aldéhydiques, sans thiol carné (EV-S-0018).
  - Brevet DSM : sucre + cystéine + acide arachidonique extrudés donnent un « authentic boiled fatty chicken » (EV-S-0023).

## 2. Contradictions repérées

- **CT-11, précisée.**
  - Côté défavorable : EV-A-0049, EV-S-0036 (UBA, 4,1–4,6) et EV-S-0047 (modèle, 74).
  - Côté favorable : EV-A-0050, EV-S-0004, EV-S-0014.
  - Explication : année et énergie (chaleur fatale ; EV-S-0037, EV-S-0038), modèle contre usine, base produit contre base protéine (facteur ~2), périmètre (EV-S-0040).
  - Par kg de protéine : 18–22 (ESU 2016) contre 16–25 kg CO2e/kg pour le poulet (calcul de l'agent). Avantage non démontré de façon indépendante.
- **Nouvelle — digestibilité des analogues.** In vitro 81–93 % et DIAAS 52–65 (EV-S-0013) ↔ TID in vivo > 0,90 (EV-A-0012 ; EV-S-0011). Le champ `contradicts` est rempli dans EV-S-0013.
- **Nouvelle — qualité des protéines bactériennes.** Profil d'acides aminés complet (EV-A-0020) ↔ ivDIAAS de Solein ≈ 51 (EV-S-0003).
- **Nouvelle — mycoprotéine.** « PDCAAS 0,99 » (cité par Ariëns 2026 et le rapport Imperial 2025) ↔ ivDIAAS enfant de 83 (EV-S-0001). L'écart tient à la méthode.
- **Incohérence interne du rapport FeedKind.** Le texte donne 7,99 t CO2e/t de protéine, la Table B 2,23–2,65 sans scénario (EV-S-0027).
- **Écarts mineurs.** Marge de Shougang LanzaTech : −24,4 % (EV-S-0029) ou −24,5 % (EV-S-0030).

## 3. Lacunes (cherché sans succès)

- DIAAS in vivo de la mycoprotéine et des SCP ; DIAAS de C. glutamicum (Park 2024, 403) ; texte intégral de Hodgkinson 2025.
- Énergie totale (mécanique + thermique) par kg d'extrudat sur une ligne HME industrielle : aucune source en en, ko ou fr. Chiffre de la cellule de Couette non vérifiable (thèse Krintiras 2016 en 404).
- TEA publique de la mycoprotéine : Upcraft 2021 bloqué (RSC 403, ILRI 429, absent de Spiral). Rapport Carbon Trust 2023 de Quorn non public.
- ACV primaire de Solein : Järviö 2021, dépôt Luke en 503. Sillman 2020 : page anti-robot de Springer.
- Comparaison AEDA analogue de poulet vs poulet (seule une étude SPME/ROAV chinoise existe).
- Teneur en protéines du Quorn haché (NEVO soumis à conditions) pour fermer la comparaison RIVM par kg de protéine.
- Prix unitaire de la protéine de Shougang LanzaTech (prospectus HKEX non lu) ; annonce primaire d'Adisseo à la Bourse de Shanghai.

## 4. Questions pour d'autres agents

- **→P.** Liberté d'exploitation d'EP3054792B1 (DSM, priorité 2013, « actif » jusqu'en 2034 selon Google). Une HME qui contient sucre + cystéine + acide arachidonique dans la matrice protéique tombe-t-elle sous la revendication 1 (« heated and extruded ») ? Existe-t-il des familles équivalentes (CN, JP, US) et des brevets d'arôme de poulet sans acide arachidonique (phospholipides) ?
- **→K/E.** Utiliser les valeurs par kg de protéine du rapport (§4.2) en précisant la nature de chaque chiffre : Q-S-0019, Q-S-0023, Q-S-0082, Q-S-0085 et Q-S-0051 à Q-S-0055. Pour le poulet, le RIVM donne 3,94 kg CO2e/kg de filet (≈ 16,7 kg/kg de protéine, Q-S-0085). Lire le prospectus HKEX de Shougang LanzaTech (2553.HK) pour un coût réel de SCP.
- **→N/M.** Pour l'aliment volaille, FeedKind émet 3 à 10 fois plus que le concentré de soja par kg de protéine (EV-S-0028). La première usine industrielle est à l'arrêt (EV-S-0044). La protéine de Clostridium de Shougang LanzaTech (destinée à l'alimentation animale ; un certificat chinois de 2021 est cité par la presse mais n'a pas été vérifié) a-t-elle été testée chez le poulet de chair ?
- **→R.** Statut UE de Solein après 2025 ; statut chinois de FeedKind (le MARA l'a approuvé pour l'aquaculture en 2024 selon SRC-S-0033) ; extension éventuelle à la volaille.
- **→C/B.** La réduction de l'ARN (68 °C, jusqu'à 30 % de perte de matière sèche, EV-S-0035) concerne-t-elle la biomasse cellulaire cultivée (ARN des cellules en prolifération) ? Utile pour les comparaisons de rendement.

## 5. Pistes d'innovation (détails au §9 du rapport)

1. **S-1 (révision d'INN-10).** Arôme de poulet généré dans l'extrudeuse : cystéine + pentose + huile riche en acide arachidonique dans le pré-mélange HME.
   - Fondement : EV-S-0023, EV-S-0022, EV-S-0017, EV-S-0018.
   - Validation : SAFE-AEDA contre bouillon et filet rôti, dosage de la lysine réactive.
   - Risque principal : liberté d'exploitation face au brevet DSM.
2. **S-2.** Analogue de poulet à DIAAS enfant ≥ 100, par correction de l'histidine et des acides aminés soufrés et par texturation à ≤ 140 °C ou en cellule de cisaillement.
   - Fondement : EV-S-0002, EV-S-0001, EV-S-0012, EV-S-0042.
   - Validation : INFOGEST, puis miniporc avec lysine réactive.
3. **S-3.** Fermentation protéique adossée à une source de chaleur fatale à ≥ 70 °C, avec ACV revue selon ISO 14040 par kg de protéine digestible.
   - Fondement : EV-S-0037, EV-S-0038, EV-S-0041.
   - Cible : ≤ 10 kg CO2e/kg de protéine.

INN-09 est renforcée sur le plan énergétique : cellule de Couette ≤ 33 kJ/kg (déclaration, EV-S-0009) contre une SME de HME de 150–760 kJ/kg (EV-S-0007, EV-S-0008). INN-15 est inchangée.

## 6. Recherches restantes prioritaires

1. Prospectus HKEX de Shougang LanzaTech : prix et volume de la protéine, coût de revient.
2. Inventaire de la mycoprotéine : rapport Carbon Trust 2023, Upcraft 2021 par un autre miroir, Finnigan 2010.
3. DIAAS in vivo de la mycoprotéine et d'une SCP ; Hodgkinson 2025 en texte intégral.
4. AEDA tête-à-tête analogue de poulet vs filet rôti, avec MFT dosé par dilution isotopique.
5. Énergie totale d'une ligne HME industrielle ; thèse Krintiras 2016 ; protéine du Quorn haché (NEVO).

## 7. Limites d'accès rencontrées

- **Payant ou bloqué.**
  - RSC (403) : Upcraft 2021.
  - ScienceDirect (403) et API Elsevier sans clé (429/400) : Shahid 2024.
  - Springer (page anti-robot) : Sillman 2020.
  - tandfonline et DOAJ (403) : Park 2024.
  - Luke (503) : Järviö 2021.
  - research.tudelft.nl (404) : Krintiras 2016.
  - businesswire : connexion refusée.
- **Sous conditions.** Formulaire du Carbon Trust (contourné par le lien public direct du PDF FeedKind) ; téléchargement NEVO-online (non fait).
- **Images non lisibles.** Tableaux de résultats de la thèse Guyony et tableaux sensoriels de JP2010220520A.
- **Lu au niveau du résumé seulement.** Alotaibi 2026, Caliskan 2026, Fan 2018, Ishida 1978, Jeong 2023, Campusano 2023.
- **access_level d'autres agents.** Aucune source déjà enregistrée en `abstract_only` n'a pu être lue en texte intégral ; aucun `access_level` d'un autre agent n'a été modifié.
- **Outils.** `kb.py` accepte désormais les titres en caractères CJK (le bogue signalé par l'agent A ne s'est pas reproduit). Les chiffres « 108 pour le poulet » et « EAAI 118,6 pour C. necator » de la revue npj 2026 (PMC13402606) sont secondaires et n'ont pas été enregistrés.
