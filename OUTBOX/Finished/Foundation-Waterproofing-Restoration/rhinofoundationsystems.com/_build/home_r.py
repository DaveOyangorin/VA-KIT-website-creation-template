"""Home page for rhinofoundationsystems.com: "Down to solid ground".
Signature, "Drive the pier": a drawn section through the ground under a settling house. Drag the depth gauge and a helical pier
goes down through loam, silt, clay and sand; each layer reads back Rhino's own description of how that soil behaves under a house.
Once the pier passes the frost line (Rhino: helical piers anchor "below the frost line" and "evenly distribute the weight") the
house rotates back to level and the wall crack closes. Labelled as an illustration: real layers vary from lot to lot."""
from engine import img, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME
from pagekit import ARROW, PHONE, HOME, form
import p_blog

LAYERS = [  # name, top, bottom, colour class, client's own words
    ("Loam", 170, 232, "lo", "Loam is the ideal soil for foundations due to its balanced composition of clay, sand, and silt. It offers excellent drainage, minimal expansion or contraction, and strong support."),
    ("Silt", 232, 302, "si", "Silt soil retains moisture better than sand and provides moderate support when compacted. Unfortunately, it is highly prone to water retention and frost heave, causing foundation settling and shifting."),
    ("Clay", 302, 382, "cl", "Clay soil is dense and provides good load-bearing capacity when dry. However, it expands significantly when wet, leading to potential foundation movement, cracks, and structural instability."),
    ("Sand", 382, 450, "sa", "Sand soil provides good drainage. However, its loose, granular nature makes it prone to shifting or displacement under heavy loads."),
    ("Below the frost line", 450, 560, "be", "Helical piers are installed like a corkscrew, deeply anchoring the foundation below the frost line. Once in place, they evenly distribute the weight of the structure, stabilizing the foundation and preventing future settlement or shifting."),
]
QUOTES = [("Chase and Casey visited our house, and we explained the flooding situation with our basement. They were insightful, thorough, helpful, honest, and recommended some cost-effective ways we could fix our problems. They didn&rsquo;t try to upsell us or push us to something that wasn&rsquo;t necessary. Definitely earned our trust!", "Michael Sean", "American Fork, Utah"),
          ("I wasn&rsquo;t even sure that my old leaking basement could be fixed. But these guys not only fixed it but fixed it beautifully. They were professional, upfront, friendly, and responsive and treated me like a big client, even though I know my project was small for them. I&rsquo;m so pleased.", "Eliza Fry", "Salt Lake City, Utah"),
          ("We were very happy with Rhino Foundation Systems through this entire process. Everyone that we worked with was professional, honest, and took the time to answer all of our questions! We have already recommended RFS to our friend in need of basement waterproofing.", "Margaret Tew", "Lehi, Utah")]
SIGNS = [("Settlement cracks", "Horizontal cracks in your foundation may not necessarily mean that you have a serious foundation problem, but it&rsquo;s worth checking out. If it&rsquo;s a horizontal rather than a vertical crack in the basement wall, get in touch as soon as possible.", "brick-stair-crack", "Stair-step cracks in a brick wall"),
         ("Wall cracks", "Cracks in both the drywall and foundation walls can be signs of structural issues. While drywall cracks may seem minor, they can indicate shifting that impacts your foundation.", "wall-crack-door", "A crack running up from a door frame"),
         ("Water in the basement or crawl space", "Unaddressed moisture in these areas can create ideal conditions for foundation problems, as temperature fluctuations may cause cracks to form and worsen over time.", None, ""),
         ("Bowing or leaning walls", "Bowing walls may indicate pressure from the soil surrounding your home or shifting within the foundation itself. Check whether the walls are misaligned at the top or bottom.", None, "")]
