"""Original drawings for armour-crete.com: "Sealed for the desert".
texture(kind): concrete finishes as drawn surfaces (broom finish, exposed aggregate, wet-look sheen, pool deck coping, sawn joint,
blacktop). slab(state): the client's own explanation of why concrete fails, drawn as a cross-section of a slab:
moves (thermal expansion arrows), drinks (water wicking into pores), breaks (ice and salt crystals pushing out), sealed (drops beading).
The 5.5 millionths of an inch per inch per degree F figure and the 1/3 in. on a 50 ft driveway are from the client's home page."""
import random


def _svg(p, title, inner, vb="0 0 400 300", cls="tex"):
    return f'<svg class="{cls}" viewBox="{vb}" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="{p}t"><title id="{p}t">{title}</title>{inner}</svg>'


def texture(kind, p=None):
    p = p or "tx-" + kind
    rnd = random.Random(kind)
    if kind == "broom":
        lines = "".join(f'<path d="M{x} 0 q {rnd.uniform(-6, 6):.1f} 150 {rnd.uniform(-4, 4):.1f} 300" stroke="#9a948c" stroke-width="{rnd.uniform(.4, 1.2):.2f}" opacity=".55" fill="none"/>' for x in range(0, 400, 5))
        return _svg(p, "Broom-finished concrete", f'<rect width="400" height="300" fill="#c9c3b8"/>{lines}<path d="M0 150 H400" stroke="#8f887e" stroke-width="3"/>')
    if kind == "aggregate":
        dots = "".join(f'<ellipse cx="{rnd.randint(0, 400)}" cy="{rnd.randint(0, 300)}" rx="{rnd.uniform(3, 9):.1f}" ry="{rnd.uniform(2.5, 7):.1f}" fill="{rnd.choice(("#8a6f5a", "#a48a72", "#6f6259", "#c2a98e", "#5d544e", "#b9926f"))}" transform="rotate({rnd.randint(0, 180)})"/>' for _ in range(520))
        return _svg(p, "Exposed aggregate concrete", f'<rect width="400" height="300" fill="#b5ab9e"/>{dots}')
    if kind == "wetlook":
        dots = "".join(f'<ellipse cx="{rnd.randint(0, 400)}" cy="{rnd.randint(0, 300)}" rx="{rnd.uniform(3, 9):.1f}" ry="{rnd.uniform(2.5, 7):.1f}" fill="{rnd.choice(("#5a4535", "#7a5f48", "#3f3530", "#9a7c60", "#2f2925", "#8a6440"))}"/>' for _ in range(520))
        return _svg(p, "Wet-look sealed concrete with deepened colour", f'<defs><linearGradient id="{p}g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/><stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset=".7" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs><rect width="400" height="300" fill="#6e5d50"/>{dots}<rect width="400" height="300" fill="url(#{p}g)"/>')
    if kind == "pool":
        ripples = "".join(f'<path d="M0 {y} q 50 -8 100 0 t 100 0 t 100 0 t 100 0" stroke="#e8f6f8" stroke-width="1.4" opacity=".55" fill="none"/>' for y in range(30, 130, 18))
        return _svg(p, "Pool deck beside salt water", f'<rect width="400" height="300" fill="#d8cbb6"/><rect width="400" height="140" fill="#3a9bb0"/>{ripples}<rect y="140" width="400" height="22" fill="#efe6d6"/><path d="M0 162 H400" stroke="#b9ab94" stroke-width="2"/>' +
                    "".join(f'<circle cx="{rnd.randint(0, 400)}" cy="{rnd.randint(170, 300)}" r="{rnd.uniform(.8, 2):.1f}" fill="#fff" opacity=".8"/>' for _ in range(60)))
    if kind == "joint":
        grain = "".join(f'<circle cx="{rnd.randint(0, 400)}" cy="{rnd.randint(0, 300)}" r=".9" fill="#8f887e"/>' for _ in range(500))
        return _svg(p, "Expansion joint in a concrete slab", f'<rect width="400" height="300" fill="#cfc8bc"/>{grain}<rect x="188" y="0" width="24" height="300" fill="#3d3833"/><rect x="192" y="0" width="16" height="300" fill="#6b625a"/><path d="M200 0 V300" stroke="#2a2622" stroke-width="1"/>')
    if kind == "blacktop":
        grain = "".join(f'<circle cx="{rnd.randint(0, 400)}" cy="{rnd.randint(0, 300)}" r="{rnd.uniform(.6, 1.8):.1f}" fill="{rnd.choice(("#4a4a4a", "#6a6a66", "#2b2b2b", "#808078"))}"/>' for _ in range(900))
        return _svg(p, "Sealed asphalt blacktop", f'<rect width="400" height="300" fill="#1f1f1f"/>{grain}<path d="M0 230 H400" stroke="#e8c547" stroke-width="7" stroke-dasharray="60 40"/>')
    return ""


