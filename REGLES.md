# RÈGLES.md — Spécification des règles implémentées dans le globe historique

Document de référence : chaque règle de représentation, de classement ou de
comportement implémentée dans `globe.html` / `build_*.py` est spécifiée ici.
Toute nouvelle règle doit être ajoutée à ce fichier (exigence utilisateur,
2026-07-06).

## R1 — Frise chronologique
- **R1.1** : 44 pas de temps, de −10 000 à 2010. Pas millénaires avant −2000,
  puis −1500, −1000, −700, −500, −300, −100, 1, séculaires de 100 à 1800,
  puis **cadence resserrée à l'époque contemporaine** : 1815, 1880, 1900, 1914,
  1920, 1930, 1938, 1945, 1960, 1994, 2000, 2010.
- **R1.2** : lecture automatique = 1 pas / 2,5 s ; **pause doublée (5 s)** sur les
  siècles charnières majeurs {300, 900, 1100, 1900}. Arrêt au toucher du globe,
  du slider, des flèches ; désactivée si `prefers-reduced-motion`.

## R2 — Niveau d'organisation socio-politique (code couleur évolutif)
Classement `niveau(n)` sur le nom source de l'entité, 5 paliers :
- **N0 chasseurs-cueilleurs** : regex `hunter|gatherer|forag|fisher|shellfish|paleo-`
  → gris sombre `hsl(t, 3%, 17%)`.
- **N1 nomades, pasteurs, tribus** : regex `nomad|pastoral|tribes|peoples|aboriginal|
  indigenous|proto-|cimerian` + ethnonymes courts non répertoriés
  → gris `hsl(t, 5%, 23%)` (désaturé volontairement : « niveau de développement
  retardé », exigence utilisateur).
- **N2 cultures, chefferies, cités-États** : regex `culture|chiefdom|farmer|
  civilization|city-states|complex|pottery|neolithic|bronze age` → tons sourds
  `hsl(t, 20%, 31%)`.
- **N3 royaumes, États constitués** (défaut) : palette curatée de 24 teintes
  riches (charte or/tuf).
- **N4 empires, califats, khaganats** : regex `empire|caliphate|khaganate|tsardom|
  imperial|great khanate|golden horde|soviet|ilkhanate` → palette « impériale »
  (mêmes teintes, +16 pts saturation, +12 pts lumière) + liseré clair.
- **Règle générale** : la teinte (hash du nom, stable) identifie l'entité ;
  la **luminosité croît avec le niveau d'organisation**.
- Liste blanche `ETATS_BLANCS` pour les faux positifs (Haripunjaya, Lambakannas…).
- Étiquettes : seuil d'affichage aire×zoom > 110 (N3–N4), > 300 (N0–N2, italique
  maigre) ; > 25 pour toute entité arménienne.

## R3 — Pivot arménien
- **R3.1** : toute entité dont le nom matche `armen|armén|armina|urartu|ourartou|
  syunik|artsakh|tashir|tachir|hayasa|cilicie` est rendue en **or** `#d4a548`
  (bronze `#b0762e` pour Ourartou), quel que soit son niveau.
- **R3.2 — surcouches reconstituées** (`"o":1`) : quand la source ne contient
  aucune entité arménienne à un pas de temps, une surcouche est dérivée par
  **intersection shapely** (masque Arménie arsacide de l'an 300 ∩ empire du
  moment, bornée au plateau 37–47,5°E / 37,5–41,8°N). Rendu : or translucide 50 %,
  liseré pointillé doré, étiquette prioritaire, mention « frontières
  reconstituées » dans fiche et infobulle. 37 surcouches couvrent tous les pas
  de −10000 à 2010.
- **R3.3 — corrections de source documentées** : quand le dataset contredit les
  traités (Zuhab 1639, Turkmentchaï 1828, Berlin 1878), la surcouche suit le
  traité et l'écart est consigné dans AMELIORATION.md.
- **R3.4** : préhistoire = surcouches culturelles (pas politiques) : présence
  humaine du plateau (Kouro-Araxe, Trialeti, Aratashen…).

## R4 — Villes et lieux
- **R4.1** : 62 villes datées `{de, à}` avec seuil de zoom par importance ;
  villes arméniennes (12) en or clair, seuil abaissé (visibles dès k≥3).
- **R4.2** : renommages historiques représentés par des entrées successives
  (Byzance→Constantinople→Istanbul ; Tenochtitlan→Mexico ; Edo→Tokyo).
- **R4.3** : 8 **foyers de diaspora arménienne** en triangles violets datés
  (Nouvelle-Djoulfa, San Lazzaro, Madras, Caffa…), à partir de k≥3,5.
- **R4.4** : clic dans un rayon de 12 px → fiche de la ville (dates, notice,
  bouton « Voir la période ») ; prioritaire sur le territoire.
