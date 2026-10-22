"""Original drawings for cleartopsolutions.shop (the site has no real photos of its own).
house(active, uid): a blueprint-style cutaway of a two-storey St. George house with a basement and a crawl space. Each room where
water damage starts is a zone: attic, bath (upstairs bathroom / toilet), ceiling (the living-room ceiling under the bathroom),
kitchen, basement, crawl. active=None draws every zone at rest; active="kitchen" etc. highlights one and dims the rest;
active="all" shows water everywhere (general drying / mitigation pages)."""

ZONES = {  # x, y, w, h of each zone's highlight box, and hotspot centre (viewBox 800 x 600)
    "attic": ((150, 70, 500, 118), (400, 140)),
    "bath": ((402, 192, 286, 126), (612, 286)),
    "ceiling": ((402, 320, 286, 40), (545, 338)),
    "kitchen": ((112, 320, 288, 138), (232, 418)),
    "basement": ((112, 462, 288, 106), (256, 535)),
    "crawl": ((402, 462, 286, 50), (556, 488)),
}


def house(active=None, uid="h", crop=False):
    def z(name, inner):
        on = active in (None, "all", name)
        cls = "zone" + (" on" if active == name else "") + ("" if on else " dim")
        x, y, w, h = ZONES[name][0]
        return f'<g class="{cls}" data-z="{name}"><rect class="zbox" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>{inner}</g>'
    wet = lambda name: active in (None, "all", name)
    attic = f'''<path class="ln" d="M300 188 L300 120 M500 188 L500 120 M400 188 L400 70"/>
<g class="mold"><circle cx="268" cy="168" r="7"/><circle cx="282" cy="160" r="4.5"/><circle cx="256" cy="176" r="3.5"/><circle cx="530" cy="150" r="5"/><circle cx="541" cy="158" r="3"/></g>
<path class="ln thin" d="M180 186 l40 -24 M600 186 l-40 -24"/>'''
    bath = f'''<path class="ln" d="M600 316 v-34 h44 v34 M596 282 h52 M622 282 v-34 a10 10 0 0 1 10 -10 h8 v44"/>
<rect class="ln" x="470" y="258" width="70" height="56" rx="6"/><path class="ln thin" d="M478 266 h54"/>
{'<path class="water" d="M562 316 q30 -6 60 0 q30 6 64 0 v2 h-124z"/>' if wet("bath") else ""}'''
    ceiling = f'''<path class="stain" d="M512 322 q30 18 66 2 q-8 16 -32 18 q-24 2 -34 -20z"/>
{'<g class="drip"><path class="drop" d="M545 344 q-5 8 0 12 q5 -4 0 -12z"/><path class="drop d2" d="M560 344 q-5 8 0 12 q5 -4 0 -12z"/></g>' if wet("ceiling") else ""}
<path class="ln thin" d="M520 456 v-50 h70 v50 M528 406 v-8 h54 v8"/>'''
    kitchen = f'''<path class="ln" d="M124 456 v-56 h150 v56 M124 400 v-6 h150 v6 M150 394 v-30 M128 346 h140 v-18 h-140z M200 394 q0 -26 18 -26"/>
<rect class="ln thin" x="290" y="350" width="44" height="106" rx="3"/><path class="ln thin" d="M290 396 h44 M296 372 h6"/>
{'<path class="water" d="M114 456 q40 -5 80 0 q40 5 80 0 q40 -5 80 0 q20 3 42 0 v2 h-282z"/>' if wet("kitchen") else ""}'''
    basement = f'''<path class="ln thin" d="M140 566 v-60 h60 v60 M240 566 v-34 h80 v34"/><path class="ln thin" d="M340 470 l40 60"/>
{'<path class="water deep" d="M112 568 v-30 q36 -7 72 0 q36 7 72 0 q36 -7 72 0 q36 7 72 0 v30z"/>' if wet("basement") else ""}'''
    crawl = f'''<path class="ln thin" d="M420 510 l20 -12 l20 12 l20 -12 l20 12 M540 510 l14 -8 l14 8 M600 510 l18 -10 l18 10"/>
<g class="mold"><circle cx="470" cy="478" r="5"/><circle cx="482" cy="472" r="3"/><circle cx="640" cy="482" r="4"/></g>
{'<path class="water" d="M404 510 q40 -4 80 0 q40 4 80 0 q40 -4 80 0 q24 3 40 0 v2 h-280z"/>' if wet("crawl") else ""}'''
    vb = "0 0 800 600"
    if crop and active in ZONES:
        x, y, w, h = ZONES[active][0]; pad = 46; vb = f"{x - pad} {y - pad} {w + 2 * pad} {h + 2 * pad}"
    return f'''<svg class="house{" crop" if crop else ""}" viewBox="{vb}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Cutaway drawing of a house showing where water damage starts: attic, bathroom, ceiling, kitchen, basement and crawl space">
<defs><pattern id="{uid}-g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" class="grid"/></pattern>
<pattern id="{uid}-dirt" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1" class="dirtdot"/><circle cx="9" cy="8" r="1" class="dirtdot"/></pattern></defs>
<rect width="800" height="600" fill="url(#{uid}-g)" class="gridbg"/>
<rect x="40" y="460" width="720" height="140" fill="url(#{uid}-dirt)"/>
<path class="ln ground" d="M30 460 H770"/>
<path class="ln wall" d="M90 192 L400 40 L710 192 M110 192 V460 M690 192 V460 M110 320 H690 M400 192 V460 M110 192 H690 M110 460 V570 H400 V460 M400 512 H690 V460"/>
<path class="ln thin" d="M150 270 h70 v-46 h-70z M185 224 v46 M150 247 h70"/>
<path class="ln thin" d="M640 420 h36 v-60 h-36z"/>
{z("attic", attic)}{z("bath", bath)}{z("ceiling", ceiling)}{z("kitchen", kitchen)}{z("basement", basement)}{z("crawl", crawl)}
<g class="tags"><text x="118" y="210">UPSTAIRS</text><text x="118" y="338">MAIN FLOOR</text><text x="118" y="478">BASEMENT</text><text x="408" y="478">CRAWL SPACE</text><text x="372" y="100">ATTIC</text></g>
</svg>'''


def clock48(uid="c"):
    """A 48-hour dial for the drying-window band (EPA: dry within 24-48 hours to prevent mold)."""
    ticks = "".join(f'<line class="tk{" big" if i % 6 == 0 else ""}" x1="150" y1="{18 if i % 6 == 0 else 24}" x2="150" y2="34" transform="rotate({i * 7.5} 150 150)"/>' for i in range(48))
    labels = "".join(f'<text x="{150 + 100 * __import__("math").sin(__import__("math").radians(h * 7.5)):.1f}" y="{154 - 100 * __import__("math").cos(__import__("math").radians(h * 7.5)):.1f}">{h}h</text>' for h in (0, 12, 24, 36))
    return f'''<svg class="clock48" viewBox="0 0 300 300" aria-hidden="true"><circle class="c-bg" cx="150" cy="150" r="128"/>{ticks}
<circle class="c-arc" cx="150" cy="150" r="118" pathLength="1" transform="rotate(-90 150 150)"/><circle class="c-risk" cx="150" cy="150" r="118" pathLength="1" transform="rotate(90 150 150)"/>{labels}
<text class="c-big" x="150" y="160" data-hours>0h</text><text class="c-sub" x="150" y="186">since the water</text></svg>'''
