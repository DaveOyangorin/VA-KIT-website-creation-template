"""Blog for davenportfoundationrepair.com: the 100 existing posts (same URLs and text) with the blog index and its 4 pagination
pages, plus one new post.

New post: "Collapsible Soils in Utah: Why Some Homes Settle When the Ground Gets Wet"
Main phrase: "collapsible soils utah" (informational). None of the 100 posts covers it; it targets no service keyword and links to
the settlement, push pier, downspout extension and concrete leveling pages. Facts and sources, checked 19 Oct 2026:
- Utah Geological Survey, Problem Soils: collapsible soils have considerable strength when dry and natural but settle significantly
  through hydrocompaction (loss of air space in the soil) when wetted; typically associated with young alluvial fans, debris flows
  and loess. https://geology.utah.gov/hazards/problem-soils/
- UGS Survey Notes, Protecting Utah Homes From Geologic Hazards: collapsible soils undergo a volume decrease when wet, inducing
  subsidence that may cause structural damage. https://geology.utah.gov/map-pub/survey-notes/protecting-utah-homes-from-geologic-hazards/
- UGS Special Study 127 (St. George-Hurricane area): such soils can settle up to 10 percent of the susceptible deposit's thickness
  when first wetted; grain bonds from capillary tension or binders such as silt, clay or salt weaken when wet.
  https://ugspub.nr.utah.gov/publications/special_studies/ss-127/ss-127pl7.pdf
No prices.
"""
import html, json, os, re
from engine import crumbs_ld, faq_html, faq_ld, canon, img
from cfg import U, NAME, HERE, DOMAIN
from migrate import migrate

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
POST = ("Collapsible Soils in Utah: Why Some Homes Settle When the Ground Gets Wet", "about-us/our-blog/collapsible-soils-in-utah-why-homes-settle.html")
MON = {m: i + 1 for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])}
_ = {}
PER = 21  # keeps the live five blog index pages (101 posts)


def setup(phero, cta, side, arrow, home, est, tidy, section):
    _.update(phero=phero, cta=cta, side=side, A=arrow, HOME=home, EST=est, tidy=tidy, section=section)


