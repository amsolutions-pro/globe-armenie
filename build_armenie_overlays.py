#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte dans globe_data.json des surcouches arméniennes dérivées (intersections
shapely) pour les siècles où la source ne contient aucune entité arménienne.
Marquées "o":1 (dessinées au-dessus, style or dans globe.html). Rejouable : purge
les anciennes surcouches avant réinjection.
Usage : python build_armenie_overlays.py
"""
import json, os, re, sys, urllib.request
from shapely.geometry import shape, mapping, box, MultiPolygon, Polygon, GeometryCollection
from shapely.ops import unary_union
from shapely.validation import make_valid

BASE = "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/world_{}.geojson"
SIMPLIFY, ROUND = 0.1, 2

def fname(y): return f"bc{-y}" if y < 0 else ("bc1" if y == 1 else str(y))

def load_world(y):
    f = fname(y) if y != 1 else "bc1"
    path = f"geo/world_{f}.geojson"
    if not os.path.exists(path):
        os.makedirs("geo", exist_ok=True)
        print(f"  téléchargement world_{f}.geojson…")
        urllib.request.urlretrieve(BASE.format(f), path)
    return json.load(open(path, encoding="utf-8"))

def only_poly(g):
    if isinstance(g, (Polygon, MultiPolygon)): return g
    if isinstance(g, GeometryCollection):
        p = [x for x in g.geoms if isinstance(x, (Polygon, MultiPolygon))]
        return unary_union(p) if p else None
    return None

def geom_of(world, pattern):
    """Union des géométries dont NAME matche le motif (regex, insensible à la casse)."""
    gs = []
    for f in world["features"]:
        n = (f["properties"].get("NAME") or "")
        if f.get("geometry") and re.search(pattern, n, re.I):
            g = only_poly(make_valid(shape(f["geometry"])))
            if g is not None and not g.is_empty: gs.append(g)
    return unary_union(gs) if gs else None

# Emprise du plateau arménien historique + Cilicie, pour borner les intersections
PLATEAU = box(37.0, 37.5, 47.5, 41.8)
# Cilicie : polygone suivant la crête des monts Taurus (nord) et le golfe d'Alexandrette (est)
CILICIE = Polygon([(32.3,36.0),(32.3,36.7),(33.5,37.3),(34.6,37.9),(35.6,38.3),
                   (36.6,38.2),(37.2,37.4),(36.6,35.8),(32.3,35.8)])
# Partage de Zuhab (1639) : frontière approx. Arpatchaï–Araxe vers 43,7°E
ZUHAB_OUEST = box(36.0, 35.5, 43.7, 42.5)
ZUHAB_EST   = box(43.7, 35.5, 48.5, 42.5)
# Transcaucasie russe vers 1900 (Kars 1878 + Erevan/Zanguezour, nord de l'Araxe)
RUSSE_1900  = box(42.5, 38.8, 47.5, 41.8)
# Haut-Karabagh : polygone approché de l'oblast autonome (NKAO)
KARABAGH = Polygon([(46.45,40.20),(46.85,40.05),(47.05,39.85),(46.95,39.60),
                    (46.75,39.35),(46.50,39.30),(46.30,39.45),(46.25,39.75)])

# Gabarit "Arménie étendue" : Arménie arsacide (an 300, la plus large des couches sources)
def gabarit_armenie():
    w = load_world(300)
    g = geom_of(w, r"^Armenia$")
    if g is None: sys.exit("Gabarit Armenia(300) introuvable")
    return g

# (année_cible, nom_FR, suzerain_FR, source_du_masque, motif_empire_dans_l_année_cible, emprise)
SPECS = [
    (-10000, "Chasseurs-cueilleurs du plateau arménien", "Épipaléolithique — grottes du Hrazdan et de l'Araxe", "tout", None, PLATEAU),
    (-8000, "Premiers villages du plateau arménien", "Néolithisation — obsidienne, orge et blé engrain", "tout", None, PLATEAU),
    (-5000, "Néolithique arménien (Aratashen, Aknashen)", "Villages agricoles de la vallée de l'Araxe", "tout", None, PLATEAU),
    (-4000, "Chalcolithique arménien (Areni, Sioni)", "Métallurgie du cuivre — plus vieille cave à vin du monde (Areni-1)", "tout", None, PLATEAU),
    (-3000, "Culture Kouro-Araxe", "Âge du bronze ancien — expansion du Caucase au Levant", "tout", None, PLATEAU),
    (-2000, "Cultures Trialeti et du Sevan", "Âge du bronze moyen — kourganes princiers", "tout", None, PLATEAU),
    (-500, "Armina (satrapie d'Arménie)", "Empire achéménide", "armenia:-300", r"achaemenid|persian?\b|persia", PLATEAU),
    (-100, "Grande Arménie (Artaxiades)", "Royaume indépendant — Tigrane II", "armenia:-1", None, PLATEAU),
    (400,  "Arménie arsacide (partagée en 387)", "Rome / Perse sassanide", "gabarit", None, PLATEAU),
    (500,  "Persarménie (marzpanat)", "Empire sassanide", "gabarit", r"sasanian|sassanid", PLATEAU),
    (500,  "Arménie byzantine", "Empire byzantin", "gabarit", r"byzantine|eastern roman|roman empire", PLATEAU),
    (600,  "Persarménie (marzpanat)", "Empire sassanide", "gabarit", r"sasanian|sassanid", PLATEAU),
    (600,  "Arménie byzantine", "Empire byzantin", "gabarit", r"byzantine|eastern roman|roman empire", PLATEAU),
    # 800 : gabarit conservé — l'Armenia de 700 (principauté autonome) est trop
    # étroite pour représenter l'ostikanat (terres arméniennes sous califat)
    (800,  "Arminiya (ostikanat)", "Califat abbasside", "gabarit", r"abbasid|caliphate", PLATEAU),
    (900,  "Royaume bagratide (Arménie)", "Dynastie bagratide", "armenia:1000", None, PLATEAU),
    (1300, "Arménie sous l'Ilkhanat", "Ilkhanat mongol", "armenia:1200", r"ilkhanate|il-?khan", PLATEAU),
    (1300, "Royaume arménien de Cilicie", "Dynastie héthoumide", "tout", None, CILICIE),
    (1400, "Arménie (domination timouride)", "Empire timouride", "gabarit", r"timurid", PLATEAU),
    (1500, "Arménie (Ak Koyunlu)", "Ak Koyunlu (Mouton blanc)", "gabarit", r"white sheep", PLATEAU),
    (1500, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1600, "Arménie occidentale (ottomane)", "Empire ottoman — paix de Zuhab (1639)", "gabarit", r"ottoman", PLATEAU.intersection(ZUHAB_OUEST)),
    (1600, "Arménie orientale (persane)", "Perse séfévide — paix de Zuhab (1639)", "gabarit", r"ottoman|safavid|persia", PLATEAU.intersection(ZUHAB_EST)),
    (1700, "Arménie occidentale (ottomane)", "Empire ottoman — paix de Zuhab (1639)", "gabarit", r"ottoman", PLATEAU.intersection(ZUHAB_OUEST)),
    (1700, "Arménie orientale (persane)", "Perse séfévide — paix de Zuhab (1639)", "gabarit", r"ottoman|safavid|persia", PLATEAU.intersection(ZUHAB_EST)),
    (1800, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1800, "Arménie orientale (khanats d'Erevan et du Karabagh)", "Perse kadjare", "gabarit", r"persia|qajar|central asian khanates|russia", PLATEAU),
    (1815, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1815, "Arménie orientale (khanats d'Erevan et du Karabagh)", "Perse kadjare", "gabarit", r"persia|qajar|central asian khanates|russia", PLATEAU),
    (1880, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU.difference(RUSSE_1900)),
    (1880, "Arménie russe (gouvernorats d'Erevan et de Kars)", "Empire russe — Turkmentchaï (1828), Berlin (1878)", "gabarit", r"russia|persia|ottoman", PLATEAU.intersection(RUSSE_1900)),
    (1900, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU.difference(RUSSE_1900)),
    (1900, "Arménie russe (gouvernorats d'Erevan et de Kars)", "Empire russe — traités de Turkmentchaï (1828) et Berlin (1878)", "gabarit", r"russia|persia|ottoman", PLATEAU.intersection(RUSSE_1900)),
    (1914, "Arménie occidentale (six vilayets)", "Empire ottoman — veille du génocide de 1915", "gabarit", r"ottoman", PLATEAU.difference(RUSSE_1900)),
    (1945, "RSS d'Arménie", "Union soviétique (depuis 1920/1922)", "armenia:2000", None, PLATEAU),
    (1960, "RSS d'Arménie", "Union soviétique", "armenia:2000", None, PLATEAU),
    (1994, "Haut-Karabagh (contrôle arménien)", "République autoproclamée d'Artsakh (1991–2023)", "tout", r"azerbaijan", KARABAGH),
    (2010, "Haut-Karabagh (contrôle arménien)", "République autoproclamée d'Artsakh (1991–2023)", "tout", r"azerbaijan", KARABAGH),
]

def rnd(c):
    if isinstance(c[0], (int, float)): return [round(c[0], ROUND), round(c[1], ROUND)]
    return [rnd(x) for x in c]

def main():
    data = json.load(open("globe_data.json", encoding="utf-8"))
    # purge des anciennes surcouches
    for y in data["world"]:
        data["world"][y] = [f for f in data["world"][y] if not f.get("o")]

    gab = gabarit_armenie()
    # Masques par époque : "armenia:<année>" = géométrie Armenia de l'année source
    # la plus proche documentée (au lieu du gabarit unique an 300 pour tout)
    cache_arm = {}
    def masque_armenia(an):
        if an not in cache_arm:
            cache_arm[an] = geom_of(load_world(an), r"^Armenia$")
        return cache_arm[an] if cache_arm[an] is not None else gab
    ajouts = 0
    for (y, nom, suz, source, motif, emprise) in SPECS:
        if source == "gabarit":
            masque = gab
        elif source.startswith("armenia:"):
            masque = masque_armenia(int(source.split(":")[1]))
        elif source == "tout":
            masque = None  # emprise ∩ toutes les terres
        g = None
        w = load_world(y)
        if motif:
            emp = geom_of(w, motif)
            if emp is None:
                print(f"!! {y} : empire '{motif}' introuvable — noms dispo à vérifier"); continue
            g = (masque if masque is not None else emprise).intersection(emp).intersection(emprise)
        elif masque is not None:
            g = masque.intersection(emprise)
        else:
            terres = unary_union([only_poly(make_valid(shape(f["geometry"])))
                                  for f in w["features"] if f.get("geometry")])
            g = terres.intersection(emprise)
        g = only_poly(make_valid(g))
        if g is None or g.is_empty:
            print(f"!! {y} : intersection vide pour {nom}"); continue
        gs = only_poly(g.simplify(SIMPLIFY, preserve_topology=True)) or g
        gj = mapping(gs)
        big = max(g.geoms, key=lambda x: x.area) if isinstance(g, MultiPolygon) else g
        p = big.representative_point()
        data["world"][str(y)].append({
            "t": gj["type"], "c": rnd(gj["coordinates"]),
            "n": nom, "s": suz,
            "l": [round(p.x, 1), round(p.y, 1)], "a": round(g.area, 1) or 0.1, "o": 1})
        ajouts += 1
        print(f"OK {y} : {nom} (aire {round(g.area,1)} deg²)")

    # tri : grands d'abord, surcouches "o" toujours en dernier (dessinées au-dessus)
    for y in data["world"]:
        data["world"][y].sort(key=lambda f: (f.get("o", 0), -f["a"]))
    s = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    open("globe_data.json", "w", encoding="utf-8").write(s)
    print(f"\n{ajouts} surcouches injectées — globe_data.json : {round(len(s)/1024/1024,2)} Mo")

if __name__ == "__main__":
    main()
