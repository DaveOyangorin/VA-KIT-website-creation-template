"""Original drawings for the dryhouse.com redesign, drawn like sheets in a construction submittal: hatched concrete, soil
stipple, leader lines and numbered callout bubbles. Every number on them comes from the client's own pages (coating mils,
hydrostatic head per product, Warm-N-Dri R-values) or from the Utah edition of the IRC (6 in. of fall in the first 10 ft).
Colours come from CSS classes (style.css) so the drawings follow the page theme."""


def _defs(p):
    return f'''<defs>
<pattern id="{p}conc" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" class="f-conc"/><path d="M0 14 14 0" class="l-hatch"/><circle cx="4" cy="4" r=".9" class="f-dot"/><circle cx="10" cy="9" r=".7" class="f-dot"/></pattern>
<pattern id="{p}soil" width="22" height="22" patternUnits="userSpaceOnUse"><rect width="22" height="22" class="f-soil"/><circle cx="4" cy="6" r="1.1" class="f-grain"/><circle cx="15" cy="3" r=".8" class="f-grain"/><circle cx="11" cy="15" r="1.3" class="f-grain"/><circle cx="19" cy="18" r=".8" class="f-grain"/><circle cx="3" cy="19" r=".7" class="f-grain"/></pattern>
<pattern id="{p}board" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" class="f-board"/><path d="M0 3h6" class="l-board"/></pattern>
</defs>'''


def _bubble(x, y, n, tx, ty):
    return (f'<path d="M{x} {y} L{tx} {ty}" class="l-lead"/><circle cx="{tx}" cy="{ty}" r="3" class="f-ink"/>'
            f'<circle cx="{x}" cy="{y}" r="13" class="callout"/><text x="{x}" y="{y + 4.5}" text-anchor="middle" class="t-n">{n}</text>')


SECTION_KEY = [("EnviroDri weather-resistant barrier", "services/above-grade/envirodri/", "Above grade"),
               ("Waterproofing membrane on the wall", "services/belowgrade/waterproofing/", "07 14 00"),
               ("Drainage and insulation board", "services/belowgrade/foundation-insulation/", "07 21 00"),
               ("Strip drain at the footing", "services/belowgrade/foundation-drains/", "33 46 00"),
               ("Under-slab barrier (Paraseal)", "services/horizontal-services/under-slab/", "Horizontal"),
               ("Grade sloped away from the wall", "blog/before-you-backfill-foundation-checklist/", "IRC R401.3")]


def wall_section(p="ws"):
    """Below-grade wall section, exterior on the left, basement on the right, with the client's system layers numbered."""
    return f'''<svg class="drawing" viewBox="0 0 640 500" role="img" aria-labelledby="{p}t"><title id="{p}t">Section through a basement wall showing a weather barrier above grade, waterproofing membrane, drainage board, strip drain at the footing, under-slab barrier and grade sloped away from the house</title>{_defs(p)}
<rect x="0" y="0" width="640" height="500" class="f-sheet"/>
<path d="M0 150 L282 128 L282 500 L0 500Z" fill="url(#{p}soil)"/>
<rect x="340" y="404" width="300" height="96" fill="url(#{p}soil)"/>
<rect x="250" y="440" width="150" height="40" fill="url(#{p}conc)" class="l-ink"/>
<rect x="300" y="72" width="40" height="368" fill="url(#{p}conc)" class="l-ink"/>
<rect x="340" y="384" width="300" height="20" fill="url(#{p}conc)" class="l-ink"/>
<path d="M340 407 H640" class="l-barrier"/>
<rect x="296" y="128" width="4" height="312" class="f-memb"/>
<rect x="282" y="140" width="14" height="300" fill="url(#{p}board)" class="l-thin"/>
<rect x="238" y="420" width="12" height="60" class="f-drain"/><path d="M238 432h12M238 444h12M238 456h12M238 468h12" class="l-thin"/>
<path d="M300 20 V72" class="l-wrb"/><rect x="300" y="20" width="40" height="52" class="f-frame"/><path d="M296 20 V128" class="l-wrb2"/>
<path d="M0 150 L282 128" class="l-grade"/>
<path d="M60 168 L258 152" class="l-dim"/><path d="M60 162v12M258 146v12" class="l-dim"/>
<text x="70" y="190" class="t-s">6 in. fall in the first 10 ft</text>
<path d="M352 270 h40 M372 250 v40" class="l-faint"/>
<text x="420" y="250" class="t-lab">BASEMENT</text><text x="420" y="268" class="t-s">finished space stays dry</text>
<text x="18" y="236" class="t-lab">BACKFILL</text><text x="18" y="254" class="t-s">exterior soil</text>
<path d="M330 404 v76 M326 400 h18" class="l-faint"/>
<text x="604" y="492" text-anchor="end" class="t-s">SECTION A &middot; NOT TO SCALE</text>
{_bubble(212, 52, 1, 296, 52)}{_bubble(212, 108, 2, 298, 200)}{_bubble(150, 300, 3, 288, 300)}{_bubble(170, 400, 4, 242, 440)}{_bubble(560, 452, 5, 520, 407)}{_bubble(40, 120, 6, 120, 143)}
</svg>'''


