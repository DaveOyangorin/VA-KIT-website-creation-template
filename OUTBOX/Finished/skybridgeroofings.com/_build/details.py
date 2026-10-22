"""Original line drawings: one construction detail per Sky Bridge system, drawn like a sheet in a set of roofing details.
Generic textbook build-ups (no product claims, no dimensions). Drawn for this site; not traced from anything."""


def _lab(x, y, tx, ty, text, anchor="start"):
    return (f'<path class="lead" d="M{x} {y} L{tx} {ty}"/><circle class="dot" cx="{x}" cy="{y}" r="2.6"/>'
            f'<text x="{tx + (4 if anchor == "start" else -4)}" y="{ty + 4}" text-anchor="{anchor}">{text}</text>')


def _svg(body, title, no):
    return (f'<svg class="detail" viewBox="0 0 360 230" role="img" aria-label="Detail drawing: {title}">'
            f'<rect class="sheet" x="1" y="1" width="358" height="228"/>{body}'
            f'<g class="tb"><path d="M1 204 H359"/><text x="10" y="221">{title.upper()}</text><text x="350" y="221" text-anchor="end">DETAIL {no}</text></g></svg>')


def shingles():
    b = '<path class="fill-deck" d="M30 150 L330 90 L330 104 L30 164 Z"/>'
    b += '<path class="fill-under" d="M30 146 L330 86 L330 90 L30 150 Z"/>'
    for i in range(7):
        x = 40 + i * 42
        y = 146 - (x - 30) * 0.2
        b += f'<path class="fill-sh" d="M{x} {y - 2} L{x + 50} {y - 12} L{x + 50} {y - 20} L{x} {y - 10} Z"/>'
    b += _lab(120, 112, 150, 40, "Shingle courses") + _lab(250, 98, 270, 130, "Underlayment") + _lab(80, 152, 70, 185, "Roof deck")
    return _svg(b, "Asphalt shingle roof", "01")


def metal():
    b = '<path class="fill-deck" d="M20 150 H340 V164 H20 Z"/><path class="fill-under" d="M20 146 H340 V150 H20 Z"/>'
    d = "M20 146"
    for x in (20, 120, 220, 320):
        d += f" H{x + 34} V112 H{x + 44} V146"
    b += f'<path class="ln-heavy" d="{d} H340"/>'
    for x in (54, 154, 254):
        b += f'<path class="fill-clip" d="M{x - 6} 146 H{x + 16} V140 H{x + 4} V118 H{x - 2} V140 H{x - 6} Z"/>'
    b += _lab(98, 112, 120, 50, "Standing seam") + _lab(159, 132, 200, 78, "Concealed clip") + _lab(70, 146, 40, 190, "Metal panel") + _lab(280, 148, 330, 190, "Underlayment", "end")
    return _svg(b, "Standing seam metal", "02")


def tpo():
    b = '<path class="fill-deck" d="M20 162 H340 V176 H20 Z"/><path class="fill-ins" d="M20 128 H340 V162 H20 Z"/><path class="fill-board" d="M20 120 H340 V128 H20 Z"/>'
    b += '<path class="ln-heavy" d="M20 116 H200"/><path class="ln-heavy" d="M150 112 C170 112 175 116 180 116 H340"/>'
    b += '<path class="weld" d="M150 112 H200 V118 H150 Z"/>'
    b += _lab(176, 114, 200, 52, "Heat-welded seam") + _lab(80, 116, 50, 80, "TPO membrane") + _lab(260, 124, 270, 80, "Cover board") + _lab(240, 145, 270, 196, "Insulation") + _lab(60, 170, 40, 196, "Deck")
    return _svg(b, "TPO single-ply", "03")


def epdm():
    b = '<path class="fill-deck" d="M20 162 H340 V176 H20 Z"/><path class="fill-ins" d="M20 126 H340 V162 H20 Z"/>'
    b += '<path class="ln-black" d="M20 120 H200"/><path class="ln-black" d="M160 116 H340"/><path class="tape" d="M160 117 H200 V121 H160 Z"/>'
    b += _lab(180, 118, 205, 54, "Seam tape") + _lab(90, 120, 50, 80, "EPDM rubber") + _lab(250, 145, 270, 196, "Insulation") + _lab(70, 170, 40, 196, "Deck")
    return _svg(b, "EPDM membrane", "04")


def coatings():
    b = '<path class="fill-deck" d="M20 150 H340 V164 H20 Z"/><path class="fill-old" d="M20 140 H340 V150 H20 Z"/>'
    b += '<path class="coat" d="M20 134 H230 V140 H20 Z"/><path class="ln" d="M230 134 C238 134 240 138 244 140"/>'
    b += '<g class="roller"><rect x="232" y="106" width="44" height="18" rx="9"/><path d="M276 115 H300 L318 60"/></g>'
    b += _lab(110, 136, 120, 70, "Silicone coating") + _lab(290, 145, 270, 190, "Existing roof", "end") + _lab(80, 157, 50, 190, "Deck")
    return _svg(b, "Roof coating over existing roof", "05")


