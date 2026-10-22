import re, html
from build import (U, BIZ_ID, S, ARROW, PHONE, IMG, IMGMAP, img, crumbs_ld, faq_ld, faq_html, cta, side, phero, quote_form)
import p_home, p_blog

SHINGLE_COLORS = [("Matte Black", "#43464d"), ("Brick Red", "#7d2912"), ("Brown Stone", "#957271"), ("Classic Green", "#598979"),
                  ("Copper Penny", "#ad7c55"), ("Granite Gray", "#747474"), ("Sierra Tan", "#9d7c67"), ("Polar White", "#f2f2f0")]


def swatches():
    return '<div class="swatches">' + "".join(
        f'<div class="swatch"><i style="background-color:{c}"></i><b>{n}</b><small>Aluminum shingle color</small></div>' for n, c in SHINGLE_COLORS) + "</div>"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def clean(body):
    body = re.sub(r"^<ul><li><a href=\"mailto:[^<]*</a></li><li><a href=\"tel:[^<]*</a></li></ul>", "", body)  # header contact strip
    body = body.replace("https://aluminumlockroofing.com/", "@/")
    return body


def faqs_from(body):
    out = []
    for q, a in re.findall(r"<h2>(.*?)</h2>(.*?)(?=<h2>|$)", body, flags=re.S):
        out.append((plain(q), a.strip()))
    intro = re.split(r"<h2>", body, 1)[0]
    return intro, out


