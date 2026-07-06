# Globe historique — 12 000 ans (pivot : histoire de l'Arménie)

Outil d'apprentissage de l'histoire : un globe 3D feuilletable de la préhistoire à nos jours
(−10 000 → 2010, 43 pas de temps, cadence resserrée à l'époque contemporaine),
multilingue (FR/EN/HY/RU) et un atlas Leaflet de l'Arménie historique.

## Contenu

| Fichier | Rôle |
|---|---|
| `globe.html` | Globe D3 orthographique (canvas) : rotation, zoom, clic d'identification, frise, lecture auto, notices, surcouches arméniennes |
| `atlas_armenie_historique.html` | Atlas Leaflet des 10 périodes de l'Arménie historique (autonome) |
| `globe_data.json` | Frontières mondiales par siècle (dérivées de historical-basemaps, simplifiées) + surcouches arméniennes `"o":1` |
| `periodes.json` | Notices détaillées des 10 périodes arméniennes (texte FR, capitales) |
| `traductions_fr.json` | Dictionnaire EN→FR (~700 libellés d'États et cultures) |
| `build_globe_data.py` | Régénère `globe_data.json` depuis la source (shapely requis) |
| `build_armenie_overlays.py` | Injecte les surcouches arméniennes reconstituées (à lancer APRÈS build_globe_data) |
| `AMELIORATION.md` | Journal d'autoamélioration (questions/réponses par itération) |
| `REGLES.md` | Spécification des règles implémentées (niveaux, couleurs, surcouches, i18n…) |

Source cartographique : [aourednik/historical-basemaps](https://github.com/aourednik/historical-basemaps)
(numérisation d'atlas historiques — précision variable ; les écarts corrigés sont
documentés dans `AMELIORATION.md`).

## Lancement local

`globe.html` charge ses données par `fetch()` : il faut un serveur HTTP.

```bash
python -m http.server 8000
# puis ouvrir http://localhost:8000/globe.html
```

L'atlas (`atlas_armenie_historique.html`) est autonome : double-clic suffit.

## Régénération des données

```bash
pip install shapely
python build_globe_data.py        # télécharge la source dans ./geo/ et reconstruit
python build_armenie_overlays.py  # réinjecte les 22 surcouches arméniennes
```

## Déploiement GitHub Pages (procédure — ne pas exécuter sans accord)

1. Créer le dépôt GitHub (ex. `amsolutions-pro/globe-armenie` ou le dépôt
   `amsolutions-pro.github.io` pour la racine).
2. `git remote add origin <url> && git push -u origin main`
3. Sur GitHub : *Settings → Pages → Deploy from branch → main / (root)*.
4. L'URL sera `https://amsolutions-pro.github.io/globe-armenie/globe.html`
   (le fetch des JSON fonctionne tel quel, chemins relatifs).

## Performance (ligne de base mesurée, it. 54)

Mesures sur le site publié (Chrome desktop, cache vide) :

| Ressource | Transfert (gzip) | Durée |
|---|---|---|
| `globe_data_init.json` (amorce, année −700) | 43 Ko | ~100 ms |
| `globe_data.json` (complet, 6,6 Mo brut) | 2,28 Mo | ~80 ms |
| notices + lacs + traductions | ~40 Ko | ~100 ms |
| **DOMContentLoaded** | — | **286 ms** |

Chargement en deux phases : l'amorce (`globe_data_init.json`) affiche le globe
en < 300 ms, puis `globe_data.json` complet se charge en arrière-plan (barre de
progression, slider verrouillé jusqu'au déblocage). GitHub Pages sert tout en
gzip. **Conclusion : le poids brut de 6,6 Mo n'est plus un problème de
chargement** — inutile de re-découper le JSON tant que ces chiffres tiennent.