COUNTIES = [("Utah County", [("American Fork", None), ("Alpine", None), ("Highland", None), ("Lehi", None), ("Saratoga Springs", None), ("Cedar Hills", None), ("Pleasant Grove", None)]),
            ("Salt Lake County", [("Salt Lake City", "location/"), ("West Valley", None), ("Draper", None), ("Sandy", None), ("Bluffdale", None), ("Millcreek", None)]),
            ("Summit County", [("Park City", None), ("Snyderville", None), ("Kamas", None), ("Coalville", None), ("Peoa", None)]),
            ("Davis County", [("Layton", None), ("Bountiful", None), ("Kaysville", None), ("Farmington", None), ("Centerville", None)]),
            ("Wasatch County", [("Heber City", None), ("Midway", None)]),
            ("Washington County", [("St. George", "service-area/concrete-repair/st-george/"), ("Ivins", None), ("Santa Clara", None), ("Hurricane", None), ("La Verkin", None), ("Washington", None)])]
FAQ = [("Are consultations and estimates really free?", "Yes. Rhino Foundation Systems offers free consultations and free estimates. Call 801-509-5344 or send the form."),
       ("What&rsquo;s the difference between helical piers and push piers?", "Helical piers are steel shafts with corkscrew-like plates, screwed into the soil with hydraulic power and anchored below the frost line. Push piers are long steel piles driven deep into the soil with hydraulic pressure; as they go deeper they can lift and stabilize a sinking foundation. See <a href=\"@/helical-piers-push-piers/\">helical and push piers</a>."),
       ("Does my soil matter?", "Yes. Each soil type reacts differently to moisture and weight: clay expands when wet, silt holds water and heaves with frost, sand can shift under load, and loam is the most stable. Rhino evaluates soil conditions and tailors the repair to them."),
       ("Where do you work?", "Across Utah: Salt Lake, Utah, Davis, Summit, Wasatch and Washington counties, from Lehi and American Fork to Park City and St. George.")]


def strip_art():
    bands = "".join(f'<rect class="{c}" x="0" y="{(t - 170) / 390 * 200 + 20:.0f}" width="320" height="{(b - t) / 390 * 200:.0f}"/>' for n, t, b, c, d in LAYERS)
    return (f'<svg class="strata-mini" viewBox="0 0 320 220" aria-hidden="true">{bands}<rect class="mini-house" x="70" y="0" width="120" height="20"/>'
            '<path class="mini-pier" d="M170 20 V196"/><path class="mini-helix" d="M158 176 h24 M158 188 h24"/><path class="mini-frost" d="M0 165 H320"/></svg>')


def pier_svg():
    bands = "".join(f'<g class="pl" data-l="{i}"><rect class="{c}" x="0" y="{t}" width="900" height="{b - t}"/><text x="24" y="{t + 26}">{n.upper()}</text></g>' for i, (n, t, b, c, d) in enumerate(LAYERS))
    ticks = "".join(f'<line x1="868" y1="{y}" x2="{884 if (y - 170) % 50 == 0 else 878}" y2="{y}"/>' for y in range(170, 561, 10))
    return f'''<svg class="pier-svg" viewBox="0 0 900 560" role="img" aria-labelledby="pier-t">
<title id="pier-t">Drawing of a house settling into the soil, with a helical pier being driven down through loam, silt, clay and sand to stable soil below the frost line</title>
<defs><pattern id="dots" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" class="dot"/></pattern></defs>
<rect class="sky" x="0" y="0" width="900" height="170"/>
{bands}
<rect x="0" y="170" width="900" height="390" fill="url(#dots)"/>
<path class="frost" d="M0 450 H900"/><text class="frost-t" x="600" y="444">FROST LINE</text>
<g class="house" data-house>
<rect class="footing" x="210" y="164" width="330" height="26"/>
<path class="wall" d="M232 164 V70 L375 18 L518 70 V164 Z"/>
<rect class="win" x="268" y="96" width="44" height="40"/><rect class="win" x="440" y="96" width="44" height="40"/><rect class="door" x="356" y="104" width="38" height="60"/>
<path class="crack" data-crack d="M484 70 L474 88 L486 100 L470 122 L482 138 L468 164"/>
</g>
<g class="pier" data-pier><rect class="bracket" x="500" y="176" width="34" height="18"/><line class="shaft" x1="517" y1="190" x2="517" y2="232" data-shaft/>
<g data-tip transform="translate(0 236)"><ellipse class="helix" cx="517" cy="-14" rx="20" ry="5"/><ellipse class="helix" cx="517" cy="-38" rx="17" ry="4.5"/><path class="tip" d="M511 0 L517 12 L523 0 Z"/></g></g>
<g class="gauge">{ticks}<text x="862" y="186" text-anchor="end">0</text><text x="862" y="566" text-anchor="end">DEPTH</text></g>
<text class="status" x="24" y="40" data-status>SETTLING</text>
</svg>'''


