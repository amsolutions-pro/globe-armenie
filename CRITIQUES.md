# CRITIQUES.md — Registre d'autocritique

Processus (exigence utilisateur, 2026-07-06) :
- **Au début de chaque itération** : lire ce fichier et choisir la critique
  ouverte la plus importante à traiter.
- **À la fin de chaque itération** : ajouter 3 nouvelles critiques honnêtes,
  classées par importance, dans deux familles :
  - **[UX]** — interface, ergonomie, lisibilité, apprentissage ;
  - **[DATA]** — fiabilité des données, justesse historique et cartographique.
- Marquer `✅ traité (itération N)` quand une critique est résolue.

Importance : 🔴 majeure · 🟠 notable · 🟡 mineure.

---

## Critiques ouvertes

### [DATA]
- 🟠 **Certaines surcouches gardent le gabarit an 300** (400, 500/600, 800,
  1400–1914) faute de tracé Armenia proche dans la source : acceptable pour
  « terres arméniennes sous X », mais à documenter période par période.
- 🟡 Les dates des villes (de/à) n'ont pas été systématiquement sourcées.

### [UX]

### Nouvelles critiques (it. 22)
- 🟡 [DATA] La géométrie « Armenia an 2000 » utilisée pour la RSS 1945/1960
  ignore les micro-différences de frontières soviétiques (enclaves
  Artsvashen/Karki non représentées).

---

### Nouvelles critiques (it. 23)

### Nouvelles critiques (it. 24)
- 🟠 [DATA] **verifie_donnees.py ne contrôle pas les périodes JSON annexes**
  (periodes*.json : chaque année du slider devrait avoir sa notice dans les
  3 langues ; les trous passent inaperçus).

### Nouvelles critiques (it. 25)
- 🟡 [DATA] La correspondance année→notice (indexPeriode + MINI) vit dans
  globe.html et n'est pas contrôlée par verifie_donnees.py : un siècle sans
  notice passerait inaperçu.
- 🟡 [UX] Les avertissements de verifie_donnees.py ne sont visibles que du
  développeur : aucun signal côté site quand une traduction manque.

- 🟡 [UX] Aucune indication dans l'UI que la notice affichée est une
  traduction (vs texte original français).

### Nouvelles critiques (it. 27)
- 🟡 [UX] Le bouton 🗺 n'a pas de libellé traduit (aria-label français en dur).

### Nouvelles critiques (it. 29)
- 🟡 [UX] Le chevron ⌄ sous l'année est petit : vérifier sa visibilité sur
  un vrai écran iPhone (peut nécessiter une taille supérieure).
- 🟡 [UX] L'ouverture du détail-titre ne se replie pas automatiquement quand
  on manipule le slider (il masque un peu la carte pendant la navigation).

### Nouvelles critiques (it. 30)
- 🟡 [DATA] La relecture hy a été faite par le même modèle que la traduction :
  une validation par un locuteur natif reste souhaitable à terme.
- 🟡 [DATA] periodes_en.json n'a jamais eu de relecture équivalente.

### Nouvelles critiques (it. 31)
- 🟠 [DATA] **La satrapie −500 utilise le tracé Armenia de −300** (Orontides) :
  plus proche que l'an 300, mais toujours anachronique d'un siècle et demi.
- 🟡 [DATA] Le masque « Grande Arménie » −100 (Armenia bc1) est postérieur aux
  conquêtes de Tigrane (95–66) : l'apogée impériale n'est pas représentée.
- 🟡 [DATA] Le choix du masque par période (armenia:<an> vs gabarit) n'est
  documenté que par des commentaires du script : un tableau dans README/REGLES
  serait plus transparent.

### Nouvelles critiques (it. 32)
- 🟡 [DATA] Le tracé 1878 est dessiné à main levée (15 points) : le comparer
  aux limites réelles de l'oblast de Kars et du gouvernorat d'Erevan.
- 🟡 [DATA] La ligne « Zanguezour → Karabagh » du polygone russe traverse un
  angle du Karabakh persan : vérifier au zoom en 1880.
- 🟡 [UX] Aucune capture d'écran de contrôle n'est archivée après un
  changement de frontières : ajouter un rendu de référence par époque
  faciliterait la relecture visuelle.

### Nouvelles critiques (it. 33)
- 🟡 [DATA] Les cibles carte sont limitées aux surcouches arméniennes (o=1) :
  ajouter les grands empires du siècle varierait le quiz.

### Nouvelles critiques (it. 34)
- 🟡 [UX] Le bouton « Passer » compte faux sans confirmation : un appui
  accidentel coûte un point.
- 🟡 [UX] Pendant une question carte, la rotation auto/lecture reste
  possible et peut dérouter (changer de siècle pendant la question).
- 🟡 [DATA] `reponseCarte({n:"__passe__"})` est un objet factice : fragile si
  reponseCarte évolue (préférer un paramètre explicite).

### Nouvelles critiques (it. 35)
- 🟡 [UX] Le séparateur « Notice de la période » n'apparaît que si une fiche
  territoire précède : quand la notice est seule, aucun rappel qu'on peut
  cliquer un territoire pour enrichir le panneau.
- 🟡 [UX] La fiche territoire n'a pas de libellé de section symétrique
  (« Territoire sélectionné ») — la hiérarchie reste implicite en haut.
- 🟡 [DATA] L'extrait Wikipédia se charge même quand le panneau est fermé
  aussitôt : petite requête inutile (annuler si panneau fermé).

### Nouvelles critiques (it. 36)
- 🟠 [DATA] **NIVEAU_FIXE est global, pas daté** : « Russia » de 1994 et de
  l'époque tsariste reçoivent le même niveau ; la table devrait accepter
  (entité, plage d'années).
- 🟡 [DATA] La liste NIVEAU_FIXE a été constituée par un scan des aires >300
  deg² : les empires plus petits sans mot-clé (Wu…) restent non couverts.
- 🟡 [UX] Le changement de niveau modifie la luminosité de gros pays (URSS,
  Chine…) : vérifier visuellement qu'aucun contraste ne casse la lecture.

### Nouvelles critiques (it. 37)
- 🟠 [DATA] **La part Mardakert de la NKAO reste approchée** (Tartar ∩ boîte
  46.4–47.05 / 39.9–40.35) : le district d'Aghdara n'existe pas dans
  geoBoundaries ; affiner quand une source ADM2 post-2023 sera disponible.
- 🟡 [DATA] Le fichier geo/aze_adm2.geojson est gitignoré : le build re-télécharge
  depuis un commit épinglé (9469f09) — vérifier la pérennité du lien.

### Nouvelles critiques (it. 38)
- 🟡 [UX] Le nouveau nom est long (« Haut-Karabagh et districts occupés… ») :
  vérifier qu'il ne déborde pas dans la bulle sur mobile.

### Nouvelles critiques (it. 39)
- 🟡 [DATA] La Caspienne et l'Aral ne sont pas dans lacs.json (la Caspienne
  vient des trous du dataset) : vérifier qu'aucun siècle ne l'affiche mal.
- 🟡 [UX] Les lacs réels étant plus détaillés, vérifier la performance du
  rendu sur mobile (16 tracés × ~50 points redessinés à chaque frame).

### Nouvelles critiques (it. 40)
- 🟡 [UX] Le bouton ↗ porte à 6 le nombre de boutons flottants empilés :
  la colonne devient haute sur petits écrans — envisager un regroupement.
- 🟡 [UX] La copie de lien (fallback desktop) n'affiche qu'un ✓ furtif :
  un toast « Lien copié » serait plus explicite.

### Nouvelles critiques (it. 41)
- 🟡 [DATA] globe_data_init.json duplique l'année -700 (124 Ko) : le
  chargement complet pourrait la sauter (micro-optimisation).

### Nouvelles critiques (it. 42)
- 🟡 [UX] Sur desktop rapide, le badge de phase 2 disparaît avant d'être
  visible : impossible de juger son apparence réelle — vérifier sur 4G.
- 🟡 [DATA] Le libellé « Haut-Karabagh et districts occupés… » déborde
  peut-être de la bulle au clic (non testé au zoom mobile).
- 🟡 [UX] La vue 1994 montre les frontières modernes très simplifiées
  (dataset world_1994 grossier) : contraste avec les lacs désormais précis.

### Nouvelles critiques (it. 43)
- 🟡 [UX] Aucun retour visuel si l'an du lien est invalide (silencieusement
  ignoré).
- 🟡 [DATA] localStorage peut être indisponible (navigation privée iOS) :
  try/catch posés, mais non testés.

