#!/usr/bin/env python3
"""
Cover-Generator fuer die Jack-Verbeek-Reihe.

Aufruf:   python3 tools/gen_cover.py   (aus dem Repo, Ort egal)
Ausgabe:  assets/cover-band-01.svg (+ optional PNG, siehe unten)

Stellschrauben
--------------
SH          Farbe der Palmen. Muss deutlich dunkler sein als der Himmel,
            sonst verschwinden die Silhouetten.
Himmel      <rect ... fill="#1B2B33">  — heller = mehr Daemmerung,
            dunkler = mehr Nacht, aber schlechter sichtbare Palmen.
Wasser      <rect y="762" ... fill="#101C22">
left/right  Liste von (Winkel, Laenge, Fiederlaenge) je Wedel.
            Winkel in Grad, 0 = nach rechts, negativ = nach oben.
random.seed Aendert die zufaellige Streuung der Fiedern. Anderer Wert
            = anderes Wedel-Muster bei gleichem Aufbau.

Fuer Band 2: Titelzeilen und Bandnummer unten im svg-String tauschen,
Dateinamen in der letzten Zeile anpassen.

Benoetigt fuer den PNG-Export: pip install cairosvg
"""

import math, os, random
random.seed(23)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "assets", "cover-band-01.svg")

SH = "#050A0C"   # gleiche Farbe wie der Strich unten

def frond(x0, y0, rot, L, lmax, n=42, droop_f=0.18, bw=4.2):
    """Gefuellte Palmwedel-Silhouette: Mittelrippe plus getaperte Fiedern."""
    droop = droop_f * L
    p = [f'<path d="M0 {-2.6:.0f} Q{L*0.5:.0f} {droop*0.15-2:.0f} {L:.0f} {droop:.0f} '
         f'Q{L*0.5:.0f} {droop*0.15+2:.0f} 0 {2.6:.0f} Z" fill="{SH}"/>']
    for i in range(n):
        t = 0.03 + 0.96 * i / (n - 1)
        px, py = L * t, droop * t * t
        tang = math.radians(math.degrees(math.atan2(2 * droop * t, L)))
        ln = lmax * (0.30 + 0.70 * math.sin(math.pi * (t ** 0.72))) * random.uniform(0.84, 1.16)
        b = bw * (1.05 - 0.45 * t)
        for side in (-1, 1):
            a = tang + math.radians(side * (82 - 56 * t) + random.uniform(-5, 5))
            tx, ty = px + ln * math.cos(a), py + ln * math.sin(a)
            ca = a - math.radians(side * 26)
            cxx, cyy = px + ln * 0.55 * math.cos(ca), py + ln * 0.55 * math.sin(ca)
            nx, ny = -math.sin(a), math.cos(a)
            b1x, b1y = px + b * math.cos(tang), py + b * math.sin(tang)
            b2x, b2y = px - b * math.cos(tang), py - b * math.sin(tang)
            p.append(
                f'<path d="M{b1x:.0f} {b1y:.0f} Q{cxx+nx*2.4:.0f} {cyy+ny*2.4:.0f} {tx:.0f} {ty:.0f} '
                f'Q{cxx-nx*2.4:.0f} {cyy-ny*2.4:.0f} {b2x:.0f} {b2y:.0f} Z" fill="{SH}"/>')
    return f'<g transform="translate({x0} {y0}) rotate({rot})">{"".join(p)}</g>'

def cluster(x0, y0, specs):
    out = []
    for ang, L, lm in specs:
        out.append(frond(x0 + random.uniform(-14, 14), y0 + random.uniform(-12, 12),
                         ang, L, lm, n=max(30, int(L / 11))))
    return "".join(out)

left = cluster(-46, 930, [(-97, 540, 96), (-78, 500, 92), (-58, 430, 84),
                          (-38, 360, 74), (-118, 400, 80)])
right = cluster(726, 918, [(-83, 520, 94), (-102, 545, 96), (-122, 445, 86),
                           (-142, 370, 76), (-62, 380, 78)])

svg = f'''<svg width="1200" height="1800" viewBox="0 0 680 1020" xmlns="http://www.w3.org/2000/svg" role="img">
<title>Zwoelf Tage tot — Coverentwurf Band 1</title>
<desc>Typografischer Thriller-Coverentwurf: Nachthimmel ueber Wasser, dunkle Palmwedel-Silhouetten in den unteren Ecken, aufsteigende Raketenspur, Titel in hellen Versalien.</desc>
<rect x="0" y="0" width="680" height="1020" fill="#1B2B33"/>
<rect x="0" y="762" width="680" height="258" fill="#101C22"/>
<rect x="0" y="760" width="680" height="2" fill="#2E434C"/>
<circle cx="548" cy="168" r="24" fill="#E8DCC4"/>
<path d="M150 762 C 250 700, 380 480, 560 190" fill="none" stroke="#D9793B" stroke-width="3" stroke-linecap="round"/>
<circle cx="560" cy="190" r="5" fill="#F0A45E"/>
<rect x="336" y="726" width="5" height="34" fill="#050A0C"/>
<circle cx="338" cy="720" r="6" fill="#050A0C"/>
{left}{right}
<rect x="212" y="98" width="256" height="1" fill="#4A5C63"/>
<text x="340" y="142" text-anchor="middle" fill="#C6B79A" font-family="Helvetica, Arial, sans-serif" font-size="21" font-weight="400" letter-spacing="8">TILL MERL\u00c9</text>
<rect x="212" y="164" width="256" height="1" fill="#4A5C63"/>
<text x="340" y="404" text-anchor="middle" fill="#F4EFE6" font-family="Helvetica, Arial, sans-serif" font-size="92" font-weight="500" letter-spacing="4">ZW\u00d6LF</text>
<text x="340" y="500" text-anchor="middle" fill="#F4EFE6" font-family="Helvetica, Arial, sans-serif" font-size="92" font-weight="500" letter-spacing="4">TAGE</text>
<text x="340" y="596" text-anchor="middle" fill="#D9793B" font-family="Helvetica, Arial, sans-serif" font-size="92" font-weight="500" letter-spacing="4">TOT</text>
<rect x="286" y="640" width="108" height="1" fill="#D9793B"/>
<text x="340" y="686" text-anchor="middle" fill="#9EAEB4" font-family="Helvetica, Arial, sans-serif" font-size="16" font-weight="400" letter-spacing="5">EIN JACK-VERBEEK-THRILLER</text>
<text x="340" y="962" text-anchor="middle" fill="#5E7079" font-family="Helvetica, Arial, sans-serif" font-size="15" font-weight="400" letter-spacing="4">BAND 1</text>
</svg>
'''
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(svg)
print(OUT, "bytes:", len(svg))

# PNG-Export (auskommentiert lassen, wenn cairosvg nicht installiert ist)
# import cairosvg
# cairosvg.svg2png(url="assets/cover-band-01.svg",
#                  write_to="assets/cover-band-01.png",
#                  output_width=1600)
