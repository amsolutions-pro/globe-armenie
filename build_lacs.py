# -*- coding: utf-8 -*-
"""Extrait les tracés réels des grands lacs depuis Natural Earth 50m et écrit
lacs.json (remplace les lacs-ellipses approximatifs de globe.html).
Usage : python build_lacs.py
"""
import json, os, urllib.request
from shapely.geometry import shape, mapping, MultiPolygon
from shapely.validation import make_valid

URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_lakes.geojson"
PATH = "geo/ne_50m_lakes.geojson"
CIBLES = ["Lake Van","Lake Sevan","Lake Urmia","Lake Balkhash","Lake Baikal",
          "Lake Ladoga","Lake Victoria","Lake Tanganyika","Lake Malawi",
          "Lake Chad","Lake Superior","Lake Michigan","Lake Huron",
          "Lake Erie","Lake Ontario","Lago Titicaca"]

def main():
    if not os.path.exists(PATH):
        os.makedirs("geo", exist_ok=True)
        print("téléchargement ne_50m_lakes…")
        urllib.request.urlretrieve(URL, PATH)
    w = json.load(open(PATH, encoding="utf-8"))
    dispo = {f["properties"].get("name"): f for f in w["features"] if f["properties"].get("name")}
    out = []
    for nom in CIBLES:
        f = dispo.get(nom)
        if not f:
            print(f"!! {nom} absent de NE 50m — l'ellipse de repli restera utilisée")
            continue
        g = make_valid(shape(f["geometry"])).simplify(0.05, preserve_topology=True)
        gj = mapping(g)
        def rnd(c):
            if isinstance(c[0], (int, float)): return [round(c[0], 2), round(c[1], 2)]
            return [rnd(x) for x in c]
        out.append({"nom": nom, "t": gj["type"], "c": rnd(gj["coordinates"])})
        print(f"OK {nom}")
    s = json.dumps(out, ensure_ascii=False, separators=(",", ":"))
    open("lacs.json", "w", encoding="utf-8").write(s)
    print(f"\n{len(out)} lacs — lacs.json : {round(len(s)/1024,1)} Ko")

if __name__ == "__main__":
    main()
