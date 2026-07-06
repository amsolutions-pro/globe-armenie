#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit globe_data.json : frontières mondiales par siècle (historical-basemaps).
Source : https://github.com/aourednik/historical-basemaps
Usage : python3 build_globe_data.py   (télécharge dans ./geo/ si absent)
"""
import json, os, urllib.request
from shapely.geometry import shape, mapping, MultiPolygon, Polygon, GeometryCollection
from shapely.ops import unary_union
from shapely.validation import make_valid

YEARS = [(-10000,"bc10000"),(-8000,"bc8000"),(-5000,"bc5000"),(-4000,"bc4000"),(-3000,"bc3000"),
         (-2000,"bc2000"),(-1500,"bc1500"),(-1000,"bc1000"),(-700,"bc700"),
         (-500,"bc500"),(-300,"bc300"),(-100,"bc100"),(1,"bc1")] + \
        [(y,str(y)) for y in range(100,1801,100)] +         [(1815,"1815"),(1880,"1880"),(1900,"1900"),(1914,"1914"),
         (1915,"1914"),                       # génocide — fond ottoman/russe de 1914
         (1920,"1920"),(1921,"1920"),         # Première République ; traité de Kars
         (1930,"1930"),(1938,"1938"),(1945,"1945"),(1960,"1960"),
         (1988,"1960"),                       # séisme de Spitak — fond soviétique
         (1991,"1994"),                       # indépendance — fond post-soviétique
         (1994,"1994"),(2000,"2000"),(2010,"2010"),
         (2020,"2010"),(2023,"2010"),(2026,"2010")]  # guerre 44 j., exode d'Artsakh, aujourd'hui
BASE = "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/world_{}.geojson"
SIMPLIFY, ROUND, AIRE_MIN = 0.1, 2, 0.5

def only_poly(g):
    if isinstance(g,(Polygon,MultiPolygon)): return g
    if isinstance(g,GeometryCollection):
        polys=[x for x in g.geoms if isinstance(x,(Polygon,MultiPolygon))]
        return unary_union(polys) if polys else None
    return None

from shapely.geometry import box as _box
# Emprise ≈ RSS d'Arménie (boîte, robuste face aux polygones source mal enroulés)
SSR_BOX = _box(43.4, 38.8, 46.7, 41.3)

def process(fname, annee=None):
    path = f"geo/world_{fname}.geojson"
    if not os.path.exists(path):
        os.makedirs("geo", exist_ok=True)
        urllib.request.urlretrieve(BASE.format(fname), path)
    d = json.load(open(path, encoding="utf-8"))
    # Correction : en 1930 et 1938 la source dessine une « Grande Arménie »
    # anachronique (Anatolie orientale comprise). La ramener à la RSS réelle.
    if annee in (1930, 1938):
        for f in d["features"]:
            if (f["properties"].get("NAME") or "") == "Armenia" and f.get("geometry"):
                g = shape(f["geometry"]).buffer(0).intersection(SSR_BOX)
                f["geometry"] = mapping(g) if not g.is_empty else None
    feats = []
    for f in d["features"]:
        if not f.get("geometry"): continue
        try: g = only_poly(make_valid(shape(f["geometry"])))
        except Exception: continue
        if g is None or g.area < AIRE_MIN: continue
        gs = only_poly(g.simplify(SIMPLIFY, preserve_topology=True))
        if gs is None or gs.is_empty: continue
        gj = mapping(gs)
        def r(c):
            if isinstance(c[0],(int,float)): return [round(c[0],ROUND),round(c[1],ROUND)]
            return [r(x) for x in c]
        big = max(g.geoms,key=lambda x:x.area) if isinstance(g,MultiPolygon) else g
        p = big.representative_point()
        feats.append({"t":gj["type"],"c":r(gj["coordinates"]),
                      "n":f["properties"].get("NAME") or "",
                      "s":f["properties"].get("SUBJECTO") or "",
                      "l":[round(p.x,1),round(p.y,1)],"a":round(g.area)})
    feats.sort(key=lambda f:-f["a"])  # grands d'abord, petits dessinés au-dessus
    return feats

if __name__ == "__main__":
    DATA = {"years":[], "world":{}}
    for y,fn in YEARS:
        fs = process(fn, y)
        DATA["years"].append(y); DATA["world"][str(y)] = fs
        print(y, len(fs), "entités")
    s = json.dumps(DATA, ensure_ascii=False, separators=(",",":")).replace("</","<\\/")
    open("globe_data.json","w",encoding="utf-8").write(s)
    print("Écrit globe_data.json :", round(len(s)/1024/1024,2), "Mo")
