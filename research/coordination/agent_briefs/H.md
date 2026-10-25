# Brief — Agent H : Histoire et alimentation des poules

**Lettre** : H · **Rapport** : `research/reports/history.md` · **Questions** : RQ-H1 à RQ-H5.

## Mission
Retracer les méthodes d'alimentation des poulets depuis la domestication jusqu'à aujourd'hui (Asie, Afrique, Europe, Amériques, Moyen-Orient), en distinguant strictement **preuves historiques documentées** (`historical_documented`), **reconstitutions** (`historical_reconstruction`) et **hypothèses** (`theoretical`). Identifier les innovations oubliées ou abandonnées qui pourraient avoir un intérêt moderne (aliments locaux, insectes, larves, fermentation, germination, coproduits, finition).

## Livrable spécifique en plus des livrables communs
- Une **chronologie** (tableau : date/période, lieu, pratique ou innovation, source `SRC-…`, type de preuve) dans le rapport.
- Un tableau « **innovations historiques à réévaluer** » : pratique, période, pourquoi abandonnée (si documenté), intérêt moderne potentiel, ce qu'il faudrait tester.

## Pistes et références à retrouver (à vérifier, ne pas citer de mémoire)
- Domestication et régime : travaux récents associant la domestication du coq à l'agriculture du riz et du millet en Asie du Sud-Est (ex. Peters et al. 2022 PNAS ; Best et al. 2022 Antiquity, site de Ban Non Wat) ; isotopes stables du collagène osseux de poulets archéologiques (Chine, Europe romaine, Afrique) révélant leur alimentation.
- Antiquité : Varron *Res rusticae* III.9, Columelle *De re rustica* VIII (engraissement à la farine d'orge, obscurité, confinement), Palladius, Pline l'Ancien (*Histoire naturelle* X, loi somptuaire Fannia sur les poules engraissées) ; Égypte : fours à éclosion. Utiliser des traductions disponibles en ligne (archive.org, LacusCurtius/penelope.uchicago.edu pour Columelle/Varron) — vérifier la référence exacte du passage.
- Chine : 齐民要术 (Jia Sixie, VIᵉ s.) chapitre 养鸡 ; pratiques de pisciculture-aviculture intégrées.
- Monde arabe/andalou : Ibn al-ʿAwwām, *Kitāb al-Filāḥa* (XIIᵉ s.), chapitre sur les volailles (traduction française de Clément-Mullet, XIXᵉ s., possiblement sur archive.org).
- Europe XVIIIᵉ–XIXᵉ : Réaumur (1749) *Art de faire éclore et d'élever en toute saison des oiseaux domestiques* ; traités avicoles français et anglais (Moubray, etc.) ; **verminières** / production d'asticots pour volailles ; engraissement en épinettes, gavage/« pâtons », finition au lait (Bresse, La Flèche, Le Mans).
- Afrique/Asie/Amériques : systèmes en divagation (« scavenging feed resource base », travaux FAO), utilisation des termites (Afrique de l'Ouest), larves, azolla et lentilles d'eau (Vietnam, Chine), manioc, sous-produits de rizerie ; Amériques précolombiennes ? (vérifier l'existence de poules précolombiennes : controverse El Arenal, Chili — preuves pour/contre).
- Industrialisation (XXᵉ s.) : Eijkman et la polynévrite des poules nourries au riz poli (1890s) ; découverte de la vitamine D et confinement en bâtiment (années 1920) ; « animal protein factor » / vitamine B12 ; antibiotiques facteurs de croissance (Stokstad & Jukes, ~1950) ; concours « Chicken of Tomorrow » (1948, États-Unis) ; formulation au moindre coût par programmation linéaire (Waugh 1951) ; DL-méthionine de synthèse (années 1950) et lysine par fermentation (Japon, fin des années 1950) ; tourteau de soja chauffé ; phytase commerciale (1991) ; interdiction des AGP dans l'UE (2006) ; interdiction des eaux grasses/swill (UE ~2001–2002) ; interdiction des farines animales (1994–2001) puis réautorisation partielle (insectes, 2021).
- Études comparatives de souches d'époques différentes (Havenstein et al. ; Zuidhof et al. 2014) — **l'agent N les analyse en détail** ; toi, tu les situes dans la chronologie.

## Langues
en, fr (traités avicoles, Réaumur, INRAE/ITAVI historiques), la (sources classiques via traductions), zh (齐民要术, 养鸡史, 家禽饲养史), ar (Ibn al-ʿAwwām, filāḥa), es (gallinas criollas, historia avícola), pt (galinha caipira), ja (養鶏史), hi (देसी मुर्गी पालन, si pertinent), langues africaines via sources FAO/francophones/anglophones.

## Conseils
- archive.org contient ~2 600 ouvrages avicoles avant 1925 en texte OCR : utilise `search.py archive` puis `archive-text <id> '<regex>'` pour extraire des passages précis (indique la position/chapitre dans `locator`).
- Pour une pratique historique, la source primaire est le texte d'époque ; une histoire secondaire moderne est utile mais distincte.
- Cherche les preuves **quantitatives** historiques (rations, quantités de grain par poule, durées d'engraissement, poids obtenus) et enregistre-les avec `scale=historical`, `data_nature=historical_record`.
