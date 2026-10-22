"""Blog for sfrutah.com: the 8 posts that have a Wayback capture (same URLs, the client's own text), the blog index, and one new post.
Seven newer posts in the old sitemap have no capture and are not rebuilt (listed in the notes for a redirect to /blog).
"...-for-utah-homeowners-2" is a duplicate of "...-for-utah-homeowners"; it is kept at its URL and canonicals to the original.

New post: "Expansive Clay in St. George: Why Southern Utah Foundations Crack, and What Helps"
Main phrase: "expansive soil st george" (informational). None of the client's posts covers it; the St. George page targets
"foundation repair st george" (commercial), so the post links to it rather than competing. Also links to crack repair, helical
piers and waterproofing.
Facts and sources, checked 19 Oct 2026 (geology.utah.gov refused connections from here; facts from the Utah Geological Survey pages
as indexed by search, phrased conservatively):
- UGS, Survey Notes, "Geologic-Hazard and Adverse-Construction-Condition Maps for the St. George-Hurricane Area":
  https://geology.utah.gov/map-pub/survey-notes/geologic-hazard-map-of-st-george/ - expansive soil and rock contain clay minerals
  that take on water and swell, then shrink as they dry; the swelling can exceed the weight of light structures and crack
  foundations; many local bedrock units contain shale, claystone or mudstone; UGS treats it as an adverse construction condition
  (rarely sudden or catastrophic); UGS recommends a site-specific geotechnical study for development in the area.
- UGS abstract: expansive clays of the Petrified Forest Member of the Chinle Formation have caused foundation problems in the
  St. George area.
- Washington County's hazards GIS has an "Expansive Rock and Soil" layer (from UGS Special Study 127):
  https://agisprodvm.washco.utah.gov/arcgis/rest/services/Hazards/MapServer/19
- Utah Residential Code 2021, R401.3 (6 in. of fall in the first 10 ft): https://up.codes/viewer/utah/irc-2021/chapter/4/foundations
No prices.
"""
import html, re
from engine import crumbs_ld, faq_html, faq_ld, canon, img
import json, os
from cfg import U, NAME, HERE

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
POST = ("Expansive Clay in St. George: Why Southern Utah Foundations Crack", "blog/post/expansive-clay-soil-st-george-foundations/")
DUP = "blog_post_foundation_repair_methods_a_complete_guide_for_uta_01a16a"
IMG = {"efflorescence": "crack-window-frame", "settlement": "crack-antelope-home", "helical": "pier-rig-desert", "methods": "helical-bracket", "fixing": "pier-install-yard",
       "cracks_in_walls": "crack-in-arch", "horizontal": "crack-exterior-wall"}
_ = {}


def setup(phero, cta, side, arrow, home, contact, mig):
    _.update(phero=phero, cta=cta, side=side, A=arrow, HOME=home, CONTACT=contact, mig=mig)


def posts():
    out = []
    for k, v in EXT.items():
        if not k.startswith("blog_post_"): continue
        path = v["url"].replace(U, "").strip("/") + "/"
        title = html.unescape(v["title"]).split(" | ")[0].strip()
        im = next((i for w, i in IMG.items() if w in k), "helical-bracket")
        out.append((k, path, title, im))
    return out


def meta_for(title, k):
    m = html.unescape(EXT[k]["meta"] or "")
    if not m or "Plumbing" in m or len(m) < 120:
        m = f"{title}: a guide from Superior Foundation Repair Utah, with offices in Salt Lake City and St. George. Free foundation inspections across Utah."
    return m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "..."


