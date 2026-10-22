"""Pages for the stgeorgehomeservices.com redesign: "The paper trail".

The live site is already careful: 197 pages, every number footnoted to a document, the owner on camera, the terms in writing.
So the redesign keeps every word, table, footnote and source list (sx.py extracts the client's own markup structure), and gives
it a documentary shell: paper ground, a literary serif, mono footnote marks, and the client's own photographs captioned like
evidence. References (screenshotted 20 Oct 2026): Basecamp (a plain-spoken letter on paper, signed by the founder), Everlane
"Radical Transparency" (big photography beside a mission statement, cost laid bare), Stripe Press (editorial serif typography).
Signatures on the home page: the printing quote receipt (Plain Terms, line by line) and the eight-town switcher (each town's
facts with their sources, read from the client's own town pages).
All 197 live URLs kept (no trailing slash) with their own canonicals; new blog post under /guides is NOT used (guides are the
client's); the new post lives at /blog/... so it never collides with their guide URLs."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon, crumbs_html, crumbs_ld
from cfg import U, NAME, HERE, AREAS, PHONES, EMAIL, HOURS
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import sx
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
X = {k: sx.extract(k) for k in EXT}
ALT = {}
for v in X.values():
    for n, a in v["imgs"]: ALT.setdefault(n, a)
META = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))
HUBS = ["plumbing", "hvac_st_george_ut", "accessible_living", "water_wise_landscape", "epoxy_flooring_st_george_ut", "painting_st_george_ut", "handyman_st_george_ut",
        "permanent_lighting_st_george_ut", "indoors", "outdoors"]
HUBLABEL = {"plumbing": "Plumbing", "hvac_st_george_ut": "Heating and air", "accessible_living": "Accessible living", "water_wise_landscape": "Water-wise landscape",
            "epoxy_flooring_st_george_ut": "Concrete coatings", "painting_st_george_ut": "Painting", "handyman_st_george_ut": "Handyman", "permanent_lighting_st_george_ut": "Permanent lighting",
            "indoors": "Indoors", "outdoors": "Outdoors"}
FALLBACK = ["graded-tile-plumbing", "work-bathroom-remodel-wide", "graded-hero-filtration", "work-ac-condenser-gauges-st-george", "coatings-garage-flake-low-angle-door",
            "work-water-wise-front-yard-wide-st-george", "painting-accent-wall-after", "work-tankless-interior-closet", "work-sewer-excavation-new-and-old-pipe", "work-shower-after-1600"]


def iname(n): return os.path.splitext(n)[0].replace("__", "-")


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


PARENT = {}
for h in ["hvac_st_george_ut", "accessible_living", "water_wise_landscape", "epoxy_flooring_st_george_ut", "painting_st_george_ut", "permanent_lighting_st_george_ut", "handyman_st_george_ut", "plumbing", "indoors", "outdoors"]:
    raw = open(os.path.join(HERE, "src", "pages", h + ".html"), encoding="utf-8").read()
    for s in re.findall(r'href="/services/([a-z0-9\-]+)"', raw):
        PARENT.setdefault("services_" + s.replace("-", "_"), h)


def phero(trail, h1, lede, tag, image=None, alt="", art=None):
    """Documentary hero: paper ground, the title set like a book page, the client's own photograph with its caption."""
    lab, ph, tel = K.P1()
    fig = ""
    if image:
        cap = alt or ALT.get(image, "")
        fig = f'<figure class="ev">{img(image, cap, priority=True)}<figcaption><span class="ev-k">Our photo</span>{html.escape(cap) if cap else ""}</figcaption></figure>'
    return f'''<section class="dh{" has-fig" if fig else ""}"><div class="wrap dh-in"><div class="dh-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}
<div class="btn-row"><a class="btn accent" href="tel:{tel}">{PHONE} {ph}</a><a class="btn ghost" href="@/{K.C.CTA_PATH}">{K.C.CTA_LABEL} {ARROW}</a></div></div>{fig}</div></section>'''


K.phero = phero


def clean(body):
    body = re.sub(r"(</ul>)\s*See [^<]{2,60}(</li>)", r"\1\2", body)
    body = re.sub(r"<p>\s*(Call \(435\) 850-0053|Ask for a visit|Read our Plain Terms)[^<]{0,40}</p>", "", body)
    return body


