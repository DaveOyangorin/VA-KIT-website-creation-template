"""Pages for the greenjanitorialservice.com redesign: "Spotless & green".

GJS sells two things at once: a detailed, almost luxury clean, and biodegradable products that are safe for people, pets and plants.
So the home page opens on the one photo that is truly theirs, the two GJS vans, full-bleed under a deep forest green, and the signature is
the service finder: choose the space (home, office or retail, medical or public facility, construction site, move-in/out) and the kind
of clean (routine, deep, specialized), and a card shows exactly which GJS services fit, in their own words, with their maintenance rhythm.
Forest green and leaf green from the name; Jost (close to their logo's Futura), Instrument Sans, DM Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 11 URLs plus the 6 linked blog posts (no trailing slash); /home-4514 duplicate kept noindex. One new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL, CITIES
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta
NAVS = {"Home", "Commercial Services", "Residential Services", "Specialized Services", "Our Story", "Careers", "Blog", "Contact", "Our Services"}
STOP = re.compile(r"^(COMPANY|Schedule a Service|Read More Reviews|Share this|Related|Recent Posts|Subscribe|Previous|Next|Back to Blog)", re.I)


def blocks(key, start_h1=True):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    s = re.sub(r"(?s)<(script|style|svg|noscript|nav|header|footer)\b.*?</\1>", "", s)
    out, started, seen = [], not start_h1, set()
    for t, x in re.findall(r"(?s)<(h1|h2|h3|h4|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).replace(" ,", ",").replace(" .", ".").strip()
        if not x: continue
        if t == "h1": started = True; continue
        if not started: continue
        if STOP.search(x): break
        if t == "li" and x in NAVS: continue
        if x in seen: continue
        seen.add(x); out.append((t, x))
    return out


def render(b):
    res, ul = [], []
    def flush():
        if ul: res.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in b:
        if t == "li": ul.append(x); continue
        flush()
        if t == "p" and len(x) < 45 and not x.endswith((".", "!", "?", ":")): t = "h3"
        if x in NAVS: continue
        res.append(f"<p>{html.escape(x)}</p>" if t == "p" else f"<{'h2' if t in ('h2',) else 'h3'}>{html.escape(x)}</{'h2' if t in ('h2',) else 'h3'}>")
    flush()
    return "\n".join(res)


# their services, their words (commercial, residential and specialized pages)
SV = {
    "site": ("Commercial site cleaning", "commercial/", "Offices, retail establishments and industrial facilities, cleaned with professional-grade tools and eco-friendly products."),
    "facility": ("Comprehensive facility cleaning", "commercial/", "Public buildings such as hospitals, rehabilitation centers and other facilities, from routine maintenance to specialized tasks."),
    "construction": ("Construction site cleaning", "commercial/", "Debris, dust and residues cleared with advanced equipment and water, for a safe, tidy workspace."),
    "deep": ("Deep cleaning", "commercial/", "Intensive cleaning that removes dirt, grime and contaminants from all surfaces."),
    "move": ("Move-in / move-out cleaning", "residential/", "A fresh start for new tenants, staging your home for sale, or the final clean that gets your deposit back."),
    "home": ("Home maintenance cleaning", "residential/", "A deep clean, then weekly, bi-weekly or monthly maintenance: kitchens, bathrooms, living areas and bedrooms, bedmaking, vacuuming, mopping, dusting blinds, garbage and cans."),
    "detail": ("Detail add-ons", "residential/", "Oven and refrigerator, baseboards, window cleaning and more."),
    "carpet": ("Carpet cleaning", "specialized/", "Advanced techniques and equipment to deep clean carpets and remove stains."),
    "disinfect": ("Disinfection", "specialized/", "Electrostatic sprayers for thorough disinfection of your premises."),
    "floor": ("Floor scrubbing", "specialized/", "Industrial-grade scrubbers to clean and restore floor surfaces."),
    "strip": ("Strip &amp; wax", "specialized/", "Stripping and waxing that turns dull, worn floors into polished surfaces."),
    "power": ("Power washing", "specialized/", "Storefront windows, decks and patios."),
    "high": ("High dusting", "specialized/", "Dust and debris removed from high, hard-to-reach areas."),
    "window": ("Window cleaning", "specialized/", "Streak-free windows in commercial and residential settings."),
}
SPACES = [("home", "Home"), ("office", "Office or retail"), ("facility", "Medical or public facility"), ("construction", "Construction site"), ("move", "Move-in / move-out")]
NEEDS = [("routine", "Routine"), ("deep", "Deep clean"), ("special", "Specialized")]
MATRIX = {
    ("home", "routine"): ["home", "detail"], ("home", "deep"): ["home", "detail", "carpet"], ("home", "special"): ["carpet", "window", "power", "high"],
    ("office", "routine"): ["site", "window"], ("office", "deep"): ["deep", "carpet", "floor"], ("office", "special"): ["strip", "floor", "high", "power", "disinfect"],
    ("facility", "routine"): ["facility"], ("facility", "deep"): ["facility", "deep", "disinfect"], ("facility", "special"): ["disinfect", "strip", "floor", "high"],
    ("construction", "routine"): ["construction"], ("construction", "deep"): ["construction", "deep", "window"], ("construction", "special"): ["construction", "power", "high", "floor"],
    ("move", "routine"): ["move"], ("move", "deep"): ["move", "deep", "detail"], ("move", "special"): ["move", "carpet", "window"],
}


def finder():
    sp = "".join(f'<button type="button" class="chip" data-sp="{k}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n) in enumerate(SPACES))
    nd = "".join(f'<button type="button" class="chip" data-nd="{k}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n) in enumerate(NEEDS))
    data = {"sv": {k: {"t": t, "href": "@/" + h, "d": d} for k, (t, h, d) in SV.items()}, "m": {f"{a}|{b}": v for (a, b), v in MATRIX.items()}}
    return f'''<div class="finder" data-finder>
<div class="fd-q"><p class="fd-n"><span>1</span>What are we cleaning?</p><div class="chips" role="group" aria-label="Space">{sp}</div>
<p class="fd-n"><span>2</span>What kind of clean?</p><div class="chips" role="group" aria-label="Type of clean">{nd}</div>
<p class="fd-note">Every service uses biodegradable, environmentally friendly products.</p></div>
<div class="fd-card" aria-live="polite"><div class="fd-tag" aria-hidden="true"></div><p class="label" data-fd-h>Your GJS clean</p><div data-fd-list></div>
<a class="btn accent" href="@/contact-5033/">Request a quote {ARROW}</a></div>
<script type="application/json" data-fd-data>{json.dumps(data)}</script>
<noscript><p>Commercial: site, facility, construction and deep cleaning. Residential: weekly, bi-weekly or monthly maintenance and move-in/move-out. Specialized: carpet, floors, strip &amp; wax, power washing, high dusting, windows, disinfection.</p></noscript>
</div>'''


QUOTES = ["Green Janitorial has been cleaning where I work for close to 8 years. The products they use are green and environment-friendly. They pay attention to the small details and do an excellent job! I highly recommend their company!",
          "We had GJS do the final cleaning on one of our jobs. They were so amazing to work around difficult schedules, added items, messy subcontractors and one of our top superintendents.",
          "When they are done, I notice they have cleaned things I thought were uncleanable.",
          "My stainless steel surfaces look better than ever. I am super happy with their work and recommend them to anyone in the market for cleaning services."]
FAQ = [("What areas do you serve?", "<p>South Salt Lake and the Salt Lake Valley, including Salt Lake City, Sugar House, Millcreek, Holladay, Murray, Midvale, Sandy, Draper, South Jordan, Daybreak, Taylorsville, West Valley and more.</p>"),
       ("What products do you use?", "<p>Biodegradable, environmentally friendly products that are safe for people, pets and plants, without compromising cleanliness.</p>"),
       ("How often can you clean my home?", "<p>We start with a deep cleaning, followed by weekly, bi-weekly or monthly maintenance.</p>"),
       ("What are your hours?", "<p>Monday to Friday 7:00 AM to 7:00 PM, Saturday 7:00 AM to 5:00 PM. Closed Sunday.</p>")]


def home():
    body = f'''
<section class="g-hero"><div class="gh-img" data-parallax="0.08">{img("gj-vans", "Two white Green Janitorial Services vans with the green GJS logo, parked outside", priority=True)}</div>
<div class="wrap gh-in"><div class="gh-txt"><p class="label">South Salt Lake &middot; Family-owned since 2018</p>
<h1>Janitorial services in South Salt Lake, <em>done green.</em></h1>
<p class="lede">Green Janitorial Services (GJS) is a family-owned janitorial and residential cleaning company in South Salt Lake. Offices, facilities, construction sites and homes, cleaned in detail with biodegradable, environmentally friendly products.</p>
<div class="btn-row"><a class="btn accent" href="@/contact-5033/">Get a quote {ARROW}</a><a class="btn ghost" href="tel:+18015778703">{PHONE} +1 801-577-8703</a></div></div></div>
<div class="gh-strip"><div class="wrap"><span><b>3</b> service lines: commercial, residential, specialized</span><span><b>21</b> neighborhoods &amp; cities</span><span><b>Mon&ndash;Sat</b> from 7:00 AM</span></div></div></section>

<section class="sec g-find" id="finder"><div class="wrap">
<div class="g-head split-h reveal"><div><p class="label">Find your clean</p><h2>Tell us the space. <em>We&rsquo;ll match the clean.</em></h2></div><p class="lede">Two taps show which GJS services fit, from routine maintenance to strip-and-wax.</p></div>
{finder()}
</div></section>

<section class="sec g-vals"><div class="wrap">
<div class="g-head reveal"><p class="label">How we work</p><h2>Detail-obsessed. <em>Planet-friendly.</em></h2></div>
<div class="vals">
<div class="val reveal"><span class="leaf" aria-hidden="true"></span><b>Sustainable excellence</b><p>Our biodegradable, environmentally friendly products benefit our employees, clients, and community.</p></div>
<div class="val reveal"><span class="leaf" aria-hidden="true"></span><b>Commitment to quality</b><p>Detailed cleaning for a healthier environment, and continuous training that keeps our team ahead of the curve.</p></div>
<div class="val reveal"><span class="leaf" aria-hidden="true"></span><b>Safe for people, pets &amp; plants</b><p>Traditional chemicals can harm health and damage furniture and fixtures. We use biodegradable products instead.</p></div>
</div></div></section>

<section class="g-band"><div class="band-img" data-parallax="0.1">{img("gj-skyline", "Downtown Salt Lake City skyline with the Wasatch Mountains")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our story</p><p>Our journey began 11 years ago when our family moved from Mexico to the United States. In 2018, we founded Green Janitorial Services.</p><a class="tlink" href="@/ourstory/">Read our story {ARROW}</a></blockquote></div>
<p class="credit">Salt Lake City &middot; Invictus323, CC BY 4.0, via Wikimedia Commons</p></section>

<section class="sec g-revs"><div class="wrap">
<div class="g-head reveal"><p class="label">What our clients are saying</p><h2>&ldquo;They pay attention to <em>the small details.</em>&rdquo;</h2></div>
<div class="revs">{"".join(f'<blockquote class="rev reveal"><p>&ldquo;{html.escape(q)}&rdquo;</p><cite>GJS client</cite></blockquote>' for q in QUOTES)}</div>
</div></section>

<section class="sec g-areas"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Where we clean</p><h2>Proudly serving <em>the valley.</em></h2><div class="cities">{"".join(f"<span>{c}</span>" for c in CITIES)}</div>
<a class="post-card g-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What EPA&rsquo;s Safer Choice and Design for the Environment labels mean, and why &ldquo;eco-friendly&rdquo; alone says little.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Janitorial Services South Salt Lake | Green Janitorial (GJS)",
            "meta": "Green Janitorial Services: family-owned janitorial and residential cleaning in South Salt Lake, UT. Offices, facilities, construction and homes, cleaned green.",
            "body": body, "body_class": "is-home", "og": "gj-vans", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


POSTS = [("post/cleaning-hacks-for-a-relaxing-december/", "post_cleaning_hacks_for_a_relaxing_december", "Nov 14, 2025", "2025-11-14"),
         ("post/cleaning-with-purpose/", "post_cleaning_with_purpose", "Nov 14, 2025", "2025-11-14"),
         ("post/how-mess-impacts-health/", "post_how_mess_impacts_health", "Oct 1, 2025", "2025-10-01"),
         ("post/clean-home-supports-healthy-aging/", "post_clean_home_supports_healthy_aging", "Sep 2, 2025", "2025-09-02"),
         ("post/outsourcing-cleaning/", "post_outsourcing_cleaning", "Aug 5, 2025", "2025-08-05"),
         ("post/outdoor-home-maintenance/", "post_outdoor_home_maintenance", "Jul 1, 2025", "2025-07-01")]


TT = {"post_cleaning_hacks_for_a_relaxing_december": "Holiday Cleaning Hacks for a Relaxing December | GJS Blog",
      "post_cleaning_with_purpose": "Cleaning with Purpose: Donate, Declutter, Give Back | GJS",
      "post_how_mess_impacts_health": "How Dirt and Mess at Home Can Impact Health | GJS Blog",
      "post_outdoor_home_maintenance": "Deep Cleaning Outdoor Spaces for Summer Gatherings | GJS",
      "post_clean_home_supports_healthy_aging": "How a Clean, Organized Home Supports Healthy Aging | GJS"}


def post_meta(key):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    t = html.unescape(re.search(r"<title>([^<]*)", s).group(1)).strip()
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    return t, html.unescape(m.group(1)).strip() if m else ""


def fitmeta(m, extra):
    m = re.sub(r"\s+", " ", m)
    if len(m) < 150: m = (m.rstrip(".") + ". " + extra).strip()
    if len(m) > 160: m = m[:157].rsplit(" ", 1)[0] + "&hellip;"
    return m


CR = {"gj-ssl": "South Salt Lake City Hall &middot; SSLaker3, CC BY-SA 3.0, via Wikimedia Commons", "gj-slc": "Salt Lake City &middot; Garrett from Salt Lake City, CC BY 2.0, via Wikimedia Commons",
      "gj-skyline": "Salt Lake City &middot; Invictus323, CC BY 4.0, via Wikimedia Commons"}


def credit(im):
    return f'<p class="small photo-credit">Banner photo: {CR[im]}</p>'


def make_pages():
    out = [home()]
    out.append(dict(home(), path="home-4514/", canonical=U, robots="noindex, follow", sitemap=False))
    cm = '<p class="answer">Commercial cleaning tailored to your space: offices, retail, industrial, public and medical facilities, construction sites, deep cleans and move-ins, with eco-friendly products.</p>' + render(blocks("commercial"))
    out.append(K.page("commercial/", "Commercial", "Commercial cleaning services", "Offices, facilities and construction sites.", "Commercial", "Commercial &amp; Office Cleaning, South Salt Lake | GJS",
                      "Commercial and office cleaning from GJS in South Salt Lake: offices, retail, facilities, construction sites, deep cleaning and move-in/move-out, done green.",
                      cm + credit("gj-ssl"), image="gj-ssl", alt="South Salt Lake City Hall", canonical=EXT["commercial"]["canon"], schema=[K.svc_schema("commercial/", "Commercial cleaning", "South Salt Lake and the Salt Lake Valley, UT")]))
    rs = '<p class="answer">A deep cleaning followed by weekly, bi-weekly or monthly maintenance, with 100% environmentally friendly, biodegradable products that are safe for people, pets and plants.</p>' + render(blocks("residential"))
    out.append(K.page("residential/", "Residential", "Residential cleaning services", "Weekly, bi-weekly or monthly.", "Residential", "House Cleaning in South Salt Lake &amp; Salt Lake | GJS",
                      "Residential cleaning from GJS: a deep clean, then weekly, bi-weekly or monthly house cleaning across the Salt Lake Valley, with biodegradable products.",
                      rs + credit("gj-slc"), image="gj-slc", alt="Salt Lake City", canonical=EXT["residential"]["canon"], schema=[K.svc_schema("residential/", "Residential cleaning", "the Salt Lake Valley, UT")]))
    sp = '<p class="answer">Specialized cleaning for homes and businesses: carpet cleaning, disinfection with electrostatic sprayers, floor scrubbing, power washing, high dusting, strip and wax, and windows.</p>' + \
         render([(t, ("Strip &amp; Wax" if x == "Strip" else x.replace("COVID-19 Disinfection Services", "Disinfection Services"))) for t, x in blocks("specialized") if not x.startswith("Embrace the luxury")])
    out.append(K.page("specialized/", "Specialized", "Specialized cleaning services", "Carpets, floors, windows and more.", "Specialized", "Specialized Cleaning: Floors, Carpet &amp; Windows | GJS",
                      "Specialized cleaning from GJS in South Salt Lake: carpet cleaning, floor scrubbing, strip and wax, power washing, high dusting, windows and disinfection.",
                      sp + credit("gj-skyline"), image="gj-skyline", alt="Salt Lake City skyline", canonical=EXT["specialized"]["canon"], schema=[K.svc_schema("specialized/", "Specialized cleaning", "the Salt Lake Valley, UT")]))
    st = render(blocks("ourstory", False)) + f'<figure class="pfig">{img("gj-vans", "Two GJS vans")}<figcaption>The GJS vans.</figcaption></figure>'
    out.append(K.page("ourstory/", "Our story", "Our story", "From Mexico to South Salt Lake, family-owned since 2018.", "Our story", "Our Story: Family-Owned Since 2018 | Green Janitorial (GJS)",
                      "Our journey began 11 years ago when our family moved from Mexico. In 2018 we founded Green Janitorial Services: luxury, eco-friendly cleaning in Utah.",
                      st, image="gj-vans", alt="The GJS vans", canonical=EXT["ourstory"]["canon"]))
    jb = render(blocks("join_our_team"))
    out.append(K.page("join-our-team/", "Careers", "Join our team", "Residential and commercial cleaner openings.", "Careers", "Cleaning Jobs in Salt Lake | Join Green Janitorial Services",
                      "Join Green Janitorial Services: residential and commercial cleaner jobs in the Salt Lake Valley with paid training, flexible schedules and transportation.",
                      jb, canonical=EXT["join_our_team"]["canon"], form_side=True))
    con = f'''<p class="answer">Tell us about your space and we&rsquo;ll get back to you with a quote.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18015778703">+1 801-577-8703</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd><address>2685 S W Temple St Suite 6<br>South Salt Lake, UT 84115</address></dd></div><div><dt>Hours</dt><dd>Mon&ndash;Fri 7:00 AM&ndash;7:00 PM<br>Saturday 7:00 AM&ndash;5:00 PM<br>Sunday closed</dd></div></dl>'''
    out.append(K.page("contact-5033/", "Contact", "Contact GJS", "Commercial, residential and specialized cleaning quotes.", "Contact", "Contact Green Janitorial Services | South Salt Lake, UT",
                      "Contact Green Janitorial Services in South Salt Lake: call +1 801-577-8703, Monday to Saturday from 7:00 AM, or send the form for a free cleaning quote today.",
                      con, canonical=EXT["contact_5033"]["canon"], form_side=True))
    cards = f'<a class="cat" href="@/{p_blog.SLUG}"><b>{p_blog.H1}</b><span>Oct 22, 2026</span><em>Read {ARROW}</em></a>'
    for p, k, d, iso in POSTS:
        t, m = post_meta(k)
        cards += f'<a class="cat" href="@/{p}"><b>{html.escape(t)}</b><span>Claudia Hinojosa &middot; {d}</span><em>Read {ARROW}</em></a>'
    for path, key, h1, title in (("bloghome/", "bloghome", "The GJS blog", "Cleaning Tips &amp; News Blog | Green Janitorial Services Utah"), ("blog/", "blog", "Blog", "Blog | Green Janitorial Services, South Salt Lake, Utah")):
        out.append(K.page(path, "Blog", h1, "Cleaning tips for Utah homes and workplaces.", "Blog", title,
                          "The Green Janitorial Services blog: cleaning tips for Utah homes and workplaces, from holiday cleaning hacks and decluttering to healthy aging and transitions.",
                          f'<div class="cats">{cards}</div>', canonical=EXT[key]["canon"] or canon(path)))
    for p, k, d, iso in POSTS:
        t, m = post_meta(k)
        tt = TT.get(k) or (t if len(t) > 50 else t + " | GJS Blog")
        out.append(K.page(p, t[:40], html.escape(t), f"By Claudia Hinojosa &middot; {d}", "Blog", html.escape(tt), html.escape(fitmeta(m or t, "Tips from Green Janitorial Services in South Salt Lake.")).replace("&amp;hellip;", "&hellip;"),
                          render(blocks(k)), crumbs=[("Blog", "bloghome/")], canonical=canon(p), ogtype="article",
                          schema=[{"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": t, "datePublished": iso, "author": {"@type": "Person", "name": "Claudia Hinojosa"}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)}]))
    out.append(K.page("termsofservice/", "Terms of service", "Terms &amp; conditions", "Green Janitorial Services LLC", "Legal", "Terms of Service | Green Janitorial Services LLC, Utah",
                      "Green Janitorial Services LLC terms and conditions for residential, commercial and construction cleaning: scheduling, payment, cancellations and more.",
                      render(blocks("termsofservice", start_h1=False)[0:400]), canonical=canon("termsofservice/")))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Commercial", "commercial/"), ("Residential", "residential/"), ("Contact", "contact-5033/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call +1 801-577-8703.", " South Salt Lake, UT.")) for x in out]
