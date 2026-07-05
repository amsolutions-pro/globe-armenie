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
CILICIE = box(32.5, 36.0, 37.0, 38.4)

# Gabarit "Arménie étendue" : Arménie arsacide (an 300, la plus large des couches sources)
def gabarit_armenie():
    w = load_world(300)
    g = geom_of(w, r"^Armenia$")
    if g is None: sys.exit("Gabarit Armenia(300) introuvable")
    return g

# (année_cible, nom_FR, suzerain_FR, source_du_masque, motif_empire_dans_l_année_cible, emprise)
SPECS = [
    (-500, "Armina (satrapie d'Arménie)", "Empire achéménide", "gabarit", r"achaemenid|persian?\b|persia", PLATEAU),
    (-100, "Grande Arménie (Artaxiades)", "Royaume indépendant — Tigrane II", "gabarit", None, PLATEAU),
    (400,  "Arménie arsacide (partagée en 387)", "Rome / Perse sassanide", "gabarit", None, PLATEAU),
    (500,  "Persarménie (marzpanat)", "Empire sassanide", "gabarit", r"sasanian|sassanid", PLATEAU),
    (500,  "Arménie byzantine", "Empire byzantin", "gabarit", r"byzantine|eastern roman|roman empire", PLATEAU),
    (600,  "Persarménie (marzpanat)", "Empire sassanide", "gabarit", r"sasanian|sassanid", PLATEAU),
    (600,  "Arménie byzantine", "Empire byzantin", "gabarit", r"byzantine|eastern roman|roman empire", PLATEAU),
    (800,  "Arminiya (ostikanat)", "Califat abbasside", "gabarit", r"abbasid|caliphate", PLATEAU),
    (900,  "Royaume bagratide (Arménie)", "Dynastie bagratide", "armenia1000", None, PLATEAU),
    (1300, "Arménie sous l'Ilkhanat", "Ilkhanat mongol", "gabarit", r"ilkhanate|il-?khan", PLATEAU),
    (1300, "Royaume arménien de Cilicie", "Dynastie héthoumide", "tout", None, CILICIE),
    (1400, "Arménie (domination timouride)", "Empire timouride", "gabarit", r"timurid", PLATEAU),
    (1500, "Arménie (Ak Koyunlu)", "Ak Koyunlu (Mouton blanc)", "gabarit", r"white sheep", PLATEAU),
    (1500, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1600, "Arménie sous l'Empire ottoman", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1700, "Arménie sous l'Empire ottoman", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1800, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1800, "Arménie orientale (khanats d'Erevan et du Karabagh)", "Perse kadjare", "gabarit", r"persia|qajar|central asian khanates|russia", PLATEAU),
    (1900, "Arménie occidentale (ottomane)", "Empire ottoman", "gabarit", r"ottoman", PLATEAU),
    (1900, "Arménie orientale (russe)", "Empire russe", "gabarit", r"russia|persia", PLATEAU),
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
    arm1000 = None
    ajouts = 0
    for (y, nom, suz, source, motif, emprise) in SPECS:
        if source == "gabarit":
            masque = gab
        elif source == "armenia1000":
            if arm1000 is None:
                arm1000 = geom_of(load_world(1000), r"^Armenia$")
            masque = arm1000 if arm1000 is not None else gab
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
