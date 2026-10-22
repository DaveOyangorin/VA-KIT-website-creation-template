"""Pages for the ezelectric.com redesign: "Flip it on".

EZ Electric's name and voice are built on puns about switching things on ("amp up", "bring the spark back"), and their best photo is
landscape lighting glowing at dusk. So the site is dusk-dark with warm light: a full-height night hero, the signature breaker panel
(each breaker one of their own service lines; flip it and the circuit's job lights up, throw the main for all), service "doors" with
their own job photos, the free consult in three steps, and three Google reviews word for word.
References (screenshotted 21 Oct 2026): Flos (light as the object, quiet type, lots of air), Enphase (dusk landscapes, energy
without jargon), Rivian (big confident type on a calm ground). Lutron and Tesla blocked the screenshot. Brand: the EZ Electric red lightning ring logo; EZ red with warm bulb amber.
Same 6 URLs and canonicals plus one new post. Service pages keep their own section titles and text (claims trimmed)."""
import html, json, os, re
from engine import img, canon, faq_html
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from fx import blocks
import home_ez
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CLAIMS = re.compile(r"over 15 years|top-rated|guarantee|certified", re.I)
cta = K.cta


def header():
    return K.header()


def footer():
    f = K.footer()
    return re.sub(r'<span class="flogo"><img[^>]*></span>', '<span class="flogo">' + img("ez-logo-white", "EZ Electric logo") + '</span>', f)


def sections(k):
    """intro paragraphs + (title, paragraph) sections, titles recovered from the page text just before each paragraph."""
    t = EXT[k]["text"]; pos = 0; intro, secs = [], []
    ps = [i for tg, i in blocks(k) if tg == "p" and len(re.sub(r"<[^>]+>", "", i)) > 80]
    for p in ps:
        plain = html.unescape(re.sub(r"<[^>]+>", "", p))
        i = t.find(plain[:60], pos)
        if i < 0: continue
        gap = re.sub(r"\s+", " ", t[pos:i].replace("Schedule Service", "")).strip()
        pos = i + len(plain)
        if CLAIMS.search(plain): plain = " ".join(x for x in re.split(r"(?<=[.!?])\s+", plain) if not CLAIMS.search(x)); p = html.escape(plain)
        title = gap.split(".")[-1].strip() if "." in gap[-120:] else gap[-80:].strip()
        title = re.sub(r"^.*site-main\"> ?", "", title)
        if not secs and (len(title) > 60 or title in ("", html.unescape(EXT[k]["heads"][0][1]))): intro.append(p); continue
        secs.append((title, p))
    if not intro and secs:  # intro copy sits in a text widget, not a <p>: take the page text between the H2 and the first section title
        h2 = html.unescape(next((x for tg, x in EXT[k]["heads"] if tg == "h2"), ""))
        a0 = t.find(h2) + len(h2) if h2 and h2 in t else 0
        b0 = t.find(html.unescape(secs[0][0]), a0)
        chunk = re.sub(r"\s+", " ", t[a0:b0].replace("Schedule Service", "")).strip()
        intro = [html.escape(x.strip()) for x in re.split(r"(?=At EZ Electric, )", chunk) if x.strip()]
    return intro, secs


PAGES = [("residential_services", "residential-services/", "Residential", "Residential Electrical Services in Salt Lake City &amp; Utah County",
          "Residential Electrician Salt Lake City | EZ Electric", "ez-panel-brick", "EZ Electric electricians at a home&rsquo;s electrical panel"),
         ("commercial_services", "commercial-services/", "Commercial", "Commercial Electrical Services for Salt Lake &amp; Utah County Businesses",
          "Commercial Electrician Salt Lake City | EZ Electric", None, ""),
         ("outdoor_specialty_electrical_services", "outdoor-specialty-electrical-services/", "Outdoor &amp; Specialty", "Outdoor &amp; Specialty Electrical Services in Salt Lake City",
          "Outdoor &amp; Specialty Electrician Salt Lake City | EZ Electric", "ez-landscape-lighting", "Landscape lighting on a stone wall at dusk")]