def make_pages(ex):
    recs = {("" if r["file"] == "home.html" else r["file"][:-5] + "/"): r for r in ex}
    pages = []

    # home
    r = recs[""]
    home = {"path": "", "canonical": U, "modified": None}
    home.update(p_home.build(r, swatches()))
    pages.append(home)

    # services (the client's text, plus facts from their own home and about pages)
    r = recs["services/"]
    url = U + "services/"
    trail = [("Home", ""), ("Aluminum Shingle Roof Installation", "services/")]
    gallery = "".join(f'<figure class="snap">{img(n, a)}<figcaption>{c}</figcaption></figure>' for n, a, c in [
        ("green-aluminum-shingle-log-home", "Log home with a classic green aluminum shingle roof", "Classic Green on a log home"),
        ("brick-red-aluminum-shingle-stone-cottage", "Stone cottage with a brick-red aluminum shingle roof", "Brick Red over stone"),
        ("gray-aluminum-shingle-two-story-home", "Two-story home with a gray aluminum shingle roof", "Granite Gray, two-story home")])
    body = f'''
<div class="answer">Aluminum Lock Roofing installs interlocking aluminum shingle roofs on homes in Salt Lake City and other locations we serve. Contact us to discuss your project and confirm installation availability for your location.</div>
<h2>Plan your roof installation</h2>
<p>Start with your project location, current roof type and what you want to accomplish. The roof's condition, slope and details help determine the installation approach. Ask what your estimate includes, from preparation and any necessary removal to materials and finishing details.</p>
<p>A roof-over may be possible on some buildings, but the existing roof, decking and applicable requirements need to be assessed first. Our guide <a href="@/blog/can-you-put-a-new-roof-over-an-old-roof/">can you put a new roof over an old roof?</a> explains what decides it.</p>
<h2>How the interlocking aluminum shingle system works</h2>
<p>Four-sided interlocks connect each shingle to the surrounding shingles. The shingles are one part of the system: underlayment and correctly fitted flashings at eaves, rakes, valleys, walls and penetrations work together to manage water.</p>
<ul>
<li>Interlocking edges help form a connected roofing surface</li>
<li>Concealed attachment details reduce exposed fasteners across the shingle field</li>
<li>Installation details accommodate expansion and contraction</li>
<li>Perimeter flashings help direct water at roof edges and transitions</li>
</ul>
<h2>Why homeowners choose aluminum shingles</h2>
<div class="tablebox"><table><thead><tr><th>Property</th><th>What it means for your roof</th></tr></thead><tbody>
<tr><td>Noncombustible aluminum</td><td>Aluminum doesn't burn. A roof assembly's fire rating depends on all its components and installation, so ask about the requirements for your project.</td></tr>
<tr><td>Rust-free</td><td>Aluminum does not rust like steel. Appropriate finishes, compatible materials and installation details help protect the system over time.</td></tr>
<tr><td>Lightweight</td><td>A lighter roofing option. The roof structure, decking and complete assembly still need to be assessed for each project.</td></tr>
<tr><td>Wind-resistant interlocks</td><td>Interlocking shingles work with underlayment and flashings to shed water and resist wind, when installed correctly.</td></tr>
<tr><td>Shingle-style look</td><td>The classic look of shingles, in eight finish colors.</td></tr>
</tbody></table></div>
<h2>Plan for Salt Lake City's climate</h2>
<p>Every roof faces different conditions. We can discuss the roof assembly and installation details appropriate for your location, including:</p>
<ul><li>Snow loads and safe snow-shedding details</li><li>Local wind requirements and fastening details</li><li>Finish selection and exposure conditions</li><li>Thermal movement and moisture management</li><li>Roof color, ventilation and thermal performance</li></ul>
<h2>Aluminum shingle colors</h2>
{swatches()}
<p style="margin-top:14px;font-size:.9rem;color:var(--steel)">Colors shown on screen are approximate. Ask to see the finish options for your project.</p>
<h2>Recent aluminum shingle roofs</h2>
<div class="snaps">{gallery}</div>
<h2 id="materials">Roofing materials for contractors</h2>
<p>We also sell aluminum roofing materials to roofers. Contact us with your project location and approximate quantities to discuss product options, required components and ordering arrangements.</p>
<p><a class="btn navy" href="tel:{S["tel"]}">{PHONE} Call about roofing materials</a></p>
<h2>Ask about warranty terms</h2>
<p>Ask for the applicable written warranty before choosing a roofing system. Review its coverage, exclusions and maintenance requirements, and confirm which terms apply to your materials and installation.</p>
'''
    pages.append({"path": "services/", "canonical": url,
                  "title": "Aluminum Shingle Roofing in Salt Lake City | Aluminum Lock",
                  "meta": "Interlocking aluminum shingle roof installation in Salt Lake City from Aluminum Lock Roofing, plus aluminum roofing materials for roofers. Call (801) 484-3321.",
                  "og": "green-aluminum-shingle-log-home",
                  "body": phero(trail, "Aluminum Shingle Roof Installation in Salt Lake City", "Interlocking aluminum shingle roofs, installed, plus materials for roofing professionals.",
                                "gray-aluminum-shingle-two-story-home", "Home with an aluminum shingle roof", "Services")
                          + f'<section class="sec"><div class="wrap layout"><article class="prose">{body}</article>{side([("About us", "about-us/"), ("Roofing FAQ", "faq/"), ("Roof over an old roof?", "blog/can-you-put-a-new-roof-over-an-old-roof/"), ("Contact", "contact-us/")])}</div></section>' + cta(),
                  "schema": [crumbs_ld(url, trail),
                             {"@type": "Service", "@id": url + "#service", "name": "Aluminum Shingle Roof Installation", "url": url, "provider": {"@id": BIZ_ID},
                              "description": "Installation of interlocking aluminum shingle roofing systems.", "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}},
                             {"@type": "Service", "@id": url + "#materials", "name": "Aluminum Roofing Materials for Roofers", "url": url + "#materials", "provider": {"@id": BIZ_ID},
                              "description": "Supply of aluminum shingle roofing systems and components to roofing contractors."}],
                  "full_biz": True})

    # about
    r = recs["about-us/"]; url = U + "about-us/"
    trail = [("Home", ""), ("About Us", "about-us/")]
    body = '<div class="answer">Aluminum Lock Roofing is a Salt Lake City roofing company that specializes in interlocking aluminum shingle roofing. We manufacture and supply aluminum roofing systems, install aluminum shingle roofs, and sell roofing materials to roofers.</div>' + re.sub(r"^<p>.*?</p>", "", clean(r["body"]), count=1)
    pages.append({"path": "about-us/", "canonical": url,
                  "title": "About Aluminum Lock Roofing | Salt Lake City Aluminum Roofs",
                  "meta": "Aluminum Lock Roofing specializes in interlocking aluminum shingle roofing in Salt Lake City: we manufacture, supply and install, and sell materials to roofers.",
                  "og": "copper-aluminum-shingle-cabin",
                  "body": phero(trail, "About Aluminum Lock Roofing", "A Salt Lake City company focused on one thing: interlocking aluminum shingle roofs.",
                                "copper-aluminum-shingle-cabin", "Cabin with a copper-colored aluminum shingle roof", "About us")
                          + f'<section class="sec"><div class="wrap layout"><article class="prose">{body}</article>{side([("Services", "services/"), ("FAQ", "faq/"), ("Contact", "contact-us/")])}</div></section>' + cta(),
                  "schema": [crumbs_ld(url, trail), {"@type": "AboutPage", "@id": url + "#page", "url": url, "name": "About Aluminum Lock Roofing", "about": {"@id": BIZ_ID}}],
                  "full_biz": True})

    # FAQ
    r = recs["faq/"]; url = U + "faq/"
    intro, faqs = faqs_from(clean(r["body"]))
    trail = [("Home", ""), ("FAQ", "faq/")]
    pages.append({"path": "faq/", "canonical": url,
                  "title": "Aluminum Shingle Roofing FAQ | Aluminum Lock Roofing",
                  "meta": "Answers about Aluminum Lock Roofing's interlocking aluminum shingles: how the system works, roof-overs, warranties, estimates and materials for roofers.",
                  "og": "green-aluminum-shingle-commercial-mountains",
                  "body": phero(trail, "Aluminum Shingle Roofing FAQ", "Common questions about our roofs, installation and buying materials.",
                                "green-aluminum-shingle-commercial-mountains", "Commercial building with a green aluminum shingle roof below snowy mountains", "FAQ")
                          + f'<section class="sec"><div class="wrap layout"><article class="prose">{intro}{faq_html(faqs)}<p style="margin-top:24px">More detail on roof-overs: <a href="@/blog/can-you-put-a-new-roof-over-an-old-roof/">can you put a new roof over an old roof?</a></p></article>{side([("Services", "services/"), ("About us", "about-us/"), ("Contact", "contact-us/")])}</div></section>' + cta(),
                  "schema": [crumbs_ld(url, trail), faq_ld(faqs)], "full_biz": False})

    # contact
    url = U + "contact-us/"; trail = [("Home", ""), ("Contact", "contact-us/")]
    body = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">
<h2>Tell us about your project</h2><p>Planning an aluminum shingle roof installation? Call or email us to discuss your project. We also supply aluminum roofing materials to roofers.</p>
<p>When you call or email, please include:</p><ul><li>Your project location</li><li>Your current roof type</li><li>Whether you need roof installation or roofing materials</li></ul>
<p>For installation, tell us what you would like to accomplish. If you are buying materials, include the products and approximate quantities you need.</p>
<div class="pillars" style="grid-template-columns:1fr;margin-top:20px">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Phone</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a></p></div></div>
<div class="pillar"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><div><h3>Email</h3><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div></div>
</div></div><div>{quote_form()}</div></div></section>'''
    pages.append({"path": "contact-us/", "canonical": url,
                  "title": "Contact Aluminum Lock Roofing | Salt Lake City, UT",
                  "meta": "Contact Aluminum Lock Roofing in Salt Lake City about an aluminum shingle roof or materials for roofers. Call (801) 484-3321 or send us an email today.",
                  "og": "gray-aluminum-shingle-two-story-home",
                  "body": phero(trail, "Contact Aluminum Lock Roofing", "Call or email to discuss an installation or a materials order.",
                                "red-aluminum-shingle-white-home", "White home with a red aluminum shingle roof", "Contact") + body,
                  "schema": [crumbs_ld(url, trail), {"@type": "ContactPage", "@id": url + "#page", "url": url, "name": "Contact Aluminum Lock Roofing", "about": {"@id": BIZ_ID}}],
                  "full_biz": True})

    # privacy policy: the current page is only a placeholder; kept, but out of the index until real text exists
    url = U + "privacy-policy/"; trail = [("Home", ""), ("Privacy Policy", "privacy-policy/")]
    pages.append({"path": "privacy-policy/", "canonical": url, "title": "Privacy Policy | Aluminum Lock Roofing",
                  "meta": "Privacy policy for Aluminum Lock Roofing.", "robots": "noindex, follow", "sitemap": False,
                  "body": phero(trail, "Privacy Policy", "", "matte-black-aluminum-shingle-home", "Aluminum shingle roof", "Legal")
                          + f'<section class="sec"><div class="wrap prose"><p>[[NEEDS: privacy policy text from the client. The current page only says the site is being updated.]]</p><p>Questions? Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or email <a href="mailto:{S["email"]}">{S["email"]}</a>.</p></div></section>',
                  "schema": [crumbs_ld(url, trail)], "full_biz": False})

    pages += p_blog.pages()
    pages.append({"path": "404.html", "title": "Page Not Found | Aluminum Lock Roofing", "meta": "That page doesn't exist.", "canonical": None,
                  "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn't here", "Try the home page or contact us.",
                                "matte-black-aluminum-shingle-home", "Aluminum shingle roof", "Error 404")})
    return pages, {"?elementskit_template=header": "", "metform-form/new-form-1768995728/": ""}
