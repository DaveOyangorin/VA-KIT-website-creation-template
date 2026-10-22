from build import (SITE, ARROW, PHONE, img, cta_band, faq_html, faq_schema, crumbs_schema, BIZ_ID, crumbs_html)

U = SITE["url"] + "/"
NDSU = "https://www.ag.ndsu.edu/news/newsreleases/2023/january/reduce-ice-dam-and-icicle-damage"
UOU = "https://www.inscc.utah.edu/~steenburgh/utah_climo/snowstorms.html"
DOE = "https://www.energy.gov/sites/prod/files/guide_to_cool_roofs.pdf"
PATH = "blog/how-long-do-roofs-last-in-utah/"

# Main keyword: "how long do roofs last in utah" (question / Tier 3 - blog only)
# Supporting long-tail: roof lifespan in Utah, how long does a shingle roof last, how long does a metal roof last,
# signs you need a new roof, does snow shorten roof life.
# Deliberately NOT targeted here (they belong to service pages): roofing company salt lake city,
# roof repair salt lake city, roof replacement salt lake city, commercial roofing salt lake city.

FAQ = [
    ("Does snow shorten a roof's life?",
     "Snow on its own is rarely the problem. The damage comes from meltwater refreezing at the eaves into ice dams, from freeze-thaw cycles opening small cracks, and from heavy loads on weak framing. A well-vented, well-flashed roof handles Utah snow fine for its full life."),
    ("How long does a metal roof last in Utah?",
     "Metal roofs last a long time and may come with a lifetime warranty. They shed snow well and need little maintenance, which suits Utah winters. The fasteners, seals and flashing still need checking over the years, so plan on occasional inspections rather than none at all."),
    ("Can a roof last longer than its warranty?",
     "Yes. A warranty is the manufacturer's promise, not an expiry date. Roofs that were installed carefully, vented properly and kept clear of debris often outlast it. Roofs with poor ventilation or neglected leaks can fail well before it, so the warranty is only a rough guide."),
    ("How often should a Utah roof be inspected?",
     "Once a year is a sensible habit, ideally in late summer or fall before snow arrives, plus a quick look after any big wind or hail storm. Commercial roofs with foot traffic and rooftop equipment benefit from a scheduled maintenance program with more frequent checks."),
    ("Is it worth repairing a 20-year-old shingle roof?",
     "It can be, if the damage is in one spot and the rest of the roof is sound. If the shingles are curling everywhere, gutters are full of granules or leaks keep appearing in new places, money spent on repairs is better put toward a replacement."),
]

TOC = [("by-material", "Roof lifespan in Utah by material"), ("weather", "How Utah weather ages a roof"),
       ("what-decides", "What decides how long your roof lasts"), ("signs", "Signs your roof is near the end"),
       ("repair-or-replace", "Repair or replace?"), ("last-longer", "How to make a Utah roof last longer"),
       ("timing", "When to schedule roof work"), ("faq", "Questions")]
toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in TOC)

