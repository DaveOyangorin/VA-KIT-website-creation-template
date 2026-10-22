"""Original drawing for saltcityroofers.com: the asphalt roof system the client lists on its own asphalt page, drawn as an exploded
stack from the deck up (decking, drip edge, underlayment, ice & water, flashings, shingles, nails, ventilation)."""

LAYERS = [("01", "Decking", "The plywood that holds everything. Soft boards are re-sheeted after tear-off."),
          ("02", "Drip edge", "Metal at the eaves and rakes that sheds water into the gutter."),
          ("03", "Ice &amp; water", "Self-adhering membrane at eaves and valleys, where ice backs water up."),
          ("04", "Underlayment", "The waterproofing layer across the rest of the deck."),
          ("05", "Flashings", "Flashing and counter-flashing at walls, chimneys and pipes."),
          ("06", "Shingles", "The visible roof, installed to the manufacturer&rsquo;s specification."),
          ("07", "Nails", "The application materials: the right fastener, in the right place."),
          ("08", "Ventilation", "Intake at the eaves and exhaust at the ridge, so the attic breathes.")]


def stack():
    rows = []
    for i, (n, t, d) in enumerate(LAYERS):
        j = len(LAYERS) - 1 - i
        y = 24 + j * 42
        x = 10 + j * 16
        rows.append(f'<g class="ly l{i}"><path d="M{x} {y + 22} L{x + 190} {y} L{x + 520} {y} L{x + 330} {y + 22} Z"/><text x="{x + 535}" y="{y + 15}"><tspan class="n">{n}</tspan> {t.replace("&amp;", "&#38;")}</text></g>')
    return ('<svg class="stack" viewBox="0 0 800 370" role="img" aria-label="Exploded drawing of an asphalt roof system, from the decking at the bottom to the ventilation at the top">'
            + "".join(reversed(rows)) + "</svg>")


def legend():
    return '<ol class="legend">' + "".join(f'<li><span class="mono">{n}</span><b>{t}</b><p>{d}</p></li>' for n, t, d in LAYERS) + "</ol>"
