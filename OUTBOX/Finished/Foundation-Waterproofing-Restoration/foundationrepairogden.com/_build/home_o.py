"""Home page for foundationrepairogden.com: "Fortified".
Hero: an engraved "plate" of a house on a cut-stone foundation over Weber clay, a stair-step crack through the courses.
Signature, "Heave or settle?": the client's own FAQ says heaving comes from hard compact clay that expands whenever it gets wet,
"like a dry, solid sponge", and that heaving foundations are often diagnosed as settlement. Drag the moisture gauge and the clay
cells swell and push the basement floor up in the middle; switch to settlement and the same floor drops at one side instead.
Both crack the floor, differently, which is why the client says the only way to know is an evaluation on site."""
import random
from engine import faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, AREAS, HOURS
from pagekit import ARROW, PHONE, HOME, form, cta
import p_blog

FAQ = [("How will I know if there is an issue with my home&rsquo;s foundation?", "There&rsquo;s only one way to know for sure and that is by hiring a foundation estimator to conduct an evaluation on site. If there&rsquo;s an apparent issue with the foundation, the estimator will offer a price quote and a repair plan to remedy it."),
       ("What can cause a foundation to heave?", "Heaving is usually caused by the expansion of hard compact clays due to the presence of water. It&rsquo;s like a dry, solid sponge which expands whenever it gets wet. Most of the time, foundations that are heaving are diagnosed as settlement."),
       ("What would happen if a foundation repair is delayed or ignored?", "Each case is unique on its own. However, most conditions worsen as time passes. Foundation damage can cause roof trusses to be unstable, making your windows and doors inoperable."),
       ("How long does a foundation crack repair take?", "A foundation crack repair usually takes about a week to complete. It can take less or more time; it all depends on the extent of the damage.")]
SERVICES = [("Foundation repair", "Basement cracks or foundation slipping"), ("Foundation cracks", "Wall, floor and basement cracks"), ("Basement waterproofing", "Keep your cellar dry and your home safe"),
            ("Emergency water removal", "When water is already in"), ("Wall cracks", "Cracks in foundation and basement walls"), ("Uneven floors", "Sagging and sloping floors"),
            ("Concrete", "Stamped, epoxy, or just plain patios"), ("Block foundations", "Repairs to block walls"), ("Flooded basements", "Water in the basement"),
            ("Foundation inspection", "We can tell you if anything&rsquo;s off in your basement"), ("Foundation forms", "Forms for new foundation work")]
TOWNS = [("Roy", "foundation-repair-roy-weber-county/"), ("Layton", "layton-84040-concrete-company/"), ("Clearfield", "clearfield-foundation/"), ("Kaysville", "foundation-kaysville-ut/"),
         ("Syracuse", "foundation-experts-syracuse-utah/"), ("Hooper", "hooper-ut-foundationservice/"), ("Hill AFB", "foundation-companies-hill-afb/"), ("Eden", "eden-ut-foundationservices/")]
MODES = [("Heave", "Wet clay swells", "Heaving is usually caused by the expansion of hard compact clays due to the presence of water. It&rsquo;s like a dry, solid sponge which expands whenever it gets wet."),
         ("Settlement", "One side drops", "Most of the time, foundations that are heaving are diagnosed as settlement. From inside, both crack the floor; the pattern is different, which is why the only way to know for sure is an evaluation on site.")]


def stones(x0, y0, w, h, rows, rw=58, cls="st"):
    out, y, rh = [], y0, h / rows
    for r in range(rows):
        x = x0 - (rw / 2 if r % 2 else 0)
        while x < x0 + w:
            a, b = max(x, x0), min(x + rw, x0 + w)
            if b - a > 4: out.append(f'<rect class="{cls}" x="{a:.0f}" y="{y:.0f}" width="{b - a - 3:.0f}" height="{rh - 3:.0f}"/>')
            x += rw
        y += rh
    return "".join(out)


def hatch(x0, y0, w, h, step=9):
    return "".join(f'<line x1="{x0 + i:.0f}" y1="{y0}" x2="{x0 + i - h * .5:.0f}" y2="{y0 + h}"/>' for i in range(0, int(w + h * .5), step))


def plate():
    return f'''<svg class="plate" viewBox="0 0 520 620" role="img" aria-label="Engraving-style drawing of a house on a cut-stone foundation over clay, with a stair-step crack through the stone courses">
<rect class="pl-bg" x="0" y="0" width="520" height="620"/><rect class="pl-frame" x="14" y="14" width="492" height="592"/>
<text class="pl-cap" x="34" y="48">PLATE I</text><text class="pl-cap r" x="486" y="48">THE FOUNDATION</text>
<path class="pl-mtn" d="M34 210 L120 150 L160 172 L230 96 L290 150 L330 128 L410 190 L486 166"/>
<path class="pl-house" d="M110 300 V196 L260 120 L410 196 V300"/><rect class="pl-win" x="150" y="222" width="46" height="46"/><rect class="pl-win" x="324" y="222" width="46" height="46"/><rect class="pl-door" x="238" y="236" width="44" height="64"/>
<line class="pl-ground" x1="34" y1="300" x2="486" y2="300"/>
<g class="pl-clay">{hatch(34, 300, 452, 270)}</g>
<g class="pl-wall">{stones(96, 300, 328, 190, 6)}</g>
<rect class="pl-foot" x="84" y="490" width="352" height="26"/>
<path class="pl-crack" d="M300 300 L300 332 L330 332 L330 364 L272 364 L272 396 L300 396 L300 428 L242 428 L242 460"/>
<text class="pl-cap" x="34" y="592">WEBER CLAY</text><text class="pl-cap r" x="486" y="592">OGDEN, UTAH</text>
</svg>'''


