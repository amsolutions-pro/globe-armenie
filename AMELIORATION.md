# Journal d'autoamélioration — Globe & Atlas d'histoire (pivot : Arménie)

Chaque itération : 3 questions « est-ce assez bien, et comment faire mieux ? »,
les réponses sont appliquées à l'itération suivante (ou immédiatement si possible).

---

## Itération 1 — 2026-07-05

**Q1. Les libellés sont-ils vraiment francisés, ou seulement les plus connus ?**
Mesure : 1 473 noms uniques dans `globe_data.json`, seulement 168 couverts (11 %).
→ **Réponse appliquée** : création de `traductions_fr.json` (~700 entrées : cultures
préhistoriques, royaumes indiens/africains/asiatiques, peuples amérindiens, pays
modernes, coquilles de la source corrigées — « Cimerians », « Nothumbria »…).
Les ethnonymes propres (peuples aborigènes d'Australie, etc.) restent tels quels,
c'est correct. Chargé par fetch et fusionné au dictionnaire embarqué.

**Q2. Les entités arméniennes sont-elles toutes reconnues (dorées, seuil d'étiquette abaissé) ?**
Non : en 1100, les données contiennent **Syunik, Tashir, Artsakh** — non détectés par
la regex `armen|urartu`.
→ **Réponse appliquée** : regex étendue à `syunik|artsakh|tashir|hayasa` + traductions
FR explicites (« Syunik (principauté arménienne) », etc.).

**Q3. Le globe raconte-t-il l'Arménie à CHAQUE siècle, comme l'exige le pivot ?**
Non. Audit (arm_check.txt) : aucune entité arménienne aux siècles **−500, −100,
400–600, 800–900, 1300–1900**. L'atlas résolvait cela par intersections shapely
(satrapie Armina, Persarménie, ostikanat, Cilicie…) ; le globe utilise les données
brutes.
→ **Réponse pour l'itération 2** : étendre `build_globe_data.py` pour injecter des
surcouches arméniennes dérivées (mêmes intersections que l'atlas, adaptées aux
millésimes du globe : Armina −500 = Arménie(−300)∩Achéménide(−500) ; Artaxiades −100 ;
Persarménie/Arménie byzantine 400–600 ; Arminiya 800 ; Bagratides 900 ; Cilicie
1300 ; vilayets/khanats 1400–1800 ; Arménie russe 1900), régénérer `globe_data.json`.

### Constats en réserve (à traiter dans les itérations suivantes)
- « Urartu » présent dès −1500/−1000 dans la source : anachronisme (royaume ~860 av.
  J.-C.) — envisager de renommer la couche −1500/−1000 en « Hayasa / proto-arméniens »
  ou d'annoter la notice.
- Notices manquantes pour −2000…−1000, 1400, 1900, 2000 (mini-notices à rédiger).
- 1 225 entités sans nom (« Terres non revendiquées ») — vérifier leur rendu.
- Anti-collision des étiquettes : les petits États arméniens de 1100 (Syunik…)
  risquent d'être masqués par « Arménie » byzantine — à vérifier visuellement.

---

## Itération 2 — 2026-07-05

**Fait** : `build_armenie_overlays.py` — 20 surcouches arméniennes dérivées par
intersections shapely, injectées dans `globe_data.json` (champ `"o":1`, dessinées
au-dessus, or translucide + liseré pointillé doré, étiquette prioritaire). L'Arménie
est désormais visible et nommée à CHAQUE pas de temps de −1500 à 2000. Script
rejouable (purge avant réinjection). Vérifié dans Chrome (500 : Persarménie +
Arménie byzantine ; 1300 : Cilicie + Arménie ilkhanide).

Découverte de justesse : le jeu de données diverge de l'histoire attendue —
1500 : plateau sous Ak Koyunlu (pas Séfévides) ; 1600–1700 : tout ottoman (pas de
partage de Zuhab) ; 1900 : Erevan sous « Perse » (pas la Russie !). Les surcouches
suivent les polygones du dataset mais les libellés ont été adaptés (1900 est
étiqueté « Arménie orientale (russe) » — voir Q6).

**Q4. La Cilicie dérivée est-elle géographiquement juste ?**
Non : découpée par une boîte rectangulaire (bords droits visibles au nord, déborde
sur l'intérieur seldjoukide au lieu de s'arrêter aux monts Taurus).
→ **Réponse pour l'itération 3** : remplacer la boîte par un polygone dessiné suivant
la crête du Taurus.

**Q5. Les surcouches expliquent-elles leur nature (frontières reconstituées) ?**
Non : l'infobulle les présente comme n'importe quel État.
→ **Réponse pour l'itération 3** : ajouter dans l'infobulle et le panneau la mention
« Frontières reconstituées (intersection de cartes historiques) » quand `f.o`.

**Q6. Que faire quand le dataset contredit l'histoire (Zuhab 1639, Turkmentchaï 1828) ?**
Le dataset donne tout le plateau aux Ottomans en 1600–1700 et Erevan à la Perse en 1900.
→ **Réponse pour l'itération 3** : scinder les surcouches 1600/1700 par une ligne
approximative de la paix de Zuhab (méridien ~44,5°E infléchi vers l'Araxe), et pour
1900 forcer la limite russe au sud d'Erevan (frontière de l'Araxe, Turkmentchaï) —
en documentant l'écart à la source dans ce journal.

---

## Itération 3 — 2026-07-05

**Fait** (réponses à Q4–Q6) : Cilicie découpée par un polygone suivant la crête du
Taurus (7,1 deg², plus de bords rectangulaires au nord) ; mention « Frontières
reconstituées (intersection de cartes historiques) » dans l'infobulle et le panneau
pour toute surcouche `o:1` ; surcouches 1600/1700 scindées selon la paix de Zuhab
(frontière Arpatchaï–Araxe ~43,7°E : Arménie occidentale ottomane / orientale
persane) ; 1900 corrigé : « Arménie russe (gouvernorats d'Erevan et de Kars) » au
nord-est (boîte Transcaucasie 42,5–47,5°E / 38,8–41,8°N, conforme à Turkmentchaï
1828 + Berlin 1878), Arménie ottomane amputée de Kars. **Écart au dataset documenté** :
la source aourednik donne tout le plateau aux Ottomans en 1600–1700 et Erevan à la
Perse en 1900 ; nos surcouches corrigent d'après les traités. Vérifié dans Chrome (1700).

**Q7. Les siècles sans notice (−2000…−1000, 1400, 1900, 2000) privent-ils l'apprenant de contexte ?**
Oui : le panneau affiche « pas de notice détaillée ».
→ **Réponse pour l'itération 4** : rédiger des mini-notices embarquées dans globe.html
(Hayasa/proto-arméniens −2000…−1000 ; Kara/Ak Koyunlu 1400 ; veille du génocide et
question arménienne 1900 ; 3ᵉ République + Artsakh 2000), même gabarit que periodes.json.

**Q8. La navigation temporelle est-elle un outil d'apprentissage ou un simple slider ?**
Un simple slider : rien n'incite à observer l'évolution.
→ **Réponse pour l'itération 4** : bouton « lecture » (▶ animé) qui avance d'un siècle
toutes les 2,5 s avec pause au toucher, pour « feuilleter » les 4 millénaires.

**Q9. L'apprenant sait-il ce que signifient l'or plein (États du dataset) et l'or pointillé (reconstitutions) ?**
Non, aucune légende.
→ **Réponse pour l'itération 4** : mini-légende discrète (coin bas-gauche) : or plein =
État arménien attesté dans la source, or pointillé = présence arménienne reconstituée.

---

## Itération 4 — 2026-07-05

**Fait** (réponses à Q7–Q9) : 6 mini-notices embarquées dans globe.html (−2000 aube
du plateau, −1500 Hayasa-Azzi/Nairi — avec avertissement d'anachronisme de la source
sur « Ourartou », −1000 unification ourartéenne, 1400 Timour et les Turkmènes +
restauration d'Etchmiadzin 1441, 1900 question arménienne et veille du génocide,
2000 Troisième République et Artsakh) ; bouton lecture ⏵/⏸ (1 siècle / 2,5 s, arrêt
au toucher du globe, du slider ou des flèches) ; légende bas-gauche (or plein =
Arménie attestée, pointillé = présence reconstituée). Vérifié dans Chrome.

**Q10. Le clic sur une capitale de notice fonctionne-t-il aussi pour les mini-notices ?**
Non : les mini-notices n'ont pas de capitales cliquables, alors qu'Erevan (1900, 2000),
Tabriz (1400) ou Tushpa (−1000) seraient pédagogiques.
→ **Réponse pour l'itération 5** : ajouter un champ `capitales` aux mini-notices
(réutiliser le rendu existant).

**Q11. Un élève comprend-il POURQUOI la carte change entre deux siècles ?**
Non : le saut est brutal, sans transition ni explication de l'événement charnière.
→ **Réponse pour l'itération 5** : afficher sous l'année un bandeau d'une ligne
« événement charnière » (ex. 1045→1100 : « chute d'Ani (1045), Manzikert (1071) »)
tiré d'un petit dictionnaire embarqué des transitions siècle→siècle côté Arménie.

**Q12. Le projet est-il consultable ailleurs que sur ce poste (iPhone de l'utilisateur) ?**
Non : servi seulement en localhost.
→ **Réponse pour l'itération 5+** : préparer le déploiement GitHub Pages
(amsolutions-pro.github.io) — nécessite l'accord explicite de l'utilisateur pour
publier ; en attendant, tout committer proprement et documenter la procédure dans
un README.

---

## Itération 5 — 2026-07-06

**Fait** (réponses à Q10–Q12) : capitales/lieux clés cliquables ajoutés aux 6
mini-notices (Metsamor, Kummaha, Tushpa+Arzashkun, Etchmiadzin+Tabriz,
Erevan+Kars+Van, Erevan+Stepanakert — vol animé vers le lieu au clic) ; bandeau
« événement charnière » sous l'année (28 entrées, d'« Arame unifie le Nairi » à
« exode d'Artsakh 2023 ») ; README.md avec lancement local, régénération des données
et procédure GitHub Pages (non exécutée — accord utilisateur requis pour publier).
Vérifié dans Chrome (1100 : bandeau Ani/Manzikert, légende, Arménie dorée).

**Q13. L'outil relie-t-il le globe (vue monde) et l'atlas (vue détaillée) ?**
Non : deux fichiers sans lien entre eux, l'apprenant ne découvre pas l'atlas.
→ **Réponse pour l'itération 6** : dans le panneau du globe, quand une période
arménienne est affichée, bouton « Ouvrir l'atlas détaillé de cette période » →
atlas_armenie_historique.html (même dossier).

**Q14. Le rendu est-il fluide sur iPhone (cible déclarée) ?**
Risque : render() complet à chaque pointermove (200+ tracés canvas), sans limitation.
→ **Réponse pour l'itération 6** : regrouper les rendus dans requestAnimationFrame
(un seul render par frame même si plusieurs événements pointeur).

**Q15. L'outil est-il accessible (clavier, lecteurs d'écran, mouvement réduit) ?**
Partiel : flèches clavier OK, mais boutons sans aria-pressed, pas de focus visible,
lecture auto ignore prefers-reduced-motion.
→ **Réponse pour l'itération 6** : styles :focus-visible, aria-label complétés,
désactiver l'auto-lecture si prefers-reduced-motion.

---

## Itération 6 — 2026-07-06 (+ directives utilisateur)

**Fait (Q13–Q15)** : bouton « Ouvrir l'atlas détaillé » dans le panneau des périodes
arméniennes ; render() regroupé dans requestAnimationFrame (drag/pincement/molette) ;
accessibilité (:focus-visible or, prefers-reduced-motion ⇒ pas d'auto-lecture).

**Directives utilisateur intégrées** (« travaille mieux les couleurs et les noms,
accentue les États par rapport aux tribus et peuplements, situe les villes ») :
1. **Couleurs** : palette curatée de 24 teintes riches pour les **États constitués**
   (frontières nettes, alpha .95) ; **tribus/peuplements/cultures** détectés par
   classifieur (regex chasseurs/nomades/cultures/ethnonymes courts non traduits) et
   rendus en tons éteints gris-brun (sat 7–14 %) avec liseré à peine visible — les
   États ressortent immédiatement.
2. **Noms** : étiquettes d'États en 500, plus contrastées ; tribus en italique
   maigre, plus petites, seuil d'affichage 3× plus haut (300 vs 110).
3. **Villes principales** : 56 villes historiques datées (de/à) avec point + nom,
   seuil de zoom par importance, anti-collision partagé avec les étiquettes d'États ;
   12 villes arméniennes (Erebouni, Tushpa, Armavir, Artashat, Tigranakert, Dvin,
   Ani, Kars, Sis, Etchmiadzin, Van, Stepanakert) en or clair, visibles plus tôt.
4. Légende enrichie (État constitué / peuplement / ville).
Vérifié dans Chrome (−100 : Artaxiades + Rome/Athènes/Damas/Erevan/Tushpa).

**Q16. Les périodes de la ville sont-elles justes (Byzance→Constantinople→Istanbul) ?**
Traité pour Constantinople ; vérifier les autres renommages (Edo→Tokyo fait,
Tenochtitlan→Mexico fait). → Itération 7 : relire les dates des 56 villes.

**Q17. Le classifieur tribu/État se trompe-t-il sur des cas importants ?**
Risque : ethnonymes d'États réels courts (ex. « Chola », « Saba ») sont dans FR/FRX
donc protégés, mais à auditer. → Itération 7 : échantillonner 30 noms classés tribu
et corriger les faux positifs (liste blanche).

**Q18. Les villes arméniennes disparues (Ani après 1319) racontent-elles leur fin ?**
Non : le point disparaît sans explication. → Itération 7 : au clic sur une ville,
mini-fiche (fondation, apogée, fin) dans l'infobulle.

---