def mil_gauge(p="mg"):
    """Coating thickness at 4 px per mil: damp proofing 10-20 mils vs waterproofing 40 to 80+ mils (client's below-grade page)."""
    rows = [("Damp proofing", 10, 20, "10&ndash;20 mils", "Vapor retarder. Cracks with the concrete."),
            ("Waterproofing, minimum", 40, 40, "40 mils", "Rubber-modified. Stretches over cracks."),
            ("Waterproofing, heavy", 80, 80, "80+ mils", "Custom homes and high water pressure.")]
    out = []
    for i, (lab, a, b, num, note) in enumerate(rows):
        y = 70 + i * 92
        out.append(f'<rect x="40" y="{y}" width="70" height="56" fill="url(#{p}conc)" class="l-ink"/>')
        if a != b:
            out.append(f'<rect x="110" y="{y}" width="{a * 4}" height="56" class="f-memb"/><rect x="{110 + a * 4}" y="{y}" width="{(b - a) * 4}" height="56" class="f-memb2"/>')
        else:
            out.append(f'<rect x="110" y="{y}" width="{a * 4}" height="56" class="f-memb"/>')
        out.append(f'<text x="{122 + b * 4 + (6 if b < 80 else 0)}" y="{y + 24}" class="t-big">{num}</text><text x="{122 + b * 4}" y="{y + 44}" class="t-s">{lab}</text>' if b < 60 else
                   f'<text x="122" y="{y + 24}" class="t-big inv">{num}</text><text x="122" y="{y + 44}" class="t-s inv">{lab}</text>')
        out.append(f'<text x="40" y="{y + 74}" class="t-xs">{note}</text>')
    ticks = "".join(f'<path d="M{110 + m * 4} 44 v{10 if m % 20 == 0 else 5}" class="l-ink"/>' + (f'<text x="{110 + m * 4}" y="38" text-anchor="middle" class="t-xs">{m}</text>' if m % 20 == 0 else "") for m in range(0, 101, 10))
    return f'''<svg class="drawing" viewBox="0 0 560 360" role="img" aria-labelledby="{p}t"><title id="{p}t">Coating thickness drawn to scale: damp proofing 10 to 20 mils, waterproofing 40 mils minimum and up to 80 mils or more; a credit card is about 30 mils thick</title>{_defs(p)}
<rect width="560" height="360" class="f-sheet"/>
<text x="40" y="22" class="t-lab">COATING THICKNESS &middot; MILS (1 mil = 1/1000 in.)</text>
<path d="M110 54 H510" class="l-ink"/>{ticks}
<path d="M230 56 V340" class="l-ref"/><text x="236" y="350" class="t-xs">a credit card &asymp; 30 mils</text>
{"".join(out)}
</svg>'''


HEAD = [("Damp Proof", 0, "0 ft", "$", "Slab on grade / crawlspace (unconditioned)", "Minimum (code)"),
        ("Watchdog H3", 3, "3 ft", "$$", "Basement (8&ndash;12 ft deep) / crawlspace (conditioned)", "Finished space"),
        ("Tuff-N-Dri QC", 12, "8 ft / 12 ft", "$$$", "Basement (custom) / commercial", "Premium")]


