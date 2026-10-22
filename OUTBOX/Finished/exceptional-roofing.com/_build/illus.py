"""Original drawings for exceptional-roofing.com: "Material specimen board".
swatch(kind): a square specimen of each roofing material the client installs, drawn as its real surface pattern
(architectural shingle courses with offset tabs, standing seam ribs, hand-split cedar shake, copper with a patina edge,
TPO membrane with heat-welded seams). Colours are fixed (they depict materials), so the drawings read the same in both themes."""
import random


def _wrap(p, title, inner):
    return f'<svg class="swatch" viewBox="0 0 240 240" role="img" aria-labelledby="{p}t"><title id="{p}t">{title}</title>{inner}</svg>'


def swatch(kind, p=None):
    p = p or "sw-" + kind
    rnd = random.Random(kind)
    if kind == "asphalt":
        rows = []
        for r, y in enumerate(range(-10, 250, 34)):
            off = (r % 2) * 22 + rnd.randint(-6, 6)
            x = -off
            while x < 250:
                w = rnd.choice((36, 44, 52, 30))
                shade = rnd.choice(("#3b3f45", "#44484f", "#33373c", "#4c5057", "#2e3236"))
                rows.append(f'<rect x="{x}" y="{y}" width="{w - 2}" height="32" fill="{shade}"/>')
                x += w
            rows.append(f'<rect x="0" y="{y + 30}" width="240" height="4" fill="#1d2023" opacity=".55"/>')
        inner = '<rect width="240" height="240" fill="#2a2d31"/>' + "".join(rows) + "".join(f'<circle cx="{rnd.randint(0,240)}" cy="{rnd.randint(0,240)}" r=".9" fill="#7c8088"/>' for _ in range(160))
        return _wrap(p, "Architectural asphalt shingles", inner)
    if kind == "metal":
        ribs = "".join(f'<rect x="{x}" y="0" width="58" height="240" fill="url(#{p}g)"/><rect x="{x + 56}" y="0" width="6" height="240" fill="#16191c"/><rect x="{x + 57}" y="0" width="2" height="240" fill="#7d858c"/>' for x in range(-20, 240, 62))
        inner = f'<defs><linearGradient id="{p}g" x1="0" x2="1"><stop offset="0" stop-color="#3a4046"/><stop offset=".55" stop-color="#4a5158"/><stop offset="1" stop-color="#30353a"/></linearGradient></defs>{ribs}'
        return _wrap(p, "Standing seam metal panels", inner)
    if kind == "shake":
        rows = []
        for r, y in enumerate(range(-20, 250, 30)):
            x = -rnd.randint(0, 30)
            while x < 250:
                w = rnd.randint(18, 40)
                c = rnd.choice(("#9a6a3f", "#a8744a", "#8b5d36", "#b07d52", "#7f5532"))
                rows.append(f'<path d="M{x} {y} h{w - 2} l{rnd.randint(-2, 2)} 34 h-{w - 2}z" fill="{c}"/>' + "".join(f'<path d="M{x + rnd.randint(3, w - 4)} {y + 3} v{rnd.randint(14, 28)}" stroke="#5e3f24" stroke-width=".7" opacity=".55"/>' for _ in range(3)))
                x += w
            rows.append(f'<rect x="0" y="{y + 32}" width="240" height="3" fill="#4a3018" opacity=".6"/>')
        return _wrap(p, "Hand-split cedar shake", '<rect width="240" height="240" fill="#6e4a2c"/>' + "".join(rows))
    if kind == "copper":
        seams = "".join(f'<rect x="{x}" y="0" width="3" height="240" fill="#7a3f1d" opacity=".7"/>' for x in range(38, 240, 48))
        inner = (f'<defs><linearGradient id="{p}c" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d9915a"/><stop offset=".45" stop-color="#b8693a"/><stop offset=".8" stop-color="#9b5530"/><stop offset="1" stop-color="#5f9c86"/></linearGradient>'
                 f'<linearGradient id="{p}v" x1="0" y1="0" x2="0" y2="1"><stop offset=".7" stop-color="#5f9c86" stop-opacity="0"/><stop offset="1" stop-color="#5f9c86" stop-opacity=".85"/></linearGradient></defs>'
                 f'<rect width="240" height="240" fill="url(#{p}c)"/>{seams}<rect width="240" height="240" fill="url(#{p}v)"/>' +
                 "".join(f'<path d="M0 {y} H240" stroke="#f0b98a" stroke-width=".6" opacity=".35"/>' for y in range(20, 240, 40)))
        return _wrap(p, "Copper roofing with a patina edge", inner)
    if kind == "tpo":
        seams = "".join(f'<path d="M0 {y} H240" stroke="#c9ced3" stroke-width="7"/><path d="M0 {y + 4} H240" stroke="#aeb4ba" stroke-width="1.2" stroke-dasharray="2 3"/>' for y in (70, 160))
        inner = '<rect width="240" height="240" fill="#e9ecef"/>' + seams + "".join(f'<circle cx="{rnd.randint(0,240)}" cy="{rnd.randint(0,240)}" r="{rnd.choice((.8, 1.2))}" fill="#c3c8cd"/>' for _ in range(90)) + \
            '<circle cx="180" cy="200" r="16" fill="#dfe3e7" stroke="#aeb4ba" stroke-width="2"/><circle cx="180" cy="200" r="6" fill="#8d949b"/>'
        return _wrap(p, "TPO membrane with heat-welded seams and a drain", inner)
    return ""


MATERIALS = [("asphalt", "Asphalt shingle", "GAF Timberline HDZ, CertainTeed Landmark, CertainTeed Presidential TL, GAF Grand Sequoia", "asphalt-roofing/"),
             ("metal", "Standing seam metal", "Concealed fasteners; custom corrugated; CMG Metals colors and finishes", "metal-roofing/"),
             ("shake", "Wood shake", "Cedar shake and wood shingle, including historic-style homes", "roof-replacement/"),
             ("copper", "Copper", "Custom copper roofs and details, chimney caps, flashing and trim", "metal-roofing/"),
             ("tpo", "TPO / PVC", "GAF EverGuard TPO and PVC for flat and low-slope roofs", "tpo-roofing/")]
