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
         (1918,"1920"),                        # proclamation de la Première République
         (1920,"1920"),(1921,"1920"),         # apogée républicaine ; traité de Kars
         (1923,"1930"),                        # création de l'oblast du Haut-Karabagh
         (1930,"1930"),(1938,"1938"),(1945,"1945"),(1960,"1960"),
         (1988,"1960"),                       # séisme de Spitak — fond soviétique
         (1991,"1994"),                       # indépendance — fond post-soviétique
         (1994,"1994"),(2000,"2000"),(2010,"2010"),(2018,"2010"),  # Révolution de velours
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
# Géométrie réelle de la RSS d'Arménie ≈ Arménie moderne (world_2000), pour
# clipper les « Grande Arménie » anachroniques sans produire de forme anguleuse.
_ARM_MODERNE = None
def arm_moderne():
    global _ARM_MODERNE
    if _ARM_MODERNE is None:
        p = "geo/world_2000.geojson"
        if not os.path.exists(p):
            urllib.request.urlretrieve(BASE.format("2000"), p)
        w = json.load(open(p, encoding="utf-8"))
        gs = [make_valid(shape(f["geometry"])) for f in w["features"]
              if (f["properties"].get("NAME") or "") == "Armenia" and f.get("geometry")]
        _ARM_MODERNE = unary_union(gs) if gs else None
    return _ARM_MODERNE

def process(fname, annee=None):
    path = f"geo/world_{fname}.geojson"
    if not os.path.exists(path):
        os.makedirs("geo", exist_ok=True)
        urllib.request.urlretrieve(BASE.format(fname), path)
    d = json.load(open(path, encoding="utf-8"))
    # Corrections cartographiques de la source (erreurs sur le Caucase 1900–1940).
    # (a) 1921/1923/1930/1938 : la source dessine une « Grande Arménie » anachronique
    #     (tracé de Sèvres, jusqu'en Anatolie) alors que seule la petite RSS existe.
    #     → clip sur la forme RÉELLE de l'Arménie moderne (pas une boîte : évite le
    #     « triangle » anguleux signalé pour 1921).
    if annee in (1921, 1923, 1930, 1938):
        mask = arm_moderne()
        if mask is not None:
            for f in d["features"]:
                if (f["properties"].get("NAME") or "") == "Armenia" and f.get("geometry"):
                    f["geometry"] = mapping(mask)   # remplacer par la RSS réelle
    # (b) 1914/1915 : la source montre Arménie/Azerbaïdjan/Géorgie INDÉPENDANTES,
    #     or en 1914 le Caucase du Sud est russe. → fusionner en UN SEUL polygone
    #     « Russian Empire » (sinon des frontières internes fantômes apparaissent).
    if annee in (1914, 1915):
        russes = [f for f in d["features"]
                  if (f["properties"].get("NAME") or "") in ("Russian Empire", "Armenia", "Azerbaijan", "Georgia")
                  and f.get("geometry")]
        if russes:
            union = unary_union([make_valid(shape(f["geometry"])).buffer(0) for f in russes])
            russes[0]["properties"]["NAME"] = "Russian Empire"
            russes[0]["properties"]["SUBJECTO"] = "Russian Empire"
            russes[0]["geometry"] = mapping(union)
            for f in russes[1:]:
                f["geometry"] = None
    # (c) 1918/1920 : l'Azerbaïdjan de la source (fond 1920) déborde vers l'ouest sur
    #     le Zanguezour/Syunik arménien. → lui soustraire l'Arménie moderne.
    if annee in (1918, 1920):
        mask = arm_moderne()
        if mask is not None:
            for f in d["features"]:
                if (f["properties"].get("NAME") or "") == "Azerbaijan" and f.get("geometry"):
                    g = make_valid(shape(f["geometry"])).difference(mask)
                    f["geometry"] = mapping(g) if not g.is_empty else None
    # (d) 1880/1900 : la source fait couvrir Erevan/Syunik par la PERSE, or ils
    #     sont russes depuis Turkmentchaï (1828). → transférer la Transcaucasie
    #     russe (nord de l'Araxe) de la Perse vers l'Empire russe.
    if annee in (1880, 1900):
        from shapely.geometry import Polygon as _Poly
        RUSSE_TRANS = _Poly([(42.5,41.9),(42.55,41.3),(42.7,40.9),(42.8,40.4),
                             (43.4,40.05),(44.0,39.85),(44.32,39.72),(44.8,39.70),
                             (45.4,39.56),(45.8,39.30),(46.2,38.95),(46.55,38.87),
                             (47.1,39.15),(47.6,39.35),(47.6,41.9)])
        perse = russie = None
        for f in d["features"]:
            nm = f["properties"].get("NAME") or ""
            if nm == "Persia" and f.get("geometry"): perse = f
            elif nm == "Russian Empire" and f.get("geometry"): russie = f
        if perse is not None:
            gp = make_valid(shape(perse["geometry"])).buffer(0)
            transfert = gp.intersection(RUSSE_TRANS)
            perse["geometry"] = mapping(gp.difference(RUSSE_TRANS))
            if russie is not None and not transfert.is_empty:
                gr = make_valid(shape(russie["geometry"])).buffer(0)
                russie["geometry"] = mapping(unary_union([gr, transfert]))
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
