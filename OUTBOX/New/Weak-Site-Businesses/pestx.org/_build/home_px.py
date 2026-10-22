"""Home page for the pestx.org redesign: "A field guide to the Utah home".
Every pest fact below is quoted or condensed from Pestx's own pest pages (src/extract.json); nothing is added."""
import html
from engine import img, faq_html, faq_ld, crumbs_ld
from cfg import U, PESTS, INK
import pagekit as K
from pagekit import ARROW, PHONE, HOME

# where / when line for each specimen plate (from each pest page)
SEEN = {"mosquito": ("Late spring to early fall", "Near standing water: ponds, ditches, birdbaths, clogged gutters"),
        "ants": ("Indoors", "Trails along counters and floors"),
        "spiders": ("Indoors", "Basements, garages and corners of rooms"),
        "rodents": ("Indoors and out", "House mice, deer mice, voles and pack rats"),
        "wasps": ("Around the house", "Under eaves, in trees, inside wall voids"),
        "beetles": ("Especially in the fall", "The sunny sides of buildings"),
        "flies": ("Indoors", "Garbage, overripe produce, sink and shower drains"),
        "moths": ("Indoors", "Kitchen cabinets, closets and storage areas"),
        "snails-and-slugs": ("Mornings and evenings", "Damp, shaded garden beds"),
        "grasshopper": ("Hot, dry summers", "Gardens and landscapes")}
LINE = {"mosquito": "Swarm near water from late spring to fall; some species spread West Nile virus.",
        "ants": "Tiny but persistent, they come inside looking for food and water.",
        "spiders": "Most are harmless; black widows and hobo spiders call for caution.",
        "rodents": "Gnaw wiring and insulation, contaminate food and pose health risks.",
        "wasps": "Paper wasps, yellow jackets and hornets defend their nests hard.",
        "beetles": "Boxelder and elm seed bugs gather on homes in large numbers.",
        "flies": "Houseflies, fruit flies and drain flies can spread bacteria.",
        "moths": "Pantry moths go for dry goods; clothes moths go for fabrics.",
        "snails-and-slugs": "Slow-moving but hard on Utah gardens and landscapes.",
        "grasshopper": "Multiply fast and strip gardens in hot, dry summers."}
# the old site's own "Full home coverage" diagram: A Eaves, B Bedrooms, C Garage, D Kitchen & Living Room, E Yard, F Foundation, G Basement
ZONES = [("A", "Eaves", 118, 196, [("wasps", "Paper wasps, yellow jackets and hornets build nests under eaves, in trees and even inside wall voids."),
                                  ("beetles", "Elm seed and boxelder bugs gather on the sunny sides of buildings, especially in the fall.")]),
         ("B", "Bedrooms", 300, 250, [("moths", "Clothes moths hide in closets and storage areas and damage fabrics."),
                                      ("spiders", "Spiders turn up in corners of rooms; regular dusting and vacuuming discourages new webs.")]),
         ("C", "Garage", 612, 318, [("spiders", "Garages are one of the places Utah spiders are most often found."),
                                    ("rodents", "Seal cracks and gaps around doors to keep rodents from getting in.")]),
         ("D", "Kitchen &amp; Living Room", 300, 340, [("ants", "Ants come in for food and moisture, forming long trails along counters and floors."),
                                                     ("moths", "Pantry moths target flour and grains in kitchen cabinets."),
                                                     ("flies", "Houseflies gather around garbage, fruit flies near overripe produce, drain flies in drains."),
                                                     ("rodents", "Rodent activity runs along walls, in pantries and behind appliances.")]),
         ("E", "Yard", 62, 352, [("mosquito", "Mosquitoes breed in standing water: ponds, ditches, birdbaths, clogged gutters."),
                                 ("snails-and-slugs", "Snails and slugs feed on plants in damp, shaded areas."),
                                 ("grasshopper", "Grasshoppers strip gardens and landscapes in hot, dry summers.")]),
         ("F", "Foundation", 548, 452, [("ants", "Ants get in through cracks in the foundation; sealing them is the first prevention step."),
                                        ("rodents", "Rodents use cracks and gaps around foundations to get inside.")]),
         ("G", "Basement", 300, 430, [("spiders", "Basements are one of the places Utah spiders are most often found."),
                                      ("rodents", "Signs of rodents: droppings, gnawed materials and scratching in walls or ceilings.")])]
SEASONS = [("mosquito", "Mosquitoes", 4, 8, "Late spring through early fall"), ("grasshopper", "Grasshoppers", 5, 7, "Hot, dry summers"),
           ("beetles", "Boxelder &amp; elm seed bugs", 8, 11, "Especially in the fall")]
MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
NAMES = {s: n for s, n, t in PESTS}
HOME_FAQ = [("Is pest control safe for pets?", "<p>It depends on what&rsquo;s used. Many commercial pesticides contain chemicals like pyrethroids and organophosphates, which can be toxic to pets if ingested or inhaled. Pestx uses eco-friendly practices that remove the dangers pests pose to your animals, and treated areas should stay off-limits to pets until sprays or powders have dried. <a href=\"@/blogs/is-pest-control-safe-for-pets/\">Read the full post</a>.</p>"),
            ("Does one spray work for most bugs?", "<p>No. Different pests react to different treatments, some bugs build resistance, and eggs and larvae hidden away often need follow-up treatments. A combination of targeted solutions works better than one spray. <a href=\"@/blogs/does-one-spray-work-for-most-bugs/\">Read the full post</a>.</p>"),
            ("How do bugs get inside my home?", "<p>Through gaps around windows and doors, cracks in the foundation and walls, vents and chimneys, and gaps around pipes and wiring. Uncovered food and open trash bins give them a reason to look. <a href=\"@/blogs/how-bugs-get-inside-your-home/\">Read the full post</a>.</p>"),
            ("What does year-round protection mean?", "<p>All-season pest control coverage, month to month, that adapts to seasonal changes, because peace of mind should never have an off-season.</p>"),
            ("What if the pests come back?", "<p>Satisfaction is guaranteed: our technicians will return as often as necessary to make sure you are satisfied.</p>")]


def plate_data():
    out = []
    for i, (s, n, tax) in enumerate(PESTS):
        when, where = SEEN[s]
        out.append(f'<figure class="pl-f{" on" if i == 0 else ""}" data-pl="{i}">{img(INK[s], f"Ink drawing of {n.lower()}", priority=(i == 0), lazy=(i != 0))}'
                   f'<figcaption><span class="pl-no">Plate {i + 1:02d}</span><b>{n}</b><i>{tax}</i><span class="pl-meta"><em>Seen</em> {when}</span><span class="pl-meta"><em>Where</em> {where}</span>'
                   f'<a class="pl-go" href="@/pests/{s}/">Field notes {ARROW}</a></figcaption></figure>')
    return "".join(out)


def house_svg():
    marks = "".join(f'<g class="hz{" on" if i == 0 else ""}" data-z="{i}" tabindex="0" role="button" aria-label="Zone {l}: {html.unescape(n)}"><circle cx="{x}" cy="{y}" r="19"/><text x="{x}" y="{y + 6}" text-anchor="middle">{l}</text></g>'
                    for i, (l, n, x, y, p) in enumerate(ZONES))
    grass = "".join(f'<path d="M{x} 380 l-4 -12 M{x + 5} 380 l2 -14 M{x + 10} 380 l5 -10"/>' for x in (8, 40, 74, 712, 746, 778))
    return f'''<svg class="house" viewBox="0 0 800 560" role="img" aria-label="A house in cross-section with seven lettered zones: eaves, bedrooms, garage, kitchen and living room, yard, foundation and basement">
<defs><pattern id="soil" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="3" cy="4" r="1.1"/><circle cx="10" cy="10" r=".9"/></pattern></defs>
<rect class="h-soil" x="0" y="380" width="800" height="180" fill="url(#soil)"/>
<path class="h-ground" d="M0 380 H800"/>
<g class="h-line">{grass}
<path d="M104 204 L330 64 L556 204"/><path d="M128 200 V380 M532 200 V380"/><path d="M128 290 H532"/><path d="M128 200 H532"/>
<path d="M532 262 L708 240 V380 M708 380 H532"/><path d="M560 300 H690 V380 M560 300 V380" class="h-door"/><path d="M560 320 H690 M560 340 H690 M560 360 H690" class="h-door"/>
<path d="M128 380 V470 H532 V380"/><path d="M112 470 H548 V492 H112 Z" class="h-foot"/>
<rect x="170" y="226" width="56" height="40"/><rect x="400" y="226" width="56" height="40"/><path d="M198 226 V266 M428 226 V266"/>
<rect x="170" y="316" width="56" height="44"/><path d="M370 380 V318 H420 V380"/><path d="M450 330 H510 V352 H450 Z"/>
<rect x="160" y="404" width="70" height="30" class="h-thin"/><path d="M420 470 V420 H500 V470" class="h-thin"/><path d="M268 300 l0 0" />
<path d="M330 64 V40 H348 V76" class="h-thin"/>
<path d="M44 380 C40 330 28 300 50 270 C30 250 46 214 74 222 C88 196 120 214 112 240 C134 252 124 290 98 292 C96 320 92 350 92 380" class="h-thin"/>
<ellipse cx="740" cy="384" rx="34" ry="6" class="h-water"/></g>
{marks}</svg>'''


