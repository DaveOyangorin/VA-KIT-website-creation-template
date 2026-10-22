"""Original drawings for utahroofingpros.com: the service-area map (52 cities plotted from approximate coordinates, the office
marked, an approximate I-15 line for orientation), the sun-over-ridge mark from the logo, and a vent diagram for the blog post."""
from cfg import REGIONS

W, LON0, LON1, LAT0, LAT1 = 420, -112.36, -111.34, 40.07, 41.36
K = W / (LON1 - LON0)
H = round((LAT1 - LAT0) * K * 1.32)
RCOL = ["r0", "r1", "r2", "r3", "r4"]
I15 = [(41.223, -111.974), (41.162, -112.000), (41.060, -111.971), (40.980, -111.900), (40.889, -111.895), (40.849, -111.907), (40.761, -111.905),
       (40.667, -111.902), (40.611, -111.903), (40.540, -111.893), (40.470, -111.905), (40.392, -111.851), (40.377, -111.796), (40.297, -111.712),
       (40.234, -111.672), (40.165, -111.625), (40.115, -111.640)]


def xy(lat, lon):
    return round((lon - LON0) * K, 1), round((LAT1 - lat) * K * 1.32, 1)


def map_svg(highlight=None, labels=True, link=True):
    """highlight = a city slug to mark; link wraps each dot in an @/ link to its page."""
    road = " ".join(f"{x},{y}" for x, y in (xy(a, b) for a, b in I15))
    dots, labs = [], []
    big = {"salt-lake-city", "ogden", "provo", "park-city", "tooele", "lehi", "sandy", "layton", "heber-city", "herriman"}
    for ri, (reg, cities) in enumerate(REGIONS):
        for slug, name, lat, lon in cities:
            x, y = xy(lat, lon)
            on = " on" if slug == highlight else ""
            c = f'<circle class="dot {RCOL[ri]}{on}" cx="{x}" cy="{y}" r="{9 if on else 6.2}"><title>{name}</title></circle>'
            dots.append(f'<a href="@/service-areas/{slug}/" data-r="{ri}" aria-label="{name}">{c}</a>' if link else f'<g data-r="{ri}">{c}</g>')
            if labels and (slug in big or on) and slug != "cottonwood-heights":
                anchor = "end" if lon < -112.0 else "start"
                dx = -11 if anchor == "end" else 11
                labs.append(f'<text class="ml{on}" x="{x + dx}" y="{y + 4}" text-anchor="{anchor}">{name}</text>')
    ox, oy = xy(40.620, -111.810)
    office = (f'<g class="office"><circle cx="{ox}" cy="{oy}" r="13" class="halo"/><path d="M{ox - 8} {oy + 4} L{ox} {oy - 5} L{ox + 8} {oy + 4}" class="roof"/>'
              f'<text class="ml office-l" x="{ox + 17}" y="{oy + 5}">Cottonwood Heights office</text></g>')
    return (f'<svg class="map" viewBox="-80 -16 {W + 175} {H + 34}" role="img" aria-label="Map of the 52 Utah cities Utah Roofing Pros serves, from North Ogden to Spanish Fork, with the office in Cottonwood Heights">'
            f'<polyline class="road" points="{road}"/><text class="road-l" x="{xy(40.50, -111.905)[0] - 8}" y="{xy(40.50, -111.905)[1]}" text-anchor="end">I-15</text>'
            + "".join(dots) + "".join(labs) + office + "</svg>")


def sun(cls="sun"):
    """The logo's idea, redrawn: a sun rising behind three roof chevrons."""
    return (f'<svg class="{cls}" viewBox="0 0 240 130" aria-hidden="true"><path d="M30 120 A90 90 0 0 1 210 120" class="disc"/>'
            '<path d="M8 128 L120 52 L232 128" class="ch"/><path d="M40 128 L120 74 L200 128" class="ch"/><path d="M72 128 L120 96 L168 128" class="ch"/></svg>')


def vents():
    """Attic section: intake at the eaves, exhaust at the ridge, air path between."""
    return '''<figure class="diagram"><svg viewBox="0 0 640 300" role="img" aria-label="Attic cross-section: outside air enters at soffit vents, rises under the roof deck past baffles and leaves through a ridge vent">
<path d="M20 230 L320 40 L620 230" class="deck"/><path d="M60 230 L580 230" class="ceil"/>
<path d="M90 236 h460" class="ins"/>
<path d="M58 222 L110 190" class="baffle"/><path d="M582 222 L530 190" class="baffle"/>
<path d="M300 40 h40" class="ridge"/>
<path d="M40 246 C70 236 90 214 120 196 S240 120 300 80 L318 50" class="air"/><path d="M600 246 C570 236 550 214 520 196 S400 120 340 80 L322 50" class="air"/>
<path d="M318 50 L318 18" class="air out"/><path d="M322 50 L322 18" class="air out"/>
<text x="24" y="276">Intake: soffit vents</text><text x="616" y="276" text-anchor="end">Intake: soffit vents</text>
<text x="320" y="12" text-anchor="middle">Exhaust: ridge vent</text>
<text x="320" y="252" text-anchor="middle">Insulation on the attic floor, air sealed below</text>
<text x="128" y="182">Baffle keeps the path open</text>
</svg><figcaption>A balanced attic: air comes in low at the eaves and leaves high at the ridge. Drawing for illustration, not to scale.</figcaption></figure>'''