def mini_art(label):
    return (f'<div class="art-card"><svg class="mini" viewBox="0 0 300 180" aria-hidden="true"><rect class="pl-bg" width="300" height="180"/><line class="pl-ground" x1="0" y1="60" x2="300" y2="60"/>'
            f'<g class="pl-clay">{hatch(0, 60, 300, 120, 10)}</g><g class="pl-wall">{stones(40, 60, 220, 90, 3, 44)}</g><rect class="pl-foot" x="30" y="150" width="240" height="14"/></svg><span>{label}</span></div>')


def heave_svg():
    random.seed(7)
    cells = "".join(f'<circle class="cell" cx="{x}" cy="{y}" r="{random.choice((11, 13, 15))}" style="--d:{random.random() * .6:.2f}s"/>' for y in range(372, 470, 26) for x in range(130 + (y // 26 % 2) * 13, 790, 26))
    drops = "".join(f'<path class="drop" d="M{x} {y} q5 9 0 12 q-5 -3 0 -12z"/>' for x, y in ((180, 390), (300, 430), (450, 400), (590, 445), (700, 395), (380, 455), (520, 380)))
    return f'''<svg class="heave-svg" viewBox="0 0 900 500" role="img" aria-labelledby="hv-t">
<title id="hv-t">Drawing of a basement on clay soil. Wet clay swells and pushes the floor up in the middle (heave); in settlement mode one side of the floor drops instead.</title>
<defs><clipPath id="soil"><rect x="0" y="330" width="900" height="170"/></clipPath></defs>
<rect class="hv-sky" width="900" height="150"/>
<rect class="hv-earth" x="0" y="150" width="900" height="350"/>
<g class="hv-hatch">{hatch(0, 150, 900, 180, 14)}</g>
<g clip-path="url(#soil)" class="hv-cells">{cells}</g>
<g class="hv-drops">{drops}</g>
<path class="hv-house" d="M190 150 V70 L450 14 L710 70 V150"/>
<g class="hv-walls" data-walls><rect class="hv-wall" x="190" y="150" width="34" height="190"/><rect class="hv-wall wr" x="676" y="150" width="34" height="190"/>
<rect class="hv-foot" x="176" y="338" width="62" height="20"/><rect class="hv-foot fr" x="662" y="338" width="62" height="20"/></g>
<path class="hv-slab" data-slab d="M224 318 Q450 318 676 318 L676 340 Q450 340 224 340 Z"/>
<path class="hv-crack" data-crack d="M450 300 L444 312 L456 322 L448 340"/>
<path class="hv-void" data-void d="M600 340 Q660 372 720 344 L720 360 Q660 392 596 356 Z"/>
<line class="hv-level" x1="224" y1="318" x2="676" y2="318"/>
<text class="hv-read" x="24" y="40" data-read>DRY</text>
</svg>'''


CREDIT = ("Historic photographs: Ogden, Utah, and Ogden Canyon, 1870s, by William Henry Jackson and others, U.S. National Archives "
          "(public domain, via Wikimedia Commons). Shown for atmosphere; not Fortified Foundations&rsquo; work.")


def home():
    svcs = "".join(f'<li><span class="lg-n">{i + 1:02d}</span><b>{t}</b><em>{d}</em></li>' for i, (t, d) in enumerate(SERVICES))
    towns = "".join(f'<a class="stone" href="@/{p}"><b>{t}</b><span>Foundation &amp; waterproofing {ARROW}</span></a>' for t, p in TOWNS)
    marquee = "".join(f"<span>{t}</span>" for t, p in TOWNS) * 2
    modes = "".join(f'<button type="button" data-mode="{i}" aria-pressed="{"true" if i == 0 else "false"}"><b>{m}</b><span>{s}</span></button>' for i, (m, s, d) in enumerate(MODES))
    mtxt = "".join(f'<div class="hv-tx{" on" if i == 0 else ""}" data-i="{i}"><p class="hv-k">{m}</p><p>{d}</p></div>' for i, (m, s, d) in enumerate(MODES))
    body = f'''
<section class="v-hero">
<figure class="v-hero-bg" data-par="0.18"><img src="@img/og-hero.webp" alt="The Wasatch Mountains above Ogden, Utah, in a photograph from the 1870s" width="2000" height="1000" fetchpriority="high"></figure>
<div class="wrap v-hero-in">
<p class="v-kick"><span>Fortified Foundations</span><span>Ogden, Utah</span><span>Every day 7am&ndash;11pm</span></p>
<h1 class="v-h1"><span class="ln"><span>Foundation repair</span></span><span class="ln"><span>in Ogden,</span></span><span class="ln"><em>solid as stone.</em></span></h1>
<div class="v-hero-foot">
<p class="lede">Fortified Foundations does foundation repair in Ogden and nearby towns: foundation and wall cracks, basement waterproofing, uneven floors, concrete and foundation inspections. An estimator looks at it on site and gives you a quote and a repair plan.</p>
<div class="v-ticket"><small>Call any day, 7 a.m.&ndash;11 p.m.</small><a href="tel:+13852132324">(385) 213-2324</a><a class="btn accent" href="@/contact/">Free estimate {ARROW}</a></div>
</div></div>
<p class="v-plate">Plate I &middot; Ogden, Utah, 1870s &middot; U.S. National Archives</p>
</section>
<div class="v-marq" aria-hidden="true"><div class="v-marq-in">{marquee}</div></div>

<section class="sec v-state"><div class="wrap v-state-in">
<p class="o-num reveal-up">I. &nbsp;The ground</p>
<p class="v-big reveal-up">The mountains in that photograph are the same ones over Ogden today. <em>Your house stands on what washed down from them.</em> We look at what&rsquo;s under it.</p>
<figure class="v-plate-art reveal-up">{plate()}</figure>
</div></section>

<section class="sec ledger-sec"><div class="wrap ledger-in">
<div class="o-head reveal-up"><p class="o-num">II. &nbsp;The work</p><h2>Everything a foundation <em>can go wrong with.</em></h2><p class="lede">From a hairline crack to a flooded basement. Every job starts the same way: an evaluation on site.</p><a class="tlink" href="@/services/">All services {ARROW}</a></div>
<ol class="ledger reveal-up">{svcs}</ol>
</div></section>

<section class="heave-sec" id="heave"><div class="wrap">
<div class="o-head light reveal-up"><p class="o-num">III. &nbsp;Heave or settle?</p><h2>Clay is a dry sponge. <em>Add water.</em></h2>
<p class="lede">Hard, compact clay swells when it gets wet. Drag the gauge to wet it and watch the floor; then switch to settlement and compare. Both crack a basement floor, in different ways.</p></div>
<div class="heave" data-heave data-mode="0">
<div class="hv-draw"><div class="hv-canvas">{heave_svg()}</div>
<label class="hv-gauge"><span data-glabel>Moisture in the clay</span><input class="hv-range" type="range" min="0" max="100" step="1" value="0" aria-label="Moisture in the clay, dry to wet"><i>Dry</i><i>Wet</i></label>
<p class="hv-note">Drawing for illustration &middot; exaggerated to show the difference</p></div>
<div class="hv-panel"><div class="hv-modes" role="group" aria-label="What is happening under the floor">{modes}</div><div class="hv-texts" aria-live="polite">{mtxt}</div>
<p class="hv-src">The explanation is Fortified Foundations&rsquo; own.</p><a class="btn accent" href="@/contact/">Book an evaluation {ARROW}</a></div>
</div></div></section>

<section class="v-canyon"><div class="v-canyon-ph" data-par="0.12"><img src="@img/og-canyon-tall.webp" alt="Ogden Canyon in a photograph from the 1870s" width="1200" height="1714" loading="lazy"></div>
<div class="wrap v-canyon-in"><div class="v-canyon-card reveal-up"><p class="o-num">IV. &nbsp;How it goes</p><h2>One visit, <em>then a plan.</em></h2>
<ol class="how"><li><b>Call or send the form</b><span>(385) 213-2324, any day from 7 a.m. to 11 p.m.</span></li>
<li><b>Evaluation on site</b><span>A Fortified Foundations employee comes to your home and analyzes your foundation, including cracks in the basement walls.</span></li>
<li><b>Quote and repair plan</b><span>If there&rsquo;s an issue, you get a price quote and a repair plan to remedy it.</span></li>
<li><b>The repair</b><span>A foundation crack repair usually takes about a week, depending on the extent of the damage.</span></li></ol></div></div>
<p class="v-plate">Plate II &middot; Ogden Canyon, 1870s &middot; U.S. National Archives</p></section>

<section class="sec towns-sec"><div class="wrap">
<div class="o-head reveal-up"><p class="o-num">V. &nbsp;Where we work</p><h2>Ogden, and the towns <em>around it.</em></h2></div>
<div class="masonry reveal-up">{towns}</div>
</div></section>

<section class="sec faq-sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="o-num">VI. &nbsp;Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span>New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{form("Get a free estimate", msg_label="What are you seeing? Cracks, water, uneven floors?")}</div>
</div></section>
<div class="wrap"><p class="v-credit">{CREDIT}</p></div>
'''
    return {"path": "", "canonical": U, "title": "Foundation Repair Ogden, UT | Fortified Foundations",
            "meta": "Foundation repair in Ogden, UT: foundation and wall cracks, basement waterproofing, uneven floors, concrete and inspections. Call (385) 213-2324, 7am to 11pm.",
            "body": body + cta(), "og": "og-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