### Nouvelles critiques (it. 44)
- 🟡 [DATA] La notice hy[4] (Arsacides) indique « 66 – 428 » sans précision
  d'ère : ambigu pour un lecteur non averti (contrairement à « Ք.ա. … »).
- 🟡 [UX] Le lien ?an= validé en desktop uniquement ; à tester sur iPhone
  (Safari gère parfois différemment location.search avec l'écran d'accueil).

### Nouvelles critiques (it. 45)
- 🟡 [DATA] L'extraction de SPECS par regex dans verifie_donnees.py casse
  silencieusement si le format du bloc change (split sur « SPECS = [ »).
- 🟡 [UX] « données v2026-07-06r » n'est lisible qu'en ouvrant la légende :
  acceptable (R11) mais non documenté dans l'aide.
- 🟡 [UX] Les suffixes de version (d, e, … r) ne disent pas ce qui a changé :
  un lien vers le journal des commits serait plus utile.

### Nouvelles critiques (it. 46)
- 🟡 [UX] Le surlignage de 1,5 s n'est pas annoncé : l'utilisateur peut
  cliquer ailleurs pendant ce délai (événements non bloqués).
- 🟡 [UX] Sur un territoire minuscule (Karabagh), le surlignage peut être
  invisible sans zoom : centrer/zoomer brièvement serait plus clair.
- 🟡 [DATA] afficheVerdictCarte relit quizEtat.qs[quizEtat.i].nom : si
  l'utilisateur enchaîne très vite, l'état peut avoir avancé (bord de course).

### Nouvelles critiques (it. 47)
- 🟡 [UX] Le menu langue s'ouvre vers la gauche du bouton : sur très petit
  écran il peut sortir du cadre — vérifier le positionnement sur iPhone.
- 🟡 [UX] Un simple clic sur le bouton n'affiche plus le cycle rapide : les
  habitués du cycle FR→EN→HY→RU doivent maintenant viser dans le menu.

### Nouvelles critiques (it. 48)
- 🟡 [UX] Le pulse d'année est ignoré si prefers-reduced-motion est actif —
  cohérent, mais alors aucun signal de pause pour ces utilisateurs.
- 🟡 [UX] La pause double (2 × 2,5 s) sur un tournant peut sembler longue :
  vérifier le ressenti sur mobile pendant une lecture complète.

### Nouvelles critiques (it. 49)
- 🟡 [A11Y] Le menu langue manque encore d'un piège de focus complet (Tab
  peut sortir du menu ouvert) : suffisant pour l'usage mais imparfait.
- 🟡 [A11Y] Les boutons flottants (֎, ✦, ?, ↗, 🗺) n'ont pas tous d'états
  focus visibles au clavier : passe d'accessibilité globale à prévoir.

### Nouvelles critiques (it. 50)
- 🟡 [UX] L'écran de chargement affiche « → 1920 » mais pas l'événement de
  cette année : un aperçu (charnière) donnerait envie d'attendre.
- 🟡 [DATA] Deux critiques auto-générées se sont révélées fausses (provinces
  cliquables dans globe.html, unification MAJEURS) : signe qu'il faut vérifier
  le code avant d'inscrire une critique DATA/UX.

### Nouvelles critiques (it. 51)
- 🟡 [A11Y] L'annonce aria-live ne liste pas les entités visibles à l'écran
  (seulement année + charnière) : un lecteur d'écran ne « voit » pas la carte.

### Nouvelles critiques (it. 52)
- 🟡 [A11Y] Les flèches ←→ déplacent le temps même quand le focus est sur un
  bouton : comportement global pratique mais surprenant au clavier.
- 🟡 [DATA] L'annonce aria-live pourrait mentionner le niveau de zoom / la
  région centrée, pas seulement l'année.

### Nouvelles critiques (it. 53)
- 🟡 [A11Y] Le liseré intérieur du canvas (box-shadow inset) n'apparaît qu'au
  focus clavier : vérifier qu'il ne gêne pas visuellement pendant le rendu.

### Nouvelles critiques (it. 54)
- 🟡 [DATA] L'audit n'a porté que sur Chrome desktop : pas de mesure réelle
  sur iPhone/4G (débit et rendu tactile peuvent différer).
- 🟡 [UX] Le globe compte beaucoup de fonctionnalités peu découvrables
  (partage, quiz carte, détail-titre) : un mini-tutoriel au 1er lancement
  au-delà du voile actuel aiderait.
- 🟡 [DATA] Fizouli/Agdam en entier dans la zone 1994 : ne peut être affiné
  qu'avec un polygone d'occupation SOURCÉ (clipper sur une longitude inventée
  violerait R3.2) — en attente d'une source, pas d'un correctif arbitraire.

## Critiques invalidées
- ❌ (it. 54) [UX] « 33 erreurs console » : ce ne sont PAS des erreurs de la
  page — signature `:0:0` « message channel closed », émises par une extension
  Chrome. La page globe.html a 0 erreur propre (vérifié à l'audit).

## Critiques invalidées
- ❌ (it. 53) [DATA] « 2010 devrait différer de 1994 » : rejeté — la ligne de
  contact du Karabagh est restée gelée du cessez-le-feu de 1994 à la guerre de
  2020 ; des surcouches identiques sur cette période sont historiquement justes. (vérification du code)
- ❌ [DATA] « Notices hy sans provinces → libellé français au clic » : faux,
  globe.html n'affiche pas les provinces au clic (champ utilisé seulement
  dans atlas_armenie_historique.html, page francophone séparée).
- ❌ [UX] « Unifier MAJEURS avec les événements charnière » : rejeté —
  MAJEURS est un sous-ensemble volontairement restreint (double-pause sur les
  tournants les plus importants) ; tout unifier ferait pauser partout.

### Nouvelles critiques (it. 56)
- 🟡 [DATA] Le contour « foyer arménien » est l'aire MAXIMALE (Arménie an 300 +
  Cilicie) : il ne varie pas dans le temps, alors que le peuplement s'est réduit
  après 1915/1923 — un second contour « aire résiduelle moderne » serait juste.
- 🟡 [UX] 6 boutons flottants empilés + bouton présence = colonne haute sur
  petit écran ; regroupement à envisager.

### Nouvelles critiques (it. 57)
- 🟡 [UX] Le pictogramme de légende (rectangle pointillé) diffère un peu du
  rendu réel (contour libre) : cohérence graphique perfectible.

### Nouvelles critiques (it. 58)
- 🟡 [UX] La légende défilante (overflow-y) est peu visible comme telle : sur
  un écran minuscule où elle déborde, l'utilisateur peut ne pas deviner qu'elle
  défile.
- 🟡 [DATA] « Aire maximale (an 300) » : formulation dense ; une note d'aide
  expliquerait mieux que le foyer réel s'est réduit après 1915.

### Nouvelles critiques (it. 59)
- 🟠 [UX] Toujours pas de test tactile sur iPhone RÉEL (Safari iOS) : les
  vérifs se font en Chrome à fenêtre étroite (390 px), fidèle au layout mais
  pas au tactile ni au moteur WebKit.

### Nouvelles critiques (it. 60)
- 🟡 [DATA] Les notices 2020/2023 n'ont pas de version arménienne dédiée
  (MINI_HY inexistant) : en hy elles retombent sur le FR — traduire.
- 🟡 [UX] La carte 2020/2023 (fond world_2010) ne montre pas la perte
  territoriale réelle : seule la surcouche 2020 (Artsakh résiduel) et la
  notice la décrivent.

### Nouvelles critiques (it. 61)
- 🟡 [UX] Beaucoup d'années récentes ont maintenant des notices riches : un
  fil chronologique déroulant du XXe–XXIe siècle serait un bon complément.

### Nouvelles critiques (it. 62)
- 🟡 [UX] La densité de villes/capitales du XXe-XXIe (Deir ez-Zor, Musa Dagh…)
  n'apparaît qu'à fort zoom : un rappel dans la notice suffirait.

### Nouvelles critiques (it. 63)
- 🟡 [DATA] Seules les 5 notices récentes ont une version hy (MINI_HY) ; les
  mini-notices anciennes (préhistoire, Timour…) restent FR/EN en mode hy.
- 🟡 [DATA] Les noms de lieux/capitales (Deir ez-Zor, Spitak…) restent en
  graphie latine même en arménien (pas de VILLES_HY pour ces lieux de notice).
- 🟡 [UX] La traduction hy récente n'a pas été relue par un tiers (même risque
  qu'it. 30) : à faire valider par un locuteur.

### Nouvelles critiques (it. 64)
- 🟡 [DATA] Les notices FR anciennes (préhistoire→1400) restent sans HY :
  gros volume, à traduire progressivement.
