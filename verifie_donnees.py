# -*- coding: utf-8 -*-
"""Vérifications de cohérence de globe_data.json avant publication.

Usage : python verifie_donnees.py   (code retour 0 = OK, 1 = erreurs)
"""
import json, sys, math

ERREURS = []
AVERTS  = []

def err(msg):  ERREURS.append(msg)
def warn(msg): AVERTS.append(msg)

import re as _re
def nombres(texte):
    """Ensemble des nombres d'un texte, séparateurs de milliers/décimaux normalisés."""
    t = texte
    for _ in range(3):
        t = _re.sub(u"([0-9])[    ,.]([0-9])", lambda m: m.group(1) + m.group(2), t)
    return set(_re.findall(r"\d{3,}|\d{1,2}(?!\d)", t))

def aire_spherique(ring):
    """Aire de l'anneau sur la sphère unité, en stéradians (valeur absolue)."""
    s = 0.0; n = len(ring)
    for i in range(n):
        lo1, la1 = math.radians(ring[i][0]), math.radians(ring[i][1])
        lo2, la2 = math.radians(ring[(i + 1) % n][0]), math.radians(ring[(i + 1) % n][1])
        s += (lo2 - lo1) * (2 + math.sin(la1) + math.sin(la2))
    return abs(s / 2.0)

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
                # Anneau extérieur inversé (> 2π stéradians) : remplirait la sphère
                # au rendu (bug historique « océans qui changent de couleur »).
                if poly and len(poly[0]) >= 4 and aire_spherique(poly[0]) > 6.283:
                    err(f"{y}/{nom} : anneau extérieur inversé (enroulement)")

    # 3. Surcouches arméniennes (o=1) : nombre attendu = len(SPECS) du script
    # de build (lu par regex pour éviter d'exécuter son code au niveau module)
    import re as _re
    src = open("build_armenie_overlays.py", encoding="utf-8").read()
    bloc = src.split("SPECS = [", 1)[1].split("\n]", 1)[0]
    attendu = len(_re.findall(r"^\s*\(", bloc, _re.M))
    ov = [(int(y), f["n"]) for y in d["world"] for f in d["world"][y] if f.get("o")]
    if len(ov) != attendu:
        warn(f"{len(ov)} surcouches o=1 ({attendu} attendues d'après SPECS)")
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

    # 5. Notices de périodes : les 3 langues alignées, champs essentiels, capitales valides
    per = {}
    for fn in ("periodes.json", "periodes_en.json", "periodes_hy.json"):
        try:
            per[fn] = json.load(open(fn, encoding="utf-8"))
        except Exception as e:
            err(f"{fn} : illisible ({e})")
    if len(per) == 3:
        n0 = len(per["periodes.json"])
        for fn, lst in per.items():
            if len(lst) != n0:
                err(f"{fn} : {len(lst)} notices au lieu de {n0} (langues désalignées)")
            for i, p in enumerate(lst):
                if p is None:
                    warn(f"{fn}[{i}] : notice null (traduction manquante, repli sur une autre langue)")
                    continue
                for champ in ("nom", "dates", "pouvoir", "apercu"):
                    if not p.get(champ):
                        err(f"{fn}[{i}] : champ '{champ}' vide ou absent")
                for cap in p.get("capitales", []):
                    if not (-90 <= cap.get("lat", 999) <= 90 and -180 <= cap.get("lng", 999) <= 180):
                        err(f"{fn}[{i}] : capitale {cap.get('nom','?')} hors bornes")
        # provinces : présentes en FR, tolérées absentes ailleurs mais signalées
        for i, p in enumerate(per["periodes.json"]):
            if not p.get("provinces"):
                warn(f"periodes.json[{i}] ({p.get('nom','?')}) : pas de provinces")
        # Fidélité numérique des aperçus : aucun nombre EN/HY absent du FR.
        fr_lst = per["periodes.json"]
        for fn in ("periodes_en.json", "periodes_hy.json"):
            for i, p in enumerate(per.get(fn, [])):
                if p is None or i >= len(fr_lst) or fr_lst[i] is None:
                    continue
                nf = nombres(" ".join(fr_lst[i].get("apercu", [])))
                nt = nombres(" ".join(p.get("apercu", [])))
                surplus = nt - nf
                if surplus:
                    warn(f"{fn}[{i}] : nombre(s) absent(s) du FR : {sorted(surplus)} (format ?)")

    # 6. lacs.json : 16 lacs, anneaux fermés, coordonnées bornées
    try:
        lacs = json.load(open("lacs.json", encoding="utf-8"))
        if len(lacs) != 16:
            warn(f"lacs.json : {len(lacs)} lacs (16 attendus)")
        for l in lacs:
            polys = [l["c"]] if l["t"] == "Polygon" else l["c"]
            for poly in polys:
                for ring in poly:
                    if ring[0] != ring[-1]:
                        err(f"lacs.json/{l['nom']} : anneau non fermé")
                    for lon, lat in ring:
                        if not (-180.001 <= lon <= 180.001 and -90.001 <= lat <= 90.001):
                            err(f"lacs.json/{l['nom']} : coordonnée hors bornes"); break
    except FileNotFoundError:
        warn("lacs.json absent (les ellipses de repli seront utilisées)")

    # 7. Fidélité numérique des notices traduites : aucun nombre d'une notice
    # EN ou HY ne doit être absent de la notice FR (garde-fou anti-erreur de
    # date/chiffre lors des traductions — cf. it. 74).
    import re as _re2
    try:
        html = open("globe.html", encoding="utf-8").read()
        def _bloc(nom):
            i = html.index("const " + nom + " = {")
            return html[i:html.index("};", i)]
        def _apercu(bl, key):
            m = _re2.search(r'"' + _re2.escape(key) + r'":\{.*?apercu:\[(.*?)\](?:,capitales|\})', bl, _re2.S)
            return m.group(1) if m else None
        def _nums(t):
            for _ in range(3):
                t = _re2.sub(u"([0-9])[    ,.]([0-9])", lambda m: m.group(1)+m.group(2), t)
            return set(_re2.findall(r"\d{3,}|\d{1,2}(?!\d)", t))
        fr_b = _bloc("MINI")
        for lang in ("MINI_EN", "MINI_HY"):
            tr_b = _bloc(lang)
            for key in _re2.findall(r'"(-?\d+)":\{', tr_b):
                af, at = _apercu(fr_b, key), _apercu(tr_b, key)
                if af is None or at is None:
                    continue
                surplus = _nums(at) - _nums(af)
                if surplus:
                    warn(f"{lang}[{key}] : nombre(s) absent(s) du FR : {sorted(surplus)} (format ?)")
    except (FileNotFoundError, ValueError):
        warn("globe.html : contrôle de fidélité numérique des notices ignoré")

    for m in AVERTS:  print("AVERT :", m)
    for m in ERREURS: print("ERREUR:", m)
    if ERREURS:
        print(f"\n{len(ERREURS)} erreur(s)."); sys.exit(1)
    print(f"OK — {len(years)} pas de temps, {len(ov)} surcouches, {len(AVERTS)} avertissement(s).")

if __name__ == "__main__":
    main()
