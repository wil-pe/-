# Handoff — Agent M (phase 4, mission N2 : économie de la nutrition avicole, littérature non anglophone, voie A)

Date : 2026-10-25. Rapport : `research/reports/deep/M_economie_nutrition.md`. Prolonge l'agent N.
Bilan : 30 sources nouvelles (SRC-M-0001 à 0030 ; 15 non anglophones, soit 50 % : zh 7, pt 3, nl 2, es 1, ja 1, fr 1) ; 49 affirmations (EV-M-0001 à 0049) ; 95 mesures (Q-M-0001 à 0095) — vérifié avec `kb.py stats` et `kb.py check` (0 problème). Sources réutilisées : SRC-A-0004, SRC-A-0021, SRC-A-0032, SRC-E-0001, SRC-K-0007, SRC-N-0012. Journal : ~70 requêtes en 7 langues (en, zh, pt, es, fr, nl, ja).

## 1. Résultats clés

1. **Coût d'un point de PB en moins (calcul agent M)** : prix d'équilibre du mélange d'AA libres = 2,05 USD/kg (prix mondiaux 2024), 8,80 RMB/kg (Chine, déc. 2025), 8,68 R$/kg (Brésil, 2020), soit 2,7 à 5,1 fois le prix du tourteau de soja selon le rapport maïs/soja (Q-M-0080 à 0082). Lys/Met/Thr sont sous ce seuil au Brésil ; en Chine la lysine 98 % (7,94 RMB/kg) est juste en dessous, la thréonine (9,41) au-dessus.
2. **Prix chinois des AA (marché, TVA incluse)** : lysine 98 % 10 885 → 7 939 RMB/t, thréonine 10 855 → 9 408 RMB/t de 2024 à 2025 (EV-M-0001 ; Q-M-0021 à 0024) ; série ASP thréonine Fufeng 2018-2025 entre 6 782 et 9 847 RMB/t ; maïs = 56,6 % du coût de production des AA (EV-M-0003).
3. **Qualité alimentation animale vs culture cellulaire** : L-Lys HCl EFSA 10-29 UI/g d'endotoxines contre < 10 UE/g pour une spécification de culture cellulaire (écart ×1 à 3, EV-M-0013), mais L-thréonine EFSA 288-319 UI/mg (×~30 000, EV-M-0014) : la variable décisive est l'endotoxine par AA et par fournisseur, pas la « qualité ».
4. **CT-12 (insectes)** : le « 28 % recommandé » d'Okon 2026 = inclusion moyenne de la méta-régression, pente d'IC non significative (EV-M-0017) ; neutralité jusqu'à ~15 % du régime (Martínez Marín 2023, EV-M-0020) ; effet négatif dès 10 % de *remplacement* (Moula 2019, EV-M-0022).
5. **Laisse 2018 contre-vérifié** (demande du coordinateur) : tableau 6, p. 12 du PDF HAL : ECp 0,54 ; ECpc 0,88 ; Ppc ration 40 % (EV-M-0038). CT-20 = définition : maïs 15 % et soja 60 % consommables chez Laisse ; grains et tourteau de soja comptés entièrement chez Mottet (selon Laisse) (EV-M-0039, 0040).
6. **Dilution protéique vs souche lente** : Ross 308 à 80 % de protéine équilibrée → IC 1,543 → 1,756, coût du filet +24 % ; à croissance égale, Ranger Classic nourri à 100 % produit le filet ~11 % moins cher (EV-M-0034).
7. **Souches lentes en conditions commerciales** : Norvège (64,6 M) mortalité après 7 j 3,05 % (Ross) vs 1,49 % (Hubbard JA787) (EV-M-0032) ; Danemark (8 fermes) NS (EV-M-0031) ; Pays-Bas KWIN : IC 1,58 vs 2,02 et N/poulet +38 %, N/m² −50 % (EV-M-0036).
8. **Chaîne aliment → protéine** : USDA 21,39 g/100 g (viande crue) et TACO 20,6-21,5 g ⇒ 60 g de protéines de viande par kg d'aliment à IC 1,531 (−6 % vs N) (EV-M-0047 ; Q-M-0092).
9. **NASEM 2026** : 10e édition des besoins des volailles publiée (remplace NRC 1994 ; poulets par poids vif) (EV-M-0027) ; texte BCC lu : aucune vitesse de croissance ni IC chiffrés (EV-M-0029).
10. **Économie des insectes** : ténébrion industriel 135 R$/kg (79 × le soja), marge −83 à −95 %, prix d'équilibre 4,53 R$/kg (EV-M-0045) vs larves de mouche domestique produites à la ferme sur lisier (Colombie) : performances NS, coût −40 % annoncé (EV-M-0049, faible).