ART = f'''
<div class="answer"><strong>Short answer:</strong> most asphalt shingle roofs in Utah carry 20- to 30-year warranties, and metal roofs can come with lifetime warranties. How long yours really lasts depends on how well it was installed, how well the attic is vented, and how hard snow, ice and high-altitude sun hit it. Trouble usually starts at the eaves and flashing first.</div>

<p>We get this question on almost every roof we look at in Salt Lake City. The honest answer is "it depends," but it depends on things you can check. This guide walks through each material, how our weather wears roofs down, the warning signs to look for, and what you can do to get more years out of the roof you have.</p>

<div class="toc"><h3>In this guide</h3><ol>{toc_html}</ol></div>

<h2 id="by-material">Roof lifespan in Utah by material</h2>
<p>Material sets the ceiling on how long a roof can last. Installation and upkeep decide whether you get anywhere near it. Here's how the common options compare for Utah homes and buildings.</p>
<div class="table-wrap"><table>
<thead><tr><th>Material</th><th>Lifespan guide</th><th>Utah notes</th></tr></thead>
<tbody>
<tr><td>Asphalt (composition) shingles</td><td>Generally guaranteed 20–30 years</td><td>Most common and least expensive. Sun and ice dams wear the edges first.</td></tr>
<tr><td>Metal panels or tiles</td><td>Long life; may carry a lifetime warranty</td><td>Sheds snow well and needs little upkeep. Costs a bit more than double asphalt.</td></tr>
<tr><td>Concrete or clay tile</td><td>Comparable to metal</td><td>Very heavy, so the framing must be checked. Can mimic wood or slate.</td></tr>
<tr><td>Wood shakes and shingles</td><td>Shakes outlast thinner wood shingles</td><td>Shakes handle hail well. Less common now because of fire concerns.</td></tr>
<tr><td>Flat commercial membranes</td><td>Depends on the membrane and maintenance</td><td>Ponding water and foot traffic shorten life; a maintenance program extends it.</td></tr>
</tbody></table></div>
<p>A warranty isn't a promise that the roof will last that long. It's the manufacturer's coverage on the material. The figure that matters to you is service life, and that's where Utah weather comes in. For a deeper look at each material, see our <a href="@/residential/">residential roofing</a> page.</p>

<figure>{img("snow-on-roof-edge", "Thick layer of snow hanging over the edge of a roof")}<figcaption>Snow on the roof is normal. Water that refreezes at the edge is what does the damage.</figcaption></figure>

<h2 id="weather">How Utah weather ages a roof</h2>
<p>Salt Lake City sits at about 4,300 feet. That gives us cold, snowy winters, hot dry summers and strong sun most of the year. Each one wears a roof in its own way.</p>

<h3>Snow and lake-effect storms</h3>
<p>According to the University of Utah's <a href="{UOU}" rel="noopener">Salt Lake Valley snowstorm climatology</a>, Salt Lake City International Airport averages about 65 inches of snow a year, and the populated benches around the valley get closer to 100 inches. The same source notes that the Great Salt Lake produces localized snowbands several times each winter. If you live on the east bench or up a canyon, your roof sees a lot more snow than the airport does.</p>

<h3>Ice dams</h3>
<p>Ice dams are the biggest winter threat to Utah roofs. North Dakota State University Extension explains how they form: <a href="{NDSU}" rel="noopener">heat escaping into the attic melts the snow</a>, and when that meltwater reaches the colder eaves, it freezes. The ice builds into a ridge, and water backs up behind it and under the shingles. That's why so many winter leaks show up along exterior walls.</p>

<h3>Freeze-thaw cycles</h3>
<p>Valley winters often swing above and below freezing in a single day. Water gets into a small crack, freezes, expands, and makes the crack a little bigger. Over a few winters, that cycle loosens flashing, opens seams on flat roofs and breaks down sealant around vents.</p>

<h3>Sun at altitude</h3>
<p>Sunlight is harsher at elevation, and our summers are dry and bright. UV dries out asphalt shingles, which makes them brittle and quick to shed their protective granules. South- and west-facing slopes usually age first. On commercial roofs, reflectivity also affects how hot the roof gets; the U.S. Department of Energy's <a href="{DOE}" rel="noopener">Guide to Cool Roofs</a> notes that many roofs lose reflectivity over time.</p>

<h3>Wind and hail</h3>
<p>Spring and summer storms can lift shingle edges, crack tiles and dent metal. One storm rarely ends a roof's life, but unrepaired storm damage lets water in and speeds up everything above.</p>

<h2 id="what-decides">What decides how long your roof lasts</h2>
<p>Two roofs with the same shingles, on the same street, can last very different lengths of time. These are the reasons why.</p>
<ul>
<li><strong>Installation quality.</strong> Nailing, starter strips, underlayment and flashing details are invisible from the ground but decide how the roof handles water and wind.</li>
<li><strong>Attic ventilation.</strong> A cold, well-vented roof deck resists ice dams and keeps shingles from baking. One of our clients told us that after their roof was replaced and vented properly, it was "the first winter we did not need to use a space heater in one particular room" in 20 years.</li>
<li><strong>Insulation and air sealing.</strong> Warm air leaking from the house is what melts the snow in the first place. NDSU Extension suggests attics in northern climates need roughly 15 inches of blown-in insulation, and that gaps around pipes, wiring, recessed lights and attic hatches should be sealed.</li>
<li><strong>Drainage and gutters.</strong> Water and snow have to leave the roof. Blocked gutters and drains let ice and water build up right where the roof is weakest.</li>
<li><strong>Maintenance.</strong> A loose piece of flashing caught early is a small repair. Left for two winters, it can mean a rotten deck.</li>
<li><strong>Foot traffic and other trades.</strong> On commercial buildings, HVAC and satellite technicians walking on the roof can damage it without anyone noticing.</li>
</ul>

<h2 id="signs">Signs your roof is near the end</h2>
<p>You can spot most of these from the ground, from the attic or by looking in your gutters. Don't climb onto a steep, wet or icy roof to check.</p>
<ol>
<li>Shingles curling, cupping or cracking across large areas of the roof</li>
<li>Bald patches and lots of granules collecting in gutters and at downspouts</li>
<li>Leaks that keep showing up in different rooms</li>
<li>Daylight or water stains on the underside of the roof deck in the attic</li>
<li>A deck that looks wavy or sags between rafters</li>
<li>Flashing that's rusted, loose or was patched over with tar more than once</li>
<li>Big ice dams and icicles every winter, even after repairs</li>
</ol>
<p>One or two of these may only call for a repair. Several at once usually mean it's time to start planning a new roof.</p>

<figure>{img("shingle-roof-homes", "Gabled asphalt shingle roofs on two-story homes")}<figcaption>Valleys, eaves and the joints around dormers are where most shingle roofs start to fail.</figcaption></figure>

<h2 id="repair-or-replace">Repair or replace?</h2>
<p>A simple way to think about it: if the problem is local and the roof is otherwise healthy, repair it. If the problems are spread out or keep coming back, the money is better spent on replacement.</p>
<div class="table-wrap"><table>
<thead><tr><th>Lean toward repair</th><th>Lean toward replacement</th></tr></thead>
<tbody>
<tr><td>Damage from one storm, branch or vent</td><td>Leaks in several places, or the same leak coming back</td></tr>
<tr><td>A handful of missing or cracked shingles</td><td>Curling, bald or brittle shingles across the roof</td></tr>
<tr><td>Roof is well within its warranty period</td><td>Roof is near or past the end of its warranty</td></tr>
<tr><td>Deck is solid underfoot</td><td>Deck is soft, rotten or sagging</td></tr>
</tbody></table></div>
<p>If you're in the Salt Lake Valley and aren't sure which side you're on, our <a href="@/roof-repair/">roof repair</a> crew will look and tell you honestly. For businesses, our <a href="@/commercial/">commercial roofing</a> page covers re-roofing and maintenance programs.</p>

<h2 id="last-longer">How to make a Utah roof last longer</h2>
<p>Most of these cost little or nothing, and they add years.</p>
<ol>
<li><strong>Get a roof check every fall.</strong> Have flashing, seals and vents looked at before snow arrives, and again after any big storm.</li>
<li><strong>Clean gutters in late fall and spring.</strong> Clear leaves before the first freeze so meltwater has somewhere to go.</li>
<li><strong>Fix attic ventilation and insulation.</strong> Balanced intake at the soffits and exhaust near the ridge, plus air sealing, keeps the deck cold and prevents ice dams.</li>
<li><strong>Deal with small leaks right away.</strong> A stain on the ceiling is a sign water has been getting in for a while.</li>
<li><strong>Clear heavy snow from the ground.</strong> A roof rake used from the ground can pull snow off the lower edge. Leave anything higher to a pro.</li>
<li><strong>Keep other trades honest.</strong> Ask HVAC, solar and satellite installers to protect the roof and to tell you if they've cut or moved anything up there.</li>
</ol>
<p>On low-slope sections, balconies and flat roofs, <a href="@/waterproofing/">waterproofing</a> can add years by keeping water out of the seams where freeze-thaw does its damage.</p>

<h2 id="timing">When to schedule roof work in Salt Lake City</h2>
<p>Shingles seal best in warm, dry weather, so late spring through fall is the main roofing season here. Repairs, though, can't always wait. A leak in January still needs fixing, and a good crew can make safe temporary or permanent repairs in winter.</p>
<p>The smart move is to book an inspection in late summer or early fall. That leaves time to schedule repairs, or a replacement if you need one, before the first big storm rolls off the lake.</p>

<h2 id="faq">Questions about roof lifespan in Utah</h2>
{faq_html(FAQ)}

<h2>Not sure how much life your roof has left?</h2>
<p>Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> or <a href="@/get-a-quote/">request a free quote</a>. We'll look at your roof, take photos of anything that needs attention, and tell you straight whether it needs a repair, a little maintenance or a full replacement.</p>

<h3>Sources</h3>
<ul style="font-size:.92rem">
<li>University of Utah, Department of Atmospheric Sciences: <a href="{UOU}" rel="noopener">Salt Lake Valley Snowstorms</a></li>
<li>North Dakota State University Extension: <a href="{NDSU}" rel="noopener">Reduce ice dam and icicle damage</a> (January 2023)</li>
<li>U.S. Department of Energy: <a href="{DOE}" rel="noopener">Guide to Cool Roofs</a></li>
<li>Material warranty ranges: Advanced Roofing &amp; Moisture Control's <a href="@/residential/">residential roofing materials guide</a></li>
</ul>
'''

