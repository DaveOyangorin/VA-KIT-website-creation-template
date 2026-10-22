"""Signature piece for the sandsroofingutah.com home page: "Layer by layer".

A drawn section through one slope of a gable roof at a 6/12 pitch (26.565 degrees). Dragging the handle up the slope builds the
roof the way a re-roof goes on: deck (after the tear-off), flashing and underlayment, shingles, ridge vent, final inspection. Each
stage swaps in a real S&S crew photo of that step. The words are the client's own (home page, residential page and the
"How your roof protects your entire home" post). The drawing is labelled as an illustration.
"""
import math
from engine import img

TH = math.radians(math.degrees(math.atan(6 / 12)))
C, S_ = math.cos(TH), math.sin(TH)
EAVE = (60, 350)
W, H = 620, 380
VX, VY = 20, 40
K = 1.8


def P(s, d):
    """Local slope coordinates (s along the slope from the eave, d perpendicular, negative = above the surface) -> SVG."""
    return (EAVE[0] + s * C + d * S_, EAVE[1] - s * S_ + d * C)


def f(p):
    return f"{p[0]:.1f} {p[1]:.1f}"


STAGES = [
    ("Tear-off", "Down to the deck", "From tear-off to final inspection, every layer is installed with precision. It starts at the deck, which plays a key structural role by distributing weight evenly across the home.",
     "crew-tear-off-deck", "Roofer at a tear-off, down to the deck"),
    ("Flashing", "Flashing and underlayment", "Leaks can occur due to damaged shingles, broken flashing, or clogged gutters. Shingles, underlayment, flashing and ventilation all work together like a team.",
     "crew-drip-edge", "Crew fitting metal edge flashing"),
    ("Shingles", "Course by course", "Our experienced team will install your new roof with precision and care, ensuring your home is fully protected.",
     "crew-shingle-nailing", "Two roofers nailing shingles"),
    ("Ridge", "Ridge and ventilation", "Ventilation is part of the team. In the drawing the ridge is capped and vented: the last layer before the final check.",
     "crew-ridge-shingles", "Roofer installing ridge shingles"),
    ("Inspection", "Final inspection", "After installation, we perform a detailed inspection to ensure the roof is properly installed and meets our high-quality standards.",
     "drone-home-shingles", "Aerial view of a finished shingle roof"),
]


