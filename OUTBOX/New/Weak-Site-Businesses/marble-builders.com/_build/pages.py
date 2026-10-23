"""Pages for the marble-builders.com redesign: "Veined".

Marble Builders does two kinds of work: design-led remodels, and the rebuild after water or fire damage, picking up where the restoration
company stops. Their blog explains that hand-off in detail, so the signature is "After the damage": a two-lane timeline of mitigation
(what the restoration company does, in Marble's own words) and the rebuild (what Marble does), step by step. The look is the name: honed
charcoal, Carrara white with CSS-drawn grey veining, brushed brass. Their photos were not archived, so the banner is a credited photo of
Lone Peak's granite above the south valley. Gloock, Inter Tight, IBM Plex Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same WordPress URLs (trailing slash); demo and unrecoverable pages kept noindex. One new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer
cta = K.cta
NAVS = {"Contact Us", "Home", "Services", "Locations Kansas City, Missouri", "Boise, Idaho", "Dallas, Texas", "Salt Lake City, Utah", "Denver, Colorado", "About Us", "Blog",
        "facebook pinterest linkedin instagram", "Menu", "Locations", "Portfolio", "Contact", "Get a Quote", "Learn More About Us", "read more read less"}
STOP = re.compile(r"^(Related Posts|Comments are closed|Check Out Photos From Our Latest Work|Frequently Asked Questions|We can.t wait to help you|C o n t a c t)", re.I)
CREDIT = '<p class="small photo-credit">Banner photo: Lone Peak, Utah &middot; runt35, CC BY 3.0, via Wikimedia Commons</p>'


def src(key):
    return open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8", errors="ignore").read()


def meta_title(key):
    s = src(key)
    t = re.search(r"<title>([^<]*)", s); m = re.search(r'<meta name="description" content="([^"]*)', s)
    return (html.unescape(t.group(1)).strip() if t else ""), (html.unescape(m.group(1)).strip() if m else "")


def blocks(key, skip_h1=True):
    s = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", src(key))
    out, started, h1 = [], False, ""
    for t, x in re.findall(r"(?s)<(h1|h2|h3|h4|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).replace(" ,", ",").replace(" .", ".").replace(" :", ":").strip()
        if not x or x in NAVS: continue
        if STOP.search(x):
            if started: break
            continue
        if t in ("h1", "h2") and not started: started = True
        if not started: continue
        if t == "h1" and not h1:
            h1 = x
            if skip_h1: continue
        x = x.replace("https://marble-builders.com/contact/", "")
        out.append((t, x))
    return h1, out


def render(b):
    res, ul = [], []
    def flush():
        if ul: res.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in b:
        if t == "li": ul.append(x); continue
        flush()
        if t == "p": res.append(f"<p>{html.escape(x)}</p>")
        else: res.append(f"<{'h2' if t in ('h1', 'h2') else 'h3'}>{html.escape(x)}</{'h2' if t in ('h1', 'h2') else 'h3'}>")
    flush()
    return "\n".join(res)


def fitmeta(m, extra=" Call Marble Builders at 801-828-5540."):
    m = re.sub(r"\s+", " ", html.unescape(m)).strip()
    if len(m) < 150: m = (m.rstrip(".") + "." + extra)
    if len(m) > 160: m = m[:157].rsplit(" ", 1)[0].rstrip(",;:") + "&hellip;"
    return html.escape(m).replace("&amp;hellip;", "&hellip;")


def fittitle(t):
    t = re.sub(r"\s*[|\-]\s*Marble Builders\s*$", "", t).strip()
    for s in (" | Marble Builders", " | Marble"):
        if 50 <= len(t + s) <= 60: return html.escape(t + s)
    return html.escape((t + " | Marble Builders") if len(t + " | Marble Builders") <= 60 else t[:60])


LANES = [("01", "Emergency &amp; mitigation", "The restoration company stops the damage: water extraction, drying and dehumidification, moisture mapping, removal of soaked drywall, flooring and insulation; soot, smoke and odor removal; mold containment.", "Restoration company"),
         ("02", "Documentation", "Photos, moisture readings and a mitigation scope go to your insurance adjuster.", "Restoration company"),
         ("03", "The gap", "Restoration companies don&rsquo;t typically rebuild what was removed. This is where many homeowners get stuck, left to find, hire and coordinate a contractor on their own.", "Where most homeowners stall"),
         ("04", "Rebuild scope", "Marble reviews the restoration scope, coordinates with the project manager and plans the rebuild, knowing which items need supplements and how to document the work for the carrier.", "Marble Builders"),
         ("05", "Rebuild", "Drywall, flooring, cabinetry, kitchens and bathrooms put back, with clear communication to you and your adjuster from demo to finish.", "Marble Builders"),
         ("06", "Better than before", "&ldquo;Marble didn&rsquo;t just put our basement back together after the water damage, they actually made it better.&rdquo; Eric B.", "Marble Builders")]


def lanes():
    steps = "".join(f'<button type="button" class="ln-s{" is-marble" if who == "Marble Builders" else (" is-gap" if "stall" in who else "")}" data-ln="{i}" aria-pressed="{"true" if i == 2 else "false"}"><span class="mono">{n}</span><b>{t}</b></button>' for i, (n, t, d, who) in enumerate(LANES))
    cards = "".join(f'<div class="ln-c" data-lc="{i}"{"" if i == 2 else " hidden"}><p class="mono">{n} &middot; {who}</p><h3>{t}</h3><p>{d}</p></div>' for i, (n, t, d, who) in enumerate(LANES))
    return f'''<div class="lanes" data-lanes>
<div class="ln-key"><span class="k-r">Restoration company</span><span class="k-m">Marble Builders</span></div>
<div class="ln-track">{steps}</div>
<div class="ln-cards" aria-live="polite">{cards}</div>
<p class="small">Mitigation steps as described in Marble Builders&rsquo; post <a href="@/2025/05/do-restoration-companies-rebuild/">Do restoration companies rebuild homes?</a></p>
</div>'''


REVIEWS = [("Dave Taylor and his team were an excellent choice for my bathroom remodel. Dave listened to what I wanted and provided feedback on what would &amp; would not work from a construction aspect. His crew was exceptional. My bathroom is exactly what I wanted and is structurally sound.", "Debi E."),
           ("Dave was so easy to work with! He was patient as we worked through all the insurance nuances and was communicative along the way.", "Trent F."),
           ("They did a great job, were quick to get the job done, and Hunter came to check things out and was meticulous about being sure everything was done right and to my satisfaction.", "Catherine Bristow"),
           ("We had a flood in our kitchen, we reached out to Jerry with Marble Builders and he was fantastic! They got mitigation going right away and Ally our estimator was the best!", "Aaron Thornock")]
SERV4 = [("remodels-service-page/", "Remodels", "Kitchens, bathrooms, basements and mother-in-law apartments, designed with you."),
         ("property-repairs-service-page/", "Property repairs", "Repairs and insurance rebuilds after water, fire or other damage."),
         ("custom-homes-service-page/", "Custom homes", "Homes built from the ground up around your lifestyle."),
         ("commercial-development-service-page/", "Commercial development", "Commercial projects, from small repairs to full developments.")]
FAQ = [("Do you work with insurance claims?", "<p>Yes. Whether your job is a small property repair or a complete rebuild, we can help you make the most of your insurance claim, and we know how to read and execute a restoration scope.</p>"),
       ("Do restoration companies rebuild homes?", "<p>Not always. Many handle mitigation (drying, demo, cleanup) but don&rsquo;t rebuild what was removed, so you may need a separate contractor. That&rsquo;s where Marble Builders steps in.</p>"),
       ("What areas do you serve in Utah?", "<p>Our Utah team is located in Riverton and serves homeowners anywhere from Payson to Ogden.</p>"),
       ("How fast will you respond?", "<p>Fill out the quote form or call, and a representative will reach out within 24 hours. Business hours are Monday to Friday, 9am to 5pm.</p>")]


def home():
    body = f'''
<section class="m-hero"><div class="mh-img" data-parallax="0.08">{img("mb-hero", "The granite face of Lone Peak in the Wasatch Mountains above the south Salt Lake Valley", priority=True)}</div>
<div class="wrap mh-in"><div class="mh-txt"><p class="label">Riverton, Utah &middot; Payson to Ogden</p>
<h1>General contractor in Riverton, <em>remodels and rebuilds.</em></h1>
<p class="lede">Marble Builders is a general contractor based in Riverton, Utah, with over 20 years of experience. Kitchen, bathroom and basement remodels, property repairs and insurance rebuilds after water or fire damage, custom homes and commercial work, from Payson to Ogden.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18018285540">{PHONE} Call 801-828-5540</a><a class="btn ghost" href="#rebuild">After the damage {ARROW}</a></div></div></div>
<p class="credit">Lone Peak, Utah &middot; runt35, CC BY 3.0, via Wikimedia Commons</p></section>

<section class="sec m-promise"><div class="wrap m-pr-in">
<div class="reveal"><p class="label">Our promise</p><h2>The same care, <em>no matter the size.</em></h2></div>
<div class="reveal"><p class="lede">Our promise is to give the same level of quality and attention to all of our services. Whether your job is a small property repair or a complete commercial development, we can take your vision, assist you with making the most of your insurance claim, and execute a carefully crafted plan to make your vision a reality.</p></div>
</div></section>

<section class="sec m-rebuild" id="rebuild"><div class="wrap">
<div class="m-head split-h reveal"><div><p class="label">After the damage</p><h2>Mitigation dries it out. <em>We put it back.</em></h2></div><p class="lede">After a burst pipe or a fire, two companies usually touch your home. Here&rsquo;s who does what, and where Marble Builders takes over.</p></div>
{lanes()}
</div></section>

<section class="sec m-serv"><div class="wrap">
<div class="m-head split-h reveal"><div><p class="label">What we build</p><h2>Four services. <em>One standard.</em></h2></div><a class="tlink" href="@/services/">All services {ARROW}</a></div>
<div class="slabs">{"".join(f'<a class="slab reveal" href="@/{p}"><span class="mono">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p><em>{ARROW}</em></a>' for i, (p, t, d) in enumerate(SERV4))}</div>
<div class="proj reveal"><p class="label">Recent Utah projects</p>
<a href="@/2025/04/main-level-remodel-with-kitchen-transformation-in-bountiful-ut/"><b>Main-level remodel with kitchen transformation</b><span>Bountiful, UT &middot; wall removed with a hidden structural beam, new kitchen with a 12&Prime; overhang island, two bathrooms reworked</span></a>
<a href="@/2025/04/elegant-bathroom-remodel-in-farmington-ut/"><b>Elegant bathroom remodel</b><span>Farmington, UT</span></a></div>
</div></section>

<section class="sec m-steps"><div class="wrap">
<div class="m-head reveal"><p class="label">How it works</p><h2>Three steps, <em>start to finish.</em></h2></div>
<div class="steps3">{"".join(f'<div class="st reveal"><span class="mono">Step {i + 1}</span><p>{d}</p></div>' for i, d in enumerate(("Schedule a consultation with our design team to talk through your goals, preferences and budget.", "Our designers and craftsmen plan a remodel that matches your vision, with clear communication throughout.", "We bring it to life with regular updates and open communication, until you&rsquo;re presented with the finished space.")))}</div>
<p class="guar reveal"><b>Our quality guarantee.</b> We stand behind our work: if any issues arise, we will promptly address them to ensure your complete satisfaction.</p>
</div></section>

<section class="sec m-revs"><div class="wrap">
<div class="m-head reveal"><p class="label">What they&rsquo;re saying</p><h2>&ldquo;They actually <em>made it better.&rdquo;</em></h2></div>
<div class="revs">{"".join(f'<blockquote class="rev reveal"><p>&ldquo;{q}&rdquo;</p><cite>{n}</cite></blockquote>' for q, n in REVIEWS)}</div>
</div></section>

<section class="sec m-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card m-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What EPA says about lead paint and asbestos when you remodel a home built before 1978.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "General Contractor Riverton, UT | Remodels &amp; Rebuilds | Marble",
            "meta": "Marble Builders: general contractor in Riverton, Utah. Kitchen, bath and basement remodels, insurance rebuilds after water or fire damage, and custom homes.",
            "body": body, "body_class": "is-home", "og": "mb-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


SERVICES = [("services", "services/", "Our services", None), ("remodels_service_page", "remodels-service-page/", "Remodels", "Remodeling Services in Riverton &amp; Salt Lake | Marble"),
            ("property_repairs_service_page", "property-repairs-service-page/", "Property repairs", "Property Repairs &amp; Insurance Rebuilds, Utah | Marble"),
            ("custom_homes_service_page", "custom-homes-service-page/", "Custom homes", "Custom Home Builder in Utah | Marble Builders, Riverton"),
            ("commercial_development_service_page", "commercial-development-service-page/", "Commercial development", "Commercial Development &amp; Construction | Marble Builders")]
CITIES = [("salt_lake_city_utah_home_remodeling", "salt-lake-city-utah-home-remodeling/", "Salt Lake City, Utah"), ("denver_colorado_home_remodeling", "denver-colorado-home-remodeling/", "Denver, Colorado"),
          ("boise_idaho_home_remodeling", "boise-idaho-home-remodeling/", "Boise, Idaho"), ("dallas_texas_home_remodeling", "dallas-texas-home-remodeling/", "Dallas, Texas"),
          ("kansas_city_missouri_home_remodeling", "kansas-city-missouri-home-remodeling/", "Kansas City, Missouri")]
LOST = ["las-vegas-nevada-home-remodeling/", "2025/05/rebuild-process-after-mitigation/", "2025/06/contractor-vs-preferred-vendor/", "2025/06/insurance-bathroom-remodel/", "2025/06/realtor-remodeling-partner/",
        "2025/06/realtor-selling-older-homes/", "2025/07/flood-mitigation-next-steps/", "2025/07/kitchen-remodel-trends-for-2025/", "2025/07/rebuild-contractor-after-house-fire/", "2025/07/rebuild-partner-for-restoration/"]
DEMO = [("salient_architect_about", "salient-architect-about/"), ("salient_architect_landing", "salient-architect-landing/"), ("sample_page", "sample-page/"), ("project__example_project", "project/example-project/"),
        ("project__101_city_blvd", "project/101-city-blvd/"), ("project__590_odessa_ave", "project/590-odessa-ave/"), ("project__the_penn_center", "project/the-penn-center/"),
        ("project_type__commercial", "project-type/commercial/"), ("project_type__remodel", "project-type/remodel/"), ("project_type__residential", "project-type/residential/"),
        ("insuranceclaims", "insuranceclaims/"), ("marble_builders_portfolio", "marble-builders-portfolio/")]


def make_pages():
    out = [home()]
    for key, path, label, title in SERVICES:
        h1, b = blocks(key)
        t0, m0 = meta_title(key)
        cards = "".join(f'<a class="slab" href="@/{p}"><h3>{t}</h3><p>{d}</p><em>{ARROW}</em></a>' for p, t, d in SERV4) if key == "services" else ""
        out.append(K.page(path, label, html.escape(h1 or label), "Riverton &middot; Payson to Ogden", "Marble Builders", title or fittitle(t0.replace("Denver &amp; Surrounding Areas", "Utah").replace("Denver & Surrounding Areas", "Utah")),
                          fitmeta((m0 or "").replace("Denver", "Utah") or f"{label} by Marble Builders."), (f'<div class="slabs in-prose">{cards}</div>' if cards else "") + render(b) + CREDIT,
                          image="mb-hero", alt="Lone Peak, Utah", canonical=canon(path), schema=[K.svc_schema(path, html.unescape(label), "Riverton and the Wasatch Front, UT")] if key != "services" else None))
    for key, path, city in CITIES:
        h1, b = blocks(key)
        t0, m0 = meta_title(key)
        out.append(K.page(path, city, f"Home remodeling in {city}", "Marble Builders", "Location", fittitle(f"Home Remodeling in {city}"),
                          fitmeta(m0 or f"Marble Builders offers home remodeling, property repairs, insurance rebuilds and custom homes in {city}."), render(b) + CREDIT,
                          image="mb-hero", alt="Lone Peak, Utah", crumbs=[("Locations", "locations/")], canonical=canon(path)))
    locs = '<p class="answer">Marble Builders serves homeowners in six metro areas. Our Utah team is located in Riverton, serving anywhere from Payson to Ogden.</p><div class="slabs in-prose">' + \
           "".join(f'<a class="slab" href="@/{p}"><h3>{c}</h3><em>{ARROW}</em></a>' for k, p, c in CITIES) + '<div class="slab"><h3>Las Vegas, Nevada</h3><p>(702) 608-8854</p></div></div>'
    out.append(K.page("locations/", "Locations", "Marble Builders locations", "Six metros, one standard.", "Locations", "Locations: Utah, Denver, Boise &amp; More | Marble Builders",
                      "Marble Builders serves Salt Lake City and the Wasatch Front from Riverton, plus Denver, Boise, Dallas, Kansas City and Las Vegas. Call 801-828-5540 for Utah.", locs + CREDIT,
                      image="mb-hero", alt="Lone Peak, Utah", canonical=canon("locations/")))
    h1, b = blocks("about_us")
    ab = render([(t, x) for t, x in b if not x.startswith(("Marble didn", "Dave ", "David was"))]) + "<h2>What they&rsquo;re saying</h2>" + "".join(f'<blockquote><p>&ldquo;{q}&rdquo;</p><cite>{n}</cite></blockquote>' for q, n in REVIEWS[:2])
    out.append(K.page("about-us/", "About", "About Marble Builders", "Our story.", "About", "About Marble Builders | Remodeling &amp; Rebuild Experts, Utah",
                      "Marble Builders began with one principle: top-quality home renovations that exceed expectations, now across six metro areas from a Riverton, Utah base.", ab + CREDIT,
                      image="mb-hero", alt="Lone Peak, Utah", canonical=canon("about-us/")))
    con = f'''<p class="answer">If you have a project in mind, we&rsquo;d love to help. Fill out the form or give us a call and a representative will reach out within 24 hours.</p>
<dl class="info"><div><dt>Utah</dt><dd><a href="tel:+18018285540">801-828-5540</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd><address>12166 S Redwood Rd<br>Riverton, UT 84065</address></dd></div><div><dt>Hours</dt><dd>M&ndash;F 9am&ndash;5pm</dd></div></dl>
<h2>Other locations</h2><ul><li>Boise, Idaho: (208) 314-6442</li><li>Denver, Colorado: (720) 419-2474</li><li>Dallas, Texas: (469) 320-1227</li><li>Kansas City, Missouri: (816) 325-3477</li><li>Las Vegas, Nevada: (702) 608-8854</li></ul>'''
    out.append(K.page("contact/", "Contact", "Contact Marble Builders", "Request a quote.", "Contact", "Contact Marble Builders | Riverton, Utah General Contractor",
                      "Contact Marble Builders in Riverton, Utah: call 801-828-5540 or email info@marble-builders.com. A representative reaches out within 24 hours, M-F 9-5.",
                      con, canonical=canon("contact/"), form_side=True))
    out.append(K.page("getquote/", "Get a quote", "Get a quote", "Tell us about your project.", "Quote", "Get a Remodeling or Rebuild Quote | Marble Builders, Utah",
                      "Get a quote from Marble Builders for a remodel, property repair, insurance rebuild, custom home or commercial project. Call 801-828-5540 or send the form.",
                      '<p class="answer">Tell us about your project and a representative will reach out within 24 hours.</p>', canonical=canon("getquote/"), form_side=True))
    posts = sorted([f[:-5] for f in os.listdir(os.path.join(HERE, "src", "pages")) if re.match(r"20\d\d__", f)], reverse=True)
    cards = f'<a class="cat" href="@/{p_blog.SLUG}"><b>{p_blog.H1}</b><span>Oct 23, 2026</span><em>Read {ARROW}</em></a>'
    for k in posts:
        y, mo, slug = k.split("__")
        path = f"{y}/{mo}/{slug.replace('_', '-')}/"
        h1, b = blocks(k)
        t0, m0 = meta_title(k)
        h1 = h1 or t0
        cards += f'<a class="cat" href="@/{path}"><b>{html.escape(h1)}</b><span>{["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(mo) - 1]} {y}</span><em>Read {ARROW}</em></a>'
        first = next((x for t, x in b if t == "p" and len(x) > 60), h1)
        out.append(K.page(path, h1[:40], html.escape(h1), f"Marble Builders blog &middot; {y}", "Blog", fittitle(h1), fitmeta(m0 or first), render(b) + CREDIT,
                          image="mb-hero", alt="Lone Peak, Utah", crumbs=[("Blog", "blog/")], canonical=canon(path), ogtype="article",
                          schema=[{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": html.unescape(h1), "datePublished": f"{y}-{mo}-01", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)}]))
    out.append(K.page("blog/", "Blog", "The Marble Builders blog", "Remodeling, rebuilds and design.", "Blog", "Remodeling &amp; Rebuild Blog | Marble Builders, Riverton, Utah",
                      "The Marble Builders blog: kitchen and bathroom design, remodeling costs, custom homes, and what happens after water or fire damage and mitigation.",
                      f'<div class="cats">{cards}</div>', canonical=canon("blog/")))
    for p in LOST:
        out.append(K.page(p, "Archived", "This page is being restored", "", "Marble Builders", "Marble Builders | Remodeling &amp; Insurance Rebuilds, Utah",
                          "Marble Builders: remodels, property repairs and insurance rebuilds in Riverton and across Utah. Call 801-828-5540 or browse the blog for more.",
                          f'<p>This page is being restored. In the meantime, see <a href="@/blog/">the blog</a> or <a href="@/contact/">contact us</a>.</p>', canonical=canon(p), robots="noindex, follow", sitemap=False))
    for k, p in DEMO:
        out.append(K.page(p, "Page", "Marble Builders", "", "Marble Builders", "Marble Builders | Remodeling &amp; Insurance Rebuilds, Utah",
                          "Marble Builders: remodels, property repairs and insurance rebuilds in Riverton and across Utah. Call 801-828-5540 or browse the blog for more.",
                          f'<p><a class="btn" href="@/">Home {ARROW}</a></p>', canonical=U, robots="noindex, follow", sitemap=False))
    out.append(K.page("privacy-policy/", "Privacy policy", "Privacy policy", "", "Legal", "Privacy Policy | Marble Builders, Riverton, Utah Contractor",
                      "Marble Builders privacy policy for marble-builders.com. Questions about your information? Email info@marble-builders.com or call 801-828-5540.",
                      render(blocks("privacy_policy")[1]) or "<p>Questions? Email info@marble-builders.com.</p>", canonical=canon("privacy-policy/")))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Services", "services/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-828-5540.", " Riverton, Utah.")) for x in out]
