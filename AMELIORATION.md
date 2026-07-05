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