- 🟡 [UX] Un fil chronologique récapitulatif (1915→2026) donnerait une vue
  d'ensemble des notices désormais riches.

### Nouvelles critiques (it. 65)
- 🟡 [DATA] Le parcours XIXe-XXIe est intégralement en hy ; restent sans hy les
  mini-notices antérieures à 1878 (préhistoire → 1400) et les notices longues
  de periodes_hy.json (déjà traduites en it.26).
- 🟡 [DATA] Volume de traduction hy important cumulé sans relecture native :
  planifier une passe de relecture globale.
- 🟡 [UX] Le panneau notice devient long sur ces siècles riches ; un repli
  « aperçu / détail » (R11) allègerait la lecture mobile.

### Nouvelles critiques (it. 66)
- 🟡 [DATA] 1920 conserve l'Arménie « de Sèvres » (17 deg²) : les 3 républiques
  caucasiennes existaient bien en 1920, mais la République n'a jamais contrôlé
  l'attribution wilsonienne — choix assumé (la notice l'explique), faute d'un
  polygone sourcé du contrôle réel de 1920.
- 🟡 [DATA] En 1914/1915 les territoires caucasiens sont désormais « Empire
  russe » (correct) mais sans sous-libellé « gouvernorats d'Erevan/Kars » :
  la granularité impériale est perdue.
- 🟡 [UX] Vérifier en ligne le rendu corrigé de 1914–1921 (couleurs, absence
  de trou) après déploiement.

### Nouvelles critiques (it. 67)
- 🟡 [DATA] 1918 et 2020 conservent des géométries « de Sèvres » / résiduelles
  approximées ; le contrôle réel de la Première République en 1918-1920 reste
  sans polygone sourcé.

### Nouvelles critiques (it. 68)
- 🟡 [DATA] Les tracés NKAO et zone 1994 sont désormais manuels (documentés,
  ~4 700 et ~13 900 km²) : moins précis que des limites cadastrales, à raffiner
  si une source NEUTRE de l'oblast historique devient disponible.
