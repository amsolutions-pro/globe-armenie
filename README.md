# Globe historique — 12 000 ans (pivot : histoire de l'Arménie)

Outil d'apprentissage de l'histoire : un globe 3D feuilletable de la préhistoire à nos jours
(−10 000 → 2026, **53 pas de temps**, cadence resserrée à l'époque contemporaine avec les
grandes dates arméniennes : génocide 1915, Sardarabad 1918, indépendance 1991, guerre 2020,
exode d'Artsakh 2023…), multilingue (FR/EN/HY/RU, **arménien par défaut**) et un atlas
Leaflet de l'Arménie historique.

**77 villes et lieux** arméniens (capitales historiques, monastères UNESCO, hauts lieux de
mémoire), une **couche « foyer arménien historique »** (plateau + Cilicie) activable, et une
note **« Sources & méthodologie »** intégrée. En ligne :
<https://amsolutions-pro.github.io/globe-armenie/globe.html>

## Contenu

| Fichier | Rôle |
|---|---|
| `globe.html` | Globe D3 orthographique (canvas) : rotation, zoom, clic d'identification, frise, lecture auto, notices, surcouches arméniennes |
| `atlas_armenie_historique.html` | Atlas Leaflet des 10 périodes de l'Arménie historique (autonome) |
| `globe_data.json` (+ `globe_data_init.json`) | Frontières mondiales par pas de temps (+ amorce année −700 pour un affichage immédiat) + surcouches arméniennes `"o":1` |
| `periodes*.json` | Notices détaillées des périodes arméniennes — FR (`periodes.json`), EN, HY |
| `presence_armenienne.json` | Contour du « foyer arménien historique » (plateau + Cilicie) |
| `lacs.json` | Grands lacs (tracés réels Natural Earth) |
| `traductions_fr.json` | Dictionnaire EN→FR (~700 libellés d'États et cultures) |
| `build_globe_data.py` | Régénère `globe_data.json` + corrige les anachronismes de source (shapely) |
| `build_armenie_overlays.py` | Injecte les surcouches arméniennes (à lancer APRÈS build_globe_data) |
| `build_lacs.py` | Régénère `lacs.json` depuis Natural Earth |
| **`verifie_donnees.py`** | Contrôles avant publication : géométrie, enroulement, traductions, villes (**doit passer à 0 erreur**) |
| **`REGLES.md`** | Règles implémentées + liste des corrections de source (R9) |
| **`CRITIQUES.md`** | Registre d'autocritique par itération (ouvertes / traitées / invalidées) |
| `AMELIORATION.md` | Journal des premières itérations — **archivé**, voir CRITIQUES.md |

Sources (toutes neutres, **aucune source azerbaïdjanaise**) :
[aourednik/historical-basemaps](https://github.com/aourednik/historical-basemaps) (frontières),
Natural Earth (lacs). Le tracé du Haut-Karabagh est un polygone du NKAO historique reconstitué.
La source comporte des anachronismes sur le Caucase (Erevan persan en 1700, russe en 1880/1900,
Arménie de Sèvres surdimensionnée…) : ils sont **corrigés avec des données sourcées** (jamais
inventées) dans `build_globe_data.py` et documentés dans `REGLES.md` (R9). Un contrôle
`verifie_donnees.py` valide cohérence géométrique et fidélité numérique des traductions.

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