def slab(state, p=None):
    """Cross-section of a slab on its sub-base. state: moves | drinks | breaks | sealed."""
    p = p or "sl-" + state
    rnd = random.Random("slab")
    pores = [(rnd.randint(30, 370), rnd.randint(118, 196), rnd.uniform(2.5, 5)) for _ in range(46)]
    base = (f'<rect width="400" height="300" fill="#f7f1e8"/><rect x="0" y="210" width="400" height="90" fill="#d9c7a8"/>' +
            "".join(f'<circle cx="{rnd.randint(0, 400)}" cy="{rnd.randint(214, 298)}" r="{rnd.uniform(1, 3):.1f}" fill="#b49a76"/>' for _ in range(80)) +
            '<rect x="20" y="110" width="360" height="100" fill="#cfc6b8" stroke="#3a332d" stroke-width="2"/>')
    crack = '<path d="M196 110 l6 20 l-5 18 l7 22 l-4 18 l5 22" stroke="#3a332d" stroke-width="2" fill="none"/>'
    pore_fill = lambda wet: "".join(f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{"#3f8fb0" if wet else "#ffffff"}" stroke="#8a8075" stroke-width=".6"/>' for x, y, r in pores)
    if state == "moves":
        inner = base + pore_fill(False) + crack + '<path d="M24 90 H120 M24 90 l10 -6 M24 90 l10 6 M376 90 H280 M376 90 l-10 -6 M376 90 l-10 6" stroke="#b8502f" stroke-width="3" fill="none"/>' + \
            '<text x="200" y="70" text-anchor="middle" class="sl-t">100&deg;F swing &middot; about 1/3 in. on a 50 ft slab</text><text x="200" y="88" text-anchor="middle" class="sl-s">5.5 millionths of an inch, per inch, per &deg;F</text>'
        t = "A concrete slab expanding and contracting with temperature, opening a hairline crack"
    elif state == "drinks":
        drops = "".join(f'<path d="M{x} {y} q 5 8 0 12 q -5 -4 0 -12z" fill="#3f8fb0"/>' for x, y in ((120, 60), (200, 50), (280, 66), (196, 92), (150, 84), (250, 88)))
        inner = base + pore_fill(True) + crack + drops + '<path d="M199 110 V205" stroke="#3f8fb0" stroke-width="4" opacity=".7"/><text x="200" y="36" text-anchor="middle" class="sl-t">Water wicks into pores and cracks, carrying salt</text>'
        t = "Water soaking into the pores and the crack of an unsealed slab"
    elif state == "breaks":
        crystals = "".join(f'<path d="M{x} {y - 5} l3 5 l-3 5 l-3 -5z" fill="#ffffff" stroke="#6a8fa0" stroke-width=".8"/>' for x, y, r in pores[::2])
        flakes = '<path d="M60 110 l20 -14 l26 6 l10 8z M300 110 l16 -12 l24 4 l8 8z" fill="#cfc6b8" stroke="#3a332d" stroke-width="1.5"/>'
        inner = base + pore_fill(True) + crystals + crack + flakes + '<text x="200" y="40" text-anchor="middle" class="sl-t">Ice and salt crystals grow and push the surface off</text><text x="200" y="58" text-anchor="middle" class="sl-s">scaling &middot; spalling &middot; efflorescence</text>'
        t = "Ice and salt crystals growing in saturated pores and flaking the surface of the slab"
    else:
        beads = "".join(f'<ellipse cx="{x}" cy="104" rx="{r}" ry="{r * .62:.1f}" fill="#3f8fb0"/><ellipse cx="{x - r * .3:.1f}" cy="{104 - r * .25:.1f}" rx="{r * .3:.1f}" ry="{r * .18:.1f}" fill="#ffffff" opacity=".7"/>' for x, r in ((80, 9), (130, 6), (175, 11), (232, 7), (286, 10), (334, 6)))
        inner = base + pore_fill(False) + '<rect x="20" y="108" width="360" height="5" fill="#b8502f" opacity=".75"/>' + beads + '<text x="200" y="60" text-anchor="middle" class="sl-t">Sealed: the pores stay dry, water beads and runs off</text>'
        t = "A sealed slab with water beading on the surface and dry pores"
    return _svg(p, t, inner, cls="slab")


SERVICES = [("driveway-sealing/", "Driveway sealing", "broom", "DECO 20 Clear, penetrating, no film. Back on it in 24 hours."),
            ("wet-look-concrete-sealing/", "Wet-look &amp; decorative", "wetlook", "Colour deepened on purpose, aggregate lifted."),
            ("pool-deck-sealing/", "Pool decks &amp; salt", "pool", "Salt Shield 303 against the salt off the pool and the softener."),
            ("expansion-joint-replacement/", "Expansion joints", "joint", "Old filler cut out, channel cleaned, re-filled."),
            ("foundation-waterproofing/", "Foundation waterproofing", "aggregate", "Below grade, for new builds, on the build calendar."),
            ("asphalt-sealing/", "Asphalt sealing", "blacktop", "Bio Blacktop: natural oil, no asphalt, no tar.")]
