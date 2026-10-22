import html, re
from build import U, BIZ_ID, S, ARROW, PHONE, IMGMAP, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

PATH = "blog/how-to-prevent-ice-dams-on-a-utah-roof/"
NDSU = "https://www.ag.ndsu.edu/news/newsreleases/2023/january/reduce-ice-dam-and-icicle-damage"
UOU = "https://www.inscc.utah.edu/~steenburgh/utah_climo/snowstorms.html"
ICC = "https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes"
FHB = "https://www.finehomebuilding.com/project-guides/roofing/ice-barriers-explained-far-roof-slope"

# Main keyword: "how to prevent ice dams" (+ Utah). Informational, long-tail, blog only.
# Supporting: what causes ice dams, are icicles bad for your roof, ice dam removal, heat cables for ice dams, ice and water shield.
# Kept off this page on purpose (owned by service pages, linked only): roof leak repair, emergency roofing, rain gutters,
# roof repair salt lake city, roofing company utah. Does not overlap the existing posts on winter prep, seasonal maintenance
# or roof lifespan; it links to them instead.

FAQ = [
    ("Are icicles bad for your roof?",
     "A few small icicles are normal. A row of thick icicles along the eaves, especially over heated rooms, usually means an ice dam is forming behind them. The icicles themselves can pull on gutters and fall on people, so treat large ones as a warning sign, not decoration."),
    ("What is the fastest way to get rid of an ice dam?",
     "Pulling snow off the lower few feet of roof with a roof rake from the ground takes away the meltwater supply. Never chip ice with an axe or hammer, which tears shingles. If water is already coming inside, call a roofer; steaming ice off is a job for professionals."),
    ("Do heat cables stop ice dams?",
     "Heat cables can keep a channel open so meltwater drains, which helps on problem spots like valleys and low eaves. They treat the symptom, not the cause. NDSU Extension warns that homeowners often try to fix ice dams with things like heat tape instead of preventing the problem."),
    ("Will a new roof stop ice dams?",
     "A new roof with an ice barrier at the eaves will keep backed-up water out much better. But if warm air is still leaking into the attic, the snow will keep melting and refreezing. The lasting fix is a roof replacement plus air sealing, insulation and ventilation."),
    ("Does homeowners insurance cover ice dam damage?",
     "It depends on your policy and the cause. Many policies treat sudden water damage from an ice dam differently from long-term wear. Take photos, write down dates, and call your agent. We can document the roof damage and give you a repair estimate to share with them."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> to prevent ice dams, keep your roof deck cold. Seal the air leaks that let house heat into the attic, add insulation, and make sure the attic is vented from the soffits to the ridge. Then keep gutters clear, rake heavy snow off the lower roof from the ground, and make sure the eaves have an ice barrier under the shingles.</div>

<p>It's a common winter call in Utah: a water stain on a bedroom ceiling, usually along an outside wall, right after a cold snap. Often the roof itself isn't broken. Water from melting snow has backed up behind a ridge of ice at the eaves and found its way under the shingles.</p>
<p>That ridge of ice is an ice dam. Here's what causes them, how to stop them, and what to do if you already have one.</p>

<h2>What causes ice dams</h2>
<p>An ice dam needs three things: snow on the roof, a roof deck that's warm enough to melt it, and cold eaves where the meltwater can freeze again.</p>
<p>North Dakota State University Extension explains it plainly: <a href="{NDSU}" rel="noopener">heat escaping into the attic warms the roof and melts the snow</a>, and when that water reaches the colder edge of the roof, it freezes. Day after day the ice builds up into a dam. New meltwater pools behind it, and shingles are built to shed water, not hold back a puddle. So it seeps under them and into the house.</p>
<p>That's why ice dams show up over heated rooms and not over an unheated garage. The heat source is your house.</p>

<figure>{img("icicles-snow-overhang-roof", "Thick snow overhang with icicles hanging from a roof edge")}<figcaption>A thick snow overhang with icicles is the classic sign that meltwater is refreezing at the eave.</figcaption></figure>

<h2>Why Utah roofs get ice dams</h2>
<p>The Salt Lake Valley gets real snow. The University of Utah's <a href="{UOU}" rel="noopener">Salt Lake Valley snowstorm climatology</a> puts the average at about 65 inches a year at the airport and close to 100 inches on the benches around the valley. It also notes that the Great Salt Lake produces localized snowbands several times each winter.</p>
<p>Add our typical pattern of cold nights and sunny days, and you get the perfect cycle: snow sits on the roof, the house and the sun warm the upper roof, and the water freezes again at the shaded, cold eaves overnight. Homes on the benches, in Park City and up the canyons get more snow, but valley homes get ice dams too.</p>

<h2>How to prevent ice dams: fix the attic first</h2>
<p>The long-term cure happens inside the attic, not on the roof. The goal is a roof deck that stays close to the outdoor temperature, so snow melts evenly or not at all.</p>

<h3>1. Seal attic air leaks</h3>
<p>Warm, moist air rises into the attic through every gap in the ceiling below. NDSU Extension lists the usual leaks: gaps around chimneys, plumbing vents, wiring, recessed lights, ceiling fan mounts and the attic hatch. Seal those with the right materials (fire-rated where needed around chimneys and flues) before adding insulation.</p>

<h3>2. Add insulation</h3>
<p>Insulation slows the heat that does get through. NDSU suggests attics in northern climates need roughly 15 inches of blown-in insulation. Keep it off the soffit vents, using baffles at the eaves so air can still flow in.</p>

<h3>3. Vent from the soffits to the ridge</h3>
<p>Ventilation carries away the heat that sneaks past the insulation. Cold outside air comes in at the soffits, sweeps under the roof deck, and leaves at a ridge vent or high vents. Both halves matter: a ridge vent with blocked soffits doesn't move much air. If you're not sure what a ridge vent does, our article on <a href="@/blog/what-is-a-ridge-vent-what-are-some-advantages-to-having-a-ridge-vent/">ridge vents and their advantages</a> explains it.</p>

<h3>4. Move heat sources out of the attic</h3>
<p>Bathroom and kitchen fans should vent outside, not into the attic. Old ductwork running through the attic should be sealed and insulated. An old swamp cooler opening can be a big heat leak in winter, too; our article on <a href="@/blog/how-to-remove-a-swamp-cooler-what-you-need-to-know/">removing a swamp cooler</a> covers what's involved.</p>

<h2>Roof details that keep ice dam water out</h2>
<p>Even a well-sealed attic can't stop every ice dam during a long cold snap. These details make sure the water that does back up stays out of the house.</p>

<h3>Ice barrier at the eaves</h3>
<p>Utah adopted the <a href="{ICC}" rel="noopener">2021 International Residential Code</a>, which includes an ice barrier rule for shingle and other steep-slope roofs in areas where ice has historically formed along the eaves. Where it applies, the barrier is a self-adhering membrane (often called ice and water shield) or two layers of cemented underlayment. It runs from the edge of the roof to at least 24 inches inside the exterior wall line.</p>
<p>That 24 inches is measured horizontally, inside the wall, so on a typical overhang the membrane has to run a lot farther up the roof than one 36-inch roll. <a href="{FHB}" rel="noopener">Fine Homebuilding</a> works through examples where it ends up around 47 to 50 inches up the slope. Your city's building department decides whether it's required where you live. Even where it isn't, it's worth asking for on any roof that gets snow.</p>

<h3>Gutters and downspouts that drain</h3>
<p>A gutter packed with leaves or ice holds water right at the eave, which is exactly where you don't want it. Clean gutters before the first freeze, and make sure downspouts drain away from walkways where meltwater will refreeze. Our <a href="@/blog/the-best-way-to-clean-gutters-safely/">guide to cleaning gutters safely</a> covers the how-to.</p>

<h3>Flashing and valleys</h3>
<p>Valleys, chimneys and wall junctions collect snow and meltwater. Loose or rusted flashing there turns a small ice dam into a leak. A pre-winter roof check is the time to catch it.</p>

<figure>{img("snowy-house-evergreens", "Two-story house and evergreen trees covered in fresh snow")}<figcaption>Even snow cover across the whole roof usually means the attic is staying cold. Bare patches over the house and heavy icicles at the eaves mean heat is getting out.</figcaption></figure>

<h2>Already have an ice dam? Do this</h2>
<ol>
<li><strong>Clear snow from the ground.</strong> Use a roof rake with an extension pole to pull snow off the bottom three or four feet of the roof. Less snow means less meltwater feeding the dam.</li>
<li><strong>Don't climb onto an icy roof.</strong> Falls from ladders and roofs are a real risk in winter. Leave rooftop work to a crew with the right gear.</li>
<li><strong>Never chip the ice.</strong> Hammers, axes and shovels tear shingles and gutters, and can turn a temporary problem into a roof repair.</li>
<li><strong>Catch the water inside.</strong> Put down towels and buckets, move valuables, and take photos of any stains and drips with the date.</li>
<li><strong>Call a roofer if water is getting in.</strong> A professional can open a channel through the ice safely and check the roof for damage once it melts.</li>
</ol>
<p>If water is already coming through the ceiling, our <a href="@/services/emergency-roofing-utah/">emergency roofing</a> crew can help. For leaks that show up after the thaw, see our <a href="@/services/roof-leak-repair-service/">roof leak repair</a> service.</p>

<h2>Heat cables, salt and other quick fixes</h2>
<p>Heat cables (heat tape) zigzagged along the eaves can keep a drainage path open over a problem spot. They're useful on a stubborn valley or a low eave over a porch. But they use electricity all winter, they can fail without anyone noticing, and they don't stop the melting that causes the dam. NDSU Extension warns that homeowners often try to treat the symptoms of ice dams with things like heat tape instead of preventing the problem in the first place.</p>
<p>Calcium chloride ice melt in a stocking laid across the dam can melt a channel in a pinch. Avoid rock salt (sodium chloride), which can damage shingles, gutters and the plants below.</p>

<h2>Does an ice dam mean you need a new roof?</h2>
<p>Usually not. Most ice dam leaks are fixed by repairing the damaged area and fixing the attic so it doesn't happen again. That's the idea behind our Repair-First Promise: if your roof can be repaired, we won't sell you a replacement.</p>
<p>If your roof is near the end of its life anyway, or the leaks have rotted the deck at the eaves, a replacement with a proper ice barrier and balanced ventilation is often the better spend. Our article on <a href="@/blog/roof-repair-vs-roof-replacement-how-to-choose/">roof repair vs. roof replacement</a> walks through that decision, and <a href="@/blog/how-long-do-roofs-last-in-utah/">how long roofs last in Utah</a> can help you judge where yours is.</p>

<h2>A simple pre-winter ice dam checklist</h2>
<ul>
<li>Gutters and downspouts clean and draining</li>
<li>Attic hatch, recessed lights and plumbing gaps sealed</li>
<li>Insulation even, deep, and kept off the soffit vents</li>
<li>Soffit and ridge vents open</li>
<li>Bath and kitchen fans venting outdoors</li>
<li>Flashing at chimneys, valleys and walls tight</li>
<li>A roof rake hanging in the garage</li>
</ul>
<p>For the rest of your fall to-do list, see our <a href="@/blog/seasonal-roof-maintenance-checklist/">seasonal roof maintenance checklist</a>.</p>

<h2>Ice dam questions</h2>
{faq_html(FAQ)}

<h2>Get your roof ready before the snow</h2>
<p>American Roofing Company has worked on Utah roofs since 1954. We'll look at your roof and attic venting, explain what we find, and give you complete pricing before anything is scheduled. Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or <a href="@/request-free-quote/">request a free quote</a>.</p>

<h3>Sources</h3>
<ul style="font-size:.92rem">
<li>North Dakota State University Extension: <a href="{NDSU}" rel="noopener">Reduce ice dam and icicle damage</a> (January 2023)</li>
<li>University of Utah, Department of Atmospheric Sciences: <a href="{UOU}" rel="noopener">Salt Lake Valley Snowstorms</a></li>
<li>International Code Council: <a href="{ICC}" rel="noopener">Utah adoption of the 2021 International Codes</a></li>
<li>Fine Homebuilding: <a href="{FHB}" rel="noopener">Ice barriers explained</a></li>
</ul>
'''


def ice_dams():
    url = U + PATH
    trail = [("Home", ""), ("Blog", "blog/"), ("How to Prevent Ice Dams on a Utah Roof", PATH)]
    rel = [("Roof Leak Repair", "services/roof-leak-repair-service/"), ("Emergency Roofing", "services/emergency-roofing-utah/"),
           ("Rain Gutters", "services/rain-gutters/"), ("Roof Replacements", "services/roof-replacements/"),
           ("Seasonal Maintenance Checklist", "blog/seasonal-roof-maintenance-checklist/")]
    extra = '<div class="meta-line"><span>By American Roofing Company</span><span>Published <time datetime="2026-10-16">October 16, 2026</time></span><span>About 9 minutes to read</span></div>'
    body = (phero(trail, "How to Prevent Ice Dams on a Utah Roof",
                  "What causes ice dams, how to stop them for good, and what to do if one is already leaking.",
                  "icicles-log-cabin-eave", "Icicles hanging from a snow-covered roof eave", "Winter roofing guide", extra)
            + f'<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>{side(rel)}</div></section>'
            + cta("Ready for winter?", "Book a free roof evaluation before the first big storm. We'll check flashing, gutters and attic venting."))
    return {"path": PATH, "title": "How to Prevent Ice Dams on a Utah Roof | American Roofing",
            "meta": "How to prevent ice dams on a Utah roof: what causes them, the attic fixes that stop them, ice barrier code rules, and what to do if one is already leaking.",
            "canonical": url, "modified": "2026-10-16", "ogtype": "article", "og": "icicles-snow-overhang-roof", "full_biz": False,
            "body": body,
            "schema": [{"@type": "BlogPosting", "@id": url + "#article", "headline": "How to Prevent Ice Dams on a Utah Roof",
                        "description": "What causes ice dams on Utah roofs, how to prevent them, and what to do if one is already leaking.",
                        "url": url, "mainEntityOfPage": url, "image": U + "assets/img/icicles-snow-overhang-roof.webp",
                        "datePublished": "2026-10-16", "dateModified": "2026-10-16", "inLanguage": "en-US",
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "about": ["Ice dams", "Roof maintenance", "Utah winter"]},
                       faq_ld(FAQ), crumbs_ld(url, trail)]}


def index(r, posts):
    cards = [f'<a class="postcard reveal" href="@/{PATH}">{img("icicles-snow-overhang-roof", "Snow overhang with icicles on a roof edge")}<div class="in"><small>Oct 16, 2026 &middot; New</small><b>How to Prevent Ice Dams on a Utah Roof</b></div></a>']
    for i, (p, pr) in enumerate(posts):
        im = IMGMAP.get(pr.get("og_image") or "") or ["roofing-project-utah-residential", "hero-house", "roofing-project-utah-blue-home", "shingle-damage-closeup", "metal-roof-chimney-dusk"][i % 5]
        d = (pr.get("published") or "")[:10]
        cards.append(f'<a class="postcard reveal" href="@/{p}">{img(im, pr["h1"] or pr["title"])}<div class="in"><small>{d}</small><b>{html.escape(pr["h1"] or pr["title"])}</b></div></a>')
    body = (phero([("Home", ""), ("Blog", "blog/")], "The American Roofing Blog", "Straight answers about Utah roofs: repairs, replacements, insurance, materials and winter care.",
                  "roof-work-in-utah-winter", "Roofers working on a snowy Utah roof", "Roofing blog")
            + f'<section class="sec"><div class="wrap"><div class="grid">{"".join(cards)}</div></div></section>' + cta())
    return {"body": body, "og": "roof-work-in-utah-winter", "full_biz": False,
            "schema": [{"@type": "Blog", "@id": U + "blog/#blog", "url": U + "blog/", "name": "American Roofing Blog", "publisher": {"@id": BIZ_ID}},
                       crumbs_ld(U + "blog/", [("Home", ""), ("Blog", "blog/")])]}
