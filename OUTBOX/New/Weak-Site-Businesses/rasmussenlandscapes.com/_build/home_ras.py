"""Home page for rasmussenlandscapes.com: "Your yard. Our work."
The Yard year dial uses only timing stated on Rasmussen's own pages (sprinklers, aerate, hedging, fall-cleanup, sprinkler-maintenance,
weeding, snow-removal). Where a page names a season rather than months, the item shows across that season and quotes the season."""
import math
from engine import img, faq_html, faq_ld, crumbs_ld
from cfg import U, AREAS
import pagekit as K
from pagekit import ARROW, PHONE, HOME

MON = "January February March April May June July August September October November December".split()
SPRING, SUMMER, FALL, WINTER = [2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 0, 1]
# (title, months, quote from their page, page path)
YEAR = [("Sprinkler turn-on", [3, 4], "Mostly in the months of April and May, our sprinkler teams are busy starting sprinkler systems back up, with a top-to-bottom check of every zone.", "sprinklers/"),
        ("Spring aeration", [2, 3], "The Rasmussen Way of aerating is once in the spring (March through April)&hellip;", "aerate6eed311a/"),
        ("Late-summer aeration", [7, 8], "&hellip;and again before the fall growth spurt (late August into September) for maximum results.", "aerate6eed311a/"),
        ("Early-spring hedge trim", [2], "The first time to trim hedges is in early spring, right before the first big spring growth.", "hedging/"),
        ("Summer hedge trim", SUMMER, "The second time is in the summer, after the spring growth spurt, so hedges look tidy all summer.", "hedging/"),
        ("Fall hedge trim", [8, 9], "The last trim is in the fall, right as the final growth spurt happens, to prepare for heavy snow.", "hedging/"),
        ("Summer sprinkler tune-up", [6, 7, 8], "Beginning in July and sometimes through September, the temperatures get very hot and the watering needs of your plants change.", "sprinklers/"),
        ("Sprinkler maintenance", [4, 5, 6, 7, 8, 9], "When it&rsquo;s growing season (May to October) our beloved plants, flowers, and vegetables need enough water not only to survive, but to thrive.", "sprinkler-maintenance/"),
        ("Winter shut-off", [9, 10], "Starting in October, our sprinkler teams begin shutting off sprinkler systems and evacuating any water left in the system.", "sprinklers/"),
        ("Spring cleanup", SPRING, "In the spring, debris needs cleaning up, annuals need planting, and preparing lawns for the growing season is at the top of everyone&rsquo;s list.", "fall-cleanup/"),
        ("Fall cleanup", FALL, "In the fall, leaves need cleaning up, perennials need cutting back, bulbs should be planted, and coniferous plants need to be prepped for winter.", "fall-cleanup/"),
        ("Plant bed weeding", SPRING + SUMMER + FALL, "We insist that weeding be done often, so that yards look great every day of the week for the entire spring, summer, and fall.", "weeding/"),
        ("Snow removal", WINTER, "When it&rsquo;s time to put our mowers and trimmers away, we dust off our winter boots and snow blowers and stand at the ready.", "snow-removal/")]
QUOTES = [("They were on time and very responsive to our questions. They drastically updated our system. Some of the new sprinkler heads were not working as expected when they were installed. Rasmussen promptly came out and resolved the issue. Incredible customer service.", "Henri Vanderbeek"),
          ("Rasmussen did beautiful landscaping tidying, cleanup, lawn maintenance and irrigation repair work at my house in the Avenues. Most neighbors use Rasmussen, and I know why! They are clean, courteous and take pride in their work. I strongly recommend Rasmussen for any yard work, landscaping and irrigation work.", "Chris Bachorowski"),
          ("They do an quick and efficient job mowing my lawn. I love that it includes mowing up the leaves through out the fall. Everything looks great after they leave.", "Kathi Kimble"),
          ("I have used Rasmussen Landscapes for years and look forward to many more years to come. They really are the best in the business. No need to look anywhere else!", "Lance Poulsen")]
HOME_FAQ = [("Can I get a quote over the phone?", "<p>Yes. In one phone call you can get a price, get answers to your questions, sign a service agreement and have your service scheduled. We use satellite imaging to measure the size and scope of your project, so we can give you an accurate price right over the phone: (801) 466-0303.</p>"),
            ("When do you turn sprinklers on and off?", "<p>Turn-ons happen mostly in April and May. Shut-offs start in October, when we blow out every zone with an industrial air compressor. See <a href=\"@/sprinklers/\">sprinklers</a>.</p>"),
            ("When should my lawn be aerated?", "<p>The Rasmussen Way is twice a year: once in the spring (March through April) and again before the fall growth spurt (late August into September).</p>"),
            ("Do you design and build new landscapes?", "<p>Yes. Our process is <a href=\"@/dream/\">dream</a>, <a href=\"@/plan/\">plan</a> and <a href=\"@/execute/\">execute</a>: demolition, soil preparation and sprinklers, then rock walls, water features, patios and fencing, then sod, trees, shrubs and flowers.</p>")]