- 🟡 [DATA] geo/aze_adm2.geojson supprimé : vérifier qu'aucun autre script n'y
  fait référence (build_globe_data n'en dépendait pas).
- 🟡 [UX] Vérifier en ligne (VDATA m) que le Karabagh redessiné reste cohérent
  visuellement au zoom.

### Nouvelles critiques (it. 69)
- 🟡 [DATA] La zone de contrôle 1994 manuelle englobe Fizouli/Agdam en entier
  (occupation partielle) — même limite qu'avant, mais désormais sans source AZE.

### Nouvelles critiques (it. 70)
- 🟡 [DATA] Toutes les années arméniennes modernes (1915→2026) ont désormais
  une notice dédiée trilingue ; le chantier de fond bascule vers les périodes
  anciennes (mini-notices sans hy, sourçage des dates de villes).
- 🟡 [UX] Le mémorial de Sardarabad (1968) pourrait être une ville/lieu
  affichable sur la carte, pas seulement dans la notice.
- 🟡 [DATA] Bash-Aparan/Karakilissa sont des lieux de notice sans entrée dans
  VILLES : non cliquables sur le globe.

### Nouvelles critiques (it. 71)
- 🟡 [DATA] 1918/1920 : l'Arménie reste la « Grande Arménie » de Sèvres
  (source), non clippée (années d'indépendance) — cohérent mais généreux.
- 🟡 [DATA] 1918 : l'Azerbaïdjan a été recentré par soustraction de l'Arménie
  moderne ; vérifier qu'il ne laisse pas un liseré fin le long de la frontière.

### Nouvelles critiques (it. 73)
- 🟡 [DATA] Le contrôle d'enroulement ne teste que l'anneau extérieur ; un trou
  (lac) inversé passerait — cas rare mais non couvert.
- 🟡 [DATA] Audit limité aux surcouches et à l'enroulement ; la justesse
  historique fine des tracés source (hors Arménie) n'est pas vérifiable.
- 🟡 [UX] verifie_donnees.py est un outil dev ; un récap visuel des surcouches
  par période aiderait la relecture humaine.

### Nouvelles critiques (it. 74)
- 🟠 [DATA] Relecture orthographique/terminologique native des notices hy
  toujours en attente (vérif automatique ne couvre que les nombres) : idéalement
  un locuteur arménien relit les 13 notices récentes.

### Nouvelles critiques (it. 75)
- 🟡 [DATA] Le contrôle ne compare que MINI/MINI_EN/MINI_HY ; les notices
  longues (periodes*.json) ne sont pas croisées numériquement.
- 🟡 [UX] Les avertissements de verifie_donnees.py s'accumulent ; un mode
  « --strict » qui n'affiche que les erreurs aiderait en CI.

### Nouvelles critiques (it. 76)
- 🟡 [DATA] Les toponymes anciens hy (Խիրբեթ Քերաք, Յամնայա…) sont des
  translittérations à faire valider par un spécialiste.
- 🟡 [UX] La couverture hy est désormais inégale (moderne complète, ancienne
  partielle) : un indicateur « traduction disponible » par langue aiderait.

### Nouvelles critiques (it. 77)
- 🟡 [DATA] Traduction des dates en chiffres romains (V–IV հազարամյակ, IX դար)
  cohérente FR↔HY mais divergente de l'anglais (arabe) : sans gravité.
- 🟡 [UX] La densité de notices anciennes en hy justifierait un test de rendu
  arménien sur ces siècles préhistoriques.

### Nouvelles critiques (it. 78)
- 🟡 [DATA] 1918/1920 : l'Arménie reste la « Grande Arménie » de Sèvres (17
  deg², jusqu'en Anatolie) — non signalée par l'utilisateur mais généreuse ;
  faute de polygone sourcé du contrôle réel, laissée telle quelle.
- 🟡 [DATA] La soustraction Az−Arménie moderne peut laisser un fin liseré le
  long de la frontière Syunik/Nakhitchevan : à vérifier au zoom.

### Nouvelles critiques (it. 79)
- 🟡 [DATA] MINI_HY complet, mais periodes_hy.json (notices longues -700→1815)
  mériterait une relecture native cohérente avec les mini-notices.
- 🟡 [DATA] Translittérations arméniennes de toponymes préhistoriques
  (Քարահունջ, Ակնաշեն, Գյոբեկլի Թեփե…) à valider par un spécialiste.

### Nouvelles critiques (it. 80)
- 🟡 [DATA] Le transfert Perse→Russie utilise un polygone Transcaucasie fixe :
  à comparer au tracé réel de la frontière de Turkmentchaï (1828) le long de
  l'Araxe pour d'éventuels écarts fins.
- 🟡 [DATA] 1800/1815 laissent Erevan à la Perse/khanats (correct avant 1828)
  mais le libellé source « central Asian khanates » (1800) est peu précis.

### Nouvelles critiques (it. 81)
- 🟡 [DATA] 1600 laissé Ottoman à Erevan (défendable : occupation 1583-1604) ;
  mais l'overlay « Arménie orientale (persane) » du même an suppose déjà Zuhab
  (1639) — légère incohérence base/overlay pour ce seul millésime.
- 🟡 [DATA] Le transfert 1700 utilise une boîte (est de 43,7°) : la vraie
  frontière de Zuhab suivait l'Arpatchaï puis les crêtes — approximation.

### Nouvelles critiques (it. 82)
- 🟡 [DATA] L'audit « qui couvre Erevan » couvre l'Arménie ; les frontières
  hors-Arménie (autres régions du monde) ne sont pas auditées — hors périmètre.
- 🟡 [DATA] Les corrections de source sont des transferts par polygone/boîte :
  documentées dans REGLES, mais chacune est une approximation des vraies
  frontières historiques.

### Nouvelles critiques (it. 83)
- 🟡 [UX] La note Sources s'ouvre depuis l'accueil et la ligne de version
  (légende) ; sa découvrabilité via la version dépend de l'ouverture de la
  légende — acceptable (R11) mais peu évident.
- 🟡 [DATA] Le texte des corrections dans la note est un résumé ; il pourrait
  diverger de REGLES si l'un est mis à jour sans l'autre.

### Nouvelles critiques (it. 84)
- 🟡 [UX] Le lien GitHub est en dur ; si le dépôt est renommé/déplacé, à mettre
  à jour manuellement dans la note.
- 🟡 [UX] La note Sources pourrait indiquer la licence des données sources
  (ODbL pour Natural Earth/OSM, etc.) pour la conformité.
- 🟡 [DATA] Le résumé des corrections dans la note et REGLES sont maintenus en
  double : un point de vérité unique serait mieux.

### Nouvelles critiques (it. 85)
- 🟡 [DATA] Manquent encore Vanadzor, Goris, Dilijan, Aghtamar, Mush, Bitlis,
  Nakhitchevan pour une couverture urbaine arménienne complète.
- 🟡 [UX] Beaucoup de villes au même endroit (Chouchi/Stepanakert à 46.75) :
  vérifier qu'elles ne se chevauchent pas à faible zoom.

### Nouvelles critiques (it. 86)
- 🟡 [DATA] Beaucoup de villes anciennes (Portasar, Metsamor…) n'ont pas de
  VILLES_RU : leurs libellés russes retombent sur le nom translittéré.
- 🟡 [UX] Vérifier que Chouchi (39.76) et Stepanakert (39.82) à 46.75°E ne se
  chevauchent pas à faible zoom (z:6 pour les deux).

### Nouvelles critiques (it. 87)
- 🟡 [UX] Densité de lieux au sud-est (Tatev, Kapan, Chouchi, Stepanakert
  proches) : vérifier la lisibilité des étiquettes à moyen zoom.
- 🟡 [DATA] Aghtamar existe aussi comme capitale dans la notice 900 (MINI) :
  léger doublon conceptuel ville/notice.

### Nouvelles critiques (it. 88)
- 🟡 [DATA] La date « de » de Mush (300) et Nakhitchevan (-100) est
  approximative (ancienneté attestée mais fondation imprécise) : à sourcer.
- 🟡 [UX] 73 villes/lieux : vérifier globalement les collisions d'étiquettes
  aux zooms intermédiaires sur tout le globe.

### Nouvelles critiques (it. 89)
- 🟡 [DATA] Les monastères apparaissent dès leur date de construction (de:) ;
  certains sites (Ayrivank pour Guéghard) sont bien plus anciens — nuance
  portée par la note seulement.
- 🟡 [DATA] Couverture des monuments quasi complète ; prochaine profondeur =
  lieux de la diaspora historique ou événements ponctuels.

### Nouvelles critiques (it. 90)
- 🟡 [DOC] README mis à jour mais AMELIORATION.md (journal d'itérations) n'est
  plus tenu depuis longtemps : à archiver ou reprendre.
- 🟡 [UX] Le projet est mature ; les prochaines améliorations seront
  incrémentales (relecture native hy, tests device réel iPhone).

### Nouvelles critiques (it. 91)
- 🟡 [DATA] Le contrôle ne vérifie que le sens traduction→FR ; un nombre FR
  oublié dans la traduction n'est pas signalé (moins grave).
- 🟡 [DOC] AMELIORATION.md toujours à archiver/reprendre.

### Nouvelles critiques (it. 92)
- 🟡 [DATA] Le whitelist FIDELITE_OK est manuel : si une notice est réécrite,
  l'entrée peut devenir obsolète (référence à un index/nombre qui a changé).
- 🟡 [DATA] Un vrai nombre EN/HY masqué par erreur dans le whitelist passerait
  inaperçu : le whitelist doit rester minimal et justifié.

### Nouvelles critiques (it. 93)
- 🟡 [DATA] Le contrôle des villes lit VILLES par ligne (globe.html) : fragile
  si une entrée est reformatée sur plusieurs lignes.

### Nouvelles critiques (it. 94)
- 🟡 [DATA] La zone de plausibilité arm:1 (28–52°E, 34–43°N) exclut d'éventuels
  lieux de diaspora marqués arm:1 : vérifier qu'aucun lieu légitime hors zone
  n'est ainsi mal signalé (aucun aujourd'hui).
- 🟡 [UX] Tests device réel iPhone (Safari tactile) toujours en attente.

### Nouvelles critiques (it. 95)
- 🟡 [DOC] Le README ne mentionne pas atlas_armenie_historique dans la nouvelle
  table remaniée : vérifier qu'il y figure toujours.
- 🟡 [UX] Tests device réel iPhone toujours en attente (seule limite connue).

### Nouvelles critiques (it. 96)
- 🟡 [DATA] verifie_donnees.py grossit (9 contrôles) : un découpage en
  fonctions nommées améliorerait la lisibilité.
- 🟡 [UX] Tests device réel iPhone toujours la seule limite ouverte notable.

### Nouvelles critiques (it. 97)
- 🟡 [DATA] Le croisement compare les capitales FR (periodes + MINI) à VILLES ;
  les capitales des versions EN/HY ne sont pas recoupées (mais partagent les
  coordonnées FR, donc peu de risque).
- 🟡 [DATA] verifie_donnees.py : 9 contrôles dans une seule fonction main() —
  un refactor en fonctions nommées reste souhaitable pour la maintenabilité.
- 🟡 [UX] Tests device réel iPhone (Safari tactile) : seule limite ouverte.

### Nouvelles critiques (it. 98)
- 🟡 [DATA] La Première République 1918/1920 utilise Arménie moderne + boîte
  Kars-Sourmalou : le tracé exact (frontières de 1919-1920, Nakhitchevan
  contesté) reste approximé.
- 🟡 [DATA] Le comblement côtier PONT est un polygone manuel : à comparer à la
  vraie côte pontique si une source précise apparaît.

### Nouvelles critiques (it. 100)
- 🟡 [DATA] Le comblement côtier PONT (polygone manuel) est appliqué à
  1800–1960 ; en 1945/1960 son bord est (41,5°E) pourrait frôler Batoumi
  soviétique — vérifier l'absence de recouvrement gênant.
- 🟡 [DATA] D'autres trous de source rendus en mer peuvent exister ailleurs
  qu'au pourtour arménien (hors périmètre d'audit actuel).
- 🟡 [UX] Vérifier en ligne (VDATA f) la côte pontique sur 1900 et 1945.

### Nouvelles critiques (it. 101)
- 🟡 [DATA] L'extension revendiquée 1918 (Artsakh/Nakhitchevan/Djavakhk) est une
  interprétation « maximale » : ces régions étaient contestées, non fermement
  contrôlées — d'où le libellé « revendiquée » dans la notice.

### Nouvelles critiques (it. 103)
- 🟡 [DATA] La fermeture morphologique (buffer 0,07°) peut légèrement combler
  une concavité réelle entre deux régions : effet cosmétique mineur assumé.
- 🟡 [DATA] Les polygones des régions revendiquées restent des approximations
  manuelles ; à affiner si des tracés sourcés de 1918-1920 émergent.

### Nouvelles critiques (it. 104)
- 🟡 [DATA] 1918 et 1920 partagent la même extension maximale ; historiquement
  la République de mai 1918 (fondation) était plus petite que son apogée de
  1920 — nuance non représentée (choix « République revendiquée » assumé).
- 🟡 [DATA] Le bord ouest (Kars-Sourmalou) reste assez droit (frontière ≈
  Arpatchaï) : acceptable mais perfectible si tracé sourcé.
- 🟡 [UX] Tests device réel iPhone toujours la seule limite ouverte notable.

### Nouvelles critiques (it. 105)
- 🟡 [DATA] Le contour est du remplissage Anatolie orientale (frontière de Kars
  1921) est un polygone manuel : approximation de la vraie ligne Arpatchaï-Ararat.
- 🟡 [DATA] Kars est arménien en 1918/1920 puis turc dès 1921 (traité de Kars) :
  transition correcte mais à vérifier visuellement.

### Nouvelles critiques (it. 107)
- 🟡 [DATA] Un trou résiduel subsiste au tripoint Turquie-Iran-Irak (44,9°E ;
  38,7°N) : non comblé pour ne pas mordre sur l'Iran — négligeable (1 point).
- 🟡 [DATA] Micro-trous de tripoint isolés à d'autres années (ex : 1880-1915
  vers l'Ararat/Surmalou, 1100 vers le Nakhitchevan) : effets de bord de la
  source, très localisés.
- 🟡 [DATA] La ligne « trous » à lat 41,1 (côte pontique) est de la MER (présente
  à toutes les années dont 2026) — pas une erreur : confirmé.

### Nouvelles critiques (it. 108)
- 🟡 [DATA] L'audit grille couvre le pourtour arménien ; le reste du monde
  (Afrique, Asie, Amériques) n'est pas audité pour les trous — hors périmètre.
- 🟡 [UX] Le thread « audit cartographique » est clos ; réorienter vers d'autres
  axes (contenu, UX, tests device).

### Nouvelles critiques (it. 109)
- 🟡 [DATA] verifie_donnees.py compte 10 contrôles dans main() : refactor en
  fonctions nommées toujours souhaitable pour la maintenabilité.
- 🟡 [UX] Tests device réel iPhone : seule limite ouverte notable.

### Nouvelles critiques (it. 110)
- 🟡 [DATA] verifie_donnees.py : refactor en fonctions nommées toujours
  souhaitable (reporté : risque de régression sur l'état partagé, faible gain).
- 🟡 [UX] Tests device réel iPhone : seule limite ouverte notable.

### Nouvelles critiques (it. 111)
- 🟡 [DATA] Le comblement 1100 étend « Armenia » sur un petit rectangle : peut
  déborder de ~qq km sur Syunik/Goghtn (tous arméniens) — cosmétique négligeable.
- 🟡 [DATA] D'autres interstices topologiques de source pourraient exister
  entre entités adjacentes ailleurs (hors repères testés).
- 🟡 [UX] Tests device réel iPhone : seule limite ouverte notable.

## Critiques traitées
- ✅ (it. 111) [DATA] Micro-trou 1100 corrigé : interstice topologique de la
  source entre « Armenia » et « Syunik » à Nakhitchevan (les deux arméniens) →
  « Armenia » étendu sur le gap. Nakhitchevan AJOUTÉ au filet anti-trou
  (13 repères, tous couverts de −500 à 2026). 0 avertissement.
- ✅ (it. 110) [DATA] Contrôle anti-trou élargi de 8 à 12 repères stables
  couvrant toute la géographie arménienne : + Sis (Cilicie), Tigranakert
  (plateau ouest), Stepanakert (Karabagh), Tabriz (bordure perse). Sortie
  identique (0 avertissement) ; filet anti-régression « rendu en mer » renforcé.
- ✅ (it. 109) [DATA] Contrôle anti-trou AJOUTÉ à verifie_donnees.py (#10) :
  8 repères arméniens (Erevan, Van, Ani, Kars, Erzurum, Bitlis, Dvin, Mush)
  doivent être couverts par une entité à chaque pas ≥ −500 (point-dans-polygone
  avec exclusion des trous/lacs). Prévient toute régression « rendu en mer ».
  Passe à 0 erreur.
- ✅ (it. 108) [DATA] Audit grille ÉTENDU à la Cilicie (32-37°E) et à la bordure
  persane (45-49°E) : les seuls « trous » (golfe d'Alexandrette 34,6/36,5 ;
  mer Caspienne lon 49) sont de la MER (présents aussi en 2026). CONCLUSION :
  audit du pourtour arménien terminé, aucun trou terrestre réel restant (hors
  1 point de tripoint Turquie-Iran-Irak, négligeable). Intégrité côtière validée.
- ✅ (it. 107, audit systématique grille) [DATA] Balayage complet du pourtour
  arménien (36-48°E, 37-42°N) toutes années : la « côte mer Noire » (lat 41,1)
  est de l'eau (non-erreur). Trous terrestres résiduels de 1918-1938 (bord
  Erzurum, sud de Van/Hakkari, Surmalou) comblés en élargissant le remplissage
  Anatolie orientale ; Arménie 1918 intacte. Reste 1 point de tripoint (négl.).
- ✅ (it. 106) [DATA] Anatolie orientale comblée VÉRIFIÉE en ligne (capture
  1921) : Van, Mush, Erzurum, Kars sont terre ottomane/turque (violet), plus de
  trou « mer ». Kars turc en 1921 (traité de Kars), arménien en 1918 :
  transition correcte. Arménie soviétique réduite à l'est. Cohérent.
- ✅ (it. 105, audit) [DATA] 🔴 Effet de bord détecté et corrigé : le retrait de
  l'Arménie de Sèvres avait laissé l'Anatolie orientale (Van, Bitlis, Erzurum,
  Kars) VIDE en 1918-1938 (rendue en « mer »). → Turquie/Empire ottoman étendu
  sur l'Anatolie orientale (moins l'Arménie du moment). Tous les trous comblés,
  Arménie 1918 intacte (garde Kars et Artsakh). Documenté REGLES R9.
- ✅ (it. 104) [UX] Rendu adouci de la République 1918 VÉRIFIÉ en ligne : coins
  arrondis, jonctions lissées, les 5 régions (Erevan, Artsakh, Nakhitchevan,
  Djavakhk, Kars) toujours présentes. Demande utilisateur pleinement satisfaite.
- ✅ (it. 103) [UX] Contours de la République 1918 adoucis : fermeture
  morphologique (buffer +0,07°/−0,07°) qui arrondit les angles vifs des boîtes
  Kars-Sourmalou et Djavakhk et lisse les jonctions, sans changer les
  territoires (aire 7,6 deg², les 5 régions toujours incluses).
- ✅ (it. 102) [DATA] République maximale 1918 VÉRIFIÉE en ligne (capture) :
  Erevan, Artsakh (Gandzasar/Chouchi/Goris/Kapan), Zanguezour, Nakhitchevan,
  Kars, Djavakhk bien dans le territoire arménien or ; Azerbaïdjan réduit à
  l'est, Géorgie au nord. Contours un peu anguleux (reconstitution) mais
  cohérents. Conforme à la précision utilisateur.
- ✅ (it. 101, précision utilisateur) [DATA] 1918/1920 : la Première République
  inclut désormais ses régions arméniennes revendiquées — Artsakh (Karabagh),
  Zanguezour, Nakhitchevan, Djavakhk (Akhalkalaki) — en plus d'Erevan et Kars
  (aire 7,5 deg²). Notice enrichie (FR/EN/HY) expliquant ces territoires
  contestés puis cédés à l'Azerbaïdjan (Karabagh, Nakhitchevan) ou restés
  géorgiens (Djavakhk). Documenté REGLES R9.
- ✅ (it. 100) [DATA] Audit du trou côtier mer Noire orientale : présent sur
  TOUTES les années 1800–1960 (pas seulement 1921). Correction généralisée —
  l'entité couvrant l'Anatolie centrale (Ottoman/Turquie, quel que soit son
  nom) est étendue le long de la côte. Tous les trous comblés (10 années
  vérifiées), 0 avertissement.
- ✅ (it. 99) [DATA] Corrections it.98 VÉRIFIÉES en ligne (captures) : 1918 =
  Première République centrée sur Erevan (Erevan/Kars dans le territoire or,
  Erzurum hors Arménie — Sèvres écarté) ; 1921 = côte pontique ottomane
  continue jusqu'à la Géorgie soviétique, la mer Noire ne déborde plus.
- ✅ (it. 98, signalements utilisateur) [DATA] 🔴 (1) 1918/1920 : la « carte de
  la Première République » montrait l'Arménie de Sèvres (Anatolie, SANS Erevan)
  → remplacée par la République réelle centrée sur Erevan (Arménie moderne +
  Kars-Sourmalou, aire 5,8 deg², contient Erevan et Kars). (2) 1921 mer Noire :
  trou côtier Trabzon-Lazistan rendu en « mer » → comblé (côte pontique
  ottomane). Documenté dans REGLES R9.
- ✅ (it. 97) [DATA] Contrôle croisé capitales↔VILLES ÉTENDU aux mini-notices
  (MINI dans globe.html) : 33 capitales extraites, 23 croisées avec VILLES,
  toutes concordantes (< 30 km). Le garde-fou couvre notices longues ET
  courtes ; rapport toujours à 0 avertissement.
- ✅ (it. 96) [DATA] Cohérence croisée capitales↔VILLES AUTOMATISÉE dans
  verifie_donnees.py (contrôle #9) : une capitale citée dans une notice et
  présente dans VILLES doit avoir les mêmes coordonnées (< 0,3° ≈ 30 km),
  sinon erreur. Rapport toujours à 0 avertissement.
- ✅ (it. 95) [DATA] Relecture croisée : les coordonnées des capitales dans les
  notices concordent avec VILLES (0 écart >30 km). [DOC] Table du README
  complétée et clarifiée (fichiers de suivi CRITIQUES/REGLES/AMELIORATION,
  verifie_donnees, presence/lacs, amorce).
- ✅ (it. 94) [DATA] Contrôle des villes renforcé : zone de plausibilité
  arménienne (28–52°E, 34–43°N) pour les lieux arm:1 (avertit si coquille de
  coordonnées). [DOC] AMELIORATION.md clôturé proprement (en-tête d'archivage
  pointant vers CRITIQUES.md/REGLES.md, contenu historique conservé).
- ✅ (it. 93) [DATA] Relecture des 77 villes : 33 arméniennes toutes dans la
  zone plausible (28–50°E, 35–42°N), aucune date incohérente (fin ≥ début).
  Contrôle AJOUTÉ à verifie_donnees.py (coordonnées bornées + cohérence des
  dates de/à des villes). Rapport toujours à 0 avertissement.
- ✅ (it. 92) [DATA] Contrôle de fidélité numérique : rapport à **0
  avertissement**. Les 2 seules divergences (numéral/lettres « 1001 églises »
  vs « mille et une » ; romain/arabe « 9th »/« IXᵉ ») sont whitelistées
  explicitement (FIDELITE_OK, commentées) ; le contrôle reste actif pour toute
  vraie erreur de date/chiffre.
- ✅ (it. 91) [DATA] Contrôle de fidélité numérique ÉTENDU aux notices longues
  periodes*.json (EN + HY vs FR) : 0 erreur de contenu ; seul faux positif =
  « 1001 églises » (EN) écrit « mille et une » (FR). Le garde-fou couvre
  désormais MINI + periodes.
- ✅ (it. 90) [UX/DOC] Densité d'étiquettes du sud (5 monastères proches)
  vérifiée en ligne en l'an 1300 : aucune collision illisible, placement propre.
  README actualisé (53 pas de temps → 2026, 77 lieux, arménien par défaut,
  sources neutres + corrections, URL en ligne).
- ✅ (it. 89) [DATA] 4 monastères emblématiques ajoutés (dates sourcées +
  traductions hy/ru) : Khor Virap (face à l'Ararat, saint Grégoire),
  Guéghard (UNESCO, 1215), Noravank (Momik, XIIIᵉ s.), Gandzasar
  (Haut-Karabagh, 1216–1238). 77 villes/lieux au total.
- ✅ (it. 88) [DATA] 3 lieux historiques ajoutés (traductions hy/ru) : Mush
  (Taron, berceau des Mamikonian, génocide 1915), Nakhitchevan (tutelle azérie
  1921, khatchkars de Djoulfa détruits), Goris (Syunik, David Bek). Nouveaux
  lieux it.87 vérifiés en ligne : affichage arménien net, sans chevauchement.
- ✅ (it. 87) [DATA] 4 hauts lieux culturels ajoutés avec dates sourcées +
  traductions hy/ru : Aghtamar (Sainte-Croix 915–921), Tatev (monastère-
  université IXᵉ/XIVᵉ s.), Sanahin & Haghpat (UNESCO, Xᵉ s.), Vanadzor
  (3ᵉ ville, séisme 1988). 70 villes/lieux au total.
- ✅ (it. 86) [DATA] Traductions hy et ru des 4 nouvelles villes ajoutées
  (Գյումրի/Гюмри, Կապան/Капан, Շուշի/Шуши, Կարին/Карин) ; en FR/EN le nom
  d'origine sert de libellé (Gyumri, Kapan, Shusha, Erzurum reconnaissables).
- ✅ (it. 85) [DATA] 4 villes arméniennes emblématiques ajoutées à VILLES avec
  dates et notes sourcées : Gyumri (Alexandropol 1837, séisme 1988), Kapan
  (capitale du Syunik Xᵉ s.), Chouchi (1752, prise 2020), Karin/Erzurum
  (Théodosiopolis Vᵉ s., génocide 1915).
- ✅ (it. 84) [UX] Note « Sources » vérifiée en ligne (s'ouvre, en arménien) ;
  ajout d'un lien vers le dépôt GitHub (github.com/amsolutions-pro/globe-armenie)
  pour la transparence du code et des données.
- ✅ (it. 83) [UX] Note « Sources & méthodologie » exposée dans l'app (R11) :
  voile ouvrable depuis l'accueil et depuis la ligne de version de la légende,
  en 4 langues — liste les sources neutres (aucune azerbaïdjanaise) et les
  corrections d'anachronismes appliquées. Transparence répondant à la demande
  utilisateur sur les sources.
- ✅ (it. 82) [DATA] Audit « qui couvre Erevan » TERMINÉ sur les 53 années :
  1700 corrigé (vérifié en ligne, Erevan séfévide) ; -100 (surcouche Artaxiade
  couvre Erevan) et 400 (base Perse + surcouche Arsacide = Persarménie) déjà
  corrects via le système de surcouches. Liste complète des corrections de
  source documentée dans REGLES R9.
- ✅ (it. 81) [DATA] Audit « qui couvre Erevan » sur les 53 années : cohérent
  sauf 1700 (corrigé). 1880/1900 (Erevan russe) vérifié visuellement en ligne.
  🔴 1700 : la source plaçait Erevan sous les Ottomans alors qu'après Zuhab
  (1639) l'Arménie orientale était séfévide → plateau oriental transféré
  Ottoman→Séfévides (Erevan désormais persan).
- ✅ (it. 80) [DATA] Couverture arménienne de TOUTE la frise (53 années)
  vérifiée en ligne : 0 repli français. [DATA] 🔴 Audit 1800-1900 : erreur
  détectée et corrigée — en 1880/1900 la source plaçait Erevan/Syunik sous la
  PERSE alors qu'ils étaient russes depuis Turkmentchaï (1828) → Transcaucasie
  russe transférée de la Perse vers l'Empire russe. 1800/1815 laissés (Erevan
  encore persan, correct).
- ✅ (it. 79) [DATA] Couverture MINI_HY COMPLÈTE : ajout de -8000
  (néolithisation) et -5000 (villages de l'Araxe, Karahunj) → toutes les
  mini-notices ont leur version arménienne. 1920 (Azerbaïdjan corrigé)
  vérifié visuellement en ligne : frontière nette, plus de débordement.
- ✅ (it. 78, signalement utilisateur) [DATA] 🔴 1920 : Azerbaïdjan trop grand
  (13,5 deg², débordant sur le Zanguezour à 43,5°E) → correction du fond 1920
  étendue de 1918 à 1920 (soustraction de l'Arménie moderne) : Azerbaïdjan
  ramené à 10,3 deg², bord ouest 44,7°E.
- ✅ (it. 77) [DATA] MINI_HY étendu à 4 nouvelles mini-notices préhistoriques :
  -10000 (premiers habitants, Nor Geghi, Portasar), -4000 (Chalcolithique,
  vin d'Areni), -2000 (aube du plateau, Trialeti), -1000 (unification
  ourartéenne, Aramé) ; fidèles au FR, contrôle numérique OK.
- ✅ (it. 76) [DATA] Extension de MINI_HY aux mini-notices anciennes
  emblématiques : -3000 (culture Kouro-Araxe), -1500 (Hayasa-Azzi et Nairi),
  1400 (entre Timour et les Turkmènes) traduites en arménien, fidèles au FR ;
  contrôle de fidélité numérique OK.
- ✅ (it. 75) [DATA] Contrôle de fidélité numérique des notices AUTOMATISÉ dans
  verifie_donnees.py : compare les nombres des aperçus EN/HY à ceux du FR
  (séparateurs de milliers et décimaux normalisés), alerte si un chiffre de la
  traduction est absent de l'original. 0 erreur sur les notices modernes.
- ✅ (it. 74) [DATA] Fidélité numérique des traductions hy VÉRIFIÉE : aucune
  notice arménienne (1900→2023) ne contient de nombre absent du français ;
  tous les chiffres-clés présents (1,5 M, 24 avril, 25 000, 7 déc., 21 sept.
  1991, 44 j., 6 500, 100 000, 19 sept., 94 %, 7 juil. 1923, 13 oct. 1921,
  28 mai, 1045). R3.2 respecté ; relecture native encore souhaitable.
- ✅ (it. 73) [DATA] Audit de carte complet : 0 surcouche débordant du plateau/
  Cilicie/Karabagh, 0 anneau inversé (calcul sphérique), 0 écart aire
  déclarée/réelle. Contrôle d'enroulement sphérique AJOUTÉ à verifie_donnees.py
  (attrape le bug historique des anneaux inversés qui remplissent la sphère).
- ✅ (it. 72) [DATA] Corrections it.71 VÉRIFIÉES en ligne (captures) : 1914 =
  Caucase russe unifié sans frontière interne (Erevan dans le bloc vert Empire
  russe) ; 1921 = Arménie en forme réelle (Sevan visible, plus de triangle),
  Géorgie/Azerbaïdjan/Ottoman correctement positionnés ; 1918 Az recentré
  (borne ouest 44,7) confirmé côté données.
- ✅ (it. 71, signalement utilisateur) [DATA] 🔴 Trois erreurs de carte
  corrigées : (1) 1914/1915 — frontières internes fantômes du Caucase russe
  → Empire russe fusionné en UN polygone ; (2) 1918 — Azerbaïdjan débordant sur
  le Zanguezour arménien → Arménie moderne soustraite (borne ouest 43,5→44,7) ;
  (3) 1921 — « triangle » anguleux dû au clip sur boîte → remplacement par la
  forme RÉELLE de l'Arménie moderne (idem 1923/1930/1938).
- ✅ (it. 70) [DATA] Notice dédiée 1918 (Sardarabad : 21-29 mai 1918, gén.
  Silikian, batailles simultanées de Bash-Aparan et Karakilissa, proclamation
  de la République le 28 mai, première depuis 1045) en FR+EN+HY, 3 lieux
  situés ; alias 1918→1918. Karabagh neutre vérifié cohérent en 1923 et 2020.
- ✅ (it. 69) [DATA] Notice dédiée 2018 (Révolution de velours : printemps 2018,
  Sargsian PM avorté, marche de Pachinian, démission 23 avril, élection 8 mai,
  transition sans violence) en FR+EN+HY ; alias 2018→2018. Rendu du Karabagh
  neutre vérifié cohérent en 1994 (Stepanakert, pas de débordement).
- ✅ (it. 68, demande utilisateur) [DATA] 🟠 Dépendance geoBoundaries AZE ADM2
  (découpage administratif azerbaïdjanais) SUPPRIMÉE : NKAO et zone de contrôle
  1994 redéfinis en polygones manuels documentés (source neutre), fichier AZE
  effacé. Plus aucune source azerbaïdjanaise dans le projet (REGLES R9 à jour).
- ✅ (it. 67, demande utilisateur) [DATA] 3 années ajoutées pour mieux décrire :
  1918 (Sardarabad, proclamation de la République), 1923 (création du NKAO,
  origine du conflit — notice dédiée FR+EN+HY), 2018 (Révolution de velours) ;
  53 pas de temps, charnières trilingues. Sources auditées : toutes neutres
  (aucune azerbaïdjanaise) ; documentées dans REGLES R9.
- ✅ (it. 66, signalement utilisateur) [DATA] 🔴 Erreurs de carte 1900–1940 :
  (1) 1914/1915 montraient Arménie/Azerbaïdjan/Géorgie indépendantes alors que
  le Caucase était russe → reclassées « Empire russe » (couvre Erevan/Bakou/
  Tbilissi) ; (2) 1921 dessinait une Arménie de Sèvres (17 deg²) déjà soviétisée
  → clippée à la RSS (2,3 deg²). 1938 vérifié OK (l'URSS couvre le Caucase).
- ✅ (it. 65) [DATA] MINI_HY complété : notices 1900 (question arménienne),
  1920 (Première République), 1945 (Arménie soviétique), 2000 (Troisième
  République) traduites en arménien → tout le parcours 1878→2026 est désormais
  lisible en arménien (langue par défaut).
- ✅ (it. 64) [DATA] Notice dédiée 1921 (traité de Kars : 13 oct. 1921,
  frontière turco-arménienne, Kars/Ardahan/Ararat côté turc, Nakhitchevan et
  Karabagh sous tutelle azérie) en FR+EN+HY, lieux situés ; alias 1921→1921.
  Vérifié en ligne (it.63) : MINI_HY déployé, notice 2023 s'affiche en arménien.
- ✅ (it. 63) [DATA] Dictionnaire MINI_HY créé et branché (remplirPanneauPeriode
  sélectionne MINI_HY quand LANG=hy, comme MINI_EN pour l'anglais) : notices
  1915, 1988, 1991, 2020, 2023 désormais en arménien — comble la lacune de la
  langue par défaut.
- ✅ (it. 62) [DATA] Notice dédiée 1915 (génocide : 24 avril, Talaat/Enver/
  Cemal, déportations vers Deir ez-Zor, ~1,5 M de victimes, résistances de Van
  et du Musa Dagh, négationnisme turc) en FR+EN, 3 capitales/lieux situés ;
  alias 1915→1915. Vérifié en ligne : notices 1988/1991/2020/2023 s'affichent.
- ✅ (it. 61) [DATA] Notices dédiées 1988 (séisme de Spitak : 7 déc. 1988,
  M6,8, ~25 000 morts, Spitak rasée, Gyumri/Leninakan ; mouvement du Karabagh,
  Soumgaït) et 1991 (indépendance : référendum 21 sept., Ter-Petrossian,
  guerre du Karabagh, années noires) en FR+EN, capitales situées ; alias
  1988→1988, 1991→1991.
- ✅ (it. 60) [DATA] Notices dédiées pour 2020 (guerre des 44 jours : dates,
  drones, Chouchi 8 nov., cessez-le-feu 10 nov., ~6 500 morts) et 2023 (exode :
  blocus de Latchine, offensive du 19 sept., ~100 000 réfugiés, dissolution de
  l'Artsakh au 1ᵉʳ janv. 2024) en FR + EN, avec capitales situées ; alias
  2020→2020, 2023→2023.
- ✅ (it. 59) [UX] 🟡 Vérifié en Chrome à 390×720 (type iPhone) : légende
  bornée (280 px large, 388→574 px, aucun débordement), 6 entrées lisibles en
  arménien dont « aire maximale (300) », contour du foyer visible. Couverture
  arménienne complète de −500 à 2026 confirmée (aucune année sans entité).
- ✅ (it. 58) [UX/DATA] 🟡 Légende : largeur max (retour à la ligne) +
  hauteur max avec défilement de sécurité (pas de débordement iPhone) ; le
  foyer arménien est précisé comme « aire maximale (an 300) » en 4 langues.
- ✅ (it. 57) [UX] 🟡 Couche « foyer arménien » inexpliquée → entrée de légende
  dédiée (pictogramme pointillé or + libellé 4 langues via T("presence")).
- ✅ (it. 56, demande utilisateur) [DATA/UX] Couche « foyer arménien historique »
  (plateau + Cilicie, aire maximale sourcée = Arménie an 300 ∪ Cilicie) :
  contour pointillé or permanent, activable à la demande (bouton ֍, R11),
  distinct des entités politiques. Vérifié en ligne (VDATA b) : s'affiche à
  travers les siècles, langue arménienne par défaut confirmée, carte 1938
  corrigée (2 deg²), nouvelles années présentes.
- ✅ (it. 55, demandes utilisateur) [DATA] XXe–XXIe siècles densifiés : ajout
  des années 1915 (génocide), 1921 (Kars), 1988 (Spitak), 1991 (indépendance),
  2020 (guerre 44 j.), 2023 (exode d'Artsakh), 2026 (aujourd'hui) — 50 pas de
  temps ; charnières FR/EN/HY, surcouches arméniennes, notices aliasées.
- ✅ (it. 55, signalement utilisateur) [DATA] 🔴 Carte 1930/1938 : la source
  dessinait une « Grande Arménie » anachronique (17 deg², Anatolie orientale
  comprise) → clippée à la RSS réelle (2,3 deg²) dans build_globe_data.py.
- ✅ (it. 55, question utilisateur) [DATA] Atropatène : vérifié — présentée
  uniquement comme conquête de Tigrane II (correct) ; c'était un royaume
  distinct de Médie, pas une province arménienne. Contenu exact, rien à changer.
- ✅ (it. 55, demande utilisateur) [UX] Langue par défaut = arménien (hy) au
  premier atterrissage (le choix reste mémorisé ensuite).
- ✅ (it. 54) [PERF/A11Y] 🟡 Audit objectif du site publié : DOMContentLoaded
  286 ms, amorce 43 Ko/100 ms, complet 2,28 Mo gzip/80 ms, 0 erreur page,
  canvas focusable+aria OK, aria-live OK, tous les boutons nommés. Ligne de
  base de performance documentée dans README ; le poids brut 6,6 Mo n'est plus
  un problème (2,28 Mo gzip) → pas de re-découpage nécessaire.
- ✅ (it. 53) [A11Y] 🟡 Canvas sans focus visible net sur fond sombre →
  liseré intérieur doré (box-shadow inset) au focus clavier, l'outline externe
  étant invisible sur un canvas plein écran.
- ✅ (it. 52) [A11Y] 🟡 Canvas non focusable / aria-label figé → tabindex=0 +
  aria-label instructif traduit (canvasAria, 4 langues, mis à jour au
  changement de langue) ; la navigation temporelle au clavier (←→) existait
  déjà globalement.
- ✅ (it. 51) [A11Y] 🟡 Canvas sans alternative textuelle → role=img +
  aria-label, et région aria-live annonçant « <année> — <événement> » à
  chaque changement de siècle (classe .sr-only ajoutée).
- ✅ (it. 50) [UX] 🟡 Lien partagé ?an= appliqué seulement après chargement
  complet → l'écran de chargement annonce désormais la destination
  (« → 1920 ») pour que l'utilisateur en 4G sache où il va atterrir.
- ✅ (it. 49) [A11Y] 🟡 Menu langue navigable au clavier : rôles ARIA
  menu/menuitem, flèches ↑↓ pour circuler, Entrée pour choisir, Échap pour
  fermer, focus posé sur la langue active à l'ouverture et rendu au bouton
  à la fermeture.
- ✅ (it. 48) [UX] 🟡 Pause de lecture auto invisible sur les siècles
  majeurs → l'année pulse en or (animation 1,2 s) pendant la pause double,
  signalant un temps d'arrêt volontaire et non un blocage.
- ✅ (it. 47) [UX] 🟡 Bouton langue cyclique opaque → menu déroulant montrant
  les 4 choix (code · nom natif), langue active en or, ouvert à la demande
  et refermé au clic extérieur (R11).
- ✅ (it. 46) [UX] 🟡 Quiz carte : après une mauvaise réponse, le bon
  territoire est surligné 1,5 s sur le globe avant l'affichage du verdict.
- ✅ (it. 45) 🟡×3 : texte de chargement traduit dès l'init de la langue ;
  version des données affichée au bas de la légende (visible à la demande,
  R11) ; seuil des surcouches lu depuis SPECS au lieu de 37 en dur.
- ✅ (it. 44) 🟡×2 : dates hy harmonisées (suppression du « թթ. » isolé) ;
  texte de progression du chargement traduit en 4 langues (chargeTxt).
  Vérifié en ligne : ?an=1920 saute bien à 1920 (VDATA p).
- ✅ (it. 43) [UX/DATA] 🟡×3 : lien de partage avec ?an=<année> + saut à
  l'année au chargement ; bouton quiz verrouillé pendant la phase 2 ;
  état de la légende mémorisé (localStorage).
- ✅ (it. 42) [UX] 🟠 Test navigateur réel (Chrome/site publié) : amorce
  rendue, slider débloqué, 43 années, badge retiré, 0 erreur console ;
  vue 1994 vérifiée visuellement (zone Karabagh pointillée, Stepanakert,
  lacs Van/Sevan/Ourmia réels). Test iPhone réel rétrogradé 🔴→🟠.
- ✅ (it. 41) [DATA/PERF] 🟠 JSON monolithique → analyse : gzip de Pages
  ramène déjà le transfert à 2,26 Mo ; ajout d'une amorce
  globe_data_init.json (124 Ko, année -700) : le globe s'affiche
  immédiatement, le fichier complet se charge en arrière-plan (badge de
  progression discret, slider verrouillé puis débloqué).
- ✅ (it. 40) [UX] 🟠 Pas de bouton partager → bouton flottant ↗ : feuille
  de partage native iOS/Android (navigator.share), copie du lien en repli
  desktop, libellés 4 langues ; [DATA] 🟡 lacs.json contrôlé par
  verifie_donnees.py (16 lacs, anneaux, bornes).
- ✅ (it. 39) [DATA] 🟠 Lacs-ellipses approximatifs → tracés réels Natural
  Earth 50m (build_lacs.py → lacs.json, 11 Ko, 16 lacs dont Van/Sevan/Ourmia),
  chargés au démarrage avec repli sur les ellipses.
- ✅ (it. 38) [DATA] 🟡 1994 : la surcouche représente désormais la ligne de
  contact réelle — NKAO + 7 districts occupés (geoBoundaries), aire 1,2 deg²
  (~12 000 km²), nom et traductions (en/hy/ru) mis à jour.
- ✅ (it. 37) [DATA] 🔴 Polygone NKAO à main levée → tracé documenté
  geoBoundaries (gbOpen AZE ADM2, commit épinglé) : union Khankendi, Khojaly,
  Choucha ville+district, Khojavend + partie montagneuse de Tartar
  (Mardakert) ; aire ≈ 4 000 km² vs 4 400 km² officiels.
- ✅ (it. 36) [DATA] 🟠 niveau() par mots-clés anglais → table de surcharges
  NIVEAU_FIXE (USSR, Persia kadjare, Ottoman Sultanate, Russia, China,
  United States, Chagatai Khanate → empires ; Siberians, Khoiasan,
  Cuman-Kipchak → peuples), constituée par scan des grandes entités sans
  mot-clé du dataset.
- ✅ (it. 35) [UX] 🟠 Panneau dense sans hiérarchie → séparateur horizontal +
  libellé de section « Notice de la période » (4 langues) entre la fiche
  territoire cliquée et la notice, y compris pour les mini-notices.
- ✅ (it. 34) [UX] 🟠 Pas d'échappatoire sur les questions carte → bouton
  « Passer » dans le bandeau (compte faux, révèle la bonne réponse), 4 langues.
- ✅ (it. 33) [UX] 🟠 Le quiz n'utilisait pas la carte → nouveau type de
  question « Trouvez sur la carte : X (année) » : le voile se ferme, le globe
  saute à l'année, bandeau « Touchez : X », clic intercepté et validé ;
  libellés en 4 langues.
- ✅ (it. 32) [DATA] 🟠 Boîte rectangulaire « Transcaucasie russe » →
  polygone suivant la frontière russo-ottomane de 1878 (Ardahan–Kars–Ararat)
  puis l'Araxe (Nakhitchevan, Zanguezour) ; l'Arménie occidentale 1880/1900/
  1914 suit désormais la même ligne par différence.
- ✅ (it. 31) [DATA] 🔴 Gabarit unique « an 300 » pour toutes les époques →
  mécanisme armenia:<année> : satrapie −500 sur Armenia(−300), Artaxiades −100
  sur Armenia(−1), Ilkhanat 1300 sur Armenia(1200), Bagratides 900 et RSS
  1945/60 déjà sur leurs années propres ; gabarit conservé (et justifié en
  commentaire) pour l'ostikanat 800 et les périodes sans tracé proche.
- ✅ (it. 30) [DATA] 🟠 Relecture des traductions hy (it. 26) → 8 corrections
  (կառավարում, Օմայյան, Ղաջարական, Չալդրան, Սեն-Դենի, լեռնաշխարհ×3),
  terminologie alignée sur les notices d'origine.
- ✅ (it. 29) [UX] 🟠 Année tactile invisible → chevron ⌄/⌃ sous l'année sur
  mobile ; [DATA] 🟡 aria-labels des toggles (année, 🗺) traduits en 4 langues
  via applyLang. L'événement charnière reste accessible d'un toucher (28-🟡
  couverte par le chevron).
- ✅ (it. 28) [UX] 🟠 Bandeau-titre imposant sur iPhone → R11 appliqué :
  sur mobile seule l'année reste affichée en haut ; toucher l'année
  déplie/replie titre, sous-titre et événement charnière.
- ✅ (it. 27) [UX] 🔴 (décision utilisateur, capture iPhone) La légende
  occupait la moitié de l'écran mobile → repliée par défaut, bouton 🗺 pour
  l'afficher ; règle générale R11 « affichage à la demande » ajoutée à
  REGLES.md (amendement de R8 « légende permanente » par l'utilisateur).
- ✅ (it. 26) [DATA] 🔴 7 notices sur 10 manquaient en arménien
  (periodes_hy.json[3..9] = null) → traduites (Artaxiades → partages
  ottomano-persans), verifie_donnees.py repasse à 0 avertissement.
- ✅ (it. 25) [DATA] 🟠 verifie_donnees.py ne contrôlait pas les periodes*.json
  → alignement des 3 langues, champs essentiels, capitales bornées ; a
  immédiatement révélé les 7 notices hy manquantes.
- ✅ (it. 24) [DATA] 🟠 Aucun test automatisé de cohérence → verifie_donnees.py
  (années triées, anneaux fermés ≥4 pts, coordonnées bornées, 37 surcouches,
  présence d'Armenia aux périodes clés) ; à lancer avant chaque push.
- ✅ (it. 23) [UX] 🟠 Chargement des 6,6 Mo sans indicateur de progression
  → téléchargement en streaming avec % et Mo reçus affichés sous l'anneau.
- ✅ (it. 22) [DATA] 🔴 Boîtes rectangulaires des surcouches modernes → RSS
  d'Arménie 1945/1960 découpée sur la géométrie réelle « Armenia » (an 2000),
  Haut-Karabagh en polygone NKAO (la Transcaucasie russe reste ouverte, cf. 🟠).
- ✅ (it. 21) [UX] 🔴 Le bouton de langue était masqué par le volet PC ouvert
  → décalage des boutons flottants.
- ✅ (it. 21) [DATA] 🔴 Les lacs disparaissaient selon les siècles (trous
  absents du dataset) → couche permanente de 18 grands lacs, dont Van, Sevan,
  Ourmia (lacs arméniens historiques).
