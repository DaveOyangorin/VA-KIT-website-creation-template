"""Pages for the dryhouse.com redesign: "Submittal".

Rocky Mountain Waterproofing sells to architects and builders as much as to homeowners (their own "ABC": Architects, Builders,
Common ground), and their pages read like product data: mils, hydrostatic head, R-values, IRC sections. So the site is set like
a construction submittal: section numbers in the MasterFormat style (07 11 00 Dampproofing, 07 14 00 Fluid-applied
waterproofing, 07 21 00 Thermal insulation, 33 46 00 Subdrainage), original drawings (a wall section with every layer they
install, a coating-thickness gauge in mils, hydrostatic-head columns from their own comparison chart, an interior wall elevation
of the six leak points), and a footer drawn as a sheet title block. Their own job photos (The House That SHE Built, 2020) are the
"site log". Colours from the logo: charcoal, the sun's amber, the sky's blue for water; membrane black and drafting paper.
All 47 live URLs kept (no trailing slash; /index.php is a duplicate of the home page and gets a redirect instead). Pages had no
canonical tags; the draft gives each page a self canonical, except the blog listing duplicates, which point to /blog.
Home targets "basement waterproofing west jordan"; every service page names West Jordan in title, H1 and first paragraph.
Left out until confirmed: "over 57 years" (dated), "85% of most common issues...", "Up to 40% of home energy loss...",
"200mph wind driven rain", "some of the best warranties in the industry", "leading brand in the nation", "Thousands of ...
project references", "one of the first companies in the nation", "leak free for over 45 years".
"""
import html, json, os, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, NAME, LEGAL, U, HERE, DOMAIN, CITIES
from migrate import migrate
from illus import wall_section, mil_gauge, head_columns, leak_elevation, SECTION_KEY, LEAKS, HEAD
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
BID = "estimate/"
LEAKREQ = "contact/leak-repair-request/"
HOME = ("Home", "")
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
NOTHING = re.compile(r"(?!x)x")
DROP = re.compile(r"over 57 years|85% of|Up to 40 ?%|200 ?mph|best warranties|leading brand|Thousands of Local|one of the first|leak free for over|"
                  r"^Print|^Preview$|Rate this item|votes\)|Subscribe to this RSS|^Written by|Last modified|Need a bid\?|^Apply Now|^Learn More|"
                  r"^\\r\\n$|gmi_url|Possible Trip Charge|Serves The Following|^\d+$|^Jobs$", re.I)