## 2. Contradictions repérées

- **CT-12** : EV-M-0017/0018/0020/0022 ↔ EV-A-0024 (lecture « 28 % ») et EV-A-0032 — largement résolue (unités et lecture).
- **CT-20** : EV-M-0038/0039/0040 ↔ EV-N-0026 — précisée (définition de « consommable »).
- **CT-21** : EV-M-0034 (dilution de toute la protéine → filet −4,5 points) et EV-M-0044 (pénalité transitoire) ↔ EV-N-0014/0016/0018 — portée précisée.
- **Nouvelle** : mortalité des souches lentes en conditions commerciales EV-M-0032 ↔ EV-M-0031 et EV-N-0055.
- **Nouvelle** : AA de qualité alimentation animale « impropres » aux milieux EV-M-0015 (Humbird) ↔ EV-M-0013 (lysine) ; confirmé pour la thréonine EV-M-0014.
- **Nouvelle** : économie des insectes EV-M-0045 (industriel, Brésil) ↔ EV-M-0049 (ferme, Colombie).
- **Incohérences internes signalées** : Moula 2019 (IC poolé −0,18 à IC95 excluant 0 présenté comme nul) ; Okon 2026 (résumé « recommandé 28 % » non soutenu par le tableau 7) ; communiqué Rostagno (1re édition 1983 vs 2000).

## 3. Lacunes (cherché sans succès)

