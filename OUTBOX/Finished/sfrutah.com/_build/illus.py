"""Original drawings for the sfrutah.com redesign.
utah_map(): Utah drawn from its real boundary (37-42 N, 114.05-109.04 W, with the northeast notch at 111.05 W / 41 N) in an
equirectangular projection (x scaled by cos 39.5 deg), the I-15 corridor through real town coordinates, both offices and every
city the client has a page for. pier_section(): the Orem case study as a section: lake-bed sediment and a spring under the
house, helical piers to 33-40 ft (deepest 43 ft), the 11-inch corner settlement. Numbers are from the client's case study."""
import math

K = math.cos(math.radians(39.5))
W0, N0, SC = -114.052, 42.0, 92  # px per degree of latitude


def P(lat, lon):
    return round((lon - W0) * K * SC + 84, 1), round((N0 - lat) * SC + 24, 1)


TOWNS = {"Salt Lake City": (40.761, -111.891, "salt_lake_city/"), "St. George": (37.096, -113.568, "st_george/"), "Cedar City": (37.677, -113.062, "cedar_city/"),
         "Kanab": (37.047, -112.526, "kanab/"), "Duck Creek Village": (37.520, -112.660, "duck_creek_village/"), "Provo": (40.234, -111.659, "provo/"),
         "Ogden": (41.223, -111.974, "ogden/"), "Park City": (40.646, -111.498, "park_city/"), "Price": (39.599, -110.811, "price/"), "Herriman": (40.514, -112.033, "herriman/")}
LABEL = {"Salt Lake City": (-12, -6, "end"), "St. George": (-12, 4, "end"), "Cedar City": (-10, 4, "end"), "Kanab": (10, 16, "start"), "Duck Creek Village": (10, 2, "start"),
         "Provo": (12, 10, "start"), "Ogden": (12, 4, "start"), "Park City": (12, 2, "start"), "Price": (10, 4, "start"), "Herriman": (-10, 12, "end")}
I15 = [(37.0, -113.75), (37.096, -113.568), (37.677, -113.062), (38.276, -112.641), (38.969, -112.323), (39.710, -111.836), (40.234, -111.659), (40.514, -111.89),
       (40.761, -111.891), (41.223, -111.974), (41.510, -112.015), (42.0, -112.25)]


def utah_map(p="um", link=True):
    border = [(42, -114.052), (42, -111.047), (41, -111.047), (41, -109.041), (37, -109.041), (37, -114.052)]
    poly = " ".join("%s,%s" % P(a, b) for a, b in border)
    road = " ".join("%s,%s" % P(a, b) for a, b in I15)
    w, h = P(37, -109.041)[0] + 40, P(37, -109.041)[1] + 60
    grat = "".join(f'<path d="M{P(lat, -114.052)[0]} {P(lat, -114.052)[1]} H{P(lat, -109.041)[0]}" class="m-grat"/><text x="{P(lat, -109.041)[0] + 4}" y="{P(lat, -109.041)[1] + 3}" class="m-xs">{lat}&deg;N</text>' for lat in (38, 39, 40, 41))
    towns = []
    for n, (la, lo, path) in TOWNS.items():
        x, y = P(la, lo); dx, dy, anc = LABEL[n]
        office = n in ("Salt Lake City", "St. George")
        dot = f'<rect x="{x - 7}" y="{y - 7}" width="14" height="14" class="m-office"/>' if office else f'<circle cx="{x}" cy="{y}" r="5" class="m-town"/>'
        lab = f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anc}" class="m-lab{" m-off" if office else ""}">{n}</text>'
        towns.append(f'<a href="@/{path}">{dot}{lab}</a>' if link else dot + lab)
    ox, oy = P(40.297, -111.695)
    return f'''<svg class="map" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{p}t"><title id="{p}t">Map of Utah with Superior Foundation Repair's offices in Salt Lake City and St. George and the cities they serve along I-15, from Ogden to Kanab</title>
<polygon points="{poly}" class="m-land"/>{grat}
<polyline points="{road}" class="m-road"/><text x="{P(38.6, -112.5)[0] + 6}" y="{P(38.6, -112.5)[1]}" class="m-xs m-roadlab">I-15</text>
<circle cx="{ox}" cy="{oy}" r="9" class="m-case"/><text x="{ox - 14}" y="{oy + 16}" text-anchor="end" class="m-xs">Orem case study</text>
{"".join(towns)}
<text x="{P(41.6, -113.9)[0]}" y="{P(41.6, -113.9)[1]}" class="m-big">UTAH</text>
<g transform="translate(84,{h - 22})"><rect width="12" height="12" class="m-office"/><text x="18" y="10" class="m-xs">Office</text><circle cx="96" cy="6" r="5" class="m-town"/><text x="108" y="10" class="m-xs">City page</text></g>
</svg>'''


