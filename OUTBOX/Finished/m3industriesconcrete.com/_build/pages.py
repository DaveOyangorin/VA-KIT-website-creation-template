"""Pages for the m3industriesconcrete.com redesign: "From red dirt to finished slab".

M3 Industries pours concrete in St. George's red dirt: footings, forms, slabs, driveways, then coats and seals. Their own pitch
is about what happens under the surface ("We don't cut corners underground: that's what separates a 5-year concrete job from a
30-year one"). So the site is built around the layers of a slab. References (screenshotted 20 Oct 2026): Holcim (photo-tiled
grid on dark navy), The Concrete Collective (photo hero, serif, dark services band), Hilti (industrial tiles, one hard accent).
CEMEX was behind a security check. Signature: the exploded slab, layer by layer, with the client's own job photo for each.
All 37 live URLs kept (Wix, no trailing slash) with their own canonicals; one new blog post. The Wix template placeholder
contact details are replaced by the client's real ones everywhere. Service pages name St. George in title, H1 and first line."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, EMAIL
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
STOP = ("Get in Touch", "Get a Free Estimate in", "Contact Details")
CLAIMS = re.compile(r"100% Oil|permanent hydrophobic|for a decade|premier concrete|exceptional quality|5 Star Rated|Terry Francine|123-456-7890|info@mysite", re.I)
JUNK = re.compile(r"<p>(?:\d+ hr|1 h|\d+ US dollars?|\$\d+|St\. George, UT|Learn More|Read More)</p>|<h3>​?</h3>")
SVCMAP = {"concrete_driveway_patio": ("Concrete Driveways &amp; Patios", "m3-driveway-cones"), "concrete_coatings_st_george": ("Concrete Coatings &amp; Sealing", "m3-stained-driveway"),
          "copy_of_coatings_sealings": ("Concrete Coatings &amp; Sealing", "m3-stained-steps"), "stamped_decorative_concrete": ("Stamped &amp; Decorative Concrete", "m3-stained-steps"),
          "retaining_walls": ("Retaining Walls", "m3-retaining-wall"), "concrete_pads_slabs": ("Concrete Pads &amp; Slabs", "m3-slab-flag"), "concrete_foundations": ("Concrete Foundations", "m3-foundation-wall"),
          "concrete_sidewalks_walkways": ("Sidewalks &amp; Walkways", "m3-sidewalk-forms"), "concrete_cleaning_st_george": ("Concrete Cleaning", "m3-driveway-side"),
          "concrete_services_st_george": ("Concrete Services", "m3-pour-crew")}
BOOK = {"service_page_sidewalks_walkways": "m3-sidewalk-forms", "service_page_concrete_pads_slabs": "m3-slab-flag-2", "service_page_retaining_walls": "m3-retaining-wall",
        "service_page_concrete_driveways_patios": "m3-driveway-curve", "service_page_concrete_repairs_replacemen": "m3-screed", "service_page_concrete_foundations": "m3-footing",
        "service_page_stamped_decorative_concrete": "m3-stained-steps"}
BOOK = {next(k2 for k2 in EXT if k2.startswith(k)): v for k, v in BOOK.items()}
POSTIMG = ["m3-driveway-cones", "m3-screed", "m3-stained-steps", "m3-slab-home", "m3-pour-crew", "m3-sidewalk-forms", "m3-driveway-curve", "m3-slab-house", "m3-stained-driveway", "m3-footing", "m3-slab-flag", "m3-foundation-forms"]


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def mig(k):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x")).replace("&#39;", "&rsquo;")
    s = tidy(raw, claims=CLAIMS, stop=STOP)
    s = JUNK.sub("", s)
    s = re.sub(r"<ul><li><a [^>]*>\s*</a>\s*", "<ul><li>", s)
    s = s.replace("Craftsmenship", "Craftsmanship").replace("commericial", "commercial")
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    while re.search(r"<h3>[^<]*</h3>\s*$", s): s = re.sub(r"<h3>[^<]*</h3>\s*$", "", s)
    return s.strip(), faqs


def title_of(k): return html.escape(html.unescape(EXT[k]["title"]))


def meta_of(k, fb):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    if len(m) < 110 or "Terry" in m: m = fb
    return html.escape(m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "...")


def gallery(names):
    return '<div class="pstrip">' + "".join(f'<figure class="ps-f">{img(n, "M3 Industries job photo, St. George")}</figure>' for n in names) + "</div>"


def svc_pages():
    out = []
    for k, (lab, im) in SVCMAP.items():
        p = path_of(k); c, f = mig(k)
        h1 = f"{lab} in St. George, UT"
        intro = f"M3 Industries provides {html.unescape(lab).lower().replace('&', 'and')} in St. George, Washington, Santa Clara, Ivins and Hurricane. Call (435) 701-0081 for a free estimate."
        t = f"{lab} in St. George, UT | M3 Industries"
        if len(html.unescape(t)) > 62: t = f"{lab} St. George UT | M3 Industries"
        more = [n for n in ["m3-pour-crew", "m3-screed", "m3-driveway-cones", "m3-stained-steps"] if n != im][:3]
        out.append(K.page(p, lab, h1, "Free estimates &middot; Licensed &amp; insured", "Service", t, meta_of(k, f"{html.unescape(lab)} in St. George, UT from M3 Industries. Licensed and insured. Free estimates: (435) 701-0081."),
                          c + "<h2>From our jobs</h2>" + gallery(more), image=im, alt="M3 Industries job photo, St. George", intro=intro, crumbs=[("Services", "concrete-services-st-george/")], faqs=f,
                          canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, f"{html.unescape(lab)} in St. George, UT", "St. George, UT")))
    return out


def booking_pages():
    out = []
    for k, im in BOOK.items():
        p = path_of(k); t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        desc = html.escape(html.unescape(EXT[k]["meta"] or ""))
        body = f'<p>{desc}</p><p><a class="btn" href="@/inquiry-services-page/">Request a free estimate {ARROW}</a></p>'
        out.append(K.page(p, html.escape(t0), html.escape(t0) + " in St. George", None, "Book a service", title_of(k), meta_of(k, f"{t0} in St. George, UT from M3 Industries. Request a free estimate."),
                          body, image=im, alt="M3 Industries job photo", crumbs=[("Book online", "book-online/")], canonical=EXT[k]["canon"] or None))
    return out


def post_pages():
    out, cards = [], []
    for i, k in enumerate([k for k in EXT if k.startswith("post_")]):
        p = path_of(k); c, f = mig(k); im = POSTIMG[i % len(POSTIMG)]
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        pg = K.page(p, html.escape(t0[:36]), html.escape(t0), f"From the {NAME} blog", "Blog", title_of(k), meta_of(k, f"{t0}: from the M3 Industries concrete blog, St. George, Utah."), c, image=im, alt="",
                    crumbs=[("Blog", "blog/")], faqs=f, canonical=EXT[k]["canon"] or None, ogtype="article")
        pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
        pg["schema"].append({"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": t0, "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)})
        out.append(pg); cards.append((t0, p, im))
    return out, cards


def contact_page():
    info = f'''<p class="answer">Call (435) 701-0081 or send the form for a free, no-obligation quote. We serve St. George, Washington, Santa Clara, Ivins, Hurricane and surrounding Southern Utah communities.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+14357010081">(435) 701-0081</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Office</dt><dd>2570 South 3430 East<br>St. George, UT</dd></div></dl>'''
    return K.page("contact-5/", "Contact", "Contact M3 Industries", "Free, no-obligation quotes for concrete in St. George.", "Contact", "Contact M3 Industries | Concrete Contractor, St. George UT",
                  "Contact M3 Industries in St. George, UT: (435) 701-0081, m3industriesconcrete@gmail.com. Free estimates for driveways, patios, slabs, walls and coatings.",
                  info, canonical=EXT["contact_5"]["canon"] or None, form_side=True)


def generic(k, h1, tag, image=None, extra=""):
    c, f = mig(k)
    return K.page(path_of(k), html.escape(h1[:36]), html.escape(h1), None, tag, title_of(k), meta_of(k, f"{h1}: M3 Industries, concrete contractor in St. George, Utah. Free estimates: (435) 701-0081."),
                  extra + c, image=image, alt="", faqs=f, canonical=EXT[k]["canon"] or None)


def make_pages():
    posts, cards = post_pages()
    cards.insert(0, (p_blog.POST[0], p_blog.POST[1], "m3-screed"))
    bl = "".join(f'<a class="post-card" href="@/{p}">{img(im, "")}<b>{html.escape(t)}</b><em>Read {ARROW}</em></a>' for t, p, im in cards)
    blog = K.page("blog/", "Blog", "Concrete Blog", "Concrete in Southern Utah, explained by the people who pour it.", "Blog", title_of("blog"),
                  "The M3 Industries concrete blog: driveway pricing, stamped concrete care, sealers, pouring in St. George heat, and how to choose a concrete contractor.", f'<div class="posts">{bl}</div>',
                  canonical=EXT["blog"]["canon"] or None)
    svc_tiles = '<div class="svc-cards">' + "".join(f'<a class="svc-card" href="@/{path_of(k)}"><b>{lab}</b><em>{ARROW}</em></a>' for k, (lab, im) in SVCMAP.items() if k not in ("copy_of_coatings_sealings", "concrete_services_st_george")) + "</div>"
    book = "".join(f'<a class="svc-card" href="@/{path_of(k)}"><b>{html.escape(html.unescape(EXT[k]["title"]).split(" | ")[0])}</b><em>{ARROW}</em></a>' for k in BOOK)
    roots = [generic("faqs", "Frequently Asked Questions", "FAQs", "m3-driveway-curve"), generic("inquiry_services_page", "Request a Free Estimate", "Estimate", "m3-pour-crew"),
             K.page("book-online/", "Book Online", "Book Online", "Choose a service and we&rsquo;ll follow up with a free estimate.", "Book", title_of("book_online"),
                    "Book an M3 Industries concrete service in St. George, UT: foundations, driveways and patios, stamped concrete, retaining walls, pads, sidewalks and repairs.",
                    f'<div class="svc-cards">{book}</div>', image="m3-slab-home", alt="", canonical=EXT["book_online"]["canon"] or None),
             generic("privacy_policy", "Privacy Policy", "Legal"), generic("terms_conditions", "Terms & Conditions", "Legal")]
    out = [home_v3.home(cards)] + svc_pages() + booking_pages() + posts + [p_blog.page(K), blog, contact_page()] + roots + \
          [K.notfound((("Services", "concrete-services-st-george/"), ("FAQs", "faqs/"), ("Contact", "contact-5/")))]
    for x in out:
        if x["path"] == "concrete-services-st-george/": x["body"] = x["body"].replace('<article class="prose">', '<article class="prose">' + svc_tiles, 1)
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (435) 701-0081.", " Free estimates.")) for x in out]