- Prix publiés de L-valine, L-isoleucine, glycine ; série de prix de la DL-méthionine (seul point : 11,70 R$/kg, Brésil 2020). Rapports Meihua/Adisseo non lus.
- Version 2025-2026 du Pink Sheet (fichier téléchargé daté de janvier 2025).
- CIQUAL (503), tables INRAE-CVB (feedtables 404), valeurs du tableau 14-3 NASEM 2026, Rostagno 2024 (livre payant), Havenstein 2003 (403) → KG-COV-08 ouvert.
- Essais chinois et brésiliens BSF × poulet de chair en accès libre (CNKI, 动物营养学报, SciELO, Alice Embrapa bloqués) ; norme CFIAS « basse protéine » pour poulet (n'existe que pour le canard, T/CFIAS 8006-2024 ; projet DB11 de Pékin non téléchargeable).
- Texte officiel français de l'ECC ; étude primaire van Horne 2020 ; IC des souches lentes en conditions commerciales (hors normes KWIN).

## 4. Questions pour d'autres agents

- **→B / C (milieux)** : pouvez-vous tester AA par AA des lots de qualité alimentation animale (endotoxines LAL/rFC + croissance de fibroblastes de poulet) ? La lysine EFSA (10-29 UI/g) est proche de la spécification culture cellulaire ; la thréonine (~300 000 UI/g) ne l'est pas (EV-M-0013, 0014). Quelles teneurs en endotoxines vos milieux tolèrent-ils ?
- **→K** : j'ai utilisé TACO (SRC-K-0007) pour les protéines de la viande crue (Q-M-0064, 0065) et l'USDA (SRC-A-0004, Q-M-0062, 0063, 0091-0093) ; vérifiez la cohérence avec vos facteurs de conversion (viande désossée → protéine, −6 % vs Laisse).
- **→E / K** : les coûts néerlandais (Greenwell, KWIN, SRC-M-0021/0022) et les prix Brésil/Chine (Q-M-0043-0050) peuvent alimenter les coûts par kg de protéine de la voie A.
- **→S / A** : le prix des insectes (135 R$/kg industriel ; 800 COP/kg à la ferme) et la neutralité ≤ 15 % peuvent servir aux comparaisons de protéines alternatives.
- **→R** : statut UE du substrat « lisier » pour les larves (interdit ?) et de la glycine comme additif ; spécifications réglementaires de pureté des AA (règlements d'exécution).
- **→X (coordinateur)** : kb.py n'a pas de commande de suppression ; un double appel `add quant` crée des doublons silencieux (voir §7).

## 5. Pistes d'innovation

- **INN-01 bis — cahier des charges « AA alimentaires à faible endotoxine »** : fondement EV-M-0013/0014/0015 ; hypothèse : ≥ 6 des 10 AA indispensables disponibles en lots alimentation animale < 30 UE/g permettent ≥ 90 % de la croissance témoin ; expérience : 10 AA × 3 fournisseurs, LAL + DF-1 sur 5 passages ; ≈ 3 mois-personne.
- **INN-06 bis — cible de PB indexée sur (P_soja − P_maïs)/P_AA** : fondement Q-M-0080 à 0082 ; hypothèse : −1 % de coût par kg de protéine de viande sans pénalité d'IC > 1 % ; validation par formulation au moindre coût sur 3 jeux de prix puis parquets.
- **INN-11 bis — choisir la souche plutôt que diluer la protéine** : fondement EV-M-0034, EV-M-0036 ; hypothèse : un aliment basse PB + AA dédié réduit l'écart d'IC Ranger/Ross de 9 % à ≤ 5 % ; 2 souches × 2 aliments, 12 parquets.
- **INN-18 (verminière moderne)** : la Colombie (EV-M-0049) suggère un intérêt économique des larves produites à la ferme, contre la farine industrielle (EV-M-0045) — à tester sur substrat autorisé.

## 6. Recherches restantes prioritaires

1. Prix Val/Ile/Gly/Met : rapports annuels Meihua (梅花生物), Adisseo (安迪苏), Evonik, CJ ; enquêtes CEPEA/IEA récentes.
2. NASEM 2026 tableau 14-3 et Rostagno 2024 (accès bibliothèque).
3. Autres avis EFSA FEEDAP (valine, isoleucine 2020, glycine, méthionine) pour les endotoxines ; spécifications culture cellulaire des mêmes AA.
4. van Horne 2020 et données danoises/norvégiennes d'IC en conditions commerciales des souches lentes.
5. Essais BSF × poulet de chair chinois (Wanfang) et équatoriens (ESPOL, accès réinitialisé).

## 7. Limites d'accès et incidents

- Bloqués : SciELO 403 ; Alice Embrapa (recherche) 403 ; CIQUAL 503 ; data.gouv.fr, beijing.gov.cn, chinajan.com, dspace.espol.edu.ec : connexion réinitialisée ; feedtables.com 404 ; tandfonline 403 (contourné par IRIS Turin) ; Elsevier/poultryscience.org (Havenstein) ; API USDA FDC DEMO_KEY 429 (contourné par les fichiers SR Legacy de l'agent A) ; HAL `/document` = page anti-robot (contourné par l'URL `/file/…pdf`, via l'API HAL `files_s`).
- Extraction PDF chinoise à deux colonnes partiellement illisible (SRC-M-0008 : tableaux non transcrits).
- **Incident kb.py** : un second `kb.py add quant` sur le même fichier a créé 62 doublons (Q-M-0083 à 0144) ; supprimés avec `read_rows`/`write_rows` de kb.py (pas de commande de suppression), `kb.py check` = 0 problème ; Q-M-0083 à 0090 réattribués à 8 mesures corrigées (valeurs « A vs B » rejetées puis scindées).
- Mises à jour d'autres agents via `kb.py set` : SRC-A-0021 → `full_text_read` (+ note sur le 28 %) ; SRC-N-0012 → note de contre-vérification du tableau 6.
