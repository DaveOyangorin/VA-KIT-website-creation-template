"""Original cross-section drawings for davenportfoundationrepair.com, drawn like an engineer's section through the ground:
grade line, soil layers, depth marks in feet, the house wall and footing, and the repair the page is about.
section(kind): piers | anchors | drain | crawl | slab | helical | crack.   hero(): the whole house with numbered problem spots."""

W, H = 760, 400
G = 120  # grade line y


def _soil(depth=True):
    s = (f'<rect class="sky" x="0" y="0" width="{W}" height="{G}"/>'
         f'<rect class="top" x="0" y="{G}" width="{W}" height="40"/>'
         f'<rect class="clay" x="0" y="{G + 40}" width="{W}" height="150"/>'
         f'<rect class="firm" x="0" y="{G + 190}" width="{W}" height="{H - G - 190}"/>'
         f'<line class="grade" x1="0" y1="{G}" x2="{W}" y2="{G}"/>'
         f'<text class="lab soil-l" x="{W - 12}" y="{G + 26}" text-anchor="end">TOPSOIL</text>'
         f'<text class="lab soil-l" x="{W - 12}" y="{G + 120}" text-anchor="end">CLAY &amp; FILL SOILS</text>'
         f'<text class="lab soil-l" x="{W - 12}" y="{H - 24}" text-anchor="end">LOAD-BEARING STRATA</text>')
    if depth:
        for i, ft in enumerate(range(0, 16, 4)):
            y = G + i * 70
            s += f'<line class="tick" x1="0" y1="{y}" x2="14" y2="{y}"/><text class="lab dep" x="18" y="{y + 4}">{ft} FT</text>'
    for x, y in ((140, 240), (420, 200), (600, 280), (90, 330), (500, 350), (300, 330), (680, 220)):
        s += f'<circle class="pebble" cx="{x}" cy="{y}" r="3"/>'
    return s


def _house(slab=True, x0=230, x1=560):
    # basement wall + footing + floor slab + a wall stub above grade
    return (f'<rect class="wall" x="{x0}" y="40" width="18" height="{G - 40 + 150}"/>'
            f'<rect class="wall" x="{x1}" y="40" width="18" height="{G - 40 + 150}"/>'
            f'<rect class="foot" x="{x0 - 16}" y="{G + 150}" width="50" height="18"/><rect class="foot" x="{x1 - 16}" y="{G + 150}" width="50" height="18"/>'
            + (f'<rect class="slab" x="{x0 + 18}" y="{G + 138}" width="{x1 - x0 - 18}" height="12"/>' if slab else "")
            + f'<path class="roofl" d="M{x0 - 30} 44 L{(x0 + x1) // 2 + 9} 6 L{x1 + 48} 44"/>'
            f'<rect class="room" x="{x0 + 18}" y="{G + 6}" width="{x1 - x0 - 18}" height="{132}"/>'
            f'<text class="lab" x="{(x0 + x1) // 2 + 9}" y="{G + 70}" text-anchor="middle">BASEMENT</text>')


def _callout(x, y, n, text, tx, ty, anchor="start"):
    return (f'<line class="lead" x1="{x}" y1="{y}" x2="{tx}" y2="{ty}"/><circle class="dot" cx="{x}" cy="{y}" r="5"/>'
            f'<g class="cl"><rect x="{tx - (0 if anchor == "start" else 9 * len(text) + 34)}" y="{ty - 13}" width="{9 * len(text) + 34}" height="22" rx="2"/>'
            f'<text class="n" x="{tx + 8 - (0 if anchor == "start" else 9 * len(text) + 34)}" y="{ty + 3}">{n}</text>'
            f'<text class="ct" x="{tx + 24 - (0 if anchor == "start" else 9 * len(text) + 34)}" y="{ty + 3}">{text}</text></g>')