def head_columns(p="hc"):
    """Hydrostatic head each coating resists, from the client's comparison chart (0 ft, 3 ft, 8 ft / 12 ft)."""
    s = 22  # px per foot
    base = 320
    cols = []
    for i, (name, ft, lab, cost, use, lvl) in enumerate(HEAD):
        x = 120 + i * 140
        h = ft * s
        cols.append(f'<rect x="{x}" y="{base - 12 * s}" width="70" height="{12 * s}" class="f-tube"/>')
        if ft:
            if name.startswith("Tuff"):
                cols.append(f'<rect x="{x}" y="{base - h}" width="70" height="{h - 8 * s}" class="f-water2"/><rect x="{x}" y="{base - 8 * s}" width="70" height="{8 * s}" class="f-water"/>')
            else:
                cols.append(f'<rect x="{x}" y="{base - h}" width="70" height="{h}" class="f-water"/>')
        cols.append(f'<rect x="{x}" y="{base - 12 * s}" width="70" height="{12 * s}" class="l-ink" fill="none"/>')
        cols.append(f'<text x="{x + 35}" y="{base - h - 10}" text-anchor="middle" class="t-big">{lab}</text>')
        cols.append(f'<text x="{x + 35}" y="{base + 22}" text-anchor="middle" class="t-lab">{name}</text><text x="{x + 35}" y="{base + 40}" text-anchor="middle" class="t-xs">{cost}</text>')
    ticks = "".join(f'<path d="M72 {base - f * s} h{12 if f % 4 == 0 else 6}" class="l-ink"/>' + (f'<text x="64" y="{base - f * s + 4}" text-anchor="end" class="t-xs">{f} ft</text>' if f % 4 == 0 else "") for f in range(0, 13))
    return f'''<svg class="drawing" viewBox="0 0 560 380" role="img" aria-labelledby="{p}t"><title id="{p}t">Water pressure each coating is rated to hold back at a crack, as feet of water: damp proofing 0 ft, Watchdog H3 3 ft, Tuff-N-Dri QC 8 ft or 12 ft</title>
<rect width="560" height="380" class="f-sheet"/>
<text x="20" y="22" class="t-lab">HYDROSTATIC HEAD &middot; FEET OF WATER AT A CRACK</text>
<path d="M84 {base - 12 * s} V{base} H540" class="l-ink"/>{ticks}
{"".join(cols)}
</svg>'''


LEAKS = [("Crack under a window", "services/leak-repair/foundation-cracks/"),
         ("Form ties", "services/leak-repair/ties/"),
         ("Cold joint", "services/leak-repair/cold-joints/"),
         ("Honeycomb (rock pocket)", "services/leak-repair/honeycomb/"),
         ("Floor joint", "services/leak-repair/floor-joints/"),
         ("Pipe penetration", "services/leak-repair/pipe-penetrations/")]


def leak_elevation(p="le"):
    """Interior elevation of a basement wall with the six leak points the client describes, callout-numbered."""
    ties = "".join(f'<circle cx="{x}" cy="{y}" r="3.2" class="f-tie"/>' for x in range(70, 600, 80) for y in (80, 160, 240, 320) if not (380 <= x <= 540 and y <= 120))
    comb = "".join(f'<path d="M{x} {y} l5 -3 l5 3 l-1 6 l-8 1z" class="f-comb"/>' for x, y in [(130, 286), (142, 280), (152, 290), (138, 296), (126, 298), (160, 284), (148, 302), (118, 288), (166, 296)])
    return f'''<svg class="drawing" viewBox="0 0 640 420" role="img" aria-labelledby="{p}t"><title id="{p}t">Inside view of a basement wall marking where leaks start: a crack below a window, form ties, a cold joint, honeycomb, the floor joint and a pipe penetration</title>{_defs(p)}
<rect width="640" height="420" class="f-sheet"/>
<rect x="20" y="30" width="600" height="320" fill="url(#{p}conc)" class="l-ink"/>
<rect x="400" y="30" width="120" height="84" class="f-sheet l-ink"/><path d="M400 72 h120 M460 30 v84" class="l-thin"/>
{ties}
<path d="M402 114 l-6 30 l8 22 l-10 34 l6 26 l-9 38 l5 36 l-7 40" class="l-crack"/>
<path d="M20 206 H330" class="l-joint"/><path d="M20 211 H330" class="l-joint2"/>
{comb}
<rect x="0" y="350" width="640" height="40" fill="url(#{p}conc)" class="l-ink"/><path d="M20 350 H620" class="l-wet"/>
<path d="M90 352 q4 10 0 14 q-4 -4 0 -14z M250 352 q4 10 0 14 q-4 -4 0 -14z M470 352 q4 10 0 14 q-4 -4 0 -14z" class="f-water"/>
<rect x="540" y="276" width="60" height="16" class="f-pipe l-ink"/><circle cx="560" cy="284" r="14" class="f-pipe l-ink"/><circle cx="560" cy="284" r="6" class="f-sheet l-ink"/>
<text x="20" y="410" class="t-s">INTERIOR ELEVATION &middot; BASEMENT WALL</text>
{_bubble(350, 140, 1, 400, 160)}{_bubble(230, 132, 2, 230, 160)}{_bubble(90, 180, 3, 120, 206)}{_bubble(200, 250, 4, 160, 286)}{_bubble(330, 316, 5, 330, 350)}{_bubble(588, 236, 6, 566, 272)}
</svg>'''