def old_post(k, path, title, im):
    trail = [_["HOME"], ("Blog", "blog/"), (title[:38], path)]
    c, f = _["mig"](k, skip=(title,))
    c = re.sub(r"<p>(Share|Facebook|Twitter|LinkedIn|Recent Posts|See All|\d+ views|\d+ min read)[^<]*</p>", "", c)
    t = title if len(title) <= 46 else title[:46].rsplit(" ", 1)[0]
    t = f"{t} | Superior Foundation"
    canonical = canon("blog/post/foundation-repair-methods-a-complete-guide-for-utah-homeowners/") if k == DUP else (EXT[k]["canon"] or canon(path))
    body = _["phero"](trail, title, None, "Blog", im, title) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">{c}{f"<h2>Common questions</h2>{faq_html(f)}" if f else ""}</article>{_["side"]()}</div></section>''' + _["cta"]()
    pg = {"path": path, "canonical": canonical, "title": t, "meta": meta_for(title, k), "body": body, "og": im, "ogtype": "article",
          "schema": [crumbs_ld(path, trail), {"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": title, "image": U + f"assets/img/{im}.webp",
                                              "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canonical}] + ([faq_ld(f)] if f else [])}
    if k == DUP: pg["sitemap"] = False
    return pg


FAQ = [("Is expansive soil a problem in St. George?", "It can be. The Utah Geological Survey notes that many bedrock units around St. George contain shale, claystone or mudstone, and that expansive clays of the Petrified Forest Member of the Chinle Formation have caused foundation problems in the area."),
       ("How do I know if my lot has expansive soil?", "A geotechnical report is the reliable answer, and the UGS recommends a site-specific study for development in the St. George&ndash;Hurricane area. Washington County&rsquo;s hazard maps also show where expansive rock and soil may be present."),
       ("Can a house on expansive clay be fixed?", "Usually. The first step is controlling water around the house. Where a foundation has already moved, piers that reach below the active clay can stabilize it; an inspection tells you which, if any, is needed.")]


def new_post():
    path = POST[1]
    trail = [_["HOME"], ("Blog", "blog/"), ("Expansive clay in St. George", path)]
    A = _["A"]
    ugs = "https://geology.utah.gov/map-pub/survey-notes/geologic-hazard-map-of-st-george/"
    wc = "https://agisprodvm.washco.utah.gov/arcgis/rest/services/Hazards/MapServer/19"
    irc = "https://up.codes/viewer/utah/irc-2021/chapter/4/foundations"
    body_txt = f'''<p class="answer">Expansive clay is soil (or soft rock) that swells when it gets wet and shrinks as it dries. Around St. George, some of the ground homes are built on contains these clays, and the repeated push and pull is one of the reasons Southern Utah foundations, slabs and driveways crack even where it hardly rains.</p>
<p>We work out of a St. George office as well as Salt Lake City, and the ground in the two places behaves very differently. Up north, our best-documented job was a house in Orem sitting on wet lake-bed sediment over a spring. Down south, the problem is often the opposite: dry ground that changes size every time it gets watered. Here is what that means for a house, and what actually helps.</p>
<h2>What makes clay &ldquo;expansive&rdquo;</h2>
<p>Some clay minerals take water into their structure. As they soak it up they swell, and as they dry out they shrink again. The <a href="{ugs}" rel="noopener">Utah Geological Survey</a> explains that the swelling pressure can be greater than the weight of a light building, which is why it can lift and crack footings, slabs, sidewalks and driveways. It rarely causes sudden, dramatic damage, so the UGS files it as an &ldquo;adverse construction condition&rdquo; rather than a geologic hazard. It does its damage slowly, season after season.</p>
<h2>Why St. George has it</h2>
<p>The UGS has mapped hazards and construction conditions across the St. George&ndash;Hurricane area. It notes that many of the local bedrock units contain shale, claystone or mudstone, and that the soils weathered from them can be expansive. One unit in particular, the Petrified Forest Member of the Chinle Formation, has expansive clays that have caused foundation problems around St. George.</p>
<p>That&rsquo;s why the UGS recommends a site-specific geotechnical study for development in the area. If you&rsquo;re curious about your own lot, Washington County publishes the UGS mapping in its <a href="{wc}" rel="noopener">hazards map service (&ldquo;Expansive Rock and Soil&rdquo;)</a>. It&rsquo;s a regional map, not a lot-by-lot verdict, but it shows where to be careful.</p>
<h2>What it does to a house</h2>
<p>Expansive soil rarely moves a house evenly. Water reaches one side more than another (a sprinkler zone, a downspout, a leaking line, a planter against the wall), so one part of the foundation rises or drops more than the rest. The signs are the same ones we look for on any inspection:</p>
<ul><li>Cracks in drywall, especially from the corners of doors and windows</li><li>Doors and windows that stick or won&rsquo;t latch</li><li>Floors that slope or feel uneven</li><li>Cracks in the slab, garage floor or driveway, sometimes with one side higher than the other</li><li>Gaps between walls and ceilings, or a porch pulling away from the house</li></ul>
<p>A crack on its own doesn&rsquo;t prove anything. Concrete shrinks as it cures, and plenty of hairline cracks never change. What matters is whether it&rsquo;s moving: getting wider, longer, or offset. Marking the ends of a crack with a pencil and the date is an easy way to find out over a few months.</p>
<h2>Water is the lever</h2>
<p>Because expansive clay reacts to changes in moisture, the most effective thing a homeowner can do is keep the moisture around the foundation steady:</p>
<ul><li><b>Grade.</b> The ground should fall away from the house. The Utah Residential Code calls for at least 6 inches of fall within the first 10 feet (<a href="{irc}" rel="noopener">R401.3</a>), and desert landscaping settles over time, so check it.</li>
<li><b>Downspouts.</b> Carry roof water well away from the foundation instead of dumping it at the corner.</li>
<li><b>Sprinklers and drip lines.</b> Keep spray off the walls and drip emitters out of beds right against the house. A single over-watered planter can lift one corner.</li>
<li><b>Leaks.</b> A slow leak in a supply or sewer line under a slab can soak clay for months before anyone notices.</li>
<li><b>Consistency.</b> Wild swings (bone-dry summer, then heavy watering) are harder on clay than steady conditions.</li></ul>
<p>It also helps to keep a simple record of your own house. Photograph the cracks you have now, note which doors stick and in what season, and write down the date. If something changes after a wet spring, a new sprinkler zone or a plumbing repair, that record is the most useful thing you can hand an inspector, and it costs nothing to keep.</p>
<h2>When the foundation has already moved</h2>
<p>If a section of the foundation has dropped or heaved enough to crack walls and jam doors, fixing the water is still step one, but it won&rsquo;t put the house back. Depending on what an inspection finds, the options include <a href="@/crack_repair/">crack repair</a> for cracks that have stopped moving, <a href="@/complete_leveling_services/">house leveling</a>, and <a href="@/helical_foundation_repair/">helical piers</a>, which are advanced through the problem soil to stable ground below so the foundation no longer rides on the layer that swells and shrinks. Where water is getting in, <a href="@/waterproofing_services/">waterproofing</a> belongs in the plan too.</p>
<p>Not every crack needs a pier, and not every house on clay needs a repair at all. That&rsquo;s the point of an inspection: to find out which situation you&rsquo;re in before anyone sells you a fix.</p>
<h2>Building or buying in St. George</h2>
<p>If you&rsquo;re building, the geotechnical report the UGS recommends is the document that tells your engineer what the soil will do and what the foundation needs. If you&rsquo;re buying, ask whether one exists for the lot or subdivision, walk the house for the signs above, and look at how the yard is graded and watered.</p>
<p>Seeing cracks or sticking doors in Southern Utah? Call our <a href="@/st_george/">St. George office</a> at 435-668-0734 for a free inspection.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Sources: <a href="{ugs}" rel="noopener">Utah Geological Survey, Survey Notes: Geologic-Hazard and Adverse-Construction-Condition Maps for the St. George&ndash;Hurricane Area</a>; <a href="{wc}" rel="noopener">Washington County hazards map service, Expansive Rock and Soil layer</a>; <a href="{irc}" rel="noopener">Utah Residential Code 2021, R401.3</a>.</p>'''
    body = _["phero"](trail, POST[0], f"By {NAME} &middot; October 19, 2026", "Blog &middot; Southern Utah", "pier-rig-desert", "Pier installation rig at a home in the Southern Utah desert") + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">{body_txt}</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "Expansive Clay Soil in St. George, Utah | Superior Foundation",
            "meta": "Why expansive clay soil cracks St. George foundations, slabs and driveways, the signs to look for, and what helps, from water control to helical piers.",
            "body": body, "og": "pier-rig-desert", "ogtype": "article",
            "schema": [crumbs_ld(path, trail), faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-19", "dateModified": "2026-10-19",
                       "image": U + "assets/img/pier-rig-desert.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)}]}


def index():
    trail = [_["HOME"], ("Blog", "blog/")]
    A = _["A"]
    items = [(POST[0], POST[1], "pier-rig-desert")] + [(t, p, i) for k, p, t, i in posts() if k != DUP]
    cards = "".join(f'<a class="post-card reveal" href="@/{p}">{img(i, "")}<b>{t}</b><em>Read {A}</em></a>' for t, p, i in items)
    body = _["phero"](trail, "Foundation Repair Blog", "Guides on cracks, settlement, piers and waterproofing for Utah homeowners.", "Blog") + f'<section class="sec"><div class="wrap"><div class="posts">{cards}</div></div></section>' + _["cta"]()
    return {"path": "blog/", "canonical": EXT["blog"]["canon"] or canon("blog/"), "title": "Foundation Repair Blog for Utah Homeowners | Superior",
            "meta": "Foundation repair guides for Utah homeowners from Superior Foundation Repair: cracks, settlement, helical piers, efflorescence, expansive clay and waterproofing.",
            "body": body, "schema": [crumbs_ld("blog/", trail)]}


def pages():
    return [index(), new_post()] + [old_post(*p) for p in posts()]
