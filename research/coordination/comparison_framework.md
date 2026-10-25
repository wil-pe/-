# Cadre de comparaison des trois voies

Objectif : comparer A (élevage), B (viande cultivée), C (substituts) **sans mélanger des grandeurs de nature différente**. Toute comparaison inter-voies passe par une chaîne de conversion explicite dont chaque maillon est une ligne `quant` sourcée (ou une hypothèse marquée `model_assumption`).

## 1. Chaînes de conversion

### Voie A — élevage
```
aliment (kg, tel quel) ──IC──▶ poids vif (kg)
poids vif ──rendement carcasse──▶ carcasse (kg)
carcasse ──rendement en viande désossée / filet──▶ viande comestible (kg)
viande comestible ──teneur en protéines──▶ protéine comestible (kg)
aliment ──teneur en protéines──▶ protéine alimentaire (kg)  ⇒ efficacité protéique = protéine comestible / protéine alimentaire
aliment ──fraction consommable par l'humain──▶ « human-edible » feed  ⇒ contribution nette en protéines
```
Facteurs à sourcer (agent N, sauf mention) : IC par souche/âge/poids ; rendement carcasse ; rendement filet et viande désossée totale ; teneur en protéines de la viande (crue, cuite — tables officielles, agent A pour la référence nutritionnelle) ; teneur en protéines de l'aliment ; fraction « human-edible » (Mottet 2017, Laisse 2018) ; mortalité ; coproduits valorisés.

### Voie B — viande cultivée
```
milieu (L) ──densité cellulaire (cellules/mL)──▶ nombre de cellules
cellules ──masse par cellule ou volume cellulaire tassé──▶ biomasse humide (kg)
biomasse humide ──teneur en matière sèche──▶ matière sèche (kg)
matière sèche ──teneur en protéines──▶ protéine (kg)
biomasse ──taux d'incorporation dans le produit──▶ produit fini (kg) (souvent hybride : cellules + végétal)
milieu (L) ──consommation par kg de biomasse (L/kg)──▶ besoins en glucose, acides aminés, facteurs de croissance
```
Facteurs à sourcer (agent C ; économie agent E) : densités par système et échelle ; masse/volume cellulaire des cellules de poulet utilisées ; matière sèche et protéines de la biomasse ; consommation spécifique de milieu ; rendement de récolte ; % de cellules dans le produit (documents réglementaires).

### Voie C — substituts
```
matière première (kg) ──extraction / concentration──▶ isolat ou concentré protéique (kg)
isolat ──formulation (eau, lipides, liants)──▶ produit (kg)
substrat de fermentation (kg sucre, kg CH4, kWh d'H2) ──rendement──▶ biomasse sèche ──▶ protéine
produit ──digestibilité (DIAAS)──▶ protéine de qualité équivalente
```
Facteurs à sourcer (agent A ; économie agent E) : rendements d'extraction ; teneur en protéines des produits ; rendement biomasse/substrat ; énergie par kg de protéine ; DIAAS.

## 2. Bases de référence pour les comparaisons
1. **kg de produit comestible** tel que vendu (attention : composition différente selon la voie).
2. **kg de protéine comestible** (base principale de comparaison des ressources).
3. **kg de protéine digestible de qualité équivalente** (ajustement DIAAS), lorsque les données existent.

## 3. Indicateurs par voie (section 9 de la mission) — à ne pas croiser entre voies sans conversion
| Voie A | Voie B | Voie C |
|---|---|---|
| aliment consommé, durée de croissance, rendement musculaire, viande comestible, coût, eau, énergie, terres, impacts, santé/bien-être | biomasse cellulaire ou tissu, productivité volumique, durée de cycle, rendement de récupération, coût du milieu, coût total, énergie, eau, qualité du tissu, sécurité, capacité industrielle | protéines, acides aminés, texture, saveur, valeur nutritionnelle, coût, capacité, énergie, eau, impact |

## 4. Étiquetage obligatoire de chaque chiffre de comparaison
`measured` · `company_claim` · `published_estimate` · `model_assumption` · `model_output` · `statistical` — et échelle (`lab` → `industrial`). Une comparaison qui mélange une mesure industrielle (voie A) et une sortie de modèle (voie B) doit l'afficher explicitement.

## 5. Questions de comparaison ouvertes (à traiter en phase 7)
- Quel intrant est limitant commun aux trois voies (protéine végétale / acides aminés / énergie / capital) ?
- À quel prix de l'énergie et du capital la voie B devient-elle compétitive, sous des hypothèses démontrées ?
- Quelle combinaison hybride (A+B, A+C, B+C) réduit le plus le coût par kg de protéine comestible sous des hypothèses démontrées ?