def zone_panels():
    out = []
    for i, (l, n, x, y, ps) in enumerate(ZONES):
        items = "".join(f'<li><a href="@/pests/{s}/">{img(INK[s], "", lazy=True)}<span><b>{NAMES[s]}</b>{t}</span></a></li>' for s, t in ps)
        out.append(f'<div class="zp{" on" if i == 0 else ""}" data-zp="{i}"><p class="zp-k"><span>{l}</span>Zone {l} of G</p><h3>{n}</h3><ul>{items}</ul></div>')
    return "".join(out)


def guide_grid(cls="fg-grid"):
    cards = "".join(f'''<a class="fg-card reveal" href="@/pests/{s}/"><span class="fg-no">No. {i + 1:02d}</span><figure>{img(INK[s], f"Ink drawing of {n.lower()}")}</figure>
<b>{n}</b><i>{tax}</i><p>{LINE[s]}</p><em>Field notes {ARROW}</em></a>''' for i, (s, n, tax) in enumerate(PESTS))
    return f'<div class="{cls}">{cards}</div>'


def seasons():
    head = "".join(f'<span class="sz-m" data-m="{i}">{m}</span>' for i, m in enumerate(MON))
    rows = "".join(f'''<div class="sz-row"><a class="sz-name" href="@/pests/{s}/">{n}<small>{note}</small></a><div class="sz-track"><i style="--a:{a};--b:{b}"></i></div></div>''' for s, n, a, b, note in SEASONS)
    return f'''<div class="sz" data-seasons><div class="sz-row sz-head"><span></span><div class="sz-track sz-months">{head}<b class="sz-now" aria-hidden="true"></b></div></div>{rows}
<div class="sz-row sz-all"><span class="sz-name">Pestx coverage<small>Month to month, all year</small></span><div class="sz-track"><i style="--a:0;--b:11"></i></div></div></div>'''


