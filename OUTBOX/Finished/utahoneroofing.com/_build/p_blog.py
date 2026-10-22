"""Blog for utahoneroofing.com, a new /blog/ section with one post. (The old posts were theme demos about Colorado and the
Twin Cities and are not rebuilt; see the notes.)

Post: "Green Roofs in Utah: How They Work, What They Weigh, and Whether They Fit Our Climate"
Main phrase: "green roof utah" (informational). The client lists green roofing as a service but no page targets it, so it
competes with nothing. Kept off it: "roofing company salt lake city" (home), "roof repair salt lake city", "commercial roofing
salt lake city"; the post links to those pages instead.
Facts and sources, checked 18 Oct 2026:
- EPA, Using Green Roofs to Reduce Heat Islands: extensive vs intensive; green roofs shade, remove heat from the air and lower
  roof-surface and air temperatures; cool roofs suit limited budgets focused on energy, green roofs suit lifecycle and public
  benefits. https://www.epa.gov/heatislands/using-green-roofs-reduce-heat-islands
- University of Delaware Cooperative Extension, Green Roofs fact sheet: extensive roofs use a 2-6 inch layer of lightweight
  growing medium. https://udel.edu/content/dam/udelImages/canr/pdfs/extension/factsheets/Green-Roofs.pdf
- Iowa Stormwater Management Manual (Iowa DNR), green roof section: a 4-inch extensive system weighs about 28 psf; a 12-inch
  intensive system about 84 psf (saturated). https://www.iowadnr.gov/media/7403
- Feng et al., Water 2018, 10(3), 262 (University of Utah, Salt Lake City lysimeters): annual ET of 2.01, 2.52 and 2.69 mm/day
  for bare, sedum and grass covers; the sedums did not show significantly lower ET than native species under irrigation.
  https://www.mdpi.com/2073-4441/10/3/262
"""
from engine import img, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, U, NAME

POST = ("Green Roofs in Utah: How They Work, What They Weigh, and Whether They Fit", "blog/green-roofs-in-utah/")
_ = {}


def setup(phero, cta, arrow, home, contact):
    _.update(phero=phero, cta=cta, A=arrow, HOME=home, CONTACT=contact)


FAQ = [("What is a green roof?", "A roof with a living layer of plants and growing medium over a waterproof membrane, root barrier and drainage layer."),
       ("How much does a green roof weigh?", "It depends on the depth. One state stormwater manual puts a 4-inch extensive system at about 28 pounds per square foot when saturated, and a 12-inch intensive system at about 84."),
       ("Do green roofs need watering in Utah?", "Usually some, at least while plants establish and through dry summers. A University of Utah study on a Salt Lake City roof measured how much water different plant covers used under irrigation."),
       ("Is sedum the best plant for a Utah green roof?", "Not automatically. In the Salt Lake City study, the sedums did not use significantly less water than native species, so plant choice should be made for the site."),
       ("Can any roof take a green roof?", "Only if the structure can carry the saturated weight and the roof can be waterproofed and drained properly. An engineer should confirm the load first.")]


