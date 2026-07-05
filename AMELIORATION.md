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