WHY = '''<h2>Why choose us?</h2><ol class="cs-steps in-prose"><li><span>01</span><b>In-person discussion</b><p>A licensed electrician answers your questions and learns your needs, concerns and goals.</p></li>
<li><span>02</span><b>Free in-person consultation</b><p>An on-site inspection of your current system or project, including a safety check and load analysis.</p></li>
<li><span>03</span><b>Zero-cost evaluation</b><p>A detailed outline of the service options that suit you best. No matter what, the consult is on us.</p></li></ol>'''


def svc_pages():
    out = []
    for k, path, lab, h1, title, im, alt in PAGES:
        intro, secs = sections(k)
        h2 = html.unescape(next((x for t, x in EXT[k]["heads"] if t == "h2"), ""))
        h2 = re.sub(r";? ?Quality Work, Guaranteed\.?", "", h2).strip(" ;")
        nav = '<nav class="toc" aria-label="On this page"><p class="label">On this page</p><ol>' + "".join(f'<li><a href="#s{i + 1}">{html.escape(html.unescape(t))}</a></li>' for i, (t, p) in enumerate(secs)) + "</ol></nav>"
        body = (f'<p class="answer">{intro[0]}</p>' if intro else "") + "".join(f"<p>{x}</p>" for x in intro[1:]) + (f"<h2>{html.escape(h2)}</h2>" if h2 else "") + nav + \
            "".join(f'<section class="svc-s" id="s{i + 1}"><span class="svc-n">{i + 1:02d}</span><h3>{html.escape(html.unescape(t))}</h3><p>{p}</p></section>' for i, (t, p) in enumerate(secs)) + WHY
        meta = html.unescape(EXT[k]["meta"] or "")
        if len(meta) > 160: meta = meta[:157].rsplit(" ", 1)[0] + "..."
        out.append(K.page(path, lab, h1, "Free quotes &middot; Monday&ndash;Friday 8 AM&ndash;6 PM &middot; (385) 284-0394", "Services", title, html.escape(meta), body,
                          image=im, alt=alt, art=None if im else '<div class="ph-bolt" aria-hidden="true"></div>', crumbs=[], canonical=EXT[k]["canon"],
                          schema=K.svc_schema(path, html.unescape(lab) + " electrical services", "Salt Lake City, UT")))
    return out


def make_pages():
    out = [home_ez.home()] + svc_pages()
    bl = [b for b in blocks("contact") if b[0] != "li"]
    info = f'''<p class="answer">At EZ Electric, we make it easy to connect. Our team is responsive, professional, and ready to help with everything from quick repairs to full-scale projects. Fill out the form and tell us what you&rsquo;re looking for, or call <a href="tel:+13852840394">(385) 284-0394</a>.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13852840394">(385) 284-0394</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Areas we serve</dt><dd>Utah County &amp; Salt Lake County</dd></div><div><dt>Business hours</dt><dd>Monday &ndash; Friday: 8 AM &ndash; 6 PM<br>Closed Saturdays &amp; Sundays</dd></div></dl>
<h2>Let&rsquo;s get started</h2><p>Whether it&rsquo;s wiring a new home addition, upgrading your commercial lighting, or troubleshooting a tricky outlet, you can count on us to deliver safe, efficient, high-quality electrical work. We&rsquo;re not just here to power homes and businesses. We&rsquo;re here to build long-term relationships based on trust and great service.</p>'''
    out.append(K.page("contact/", "Contact", "Contact EZ Electric", "Planning a remodel, adding an upgrade, or need some electrical maintenance? Our licensed electricians are here to help.", "Request a service or estimate",
                      "Free Electrical Quote Salt Lake &amp; Utah County | EZ Electric",
                      "Request a free electrical quote from EZ Electric in Salt Lake City and Utah County. Call (385) 284-0394 or email info@ezelectric.com, Mon to Fri 8 to 6.",
                      info, canonical=EXT["contact"]["canon"], form_side=True))
    acc = "".join(f"<p>{x}</p>" for t, x in blocks("website_accessibility") if t == "p" and len(x) > 60 and "Copyright" not in x)
    out.append(K.page("website-accessibility/", "Website Accessibility", "Website Accessibility", "", "Legal", "Website Accessibility Statement | EZ Electric, Utah",
                      "EZ Electric's website accessibility statement: our commitment to WCAG guidelines on ezelectric.com, and how to reach us about any accessibility issue.",
                      acc, canonical=EXT["website_accessibility"]["canon"]))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Residential", "residential-services/"), ("Commercial", "commercial-services/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (385) 284-0394.",)) for x in out]
