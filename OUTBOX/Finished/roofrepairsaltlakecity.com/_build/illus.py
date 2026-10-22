"""Original line illustrations for the "repair manual" design. Drawn for this site."""

# Fig. 1: a house roof with the six places leaks most often start, numbered for the symptom finder.
SPOTS = [(1, "Chimney flashing", 292, 92), (2, "Valley", 432, 150), (3, "Pipe boot", 212, 168), (4, "Skylight", 352, 186),
         (5, "Eaves / ice dam", 138, 252), (6, "Ridge and vents", 380, 70)]


def fig_house():
    s = ['<svg class="fig" viewBox="0 0 640 400" role="img" aria-label="Figure 1: the six places on a roof where leaks most often start">',
         '<defs><pattern id="sh" width="22" height="12" patternUnits="userSpaceOnUse"><rect width="22" height="12" fill="#ddd6c4"/><path d="M0 12 H22 M11 0 V6 M0 6 H22 M0 0 V6 M22 6 V12" class="pat"/></pattern></defs>',
         '<path class="wall" d="M120 262 V362 H520 V262"/><path class="wall" d="M330 362 V300 H380 V362"/><rect class="win" x="170" y="290" width="60" height="44"/><rect class="win" x="430" y="290" width="54" height="44"/>',
         '<path class="roof" d="M90 270 L310 60 L470 60 L560 160 L560 270 Z" fill="url(#sh)"/>',
         '<path class="ln" d="M90 270 L310 60 L470 60 L560 160 M310 60 L432 196 L560 160 M432 196 L432 270"/>',
         '<rect class="chim" x="276" y="54" width="34" height="62"/><path class="ln2" d="M272 116 H314"/>',
         '<rect class="sky" x="336" y="168" width="34" height="34"/><path class="pipe" d="M206 176 V156 H218 V176"/>',
         '<path class="ice" d="M96 270 L170 254 L176 262 L102 278 Z"/><path class="drip" d="M110 280 v12 M126 277 v9 M142 273 v14 M158 270 v8"/>']
    for n, label, x, y in SPOTS:
        s.append(f'<g class="spot" data-spot="{n}"><circle cx="{x}" cy="{y}" r="15"/><text x="{x}" y="{y + 5}" text-anchor="middle">{n}</text></g>')
    s.append('<text class="cap" x="20" y="392">FIG. 1 &mdash; WHERE ROOFS LEAK</text><text class="cap" x="620" y="392" text-anchor="end">NOT TO SCALE</text></svg>')
    return "".join(s)


def swatch(kind):
    pats = {
        "shingle": '<pattern id="p-shingle" width="30" height="16" patternUnits="userSpaceOnUse"><rect width="30" height="16" class="f1"/><path d="M0 16 H30 M15 0 V8 M0 8 H30 M0 0 V8" class="k"/></pattern>',
        "tile": '<pattern id="p-tile" width="24" height="20" patternUnits="userSpaceOnUse"><rect width="24" height="20" class="f2"/><path d="M0 20 Q6 8 12 20 Q18 8 24 20" class="k"/></pattern>',
        "wood": '<pattern id="p-wood" width="40" height="18" patternUnits="userSpaceOnUse"><rect width="40" height="18" class="f3"/><path d="M0 18 H40 M9 0 V9 M27 0 V9 M0 9 H40 M18 9 V18 M36 9 V18" class="k"/><path d="M2 4 h5 M12 13 h4 M30 5 h6" class="g"/></pattern>',
        "metal": '<pattern id="p-metal" width="28" height="40" patternUnits="userSpaceOnUse"><rect width="28" height="40" class="f4"/><path d="M26 0 V40" class="seam"/></pattern>',
        "tpo": '<pattern id="p-tpo" width="80" height="60" patternUnits="userSpaceOnUse"><rect width="80" height="60" class="f5"/><path d="M0 58 H80" class="k"/><path d="M0 56 H80" class="weld"/></pattern>',
        "ballast": '<pattern id="p-ballast" width="26" height="26" patternUnits="userSpaceOnUse"><rect width="26" height="26" class="f6"/><circle cx="5" cy="6" r="3.2" class="st"/><circle cx="16" cy="4" r="2.4" class="st"/><circle cx="21" cy="15" r="3.4" class="st"/><circle cx="9" cy="17" r="2.8" class="st"/><circle cx="3" cy="23" r="2" class="st"/><circle cx="17" cy="23" r="2.2" class="st"/></pattern>',
        "membrane": '<pattern id="p-membrane" width="60" height="60" patternUnits="userSpaceOnUse"><rect width="60" height="60" class="f7"/><path d="M0 30 H60" class="k"/></pattern>',
    }
    return f'<svg class="sw" viewBox="0 0 120 80" aria-hidden="true"><defs>{pats[kind]}</defs><rect width="120" height="80" fill="url(#p-{kind})"/></svg>'


def fig_ballast():
    return ('<svg class="fig" viewBox="0 0 640 260" role="img" aria-label="Section through a ballasted single-ply roof: deck, insulation, loose-laid membrane, stone ballast">'
            '<rect class="deck" x="20" y="200" width="600" height="22"/><rect class="ins" x="20" y="150" width="600" height="50"/>'
            '<path class="mem" d="M20 146 H620"/>'
            + "".join(f'<circle class="stone" cx="{30 + (i * 37) % 590}" cy="{128 + (i * 13) % 14}" r="{6 + (i * 7) % 5}"/>' for i in range(60)) +
            '<path class="lead" d="M120 118 L150 40"/><text x="154" y="38">STONE BALLAST</text>'
            '<path class="lead" d="M300 146 L330 70"/><text x="334" y="68">LOOSE-LAID MEMBRANE</text>'
            '<path class="lead" d="M470 175 L500 100"/><text x="504" y="98">INSULATION</text>'
            '<path class="lead" d="M560 211 L590 240"/><text x="470" y="250">ROOF DECK</text>'
            '<text class="cap" x="20" y="252">FIG. 2 &mdash; BALLASTED SINGLE-PLY</text></svg>')