def make_page(k):
    x = X[k]; p = path_of(k)
    h1 = html.escape(x["h1"] or EXT[k]["title"].split(" · ")[0])
    sec = p.split("/")[0]
    crumbs, tag = [], "St. George Home Services"
    if k.startswith("services_"):
        par = PARENT.get(k)
        crumbs = [(HUBLABEL[par], path_of(par))] if par else []
        tag = HUBLABEL.get(par, "Service")
        if "St. George" not in h1: h1 = f"{h1} in St. George"
    elif k in HUBS:
        tag = "What we do"
        if "St. George" not in h1 and k not in ("indoors", "outdoors"): h1 = f"{h1} in St. George"
    elif sec == "guides" and k != "guides": crumbs, tag = [("Guides", "guides/")], "Guide"
    elif sec == "hoa" and k != "hoa": crumbs, tag = [("Associations", "hoa/")], "Association"
    elif sec == "areas" and k != "areas": crumbs, tag = [("Towns", "areas/")], "Town"
    elif sec == "emergency-plumbing" and k != "emergency_plumbing": crumbs, tag = [("Emergency plumbing", "emergency-plumbing/")], "Emergency plumbing"
    ims = [iname(n) for n, a in x["imgs"] if iname(n) in META]
    if not ims and k.startswith("services_") and PARENT.get(k):
        ims = [iname(n) for n, a in X[PARENT[k]]["imgs"] if iname(n) in META]
    image = ims[0] if ims else (None if k in ("privacy", "accessibility") else FALLBACK[sum(map(ord, k)) % len(FALLBACK)])
    alt = ""
    for n, a in X[k]["imgs"] + (X[PARENT[k]]["imgs"] if PARENT.get(k) else []):
        if iname(n) == image: alt = a; break
    if not alt and image:
        alt = next((a for n, a in ALT.items() if iname(n) == image), "")
    body = clean(x["body"])
    rest = [i for i in ims[1:4]]
    if rest and len(body) > 1500:
        body += '<div class="ev-strip">' + "".join(f'<figure class="ev sm">{img(i, next((a for n, a in ALT.items() if iname(n) == i), ""))}<figcaption><span class="ev-k">Our photo</span>{html.escape(next((a for n, a in ALT.items() if iname(n) == i), ""))}</figcaption></figure>' for i in rest) + "</div>"
    title = html.escape(html.unescape(EXT[k]["title"]))
    meta = html.escape(html.unescape(EXT[k]["meta"] or ""))
    if len(html.unescape(meta)) < 60: meta = html.escape(f"{html.unescape(h1)}: {NAME}, St. George, Utah. The quote is the number. Call (435) 850-0053.")
    pg = K.page(p, html.escape(x["h1"][:38]) if x["h1"] else h1, h1, html.escape(x["lede"]) if x["lede"] else None, tag, title, meta, body, image=image, alt=alt, crumbs=crumbs,
                faqs=x["faqs"], canonical=EXT[k]["canon"] or None,
                schema=K.svc_schema(p, html.unescape(h1), "St. George, UT") if k.startswith("services_") else None, ogtype="article" if sec == "guides" else None)
    if sec in ("guides", "research", "plain-terms", "privacy", "accessibility") or k.startswith("areas_") or k.startswith("hoa_"):
        pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose doc">', 1)
    return pg


def town_facts():
    """For the home switcher: per town, the first fact of four sections, each with its source title, from the town's own page."""
    out = []
    for k in [k for k in EXT if k.startswith("areas_")]:
        raw = open(os.path.join(HERE, "src", "pages", k + ".html"), encoding="utf-8").read()
        name = EXT[k]["title"].split(" · ")[0]
        name = re.sub(r"^.*? in ", "", X[k]["h1"]).rstrip(".") if " in " in X[k]["h1"] else name
        facts = []
        for sec in re.findall(r'<section id="[a-z\-]+" class="townfacts">.*?</section>', raw, re.S)[:4]:
            lab = re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
            m = re.search(r'<ul class="facts"><li>(.*?)<a class="cite" href="(#[^"]+)"[^>]*title="([^"]*)"', sec, re.S)
            if lab and m:
                facts.append((re.sub(r"<[^>]+>", "", lab.group(1)), html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip(), path_of(k) + m.group(2), html.unescape(m.group(3))))
        n = re.search(r"([0-9]+) checkable facts", X[k]["lede"] + EXT[k]["text"][:600])
        out.append((name, path_of(k), n.group(1) if n else "", facts))
    return out


def contact_page():
    pg = make_page("contact")
    form = f'''<form class="form" method="post" action="" id="ask"><h3>Send us three things</h3><p class="small">Your name, a number to call back, and a sentence about what&rsquo;s going on. You don&rsquo;t have to know what it&rsquo;s called.</p>
<div class="row"><label for="f-name">Your name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone number to call back *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email address (optional)<input id="f-email" type="email" name="email" autocomplete="email"></label>
<label for="f-msg">What&rsquo;s going on *<textarea id="f-msg" name="message" required></textarea></label>
<button class="btn" type="submit">Send it {ARROW}</button><p class="small">We call back. We don&rsquo;t put you on a list. Emergency? Shut the water off first, then call.</p></form>'''
    pg["body"] = re.sub(r'<aside class="sv-side">.*?</aside>', f'<div class="form-col">{form}</div>', pg["body"], count=1, flags=re.S)
    return pg


def make_pages():
    out = [home_v3.home(X, town_facts())]
    for k in EXT:
        if k == "home": continue
        pg = contact_page() if k == "contact" else make_page(k)
        if k == "win": pg.update(sitemap=False, robots="noindex, follow")
        out.append(pg)
    out += p_blog.pages(K)
    out.append(K.notfound((("Plumbing", "plumbing/"), ("Plain Terms", "plain-terms/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (435) 850-0053.",)) for x in out]
