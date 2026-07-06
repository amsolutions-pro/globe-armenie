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
- 🟠 [DATA] **Aucun test automatisé de cohérence des données** (années triées,
  polygones fermés, surcouches présentes aux 37 pas attendus) — un script
  `verifie_donnees.py` lancé avant chaque push éviterait les régressions.
- 🟡 [UX] Le texte de progression n'est pas traduit (français en dur) alors
  que l'interface est quadrilingue.

## Critiques traitées
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
