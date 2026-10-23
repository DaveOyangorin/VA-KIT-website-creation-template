"""Pages for the prestigetreeandlandscape.com redesign: "Growth rings".

Prestige's story is time: a father who started the business in 1978, a son who became Utah's youngest certified arborist at 21, 12,500
trees planted, Arbor Day honours, winters climbing in Kauai. The live home page is blank; everything else has real copy. So the home page
opens on a credited fall photo of Big Cottonwood Canyon, and the signature is a cut trunk: one growth ring per year since 1978. Tap a
highlighted ring and it tells that year's story, in their own words. The arborist's own photos (crane removals, rigging, climbing) fill a
"from the climber's camera" strip. Heartwood, sapwood and bark green with a medal-gold accent; Fraunces, Outfit, Spline Sans Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same .php URLs (the live build writes real .php files); backup files kept noindex. One new post."""
import html, json, math, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer
cta = K.cta


def blocks(key):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8", errors="ignore").read()
    s = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", s)
    out, started = [], False
    for t, x in re.findall(r"(?s)<(h1|h2|h3|h4|h5|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).replace(" ,", ",").replace(" .", ".").strip()
        if not x: continue
        if t == "h1": started = True; continue
        if not started: continue
        if x in ("Call Us Today", "Your message has been sent!", "Your message could not be sent!", "Submit Form", "Address", "Message"): continue
        out.append((t, x))
    return out


def render(b):
    res, ul = [], []
    def flush():
        if ul: res.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in b:
        if t == "li": ul.append(x); continue
        flush()
        res.append(f"<p>{html.escape(x)}</p>" if t == "p" else f"<h2>{html.escape(x[:1] + x[1:].lower() if x.isupper() else x)}</h2>")
    flush()
    return "\n".join(res)


def first_p(key):
    for t, x in blocks(key):
        if t == "p" and len(x) > 60: return x
    return ""


def meta_from(key, lead=""):
    m = re.sub(r"\s+", " ", (lead + " " + first_p(key)).strip())
    if len(m) > 158: m = m[:155].rsplit(" ", 1)[0].rstrip(",;:") + "&hellip;"
    return html.escape(html.unescape(m)).replace("&amp;hellip;", "&hellip;")


# page key -> (label, h1, title, image)
SERV = {
    "tree_pruning_php": ("Tree pruning &amp; trimming", "Tree Pruning and Trimming from a Certified Arborist", "Tree Pruning &amp; Trimming, Murray &amp; Salt Lake | Prestige", "pt-climber"),
    "stump_and_tree_removal_php": ("Stump &amp; tree removal", "Stump and Tree Removal", "Tree &amp; Stump Removal, Murray &amp; Salt Lake | Prestige Tree", "pt-crane"),
    "emergency_tree_removal_php": ("Emergency tree removal", "Emergency Tree Removal", "Emergency Tree Removal, Salt Lake Valley | Prestige", "pt-crane2"),
    "tree_cabling_and_bracing_php": ("Cabling &amp; bracing", "Tree Cabling and Bracing", "Tree Cabling &amp; Bracing by a Certified Arborist | Prestige", "pt-rigging"),
    "tree_health_php": ("Tree health", "Tree Health Care", "Tree Health Care &amp; Diagnosis, Salt Lake | Prestige", "pt-tall"),
    "tree_planting_php": ("Tree planting", "Tree Planting", "Tree Planting by a Certified Arborist, Utah | Prestige Tree", "pt-trail"),
    "lightning_protection_php": ("Lightning protection", "Lightning Protection for Trees", "Lightning Protection for Trees in Utah | Prestige Tree", "pt-gear"),
    "land_clearing_php": ("Land clearing", "Land Clearing", "Land &amp; Lot Clearing, Salt Lake Valley | Prestige Tree", "pt-crane"),
    "tree_service_php": ("Tree service", "Tree Service", "Tree Service in Murray, Utah | Prestige Tree And Landscape", "pt-climber"),
    "tree_services_php": ("Tree services", "Tree Services", "Tree Services from a Certified Arborist | Prestige Tree", "pt-helmet"),
    "landscaping_php": ("Landscaping", "Landscaping", "Landscaping in Murray &amp; the Salt Lake Valley | Prestige", None),
    "hardscaping_php": ("Hardscaping", "Hardscaping", "Hardscaping, Walls &amp; Patios, Salt Lake Valley | Prestige", None),
    "fertilization_php": ("Fertilization", "Fertilization", "Tree &amp; Lawn Fertilization in Utah | Prestige Tree", None),
    "irrigation_php": ("Irrigation", "Irrigation", "Irrigation &amp; Sprinkler Systems, Salt Lake Valley | Prestige", None),
    "landscape_design_php": ("Landscape design", "Landscape Design", "Landscape Design in Murray &amp; Salt Lake | Prestige Tree", None),
    "garden_design_php": ("Garden design", "Garden Design", "Garden Design in the Salt Lake Valley | Prestige Tree", None),
    "pest_management_php": ("Pest management", "Pest Management for Trees and Plants", "Tree &amp; Plant Pest Management, Utah | Prestige Tree", "pt-tall"),
    "disease_control_php": ("Disease control", "Tree and Plant Disease Control", "Tree &amp; Plant Disease Control, Salt Lake | Prestige Tree", "pt-tall"),
    "arborist_draper_php": ("Draper arborist", "Certified Arborist in Draper", "Certified Arborist in Draper, Utah | Prestige Tree", "pt-climber"),
    "tree_services_draper_php": ("Draper tree services", "Tree Services in Draper", "Tree Services in Draper, Utah | Prestige Tree And Landscape", "pt-helmet"),
    "tree_removal_services_draper_php": ("Draper tree removal", "Tree Removal Services in Draper", "Tree Removal Services in Draper, UT | Prestige Tree", "pt-crane"),
    "tree_removal_services_holladay_php": ("Holladay tree removal", "Tree Removal Services in Holladay", "Tree Removal Services in Holladay, UT | Prestige Tree", "pt-crane2"),
    "tree_trimming_draper_php": ("Draper tree trimming", "Tree Trimming in Draper", "Tree Trimming in Draper, Utah | Prestige Tree And Landscape", "pt-climber"),
    "tree_trimming_holladay_php": ("Holladay tree trimming", "Tree Trimming in Holladay", "Tree Trimming in Holladay, Utah | Prestige Tree", "pt-rigging"),
    "certified_arborist_php": ("Holladay arborist", "Certified Holladay Arborist", "Certified Arborist in Holladay, Utah | Prestige Tree", "pt-helmet"),
    "service_areas_php": ("Service areas", "Service Areas", "Service Areas: Murray, Holladay, Draper | Prestige Tree", None),
}
path_of = lambda k: k[:-4].replace("_", "-") + ".php/"

RINGS = [(1978, "Where it started", "&ldquo;My father started this business in 1978, and I am carrying on his tradition of care, respect, and reliability.&rdquo;"),
         (1997, "Youngest certified arborist in Utah", "Certified at age 21, the youngest certified arborist in the state of Utah at the time (the site gives both 1996 and 1997)."),
         (2009, "Winters in Kauai", "Winter arborist for Kauai Tree, Inc. in Hawaii, from 2009 to the present."),
         (2016, "Kalihiwai Ridge, Kauai", "Worked on the Kalihiwai Ridge project on Kauai, 2016&ndash;2017."),
         (2026, "48 years of growth rings", "Over 12,500 trees personally planted, Arbor Day honours, 20 years on the Utah Community Forest Council and city arborist for Daybreak.")]


def rings_svg():
    first, last = 1978, 2026
    n = last - first
    circles = []
    for i, y in enumerate(range(first, last + 1)):
        r = 14 + i * (176 / n)
        hi = any(y == ry for ry, t, d in RINGS)
        if hi:
            k = [ry for ry, t, d in RINGS].index(y)
            circles.append(f'<circle class="rg rg-hi" cx="200" cy="200" r="{r:.1f}" data-ring="{k}" tabindex="0" role="button" aria-label="{y}: {html.escape(html.unescape(RINGS[k][1]))}"/>')
        else:
            circles.append(f'<circle class="rg" cx="200" cy="200" r="{r:.1f}"/>')
    cracks = '<path class="crack" d="M200 200 L330 120 M200 200 L262 344"/>'
    labels = "".join(f'<text class="ry" x="{200 + (14 + (ry - first) * 176 / n) * math.cos(-0.6):.1f}" y="{200 + (14 + (ry - first) * 176 / n) * math.sin(-0.6) - 4:.1f}">{ry}</text>' for ry, t, d in RINGS)
    return f'<svg class="trunk" viewBox="0 0 400 400" aria-label="Growth rings from 1978 to 2026"><circle class="bark" cx="200" cy="200" r="196"/>{"".join(reversed(circles))}{cracks}</svg>'


def rings():
    panels = "".join(f'<div class="rp" data-rp="{i}"{"" if i == len(RINGS) - 1 else " hidden"}><span class="mono">{y}</span><h3>{t}</h3><p>{d}</p></div>' for i, (y, t, d) in enumerate(RINGS))
    btns = "".join(f'<button type="button" class="ry-b" data-go="{i}" aria-pressed="{"true" if i == len(RINGS) - 1 else "false"}">{y}</button>' for i, (y, t, d) in enumerate(RINGS))
    return f'<div class="rings" data-rings><div class="rings-l">{rings_svg()}<p class="hint">Tap a gold ring, or a year below.</p><div class="ry-row">{btns}</div></div><div class="rings-r" aria-live="polite">{panels}<a class="tlink" href="@/credentials-awards.php/">All credentials &amp; awards {ARROW}</a></div></div>'


TESTI = [("Exceptional", "Harold Mills"), ("These guys did a great job", "Glenn Kemp"), ("Very pleased with their services", "Creighton Rider")]
FAQ = [("Is Prestige Tree And Landscape family-owned?", "<p>Yes. The business was started in 1978 and is carried on by the founder&rsquo;s son, a certified arborist.</p>"),
       ("Why hire a certified arborist?", "<p>A certified arborist is trained in the art and science of tree care, from planting to insect and disease control to general care. When you hire one, you&rsquo;re hiring a professional who has spent years learning how trees grow and how to care for them.</p>"),
       ("What areas do you serve?", "<p>Murray, Holladay, Draper and nearby communities across the Salt Lake Valley.</p>"),
       ("What are your hours?", "<p>Monday to Friday 9AM to 6PM. Saturday and Sunday by appointment only.</p>")]
CORE = [("tree_pruning_php", "Pruning to shape and thin the canopy, remove deadwood and reduce hazards."), ("stump_and_tree_removal_php", "Safe, efficient tree and stump removal, including crane work."),
        ("tree_cabling_and_bracing_php", "Support for weak branches and split trunks."), ("tree_health_php", "Health evaluations and targeted treatments."),
        ("tree_planting_php", "The right tree in the right place, planted properly."), ("lightning_protection_php", "Protection systems for valuable trees.")]


def home():
    body = f'''
<section class="t-hero"><div class="th-img" data-parallax="0.08">{img("pt-hero", "Big Cottonwood Canyon in fall, with yellow and green trees below granite cliffs", priority=True)}</div>
<div class="wrap th-in"><div class="th-txt"><p class="label">Murray, Utah &middot; Family-owned since 1978</p>
<h1>Tree service in Murray, <em>from a certified arborist.</em></h1>
<p class="lede">Prestige Tree And Landscape is a family-owned tree service in Murray, Utah, started in 1978 and led today by a certified arborist. Pruning, removal, cabling, tree health and planting, plus landscaping and hardscaping, for homes and businesses across the Salt Lake Valley.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18018599786">{PHONE} Call 801.859.9786</a><a class="btn ghost" href="#rings">Read the rings {ARROW}</a></div></div></div>
<div class="th-strip"><div class="wrap"><span><b>1978</b> family business since</span><span><b>12,500+</b> trees personally planted</span><span><b>21</b> age certified, youngest in Utah</span><span><b>20 yrs</b> Utah Community Forest Council</span></div></div>
<p class="credit">Big Cottonwood Canyon &middot; GyozaDumpling, CC BY-SA 4.0, via Wikimedia Commons</p></section>

<section class="sec t-rings" id="rings"><div class="wrap">
<div class="t-head split-h reveal"><div><p class="label">Growth rings</p><h2>One ring <em>for every year.</em></h2></div><p class="lede">A tree keeps its history in its rings. So does this business: forty-eight of them since 1978. The gold ones mark the stories.</p></div>
{rings()}
</div></section>

<section class="sec t-serv"><div class="wrap">
<div class="t-head split-h reveal"><div><p class="label">Tree care</p><h2>Everything a tree <em>might need.</em></h2></div><a class="tlink" href="@/tree-services.php/">All tree services {ARROW}</a></div>
<div class="serv">{"".join(f'<a class="sv reveal" href="@/{path_of(k)}"><span class="mono">{i + 1:02d}</span><h3>{SERV[k][0]}</h3><p>{d}</p><em>{ARROW}</em></a>' for i, (k, d) in enumerate(CORE))}</div>
<p class="also">Also: <a href="@/landscaping.php/">landscaping</a>, <a href="@/hardscaping.php/">hardscaping</a>, <a href="@/irrigation.php/">irrigation</a>, <a href="@/fertilization.php/">fertilization</a>, <a href="@/landscape-design.php/">landscape</a> and <a href="@/garden-design.php/">garden design</a>, <a href="@/pest-management.php/">pest management</a>, <a href="@/disease-control.php/">disease control</a>, <a href="@/emergency-tree-removal.php/">emergency removal</a> and <a href="@/land-clearing.php/">land clearing</a>.</p>
</div></section>

<section class="sec t-cam"><div class="wrap">
<div class="t-head reveal"><p class="label">From the climber&rsquo;s camera</p><h2>Up in the canopy, <em>on the job.</em></h2></div>
<div class="cam">{"".join(f'<figure class="reveal">{img(n, a)}</figure>' for n, a in (("pt-crane", "A crane lifting a cut tree section during a removal"), ("pt-climber", "A climber roped into a large tree"), ("pt-rigging", "Rigging and pulleys set high in a tree"), ("pt-crane2", "A climber hanging from a crane line beside a tree"), ("pt-tall", "Tall trees in a neighborhood yard"), ("pt-gear", "Climbing carabiners and ropes clipped to a trunk")))}</div>
</div></section>

<section class="t-about"><div class="wrap t-about-in">
<figure class="reveal">{img("pt-trail", "The arborist standing among large trees on a forest trail")}</figure>
<div class="reveal"><p class="label">About Prestige</p><h2>From a two-person operation <em>to a full staff.</em></h2>
<p>Prestige Tree And Landscape was founded with one goal in mind: to provide a full range of superior landscaping services, including arborist, tree service and tree removal, at affordable rates. The company has grown from a two-person operation into a full staff of professionals.</p>
<p>We are a family-owned business with a long history of providing a valued service at a competitive price, while keeping a low impact on the environment, and we&rsquo;re involved in community outreach including Tree City USA.</p>
<div class="testi">{"".join(f"<blockquote><p>&ldquo;{q}&rdquo;</p><cite>{n}</cite></blockquote>" for q, n in TESTI)}</div>
<a class="tlink" href="@/about-us.php/">About us {ARROW}</a></div>
</div></section>

<section class="sec t-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Ask the <em>arborist.</em></h2>
<a class="post-card t-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>How deep, how wide, and why &ldquo;mulch volcanoes&rdquo; hurt trees, from the ISA and the USDA Forest Service.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Tree Service Murray, UT | Certified Arborist | Prestige Tree",
            "meta": "Prestige Tree And Landscape: family-owned tree service in Murray, UT since 1978, led by a certified arborist. Pruning, removal, cabling, planting, landscaping.",
            "body": body, "body_class": "is-home", "og": "pt-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    out.append(dict(home(), path="home.php/", canonical=U, robots="noindex, follow", sitemap=False))
    for k, (label, h1, title, im) in SERV.items():
        p = path_of(k)
        body = render(blocks(k))
        if im is None and k in ("landscaping_php", "hardscaping_php", "fertilization_php", "irrigation_php", "landscape_design_php", "garden_design_php", "service_areas_php"):
            body += '<p class="small photo-credit">Banner photo: Big Cottonwood Canyon &middot; GyozaDumpling, CC BY-SA 4.0, via Wikimedia Commons</p>'
        out.append(K.page(p, label, h1, "Prestige Tree And Landscape &middot; since 1978", "Murray, Utah", title, meta_from(k), body,
                          image=im or "pt-hero", alt=label.replace("&amp;", "and") + " by Prestige Tree And Landscape" if im else "Big Cottonwood Canyon in fall",
                          crumbs=[("Tree services", "tree-services.php/")] if im else None, canonical=canon(p), schema=[K.svc_schema(p, html.unescape(label), "Murray and the Salt Lake Valley, UT")]))
    ab = render(blocks("about_us_php")) + f'<div class="pgal">{img("pt-crane", "A crane removal")}{img("pt-climber", "Climbing a large tree")}{img("pt-trail", "Trees on a trail in Kauai")}</div>'
    out.append(K.page("about-us.php/", "About", "About Prestige Tree And Landscape", "Family-owned since 1978.", "About", "About Prestige Tree And Landscape | Family-Owned Since 1978",
                      "Prestige Tree And Landscape grew from a two-person operation into a full staff: family-owned since 1978, offering arborist, tree service and landscaping.",
                      ab, image="pt-helmet", alt="The arborist in a climbing helmet", canonical=canon("about-us.php/")))
    cr = '<p class="answer">Credentials and awards as listed by Prestige Tree And Landscape.</p>' + render([(t, x) for t, x in blocks("credentials_awards_php")])
    out.append(K.page("credentials-awards.php/", "Credentials", "Credentials and awards", "Certified Arborist &middot; Certified Tree Worker.", "Credentials", "Certified Arborist Credentials &amp; Awards | Prestige Tree",
                      "Certified Arborist and Certified Tree Worker: the youngest certified arborist in Utah at 21, over 12,500 trees planted and Arbor Day Foundation honours.",
                      cr, image="pt-rigging", alt="Climbing rigging", canonical=canon("credentials-awards.php/")))
    con = '''<p class="answer">Contact us today for a free consultation and see the difference experience makes.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18018599786">801.859.9786</a></dd></div><div><dt>Email</dt><dd><a href="mailto:service@prestigetreeandlandscape.com">service@prestigetreeandlandscape.com</a></dd></div>
<div><dt>Address</dt><dd><address>4780 S Commerce Dr<br>Murray, UT 84107</address></dd></div><div><dt>Hours</dt><dd>Mon&ndash;Fri 9AM&ndash;6PM<br>Sat&ndash;Sun by appointment only</dd></div></dl>'''
    out.append(K.page("contact-us.php/", "Contact", "Contact Prestige Tree And Landscape", "Free consultations.", "Contact", "Contact Prestige Tree And Landscape | Murray, Utah",
                      "Contact Prestige Tree And Landscape in Murray, Utah: call 801.859.9786 or email for a free consultation. Mon-Fri 9AM-6PM, weekends by appointment.",
                      con, canonical=canon("contact-us.php/"), form_side=True))
    sc = f'<div class="pgal">{"".join(img(n, a) for n, a in (("pt-crane", "Crane removal"), ("pt-crane2", "Crane work"), ("pt-climber", "Climbing"), ("pt-rigging", "Rigging"), ("pt-tall", "Tall trees"), ("pt-gear", "Climbing gear"), ("pt-helmet", "Arborist"), ("pt-trail", "Kauai trees")))}</div>'
    out.append(K.page("showcase.php/", "Showcase", "Our showcase", "From the climber&rsquo;s camera.", "Showcase", "Tree Work Showcase: Removals &amp; Climbing | Prestige Tree",
                      "Photos from Prestige Tree And Landscape&rsquo;s certified arborist: crane-assisted tree removals, rigging, climbing and tree care on the job in Utah and Kauai.",
                      sc, image="pt-crane", alt="Crane removal", canonical=canon("showcase.php/")))
    for p in ("header.php.bak.php/", "header.php.bak3.php/", "setts.php.bck.php/"):
        out.append(K.page(p, "Page", "Prestige Tree And Landscape", "", "Prestige", "Prestige Tree And Landscape | Tree Service in Murray, Utah",
                          "Prestige Tree And Landscape: family-owned tree service and landscaping in Murray, Utah since 1978. Call 801.859.9786 for a free consultation today.",
                          f'<p><a class="btn" href="@/">Home {ARROW}</a></p>', canonical=U, robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Tree services", "tree-services.php/"), ("Contact", "contact-us.php/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801.859.9786.", " Murray, Utah.")) for x in out]