- **R4.5** : anti-collision unique partagé étiquettes → villes → diaspora
  (boîtes englobantes, premier posé gagne ; petites aires d'abord).

## R5 — Fiches de territoire
- Clic sur un territoire → panneau : nom localisé, « Situation au \<siècle\> ·
  \<type N0–N4\> », suzeraineté, mention reconstitution, **résumé Wikipédia**
  (API MediaWiki `generator=search`, 4 phrases + vignette, langue courante,
  cache mémoire), liens article complet + **Wikipédia arménienne**, notice
  arménienne de la période le cas échéant.
- PC (≥900 px) : volet latéral droit 420 px, globe décalé à gauche (jamais
  couvert). Mobile : bottom-sheet.

## R6 — Multilingue (fr / en / hy / ru)
- Bouton 🌐 cyclique, choix mémorisé (`localStorage.globe_lang`).
- Traduits intégralement : interface, années, légende, accueil, quiz,
  33+ événements charnières, ~70 noms d'entités clés + surcouches, ~36 villes.
- Repli assumé : libellé source (anglais) pour les entités non répertoriées.
- Notices de période : **corps intégralement traduit en anglais**
  (periodes_en.json, chargé par fetch, repli FR) ; HY/RU : titres localisés à
  venir, corps FR avec bandeau explicite.
- Liens Wikipédia dans la langue courante ; lien hy.wikipedia systématique.

## R7 — Rendu cartographique
- **R7.1** : océan = dégradé radial bleu nuit **constant** ; tout polygone source
  couvrant plus d'une demi-sphère (enroulement inversé) est retourné au
  chargement.
- **R7.2** : **lacs** = anneaux intérieurs des polygones, remplis `#3a6478`
  (bleu clair), peints avant les territoires (les enclaves restent visibles).
- **R7.2b** : **16 grands lacs permanents** (ellipses approchées, dont Van,
  Sevan, Ourmia) dessinés au-dessus des territoires à chaque siècle — les lacs
  ne disparaissent jamais, quel que soit le dataset.
- **R7.3** : rotation = le point saisi reste sous le curseur (75/(base·k) °/px) ;
  zoom molette doux (1,0007^Δ, Δ borné ±180), pincement à deux doigts ;
  k ∈ [0,7, 60] ; latitude bornée ±90°.
- **R7.4** : performance : un seul render par frame (rAF) ; écrémage des entités
  hors champ (geoDistance > rayon de vue + rayon de l'entité) — 8 ms sur le
  siècle le plus dense.
- **R7.5** : fetch JSON versionnés (`?v=VDATA`) pour contourner le cache.

## R8 — Pédagogie
- Bandeau « événement charnière » sous l'année (44 entrées, 4 langues).
- Notices de période (10 longues + 13 mini, dont Première République 1920 et
  Arménie soviétique 1945) ; millésimes intermédiaires aliasés vers la notice
  pertinente (1914→1900, 1938→1945, 2010→2000…).
- Quiz : 5 QCM (siècle d'un événement, date de fondation d'une ville), leurres
  à ±600 ans / ±700 ans de la bonne réponse, score commenté.
- Légende repliée par défaut, affichée à la demande (bouton 🗺) ; voile
  d'accueil au premier lancement.

## R10 — Autocritique
- CRITIQUES.md : lu en début d'itération (priorité à la critique 🔴 la plus
  ancienne), 3 nouvelles critiques classées [UX]/[DATA] × 🔴🟠🟡 en fin
  d'itération.

## R9 — Sources
- **Neutralité (exigence utilisateur, 2026-07-07)** : aucune source
  azerbaïdjanaise ni anti-arménienne. Sources utilisées, toutes neutres :
  historical-basemaps (A. Ourednik, communautaire) ; geoBoundaries/gbOpen
  (laboratoire William & Mary, université américaine) ; Natural Earth. Les
  noms affichés sont arméniens/neutres (Stepanakert, Artsakh — jamais les
  toponymes azéris). Le tracé du Karabagh est un polygone MANUEL documenté du NKAO
  historique (1923–1991, ~4 400 km²) — plus aucune dépendance à un découpage
  administratif azerbaïdjanais.
- Frontières : historical-basemaps (aourednik) — précision d'atlas historique.
- Textes : synthèses rédigées (périodes arméniennes), résumés Wikipédia à la
  demande (langue courante).
- Aucune donnée inventée : toute reconstitution est marquée comme telle (R3.2).

### Corrections de source appliquées (build_globe_data.py)
La source historical-basemaps comporte des anachronismes sur le Caucase, corrigés
par des données sourcées (jamais inventées) — audit « qui couvre Erevan par
siècle » (it. 66–81) :
- **1700** : Erevan était séfévide (post-Zuhab 1639), pas ottoman → plateau
  oriental (est de la ligne de Zuhab) transféré Ottoman → Séfévides.
- **1880/1900** : Erevan/Syunik russes depuis Turkmentchaï (1828), pas persans
  → Transcaucasie russe transférée Perse → Empire russe.
- **1914/1915** : Caucase du Sud = Empire russe (pas d'États indépendants avant
  1918) → Arménie/Azerbaïdjan/Géorgie fusionnés dans « Russian Empire ».
- **1918/1920** : Azerbaïdjan débordant sur le Zanguezour → Arménie moderne
  soustraite. De plus l'« Arménie » de la source est l'attribution de Sèvres
  (Anatolie orientale, SANS Erevan, jamais appliquée) → remplacée par la
  Première République réelle (Erevan-centrée : Arménie moderne + Kars-Sourmalou).
- **1800–1960** : trou côtier persistant de la mer Noire orientale (Trabzon-
  Lazistan, terre ottomane/turque rendue en « mer ») → l'entité couvrant
  l'Anatolie centrale (Empire/sultanat ottoman ou Turquie) est étendue le long
  de la côte.
- **1921/1923/1930/1938** : « Grande Arménie » de Sèvres anachronique →
  remplacée par la forme réelle de la RSS (Arménie moderne).
- **1600** laissé tel quel (Erevan ottoman 1583–1604, historiquement correct).

## R11 — Affichage à la demande (décision utilisateur, 2026-07-06)
- Les informations complémentaires (légende, aides, notices non essentielles)
  ne s'affichent JAMAIS automatiquement : masquées par défaut, un bouton
  discret les ouvre/ferme. Motif : lisibilité sur iPhone, la carte d'abord.