def gutters():
    b = '<path class="fill-deck" d="M40 40 L230 100 L230 112 L40 52 Z"/><path class="fill-fascia" d="M230 96 H244 V170 H230 Z"/>'
    b += '<path class="ln-heavy" d="M244 112 H252 C252 150 256 160 300 160 L318 118 H326"/>'
    b += '<path class="ln" d="M226 98 L262 110"/><path class="hanger" d="M244 118 L320 118"/>'
    b += '<path class="water" d="M120 70 C170 86 230 104 268 136"/>'
    b += _lab(286, 150, 270, 196, "Seamless gutter", "end") + _lab(300, 118, 290, 70, "Hanger") + _lab(237, 150, 180, 196, "Fascia") + _lab(150, 78, 90, 120, "Roof edge")
    return _svg(b, "Seamless gutter at the eave", "06")


def walls():
    b = '<path class="fill-stud" d="M40 30 H64 V190 H40 Z"/><path class="fill-board" d="M64 30 H76 V190 H64 Z"/><path class="fill-under" d="M76 30 H80 V190 H76 Z"/>'
    for y in (50, 110, 170):
        b += f'<path class="fill-clip" d="M80 {y} H100 V{y + 10} H80 Z"/>'
    b += '<path class="ln-heavy" d="M100 30 V100 M100 106 V190"/><path class="ln" d="M100 100 H112 V106 H100"/>'
    b += _lab(52, 120, 150, 40, "Framing") + _lab(70, 150, 150, 70, "Sheathing") + _lab(78, 80, 150, 100, "Weather barrier") + _lab(90, 115, 150, 130, "Girt / clip") + _lab(100, 160, 150, 160, "Metal wall panel") + _lab(108, 103, 220, 190, "Panel reveal")
    return _svg(b, "Metal wall panel section", "07")


def repair():
    b = '<path class="fill-wall" d="M210 20 H250 V170 H210 Z"/><path class="fill-deck" d="M20 170 L210 120 L210 134 L20 184 Z"/>'
    for i in range(4):
        y = 150 - i * 11
        b += f'<path class="fill-sh" d="M{40 + i * 40} {y + 18 - i * 0} L210 {y - 18 + i * 0} L210 {y - 26} L{40 + i * 40} {y + 10} Z"/>'
    b += '<path class="flash" d="M196 128 V60 H210 M196 128 L210 124"/>'
    b += '<path class="leak" d="M150 50 C160 80 170 96 176 120"/>'
    b += _lab(203, 90, 150, 34, "Step flashing") + _lab(232, 150, 285, 150, "Wall") + _lab(110, 140, 60, 70, "Shingles") + _lab(90, 175, 60, 205, "Deck")
    return _svg(b, "Roof-to-wall flashing repair", "08")


def replacement():
    b = '<path class="fill-deck" d="M20 160 H340 V174 H20 Z"/><path class="fill-under" d="M20 156 H340 V160 H20 Z"/>'
    b += '<path class="fill-sh" d="M180 146 H340 V156 H180 Z"/>'
    b += '<path class="old" d="M40 112 L170 92 L170 104 L40 124 Z"/><path class="old" d="M50 92 L160 74 L160 84 L50 102 Z"/>'
    b += '<path class="arrow" d="M100 140 C100 128 100 120 102 112 M96 118 L102 110 L108 118"/>'
    b += _lab(110, 98, 190, 54, "Old layers torn off") + _lab(260, 150, 280, 120, "New roof") + _lab(80, 158, 50, 196, "Underlayment") + _lab(240, 168, 270, 196, "Deck checked")
    return _svg(b, "Tear-off and replacement", "09")


def inspection():
    b = '<path class="fill-plan" d="M40 30 H320 V180 H40 Z"/><path class="ln" d="M40 105 H320 M180 30 V180 M40 30 L110 105 L40 180 M320 30 L250 105 L320 180 M110 105 H250"/>'
    for i, (x, y) in enumerate([(80, 60), (200, 70), (280, 150), (150, 150)], 1):
        b += f'<circle class="mark" cx="{x}" cy="{y}" r="11"/><text class="mk" x="{x}" y="{y + 4}" text-anchor="middle">{i}</text>'
    b += '<text class="note" x="44" y="198">1 FLASHING  2 PENETRATION  3 GUTTER  4 SHINGLE WEAR</text>'
    return _svg(b, "Inspection roof plan", "10")


DETAILS = {"shingles": shingles, "metal": metal, "tpo": tpo, "epdm": epdm, "coatings": coatings, "gutters": gutters,
           "walls": walls, "roof-repair": repair, "replacement": replacement, "inspection": inspection}
