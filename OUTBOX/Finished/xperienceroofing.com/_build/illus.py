"""Original drawings for "The Collection": one profile drawing per Xperience signature system, and the Material World layer
stack. Generic profiles, drawn for this site."""


def profile(kind):
    s = '<svg class="prof" viewBox="0 0 420 220" aria-hidden="true">'
    if kind == "classic":  # architectural shingle courses, offset tabs
        for r in range(6):
            y = 40 + r * 26; off = (r % 2) * 22
            s += f'<path class="fl" d="M20 {y} H400 V{y + 30} H20 Z"/>'
            for x in range(20 + off, 400, 44):
                s += f'<path class="ln" d="M{x} {y} V{y + 26}"/><rect class="sh" x="{x + 4}" y="{y + 16}" width="18" height="10"/>'
            s += f'<path class="hv" d="M20 {y} H400"/>'
    elif kind == "standing":  # pans and raised seams
        s += '<path class="fl" d="M20 150 H400 V190 H20 Z"/>'
        d = "M20 150"
        for x in range(20, 400, 76): d += f" H{x + 64} V96 H{x + 74} V150"
        s += f'<path class="hv" d="{d} H400"/>'
        for x in range(84, 400, 76): s += f'<path class="ln" d="M{x} 96 L{x + 10} 96"/>'
    elif kind == "heritage":  # barrel tile waves
        for r in range(4):
            y = 70 + r * 36; d = f"M20 {y}"
            for x in range(20, 400, 40): d += f" Q{x + 20} {y - 34} {x + 40} {y}"
            s += f'<path class="fl" d="{d} V{y + 34} H20 Z"/><path class="hv" d="{d}"/>'
    elif kind == "summit":  # metal shake, staggered textured panels
        for r in range(5):
            y = 46 + r * 30; off = (r % 2) * 30
            for x in range(20 - off, 400, 60):
                s += f'<path class="fl" d="M{max(x, 20)} {y} H{min(x + 58, 400)} V{y + 28} H{max(x, 20)} Z"/>'
                s += f'<path class="ln" d="M{max(x + 8, 20)} {y + 8} H{min(x + 30, 400)} M{max(x + 20, 20)} {y + 18} H{min(x + 48, 400)}"/>'
            s += f'<path class="hv" d="M20 {y} H400"/>'
    elif kind == "flat":  # membrane over insulation, welded lap
        s += '<path class="deck" d="M20 160 H400 V180 H20 Z"/><path class="ins" d="M20 116 H400 V160 H20 Z"/>'
        s += '<path class="hv" d="M20 110 H240"/><path class="hv" d="M200 106 C214 106 218 110 224 110 H400"/><path class="weld" d="M200 104 H240 V112 H200 Z"/>'
    s += "</svg>"
    return s


def stack():
    """Material World: the three layers, exploded."""
    W, D = 300, 180
    iso = lambda x, y, z: (230 + (x - y) * .87, 150 + (x + y) * .5 - z)
    def slab(z, t, cls):
        P = lambda x, y, zz: "%.1f,%.1f" % iso(x, y, zz)
        return (f'<polygon class="{cls} t" points="{P(0,0,z+t)} {P(W,0,z+t)} {P(W,D,z+t)} {P(0,D,z+t)}"/>'
                f'<polygon class="{cls} r" points="{P(W,0,z+t)} {P(W,D,z+t)} {P(W,D,z)} {P(W,0,z)}"/>'
                f'<polygon class="{cls} f" points="{P(0,D,z+t)} {P(W,D,z+t)} {P(W,D,z)} {P(0,D,z)}"/>')
    s = '<svg class="stack" viewBox="0 0 760 420" role="img" aria-label="The three layers of a roof: flashing and trim, underlayment, surface">'
    s += slab(0, 10, "deck") + slab(70, 6, "under") + slab(150, 8, "surf")
    s += '<path class="trim" d="M%.1f %.1f L%.1f %.1f L%.1f %.1f" />' % (iso(0, D, 168) + iso(W, D, 168) + iso(W, 0, 168))
    lab = [("XP-MAT-001 &middot; SURFACE", 150), ("XP-MAT-002 &middot; UNDERLAYMENT", 70), ("XP-MAT-003 &middot; FLASHING &amp; TRIM", 172), ("DECK", 0)]
    for t, z in lab[:3]:
        x, y = iso(W, 0, z + 4)
        s += f'<path class="lead" d="M{x:.1f} {y:.1f} H{x + 24:.1f}"/><text x="{x + 30:.1f}" y="{y + 4:.1f}">{t}</text>'
    return s + "</svg>"