HERO = f'''<section class="page-hero">{img("herriman-winter-aerial", "Aerial view of a snowy Utah neighborhood below the mountains", priority=True)}<span class="diag" aria-hidden="true"></span>
<div class="wrap">{crumbs_html([("Home", ""), ("Blog", "blog/"), ("How Long Do Roofs Last in Utah?", PATH)])}
<p class="eyebrow light">Roof lifespan guide</p><h1>How Long Do Roofs Last in Utah?</h1>
<p class="lede">Shingles, metal, tile and wood, and what Wasatch winters do to each of them. A plain guide from a Salt Lake City roofer.</p>
<div class="byline"><span>By the {SITE["name"]} team</span><span>Published <time datetime="2026-10-16">October 16, 2026</time></span><span>About 9 minutes to read</span></div></div></section>'''

POST = {
    "path": PATH,
    "title": "How Long Do Roofs Last in Utah? Lifespan by Material",
    "meta": "How long do roofs last in Utah? See lifespan by material, how snow, ice dams and sun wear roofs down, the warning signs, and how to make yours last longer.",
    "ogtype": "article", "og": "herriman-winter-aerial", "active": "blog/", "full_biz": False,
    "body": HERO + f'''<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>
<aside class="side"><div class="card-cta"><p class="eyebrow light">Free roof check</p><h3>Want a straight answer on your roof?</h3><p>We'll inspect it and tell you how much life it has left.</p>
<a class="phone-big" href="tel:{SITE["tel"]}">{SITE["phone"]}</a><a class="btn" href="@/get-a-quote/">Get a Quote {ARROW}</a></div>
<div class="card-list"><h3>Related</h3><ul><li><a href="@/roof-repair/">Roof repair in Salt Lake City</a></li><li><a href="@/residential/">Residential roofing</a></li><li><a href="@/commercial/">Commercial roofing</a></li><li><a href="@/waterproofing/">Waterproofing</a></li></ul></div></aside>
</div></section>''' + cta_band("Is your roof ready for winter?", "Book a roof check before the first big storm. It's free, and you'll know where you stand."),
}
POST["schema"] = [
    {"@type": "BlogPosting", "@id": U + PATH + "#article", "headline": "How Long Do Roofs Last in Utah?",
     "description": POST["meta"], "url": U + PATH, "mainEntityOfPage": U + PATH,
     "image": U + "assets/img/herriman-winter-aerial.webp", "datePublished": "2026-10-16", "dateModified": "2026-10-16",
     "inLanguage": "en-US", "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID},
     "about": ["Roof lifespan", "Utah climate", "Ice dams"], "isPartOf": {"@id": U + "blog/#blog"}},
    faq_schema(FAQ),
    crumbs_schema([("Home", ""), ("Blog", "blog/"), ("How Long Do Roofs Last in Utah?", PATH)]),
]