def home():
    layer_txt = "".join(f'<div class="pr-tx{" on" if i == 0 else ""}" data-i="{i}"><p class="pr-k">Layer {i + 1:02d} of 05</p><h3>{n}</h3><p>{d}</p></div>' for i, (n, t, b, c, d) in enumerate(LAYERS))
    signs = "".join(f'<li class="reveal-up{" has-ph" if im else ""}"><span class="sg-n">{i + 1:02d}</span><div><h3>{t}</h3><p>{d}</p></div>{f"<figure>{img(im, alt)}</figure>" if im else ""}</li>' for i, (t, d, im, alt) in enumerate(SIGNS))
    quotes = "".join(f'<blockquote class="reveal-up"><p>&ldquo;{q}&rdquo;</p><footer><b>{n}</b><span>{w}</span></footer></blockquote>' for q, n, w in QUOTES)
    counties = "".join(f'<div class="cty"><h3>{c}</h3><ul>' + "".join(f'<li>{f"<a href=@/{p}>{t}</a>" if p else t}</li>' for t, p in towns) + "</ul></div>" for c, towns in COUNTIES)
    body = f'''
<section class="r-hero"><div class="wrap r-hero-in">
<div class="r-hero-text"><p class="r-kick"><span></span>Foundation repair &middot; American Fork &middot; all of Utah</p>
<h1>Foundation repair in American Fork, <em>down to solid ground.</em></h1>
<p class="lede">Rhino Foundation Systems does foundation repair in American Fork, Salt Lake City and across Utah: helical and push piers, basement waterproofing, crawl space encapsulation, drains, sump pumps and concrete lifting. Consultations and estimates are free.</p>
<div class="btn-row"><a class="btn accent" href="@/contact-us/">Get a free estimate {ARROW}</a><a class="btn ghost" href="tel:+18015095344">{PHONE} 801-509-5344</a></div></div>
<figure class="r-hero-ph"><div class="ruler" aria-hidden="true"></div>{img("rhino-truck", "A Rhino Foundation Systems truck at a job", priority=True)}<figcaption>On the job &middot; Rhino Foundation Systems</figcaption></figure>
</div>
<div class="r-band"><div class="r-band-in"><span>Free consultations</span><span>Free estimates</span><span>Licensed &amp; insured</span><span>Residential &amp; commercial</span><span>Salt Lake to St. George</span></div></div>
</section>

<section class="sec signs-sec"><div class="wrap">
<div class="r-head split-head reveal-up"><div><p class="r-num">01 / The signs</p><h2>How to tell if you need <span>foundation repair.</span></h2></div><p class="lede">Even small cracks can become major issues if left unchecked. These are four of the signs Rhino tells homeowners to watch for.</p></div>
<ol class="signs">{signs}</ol>
</div></section>

<section class="pier-sec" id="pier"><div class="wrap">
<div class="r-head light reveal-up"><p class="r-num">02 / Drive the pier</p><h2>Soil decides <span>everything.</span></h2>
<p class="lede">Each soil type reacts differently to water and weight. Drag the gauge to drive a helical pier down, layer by layer, until it reaches soil that holds.</p></div>
<div class="pier" data-pierdemo>
<div class="pr-draw"><div class="pr-canvas">{pier_svg()}<input class="pr-range" type="range" min="0" max="100" step="0.5" value="0" aria-label="Pier depth, from the surface down to below the frost line" aria-valuetext="Loam"></div>
<p class="pr-note">Drag the depth gauge &middot; drawing for illustration; real layers vary from lot to lot</p></div>
<div class="pr-panel"><div class="pr-meter"><span>Status</span><b data-meter>Settling</b></div><div class="pr-texts" aria-live="polite">{layer_txt}</div>
<p class="pr-src">The soil descriptions are Rhino&rsquo;s own. Rhino evaluates soil conditions on site and tailors the repair to them.</p><a class="tlink light" href="@/helical-piers-push-piers/">Helical &amp; push piers {ARROW}</a></div>
</div></div></section>

<section class="sec svc-sec"><div class="wrap">
<div class="r-head split-head reveal-up"><div><p class="r-num">03 / Services</p><h2>Under the house, <span>around the house.</span></h2></div><p class="lede">Residential and commercial: from the piers under a foundation to the drains around it and the concrete in front of it.</p></div>
<div class="bento">
<a class="tile t-big reveal-up" href="@/foundation-repair/"><figure>{img("helical-piers", "Helical piers on a crate, ready for installation")}</figure><div><span>Foundation</span><b>Foundation repair &amp; piers</b><em>Settling, cracks, bowed walls {ARROW}</em></div></a>
<a class="tile t-tall reveal-up" href="@/basement-waterproofing/"><figure>{img("basement-waterproofing-install", "A basement after waterproofing, with a sump pump")}</figure><div><span>Water</span><b>Basement waterproofing</b><em>Leaks, seepage, flooding {ARROW}</em></div></a>
<a class="tile t-wide reveal-up" href="@/concrete-lifting/"><figure>{img("slab-lip-measured", "A tape measure on a settled concrete slab")}</figure><div><span>Concrete</span><b>Concrete lifting &amp; repair</b><em>Sunken slabs, trip hazards {ARROW}</em></div></a>
<div class="tile t-list reveal-up"><span>Also</span><ul><li><a href="@/crawl-space-encapsulation/">Crawl space encapsulation</a></li><li><a href="@/french-drains/">French drains</a></li><li><a href="@/sump-pumps/">Sump pumps</a></li><li><a href="@/commercial-foundation-repair/">Commercial foundation repair</a></li><li><a href="@/concrete-installation/">Concrete installation</a></li><li><a href="@/vuba-stone/">Vuba Stone overlays</a></li></ul></div>
</div></div></section>

<section class="sec job-sec"><div class="wrap job-in">
<figure class="job-a reveal-up">{img("push-pier-install", "Driving push piers at a commercial job")}<figcaption>Push piers going in at a commercial job</figcaption></figure>
<div class="job-t reveal-up"><p class="r-num">04 / Commercial</p><h2>Built for loads <span>bigger than a house.</span></h2><p>Commercial foundation repair for buildings where downtime costs money: the same piers and soil work, planned around the business.</p><a class="tlink" href="@/commercial-foundation-repair/">Commercial foundation repair {ARROW}</a></div>
</div></section>

<section class="sec quote-sec"><div class="wrap">
<div class="r-head reveal-up"><p class="r-num">05 / What they say</p><h2>From homeowners <span>along the Wasatch Front.</span></h2></div>
<div class="quotes">{quotes}</div>
</div></section>

<section class="sec area-sec"><div class="wrap">
<div class="r-head split-head reveal-up"><div><p class="r-num">06 / Service area</p><h2>All of Utah, <span>county by county.</span></h2></div><p class="lede">Located in the heart of the Wasatch Front and serving the entire state. <a href="@/service-area/">See the full service area</a>.</p></div>
<div class="counties reveal-up">{counties}</div>
</div></section>

<section class="sec faq-sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="r-num">07 / Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span>New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{form("Get a free estimate", msg_label="What&rsquo;s going on with your foundation, basement or concrete?")}</div>
</div></section>
'''
    from pagekit import cta
    return {"path": "", "canonical": U, "title": "Foundation Repair American Fork, UT | Rhino Foundation Systems",
            "meta": "Foundation repair in American Fork, Salt Lake City and across Utah: helical and push piers, basement waterproofing, crawl spaces and concrete lifting. Free estimates.",
            "body": body + cta(), "og": "rhino-truck", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
