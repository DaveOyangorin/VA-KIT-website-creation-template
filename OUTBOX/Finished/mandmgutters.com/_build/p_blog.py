import re, html as h
from build import U, S, ARROW, QUOTE, BLOG, img, faq_html, faq_ld, crumbs_ld, cta, phero

# New post. Main keyword: "5 inch vs 6 inch gutters" (+ what size gutters do I need, gutter size calculator, 6 inch gutters salt lake city).
# None of the client's 160 posts covers gutter sizing. Ties to their own gutter page (5" standard, 6" available).
# Not targeted (owned by other pages, linked only): gutter installation salt lake city (home), rain gutters installation
# (service page), the cost posts ("rain gutter install cost guide 2026" and others).
TITLE, PATH = BLOG
NOAA = "https://hdsc.nws.noaa.gov/pfds/pfds_map_cont.html?bkmrk=ut"
TOH = "https://www.thisoldhouse.com/gutters/how-to-size-gutters-and-downspouts"

FAQ = [
    ("Are 6-inch gutters better than 5-inch?",
     "They carry more water: about 7,960 square feet of adjusted roof area for 6-inch K-style versus 5,520 for 5-inch, in This Old House&rsquo;s sizing table. Whether you need that extra capacity depends on how big and steep each roof section is, and on how hard it rains."),
    ("What size gutters are standard in Utah?",
     "5-inch K-style is the standard size on most homes we work on. We install 6-inch K-style too, for larger or steeper roof sections."),
    ("How hard does it rain in Salt Lake City?",
     f"NOAA&rsquo;s precipitation-frequency data for downtown Salt Lake City puts the 5-minute rainfall intensity at about 1.9 inches per hour for a 2-year storm, 3.2 for a 10-year storm and 6.5 for a 100-year storm (<a href=\"{NOAA}\" rel=\"noopener\">NOAA Atlas 14</a>)."),
    ("Do bigger gutters need bigger downspouts?",
     "The downspouts have to keep up with the gutter. A common rule of thumb is about 1 square inch of downspout for every 100 square feet of roof; a 2&times;3-inch downspout handles about 600 square feet and a 3&times;4-inch about 1,200."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> 5-inch K-style gutters handle most Salt Lake City homes. Step up to <strong>6-inch</strong> when a single gutter run drains a large or steep roof section, or when you want margin for the heaviest storms. The way to know is a quick calculation: roof area &times; pitch factor &times; local rainfall intensity, compared with what each gutter size can carry.</div>

<p>5-inch K-style gutters are the standard on most homes we work on, and we install 6-inch as well. Homeowners often ask whether the bigger size is worth it. Sometimes it is, sometimes it isn&rsquo;t, and you don&rsquo;t have to guess.</p>
<p>Here&rsquo;s the sizing method contractors use, filled in with Salt Lake City&rsquo;s own rainfall numbers.</p>

<h2>Step 1: Measure what drains into each gutter</h2>
<p>Gutters are sized run by run, not for the whole house. For each gutter run, measure the roof section that drains into it: its length times its depth, measured flat, as if you were looking down from above. Add the areas together where two roof planes empty into the same gutter (<a href="{TOH}" rel="noopener">This Old House</a>).</p>

<h2>Step 2: Adjust for the roof pitch</h2>
<p>A steeper roof catches more wind-driven rain and sends it off faster, so the area gets a pitch factor (<a href="{TOH}" rel="noopener">This Old House</a>):</p>
<div class="tablebox"><table><thead><tr><th>Roof pitch</th><th>Pitch factor</th></tr></thead><tbody>
<tr><td>Flat to 3-in-12</td><td>1.0</td></tr><tr><td>4-in-12 to 5-in-12</td><td>1.05</td></tr><tr><td>6-in-12 to 8-in-12</td><td>1.1</td></tr>
<tr><td>9-in-12 to 11-in-12</td><td>1.2</td></tr><tr><td>12-in-12 or steeper</td><td>1.3</td></tr></tbody></table></div>

<h2>Step 3: Multiply by Salt Lake City&rsquo;s rainfall intensity</h2>
<p>Gutters overflow in short, hard bursts of rain, not in a long drizzle, so the number that matters is rainfall <em>intensity</em> over a few minutes, in inches per hour. NOAA&rsquo;s precipitation-frequency data (Atlas 14) gives these figures for downtown Salt Lake City, for a 5-minute burst (<a href="{NOAA}" rel="noopener">NOAA Atlas 14, Precipitation Frequency Data Server</a>):</p>
<div class="tablebox"><table><thead><tr><th>Storm</th><th>5-minute rainfall intensity</th></tr></thead><tbody>
<tr><td>2-year (expected about every 2 years)</td><td>1.90 in/hr</td></tr><tr><td>10-year</td><td>3.23 in/hr</td></tr><tr><td>25-year</td><td>4.28 in/hr</td></tr><tr><td>100-year</td><td>6.46 in/hr</td></tr></tbody></table></div>
<p>Which storm you design for is a judgment call. The 10-year figure is a practical everyday target; designing for the 100-year figure buys margin for the rare cloudburst. Values change a little across the valley and up the benches, and NOAA&rsquo;s server will give you the figure for your exact address.</p>

<h2>Step 4: Compare with what each gutter can carry</h2>
<p>Multiply the drainage area by the pitch factor and the rainfall intensity to get an adjusted area, then compare it with the gutter capacities This Old House lists (<a href="{TOH}" rel="noopener">This Old House</a>):</p>
<div class="tablebox"><table><thead><tr><th>Gutter</th><th>Handles up to (adjusted sq ft)</th></tr></thead><tbody>
<tr><td>5-inch K-style</td><td>5,520</td></tr><tr><td>6-inch K-style</td><td>7,960</td></tr><tr><td>5-inch half-round</td><td>2,500</td></tr><tr><td>6-inch half-round</td><td>3,840</td></tr></tbody></table></div>
<p>Those figures assume fairly even runoff and gutters that aren&rsquo;t clogged.</p>

<figure>{img("copper-gutter-4", "Copper gutter and downspout installed by M&M on a Salt Lake City home")}<figcaption>Copper gutters and downspout on an M&amp;M job. Whatever the material, the size has to match the roof.</figcaption></figure>

<h2>Two worked examples</h2>
<h3>A typical rambler section</h3>
<p>A roof plane 40 feet long and 25 feet deep drains into one gutter: 1,000 square feet. At a 6-in-12 pitch, that&rsquo;s 1,000 &times; 1.1 = 1,100 square feet. At Salt Lake City&rsquo;s 10-year intensity of 3.23 in/hr, the adjusted area is about <strong>3,550</strong>, well inside a 5-inch K-style gutter&rsquo;s 5,520. Even at the 100-year figure (about 7,100), a 6-inch K-style still covers it.</p>
<p>Notice what happens with half-round: 3,550 is more than a 5-inch half-round can carry (2,500), and close to the 6-inch half-round limit (3,840). If you love the look of half-round, plan on going up a size.</p>
<h3>A big, steep two-story section</h3>
<p>A plane 50 feet long and 35 feet deep is 1,750 square feet. At an 8-in-12 pitch: 1,750 &times; 1.1 = 1,925. At 3.23 in/hr, the adjusted area is about <strong>6,220</strong>. That&rsquo;s past the 5-inch K-style limit, and comfortably inside 6-inch. This is the kind of roof where 6-inch gutters earn their keep.</p>

<h2>Don&rsquo;t forget the downspouts</h2>
<p>A gutter can only empty as fast as its downspouts drain. This Old House&rsquo;s rule of thumb is about 1 square inch of downspout for every 100 square feet of roof. A 2&times;3-inch downspout handles about 600 square feet and a 3&times;4-inch about 1,200, and gutter runs of 60 feet or more should have at least two outlets (<a href="{TOH}" rel="noopener">This Old House</a>).</p>
<p>Often the fix for an overflowing gutter is a bigger downspout or one more outlet, not a bigger gutter.</p>

<h2>Other things that push you toward 6-inch</h2>
<ul>
<li><strong>Valleys.</strong> Where two roof planes meet, water concentrates and can shoot past a small gutter at the corner.</li>
<li><strong>Long runs</strong> that drain to a single downspout.</li>
<li><strong>Trees.</strong> A bigger gutter has more room before debris causes overflow, though <a href="@/services/leaf-guards/">leaf guards</a> solve that problem more directly.</li>
<li><strong>Looks.</strong> On a large home, a 6-inch gutter can simply look more in proportion.</li>
</ul>

<h2>Why it&rsquo;s worth getting right</h2>
<p>Gutters that are too small overflow at exactly the moment you need them, dumping water against the foundation, the siding and the walkways. Because we fabricate seamless gutters on site, matching each run to its roof section doesn&rsquo;t mean ordering anything special. We measure and choose the size for each run when we quote.</p>
<p>Want a second opinion on your roof? <a href="@/{QUOTE}">Request a free quote</a> or call <a href="tel:{S["tel"]}">{S["phone"]}</a>, and see our <a href="@/services/rain-gutters-installation/">rain gutter installation</a> page.</p>

<h2>Frequently asked questions</h2>
{faq_html(FAQ)}

<p class="sources"><strong>Sources:</strong> <a href="{NOAA}" rel="noopener">NOAA Atlas 14, Precipitation Frequency Data Server: 5-minute rainfall intensity for Salt Lake City (40.761, &minus;111.891), queried 17 October 2026</a> &middot; <a href="{TOH}" rel="noopener">This Old House, &ldquo;How To Size Gutters and Downspouts,&rdquo; Thomas Baker, updated 20 April 2026</a>.</p>
'''


def page():
    trail = [("Home", ""), ("Blog", "blog/"), (TITLE, PATH)]
    lede = "How to size gutters for a Salt Lake City roof: measure each section, adjust for pitch, and use NOAA&rsquo;s local rainfall intensity."
    from pages import article
    byline = 'By <b>M&amp;M Gutters &amp; Exteriors</b> &middot; Salt Lake City &middot; 2026-10-17 &middot; 6 min read'
    body = phero(trail, TITLE, lede, "Gutters &middot; 2026-10-17", "copper-gutter-6", "Copper gutters installed by M&M on a white stucco home", buttons=False) + article(ART, byline) + cta()
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", h.unescape(re.sub(r"<[^>]+>", " ", ART))))
    return {"path": PATH, "canonical": U + PATH, "title": "5-Inch vs. 6-Inch Gutters: Which Size Do You Need? | M&M",
            "meta": "5-inch vs. 6-inch gutters: how to size gutters for a Salt Lake City roof using roof area, pitch and NOAA rainfall data, with worked examples.",
            "body": body, "og": "copper-gutter-6", "ogtype": "article", "full_biz": False, "words": words, "modified": "2026-10-17",
            "schema": [crumbs_ld(U + PATH, trail), faq_ld(FAQ),
                       {"@type": "BlogPosting", "@id": U + PATH + "#article", "headline": TITLE, "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": U + "#organization"}, "publisher": {"@id": U + "#organization"}, "mainEntityOfPage": U + PATH,
                        "image": U + "assets/img/copper-gutter-6.webp", "wordCount": words, "inLanguage": "en-US", "citation": [NOAA, TOH]}]}
