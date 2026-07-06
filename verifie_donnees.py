# -*- coding: utf-8 -*-
"""Vérifications de cohérence de globe_data.json avant publication.

Usage : python verifie_donnees.py   (code retour 0 = OK, 1 = erreurs)
"""
import json, sys

ERREURS = []
AVERTS  = []

def err(msg):  ERREURS.append(msg)
def warn(msg): AVERTS.append(msg)

def main():
    d = json.load(open("globe_data.json", encoding="utf-8"))

    # 1. Années triées, uniques, toutes présentes dans world
    years = d["years"]
    if years != sorted(set(years)):
        err("d['years'] n'est pas trié/unique")
    for y in years:
        if str(y) not in d["world"]:
            err(f"année {y} absente de d['world']")
    for y in d["world"]:
        if int(y) not in years:
            err(f"world[{y}] n'est pas déclarée dans d['years']")

    # 2. Chaque feature : type, anneaux fermés et >= 4 points, coordonnées bornées
    for y, feats in d["world"].items():
        if not feats:
            err(f"world[{y}] est vide")
        for f in feats:
            nom = f.get("n", "?")
            if f["t"] not in ("Polygon", "MultiPolygon"):
                err(f"{y}/{nom} : type {f['t']} inattendu"); continue
            polys = [f["c"]] if f["t"] == "Polygon" else f["c"]
            for poly in polys:
                for ring in poly:
                    if len(ring) < 4:
                        err(f"{y}/{nom} : anneau de {len(ring)} points (< 4)")
                    elif ring[0] != ring[-1]:
                        err(f"{y}/{nom} : anneau non fermé")
                    for lon, lat in ring:
                        if not (-180.001 <= lon <= 180.001 and -90.001 <= lat <= 90.001):
                            err(f"{y}/{nom} : coordonnée hors bornes ({lon},{lat})")
                            break

    # 3. Surcouches arméniennes (o=1) : nombre attendu et présence par période
    ov = [(int(y), f["n"]) for y in d["world"] for f in d["world"][y] if f.get("o")]
    if len(ov) != 37:
        warn(f"{len(ov)} surcouches o=1 (37 attendues — mettre à jour si volontaire)")
    for a, b in [(1945, 1960), (1994, 2010)]:
        for y in (a, b):
            if not any(yy == y for yy, _ in ov):
                err(f"aucune surcouche arménienne en {y}")

    # 4. Une entité nommée Armenia/Arménie doit exister aux périodes d'indépendance
    for y in (-300, 1000, 2000):
        if str(y) in d["world"]:
            noms = [f["n"] for f in d["world"][str(y)]]
            if not any("rmeni" in n for n in noms):
                err(f"pas d'entité 'Armenia' en {y} alors qu'attendue")

    for m in AVERTS:  print("AVERT :", m)
    for m in ERREURS: print("ERREUR:", m)
    if ERREURS:
        print(f"\n{len(ERREURS)} erreur(s)."); sys.exit(1)
    print(f"OK — {len(years)} pas de temps, {len(ov)} surcouches, {len(AVERTS)} avertissement(s).")

if __name__ == "__main__":
    main()