def home():
    body = f'''
<section class="fg-hero"><div class="fh-img" data-parallax="0.08">{img("px-wasatch", "The Wasatch Range glowing pink at sunset above fields in Utah", priority=True)}</div><div class="wrap fg-hero-in">
<div class="fg-hero-txt"><p class="label">Midvale, Utah &middot; Serving the Greater Salt Lake Area</p>
<h1>Pest control in Midvale <em>for every room and every season.</em></h1>
<p class="lede">Pestx is a family-owned pest control company founded by two brothers. We use eco-friendly, targeted treatments to keep homes and businesses across the Greater Salt Lake Area safe, with year-round protection that adapts as the seasons change.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Get a Quote {ARROW}</a><a class="btn ghost" href="tel:+18018719233">{PHONE} 801-871-9233</a></div>
<ol class="fg-motto" aria-label="Pestx in three words"><li><span>I</span>Smart</li><li><span>II</span>Trusted</li><li><span>III</span>Protected</li></ol></div>
<div class="plate" data-plate><div class="pl-top"><span>A field guide to the Utah home</span><span data-pl-count>01 / 10</span></div>
<div class="pl-frames">{plate_data()}</div>
<div class="pl-nav"><button type="button" class="pl-btn" data-pl-prev aria-label="Previous plate">&larr;</button><div class="pl-dots">{"".join(f'<button type="button" data-pl-dot="{i}" aria-label="{n}"{" class=on" if i == 0 else ""}></button>' for i, (s, n, t) in enumerate(PESTS))}</div><button type="button" class="pl-btn" data-pl-next aria-label="Next plate">&rarr;</button></div>
<div class="pl-rule" aria-hidden="true"></div></div>
</div><p class="credit">Atmosphere photo: Wasatch Range at sunset &middot; Ken Lund, CC BY-SA 2.0, via Wikimedia Commons</p></section>

<section class="sec fg-diff"><div class="wrap fg-diff-in">
<div class="fg-diff-h reveal"><p class="label">The Pestx difference</p><h2>Enjoy every moment <em>with peace of mind.</em></h2><p>Protect your family&rsquo;s health and well-being. Effective pest control makes a safer, healthier home, so you can enjoy life&rsquo;s moments.</p>{img("ink-leaf", "", lazy=True, cls="fg-leaf")}</div>
<ol class="notes">
<li class="reveal"><span class="n-no">Note I</span><h3>Smart &amp; trusted</h3><p>Eco-friendly, targeted treatments keep you safe while having minimal impact on the environment.</p></li>
<li class="reveal"><span class="n-no">Note II</span><h3>Family owned</h3><p>Founded by two brothers, Pestx brings a personal touch to pest control: trusted, high-quality service from experts who care.</p></li>
<li class="reveal"><span class="n-no">Note III</span><h3>Utah local experts</h3><p>As Utah locals, we understand the region&rsquo;s unique pest challenges and tailor our solutions to what works here.</p></li>
</ol></div></section>

<section class="cover" id="coverage"><div class="wrap">
<div class="cover-h reveal"><p class="label">Full home coverage</p><h2>Seven places pests live. <em>Tap a letter.</em></h2><p>Every space, indoors and out, from the eaves to the basement. Pick a zone to see which Utah pests turn up there and how they get in.</p></div>
<div class="cover-in" data-house><div class="cover-art">{house_svg()}<div class="hz-chips" role="tablist" aria-label="Zones">{"".join(f'<button type="button" data-zc="{i}"{" class=on" if i == 0 else ""}><b>{l}</b> {n}</button>' for i, (l, n, x, y, p) in enumerate(ZONES))}</div></div>
<div class="cover-panel" aria-live="polite">{zone_panels()}</div></div>
</div></section>

<section class="sec fg-guide"><div class="wrap">
<div class="split-head reveal"><div><p class="label">Common Utah pests</p><h2>The field guide.</h2></div><p class="lede">How to identify Utah&rsquo;s most common pests, how to get rid of them, and how to keep them from coming back. Ten species, one page each.</p></div>
{guide_grid()}
</div></section>

<section class="sec fg-year"><div class="fy-img">{img("px-sandy", "Homes in the Salt Lake Valley below the Wasatch in autumn")}</div><div class="wrap fg-year-in">
<div class="reveal"><p class="label">Year-round protection</p><h2>Peace of mind should never have <em>an off-season.</em></h2>
<p>The ultimate all-season pest control coverage: month-to-month protection that adapts as Utah&rsquo;s seasons change, from the first mosquitoes of late spring to the boxelder bugs on sunny walls in the fall.</p>
<a class="btn" href="@/contact/">Sign Up Now {ARROW}</a></div>
<div class="reveal">{seasons()}<p class="sz-note">Seasons as described on each pest&rsquo;s page. The red line is this month.</p></div>
</div></section>

<section class="sec fg-promise"><div class="wrap fg-promise-in">
<figure class="fg-fam reveal">{img("ink-family", "Ink drawing of a family walking together")}</figure>
<div class="reveal"><p class="label">The Pestx guarantee</p><blockquote>&ldquo;Our technicians will return as often as necessary to ensure you are satisfied.&rdquo;</blockquote>
<div class="promises"><div><b>Satisfaction guaranteed</b><p>Not satisfied? Our technicians come back until you are.</p></div><div><b>Pet-friendly pest control</b><p>Eco-friendly practices that remove the dangers pests pose to your animals.</p></div></div></div>
</div></section>

<section class="sec fg-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Everything you need to know</p><h2>Questions, answered.</h2>{faq_html(HOME_FAQ)}<p class="more">More questions? Call <a href="tel:+18018719233">801-871-9233</a>.</p></div>
<div class="reveal">{K.form("Get a Quote", [("city", "City")], "Comments")}</div>
</div></section>

<section class="sec fg-notes"><div class="wrap">
<div class="split-head reveal"><div><p class="label">Natural pest control solutions</p><h2>From the notebook.</h2></div><p class="lede">Knowledge for keeping a safe, healthy and protected home.</p></div>
<div class="nb">{"".join(f'<a class="nb-card reveal" href="@/{p}"><span class="fg-no">{d}</span><b>{t}</b><p>{x}</p><em>Read {ARROW}</em></a>' for p, t, d, x in POSTS)}</div>
</div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": "Pest Control Midvale, UT | Pestx Family-Owned Pest Control",
            "meta": "Family-owned pest control in Midvale, Utah: eco-friendly, targeted treatments for ants, spiders, rodents, wasps and more, with year-round protection plans.",
            "body": body, "body_class": "is-home", "og": "ink-house", "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


POSTS = [("blogs/ticks-in-utah/", "Ticks in Utah: where they live, when they bite, and what to do", "Oct 21, 2026", "Snowmelt to mid-July is tick season in Utah. Which ticks you&rsquo;ll meet, and how to remove one."),
         ("blogs/is-pest-control-safe-for-pets/", "Is Pest Control Safe for Pets?", "Feb 1, 2025", "Safe, natural solutions that keep bugs away while protecting your furry friends."),
         ("blogs/how-bugs-get-inside-your-home/", "How Bugs Get Inside Your Home", "Feb 1, 2025", "The common ways bugs sneak in, and how to seal your home to keep them out."),
         ("blogs/does-one-spray-work-for-most-bugs/", "Does One Spray Work for Most Bugs?", "Feb 1, 2025", "Why different pests need different approaches for long-term control.")]
