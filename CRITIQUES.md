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
- 🟠 **La zone Transcaucasie russe (1880/1900) reste une boîte rectangulaire**
  (reliquat it. 22 : RSS et Karabagh sont désormais en tracés réels, pas ce
  masque) ; un tracé des gouvernorats d'Erevan et de Kars serait plus juste.
- 🔴 **Le gabarit unique « Arménie an 300 » sert à toutes les époques** : la
  satrapie de −500 ou l'ostikanat de 800 n'avaient pas exactement cette
  emprise ; chaque surcouche mériterait son propre masque documenté.
- 🟠 **Le classement niveau() repose sur le nom anglais** : des États sans
  mot-clé (« Persia », « Wu ») restent N3 quand certains furent des empires ;
  inversement « Empire of Ghana » à son déclin reste N4. Un tableau
  (entité, période) → niveau serait plus juste.
- 🟠 **Les lacs-ellipses sont approximatifs** (Caspienne surtout) et peuvent
  jurer avec les trous réels du dataset à fort zoom.
- 🟡 Les dates des villes (de/à) n'ont pas été systématiquement sourcées.

### [UX]
- 🔴 **Aucun retour visuel pendant le drag sur mobile bas de gamme** : pas
  testé sur iPhone réel (cible déclarée !) — tester Safari iOS dès que possible.
- 🟠 **Le panneau des périodes est dense** : pas de hiérarchie visuelle entre
  fiche territoire et notice de période quand les deux s'empilent ; un
  séparateur/onglets aideraient.
- 🟠 **Le quiz n'utilise pas la carte** : des questions « montrez où… »
  (cliquer le territoire) seraient bien plus pédagogiques.
- 🟡 La lecture auto ne montre pas visuellement la pause sur les siècles
  majeurs (l'utilisateur croit à un blocage).
- 🟡 Le bouton 🌐 cycle sans montrer les 4 choix — un petit menu serait plus clair.

### Nouvelles critiques (it. 22)
- 🔴 [DATA] **Le polygone NKAO du Karabagh est dessiné à main levée** (8 points
  approximatifs) : mieux qu'une boîte, mais pas sourcé — le comparer à un tracé
  documenté de l'oblast autonome (1923–1991) ou de la ligne de contact 1994.
- 🟠 [DATA/PERF] **Le JSON reste monolithique (6,6 Mo)** : un découpage par
  tranches d'époques réduirait le temps d'affichage initial sur mobile.
- 🟡 [DATA] La géométrie « Armenia an 2000 » utilisée pour la RSS 1945/1960
  ignore les micro-différences de frontières soviétiques (enclaves
  Artsvashen/Karki non représentées).

---

### Nouvelles critiques (it. 23)
- 🟠 [UX] **Pas de bouton « partager / copier le lien »** : l'URL publique
  existe mais rien dans l'interface ne la mentionne ni ne facilite le partage.
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

### Nouvelles critiques (it. 26)
- 🟠 [DATA] **Les traductions hy fraîchement écrites n'ont pas été relues par
  un regard indépendant** : orthographe arménienne orientale et terminologie
  historique à faire relire (agent ou locuteur).
- 🟡 [DATA] Les notices hy n'ont pas de champ `provinces` (comme en) : au
  clic sur une province, le libellé retombe en français.
- 🟡 [UX] Aucune indication dans l'UI que la notice affichée est une
  traduction (vs texte original français).

## Critiques traitées
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