def pier_section(p="ps"):
    s = 8  # px per foot
    g = 96  # grade y
    ft = lambda f: g + f * s
    ticks = "".join(f'<path d="M48 {ft(f)} h{10 if f % 10 == 0 else 5}" class="d-ink"/>' + (f'<text x="42" y="{ft(f) + 4}" text-anchor="end" class="d-xs">{f} ft</text>' if f % 10 == 0 else "") for f in range(0, 46, 5))
    piers = "".join(f'<path d="M{x} {ft(2)} V{ft(d)}" class="d-pier"/>' + "".join(f'<ellipse cx="{x}" cy="{ft(d) - k * 10}" rx="9" ry="2.6" class="d-helix"/>' for k in (0, 1, 2)) for x, d in ((250, 36.5), (330, 43), (410, 34)))
    return f'''<svg class="drawing" viewBox="0 0 560 500" role="img" aria-labelledby="{p}t"><title id="{p}t">Section through the Orem case study: wet lake-bed sediment and a natural spring under the house, helical piers driven 33 to 40 feet and as deep as 43 feet to load-bearing soil, after one corner had sunk 11 inches</title>
<rect width="560" height="500" class="d-sheet"/>
<rect x="60" y="{g}" width="480" height="{ft(30) - g}" class="d-wet"/>
<rect x="60" y="{ft(30)}" width="480" height="{ft(45) - ft(30)}" class="d-firm"/>
<rect x="60" y="{ft(33)}" width="480" height="{ft(40) - ft(33)}" class="d-band"/>
<path d="M60 {ft(18)} q60 -10 120 0 t120 0 t120 0 t120 0" class="d-water"/><text x="70" y="{ft(18) + 18}" class="d-xs">natural spring / high water table</text>
<text x="70" y="{ft(6)}" class="d-lab">LAKE-BED SEDIMENT</text><text x="70" y="{ft(6) + 16}" class="d-xs">wet, "smelled like a swamp"</text>
<text x="70" y="{ft(41.5)}" class="d-lab">COMPETENT SOIL</text>
<text x="534" y="{ft(36.8)}" text-anchor="end" class="d-xs">typical pier depth 33&ndash;40 ft</text>
<path d="M60 {g} H540" class="d-grade"/>
<rect x="200" y="{g - 64}" width="260" height="64" class="d-house"/><path d="M190 {g - 64} L330 {g - 104} L470 {g - 64}" class="d-roof"/>
<path d="M200 {g} L200 {g + 22} L460 {g + 14} L460 {g}" class="d-found"/>
<path d="M470 {g + 2} v12" class="d-dim"/><text x="476" y="{g + 14}" class="d-xs">11 in.</text>
{piers}
<path d="M330 {ft(43)} h70" class="d-dim"/><text x="404" y="{ft(43) + 4}" class="d-xs">deepest: 43 ft</text>
<path d="M54 {g} V{ft(45)}" class="d-ink"/>{ticks}
<text x="70" y="490" class="d-xs">CASE 01 &middot; ARTESIAN ROAD, OREM &middot; 23 HELICAL PIERS &middot; NOT TO SCALE HORIZONTALLY</text>
</svg>'''
