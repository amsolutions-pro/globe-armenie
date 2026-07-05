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

YEARS = [(-2000,"bc2000"),(-1500,"bc1500"),(-1000,"bc1000"),(-700,"bc700"),
         (-500,"bc500"),(-300,"bc300"),(-100,"bc100"),(1,"bc1")] + \
        [(y,str(y)) for y in range(100,2001,100)]
BASE = "https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/world_{}.geojson"
SIMPLIFY, ROUND, AIRE_MIN = 0.1, 2, 0.5

def only_poly(g):
    if isinstance(g,(Polygon,MultiPolygon)): return g
    if isinstance(g,GeometryCollection):
        polys=[x for x in g.geoms if isinstance(x,(Polygon,MultiPolygon))]
        return unary_union(polys) if polys else None
    return None

def process(fname):
    path = f"geo/world_{fname}.geojson"
    if not os.path.exists(path):
        os.makedirs("geo", exist_ok=True)
        urllib.request.urlretrieve(BASE.format(fname), path)
    d = json.load(open(path))
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
        fs = process(fn)
        DATA["years"].append(y); DATA["world"][str(y)] = fs
        print(y, len(fs), "entités")
    s = json.dumps(DATA, ensure_ascii=False, separators=(",",":")).replace("</","<\\/")
    open("globe_data.json","w").write(s)
    print("Écrit globe_data.json :", round(len(s)/1024/1024,2), "Mo")