def section(kind, title=""):
    body, cap = "", ""
    if kind == "piers":
        body = _house()
        for x in (214, 584):
            body += f'<rect class="steel" x="{x - 4}" y="{G + 150}" width="8" height="{H - G - 150 - 34}"/><rect class="brkt" x="{x - 14}" y="{G + 140}" width="28" height="14"/>'
            body += f'<path class="arrow" d="M{x} {H - 52} l-8 -12 h16 z"/>'
        body += _callout(214, G + 148, "01", "BRACKET ON FOOTING", 20, 64) + _callout(584, H - 40, "02", "PIER DRIVEN TO FIRM SOIL", 420, H - 10 - 40, "start")
        cap = "Push piers: steel driven down to load-bearing soil, the weight of the house transferred onto them."
    elif kind == "anchors":
        body = _house()
        body = body.replace(f'<rect class="wall" x="230" y="40" width="18" height="{G - 40 + 150}"/>', f'<path class="wall bow" d="M230 40 h18 v80 q22 70 0 190 h-18 q22 -120 0 -190 z"/>')
        for y in (G + 50, G + 100):
            body += f'<line class="rod" x1="268" y1="{y}" x2="80" y2="{y + 6}"/><rect class="plate" x="262" y="{y - 14}" width="10" height="28"/><rect class="anchor" x="66" y="{y - 10}" width="16" height="32"/>'
        body += '<path class="arrow h" d="M150 210 l14 -8 v16 z"/>'
        body += _callout(266, G + 50, "01", "WALL PLATE", 300, 70) + _callout(74, G + 106, "02", "EARTH ANCHOR IN STABLE SOIL", 40, 372)
        cap = "Wall anchors: plates inside, anchors in stable soil outside, steel rods tightened to stabilize a bowing wall."
    elif kind == "drain":
        body = _house()
        body += f'<rect class="gravel" x="250" y="{G + 132}" width="34" height="22"/><circle class="pipe" cx="267" cy="{G + 143}" r="7"/>'
        body += f'<rect class="pit" x="470" y="{G + 120}" width="60" height="58"/><rect class="pump" x="488" y="{G + 146}" width="24" height="26"/><line class="dis" x1="500" y1="{G + 146}" x2="500" y2="{G - 20}"/><line class="dis" x1="500" y1="{G - 20}" x2="590" y2="{G - 20}"/>'
        for y in (G + 60, G + 100, G + 140):
            body += f'<path class="water" d="M150 {y} q30 -10 70 0"/><path class="arrow w" d="M226 {y} l-10 -6 v12 z"/>'
        body += _callout(267, G + 143, "01", "PERIMETER DRAIN IN GRAVEL", 20, 40) + _callout(500, G + 160, "02", "SUMP PIT AND PUMP", 600, 300)
        cap = "Interior drainage: water pressing in from the soil is collected at the wall base and pumped out."
    elif kind == "crawl":
        body = _soil() + (f'<rect class="wall" x="160" y="50" width="18" height="{G - 50 + 60}"/><rect class="wall" x="580" y="50" width="18" height="{G - 50 + 60}"/>'
                          f'<rect class="joist" x="160" y="{G - 10}" width="438" height="14"/><rect class="beam" x="178" y="{G + 4}" width="402" height="10"/>'
                          f'<rect class="crawlair" x="178" y="{G + 14}" width="402" height="56"/><path class="liner" d="M178 {G + 14} V{G + 70} H580 V{G + 14}"/>')
        for x in (270, 380, 490):
            body += f'<rect class="steel" x="{x - 4}" y="{G + 14}" width="8" height="52"/><rect class="brkt" x="{x - 12}" y="{G + 62}" width="24" height="8"/>'
        body += (f'<path class="roofl" d="M130 54 L389 12 L628 54"/>' + _callout(380, G + 30, "01", "STEEL SUPPORT JACKS", 40, 36)
                 + _callout(560, G + 70, "02", "SEALED VAPOR BARRIER", 470, 330))
        cap = "Crawl space: steel jacks support the floor beam; a sealed liner keeps ground moisture out."
        return _svg(body, cap)
    elif kind == "slab":
        body = _soil() + (f'<rect class="slab out" x="140" y="{G - 14}" width="480" height="18"/><path class="void" d="M300 {G + 4} q80 34 160 0 z"/>')
        for x in (330, 380, 430):
            body += f'<line class="port" x1="{x}" y1="{G - 30}" x2="{x}" y2="{G + 8}"/><path class="arrow" d="M{x} {G - 40} l-7 10 h14 z"/>'
        body += _callout(380, G + 14, "01", "VOID UNDER THE SLAB", 470, 210) + _callout(330, G - 30, "02", "SMALL INJECTION PORTS", 40, 40)
        cap = "Concrete lifting: foam injected through small ports fills the void and raises the slab back to level."
    elif kind == "helical":
        body = _soil() + f'<rect class="slab out" x="120" y="{G - 30}" width="520" height="30"/>'
        for x in (220, 380, 540):
            body += f'<rect class="steel" x="{x - 4}" y="{G}" width="8" height="{H - G - 40}"/>'
            for yy in (H - 90, H - 60):
                body += f'<ellipse class="helix" cx="{x}" cy="{yy}" rx="22" ry="6"/>'
        body += _callout(540, H - 60, "01", "HELICAL PLATES IN FIRM SOIL", 420, 60)
        cap = "Helical piles: steel shafts with helix plates screwed down to firm soil to carry new or existing structures."
    elif kind == "crack":
        body = _house() + '<path class="crackl" d="M239 70 l6 18 l-8 14 l9 20 l-7 18 l8 22 l-6 20"/>'
        body += '<path class="crackl" d="M300 258 l20 -3 l14 4 l22 -2"/>'
        body += _callout(242, 120, "01", "WALL CRACK", 300, 60) + _callout(330, 256, "02", "FLOOR CRACK", 420, 330)
        cap = "Cracks are symptoms: the pattern and width tell us whether the cause is settling, pressure or shrinkage."
    return _svg(_soil() + body if kind not in ("crawl", "slab", "helical") else body, cap)


def _svg(body, cap):
    return (f'<figure class="xsec"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{cap}">{body}</svg>'
            f'<figcaption><span class="mono">SECTION</span> {cap} Drawing not to scale.</figcaption></figure>')


SPOTS = [("01", "Settling foundation", "foundation-repair/foundation-problems/settlement-sinking.html", 214, 288),
         ("02", "Bowing wall", "foundation-repair/foundation-problems/bowing-walls.html", 239, 190),
         ("03", "Wet basement", "basement-waterproofing.html", 400, 252),
         ("04", "Sinking concrete", "concrete-leveling.html", 660, 112),
         ("05", "Wall crack", "foundation-repair/foundation-problems/wall-crack.html", 569, 160)]


def hero():
    b = _soil() + _house()
    b += '<path class="crackl" d="M575 120 l6 16 l-7 14 l8 18"/><rect class="slab out tilt" x="610" y="104" width="130" height="14" transform="rotate(5 610 110)"/>'
    b += '<path class="water" d="M150 220 q30 -10 70 0"/><path class="water" d="M150 250 q30 -10 70 0"/>'
    links = "".join(f'<a href="@/{p}" class="spot" aria-label="{t}"><circle cx="{x}" cy="{y}" r="15"/><text x="{x}" y="{y + 5}" text-anchor="middle">{n}</text></a>' for n, t, p, x, y in SPOTS)
    return f'<svg class="hero-x" viewBox="0 0 {W} {H}" role="img" aria-label="Cross-section of a Utah house and the ground below it, with five common foundation problems marked">{b}{links}</svg>'
