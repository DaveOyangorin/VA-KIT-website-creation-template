"""Pages for the thedisasterrepairteam.com redesign: "Four kinds of bad day".

Disaster Repair Team handles four losses that look and feel completely different: water, fire, smoke and mold. So the site
gives each its own colour and its own first steps, and the home page hero switches between them. The second idea is theirs:
one team from mitigation through insurance through rebuild, with fewer handoffs. References (screenshotted 20 Oct 2026):
SERVPRO (the category's green-and-orange urgency), Paul Davis (dark emergency hero with a phone panel), and Linear (a dark
interface where each state re-colours the page). Signature: the damage-type switcher; second piece: the one-team line.
All 127 live URLs kept (trailing slash) with their own canonicals; one new blog post. Service pages name Lehi in the title,
H1 and first paragraph (report: no page named Lehi); city landing pages name their own city."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, HOURS
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
STOP = ("Need help right now?", "Need help with active damage?", "GET A FREE", "Request Help or an Estimate", "Active emergency? Call now")
SKIP = ("Available 24/7", "385-287-6344", "4.9", "120+ Google reviews", "CALL NOW")
ELEM = {"water": ("drt-ceiling", "Water damage"), "sewage": ("drt-carpet", "Sewage cleanup"), "fire": ("drt-fire", "Fire damage"), "smoke": ("drt-fire", "Smoke damage"),
        "mold": ("drt-mold", "Mold remediation"), "foundation": (None, "Foundation repair"), "insulation": (None, "Insulation"), "commercial": ("drt-carpet", "Commercial restoration")}
SVCS = {"water_damage_cleanup_restoration": "water", "sewage_cleanup": "sewage", "fire_damage_cleanup_restoration": "fire", "smoke_damage_cleanup_restoration": "smoke",
        "mold_remediation_restoration": "mold", "foundation_repair": "foundation", "insulation_services": "insulation", "commercial_restoration": "commercial"}
LABEL = {"water_damage_cleanup_restoration": "Water Damage Cleanup &amp; Restoration", "sewage_cleanup": "Sewage Backup Cleanup", "fire_damage_cleanup_restoration": "Fire Damage Cleanup &amp; Restoration",
         "smoke_damage_cleanup_restoration": "Smoke Damage Cleanup &amp; Restoration", "mold_remediation_restoration": "Mold Remediation &amp; Restoration", "foundation_repair": "Foundation Crack &amp; Leak Repair",
         "insulation_services": "Insulation Removal &amp; Replacement", "commercial_restoration": "Commercial Restoration"}


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def elem_of(k):
    for e in ("water", "sewage", "fire", "smoke", "mold", "foundation", "insulation", "commercial"):
        if e in k: return e
    return None


def mig(k):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x")).replace("&#39;", "&rsquo;")
    s = tidy(raw, stop=STOP, skip=SKIP)
    s = re.sub(r"<p>(?:4\.9|120\+ Google reviews|385-287-6344|435-619-9594)</p>", "", s)
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    return s.strip(), faqs


def steps_of(k):
    s, f = mig(k)
    return re.findall(r"<h3>([^<]+)</h3>\s*<p>(.*?)</p>", s)[:4]


def title_of(k): return html.escape(html.unescape(EXT[k]["title"]))


def meta_of(k, fb):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    if len(m) < 110: m = fb
    return html.escape(m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "...")


def theme(pg, e):
    if e: pg["body_class"] = f"el-{e}"
    return pg


def svc_pages():
    out = []
    for k, e in SVCS.items():
        p = path_of(k); c, f = mig(k); im, lab0 = ELEM[e]
        lab = LABEL[k]
        h1 = f"{lab} in Lehi &amp; Across Utah"
        intro = f"Disaster Repair Team provides {html.unescape(lab).lower().replace('&', 'and')} in Lehi, across Northern Utah and in St. George. Call 385-287-6344, available 24/7, or 435-619-9594 in Southern Utah."
        t = f"{lab} in Lehi, UT | Disaster Repair Team"
        if len(html.unescape(t)) > 62: t = f"{lab0} in Lehi, UT | Disaster Repair Team"
        out.append(theme(K.page(p, lab0, h1, "Available 24/7 &middot; Northern Utah &amp; St. George", "Service", t,
                                meta_of(k, f"{html.unescape(lab)} in Lehi and across Utah from Disaster Repair Team. Available 24/7: 385-287-6344."), c, image=im, alt="Disaster Repair Team job photo" if im else "",
                                intro=intro, crumbs=[("Services", "services/")], faqs=f, canonical=EXT[k]["canon"] or None,
                                schema=K.svc_schema(p, f"{html.unescape(lab)} in Lehi, UT", "Lehi, UT")), e))
    return out


def landing_pages():
    out = []
    for k in [k for k in EXT if k.startswith("landing_pages_")]:
        p = path_of(k); c, f = mig(k); e = elem_of(k)
        im = ELEM[e][0] if e else "drt-carpet"
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        h1 = (EXT[k]["heads"][0][1] if EXT[k]["heads"] and EXT[k]["heads"][0][0] == "h1" else t0)
        out.append(theme(K.page(p, html.escape(t0[:36]), html.escape(h1), "Available 24/7 &middot; 385-287-6344", "Service area", title_of(k),
                                meta_of(k, f"{t0}: water, fire, smoke and mold restoration from Disaster Repair Team, available 24/7. Insurance documentation support."),
                                c, image=im, alt="Disaster Repair Team job photo", crumbs=[("Areas", "landing-pages/")], faqs=f, canonical=EXT[k]["canon"] or None,
                                schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": t0, "provider": {"@id": U + "#business"}}]), e))
    return out


def blog_pages():
    out, cards = [], []
    for i, k in enumerate([k for k in EXT if k.startswith("blog_")]):
        p = path_of(k); c, f = mig(k)
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        im = ["drt-ceiling", "drt-carpet", "drt-mold-corner", "drt-ceiling", "drt-carpet", "drt-mold"][i % 6]
        pg = K.page(p, html.escape(t0[:36]), html.escape(EXT[k]["heads"][0][1] if EXT[k]["heads"] else t0), f"From the {NAME} blog", "Blog", title_of(k),
                    meta_of(k, f"{t0}: from the Disaster Repair Team blog on water, fire, smoke and mold damage in Utah."), c, image=im, alt="", crumbs=[("Blog", "blog/")], faqs=f,
                    canonical=EXT[k]["canon"] or None, ogtype="article")
        pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
        pg["schema"].append({"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": t0, "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)})
        out.append(pg); cards.append((t0, p, im))
    return out, cards


def contact_page():
    info = f'''<p class="answer">Active damage? Call 385-287-6344 now. For contained damage, callbacks and estimates, use the form, and the team will follow up as quickly as possible.</p>
<div class="locs"><div class="loc"><span class="label">Northern Utah &middot; 24/7</span><a class="lp" href="tel:+13852876344">385-287-6344</a></div><div class="loc"><span class="label">Southern Utah (St. George)</span><a class="lp" href="tel:+14356199594">435-619-9594</a></div></div>
<h2>What to include</h2><ul class="ticks"><li>City and property location</li><li>Damage type and whether it&rsquo;s still active</li><li>When the damage started</li><li>Whether an insurance claim is already open</li></ul>
<dl class="info"><div><dt>Office</dt><dd>45 South 2920 West<br>Lehi, UT 84043</dd></div><div><dt>Hours</dt><dd>Available 24/7</dd></div></dl>'''
    pg = K.page("request-help/", "Request Help", "Request Help or an Estimate", "Share a few details and the team will follow up as quickly as possible.", "Contact", title_of("request_help"),
                meta_of("request_help", "Request help or a free estimate from Disaster Repair Team in Lehi, UT. Active damage? Call 385-287-6344, available 24/7. St. George: 435-619-9594."),
                info, canonical=EXT["request_help"]["canon"] or None, form_side=True)
    sel = "".join(f"<option>{o}</option>" for o in ["Water damage", "Fire damage", "Smoke damage", "Mold remediation", "Foundation repair", "Insulation services", "Commercial emergency response", "Other restoration help"])
    form = f'''<form class="form" method="post" action=""><h3>Request help</h3>
<div class="row"><label for="f-name">Full name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone number *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label><label for="f-city">City<input id="f-city" name="city"></label></div>
<div class="row"><label for="f-svc">Service needed *<select id="f-svc" name="service" required><option value="">Select one</option>{sel}</select></label><label for="f-claim">Insurance claim open?<select id="f-claim" name="claim"><option value="">Select one</option><option>Yes, claim already open</option><option>No, not yet filed</option><option>Not sure</option></select></label></div>
<label for="f-msg">What happened?<textarea id="f-msg" name="message"></textarea></label><button class="btn" type="submit">Submit Request {ARROW}</button></form>'''
    pg["body"] = re.sub(r'<div class="form-col">.*?</form>', '<div class="form-col">' + form, pg["body"], count=1, flags=re.S)
    return pg


def generic(k, h1, tag, image=None, extra=""):
    c, f = mig(k)
    return K.page(path_of(k), html.escape(h1[:36]), html.escape(h1), None, tag, title_of(k), meta_of(k, f"{h1}: Disaster Repair Team, water, fire, smoke and mold restoration in Lehi and across Utah."),
                  extra + c, image=image, alt="", faqs=f, canonical=EXT[k]["canon"] or None)


def make_pages():
    posts, cards = blog_pages()
    cards.insert(0, (p_blog.POST[0], p_blog.POST[1], "drt-ceiling"))
    bl = "".join(f'<a class="post-card" href="@/{p}">{img(im, "")}<b>{html.escape(t)}</b><em>Read {ARROW}</em></a>' for t, p, im in cards)
    blog = K.page("blog/", "Blog", "Utah Restoration Blog", "Water, fire, smoke and mold damage, explained for Utah homes.", "Blog", title_of("blog"),
                  meta_of("blog", "The Disaster Repair Team blog: water damage, insurance, hidden leaks, spring storms and what to do first after damage in a Utah home."), f'<div class="posts">{bl}</div>',
                  canonical=EXT["blog"]["canon"] or None)
    svc_grid = '<div class="svc-cards">' + "".join(f'<a class="svc-card el-{e}" href="@/{path_of(k)}"><span class="dot"></span><b>{LABEL[k]}</b><em>{ARROW}</em></a>' for k, e in SVCS.items()) + "</div>"
    roots = [generic("services", "Restoration, Foundation & Insulation Services", "Services", "drt-carpet", svc_grid), generic("about_us", "About Disaster Repair Team", "About", "drt-mold-corner"),
             generic("landing_pages", "Find Restoration Help in Your Area", "Areas", "drt-ceiling")]
    out = [home_v3.home(steps_of)] + svc_pages() + landing_pages() + posts + [p_blog.page(K), blog, contact_page()] + roots + \
          [K.notfound((("Water damage", "water-damage-cleanup-restoration/"), ("Areas", "landing-pages/"), ("Request help", "request-help/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 385-287-6344, 24/7.", " Available 24/7.")) for x in out]
