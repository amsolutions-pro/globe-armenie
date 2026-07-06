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
- 🟠 **Pas encore testé sur iPhone réel** (Safari iOS) — le test Chrome
  desktop est passé (it. 42), reste la validation tactile sur l'appareil cible.
- 🟡 La lecture auto ne montre pas visuellement la pause sur les siècles
  majeurs (l'utilisateur croit à un blocage).
- 🟡 Le bouton 🌐 cycle sans montrer les 4 choix — un petit menu serait plus clair.

### Nouvelles critiques (it. 22)
- 🟡 [DATA] La géométrie « Armenia an 2000 » utilisée pour la RSS 1945/1960
  ignore les micro-différences de frontières soviétiques (enclaves
  Artsvashen/Karki non représentées).

---

### Nouvelles critiques (it. 23)
- 🟡 [UX] Le texte de progression n'est pas traduit (français en dur) alors
  que l'interface est quadrilingue.

### Nouvelles critiques (it. 24)
- 🟠 [DATA] **verifie_donnees.py ne contrôle pas les périodes JSON annexes**
  (periodes*.json : chaque année du slider devrait avoir sa notice dans les
  3 langues ; les trous passent inaperçus).
- 🟡 [UX] **Rien n'indique la version des données sur le site** : afficher
  discrètement VDATA/date du build aiderait à vérifier qu'on voit bien la
  dernière version depuis l'iPhone.
- 🟡 [DATA] Le seuil « 37 surcouches » est codé en dur dans verifie_donnees.py :
  à synchroniser automatiquement avec SPECS de build_armenie_overlays.py.

### Nouvelles critiques (it. 25)
- 🟡 [DATA] La correspondance année→notice (indexPeriode + MINI) vit dans
  globe.html et n'est pas contrôlée par verifie_donnees.py : un siècle sans
  notice passerait inaperçu.
- 🟡 [UX] Les avertissements de verifie_donnees.py ne sont visibles que du
  développeur : aucun signal côté site quand une traduction manque.

- 🟡 [DATA] Les notices hy n'ont pas de champ `provinces` (comme en) : au
  clic sur une province, le libellé retombe en français.
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
- 🟡 [UX] Les dates des notices hy mélangent « Ք.ա. 189 – 1 » et « 66 – 428 թթ. » :
  harmoniser le format des ères sur les 10 notices.
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
- 🟡 [UX] La question carte ne surligne pas le bon territoire après une
  mauvaise réponse (le texte le nomme, mais un flash visuel aiderait).
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
- 🟡 [DATA] Fizouli et Agdam sont inclus en entier dans la zone 1994 alors
  qu'ils n'étaient occupés que partiellement (~1/3 d'Agdam) : surestimation
  à l'est, documentée mais améliorable.
- 🟡 [DATA] La surcouche 2010 devrait différer de 1994 (ajustements mineurs
  de la ligne de contact) — actuellement identiques.
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
- 🟡 [UX] Le paramètre ?an= n'est appliqué qu'après le chargement complet :
  sur 4G, l'utilisateur voit -700 quelques secondes avant de sauter à
  l'année partagée (afficher une note ou charger cette année dans l'amorce).
- 🟡 [UX] Aucun retour visuel si l'an du lien est invalide (silencieusement
  ignoré).
- 🟡 [DATA] localStorage peut être indisponible (navigation privée iOS) :
  try/catch posés, mais non testés.

## Critiques traitées
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