def posts():
    out = []
    for k, v in EXT.items():
        if not re.match(r"about_us_our_blog_\d+_", k): continue
        path = re.sub(r"^https?://(www\.)?davenportfoundationrepair\.com/", "", v["url"])
        body = _["tidy"](migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x"), skip_heads=(html.unescape(v["heads"][0][1]) if v["heads"] else "",)))
        m = re.search(r"<p>([A-Z][a-z]+) (\d{1,2})(?:st|nd|rd|th), (\d{4})(?: by ([^<]+))?</p>\n?", body)
        date, author = "2000-01-01", NAME
        if m:
            date = f"{m.group(3)}-{MON.get(m.group(1), 1):02d}-{int(m.group(2)):02d}"
            if m.group(4): author = html.unescape(m.group(4)).strip()
            body = body.replace(m.group(0), "", 1)
        title = html.unescape(v["heads"][0][1]) if v["heads"] and v["heads"][0][0] == "h1" else html.unescape(v["title"]).split("|")[0].strip()
        out.append({"key": k, "path": path, "title": title, "date": date, "author": author, "body": body, "meta": v.get("meta") or ""})
    return sorted(out, key=lambda p: (p["date"], p["path"]), reverse=True)


def nice(d):
    y, m, dd = d.split("-")
    return f"{[k for k, v in MON.items() if v == int(m)][0]} {int(dd)}, {y}" if y != "2000" else ""


def excerpt(b, n):
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b))).strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def old_post(p):
    A = _["A"]; trail = [_["HOME"], ("Blog", "about-us/our-blog.html"), (html.escape(p["title"]), p["path"])]
    body = _["phero"](trail, html.escape(p["title"]), None, "Blog" + (" &middot; " + nice(p["date"]) if nice(p["date"]) else ""), buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post"><p class="mono meta">{html.escape(p["author"])}{" &middot; " + nice(p["date"]) if nice(p["date"]) else ""}</p>
{p["body"]}<p class="more"><a class="tlink" href="@/about-us/our-blog.html">All posts {A}</a></p></article>{_["side"]()}</div></section>''' + _["cta"]()
    meta = p["meta"] or excerpt(p["body"], 155)
    meta = html.unescape(meta)
    if len(meta) > 160: meta = meta[:157].rsplit(" ", 1)[0] + "..."
    for add in (" From Davenport Foundation Repair in West Jordan, Utah.", " Davenport Foundation Repair, West Jordan, UT.", " Free inspections."):
        if len(meta) < 150 and len(meta + add) <= 160: meta += add
    t = p["title"] if len(p["title"]) > 40 else f"{p['title']} | Davenport Foundation Repair"
    if len(t) > 60: t = t[:60].rsplit(" ", 1)[0].rstrip(":,.-&")
    v = EXT[p["key"]]
    return {"path": p["path"], "canonical": v.get("canon") or canon(p["path"]), "title": html.escape(t, quote=False), "meta": html.escape(meta, quote=False), "body": body, "ogtype": "article",
            "_ex": excerpt(p["body"], 170),
            "schema": [{"@type": "BlogPosting", "@id": canon(p["path"]) + "#post", "headline": p["title"], **({"datePublished": p["date"]} if nice(p["date"]) else {}),
                        "author": {"@type": "Person", "name": p["author"]} if p["author"] != NAME else {"@type": "Organization", "@id": U + "#business"},
                        "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p["path"])}, crumbs_ld(p["path"], trail)]}


FAQ = [("What are collapsible soils?", "Soils that are strong when dry but settle when they get wet. The Utah Geological Survey describes them as losing air space within the soil (hydrocompaction) when wetted, which can make the ground beneath a foundation drop."),
       ("Where are collapsible soils found in Utah?", "The Utah Geological Survey associates them with young alluvial fans, debris-flow deposits and wind-blown silt (loess). Alluvial fans are common along Utah's mountain fronts, where many neighborhoods are built."),
       ("How much can these soils settle?", "In a Utah Geological Survey study of the St. George&ndash;Hurricane area, collapsible deposits could settle up to 10 percent of their thickness when first wetted. How much a given home settles depends on the deposit and how much water reaches it."),
       ("What wets the soil under a house?", "Usually water we add: lawn and garden irrigation against the foundation, downspouts that empty at the wall, poor grading, and leaking water or sewer lines."),
       ("Can settlement from collapsible soil be repaired?", "Often, yes. Piers driven through the problem soil to firmer layers can stabilize a settling foundation, and sunken slabs can be lifted. The first step is an inspection to confirm the cause.")]


def new_post():
    A = _["A"]; path = POST[1]; sec = _["section"]
    trail = [_["HOME"], ("Blog", "about-us/our-blog.html"), ("Collapsible soils in Utah", path)]
    body = _["phero"](trail, POST[0], "Some Utah soils hold a house up perfectly well, until water reaches them. Here is what collapsible soils are, where they occur, and what homeowners can do.", "Blog &middot; October 19, 2026", buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">
<p class="mono meta">{NAME} &middot; October 19, 2026 &middot; 6 min read</p>
<p class="answer">Collapsible soils are dry, loosely packed soils that are strong in their natural state but settle when they get wet. The Utah Geological Survey calls the process hydrocompaction: water weakens the bonds between grains, the air spaces close up, and the ground drops. Under a house, that can mean a corner or one side of the foundation sinking, often after years of no trouble at all.</p>

<h2>Strong when dry, weak when wet</h2>
<p>Most people expect the ground under a house to be either good or bad. Collapsible soil is both. In its dry, natural state it has considerable strength and can carry a foundation without complaint. The grains are held together at their contact points, by capillary tension in the small amount of water present or by binders such as silt, clay or salt, according to the Utah Geological Survey.</p>
<p>When more water arrives, those bonds weaken. The grains slide into the open spaces between them and the soil takes up less volume. Nothing about the surface warns you beforehand: the change happens below the footing, out of sight, and often long after the house was built.</p>

<h2>Where collapsible soils occur in Utah</h2>
<p>The Utah Geological Survey associates collapsible soils with young alluvial fans, debris-flow deposits and loess, the fine, wind-blown silt. Alluvial fans form where streams leave the mountains and spread their sediment out, which is exactly where much of Utah has built: along the foothills of the Wasatch Front, in Utah County and in southwestern Utah.</p>
<p>Not every alluvial fan is collapsible, and not every lot on one has a problem. But it is one of the reasons two houses on the same street can behave very differently.</p>

<h2>How much the ground can drop</h2>
<p>The amount depends on how thick the susceptible layer is and how much water reaches it. In a Utah Geological Survey study of the St. George&ndash;Hurricane area, collapsible deposits could settle up to 10 percent of their thickness when first wetted. Even a fraction of that, under one corner of a house, is enough to crack walls and tilt floors.</p>
{sec("piers")}
<p>The survey&rsquo;s summary for homeowners is plain: collapsible soils lose volume when saturated, and the subsidence that follows can cause structural damage.</p>

<h2>What wets the soil under a house</h2>
<p>Rain and snowmelt play a part, but in many cases the water is something we add ourselves:</p>
<ul>
<li><b>Irrigation against the foundation.</b> Lawns, flower beds and drip lines watered right up to the wall, season after season.</li>
<li><b>Downspouts that dump at the wall.</b> A whole roof&rsquo;s worth of water concentrated in one spot. <a href="@/basement-waterproofing/products/gutter-downspout-extensions.html">Downspout extensions</a> carry it away from the house.</li>
<li><b>Grading that slopes toward the house.</b> Water should run away from the foundation, not toward it.</li>
<li><b>Leaking water and sewer lines.</b> A slow leak under or beside a house can wet soil for months before anyone notices.</li>
</ul>
<p>That is why settlement on collapsible soil often starts at one corner or along one side: the side with the sprinklers, the downspout or the leak.</p>

<h2>Signs your house may be settling</h2>
<ul>
<li>Stair-step cracks in block or brick, or cracks that are wider at one end.</li>
<li>Doors and windows that start to stick or won&rsquo;t latch.</li>
<li>Floors that slope or feel uneven.</li>
<li>Gaps where walls meet ceilings or floors.</li>
<li>A chimney or porch pulling away from the house.</li>
<li>Sunken concrete next to the foundation, where the same wet soil has dropped under the slab.</li>
</ul>
<p>Our page on <a href="@/foundation-repair/foundation-problems/settlement-sinking.html">foundation settlement</a> shows what these look like in more detail.</p>

<h2>What can be done</h2>
<p>The first step is always to control the water: extend downspouts, pull irrigation back from the foundation, fix the grading and repair any leaking lines. That slows or stops further collapse.</p>
<p>If the foundation has already settled, the usual fix is to stop relying on the problem soil altogether. <a href="@/foundation-repair/foundation-repair-products/pier-system.html">Steel push piers</a> are driven through the weak layer to firmer soil below, and the weight of the house is transferred onto them. Where the ground has dropped under a driveway, walkway or patio, the slab can often be lifted back into place with <a href="@/concrete-leveling.html">concrete leveling</a>.</p>
<h2>What an inspection looks at</h2>
<p>When settlement is the question, the inspection looks at the whole house, not just the worst crack. That means measuring floor levels across rooms, checking the pattern and width of cracks inside and out, looking at doors, windows and the chimney, and walking the outside to see where water goes: downspouts, sprinkler heads, grading and any wet or sunken areas next to the foundation. Together those clues show which part of the house is moving and why, which is what decides the repair.</p>
<p>Every house is different, and the right repair depends on what is actually happening below grade. A free inspection is the place to start.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>Utah Geological Survey, Problem Soils: <a href="https://geology.utah.gov/hazards/problem-soils/" rel="noopener">geology.utah.gov</a></li>
<li>Utah Geological Survey, Survey Notes, Protecting Utah Homes From Geologic Hazards: <a href="https://geology.utah.gov/map-pub/survey-notes/protecting-utah-homes-from-geologic-hazards/" rel="noopener">geology.utah.gov</a></li>
<li>Utah Geological Survey, Special Study 127 (St. George&ndash;Hurricane area), collapsible soil plate: <a href="https://ugspub.nr.utah.gov/publications/special_studies/ss-127/ss-127pl7.pdf" rel="noopener">ugspub.nr.utah.gov</a></li>
</ul></div>
</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "Collapsible Soils in Utah: Why Some Homes Settle",
            "meta": "Collapsible soils in Utah are strong when dry but settle when wet. Where they occur, how much they can drop, what wets them, and how settlement is repaired.",
            "body": body, "ogtype": "article", "og": "push-pier-grantsville", "_ex": "Some Utah soils hold a house up perfectly well until water reaches them. What collapsible soils are, where they occur, and what to do.", "_date": "2026-10-19",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-19", "dateModified": "2026-10-19",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index_pages(items):
    A = _["A"]; pages = [items[i:i + PER] for i in range(0, len(items), PER)]
    out = []
    for n, chunk in enumerate(pages, 1):
        path = "about-us/our-blog.html" if n == 1 else f"about-us/our-blog/page{n}.html"
        trail = [_["HOME"], ("Blog", "about-us/our-blog.html")] + ([(f"Page {n}", path)] if n > 1 else [])
        rows = "".join(f'<a class="prow reveal" href="@/{pg["path"]}"><span class="mono">{nice(d)}</span><b>{html.escape(t)}</b><span class="ex">{pg["_ex"]}</span><i>{A}</i></a>' for pg, t, d in chunk)
        nav = '<nav class="pager" aria-label="Blog pages">' + "".join(
            (f'<span aria-current="page">{i}</span>' if i == n else f'<a href="@/{"about-us/our-blog.html" if i == 1 else f"about-us/our-blog/page{i}.html"}">{i}</a>') for i in range(1, len(pages) + 1)) + "</nav>"
        body = _["phero"](trail, "The Davenport Foundation Repair Blog" + (f" &middot; Page {n}" if n > 1 else ""), "Foundation, basement, crawl space and concrete advice for Utah homeowners." if n == 1 else None, "Blog", buttons=False) + f'''
<section class="sec"><div class="wrap"><div class="plist">{rows}</div>{nav}</div></section>''' + _["cta"]()
        key = "about_us_our_blog_html" if n == 1 else f"about_us_our_blog_page{n}_html"
        out.append({"path": path, "canonical": (EXT.get(key) or {}).get("canon") or canon(path),
                    "title": "Foundation Repair Blog | Davenport Foundation Repair" if n == 1 else f"Foundation Repair Blog, Page {n} | Davenport",
                    "meta": "The Davenport Foundation Repair blog: foundation, basement waterproofing, crawl space and concrete advice for Utah homeowners, from our West Jordan team." if n == 1 else
                            f"Page {n} of the Davenport Foundation Repair blog: foundation, basement waterproofing, crawl space and concrete articles for Utah homeowners.",
                    "body": body, "schema": [crumbs_ld(path, trail)]})
    return out


def paths():
    ps = [re.sub(r"^https?://(www\.)?davenportfoundationrepair\.com/", "", v["url"]) for k, v in EXT.items() if re.match(r"about_us_our_blog_\d+_", k)]
    n = (len(ps) + 1 + PER - 1) // PER
    return set(ps) | {POST[1], "about-us/our-blog.html"} | {f"about-us/our-blog/page{i}.html" for i in range(2, n + 1)}


def pages():
    ps = posts()
    olds = [(old_post(p), p["title"], p["date"]) for p in ps]
    np = new_post()
    items = [(np, POST[0], "2026-10-19")] + olds
    out = index_pages(items) + [np] + [o[0] for o in olds]
    for pg in out: pg.pop("_ex", None); pg.pop("_date", None)
    return out