SCRUB = re.compile(r"\s*(?:[^.<>]*?\b(?:Click (?:on|here)|Clink on|Read more|To read more|To learn more|Learn more|check out link above|"
                   r"click on this link|on the following link|with this link|Click Here)\b[^.<>]*(?:\.|$))", re.I)


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def tidy(s):
    s = re.sub(r'(?s)<ul><li><a href="[^"]*print=1.*?</ul>\s*(?:<p>Print </a></li></ul>)?', "", s)
    s = re.sub(r"(?s)<p>\s*Print\s*</a></li></ul>", "", s)
    s = s.replace("\\u00a0", " ").replace("&nbsp;", " ")
    out = []
    for blk in re.findall(r"<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s, re.S):
        if blk.startswith("<p>"):
            blk = SCRUB.sub("", blk)
            txt = html.unescape(re.sub(r"<[^>]+>", "", blk)).strip()
            if len(txt) < 3: continue
            # short label paragraphs ("Cracks under Windows") are headings in the original layout
            if len(txt) < 44 and not re.search(r"[.!?:,]$", txt) and not txt[0].isdigit() and "$" not in txt:
                blk = f"<h3>{txt}</h3>"
        if re.fullmatch(r"<h[23]>\s*</h[23]>", blk): continue
        out.append(blk)
    def head(b): return b.startswith(("<h2>", "<h3>"))
    out = [b for i, b in enumerate(out) if not (head(b) and i + 1 < len(out) and out[i + 1].startswith("<h2>"))]
    while out and head(out[-1]): out.pop()
    s = "\n".join(out)
    s = re.sub(r"<h2>", "<h3>", s)  # the page H1 + our section headings carry the outline; old H2s become H3s
    s = re.sub(r"</h2>", "</h3>", s)
    s = re.sub(r'href="@/([^"]*?)/?"', lambda m: f'href="@/{m.group(1).strip("/")}/"' if m.group(1).strip("/") else 'href="@/"', s)
    return s


def mig(key, skip=(), drop=DROP):
    return tidy(migrate(HERE, key, DOMAIN, drop, skip_heads=skip))


def section_of(h, heading, until=r"<h3>"):
    """The blocks after a given <h3> heading, up to the next h3."""
    m = re.search(r"<h3>" + re.escape(heading) + r"</h3>\s*(.*?)(?=" + until + r"|\Z)", h, re.S | re.I)
    return m.group(1).strip() if m else ""


def header():
    return Q(f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{img("rmwp-logo", NAME, lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">
<a href="@/services/belowgrade/"><small>07 10 00</small>Below grade</a><a href="@/services/belowgrade/waterproofing/"><small>07 14 00</small>Waterproofing</a><a href="@/services/belowgrade/damp-proof/"><small>07 11 00</small>Damp proofing</a>
<a href="@/services/horizontal-services/"><small>07 18 00</small>Horizontal</a><a href="@/services/above-grade/"><small>07 25 00</small>Above grade</a><a href="@/services/leak-repair/"><small>03 01 00</small>Leak repair</a><a href="@/services/"><small>&mdash;</small>All services</a></div></details></li>
<li><a href="@/services/leak-repair/">Leak Repair</a></li><li><a href="@/about/">About</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/contact/">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{PHONE}<span>{S["phone"]}</span></a><a class="btn" href="@/{BID}">Request a Bid</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/services/">All services</a><a href="@/services/belowgrade/">Below grade</a><a href="@/services/belowgrade/waterproofing/">Waterproofing</a><a href="@/services/horizontal-services/">Horizontal</a><a href="@/services/above-grade/">Above grade</a>
<a href="@/services/leak-repair/">Leak repair</a><a href="@/about/">About</a><a href="@/blog/">Blog</a><a href="@/contact/">Contact</a><a href="@/{BID}">Request a bid</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>''')


def footer():
    soc = " &middot; ".join(f'<a href="{S[k]}" rel="noopener">{n}</a>' for k, n in [("fb", "Facebook"), ("ig", "Instagram"), ("li", "LinkedIn"), ("yt", "YouTube"), ("tw", "Twitter"), ("houzz", "Houzz")])
    return Q(f'''<footer class="site-footer"><div class="wrap">
<div class="titleblock">
<div class="tb-cell tb-logo">{img("rmwp-logo", NAME + " logo")}<p>{LEGAL} &middot; DBA {NAME}</p></div>
<div class="tb-cell"><span class="tb-k">Office</span><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p class="small">{S["hours"]}</p></div>
<div class="tb-cell"><span class="tb-k">Call</span><p><a class="fph" href="tel:{S["tel"]}">{S["phone"]}</a></p><p class="small">Toll free <a href="tel:{S["tel_toll"]}">{S["toll"]}</a><br>Fax {S["fax"]}</p></div>
<div class="tb-cell"><span class="tb-k">Services</span><ul><li><a href="@/services/belowgrade/">Below grade</a></li><li><a href="@/services/horizontal-services/">Horizontal</a></li><li><a href="@/services/above-grade/">Above grade</a></li><li><a href="@/services/leak-repair/">Leak repair</a></li></ul></div>
<div class="tb-cell"><span class="tb-k">Company</span><ul><li><a href="@/about/">Who we are</a></li><li><a href="@/about/rmwp-history/">History</a></li><li><a href="@/about/jobs/">Jobs</a></li><li><a href="@/contact/accounts/">Accounts</a></li><li><a href="@/about/trade-memberships/">Memberships</a></li></ul></div>
<div class="tb-cell tb-rev"><span class="tb-k">Est.</span><b>1960</b><span class="tb-k">Motto</span><p>&ldquo;Do It Right The First Time&rdquo;</p></div>
</div>
<div class="fbottom"><span>&copy; 2026 {NAME}</span><span>{soc}</span><span><a href="@/about/privacy/">Privacy</a> &middot; <a href="@/about/social/">Social</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{BID}">Request a Bid</a></div>''')


def cta(title="Send the plans. We&rsquo;ll send the bid.", text="Builders and architects: upload plans, spec info or site pictures with the bid request. Homeowners with a leak: use the leak repair request and include photos of the leaking areas."):
    return f'''<section class="cta"><div class="wrap cta-in">
<div><p class="label">Bids &amp; leak repair</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="cta-card"><a class="btn" href="@/{BID}">Request a Bid {ARROW}</a><a class="btn ghost" href="@/{LEAKREQ}">Leak Repair Request</a>
<p class="cta-ph"><a href="tel:{S["tel"]}">{S["phone"]}</a><span>Toll free {S["toll"]} &middot; {S["hours"]}</span></p></div></div></section>'''


def phero(trail, h1, lede, code, image=None, alt="", spec=None):
    """Page hero set like a submittal cover: crumbs, section number, H1; the photo carries a spec tag."""
    sec, name = (code.split(" &middot; ", 1) + [""])[:2] if " &middot; " in code else (code, "")
    art = ""
    if image:
        tag = f'<figcaption class="spec-tag"><span>SECTION {sec}</span><b>{name or html.unescape(re.sub("<[^>]+>", "", h1))[:40]}</b><span>{NAME}</span></figcaption>' if sec and sec[0].isdigit() else ""
        art = f'<figure class="ph-img">{img(image, alt, priority=True)}{tag}</figure>'
    return f'''<section class="phero{" has-img" if image else ""}"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label code">{code}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}
<div class="btn-row"><a class="btn" href="@/{BID}">Request a Bid {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>{art}</div></section>'''


def side(extra=""):
    return f'''<aside class="sv-side"><div class="spec-card"><p class="tb-k">Submittal contact</p><p class="sc-name">{NAME}</p>
<dl><div><dt>Office</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div><div><dt>Toll free</dt><dd>{S["toll"]}</dd></div><div><dt>Hours</dt><dd>{S["hours"]}</dd></div><div><dt>Yard</dt><dd>{S["street"]}, {S["city"]}</dd></div></dl>
<a class="btn" href="@/{BID}">Request a Bid {ARROW}</a><a class="tlink" href="@/{LEAKREQ}">Leak repair request {ARROW}</a></div>{extra}</aside>'''


def compare_table():
    rows = [("Cost", [h[3] for h in HEAD]), ("Hydrostatic head", [h[2] for h in HEAD]), ("Recommended use", [h[4] for h in HEAD]), ("Level", [h[5] for h in HEAD])]
    return ('<div class="tbl-wrap"><table class="spec"><caption>Coating options compared (from our comparison chart)</caption><thead><tr><th scope="col">Spec</th>' +
            "".join(f'<th scope="col">{h[0]}</th>' for h in HEAD) + "</tr></thead><tbody>" +
            "".join(f'<tr><th scope="row">{k}</th>' + "".join(f"<td>{v}</td>" for v in vals) + "</tr>" for k, vals in rows) + "</tbody></table></div>")


def insul_table():
    data = [("Warm N Dri", "R-3 to R-15", "Low flow (sand)", "Thermal break (basement walls)", "&mdash;"),
            ("Thermal Drain", "R-3 to R-15", "Low&ndash;mid (sand)", "Thermal break (basement) / added protection", "Higher tensile strength (waterproofing)"),
            ("DrainMat + EPS", "R-5 to R-20", "Highest (gravel)", "Commercial / custom projects", "Higher R-value"),
            ("Fanfold board", "R-1", "None", "Protection course", "Low-cost protection")]
    return ('<div class="tbl-wrap"><table class="spec"><caption>Insulation and drainage boards compared</caption><thead><tr><th scope="col">Board</th><th scope="col">R-value</th><th scope="col">Flow rate</th><th scope="col">When to use</th><th scope="col">Added performance</th></tr></thead><tbody>' +
            "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in data) + "</tbody></table></div>")


def key_list(items, start=1):
    li = []
    for i, it in enumerate(items, start):
        n, p, c = (list(it) + [""])[:3]
        li.append(f'<li><span class="k-n">{i}</span><a href="@/{p}">{n}</a>{f"<small>{c}</small>" if c else ""}</li>')
    return '<ol class="key">' + "".join(li) + "</ol>"


def page(key, path, label, h1, lede, code, title, meta, image=None, alt="", intro="", content=None, before="", extra="", skip=(), drop=DROP, crumbs=None,
         form=None, robots=None, sitemap=True, canonical=None, schema=None, sidebar=True):
    trail = [HOME] + (crumbs or []) + [(label, path)]
    body_txt = content if content is not None else (mig(key, skip=skip + (html.unescape(h1), html.unescape(label)), drop=drop) if key else "")
    main = (f'<p class="answer">{intro}</p>' if intro else "") + before + body_txt + extra
    right = f'<div class="form-col">{form}</div>' if form else (side() if sidebar else "")
    body = phero(trail, h1, lede, code, image, alt) + f'''
<section class="sec"><div class="wrap sv-grid{" wide" if not right else ""}"><article class="prose">{main}</article>{right}</div></section>''' + ("" if form else cta())
    pg = {"path": path, "canonical": canonical or canon(path), "title": title, "meta": meta, "body": body, "og": image, "schema": [crumbs_ld(path, trail)] + (schema or [])}
    if robots: pg["robots"] = robots
    if not sitemap: pg["sitemap"] = False
    return pg


def svc(path, name):
    return [{"@type": "Service", "@id": canon(path) + "#service", "name": name, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": "West Jordan, UT"}}]


def towns():
    raw = open(os.path.join(HERE, "src", "pages", "home.html"), encoding="utf-8").read()
    i = raw.find("Alpine, Utah"); j = raw.find("Woods Cross, Utah", i) + 40
    seg = raw[i:j]
    out = []
    for part in re.split(r"<br\s*/?>", seg):
        t = html.unescape(re.sub(r"<[^>]+>", "", part)).strip()
        m = re.match(r"([A-Za-z .'\-]+), Utah", t)
        if m: out.append((m.group(1).strip(), "." in t[m.end():] or "<i" in part))
    return out


TOWNS = towns()

HOME_FAQ = [
    ("What is the difference between damp proofing and waterproofing?", "Damp proofing is a thin asphalt coat (10&ndash;20 mils) that slows vapor through the wall. It has almost no stretch, so it cracks with the foundation. Waterproofing is an asphalt emulsion blended with rubber, at least 40 mils and up to 80+ mils thick, so it stretches over the cracks that form in a foundation."),
    ("Is damp proofing enough for a basement?", "It is the minimum the building code allows for most new homes. Think about how the basement will be used: if you plan to finish it, waterproofing is the better match, because damp proofing cracks with the concrete when settling occurs and can cost more later in repairs."),
    ("Can you fix a leak in a basement that is already finished?", "Often, yes. We fix active leaks from the inside or the outside: cracks under windows, form ties, honeycomb, cold joints and pipe penetrations. Many can be sealed from inside with urethane injection. We don&rsquo;t fix plumbing, but we routinely fix where pipes come through the foundation."),
    ("Do you work on commercial projects?", "Yes. Our three divisions (below-grade waterproofing, specialty and horizontal waterproofing, and foundation leak repair) work on everything from simple additions to complex commercial projects, including government work with special requirements. Most work is on Net 30 terms."),
    ("Which areas do you serve?", "We&rsquo;re based in West Jordan and work across Utah. Our service-area list covers 288 Utah towns; some farther towns may need a trip charge."),
    ("How do I get a bid?", "Send the bid request with your plans, spec info or site pictures (or a Dropbox or Google Drive link), or call the office at 801-282-2100."),
]


def home():
    town_list = "".join(f'<li{" class=trip" if t else ""}>{n}</li>' for n, t in TOWNS)
    near = " &middot; ".join(CITIES)
    log = [("foundation-waterproofed", "Tuff-N-Dri waterproofing on the finished walls, window wells set"), ("trench-wasatch-truck", "Footing drain trench, Wasatch Front behind"),
           ("crew-in-trench", "Prepping the wall in the trench"), ("window-well-set", "Setting a window well against the waterproofed wall"),
           ("libby-sarah-site", "Libby and Sarah on site"), ("she-built-sign", "The House That SHE Built, 2021 Parade of Homes")]
    logs = "".join(f'<figure class="log reveal">{img(n, c)}<figcaption><span>LOG {i + 1:02d}</span>{c}</figcaption></figure>' for i, (n, c) in enumerate(log))
    divisions = [("Below grade", "services/belowgrade/", "07 10 00", "Waterproofing and damp proofing, foundation drains, insulation and drainage boards for new foundations.", "crew-in-trench"),
                 ("Horizontal", "services/horizontal-services/", "07 18 00", "Suspended slabs, post-tension slabs, decks, walkways and porch caps, plus under-slab waterproofing.", "trench-wasatch-truck"),
                 ("Above grade", "services/above-grade/", "07 25 00", "EnviroDri, a liquid-applied, vapor-permeable weather-resistive and air barrier for new homes.", "she-built-sign"),
                 ("Leak repair", "services/leak-repair/", "03 01 00", "Active leaks fixed inside or out: cracks, ties, honeycomb, cold joints, floor joints and pipes.", "honeycomb-wall")]
    divs = "".join(f'<a class="div-card reveal" href="@/{p}">{img(i, n + " work by Rocky Mountain Waterproofing")}<span class="dc-code">{c}</span><b>{n}</b><span>{d}</span><em>{n} {ARROW}</em></a>' for n, p, c, d, i in divisions)
    body = f'''
<section class="hero"><div class="wrap hero-in">
<div class="hero-text"><p class="label code">West Jordan, Utah &middot; Est. 1960</p>
<h1>Basement waterproofing in West Jordan, <span>done right the first time.</span></h1>
<p class="lede">Rocky Mountain Waterproofing has done basement waterproofing in West Jordan and across Utah since 1960: rubber-modified waterproofing and damp proofing, foundation drains and insulation for new construction, and leak repair for basements that are already finished.</p>
<div class="btn-row"><a class="btn" href="@/{BID}">Request a Bid {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
<p class="hero-note">Leaking now? <a href="@/{LEAKREQ}">Send a leak repair request</a> with photos.</p></div>
<figure class="hero-photo">{img("foundation-waterproofed", "New foundation in Utah coated with black Tuff-N-Dri waterproofing, with window wells set", priority=True)}
<figcaption class="spec-tag"><span>SECTION 07 14 00</span><b>Fluid-applied waterproofing</b><span>The House That SHE Built &middot; 2020</span></figcaption></figure>
</div></section>

<section class="facts" aria-label="Facts"><div class="wrap facts-in">
<div><b>1960</b><span>Founded as Modern Damp Proofing</span></div>
<div><b>1996</b><span>Renamed Rocky Mountain Waterproofing</span></div>
<div><b>40&ndash;80+</b><span>Mils of waterproofing, vs 10&ndash;20 for damp proofing</span></div>
<div><b>4</b><span>Douglas siblings own it today</span></div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label code">07 11 00 vs 07 14 00</p><h2>Damp proofing is <span>not</span> waterproofing.</h2>
<p>Damp proofing is the code minimum: a thin asphalt coat that slows vapor. It has almost no stretch, so when the foundation cracks (and every foundation does), the coating cracks with it.</p>
<p>Waterproofing is an asphalt emulsion blended with rubber, built up to 40 mils and as much as 80+. The rubber lets it stretch over cracks as they open. The difference shows up years later, in the number of callbacks for leaks.</p>
<p><a class="tlink" href="@/services/belowgrade/waterproofing/">Foundation waterproofing {ARROW}</a> &nbsp; <a class="tlink" href="@/services/belowgrade/damp-proof/">Damp proofing {ARROW}</a></p></div>
<figure class="sheet reveal">{mil_gauge()}<figcaption>Drawn to scale. Thicknesses from our below-grade services page.</figcaption></figure>
</div></section>

<section class="sec paper2"><div class="wrap split rev">
<figure class="sheet reveal">{wall_section()}</figure>
<div class="reveal"><p class="label code">Sheet A &middot; Wall section</p><h2>One wall. <span>Every layer we put on it.</span></h2>
<p>From the weather barrier above grade to the drain at the footing, here is where each of our systems goes on a typical Utah basement.</p>
{key_list([(n, p, c) for n, p, c in SECTION_KEY])}</div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label code">Product data</p><h2>How much water <span>each coating holds back.</span></h2>
<p>Hydrostatic head is the water pressure a coating can resist at a crack, measured in feet of water. Damp proofing is rated at none. That&rsquo;s why the coating should match the space: a crawlspace and a finished custom basement need different protection.</p>
{compare_table()}</div>
<figure class="sheet reveal">{head_columns()}</figure>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head reveal"><p class="label code">Divisions</p><h2>Four kinds of work, <span>one crew from West Jordan.</span></h2></div>
<div class="divs">{divs}</div></div></section>

<section class="sec"><div class="wrap split">
<figure class="sheet reveal">{leak_elevation()}</figure>
<div class="reveal"><p class="label code">Leak repair &middot; Interior elevation</p><h2>Already leaking? <span>We fix active leaks, inside or out.</span></h2>
<p>Most basement leaks start at one of six places. Pick yours to see what causes it and how it&rsquo;s sealed.</p>
{key_list(LEAKS)}
<a class="btn" href="@/{LEAKREQ}">Leak Repair Request {ARROW}</a></div>
</div></section>

<section class="sec paper2"><div class="wrap">
<div class="head reveal"><p class="label code">Site log &middot; Oct 2020</p><h2>The House That SHE Built.</h2>
<p class="lede">A home built entirely by women for the 2021 Parade of Homes. Libby and Sarah did the waterproofing, window wells and footing drain: Tuff-N-Dri on the walls and a strip drain in place of pipe and gravel.</p></div>
<div class="logs">{logs}</div>
<p><a class="tlink" href="@/blog/item/20-the-house-that-she-built/">Read the project story {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label code">Serving you</p><h2>A, B, C.</h2></div>
<div class="abc">
<div class="reveal"><span class="abc-l">A</span><b>Architects</b><p>Value-engineering options that meet the project budget, and fast-track engineering that speeds up the schedule.</p></div>
<div class="reveal"><span class="abc-l">B</span><b>Builders</b><p>Short lead times (often 1&ndash;2 days) regardless of project size, small or multiple trips if needed, and one source for protecting the project from the elements.</p></div>
<div class="reveal"><span class="abc-l">C</span><b>Common ground</b><p>We&rsquo;re homeowners too. In the industry or not, we speak your language, and we understand budgets and getting the most for your money.</p></div>
</div><p><a class="tlink" href="@/about/serving-you/">Serving you {ARROW}</a></p></div></section>

<section class="sec dark"><div class="wrap split">
<div class="reveal"><p class="label code">Since 1960</p><h2>A family business, <span>still in the family.</span></h2>
<ol class="timeline">
<li><b>1960</b><span>Modern Damp Proofing starts out doing damp proofing only, with Larry R. as president.</span></li>
<li><b>Then</b><span>The company passes to Cecil Douglas, who later sells it to his brother McKay Douglas.</span></li>
<li><b>1996</b><span>The name changes to match the work: Rocky Mountain Waterproofing.</span></li>
<li><b>Today</b><span>Owned by four of McKay and Ellen&rsquo;s children: Chris, Jenn, Tyler and Sam.</span></li></ol>
<a class="tlink light" href="@/about/rmwp-history/">Our history {ARROW}</a></div>
<div class="team reveal">{img("chris-douglas", "Christopher Douglas")}{img("tyler-douglas", "Tyler Douglas")}{img("sam-douglas", "Sam Douglas")}<p class="small">Christopher, Tyler and Sam Douglas</p></div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label code">Questions</p><h2>Good to know.</h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal"><p class="label code">Service area</p><h2>Based in West Jordan.</h2><p>Near the yard: {near}. Our list covers {len(TOWNS)} Utah towns, from Logan to St. George.</p>
<details class="towns"><summary>All {len(TOWNS)} towns we serve</summary><ul>{town_list}</ul><p class="small"><span class="trip-k"></span> Possible trip charge.</p></details>
<a class="guide" href="@/{p_blog.POST[1]}"><span class="label code">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Basement Waterproofing West Jordan | Rocky Mountain Waterproofing",
            "meta": "Basement waterproofing in West Jordan since 1960: waterproofing and damp proofing, foundation drains and insulation, and foundation leak repair. Request a bid.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def pages_main():
    sv = [("Services", "services/")]
    bg = sv + [("Below grade", "services/belowgrade/")]
    hz = sv + [("Horizontal", "services/horizontal-services/")]
    ag = sv + [("Above grade", "services/above-grade/")]
    ot = sv + [("Other services", "services/other-services/")]
    lr = sv + [("Leak repair", "services/leak-repair/")]
    ab = [("About", "about/")]
    ct = [("Contact", "contact/")]

    belowgrade = mig("services_belowgrade", skip=("Below Grade Services",))
    cut = belowgrade.find("<p>Foundations can be coated")
    bg_products, bg_coatings = belowgrade[:cut], belowgrade[cut:]
    bg_products = re.sub(r"(?s)<h3>Termite Control</h3>.*?(?=<p>Foundations|\Z)", "", bg_products)
    bg_products = re.sub(r"(?s)<h3>Termite Pre-Treatment</h3>\s*<p>FHA.*?</p>", "", bg_products)
    bg_coatings = bg_coatings.replace("<p>For Residential applications we offer many Waterproofing options with some of the best warranties in the industry. TREMCO brand waterproofing is the leading brand in the nation and offers competitive pricing and warranty for all projects.</p>",
                                      "<p>For residential applications we offer many waterproofing options, mainly from the TREMCO brand, with manufacturer warranties.</p>")
    leak = mig("services_leak_repair", skip=("Foundation Leak Repair", "Foundation Leak Problem Areas"))
    prev = mig("services_leak_repair_leak_prevention", skip=("Leak Prevention Overview",))
    req_pipe = "<p>We don&rsquo;t fix plumbing issues, but we routinely fix where pipes enter a home or business through the foundation.</p>"

    def wj(t): return t
    out = [
        page(None, "services/", "Services", "Waterproofing Services in West Jordan", "Below grade, horizontal, above grade and foundation leak repair, for homes and commercial projects.", "Services &middot; What we do",
             "Waterproofing Services in West Jordan | Rocky Mountain", "Waterproofing services in West Jordan since 1960: below-grade waterproofing and damp proofing, horizontal and under-slab work, EnviroDri and leak repair.",
             image="trench-wasatch-truck", alt="Footing drain trench at a new home site with the Wasatch Mountains behind",
             intro="Rocky Mountain Waterproofing provides waterproofing services in West Jordan and across Utah in three main divisions (below-grade waterproofing, specialty and horizontal waterproofing, and foundation leak repair), plus an above-grade weather barrier. We work on everything from simple additions to complex commercial projects.",
             content='<div class="svc-index">' + "".join(f'<div class="si"><p class="label code">{c}</p><h2><a href="@/{p}">{n}</a></h2><ul>' + "".join(f'<li><a href="@/{q}">{m}</a></li>' for m, q in subs) + "</ul></div>" for c, n, p, subs in [
                 ("07 10 00", "Below grade", "services/belowgrade/", [("Waterproofing", "services/belowgrade/waterproofing/"), ("Damp proofing", "services/belowgrade/damp-proof/"), ("Foundation insulation", "services/belowgrade/foundation-insulation/"), ("Foundation drains", "services/belowgrade/foundation-drains/")]),
                 ("07 18 00", "Horizontal", "services/horizontal-services/", [("TremProof 250 GC", "services/horizontal-services/tremproof250/"), ("Under-slab waterproofing", "services/horizontal-services/under-slab/")]),
                 ("07 25 00", "Above grade", "services/above-grade/", [("EnviroDri", "services/above-grade/envirodri/")]),
                 ("03 01 00", "Foundation leak repair", "services/leak-repair/", [("Leak prevention", "services/leak-repair/leak-prevention/"), ("Foundation cracks", "services/leak-repair/foundation-cracks/"), ("Cold joints", "services/leak-repair/cold-joints/"), ("Honeycomb", "services/leak-repair/honeycomb/"), ("Floor joints", "services/leak-repair/floor-joints/"), ("Pipe penetrations", "services/leak-repair/pipe-penetrations/"), ("Foundation ties", "services/leak-repair/ties/"), ("ICF foundation leaks", "services/leak-repair/icf-leaks/")]),
                 ("&mdash;", "Other services", "services/other-services/", [("Termite pre-treatment (no longer offered)", "services/other-services/termite/"), ("Window well install (no longer offered)", "services/other-services/window-wells/")])]) + "</div>" +
             f'<h2>Who we work for</h2><p>Architects, builders and homeowners. See <a href="@/about/serving-you/">how we serve each one</a>.</p>'),
        page(None, "services/belowgrade/", "Below grade", "Below-Grade Waterproofing in West Jordan", "Coatings, drainage, insulation and under-slab barriers: the whole wall, from footing to grade.", "07 10 00 &middot; Below-grade systems",
             "Below-Grade Waterproofing in West Jordan | Rocky Mountain", "Below-grade waterproofing in West Jordan: damp proofing and rubber-modified waterproofing, drainage mat, Thermal Drain, strip drain, insulation and Paraseal.",
             image="crew-in-trench", alt="Crew member in the trench beside a new concrete foundation wall",
             intro="Rocky Mountain Waterproofing installs complete below-grade systems in West Jordan and across Utah: foundation coatings (damp proofing, basic and premium waterproofing), drainage mat and Thermal Drain, strip drain footing drains, foundation insulation, and Paraseal under-slab barriers.",
             before=f'<figure class="sheet">{wall_section("bg")}</figure>{key_list(SECTION_KEY)}', content=bg_products, crumbs=sv, schema=svc("services/belowgrade/", "Below-grade waterproofing")),
        page(None, "services/belowgrade/waterproofing/", "Waterproofing", "Foundation Waterproofing in West Jordan", "Rubber-modified waterproofing, 40 to 80+ mils thick, that stretches over cracks as the foundation moves.", "07 14 00 &middot; Fluid-applied waterproofing",
             "Foundation Waterproofing in West Jordan | Rocky Mountain", "Foundation waterproofing in West Jordan: rubber-modified coatings 40 to 80+ mils thick that bridge cracks. Watchdog H3, Tuff-N-Dri QC, TremProof 260 and 250 GC.",
             image="foundation-waterproofed", alt="New foundation coated with black Tuff-N-Dri waterproofing",
             intro="Rocky Mountain Waterproofing applies foundation waterproofing in West Jordan and across Utah. Waterproofing is an asphalt-based emulsion blended with a rubberized polymer, at least 40 mils thick and up to 80+ mils, so it stretches over the cracks that form in a foundation.",
             before=f'<figure class="sheet">{mil_gauge("wp")}</figure>', content=bg_coatings, extra=f'<h2>Options compared</h2><figure class="sheet">{head_columns("wp")}</figure>{compare_table()}',
             crumbs=bg, schema=svc("services/belowgrade/waterproofing/", "Foundation waterproofing")),
        page("services_belowgrade_damp_proof", "services/belowgrade/damp-proof/", "Damp proofing", "Foundation Damp Proofing in West Jordan", "The basic code coating before backfill: a vapor retarder, not waterproof.", "07 11 00 &middot; Dampproofing",
             "Foundation Damp Proofing in West Jordan | Rocky Mountain", "Foundation damp proofing in West Jordan: MulSeal water-based asphalt emulsion, the IRC R406.1 minimum for new foundations, with under 14 g/L VOC content.",
             image="tie-patch-closeup", alt="Close-up of a coated foundation wall with patched form ties",
             intro="Rocky Mountain Waterproofing applies foundation damp proofing in West Jordan, the basic coating applied to a foundation wall before it is backfilled. It acts as a vapor retardant barrier and basic water protection, but it is not waterproof.",
             skip=("Damp Proofing",), extra=f'<h2>Damp proofing vs waterproofing</h2>{compare_table()}',
             crumbs=bg, schema=svc("services/belowgrade/damp-proof/", "Foundation damp proofing")),
        page("services_belowgrade_foundation_insulation", "services/belowgrade/foundation-insulation/", "Foundation insulation", "Foundation Insulation in West Jordan", "Extruded polystyrene, fan-fold board and Warm-N-Dri: insulation that can also drain and protect.", "07 21 00 &middot; Thermal insulation",
             "Foundation Insulation in West Jordan | Rocky Mountain", "Exterior foundation insulation in West Jordan: XPS board, fan-fold protection board, Warm-N-Dri (R-3, R-5, R-10), Thermal Drain and DrainMat with EPS.",
             image="crew-in-trench", alt="Foundation wall in a trench ready for insulation and drainage board",
             intro="Rocky Mountain Waterproofing installs foundation insulation in West Jordan. Insulation on the inside of a house is typically the most effective, but if you want insulation on the outside of the foundation, we can add it with one of our board options.",
             content=re.sub(r"(?s)<h3>3 / 4</h3>.*?inch Warm-N-Dri - \(R-10\)</p>", "", mig("services_belowgrade_foundation_insulation", skip=("Foundation Insulation", "Insulation / Drainage Compare"))) +
             '<ul><li>3/4 inch Warm-N-Dri: R-3</li><li>1 3/16 inch Warm-N-Dri: R-5</li><li>2 3/8 inch Warm-N-Dri: R-10</li></ul><h2>Insulation and drainage compared</h2>' + insul_table(),
             crumbs=bg, schema=svc("services/belowgrade/foundation-insulation/", "Foundation insulation")),
        page("services_belowgrade_foundation_drains", "services/belowgrade/foundation-drains/", "Foundation drains", "Foundation Drains in West Jordan", "Strip drain: an engineered footing drain that replaces pipe and gravel.", "33 46 00 &middot; Subdrainage",
             "Foundation &amp; Footing Drains in West Jordan | Rocky Mountain", "Foundation and footing drains in West Jordan: strip drain, an ICC-recognized engineered system that replaces pipe and gravel French drains with less labor.",
             image="trench-wasatch-truck", alt="Open trench along a new foundation for the footing drain",
             intro="Rocky Mountain Waterproofing installs foundation drains in West Jordan. Footing drain, French drain, pipe-and-gravel system, strip drain: a system with many names, but they all do the same job, draining water away from the structure.",
             skip=("Foundation Drains",), crumbs=bg, schema=svc("services/belowgrade/foundation-drains/", "Foundation drains")),
        page(None, "services/horizontal-services/", "Horizontal", "Horizontal Waterproofing in West Jordan", "Suspended slabs, post-tension slabs, decks and walkways, porch caps and horizontal drainage.", "07 18 00 &middot; Horizontal waterproofing",
             "Horizontal Waterproofing in West Jordan | Rocky Mountain", "Horizontal waterproofing in West Jordan for suspended slabs, post-tension slabs, plywood and cement decks, walkways and porch caps, plus drainage mat.",
             image="she-built-sign", alt="Front of The House That SHE Built, a new home with a porch cap",
             intro="Rocky Mountain Waterproofing does horizontal and specialty waterproofing in West Jordan: suspended slabs and porch caps over storage rooms, post-tension slabs, decks and walkways, and horizontal drainage. On The House That SHE Built we waterproofed the front porch to protect the storage room underneath.",
             content='<div class="spec-grid">' + "".join(f'<div><p class="label code">{c}</p><h3>{h}</h3><ul>' + "".join(f"<li>{x}</li>" for x in xs) + "</ul></div>" for c, h, xs in [
                 ("A", "Suspended slabs", ["Joint treatment", "Surface waterproofing"]), ("B", "Post-tension slabs", ["Preparation and detailing", "Post-tension slab waterproofing"]),
                 ("C", "Decks and walkways", ["Plywood decks", "Cement decks", "OSB decks (not recommended: we suggest plywood)"]), ("D", "Horizontal drainage", ["Drainage mat"])]) + "</div>" +
             f'<h2>Horizontal products</h2><ul><li><a href="@/services/horizontal-services/tremproof250/">TremProof 250 GC</a></li><li><a href="@/services/horizontal-services/under-slab/">Under-slab waterproofing (Paraseal)</a></li></ul><p>Tell us about the slab or deck and we&rsquo;ll recommend a detail. <a href="@/{BID}">Request a bid</a>.</p>',
             crumbs=sv, schema=svc("services/horizontal-services/", "Horizontal waterproofing")),
        page(None, "services/horizontal-services/tremproof250/", "TremProof 250 GC", "TremProof 250 GC Waterproofing in West Jordan", "One of the Tremco waterproofing membranes we apply.", "07 14 00 &middot; TremProof 250 GC",
             "TremProof 250 GC Waterproofing in West Jordan | Rocky Mountain", "TremProof 250 GC waterproofing in West Jordan: one of the Tremco membranes we apply, alongside Watchdog H3, Tuff-N-Dri QC and TremProof 260.",
             intro="Rocky Mountain Waterproofing applies TremProof 250 GC in West Jordan and across Utah. It is one of the Tremco waterproofing options we carry, along with Watchdog H3, Tuff-N-Dri QC and TremProof 260.",
             content=f'<p>Which membrane fits depends on the structure, the water conditions and how the space will be used. Send your plans or spec section and we&rsquo;ll recommend the right product and detail.</p><p><a class="tlink" href="@/services/belowgrade/waterproofing/">Compare our waterproofing options {ARROW}</a></p>',
             crumbs=hz, schema=svc("services/horizontal-services/tremproof250/", "TremProof 250 GC waterproofing")),
        page("services_horizontal_services_under_slab", "services/horizontal-services/under-slab/", "Under-slab waterproofing", "Under-Slab Waterproofing in West Jordan", "For projects deep enough to reach the water table.", "07 13 00 &middot; Under-slab barrier",
             "Under-Slab Waterproofing in West Jordan | Rocky Mountain", "Under-slab waterproofing in West Jordan for basements that reach the water table: Paraseal HDPE and bentonite, designed with an engineer, vs a sump pump.",
             intro="Rocky Mountain Waterproofing installs under-slab waterproofing in West Jordan for projects deep enough in the ground to reach the water table. There are two approaches to water table issues: mechanical pumping (a sump pump) or waterproofing under the slab.",
             skip=("Under-Slab Waterproofing",), drop=re.compile(DROP.pattern + r"|^To read more about Paraseal", re.I),
             extra='<h3>Paraseal</h3><p>Literally meaning &ldquo;two layer of seal&rdquo;, Paraseal consists of HDPE (high density polyethylene) and bentonite. It can protect against water table fluctuations and against seasonal changes causing high vapor transmission on sensitive flooring. Special care needs to be discussed when considering this barrier for successful installation.</p>',
             crumbs=hz, schema=svc("services/horizontal-services/under-slab/", "Under-slab waterproofing")),
        page(None, "services/above-grade/", "Above grade", "Above-Grade Weather Barriers in West Jordan", "EnviroDri: a liquid-applied weather-resistive and air barrier for new homes.", "07 25 00 &middot; Weather barriers",
             "Above-Grade Weather Barrier in West Jordan | Rocky Mountain", "Above-grade services in West Jordan: EnviroDri, a seamless, vapor-permeable liquid weather-resistive and air barrier that lowers air changes per hour.",
             image="she-built-sign", alt="New home framing above a waterproofed foundation",
             intro="Above grade, Rocky Mountain Waterproofing applies EnviroDri in West Jordan and across Utah: a liquid weather-resistive barrier and air barrier for new residential construction. It is vapor permeable and fluid applied, and it helps new homes meet energy goals by lowering ACH (air changes per hour).",
             content=f'<ul><li>A liquid-applied, seamless application</li><li>Fully adhered, so it will not delaminate over time</li><li>Vapor permeable: lets the wall cavity dry and keeps bulk water out</li><li>Code approved under any cladding system</li></ul><p><a class="tlink" href="@/services/above-grade/envirodri/">More about EnviroDri {ARROW}</a></p>',
             crumbs=sv, schema=svc("services/above-grade/", "Above-grade weather barrier")),
        page("services_above_grade_envirodri", "services/above-grade/envirodri/", "EnviroDri", "EnviroDri Weather-Resistant Barrier in West Jordan", "Seamless, self-healing, vapor permeable, and code approved under any cladding.", "07 27 00 &middot; Air barriers",
             "EnviroDri Weather Barrier in West Jordan | Rocky Mountain", "EnviroDri in West Jordan: a liquid-applied, self-healing, vapor-permeable weather-resistive and air barrier that seals every sheathing seam and joint.",
             intro="Rocky Mountain Waterproofing applies EnviroDri on new homes in West Jordan. EnviroDri is a liquid weather-resistive barrier and air barrier: vapor permeable, fluid applied, and made to help meet new energy goals by lowering ACH (air changes per hour).",
             skip=("EnviroDri - Weather-Resistant Barrier", "Amazing Protection"), drop=re.compile(DROP.pattern + r"|^Can withstand", re.I), crumbs=ag, schema=svc("services/above-grade/envirodri/", "EnviroDri weather-resistive barrier")),
        page(None, "services/other-services/", "Other services", "Other Services: Termite Pre-Treatment &amp; Window Wells", "Two services we used to offer, and where to go now.", "Other services",
             "Other Services: Termite &amp; Window Wells | Rocky Mountain", "Rocky Mountain Waterproofing no longer offers termite pre-treatment or window well installs. Here is what changed and how to choose a termite control company.",
             intro="Rocky Mountain Waterproofing used to offer termite pre-treatment and window well installs alongside our waterproofing work in West Jordan. We no longer provide either service, so we can focus on waterproofing and leak repair.",
             content=f'<ul class="plain"><li><a href="@/services/other-services/termite/">Termite pre-treatment</a>: no longer offered. Tips from the Utah Department of Agriculture and Food on choosing a termite control company.</li><li><a href="@/services/other-services/window-wells/">Window well install</a>: no longer offered. Questions? Contact Chris Douglas.</li></ul>',
             crumbs=sv),
        page("services_other_services_termite", "services/other-services/termite/", "Termite pre-treatment", "Termite Pre-Treatment (No Longer Offered)", "How to choose a termite control company, from the Utah Department of Agriculture and Food.", "31 31 16 &middot; Termite control",
             "Termite Pre-Treatment in Utah | Rocky Mountain Waterproofing", "Rocky Mountain Waterproofing no longer offers termite pre-treatment. Utah Department of Agriculture tips for choosing a termite control company in Utah.",
             intro="Rocky Mountain Waterproofing provided a termite pre-treatment service in West Jordan that met the requirements for FHA or VA loans. We no longer provide this service. Not all termite control companies are alike, so here are tips from the Utah Department of Agriculture and Food.",
             drop=re.compile(DROP.pattern + r"|We Provided a Termite|There are some companies|Rocky Mountain Waterproofing has been in business since 1960|We are happy to look at plans|All our Applicators|Here are some tips", re.I),
             skip=("Termite Pre-Treatment",), crumbs=ot),
        page("services_other_services_window_wells", "services/other-services/window-wells/", "Window well install", "Window Well Install (No Longer Offered)", "We&rsquo;ve discontinued window well installs.", "Other services",
             "Window Well Install: No Longer Offered | Rocky Mountain", "Rocky Mountain Waterproofing no longer installs window wells because of demand for other services. For questions, contact Chris Douglas at 801-282-2100.",
             image="window-well-fasten", alt="Crew fastening a window well against a waterproofed foundation",
             intro="Due to extreme demand for our other services in West Jordan and across Utah, Rocky Mountain Waterproofing has discontinued window well installation. For any questions, please contact Chris Douglas at 801-282-2100.",
             content=f'<p>We still waterproof the foundation behind the window well, and we fix the cracks that often start under basement windows.</p><p><a class="tlink" href="@/services/leak-repair/foundation-cracks/">Foundation cracks {ARROW}</a></p>',
             crumbs=ot),
        page(None, "services/leak-repair/", "Leak repair", "Foundation Leak Repair in West Jordan", "Active leaks fixed, inside or out: cracks, ties, honeycomb, cold joints, floor joints and pipes.", "03 01 00 &middot; Concrete repair",
             "Basement Leak Repair in West Jordan | Rocky Mountain", "Foundation and basement leak repair in West Jordan: active leaks fixed inside or out at cracks, form ties, cold joints, honeycomb, floor joints and pipes.",
             image="honeycomb-wall", alt="Honeycomb (rock pocket) in a concrete foundation wall",
             intro="Rocky Mountain Waterproofing does foundation leak repair in West Jordan and across Utah. We can fix them, even active leaks, inside or out: cracks, ties, honeycomb, cold joints, floor joints and pipe penetrations.",
             before=f'<figure class="sheet">{leak_elevation("lr")}</figure>{key_list(LEAKS)}', content=leak, crumbs=sv, schema=svc("services/leak-repair/", "Foundation leak repair")),
        page(None, "services/leak-repair/leak-prevention/", "Leak prevention", "Basement Leak Prevention in West Jordan", "The most common leaks we see, and what stops them.", "03 01 00 &middot; Leak prevention",
             "Basement Leak Prevention in West Jordan | Rocky Mountain", "Basement leak prevention in West Jordan: cracks under windows, honeycomb, form ties, floor joints, pipe penetrations, improper flashing and structural cracks.",
             intro="Rocky Mountain Waterproofing helps homeowners and builders in West Jordan prevent basement leaks. Many homes leak; here are the most common leaks we have identified over the years, to help you diagnose what is happening with your project and how to get it back on track.",
             content=re.sub(r"(?s)^.*?</ul>", "", prev, count=1) + "<h2>Outside the house</h2>" + "".join(f"<h3>{h}</h3>" + section_of(leak, h) for h in ("Sprinklers", "Gutters and Downspouts", "Landscaping")),
             crumbs=lr, schema=svc("services/leak-repair/leak-prevention/", "Basement leak prevention")),
        page("services_leak_repair_foundation_cracks", "services/leak-repair/foundation-cracks/", "Foundation cracks", "Foundation Crack Repair in West Jordan", "Every foundation cracks. Here&rsquo;s how to stop a crack from leaking, and how to find one.", "03 01 00 &middot; Foundation cracks",
             "Foundation Crack Repair in West Jordan | Rocky Mountain", "Foundation crack repair in West Jordan: why every foundation cracks, how waterproofing bridges cracks, signs a crack has leaked, and how to do a water test.",
             image="window-well-set", alt="Basement window opening in a waterproofed foundation, where cracks often start",
             intro="Rocky Mountain Waterproofing repairs leaking foundation cracks in West Jordan. Foundation cracks occur because the concrete shrinks as it cures and loses water, so every foundation will have cracks; the goal is to keep them from leaking.",
             skip=("Foundation Cracks",), crumbs=lr, schema=svc("services/leak-repair/foundation-cracks/", "Foundation crack repair")),
        page("services_leak_repair_cold_joints", "services/leak-repair/cold-joints/", "Cold joints", "Cold Joint Leak Repair in West Jordan", "Where one pour ends and the next begins: three ways to seal it.", "03 01 00 &middot; Cold joints",
             "Cold Joint Leak Repair in West Jordan | Rocky Mountain", "Cold joint leak repair in West Jordan: waterstop before the pour, an exterior waterproofing detail before backfill, or interior injection before finishing.",
             intro="Rocky Mountain Waterproofing seals cold joints in West Jordan. A cold joint forms when one pour of concrete ends and another begins, a formed crack where water can enter if it is not treated correctly. Cold joints are the second most common leak source we find in our area.",
             skip=("Cold Joints",), crumbs=lr, schema=svc("services/leak-repair/cold-joints/", "Cold joint leak repair")),
        page("services_leak_repair_honeycomb", "services/leak-repair/honeycomb/", "Honeycomb", "Honeycomb Leak Repair in West Jordan", "Rock pockets: where the cement paste didn&rsquo;t fill in.", "03 01 00 &middot; Honeycomb",
             "Honeycomb Leak Repair in West Jordan | Rocky Mountain", "Honeycomb leak repair in West Jordan: how rock pockets form, how to prevent them, and how we fill and coat them on new and existing foundations.",
             image="honeycomb-wall", alt="Honeycomb rock pocket with exposed aggregate in a foundation wall",
             intro="Rocky Mountain Waterproofing repairs honeycomb leaks in West Jordan. Honeycomb, or rock pockets, are areas in a foundation where the creamy part of the cement has not filled in, leaving exposed rock and aggregate where water can leak through.",
             skip=("Honeycomb Leak Repair",), crumbs=lr, schema=svc("services/leak-repair/honeycomb/", "Honeycomb leak repair")),
        page(None, "services/leak-repair/floor-joints/", "Floor joints", "Floor Joint Leak Repair in West Jordan", "Water at the joint between the wall and the floor.", "03 01 00 &middot; Floor joints",
             "Floor Joint Leak Repair in West Jordan | Rocky Mountain", "Floor joint leak repair in West Jordan: why water shows up where the basement wall meets the floor, from high water tables, and how it can be treated.",
             intro="Rocky Mountain Waterproofing treats floor joint leaks in West Jordan, where water shows up at the joint between the basement wall and the floor.",
             content=section_of(leak, "Floor Joints") + "<h2>Why the floor joint leaks</h2>" + section_of(prev, "Footing Joint Leak") + "<h2>Water table issues</h2>" + section_of(leak, "Water Table Issues"),
             crumbs=lr, schema=svc("services/leak-repair/floor-joints/", "Floor joint leak repair")),
        page(None, "services/leak-repair/pipe-penetrations/", "Pipe penetrations", "Pipe Penetration Leak Repair in West Jordan", "Where the water main comes through the foundation.", "03 01 00 &middot; Pipe penetrations",
             "Pipe Penetration Leak Repair in West Jordan | Rocky Mountain", "Pipe penetration leak repair in West Jordan: sealing where the water main and other pipes come through the foundation wall, before or after finishing.",
             intro="Rocky Mountain Waterproofing seals pipe penetration leaks in West Jordan, where a pipe such as the main water line comes through the foundation wall.",
             content=section_of(leak, "Pipe Penetrations") + "<h2>Why it matters</h2>" + section_of(prev, "Pipe Penetrations") + req_pipe,
             crumbs=lr, schema=svc("services/leak-repair/pipe-penetrations/", "Pipe penetration leak repair")),
        page(None, "services/leak-repair/ties/", "Foundation ties", "Foundation Tie Leak Repair in West Jordan", "The form ties left in every poured wall.", "03 01 00 &middot; Form ties",
             "Foundation Tie Leak Repair in West Jordan | Rocky Mountain", "Foundation tie leak repair in West Jordan: why form ties left in poured walls leak, and why they should be broken, patched and sealed before backfill.",
             image="tie-patch-closeup", alt="Broken and patched form ties on a coated foundation wall",
             intro="Rocky Mountain Waterproofing seals foundation tie leaks in West Jordan. When concrete is formed, ties hold the forms in place, and it is critical to have them removed and sealed before backfill.",
             content=section_of(prev, "Foundation Ties") + "<p>On new foundations our crews break and patch the ties, clean the footings and then waterproof.</p>",
             crumbs=lr, schema=svc("services/leak-repair/ties/", "Foundation tie leak repair")),
        page("services_leak_repair_icf_leaks", "services/leak-repair/icf-leaks/", "ICF foundation leaks", "ICF Foundation Leak Repair in West Jordan", "So many seams, and prone to honeycomb.", "03 01 00 &middot; ICF foundations",
             "ICF Foundation Leak Repair in West Jordan | Rocky Mountain", "ICF foundation leak repair in West Jordan: why insulated concrete forms leak, and options from exterior sealing to foam removal and urethane injection.",
             intro="Rocky Mountain Waterproofing repairs ICF foundation leaks in West Jordan. ICF foundations are very difficult to waterproof because they have so many seams to address, and they are very prone to honeycombing throughout the wall.",
             skip=("ICF Foundation Leaks", "Please contact us for more information on the avalable options."), crumbs=lr, schema=svc("services/leak-repair/icf-leaks/", "ICF foundation leak repair")),
    ]
    about_txt = mig("about", skip=("History of Rocky Mountain Waterproofing", "Christopher Douglas", "Tyler Douglas", "Sam Douglas"))
    team = '<div class="team-row">' + "".join(f'<figure>{img(i, n)}<figcaption>{n}</figcaption></figure>' for i, n in [("chris-douglas", "Christopher Douglas"), ("tyler-douglas", "Tyler Douglas"), ("sam-douglas", "Sam Douglas")]) + "</div>"
    out += [
        page(None, "about/", "About", "About Rocky Mountain Waterproofing", "A family business in West Jordan since 1960.", "About &middot; Who we are",
             "About Rocky Mountain Waterproofing | West Jordan, Since 1960", "Rocky Mountain Waterproofing is a family-owned waterproofing company in West Jordan, Utah, founded in 1960 as Modern Damp Proofing, owned by the Douglas family.",
             image="libby-sarah-site", alt="Two Rocky Mountain Waterproofing crew members in hi-vis jackets on a job site",
             intro="Rocky Mountain Waterproofing is a family business in West Jordan, Utah, that has grown over the years. We started in 1960 as Modern Damp Proofing and today the company is owned by four of McKay and Ellen Douglas&rsquo;s children: Chris, Jenn, Tyler and Sam.",
             content=section_of(about_txt, "A Family Business") + "<h2>Our mission and values</h2>" + section_of(about_txt, "Our Mission and Values") + "<h2>Our divisions</h2>" + section_of(about_txt, "Rocky Mountain Waterproofing Divisions") +
             "<h2>Our team</h2>" + team + f'<p><a class="tlink" href="@/about/rmwp-history/">Our history {ARROW}</a> &nbsp; <a class="tlink" href="@/about/trade-memberships/">Trade memberships {ARROW}</a></p>'),
        page(None, "about/rmwp-history/", "History", "History of Rocky Mountain Waterproofing", "From Modern Damp Proofing in 1960 to Rocky Mountain Waterproofing today.", "About &middot; Since 1960",
             "History of Rocky Mountain Waterproofing | Since 1960, Utah", "The history of Rocky Mountain Waterproofing: founded in 1960 as Modern Damp Proofing, renamed in 1996, and run by the Douglas family in West Jordan, Utah.",
             intro="Modern Damp Proofing, Inc., DBA Rocky Mountain Waterproofing, has been around since 1960 and is still going strong. We started as a company doing solely damp proofing, with Larry R. as president.",
             content=f'''<ol class="timeline on-light"><li><b>1960</b><span>Modern Damp Proofing starts out doing damp proofing only, with Larry R. as president.</span></li>
<li><b>Then</b><span>The company passes to Cecil Douglas, who runs it for a few years and then sells it to his brother, McKay Douglas.</span></li>
<li><b>Later</b><span>McKay passes the role of president to his son Justin, who helps the company grow, expand and use technology to be more efficient.</span></li>
<li><b>1996</b><span>The name is registered as Rocky Mountain Waterproofing, to match the move from damp proofing to waterproofing.</span></li>
<li><b>Today</b><span>Justin passes the torch to his siblings. The company is owned by Chris, Jenn, Tyler and Sam.</span></li></ol>''' +
             "<h2>What&rsquo;s in a name</h2>" + section_of(about_txt, "What's In A Name") + "<h2>A family business</h2>" + section_of(about_txt, "A Family Business"), crumbs=ab),
        page("about_serving_you", "about/serving-you/", "Serving you", "Serving Architects, Builders &amp; Homeowners", "Our basic &ldquo;ABC&rdquo;s: see if any of them fit what you&rsquo;re looking for.", "About &middot; Serving you",
             "Serving Architects, Builders &amp; Homeowners | Rocky Mountain", "How Rocky Mountain Waterproofing serves architects (value engineering), builders (1&ndash;2 day lead times) and homeowners (budgets and value) from West Jordan.",
             intro="Sure, we offer a lot of products and services from our West Jordan yard, but our real focus is providing the benefits that matter to you. Here are a few of our basic &ldquo;ABC&rdquo;s.",
             skip=("Serving You",), drop=re.compile(DROP.pattern + r"|Sure, we offer", re.I), crumbs=ab),
        page(None, "about/social/", "Social", "Follow Rocky Mountain Waterproofing", "Our social media channels.", "About &middot; Social",
             "Social: Follow Rocky Mountain Waterproofing | West Jordan, Utah", "Follow Rocky Mountain Waterproofing on Facebook, Instagram, LinkedIn, YouTube, Twitter and Houzz. We are working to be active in the community and socially.",
             intro="Follow us on social media! We are working to be active in the community and socially, and we would love to hear from you.",
             content='<ul class="plain">' + "".join(f'<li><a href="{S[k]}" rel="noopener">{n}</a></li>' for k, n in [("fb", "Facebook"), ("ig", "Instagram"), ("li", "LinkedIn"), ("yt", "YouTube"), ("tw", "Twitter"), ("houzz", "Houzz reviews"), ("glassdoor", "Glassdoor"), ("chamber", "West Jordan Chamber of Commerce listing")]) + "</ul>", crumbs=ab),
        page("about_privacy", "about/privacy/", "Privacy policy", "Privacy Policy", None, "Legal", "Privacy Policy | Rocky Mountain Waterproofing, West Jordan",
             "The Rocky Mountain Waterproofing privacy policy: we use cookies to help provide a better experience on our site, we value your privacy and never sell your data.",
             skip=("Privacy Policy",), drop=NOTHING, crumbs=ab),
        page(None, "about/jobs/", "Jobs", "Join the Rocky Mountain Waterproofing Team", "Do you have what it takes to be part of our team?", "About &middot; Jobs",
             "Jobs at Rocky Mountain Waterproofing | West Jordan, Utah", "Jobs at Rocky Mountain Waterproofing in West Jordan, Utah: apply for construction labor and waterproofing crew positions. Paid training, no experience required.",
             image="libby-shop", alt="Rocky Mountain Waterproofing team member in the shop",
             intro="Fill out the application if you are interested in a position with Rocky Mountain Waterproofing. Our crews report to our location in West Jordan each workday.",
             content=f'<h2>Open positions</h2><ul class="plain"><li><a href="@/jobs/construction-labor/">Construction Labor (full time or part time)</a>: waterproofing experience not required; we train new crew members.</li></ul>',
             form=form_job(), crumbs=ab),
        page(None, "about/trade-memberships/", "Trade memberships", "Trade Memberships", "The associations Rocky Mountain Waterproofing belongs to.", "About &middot; Memberships",
             "Trade Memberships | Rocky Mountain Waterproofing, West Jordan", "Rocky Mountain Waterproofing is a member of the Salt Lake, Utah Valley, Northern Wasatch and Park City home builders associations and the West Jordan Chamber.",
             intro="Rocky Mountain Waterproofing is a member of these trade groups and business associations in Utah.",
             content='<ul class="members"><li>Salt Lake Home Builders Association</li><li>Utah Valley Home Builders Association</li><li>Northern Wasatch Home Builders Association</li><li>Park City Area Home Builders Association</li><li>West Jordan Chamber of Commerce</li><li>Utah Safety Council</li><li>NFIB (National Federation of Independent Business)</li></ul>' +
             f'<p>Chris Douglas serves on the Salt Lake HBA Membership Committee. <a href="@/blog/item/19-salt-lake-home-builders-association-member-spotlight-rocky-mountain-waterproofing/">Read the member spotlight</a>.</p>', crumbs=ab),
        page(None, "contact/", "Contact", "Contact Rocky Mountain Waterproofing", "Office, phone, fax and hours in West Jordan.", "Contact",
             "Contact Rocky Mountain Waterproofing | West Jordan, Utah", "Contact Rocky Mountain Waterproofing: 8401 S 4300 W, West Jordan, UT 84088. Office 801-282-2100, toll free (877) 282-2100. Open Mon to Fri, 7 AM to 4 PM.",
             intro=f"To schedule a job, please call our office at {S['phone']}. For general questions, use the form. Please don&rsquo;t send sensitive data through the form.",
             content=f'''<dl class="info"><div><dt>Office</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div><div><dt>Toll free</dt><dd><a href="tel:{S["tel_toll"]}">{S["toll"]}</a></dd></div><div><dt>Fax</dt><dd>{S["fax"]}</dd></div>
<div><dt>Address</dt><dd>{S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}</dd></div><div><dt>Hours</dt><dd>{S["hours"]}</dd></div></dl>
<p><a href="https://www.google.com/maps/place/Rocky+Mountain+Waterproofing/@40.598964,-111.995247,17z" rel="noopener">Open in Google Maps</a></p>
<h2>Other ways to reach us</h2><ul class="plain"><li><a href="@/{BID}">Request a bid</a> (plans and spec uploads)</li><li><a href="@/{LEAKREQ}">Leak repair request</a> (with photos)</li><li><a href="@/contact/accounts/">Accounts</a> (billing questions)</li><li><a href="@/contact/newsletter/">Newsletter</a></li><li><a href="@/about/jobs/">Job application</a></li></ul>''',
             form=form_contact()),
        page("contact_accounts", "contact/accounts/", "Accounts", "Accounts &amp; Billing", "Payment options and Net 30 terms.", "Contact &middot; Accounts",
             "Accounts &amp; Billing | Rocky Mountain Waterproofing", "Rocky Mountain Waterproofing accounts: we accept cash, check and Visa, Mastercard and Discover. Most work is Net 30. Call Sam at 801-282-2100, option 5.",
             skip=("Accounts",), drop=re.compile(DROP.pattern + r"|Alternately you can contact", re.I), form=form_contact("Email accounts", accounts=True), crumbs=ct),
        page(None, "contact/newsletter/", "Newsletter", "Newsletter", "News and updates from Rocky Mountain Waterproofing.", "Contact &middot; Newsletter",
             "Newsletter | Rocky Mountain Waterproofing, West Jordan, Utah", "Subscribe to the Rocky Mountain Waterproofing newsletter for news and updates on foundation waterproofing, leak repair and our projects in West Jordan and Utah.",
             intro="Sign up for news and updates from Rocky Mountain Waterproofing in West Jordan.", content="", form=form_news(), crumbs=ct),
        page(None, BID, "Get an estimate", "Request a Waterproofing Bid", "Send plans, spec info or site pictures, and we&rsquo;ll get back to you with a bid.", "Estimate &middot; Bid request",
             "Request a Waterproofing Bid | Rocky Mountain Waterproofing", "Request a waterproofing bid from Rocky Mountain Waterproofing in West Jordan. Upload plans, spec info or site pictures, or share a Dropbox or Google Drive link.",
             intro="Tell us about the project and attach plans, spec info or site pictures (or share a Dropbox or Google Drive link). We&rsquo;ll get back to you as quickly as possible. To schedule a job, call the office at 801-282-2100.",
             content='<h2>What helps us bid</h2><ul><li>Plans or the spec section</li><li>The site address</li><li>Depth of the foundation and how the space will be used (crawlspace, basement, finished space)</li><li>Any known water table or soil conditions (a geotechnical report helps)</li></ul>', form=form_bid()),
        page("contact_leak_repair_request", "contact/leak-repair-request/", "Leak repair request", "Leak Repair Request", "Tell us about the leak and include pictures of the leaking areas.", "Contact &middot; Leak repair",
             "Basement Leak Repair Request | Rocky Mountain Waterproofing", "Request basement or foundation leak repair from Rocky Mountain Waterproofing in West Jordan: cracks, ties, floor joints, pipe penetrations, honeycomb and more.",
             drop=re.compile(DROP.pattern + r"|^Leak Repair Request Form$", re.I), form=form_leak(), crumbs=ct),
        page("jobs_construction_labor", "jobs/construction-labor/", "Construction labor", "Construction Labor (Full Time or Part Time)", "Waterproofing experience not required. We train new crew members.", "Jobs &middot; Construction labor",
             "Construction Labor Job in West Jordan | Rocky Mountain", "Construction labor job at Rocky Mountain Waterproofing in West Jordan: full or part time, paid training, medical premiums paid, PTO and IRA match.",
             image="crew-in-trench", alt="Crew member working in a foundation trench",
             content=re.sub(r"(?s)<ul><li>OSHA 10</li>.*?<h3>Raise Amount</h3>\s*<ul>.*?</ul>", "", mig("jobs_construction_labor")) + training_table() + f'<p><a class="btn" href="@/about/jobs/">Apply now {ARROW}</a></p>',
             crumbs=[("Jobs", "about/jobs/")]),
    ]
    return out


def training_table():
    names = ["OSHA 10", "Confined Space", "Fall Protection", "CPR/First Aid", "Defensive Driving", "Boom Lift / Scissor Lift", "Forklift", "Below Grade Waterproofing - Checklist", "Specialty Waterproofing - Checklist", "Technical Waterproofing - Checklist", "Leadership - Checklist", "Lead Applicator", "OSHA 30"]
    course = ["10 Hours", "4 Hours", "4 Hours", "4 Hours (3 Online)", "4 Hours", "In Person Training", "In Person Training", "NA", "NA", "NA", "NA", "NA", "$1000 Bonus (Paid Over Time)"]
    time = ["10 Hours (Anytime)", "3-4 Hours (Anytime)", "3-4 Hours (Anytime)", "3 Hrs (Online) / 1 Hr (In Person)", "4 Hours (Anytime)", "3-4 Hours (In Person)", "3-4 Hours (In Person)", "1-2 Months", "1-2 Months", "1-2 Months", "6 Months", "4-9 Months", "30+ Hours (Anytime)"]
    raise_ = ["$0.50", "$0.25", "$0.25", "$0.25", "$0.25", "$0.25", "$0.25", "$0.50", "$0.50", "$0.50", "$0.50", "$1.00", "$1.00"]
    return ('<h3>Training and raises</h3><div class="tbl-wrap"><table class="spec"><thead><tr><th scope="col">Training</th><th scope="col">Course</th><th scope="col">Typical complete time</th><th scope="col">Raise</th></tr></thead><tbody>' +
            "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in zip(names, course, time, raise_)) + "</tbody></table></div>")


def _f(id_, label, typ="text", req=False, extra=""):
    return f'<label for="{id_}">{label}{" *" if req else ""}<input id="{id_}" name="{id_[2:]}" type="{typ}"{" required" if req else ""}{extra}></label>'


def form_contact(title="Contact form", accounts=False):
    return f'''<form class="form" method="post" action=""><h3>{title}</h3>
<div class="row">{_f("f-name", "Name", req=True, extra=' autocomplete="name"')}{_f("f-email", "Email", "email", True, ' autocomplete="email"')}</div>
<div class="row">{_f("f-phone", "Phone (optional)", "tel", extra=' autocomplete="tel"')}{_f("f-company", "Company") if accounts else _f("f-web", "Website", "url")}</div>
<label for="f-msg">Message *<textarea id="f-msg" name="message" required></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''


def form_news():
    return f'''<form class="form" method="post" action=""><h3>Subscribe</h3>{_f("f-name", "Name", extra=' autocomplete="name"')}{_f("f-email", "Email", "email", True, ' autocomplete="email"')}
<label class="check"><input type="checkbox" name="subscribe" checked> Subscribe to our newsletter</label><button class="btn" type="submit">Subscribe {ARROW}</button></form>'''


def form_bid():
    return f'''<form class="form" method="post" action="" enctype="multipart/form-data"><h3>Bid request</h3>
<div class="row">{_f("f-name", "Name", req=True, extra=' autocomplete="name"')}{_f("f-email", "Email", "email", True, ' autocomplete="email"')}</div>
<div class="row">{_f("f-company", "Company", extra=' autocomplete="organization"')}{_f("f-phone", "Phone", "tel", extra=' autocomplete="tel"')}</div>
{_f("f-site", "Site address")}{_f("f-link", "Link (Dropbox, Google Drive, spec info, etc.)", "url")}
<label for="f-msg">Comments<textarea id="f-msg" name="comments"></textarea></label>
<label for="f-file">File upload (plans, spec info, site pictures, etc.)<input id="f-file" name="file" type="file" multiple></label>
<button class="btn" type="submit">Send bid request {ARROW}</button></form>'''


LEAK_TYPES = ["Foundation Crack Leak (Wall)", "Foundation Crack Leak (Ceiling)", "Concrete Deck Leak", "Foundation Tie Leak", "Floor Joint Leak", "Pipe Penetration Leak", "Honeycomb Leak", "Suspended Slab Leak",
              "Water Table Issues", "Dug-up Repair", "Caulking", "ICF Foundation Leak", "Block Foundation Leak", "Retaining Wall Leak", "Others"]


def form_leak():
    return f'''<form class="form" method="post" action="" enctype="multipart/form-data"><h3>Leak repair request</h3>
<div class="row">{_f("f-name", "Name", req=True, extra=' autocomplete="name"')}{_f("f-email", "Email", "email", True, ' autocomplete="email"')}</div>
<div class="row">{_f("f-phone", "Phone", "tel", extra=' autocomplete="tel"')}{_f("f-company", "Company (optional)")}</div>
<div class="row">{_f("f-when", "Best time to contact you")}<label for="f-how">Best way to contact you<select id="f-how" name="contact_by"><option>Phone</option><option>Email</option><option>Text</option></select></label></div>
<fieldset><legend>Types of leaks (check all that apply)</legend><div class="checks">{"".join(f'<label class="check"><input type="checkbox" name="leak_type" value="{t}"> {t}</label>' for t in LEAK_TYPES)}</div></fieldset>
{_f("f-addr", "Address", extra=' autocomplete="street-address"')}{_f("f-subj", "Message subject", req=True)}
<label for="f-msg">Message *<textarea id="f-msg" name="message" required></textarea></label>
{_f("f-link", "Image folder link (optional)", "url")}
<label for="f-file">Pictures of the leaks<input id="f-file" name="file" type="file" accept="image/*" multiple></label>
<button class="btn" type="submit">Send request {ARROW}</button></form>'''


def form_job():
    return f'''<form class="form" method="post" action=""><h3>Job application</h3>
<div class="row">{_f("f-name", "Name", req=True, extra=' autocomplete="name"')}{_f("f-email", "Email", "email", True, ' autocomplete="email"')}</div>
<div class="row">{_f("f-phone", "Main phone", "tel", True, ' autocomplete="tel"')}{_f("f-phone2", "Alternate phone", "tel")}</div>
<div class="row">{_f("f-start", "Available to start", "date")}{_f("f-pos", "Position you are applying for", extra=' value="Construction Labor"')}</div>
<label for="f-type">Type of employment<select id="f-type" name="employment_type"><option>Full time</option><option>Part time</option></select></label>
{_f("f-addr", "Address", extra=' autocomplete="street-address"')}
<label for="f-hist">Employment history (previous employers, dates, duties)<textarea id="f-hist" name="history"></textarea></label>
<label for="f-skills">Skills, qualifications and certifications<textarea id="f-skills" name="skills"></textarea></label>
<button class="btn" type="submit">Send application {ARROW}</button></form>'''


def make_pages():
    p_blog.setup(phero, cta, side, ARROW, HOME, BID, tidy, mig)
    out = [home()] + pages_main() + p_blog.pages() + [notfound()]
    return [_fit(dict(x, body=Q(x["body"]))) for x in out]


def _fit(pg):
    for add in (" Call 801-282-2100.", " Since 1960."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", "Try our services, leak repair, or call the office.", "404") + f'<section class="sec"><div class="wrap"><p><a class="tlink" href="@/services/">Services {ARROW}</a> &nbsp; <a class="tlink" href="@/services/leak-repair/">Leak repair {ARROW}</a></p></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Rocky Mountain Waterproofing", "meta": "This page was not found. See Rocky Mountain Waterproofing services and leak repair, or call 801-282-2100 for basement waterproofing in West Jordan, Utah.",
            "body": body, "robots": "noindex, follow", "sitemap": False}