def post():
    path = POST[1]; A = _["A"]
    trail = [_["HOME"], ("Blog", "blog/"), ("Green roofs in Utah", path)]
    body = _["phero"](trail, "Green Roofs in Utah: How They Work, What They Weigh, and Whether They Fit Our Climate", "Plants on the roof sound simple. Here is what&rsquo;s really up there, and what a Utah roof needs before you add one.", "G", "drone-roof-underlayment", "Drone view of a roof under construction", buttons=False) + f'''
<section class="sec"><div class="wrap post-grid"><article class="prose post">
<p class="meta">By {NAME} &middot; 18 Oct 2026 &middot; 7 min read</p>
<p class="answer">A green roof is a roof covered with plants growing in a lightweight medium, built over a waterproof membrane, a root barrier and a drainage layer. In Utah they can work, but they need a roof that can carry the extra weight, careful waterproofing, and a plan for water in our dry summers.</p>

<h2>What&rsquo;s actually up there</h2>
<p>From the deck up, a green roof is a stack of layers, each with a job:</p>
<ol>
<li><b>Roof deck</b> strong enough for the saturated weight of everything above it.</li>
<li><b>Waterproof membrane</b>, the roof itself. It has to be right, because it&rsquo;s hard to reach once the garden is on top.</li>
<li><b>Root barrier</b> so plant roots can&rsquo;t work into the membrane.</li>
<li><b>Drainage layer</b> that lets extra water run to the drains instead of sitting on the membrane.</li>
<li><b>Filter fabric</b> to keep the growing medium out of the drainage layer.</li>
<li><b>Growing medium</b>, a lightweight engineered mix rather than garden soil.</li>
<li><b>Plants</b> chosen for heat, wind, sun and how much water the roof can give them.</li>
</ol>

<h2>Extensive or intensive?</h2>
<p>The EPA describes two kinds. <b>Extensive</b> green roofs are the simpler, lighter type: a shallow layer of growing medium, usually 2 to 6 inches, planted with hardy groundcovers that need little upkeep. <b>Intensive</b> green roofs are deeper and heavier, more like a rooftop park, with room for grasses, shrubs and even small trees, and they need more structural support and more maintenance.</p>
<p>For most homes and commercial buildings looking at a green roof for the first time, extensive is where the conversation starts.</p>

<h2>What does a green roof weigh?</h2>
<p>This is the first question to answer, because the roof has to carry it when it&rsquo;s soaking wet. Iowa&rsquo;s stormwater manual gives a useful example: a 4-inch extensive system weighs about 28 pounds per square foot when saturated, and a 12-inch intensive system about 84. Add Utah&rsquo;s snow load on top of that, and it&rsquo;s clear why an engineer should check the structure before anything else.</p>

<h2>What green roofs do well</h2>
<ul>
<li><b>Cooler roofs and air.</b> The EPA says green roofs provide shade, remove heat from the air, and lower the temperature of the roof surface and the air around it.</li>
<li><b>Slower runoff.</b> The plants and medium hold rain and release it slowly instead of sending it straight down the drains.</li>
<li><b>A protected membrane.</b> The layers above shield the membrane from sun and temperature swings.</li>
</ul>
<p>The EPA also notes the trade-off: if the main goal is saving energy on a tight budget, a reflective cool roof is usually the better fit. Green roofs make more sense when you also care about the long-term life of the roof, stormwater and the wider environment.</p>

<h2>The Utah question: water</h2>
<p>Most green roof advice was written for wetter places. Salt Lake City is semi-arid, with hot, dry summers, so a green roof here usually needs some irrigation, at least while the plants establish.</p>
<p>Researchers at the University of Utah measured this on a green roof in Salt Lake City, weighing test beds to track how much water each plant cover used. Over a year, bare medium lost about 2.0 mm of water a day, sedum about 2.5 mm, and grass about 2.7 mm. One finding stands out: the sedums, the plants most green roofs default to, did not use significantly less water than native species under irrigation. For Utah, that means plant choice deserves real thought, and native, drought-tolerant plants are worth considering.</p>

<h2>Looking after a green roof</h2>
<p>A green roof is a garden that happens to sit on a roof, so it needs regular visits, especially in its first couple of years:</p>
<ul>
<li><b>Weeding.</b> Wind-blown seeds take root fast. Pull them before their roots reach the membrane layers.</li>
<li><b>Watering.</b> Check the plants through July and August; a dry, bare patch can lose its medium to wind.</li>
<li><b>Drains.</b> Keep the drains and the gravel strips around them clear of plants and debris.</li>
<li><b>Edges and flashing.</b> Look at the roof edges, walls and penetrations the same way you would on any flat roof.</li>
<li><b>Snow.</b> Don&rsquo;t shovel a green roof with a metal blade; you can cut into the layers underneath.</li>
</ul>

<h2>Is a green roof right for your building?</h2>
<p>Ask these before you start:</p>
<ol>
<li>Can the structure carry the saturated weight plus snow? (Engineer.)</li>
<li>Is the roof flat or low-slope, with working drains?</li>
<li>Is the membrane new, or will it be replaced first? It&rsquo;s far easier before the garden goes on.</li>
<li>Who will look after it, and how will it be watered?</li>
<li>Is a cool roof a better fit for your goals and budget?</li>
</ol>
<p>Whatever goes on top, the membrane underneath has to be sound. If your flat roof leaks or is near the end of its life, start with <a href="@/roof-repair/">roof repair</a> or talk to us about <a href="@/commercial-roofing/">commercial roofing</a> first.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>U.S. EPA, Using Green Roofs to Reduce Heat Islands: <a href="https://www.epa.gov/heatislands/using-green-roofs-reduce-heat-islands" rel="noopener">epa.gov</a></li>
<li>University of Delaware Cooperative Extension, Green Roofs: <a href="https://udel.edu/content/dam/udelImages/canr/pdfs/extension/factsheets/Green-Roofs.pdf" rel="noopener">udel.edu</a></li>
<li>Iowa Stormwater Management Manual, green roofs: <a href="https://www.iowadnr.gov/media/7403" rel="noopener">iowadnr.gov</a></li>
<li>University of Utah lysimeter study on a Salt Lake City green roof, Water 2018, 10(3), 262: <a href="https://www.mdpi.com/2073-4441/10/3/262" rel="noopener">mdpi.com</a></li>
</ul><p>Green roof design depends on the building. Have an engineer confirm loads before you start.</p></div>
</article>
<aside class="sv-side"><div class="side-card"><p class="label">Flat roof first?</p><h3>Free estimate</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{_["CONTACT"]}">Send a Message {A}</a></div></aside>
</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "Green Roofs in Utah: How They Work and What They Weigh",
            "meta": "Green roofs in Utah: the layers, extensive vs intensive, how much they weigh, what they do well, and how a Salt Lake City study looked at watering them.",
            "body": body, "ogtype": "article", "og": "drone-roof-underlayment",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index():
    A = _["A"]; trail = [_["HOME"], ("Blog", "blog/")]
    body = _["phero"](trail, "The Utah One Roofing Blog", "Straight answers about roofs in Utah.", "B", buttons=False) + f'''
<section class="sec"><div class="wrap"><a class="guide reveal" href="@/{POST[1]}">{img("drone-roof-underlayment", "")}<span><span class="label dark">Green roofing</span><b>{POST[0]}</b><em>Read it {A}</em></span></a></div></section>''' + _["cta"]()
    return {"path": "blog/", "canonical": canon("blog/"), "title": "Roofing Blog | Utah One Roofing, Salt Lake City, Utah",
            "meta": "The Utah One Roofing blog: straight answers about roofs in Utah, from green roofs to repairs, from a veteran-owned Salt Lake City roofing company.",
            "body": body, "schema": [crumbs_ld("blog/", trail)]}


def pages():
    return [index(), post()]