def dial():
    cx = cy = 200; r0, r1 = 118, 186
    segs, labels = [], []
    for i, m in enumerate(MON):
        a0 = math.radians(i * 30 - 90 + 1); a1 = math.radians((i + 1) * 30 - 90 - 1)
        p = lambda r, a: f"{cx + r * math.cos(a):.1f} {cy + r * math.sin(a):.1f}"
        d = f"M{p(r1, a0)} A{r1} {r1} 0 0 1 {p(r1, a1)} L{p(r0, a1)} A{r0} {r0} 0 0 0 {p(r0, a0)} Z"
        season = "sp" if i in SPRING else "su" if i in SUMMER else "fa" if i in FALL else "wi"
        n = sum(1 for t, ms, q, pg in YEAR if i in ms)
        segs.append(f'<path class="seg {season}" d="{d}" data-m="{i}" tabindex="0" role="button" aria-label="{m}: {n} jobs"/>')
        am = math.radians(i * 30 - 75)
        labels.append(f'<text x="{cx + 152 * math.cos(am):.1f}" y="{cy + 152 * math.sin(am) + 4:.1f}" text-anchor="middle">{m[:3]}</text>')
    seas = "".join(f'<text class="sl" x="{cx + 205 * math.cos(math.radians(a)):.1f}" y="{cy + 205 * math.sin(math.radians(a)) + 4:.1f}" text-anchor="middle">{s}</text>'
                   for s, a in (("SPRING", -15), ("SUMMER", 75), ("FALL", 165), ("WINTER", 255)))
    return f'''<svg class="dial" viewBox="-20 -20 440 440" role="group" aria-label="The yard year: pick a month">{"".join(segs)}<g class="ml" aria-hidden="true">{"".join(labels)}</g><g class="sls" aria-hidden="true">{seas}</g>
<circle class="hub" cx="200" cy="200" r="108"/><text class="hub-m" x="200" y="196" text-anchor="middle" data-hub-m>October</text><text class="hub-n" x="200" y="226" text-anchor="middle" data-hub-n>3 jobs this month</text></svg>'''


def year_items():
    return "".join(f'<li data-ms="{" ".join(str(m) for m in ms)}"><a href="@/{pg}"><b>{t}</b><span>{q}</span><em>{ARROW}</em></a></li>' for t, ms, q, pg in YEAR)


