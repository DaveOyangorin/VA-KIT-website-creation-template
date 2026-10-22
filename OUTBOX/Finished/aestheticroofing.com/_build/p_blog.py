from build import U, BIZ_ID, S, ARROW, PHONE, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

PATH = "blog/what-causes-roof-leaks/"
NDSU = "https://www.ag.ndsu.edu/news/newsreleases/2023/january/reduce-ice-dam-and-icicle-damage"
UOU = "https://www.inscc.utah.edu/~steenburgh/utah_climo/snowstorms.html"
KAYS = "https://www.kaysville.gov/DocumentCenter/View/195/Handyman-Information-PDF"
DOPL = "https://dopl.utah.gov/"

# Main keyword: "what causes roof leaks" (a real Google question from the 5 Oct audit, marked "Yes").
# Supporting long-tail: can a handyman fix a roof leak, roof leaking when it rains, roof leak around chimney,
# roof leak in winter, signs of a roof leak.
# Kept off this page on purpose: "roof repair south jordan" (the roof repair page), "roof leak repair south jordan"
# (a future service page the audit flags), "storm damage roof repair". The post only links to those pages.

FAQ = [
    ("What is the most common cause of a roof leak?",
     "Flashing is one of the most common culprits: the metal pieces that seal the roof around chimneys, vents, skylights and walls. Flashing loosens, corrodes or loses its sealant over time, and water runs straight in behind it. Missing or damaged shingles are a close second, especially after a wind storm."),
    ("Can a handyman fix a roof leak?",
     "A handyman can sometimes handle a very small fix, like resealing a vent boot, if the job is within Utah's handyman exemption and they know roofs. Anything bigger, or any leak where the cause isn't obvious, is a job for a licensed roofer, because a patch over the wrong spot just hides the problem."),
    ("Why does my roof only leak when it rains hard?",
     "Heavy or wind-driven rain pushes water sideways and upward, into gaps that stay dry in a light shower. That usually points to flashing, an open seam, a lifted shingle edge or an overflowing gutter. Note the wind direction when it leaks; it helps narrow down which side of the roof to check."),
    ("Why does my roof leak in winter but not summer?",
     "Winter-only leaks are often ice dams. Heat from the house melts roof snow, the water refreezes at the cold eaves, and meltwater backs up under the shingles. They usually show up along exterior walls. The lasting fix is better attic air sealing, insulation and ventilation, plus an ice barrier at the eaves."),
    ("Is a small roof leak an emergency?",
     "A small leak isn't usually a 911-style emergency, but it shouldn't wait weeks. Water soaks the roof deck and insulation long before it shows on the ceiling, and wet wood and drywall get worse with every storm. Catch the drip, take photos, and get the roof looked at soon."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> most roof leaks come from failed flashing around chimneys, vents and walls; missing or damaged shingles; worn pipe boots; clogged gutters; and, in Utah winters, ice dams at the eaves. The stain on your ceiling is rarely right under the hole, so the fix starts with tracing where the water really gets in.</div>

<p>A brown spot on the ceiling. A drip in the closet after a storm. A musty smell in the attic. However it shows up, a roof leak raises the same two questions: where is the water coming from, and how big a deal is it?</p>
<p>This guide covers the causes we see most on Northern Utah homes, how to narrow down the source from inside your house, and when a quick fix is fine versus when you need a licensed roofer.</p>

<h2>Why the leak is never where the stain is</h2>
<p>Water that gets through the roof doesn't fall straight down. It lands on the roof deck or the top of a rafter and runs along it, sometimes several feet, until it finds a low point or a gap in the drywall. That's why patching the shingles directly above a stain so often doesn't work.</p>
<p>Finding a leak means following the water backward: from the stain, up into the attic, along the wood, to the point where it first got in.</p>

<figure>{img("top-down-new-roof", "Top-down drone view of a shingle roof with ridges, valleys and vents")}<figcaption>Every ridge, valley, vent and wall joint on a roof is a place where water has to be directed away. Those are the spots that leak first.</figcaption></figure>

<h2>The most common causes of roof leaks</h2>

<h3>1. Damaged or loose flashing</h3>
<p>Flashing is the metal that seals the joints around chimneys, skylights, dormers and anywhere a roof meets a wall. It's one of the most common places roofs leak. Sealant dries out, nails back out, and metal shifts as the house expands and contracts through Utah's hot summers and cold winters. A leak near a chimney or along an upstairs wall usually starts here.</p>

<h3>2. Missing, cracked or lifted shingles</h3>
<p>Wind can lift shingle edges or tear shingles off entirely, and hail can crack them or knock off the protective granules. Once a shingle is gone or broken, water reaches the underlayment, and from there it's a matter of time. After a big wind storm, look for shingles in the yard or bare patches on the roof from the ground.</p>

<h3>3. Worn pipe boots and roof vents</h3>
<p>Plumbing vent pipes come through the roof with a rubber boot sealed around them. Sun and freeze-thaw cycles crack that rubber over the years, and water runs down the outside of the pipe into your attic. Box vents and exhaust fans can loosen the same way. A leak over a bathroom often traces back to a vent.</p>

<h3>4. Valleys</h3>
<p>Valleys are where two roof slopes meet and channel water down together. They carry more water than any other part of the roof, so a worn shingle, a nail in the wrong place or debris build-up there shows up fast as a leak.</p>

<h3>5. Clogged gutters</h3>
<p>When gutters fill with leaves and debris, water backs up over the edge of the roof and can soak the fascia, the roof deck and the top of the wall. Ice in winter does the same thing. A leak right along an exterior wall, near the ceiling line, is often a gutter problem rather than a shingle problem.</p>

<h3>6. Ice dams</h3>
<p>Northern Utah gets real snow. The University of Utah's <a href="{UOU}" rel="noopener">Salt Lake Valley snowstorm climatology</a> puts the airport at about 65 inches a year and the benches near 100. When heat from the house melts that snow, the water refreezes at the cold eaves. North Dakota State University Extension describes it plainly: <a href="{NDSU}" rel="noopener">heat escaping into the attic warms the roof and melts the snow</a>, and the meltwater freezes again at the edge, building a dam that pushes water up under the shingles.</p>

<h3>7. Skylights</h3>
<p>Skylights leak either around the frame, where the flashing meets the roof, or through the unit itself if the seals have failed. Condensation on the glass can look like a leak too, so check whether it happens when it rains or when it's cold.</p>

<h3>8. An old roof</h3>
<p>Every roof wears out. Shingles get brittle, lose granules and curl, and the underlayment beneath them breaks down. When leaks start showing up in different places, it's usually a sign the whole roof is near the end of its life, not just one bad spot.</p>

<h2>How to narrow down a leak from inside</h2>
<p>You can learn a lot without ever climbing a ladder. Start here:</p>
<ol>
<li><strong>Note when it leaks.</strong> Only in heavy rain? Only with wind from one direction? Only in winter? Each points to a different cause.</li>
<li><strong>Check the attic on a dry day.</strong> With a flashlight, look for dark stains, water trails on rafters, wet insulation or daylight coming through.</li>
<li><strong>Look up from the stain.</strong> Find the spot in the attic above the ceiling stain, then follow any trail uphill toward the roof.</li>
<li><strong>Check what's above it outside.</strong> From the ground, look for a chimney, vent, skylight, valley or wall joint above that area.</li>
<li><strong>Take photos with dates.</strong> They help your roofer, and they help with an insurance claim if storm damage is involved.</li>
</ol>
<p>Please don't walk on a wet, icy or steep roof to look for the leak. It's not worth the fall.</p>

<figure>{img("crew-on-roof-utah-county", "Roofing crew working on a home with snowy mountains in the background")}<figcaption>Finding a leak often means getting up on the roof with the right safety gear. Leave that part to a crew.</figcaption></figure>

<h2>Can a handyman fix a roof leak?</h2>
<p>Sometimes, for very small jobs. Utah's contractor licensing law has a "handyman exclusion" in Utah Code 58-55-305 that lets an unlicensed person take on small repairs below a set dollar value, counting both labor and materials. Above that limit, the work requires a licensed contractor. The dollar amount has been raised over the years (a <a href="{KAYS}" rel="noopener">2016 Kaysville City handyman guide</a> shows the older figures), so check the current limit with the <a href="{DOPL}" rel="noopener">Utah Division of Occupational and Professional Licensing</a> before you hire.</p>
<p>The bigger question is whether the fix will work. A handyman might reseal a cracked pipe boot just fine. But most leaks aren't that simple, and a dab of roofing tar over the wrong spot hides the symptom while water keeps soaking the deck. If you're not sure where the water is getting in, you need someone who can find the source, not just cover the stain.</p>
<div class="tablebox"><table>
<thead><tr><th>A handyman may be fine</th><th>Call a licensed roofer</th></tr></thead>
<tbody>
<tr><td>One obvious, small problem (a cracked vent boot)</td><td>You can't tell where the water is coming from</td></tr>
<tr><td>Small job within the handyman exemption</td><td>Leaks in more than one spot, or leaks that came back</td></tr>
<tr><td>No storm or insurance claim involved</td><td>Wind or hail damage you may claim on insurance</td></tr>
<tr><td>The roof is otherwise in good shape</td><td>Curling or missing shingles, soft spots, an older roof</td></tr>
</tbody></table></div>

<h2>Repair or replace?</h2>
<p>One leak from one cause on a healthy roof is usually a repair. Leaks in several places, shingles curling or bald across the roof, or a deck that feels soft are signs the roof itself is worn out, and patching will keep costing you. Our <a href="@/services/roof-repair/">roof repair</a> and <a href="@/services/roof-replacement/">roof replacement</a> pages explain how we make that call. If a storm caused it, see <a href="@/services/storm-damage-roof-repair/">storm damage roof repair</a>.</p>

<h2>What to do right now if your roof is leaking</h2>
<ul>
<li>Catch the water with buckets and towels, and move furniture and electronics out of the way.</li>
<li>If a ceiling is bulging with water, keep people away from it and call a professional.</li>
<li>Photograph the stain, the drip and anything you can see from the ground outside.</li>
<li>Book a roof inspection so the source gets found and fixed before the next storm.</li>
</ul>

<h2>Roof leak questions</h2>
{faq_html(FAQ)}

<h2>Get a straight answer about your leak</h2>
<p>Aesthetic Roofing is a GAF Master Elite&reg; roofing contractor in South Jordan. Book a free <a href="@/services/roof-inspection/">Roof Health Report</a> and a certified inspector will find where the water is getting in, show you what they found, and lay out your options. Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or <a href="@/contact/">book online</a>.</p>

<h3>Sources</h3>
<ul style="font-size:.92rem">
<li>North Dakota State University Extension: <a href="{NDSU}" rel="noopener">Reduce ice dam and icicle damage</a> (January 2023)</li>
<li>University of Utah, Department of Atmospheric Sciences: <a href="{UOU}" rel="noopener">Salt Lake Valley Snowstorms</a></li>
<li>Kaysville City: <a href="{KAYS}" rel="noopener">Handyman Information</a> (2016; quotes Utah Code 58-55-305)</li>
<li>Utah Division of Occupational and Professional Licensing: <a href="{DOPL}" rel="noopener">dopl.utah.gov</a></li>
</ul>
'''


def pages():
    url = U + PATH
    trail = [("Home", ""), ("Blog", "blog/"), ("What Causes Roof Leaks?", PATH)]
    rel = [("Roof Repair", "services/roof-repair/"), ("Roof Inspection", "services/roof-inspection/"),
           ("Storm Damage Roof Repair", "services/storm-damage-roof-repair/"), ("Roof Replacement", "services/roof-replacement/"),
           ("Gutter Services", "services/gutter-services/")]
    extra = '<div class="meta-line"><span>By Aesthetic Roofing</span><span>Published <time datetime="2026-10-16">October 16, 2026</time></span><span>About 9 minutes to read</span></div>'
    post_body = (phero(trail, "What Causes Roof Leaks?", "The usual culprits on Northern Utah homes, how to narrow down the source from inside, and when a handyman patch is enough.",
                       "aerial-new-shingle-roof", "Aerial view of a shingle roof", "Roof leak guide")
                 .replace('<div class="btn-row"', extra + '<div class="btn-row"', 1)
                 + f'<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>{side(rel)}</div></section>'
                 + cta("Leak you can't track down?", "A free Roof Health Report finds the source, not just the stain."))
    post = {"path": PATH, "title": "What Causes Roof Leaks? A Utah Roofer's Guide | Aesthetic",
            "meta": "What causes roof leaks? The common culprits on Utah homes, how to trace a leak from inside, and whether a handyman can fix it. A guide from Aesthetic Roofing.",
            "canonical": url, "modified": "2026-10-16", "ogtype": "article", "og": "top-down-new-roof", "full_biz": False, "body": post_body,
            "schema": [{"@type": "BlogPosting", "@id": url + "#article", "headline": "What Causes Roof Leaks?", "url": url, "mainEntityOfPage": url,
                        "description": "The common causes of roof leaks on Northern Utah homes, how to trace a leak, and when a handyman can fix it.",
                        "image": U + "assets/img/top-down-new-roof.webp", "datePublished": "2026-10-16", "dateModified": "2026-10-16",
                        "inLanguage": "en-US", "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "isPartOf": {"@id": U + "blog/#blog"}},
                       faq_ld(FAQ), crumbs_ld(url, trail)]}
    idx_body = (phero([("Home", ""), ("Blog", "blog/")], "The Aesthetic Roofing Blog", "Plain answers about roofs in Northern Utah.",
                      "aerial-roofs-street", "Aerial view of homes along a Utah street", "Blog")
                + f'''<section class="sec"><div class="wrap"><div class="grid">
<a class="postcard reveal" href="@/{PATH}">{img("top-down-new-roof", "Top-down drone view of a roof")}<div class="in"><small>Oct 16, 2026 &middot; Roof leaks</small><b>What Causes Roof Leaks? A Utah Roofer's Guide</b></div></a>
</div></div></section>''' + cta())
    index = {"path": "blog/", "title": "Roofing Blog | Aesthetic Roofing, South Jordan UT",
             "meta": "Roofing advice for Northern Utah homeowners from Aesthetic Roofing in South Jordan: roof leaks, repairs, replacements and what to expect from your roofer.",
             "canonical": U + "blog/", "og": "aerial-roofs-street", "full_biz": False, "body": idx_body,
             "schema": [{"@type": "Blog", "@id": U + "blog/#blog", "url": U + "blog/", "name": "Aesthetic Roofing Blog", "publisher": {"@id": BIZ_ID}},
                        crumbs_ld(U + "blog/", [("Home", ""), ("Blog", "blog/")])]}
    return [index, post]
