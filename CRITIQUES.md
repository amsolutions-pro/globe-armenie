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
- 🔴 **Les surcouches modernes utilisent des boîtes rectangulaires** (RSS
  d'Arménie, Haut-Karabagh, Transcaucasie russe) : bords droits visibles au zoom.
  Il faudrait des tracés réels (Natural Earth admin-0 Armenia pour la RSS,
  tracé de la ligne de contact 1994).
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

---

## Critiques traitées
- ✅ (it. 21) [UX] 🔴 Le bouton de langue était masqué par le volet PC ouvert
  → décalage des boutons flottants.
- ✅ (it. 21) [DATA] 🔴 Les lacs disparaissaient selon les siècles (trous
  absents du dataset) → couche permanente de 18 grands lacs, dont Van, Sevan,
  Ourmia (lacs arméniens historiques).
