"""Articles for roofrepairsaltlakecity.com: the client's /articles/ page (empty today: "Nothing Found") becomes the article
index, with one new post.

Post: "What Is a Ballasted Roof? How Stone-Ballasted Single-Ply Roofs Work"
Main phrase: "ballasted roof" (informational). The client lists ballasted roofing as a service on their home page but has no
page for it, so this fills a gap without competing with a money page. Kept off it on purpose: "roof repair salt lake city"
(home), "commercial roofing salt lake city" and the TPO pages; the post only links to them.
Facts and sources, checked 18 Oct 2026:
- IBC sections 1507.12 and 1507.13 cover single-ply roofs; ballast is designed under ANSI/SPRI RP-4; stone per ASTM D448 or
  ASTM D7655 (SPRI 2023 standards presentation). https://www.spri.org/wp-content/uploads/2023/10/6-2023-Standards-RP-4__RP-14-Chamberlain.pdf
- RP-4 design data goes up to a building height of 150 ft; it sets the stone and paver types and minimum weights for wind
  loads in different parts of the country (ANSI/SPRI RP-4).
  https://www.spri.org/download/ansi-spri_standards_2020_restructure/rp-04/ANSI_SPRI_RP-4-2013-Wind-Design-Standard-for-Ballasted-Single-Ply-Roofing-Systemsv2.pdf
- The most common gravel-ballasted roof weighs 10 pounds per square foot or more, using ASTM D448 #4 stone or larger
  (Buildings, "Ballast Can Do It All"). https://www.buildings.com/articles/34491/ballast-can-do-it-all
- Corner and perimeter areas see more wind uplift, where ballast can scour; those zones need more ballast or pavers
  (IIBEC, "A New Look at Ballasted Roof Performance"). https://iibec.org/publication-post/a-new-look-at-ballasted-roof-performance/
"""
from engine import crumbs_ld, faq_html, faq_ld, canon
from cfg import S, U, NAME
from illus import fig_ballast

POST = ("What Is a Ballasted Roof? How Stone-Ballasted Single-Ply Roofs Work", "articles/what-is-a-ballasted-roof/")
_ = {}


def setup(phero, cta, arrow, home, contact):
    _.update(phero=phero, cta=cta, A=arrow, HOME=home, CONTACT=contact)


FAQ = [("What is a ballasted roof?", "A low-slope roof where the single-ply membrane is laid loose over the insulation and held down by the weight of stone or concrete pavers instead of fasteners or adhesive."),
       ("How heavy is ballast?", "The most common gravel-ballasted roofs weigh 10 pounds per square foot or more. The exact weight is set by the wind design for the building, its height and the roof zone."),
       ("Can any building take a ballasted roof?", "Only if the structure can carry the extra weight. An engineer or the original drawings should confirm the roof&rsquo;s capacity before ballast is chosen."),
       ("Can a ballasted roof be repaired?", "Yes. The ballast is moved aside, the membrane is repaired, and the stone is put back. Leaks can be harder to trace because the membrane is hidden."),
       ("Why do corners need more ballast?", "Wind lifts hardest at roof corners and edges, which can scour loose stone. Those zones get heavier ballast or pavers.")]