def svg():
    L = 380.1
    rot = f'translate({EAVE[0]} {EAVE[1]}) rotate(-26.565) scale(1 {K})'
    shingles = "".join(f'<polygon points="{x} -15.5 {x + 30} -15.5 {x + 30} -17.6 {x} -21.8"/>' for x in range(-10, 366, 15))
    seams = "".join(f'<line x1="{x}" y1="-12" x2="{x}" y2="0"/>' for x in (85, 180, 275))
    grain = "".join(f'<line x1="{x}" y1="-{y}" x2="{x + 40}" y2="-{y}"/>' for x, y in ((10, 4), (60, 8), (120, 5), (200, 9), (250, 4), (320, 7)))
    laps = "".join(f'<line x1="{x}" y1="-15.5" x2="{x}" y2="-12"/>' for x in range(54, 370, 64))
    apex = (400, 180)
    cap_l = P(350, -40); cap_r = (800 - cap_l[0], cap_l[1])
    top = (400, P(380, -52)[1] - 4)
    vent = f'<rect x="382" y="{top[1] - 9:.1f}" width="36" height="10" rx="1"/>' + "".join(f'<line x1="{x}" y1="{top[1] - 7:.1f}" x2="{x}" y2="{top[1] - 1:.1f}"/>' for x in range(388, 414, 5))
    air = ('<path d="M300 318 C 330 270, 370 230, 396 %.1f"/><path d="M520 318 C 480 270, 430 230, 404 %.1f"/>' % (top[1] + 6, top[1] + 6))
    def call(s, d0, d1, text, i, dx=6):
        a, b = P(s, d0), P(s, d1)
        return (f'<g class="ly-call" data-c="{i}"><line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"/><circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="3"/>'
                f'<text x="{b[0] + dx:.1f}" y="{b[1] - 6:.1f}">{text}</text></g>')
    calls = (call(40, -11, -120, "DECK", 0) + call(110, -25, -120, "FLASHING + UNDERLAYMENT", 1) + call(185, -36, -120, "SHINGLES", 2) +
             f'<g class="ly-call" data-c="3"><line x1="400" y1="{top[1] - 10:.1f}" x2="400" y2="96"/><circle cx="400" cy="{top[1] - 10:.1f}" r="3"/><text x="408" y="104">RIDGE VENT</text></g>')
    return f'''<svg class="ly-svg" viewBox="{VX} {VY} {W} {H}" role="img" aria-labelledby="ly-title">
<title id="ly-title">Drawing of one slope of a roof at a 6/12 pitch, built up layer by layer: deck, flashing and underlayment, shingles, ridge vent, final inspection</title>
<defs><pattern id="ly-hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="9" class="ly-hl"/></pattern></defs>
<path class="ly-attic" d="M{f(EAVE)} L400 180 L640 300 L640 350 Z"/>
<path class="ly-guide" d="M60 350 H640 M400 180 V350 M84 350 V412"/>
<path class="ly-ghost" d="M400 180 L640 300"/>
<g class="ly-pitch"><path d="M52 128 L172 128 L172 68 Z"/><text x="112" y="146">12</text><text x="182" y="102">6</text><text class="ly-pl" x="52" y="56">6/12 PITCH</text></g>
<g transform="{rot}">
<rect class="ly-rafter" x="-16" y="0" width="398" height="20"/>
<g class="ly-g" data-l="0"><rect class="ly-deck" x="-10" y="-12" width="390" height="12"/><g class="ly-seam">{seams}{grain}</g></g>
<g class="ly-g" data-l="1"><rect class="ly-felt" x="-8" y="-15.5" width="386" height="3.5"/><g class="ly-lap">{laps}</g><path class="ly-drip" d="M-15 -16.5 L-7 -16.5 L-7 5 L-13 9"/></g>
<g class="ly-g ly-sh" data-l="2">{shingles}</g>
</g>
<g class="ly-g" data-l="3"><path class="ly-cap" d="M{f(cap_l)} L400 {top[1] + 2:.1f} L{f(cap_r)}"/><g class="ly-vent">{vent}</g><g class="ly-air">{air}</g></g>
<g class="ly-g ly-stamp" data-l="4"><circle cx="560" cy="262" r="46"/><circle cx="560" cy="262" r="39"/><path d="M540 262 L554 276 L582 246"/><text x="560" y="328">INSPECTED</text></g>
<g class="ly-calls">{calls}</g>
</svg>'''


def section(label_fn):
    a = P(34, -72)
    rng = (f'<input class="ly-range" type="range" min="0" max="4" step="0.01" value="0" aria-label="Build the roof, from tear-off to final inspection" aria-valuetext="Tear-off" '
           f'style="left:{(a[0] - VX) / W * 100:.2f}%;top:{(a[1] - VY) / H * 100:.2f}%;width:{320 / W * 100:.2f}%">')
    photos = "".join(f'<figure class="ly-ph{" on" if i == 0 else ""}" data-i="{i}">{img(n, alt)}<figcaption>{alt}</figcaption></figure>' for i, (k, t, d, n, alt) in enumerate(STAGES))
    texts = "".join(f'<div class="ly-tx{" on" if i == 0 else ""}" data-i="{i}"><p class="ly-k">Stage {i + 1:02d} of 05</p><h3>{t}</h3><p>{d}</p></div>' for i, (k, t, d, n, alt) in enumerate(STAGES))
    btns = "".join(f'<button type="button" data-go="{i}"{" aria-pressed=\"true\"" if i == 0 else " aria-pressed=\"false\""}><span>{i + 1:02d}</span>{k}</button>' for i, (k, t, d, n, alt) in enumerate(STAGES))
    return f'''<section class="layers-sec" id="layers"><div class="wrap">
<div class="sec-head light reveal">{label_fn("03", "Layer by layer")}<h2>From tear-off to final inspection, <span>every layer.</span></h2>
<p class="lede">Shingles, underlayment, flashing and ventilation all work together like a team. Drag the handle up the roof to put one on, the way our crews do.</p></div>
<div class="layers" data-layers>
<div class="ly-draw"><div class="ly-canvas">{svg()}{rng}</div><p class="ly-note">Drag up the slope &middot; drawing for illustration, photos from our jobs</p></div>
<div class="ly-panel"><div class="ly-photos">{photos}</div><div class="ly-texts" aria-live="polite">{texts}</div><div class="ly-btns" role="group" aria-label="Stages">{btns}</div></div>
</div></div></section>'''
