# Inconnues scientifiques et lacunes de couverture

Deux types d'entrées à ne pas confondre :
- **Inconnues scientifiques** : la donnée n'existe pas publiquement (cherchée sans succès par un ou plusieurs agents, journalisée).
- **Lacunes de couverture** : la réponse existe probablement, mais nous ne l'avons pas trouvée ou lue (accès, langue, temps).

Consolidé le 2026-10-25 à partir des handoffs H, N, C, A, E, P, puis de la phase 4 (B, M, S, R, K). Priorité : P1 = conditionne une conclusion principale. Les lacunes réduites en phase 4 sont marquées **[réduit]** ou **[résolu]**.

## État après la phase 4 (résumé)
- **Réduites nettement** : KG-A04 (dose-réponse insectes, agent M), KG-COV-07 (EUR-Lex contourné via CELLAR, agent R), KG-COV-12 (réglementation Corée/Chine/Suisse/États US, agent R), KG-C01 (DIAAS, agent S), KG-X01 (comparaison par kg de protéine, agent K).
- **Réduites partiellement** : KG-C02 (énergie extrusion : labo/pilote seulement), KG-C06 (TEA mycoprotéine : via Risner 2023), KG-A03 (plancher PB : prix max du mélange d'AA calculé), KG-X02 (coûts poulet 2021–2025 UE/FR/US/BR).
- **Toujours ouvertes (bloquées par l'accès ou la politique d'usage)** : KG-B01, KG-B02, KG-B03, KG-B04, KG-B05, KG-B06 (données de procédé et de composition de la biomasse de poulet — agent B interrompu par la politique d'usage, non relancé), KG-COV-05 (Pasitka texte intégral), KG-COV-08 (Havenstein texte intégral).

## 1. Inconnues scientifiques

### Voie B — viande cultivée
| ID | Prio | Inconnue | Pourquoi c'est important | Preuves partielles | Expérience / donnée qui réduirait l'incertitude |
|---|---|---|---|---|---|
| KG-B01 | P1 | Composition réelle (protéines, eau, lipides) de la biomasse de **poulet** cultivée | Fixe le coût par kg de protéine (facteur ×2,3 entre l'hypothèse de 21 % et la mesure de 9 %) | Caille : 9 g/100 g (EV-C-0020) ; hypothèse de Humbird ~21 % (EV-C-0074) | Kjeldahl/Dumas + humidité + lipides sur DF-1 et sur des fibroblastes immortalisés, en suspension sans sérum, avec et sans phase de maturation (piste I-1 de l'agent C) |
| KG-B02 | P1 | Milieu de **différenciation** sans sérum pour myoblastes/cellules satellites de poulet | Sans lui, pas de « muscle » cultivé de poulet, seulement de la biomasse de fibroblastes | Meilleur indice de fusion publié : 30 %, avec transgène MyoD (EV-C-0027) ; aucun milieu sans sérum publié | Plan factoriel (insuline/IGF, transferrine, sélénium, lipides, inhibiteurs de TGF-β, hydrolysats) avec indice de fusion et MyHC comme critères |
| KG-B03 | P1 | Lignée immortalisée de **cellules satellites** de poulet (TERT/CDK4 ou autre) gardant sa myogenèse | Prérequis d'une production de muscle à l'échelle | SV40-LT échoue (EV-C-0044) ; aucune lignée TERT/CDK4 de poulet publiée | Transduction TERT+CDK4 ; ≥ 100 doublements avec conservation de la fusion |
| KG-B04 | P1 | Densité, consommation d'O₂, production d'ammoniac/lactate, **litres de milieu par kg** et taux de contamination à l'échelle industrielle | Paramètres qui pilotent le coût du milieu et du capital (principales sensibilités, EV-E-0059) | Labo : 130 × 10⁶ cellules/mL (Q-C-0003) ; aucune donnée > 10³ L (EV-E-0055) | Campagnes de 50–200 L instrumentées et publiées (OUR, NH₃, lactate, L/kg) |
| KG-B05 | P2 | Faisabilité du **recyclage du milieu** pour les cellules de poulet | Pourrait diviser le coût du milieu | Indices partiels (EV-C-0012, EV-C-0060, EV-C-0062) | Deux bioréacteurs en parallèle, ≥ 50 % de milieu recyclé pendant 20 jours (piste I-3) |
| KG-B06 | P1 | **Pureté des intrants** réellement exigée (qualité alimentaire vs pharmaceutique, endotoxine) | Fait varier l'ACV d'un facteur ~100 (CT-09) et le coût | Aucune spécification publique | Croissance et sécurité comparées avec intrants de qualité alimentaire vs pharmaceutique |
| KG-B07 | P2 | Reproductibilité de l'immortalisation spontanée des fibroblastes de poulet hors du laboratoire d'origine ; stabilité génomique | Base de la seule voie peu coûteuse démontrée (CT-07) | Un seul laboratoire (EV-C-0015) | Réplication indépendante, caryotype, séquençage |
| KG-B08 | P2 | Texture et sensorialité du poulet cultivé, **mesures quantitatives** | Qualité du produit | Aucune donnée quantitative | TPA, cisaillement, panel, comparés au filet |
| KG-B09 | P2 | Part de cellules nécessaire pour un **effet perceptible** dans un produit hybride | Produits actuels à 3–4 % de cellules (EV-C-0075, Q-C-0069) | Aucune étude dose-réponse | Panel sensoriel sur une gamme de 0 à 50 % de cellules |

### Voie A — élevage
| ID | Prio | Inconnue | Pourquoi | Preuves partielles | Expérience / donnée |
|---|---|---|---|---|---|
| KG-A01 | P1 | Potentiel génétique restant d'amélioration de l'efficience | Borne supérieure de la voie A | Modèle : ~8 % d'énergie récupérable (EV-N-0052) ; plafond de conversion protéique vers 0,32 (Q-N-0081) | Modèles indépendants ; données de sélection récentes |
| KG-A02 | P1 | Mécanismes des myopathies (white striping, woody breast) et moyen de les découpler de la croissance | 96 % de white striping en Ontario (EV-N-0042) ; limite physiologique | Associations avec la vitesse de croissance | Études longitudinales du métabolisme et de la vascularisation du muscle |
| KG-A03 | P2 | Plancher protéique et rôle exact de glycine+sérine, du potassium et du gras abdominal | Réduction du soja et de l'azote | EV-N-0011, EV-N-0019, EV-N-0020 ; résultats variables sur le filet (CT-21) | Essais dose-réponse avec AA libres et Gly+Ser contrôlés |
| KG-A04 | P2 | Dose-réponse des insectes (par espèce, fraction, âge) | Contradiction CT-12 | — | Méta-analyse dose-réponse |
| KG-A05 | P3 | Prédicteurs de l'efficacité des additifs (protéase, probiotiques) | Effets conditionnels (EV-N-0032), probiotiques non reproduits (CT-22) | — | Essais multicentriques préenregistrés |

### Voie C — substituts
| ID | Prio | Inconnue | Pourquoi | Preuves partielles | Expérience / donnée |
|---|---|---|---|---|---|
| KG-C01 | P1 | DIAAS mesuré du filet de poulet, de la mycoprotéine et des protéines bactériennes | Comparaison nutritionnelle juste | Soja 91, pois 70, porc 117 (EV-A-0043) | Essais DIAAS (porc ou humain) |
| KG-C02 | P1 | Énergie et productivité industrielles de l'extrusion humide et de la cellule de cisaillement | Comparaisons de ressources et de coûts | Aucune donnée publique | Mesures sur lignes industrielles |
| KG-C03 | P1 | Écart de fibrosité avec le filet et moyen de le combler | Indice LMA 0,20 pour le soja extrudé (EV-A-0002) | Micro-impression post-extrusion ×5 (EV-A-0003) | Comparaison d'anisotropie avec le filet cuit selon un protocole commun |
| KG-C04 | P2 | Arôme poulet des analogues (olfactométrie) | Facteur d'acceptabilité | Précurseurs soufrés et phospholipides (EV-A-0017, EV-A-0019) | GC-O/AEDA comparant analogue et poulet |
| KG-C05 | P2 | Biodisponibilité du fer et du zinc des substituts | Écart nutritionnel (EV-A-0004, EV-A-0005) | Rapport phytate:fer de 2,5 à 45 | Études Caco-2 / isotopes stables |
| KG-C06 | P2 | TEA publique de la mycoprotéine et des SCP | Comparaison économique | 3,55 USD/kg cité sans source primaire (Q-E-0066) | TEA indépendante |

### Transversal
| ID | Prio | Inconnue | Pourquoi | Preuves partielles |
|---|---|---|---|---|
| KG-X01 | P1 | Coût par kg de **protéine comestible** sur une base homogène pour les trois voies | Comparaison principale (RQ-X1) | Voie A : 8,3–14,1 €2017 (UE standard, Q-E-0070) ; voie B : 85–670 USD (Q-X-0001 à Q-X-0003, modèle) ; voie C : ingrédients seulement (soja 1,8–8,1 €/kg de protéine, prix) |
| KG-X02 | P2 | Coûts internationaux du poulet après 2017 | Actualiser la référence | **[réduit]** UE 6 pays 2021, France 2022, États-Unis 2023, Brésil 2025 (agent K) ; étude AVEC/Wageningen 2026 introuvable |
| KG-X03 | P2 | Empreinte eau du poulet sur une base cohérente | Comparaison eau entre voies | **Nouveau (CT-28)** : 1 654 L/kg de protéine (Mekonnen & Hoekstra) vs 200 L (CE Delft) — méthodes d'empreinte eau incompatibles |

### Histoire
| ID | Prio | Inconnue | Preuves partielles |
|---|---|---|---|
| KG-H01 | P3 | Régime isotopique des premiers poulets d'Asie du Sud-Est | Ban Non Wat daté (EV-H-0001) ; isotopes ailleurs (EV-H-0005 à EV-H-0007) |
| KG-H02 | P3 | Première formulation au moindre coût (programmation linéaire) pour volailles ; date de la première phytase commerciale | Waugh 1951 portait sur un aliment pour vaches laitières (EV-H-0045) |
| KG-H03 | P3 | Rendements de production villageoise de termites et d'asticots | Pratiques documentées (EV-H-0051, EV-H-0052) |

## 2. Lacunes de couverture

| ID | Domaine | Ce qui manque | Cause | Action prévue |
|---|---|---|---|---|
| KG-COV-01 | tous | OpenAlex / Semantic Scholar / Google Scholar | quota IP / 403 | clé API OpenAlex fournie par l'utilisateur ; sinon Crossref + Europe PMC |
| KG-COV-02 | brevets | Espacenet / PATENTSCOPE / CNIPA | 403 | échantillonnage Google Patents |
| KG-COV-03 | N, H | CAB Abstracts | abonnement | AGRIS, HAL, J-STAGE |
| KG-COV-04 | Chine | CNKI / Wanfang (littérature sur 低蛋白日粮, 黑水虻, 细胞培养肉) | blocage | WebSearch en chinois, revues chinoises en accès libre (rhhz.net) |
| KG-COV-05 | C, E | Textes intégraux de Pasitka 2023, 2024 et 2025 (*Nature Food*) | paywall | manuscrits auteur, données supplémentaires, brevets correspondants |
| KG-COV-06 | C | *Disclosable safety narratives* de la FDA (CCC 000002, CCC 000039) | non encore lus | priorité de la phase 4 |
| KG-COV-07 | N, E | Textes EUR-Lex (règlement 2021/1372, registre des additifs) | EUR-Lex renvoie une page vide (HTTP 202) | publications.europa.eu, legislation.gov.uk (pour le droit UE antérieur au Brexit) |
| KG-COV-08 | N | Havenstein 1994/2003 en texte intégral | ScienceDirect 403 | rechercher les PDF sur les dépôts universitaires |
| KG-COV-09 | N | Tables INRAE-CVB, Rostagno, NRC 1994 | non lus | sources d'accès libre partielles |
| KG-COV-10 | A | CIQUAL (503) ; rapports NECTAR et GFI primaires | indisponible / lus via la presse | réessayer ; sites officiels |
| KG-COV-11 | N, E | Littérature brésilienne (SciELO 403, Embrapa) | blocage | Crossref/Europe PMC, WebSearch en portugais |
| KG-COV-12 | E | Textes primaires MFDS (Corée), NHC (Chine), OSAV (Suisse), ministère de la Santé israélien ; lois de six États américains | non lus | phase 4 réglementaire |
| KG-COV-13 | H | Articles du *Journal of Biological Chemistry* 1922–1925 (vitamine D), Moore 1946 | 403 | archive.org, PMC (JBC est en accès libre sur jbc.org pour les archives — à retester) |