def home():
    body = f'''
<section class="r-hero"><div class="r-hero-img">{img("ras-rock-steps", "Natural rock steps through a lawn under mature trees, built by Rasmussen Landscapes", priority=True)}</div>
<div class="wrap r-hero-in"><div class="r-hero-card"><p class="label">South Salt Lake &middot; Design &middot; Build &middot; Maintain</p>
<h1>Landscaping in South Salt Lake. <em>Your yard. Our work.</em></h1>
<p class="lede">Rasmussen Landscapes designs, builds and maintains yards across the Salt Lake Valley: sprinklers, sod, rock walls, patios and water features, plus weekly mowing, fertilizing, aeration, cleanups and snow removal.</p>
<div class="btn-row"><a class="btn accent" href="@/Contact/">Get a Quote {ARROW}</a><a class="btn ghost" href="tel:+18014660303">{PHONE} (801) 466-0303</a></div></div>
<p class="r-cap">Rock steps &middot; a Rasmussen project</p></div></section>

<section class="sec r-three"><div class="wrap">
<div class="r-head reveal"><p class="label">What we do</p><h2>Design, build, <em>and keep it beautiful.</em></h2></div>
<div class="r-spread">
<a class="rs rs1 reveal" href="@/DesignBuild/"><figure>{img("ras-excavator-rocks", "A Rasmussen excavator placing boulders for a new landscape")}</figure><span class="rs-k">01 &middot; Design &amp; Build</span><b>Your yard. Your sanctuary.</b><p>Dream, plan, execute: demolition, soil preparation and sprinklers, then rock walls, water features, patios and fencing, then sod, trees, shrubs and flowers.</p></a>
<a class="rs rs2 reveal" href="@/Services/"><figure>{img("ras-bench-lawn", "A freshly mowed lawn with a garden bench under shade trees")}</figure><span class="rs-k">02 &middot; Maintenance</span><b>Mow, feed, aerate, tidy.</b><p>Weekly mowing, fertilizing, aeration, weeding, hedging and pruning, cleanups and sprinkler maintenance.</p></a>
<a class="rs rs3 reveal" href="@/other-services/"><figure>{img("ras-brush-cutting", "A Rasmussen skid steer brush cutting a large lot")}</figure><span class="rs-k">03 &middot; Other services</span><b>Snow to sod patching.</b><p>Snow removal, holiday lighting, brush cutting, edging, specialty excavation, in-ground trampolines and more.</p></a>
</div></div></section>

<section class="sec r-year" id="yard-year"><div class="wrap">
<div class="r-head split-h reveal"><div><p class="label">The yard year</p><h2>What your yard needs, <em>month by month.</em></h2></div><p class="lede">Utah is the second-driest state, with hot summers and hard-freezing winters, so timing is everything. Turn the year to see what we do in your yard each month.</p></div>
<div class="yr" data-year><div class="yr-dial">{dial()}<div class="yr-nav"><button type="button" data-yr-prev aria-label="Previous month">&larr;</button><button type="button" data-yr-next aria-label="Next month">&rarr;</button></div></div>
<ul class="yr-list" aria-live="polite">{year_items()}</ul></div>
<p class="yr-note reveal">Fertilizing runs across the whole growing season in six targeted rounds: weed pre-emergent, weed &amp; feed, turf builder &amp; iron, soil conditioner, grub &amp; insect control and a lawn winterizer. <a href="@/fertilize/">How we feed Utah lawns {ARROW}</a></p>
</div></section>

<section class="r-band"><div class="r-band-img" data-parallax="0.12">{img("ras-flower-bed", "A flowering perennial bed along a flagstone path")}</div>
<div class="wrap"><blockquote class="reveal"><p>&ldquo;{QUOTES[3][0]}&rdquo;</p><footer>{QUOTES[3][1]}</footer></blockquote></div></section>

<section class="sec r-work"><div class="wrap">
<div class="r-head split-h reveal"><div><p class="label">Portfolio</p><h2>Yards we&rsquo;ve built <em>and kept.</em></h2></div><a class="tlink" href="@/portfolio/">See the portfolio {ARROW}</a></div>
<div class="mosaic">
<figure class="m1 reveal">{img("ras-patio", "A covered patio with teak furniture and potted boxwoods")}<figcaption>Patios &amp; pathways</figcaption></figure>
<figure class="m2 reveal">{img("ras-garden-path", "A gravel garden path between clipped hedges and a bench")}<figcaption>Garden design</figcaption></figure>
<figure class="m3 reveal">{img("ras-sprinkler-spray", "A pop-up sprinkler watering a lawn in morning light")}<figcaption>Sprinklers</figcaption></figure>
<figure class="m4 reveal">{img("ras-fire-pit", "A flagstone patio with a stone fire pit and stump seats")}<figcaption>Water &amp; fire features</figcaption></figure>
<figure class="m5 reveal">{img("ras-sod-roll", "A roll of fresh sod being laid")}<figcaption>Sod installation</figcaption></figure>
<figure class="m6 reveal">{img("ras-zinnia", "A magenta zinnia in a planted bed")}<figcaption>Trees, shrubs &amp; flowers</figcaption></figure>
</div></div></section>

<section class="sec r-phone"><div class="wrap r-phone-in">
<figure class="reveal">{img("ras-crew-sprinkler", "A Rasmussen crew member adjusting a sprinkler head")}</figure>
<div class="reveal"><p class="label">Quotes over the phone</p><h2>One call. <em>A price, a plan, a date.</em></h2>
<p>In one phone call you can get a price, get answers to all your questions, sign a service agreement and have your service scheduled. We use satellite imaging to measure the size and scope of your project, so we can give you an accurate price right over the phone.</p>
<a class="r-tel" href="tel:+18014660303">(801) 466-0303</a>
<div class="zq">{"".join(f'<blockquote><p>&ldquo;{q}&rdquo;</p><footer>{n}</footer></blockquote>' for q, n in (QUOTES[1], QUOTES[2]))}</div></div>
</div></section>

<section class="sec r-areas"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Service areas</p><h2>Across the valley <em>and beyond.</em></h2><p>From our office in South Salt Lake we cover the majority of the Salt Lake Valley, plus Davis, Weber, Tooele, Summit and Utah county towns.</p>
<ul class="chips">{"".join(f'<li><a href="@/{p}">{n}</a></li>' for n, p in (("Salt Lake City", "salt-lake-city/"), ("The Avenues", "the-avenues/"), ("Millcreek", "milcreek/"), ("Holladay", "holladay/"), ("Sandy", "sandy/"), ("Draper", "draper/"), ("West Jordan", "west-jordan/"), ("Herriman", "herriman/"), ("Bountiful", "bountiful/"), ("Layton", "layton/"), ("Syracuse", "syracuse/"), ("Ogden", "ogden/"), ("Tooele", "tooele/"), ("Park City", "park-city/"), ("Alpine", "alpine/"), ("Highland", "highland/"), ("Orem", "orem/"), ("Provo", "provo/")))}</ul></div>
<div class="reveal"><p class="label">Questions</p>{faq_html(HOME_FAQ)}
<a class="post-card r-post" href="@/blog/when-to-water-your-lawn-utah/"><span class="label">From the blog</span><b>When should you start watering your lawn in Utah?</b><p>Why waiting until about Mother&rsquo;s Day helps roots, and how to use the state&rsquo;s weekly watering guide.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": "Landscaping South Salt Lake | Rasmussen Landscapes, Utah",
            "meta": "Rasmussen Landscapes: landscaping in South Salt Lake and across the valley. Design and build, sprinklers, sod, rock walls, mowing, aeration and snow removal.",
            "body": body, "body_class": "is-home", "og": "ras-rock-steps", "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}
