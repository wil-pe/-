# Inventaire des capacités réellement disponibles (Phase 1)

Inspection effectuée le 2026-10-25 dans un conteneur cloud éphémère (Linux, Python 3.13), par tests directs.
Chaque ligne indique ce qui a été **testé**, pas ce qui est supposé.

## Capacités confirmées

| Capacité | Statut | Comment | Conséquence |
|---|---|---|---|
| Recherche Internet | OK | `WebSearch` (index US, renvoie liens + résumé synthétique) | Les résumés synthétiques de l'outil **ne sont pas des sources** : toute valeur doit être revérifiée dans la source primaire. |
| Lecture de pages web | OK, partiel | `WebFetch` (page convertie, interprétée par un petit modèle) | Les paywalls (Nature, Elsevier, Wiley…) redirigent vers une authentification : seul le résumé est lisible. |
| PubMed | OK | MCP PubMed (recherche, métadonnées, texte intégral PMC) + E-utilities (`search.py pubmed`) | Couverture biomédicale ; peu de littérature agronomique non indexée. |
| Europe PMC | OK | API REST (`search.py epmc`, `epmc-full`) : résumés + texte intégral libre (XML) | Principal outil de lecture intégrale des articles en accès libre. |
| Crossref | OK | API REST (`search.py crossref`, `doi`) | Vérification des métadonnées / DOI. |
| Consensus | OK, limité | MCP, 3 résultats par requête (compte gratuit), max 3 appels simultanés | Outil de découverte, pas d'exhaustivité. |
| bioRxiv | Limité | MCP par date/catégorie seulement (pas de mots-clés) ; site web en 429 | Découverte des prépublications via Europe PMC (qui indexe bioRxiv). |
| J-STAGE (Japon) | OK | API (`search.py jstage`) | Littérature japonaise (培養肉, ブロイラー飼料…). |
| HAL / theses.fr (France) | OK | API (`search.py hal`, `theses`) | Thèses et rapports INRAE, ITAVI… |
| archive.org | OK | Recherche + texte OCR intégral (`search.py archive`, `archive-text`) | Accès à ~2 600 ouvrages avicoles antérieurs à 1925 en texte intégral. |
| OSTI (DOE, USA) | OK | API (`search.py osti`) | Rapports techniques (dont un rapport CRADA sur la viande cultivée, 2026). |
| AGRIS (FAO), FAO Open Knowledge, FAOSTAT | Page d'accueil OK | Via WebFetch | Données statistiques à extraire page par page. |
| EFSA, EUR-Lex, FDA, SFA (Singapour) | OK | Via WebFetch | Textes réglementaires officiels consultables. |
| Google Patents | Partiel | Pages individuelles lisibles via `WebFetch` ; recherche bloquée (captcha) ; recherche via `WebSearch` avec `allowed_domains=["patents.google.com"]` | Cartographie des brevets par échantillonnage, non exhaustive. |
| CyberLeninka (Russie) | OK | Via WebFetch/curl | Littérature russophone. |
| Exécution de code | OK | Python 3.13, pandas, pdfplumber, pypdf, BeautifulSoup, lxml, openpyxl ; `pdftotext`, `jq`, `curl` | Extraction PDF/tableaux, calculs, modèles économiques. |
| Fichiers | OK | Création/modification dans le dépôt git | Base de connaissances en fichiers. |
| Sous-agents parallèles | OK | Outil `Agent` (agents généralistes, exécution en arrière-plan, simultanée) | Architecture à 6 agents + coordinateur. Les agents ne communiquent pas entre eux : échanges par fichiers (`agents/<X>/handoff.md`). |
| Persistance entre sessions | OK via git | Le conteneur est éphémère ; la persistance passe par des commits poussés sur la branche `claude/chicken-muscle-research-lab` du dépôt `wil-pe/-` | Fichier `progress.md` + commits fréquents. |

## Capacités indisponibles ou bloquées

| Source | Statut observé | Solution de remplacement |
|---|---|---|
| OpenAlex | 429 : budget gratuit quotidien partagé par l'adresse IP épuisé ; une clé gratuite exige d'envoyer une adresse e-mail (non fait sans accord de l'utilisateur) | Crossref + Europe PMC + Consensus (qui indexe OpenAlex). **L'utilisateur peut fournir une clé OpenAlex.** |
| Semantic Scholar API | 429 sans clé | Consensus (qui indexe Semantic Scholar) ; Crossref pour les références. |
| Google Scholar | 403 | WebSearch + Europe PMC + Crossref. |
| Espacenet, WIPO PATENTSCOPE, EPO OPS | 403 | Google Patents (pages) via WebFetch ; WebSearch ciblé. |
| Justia Patents, FreePatentsOnline, PatentsView | 403 / timeout | Idem. |
| CNIPA (Chine), CNKI | Bloqué / timeout | WebSearch en chinois ; articles chinois indexés dans Europe PMC/Crossref ; Wanfang accessible (page d'accueil 200, recherche à tester). |
| CAB Abstracts / CABI Digital Library | 403 (et abonnement) | Non consulté. AGRIS (FAO) comme substitut partiel. |
| SciELO (recherche) | 403 | Articles SciELO indexés dans Crossref/Europe PMC ; WebSearch en portugais/espagnol. |
| Gallica (BnF), Biodiversity Heritage Library | 403 | archive.org (texte intégral) ; HathiTrust (métadonnées). |
| Google Books API | 429 | archive.org. |
| Bases sur abonnement (Web of Science, Scopus, ScienceDirect texte intégral) | Non disponibles | Résumés uniquement ; versions auteur en accès libre recherchées (PMC, HAL, dépôts institutionnels). |

## Règles qui en découlent

1. Un document dont seul le résumé a été lu est enregistré `access_level=abstract_only`. Jamais `full_text_read`.
2. Une valeur trouvée dans un résumé de moteur de recherche ou dans la presse est `secondary_report` tant qu'elle n'a pas été retrouvée dans la source primaire.
3. La couverture brevets est un **échantillonnage** (Google Patents page par page), pas une analyse de familles exhaustive.
4. La couverture chinoise, coréenne et brésilienne passe surtout par WebSearch et par les articles indexés internationalement : biais documenté dans la matrice de couverture.