def post():
    path = POST[1]; A = _["A"]
    trail = [_["HOME"], ("Articles", "articles/"), ("Ballasted roofs", path)]
    body = _["phero"](trail, POST[0], "Stone instead of screws: how a ballasted roof holds a membrane down, where it works, and what to check first.", "AR-01", "ballast") + f'''
<section class="sec"><div class="wrap post-grid"><article class="prose post">
<p class="mono meta">By {NAME} &middot; 18 Oct 2026 &middot; 6 min read</p>
<p class="answer">A ballasted roof is a low-slope roof whose single-ply membrane is laid loose over the insulation and held in place by weight: a layer of river stone or concrete pavers. Nothing fastens the membrane to the deck. The ballast keeps it down in the wind and protects it from the sun.</p>

<figure>{fig_ballast()}</figure>

<h2>How a ballasted roof is built</h2>
<p>From the bottom up, a ballasted single-ply roof has the roof deck, a layer of rigid insulation, the membrane, and the ballast on top. The membrane, usually EPDM or another single-ply sheet, is unrolled over the insulation with its seams joined, and flashed at walls, curbs, drains and the roof edge like any other membrane roof. Then the stone or pavers are spread across it.</p>
<p>In the building code, single-ply roofs fall under International Building Code sections 1507.12 and 1507.13. The ballast itself is designed under a standard called ANSI/SPRI RP-4, and the stone has to meet ASTM D448 or ASTM D7655 for size and grading.</p>

<h2>How much does the ballast weigh?</h2>
<p>Enough to resist the wind. The most common gravel-ballasted roofs weigh 10 pounds per square foot or more, using #4 stone or larger. RP-4 sets the minimum weight and the stone or paver type for each part of the roof based on the wind the building sees, and its design data covers buildings up to 150 feet tall.</p>
<p>Corners and the perimeter matter most. Wind lifts hardest at the edges of a roof, and strong gusts can scour loose stone off a corner. That is why those zones get heavier stone, pavers or other measures, while the middle of the roof can carry lighter ballast.</p>

<h2>Why owners choose ballast</h2>
<ul>
<li><b>Fast to install.</b> No fastening pattern or adhesive across the field of the roof.</li>
<li><b>The membrane is protected.</b> Stone shields it from sunlight and foot traffic.</li>
<li><b>It can be reused.</b> On a re-roof, clean stone can often go back on.</li>
</ul>

<h2>When ballast is the wrong choice</h2>
<ul>
<li><b>The structure can&rsquo;t carry it.</b> Ten or more pounds per square foot is a real load. Check the original drawings or have an engineer confirm the roof&rsquo;s capacity.</li>
<li><b>The roof is steep.</b> Ballast is for low-slope roofs; stone won&rsquo;t stay put on a pitch.</li>
<li><b>The building is very tall or very exposed.</b> High wind zones and tall buildings may need a fastened or adhered system instead.</li>
</ul>

<h2>Stone or pavers?</h2>
<p>Most ballasted roofs use smooth, rounded river stone. Rounded stone matters: sharp, crushed rock can cut into the membrane as people walk on it or as it shifts in the wind. Concrete pavers do the same job with more weight in less depth, which is why they often go in the corners and along the edges where the wind is strongest.</p>
<p>Pavers have a second use. Laid in a line from the roof hatch to rooftop units, they make a walkway, so the people who service heating and cooling equipment are not stepping on loose stone and grinding it into the membrane.</p>

<h2>Looking after a ballasted roof</h2>
<p>A ballasted roof needs a few simple checks, especially after a windstorm and before winter:</p>
<ol>
<li><b>Corners and edges.</b> Look for bare patches where the wind has moved the stone. Exposed membrane needs its ballast put back.</li>
<li><b>Drains and scuppers.</b> Keep stone and debris out of drains so water can leave the roof.</li>
<li><b>Ponding.</b> Water that sits for days after a storm can mean a sagging deck or a blocked drain.</li>
<li><b>Flashing.</b> Walls, curbs and penetrations are flashed like any membrane roof and can fail like any membrane roof.</li>
<li><b>Foot traffic.</b> Keep service traffic on the walkway pavers.</li>
</ol>
<p>In Salt Lake City, snow sits on flat roofs for weeks at a time, so clear drains and sound flashing before the first storm save a lot of trouble later.</p>

<h2>Repairs and leaks</h2>
<p>Because the membrane is hidden under the stone, a leak on a ballasted roof can be harder to find. A repair means moving the ballast aside, finding and fixing the membrane, and putting the stone back so it covers the repair evenly. If you have a ballasted roof that leaks, see our pages on <a href="@/flat-roof-repair/">flat roof repair</a> and <a href="@/commercial-roof-repair/">commercial roof repair</a>.</p>

<h2>Ballasted vs. fastened vs. adhered</h2>
<p>A single-ply membrane can be held down three ways: by weight (ballasted), by screws and plates (mechanically fastened) or by glue (fully adhered). Ballast suits strong, low buildings where speed and protection matter. Fastened and adhered systems weigh far less and suit roofs that can&rsquo;t carry ballast or that see higher winds. White fastened or adhered membranes are also common on <a href="@/tpo-roofing-membrane/">TPO roofs</a>.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>SPRI, 2023 standards presentation: RP-4, IBC 1507.12 / 1507.13, ASTM D448 and D7655 stone: <a href="https://www.spri.org/wp-content/uploads/2023/10/6-2023-Standards-RP-4__RP-14-Chamberlain.pdf" rel="noopener">spri.org</a></li>
<li>ANSI/SPRI RP-4, Wind Design Standard for Ballasted Single-Ply Roofing Systems: <a href="https://www.spri.org/download/ansi-spri_standards_2020_restructure/rp-04/ANSI_SPRI_RP-4-2013-Wind-Design-Standard-for-Ballasted-Single-Ply-Roofing-Systemsv2.pdf" rel="noopener">spri.org</a></li>
<li>Buildings, &ldquo;Ballast Can Do It All&rdquo;: <a href="https://www.buildings.com/articles/34491/ballast-can-do-it-all" rel="noopener">buildings.com</a></li>
<li>IIBEC, &ldquo;A New Look at Ballasted Roof Performance&rdquo;: <a href="https://iibec.org/publication-post/a-new-look-at-ballasted-roof-performance/" rel="noopener">iibec.org</a></li>
</ul><p>Ballast design depends on the building. Have an engineer confirm loads and wind zones for your roof.</p></div>
</article>
<aside class="sv-side"><div class="side-card"><p class="label light">Ballasted roof?</p><h3>Free evaluation</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{_["CONTACT"]}">Request an Estimate {A}</a></div></aside>
</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "What Is a Ballasted Roof? How Stone-Ballasted Roofs Work",
            "meta": "What is a ballasted roof? How stone-ballasted single-ply roofs are built, how much ballast weighs, when they work, and what to check before choosing one.",
            "body": body, "ogtype": "article",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index():
    A = _["A"]; trail = [_["HOME"], ("Articles", "articles/")]
    body = _["phero"](trail, "Roofing Articles from Roof Repair Salt Lake City", "Plain explanations of roof systems, repairs and the choices behind them.", "AR-00") + f'''
<section class="sec"><div class="wrap"><ol class="index light"><li><a href="@/{POST[1]}"><span class="mono">AR-01</span><b>{POST[0]}</b><i>{A}</i></a></li></ol></div></section>''' + _["cta"]()
    return {"path": "articles/", "canonical": canon("articles/"), "title": "Roofing Articles | Roof Repair Salt Lake City, Utah",
            "meta": "Roofing articles from Roof Repair Salt Lake City: how roof systems work, from ballasted single-ply roofs to repairs, explained in plain language.",
            "body": body, "schema": [crumbs_ld("articles/", trail)]}


def pages():
    return [index(), post()]