INDEX = {
    "path": "blog/",
    "title": "Roofing Blog: Utah Roof Care & Advice | Advanced Roofing",
    "meta": "Practical roofing advice for Utah homeowners and property managers from Advanced Roofing & Moisture Control in Salt Lake City. Roof life, winter care and more.",
    "og": "herriman-winter-aerial", "full_biz": False,
    "body": f'''<section class="page-hero">{img("slc-skyline-snowy-wasatch", "Downtown Salt Lake City under the snow-covered Wasatch Mountains", priority=True)}<span class="diag" aria-hidden="true"></span>
<div class="wrap">{crumbs_html([("Home", ""), ("Blog", "blog/")])}<p class="eyebrow light">Roof care &amp; advice</p><h1>The Roofing Blog</h1>
<p class="lede">Straight answers about roofs in Utah's climate, from the crew that fixes them.</p></div></section>
<section class="sec"><div class="wrap split" style="align-items:start">
<a class="post-card reveal" href="@/{PATH}">{img("herriman-winter-aerial", "Aerial view of a snowy Utah neighborhood below the mountains")}
<div class="body"><p class="eyebrow">Roof lifespan &middot; Oct 16, 2026</p><h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">How Long Do Roofs Last in Utah?</h2>
<p class="muted">Lifespan by material, what snow, ice dams and sun do to a roof, and the signs it's time for a new one.</p><span class="textlink">Read the guide {ARROW}</span></div></a>
<div class="reveal d1"><p class="eyebrow">More coming</p><h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">Got a roofing question?</h2>
<p>Ask us when you call. The best questions become posts here.</p><a class="btn dark" href="@/contact/">Ask a question {ARROW}</a></div>
</div></section>''' + cta_band(),
    "schema": [{"@type": "Blog", "@id": U + "blog/#blog", "url": U + "blog/", "name": "The Roofing Blog", "publisher": {"@id": BIZ_ID}},
               crumbs_schema([("Home", ""), ("Blog", "blog/")])],
}

PAGES = [INDEX, POST]
