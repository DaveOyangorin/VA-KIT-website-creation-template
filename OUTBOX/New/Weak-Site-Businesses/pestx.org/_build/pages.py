"""Pages for the pestx.org redesign: "A field guide to the Utah home".

Pestx's own site already thinks like a naturalist: ten Utah pests, each with Identification, Elimination and Prevention, drawn in
ink wash; and a "Full home coverage" diagram lettering seven parts of a house (A Eaves to G Basement). So the redesign is built as a
field guide: specimen plates, numbered field notes, the house diagram as the interactive signature, and a season chart.
References (screenshotted 21 Oct 2026): Audubon (one specimen as hero, magazine restraint), iNaturalist (identification cards,
mono captions, community-science tone), Gardenista (editorial serif, home and garden photography with generous white space).
Brand kept: Pestx plum #82234C and the round X mark, the fog ground #F2F3F0, and the site's own fonts (Libre Baskerville, Manrope,
Fragment Mono). Same 18 URLs (no trailing slash) and canonicals, plus one new post (blogs/ticks-in-utah)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon, crumbs_ld
from cfg import U, NAME, HERE, PESTS, INK, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from fx import blocks
import home_px
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
MARK = open(os.path.join(HERE, "src", "pestx-mark.svg"), encoding="utf-8").read().replace('width="64" height="64"', 'viewBox="0 0 64 64" aria-hidden="true"')
NAMES = {s: n for s, n, t in PESTS}
ZONES_OF = {}
for l, n, x, y, ps in home_px.ZONES:
    for s, t in ps: ZONES_OF.setdefault(s, []).append((l, n))


def header():
    h = K.header()
    return re.sub(r'(<a class="brand"[^>]*>)<img[^>]*>(</a>)', lambda m: m.group(1) + MARK + '<span class="wm">Pestx</span>' + m.group(2), h)


def footer():
    f = K.footer()
    return re.sub(r'<span class="flogo"><img[^>]*></span>', '<span class="flogo">' + MARK + '<span class="wm">Pestx</span></span>', f)


cta = K.cta


def render(bl, skip_h1=True):
    """client blocks -> html: list items grouped, bold-only paragraphs become h2, h2 -> h2, h3 kept."""
    out, ul = [], []
    def flush():
        if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul.clear()
    for tag, inner in bl:
        if tag == "li": ul.append(inner); continue
        flush()
        if tag == "h1" and skip_h1: continue
        if tag == "p" and re.fullmatch(r"<strong>[^<]{2,90}</strong>", inner): out.append(f"<h2>{re.sub(r'</?strong>', '', inner)}</h2>"); continue
        if tag in ("h1", "h2", "h4"): tag = "h2"
        out.append(f"<{tag}>{inner}</{tag}>")
    flush()
    return "\n".join(out)


def plate(s, n, tax, i):
    return f'''<figure class="ph-plate">{img(INK[s], f"Ink drawing of {n.lower()}", priority=True, lazy=False)}<figcaption><span>Plate {i + 1:02d} / 10</span><b>{n}</b><i>{tax}</i></figcaption></figure>'''


def pest_pages():
    out = []
    for i, (s, n, tax) in enumerate(PESTS):
        k = "pests_" + s.replace("-", "_")
        bl = [b for b in blocks(k) if b[1] != "Back"]
        summary = next(x for t, x in bl if t == "p")
        rest = [b for b in bl if b[1] != summary]
        when, where = home_px.SEEN[s]
        notes = f'''<dl class="fn"><div><dt>Seen</dt><dd>{when}</dd></div><div><dt>Where</dt><dd>{where}</dd></div><div><dt>Order</dt><dd>{tax}</dd></div></dl>'''
        zones = ZONES_OF.get(s, [])
        zhtml = ("<h2>Where it shows up in your home</h2><ul class=\"chips\">" + "".join(f'<li><a href="@/#coverage">Zone {l} &middot; {z}</a></li>' for l, z in zones) + "</ul>") if zones else ""
        others = [(s2, n2) for s2, n2, t2 in PESTS if s2 != s]
        more = '<h2>More Utah pests</h2><div class="more-pests">' + "".join(f'<a href="@/pests/{s2}/">{img(INK[s2], "")}<span>{n2}</span></a>' for s2, n2 in others) + "</div>"
        body = notes + render(rest) + zhtml + more
        title = f"{n} in Utah: Identify, Eliminate, Prevent | Pestx"
        if len(title) > 60: title = f"{n} in Utah: Identification and Prevention | Pestx"
        if len(title) > 60: title = f"{n} in Utah | Pestx Pest Control, Midvale"
        meta = html.unescape(summary)
        meta = meta if 120 <= len(meta) <= 160 else (meta[:157].rsplit(" ", 1)[0] + "..." if len(meta) > 160 else meta + " Pestx, Midvale.")
        out.append(K.page(f"pests/{s}/", n, n, html.unescape(summary) and summary, "Common Utah pests", html.escape(title), html.escape(meta), body,
                          art=plate(s, n, tax, i), crumbs=[("Utah pests", "pests/")], canonical=EXT[k]["canon"],
                          schema=[{"@type": "Article", "@id": canon(f"pests/{s}/") + "#article", "headline": f"{n}: identification, elimination and prevention in Utah",
                                   "about": n, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(f"pests/{s}/")}]))
    return out


def blog_pages():
    out = []
    for slug, key in (("is-pest-control-safe-for-pets", "blogs_is_pest_control_safe_for_pets"), ("how-bugs-get-inside-your-home", "blogs_how_bugs_get_inside_your_home"),
                      ("does-one-spray-work-for-most-bugs", "blogs_does_one_spray_work_for_most_bugs")):
        bl = [b for b in blocks(key) if b[1] not in ("Back", "Feb 1, 2025")]
        h1 = next(x for t, x in bl if t == "h1")
        summary = next(x for t, x in bl if t == "p")
        body = f'<p class="answer">{summary}</p>' + render([b for b in bl if b[1] != summary]) + \
            f'<p>Questions about pests in your home? Call Pestx at <a href="tel:+18018719233">801-871-9233</a> or see the <a href="@/pests/">Utah pest field guide</a>.</p>'
        title = html.unescape(h1) + " | Pestx Pest Control Blog"
        if len(title) > 60: title = html.unescape(h1) + " | Pestx Blog"
        meta = html.unescape(summary)
        if len(meta) > 160: meta = meta[:157].rsplit(" ", 1)[0] + "..."
        p = f"blogs/{slug}/"
        out.append(K.page(p, html.unescape(h1), h1, "Natural pest control solutions &middot; Feb 1, 2025", "Blog", html.escape(title), html.escape(meta), body,
                          art=None, crumbs=[("Blog", "blogs/")], canonical=EXT[key]["canon"], ogtype="article",
                          schema=[{"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": html.unescape(h1), "datePublished": "2025-02-01",
                                   "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)}]))
    out.append(p_blog.page(K))
    cards = "".join(f'<a class="nb-card" href="@/{p}"><span class="fg-no">{d}</span><b>{t}</b><p>{x}</p><em>Read {ARROW}</em></a>' for p, t, d, x in home_px.POSTS)
    out.append(K.page("blogs/", "Blog", "Natural Pest Control Solutions", "Knowledge for keeping a safe, healthy and protected home.", "Blog",
                      "Natural Pest Control Solutions: Blog | Pestx, Midvale UT",
                      "The Pestx blog: natural pest control tips for Utah homes, from keeping pets safe and sealing entry points to dealing with ticks after a long Wasatch hike.",
                      f'<div class="nb nb-list">{cards}</div>', art=f'<figure class="ph-plate">{img("ink-leaf", "Ink drawing of a leaf", priority=True, lazy=False)}</figure>',
                      canonical=EXT["blogs"]["canon"]))
    return out


def root_pages():
    out = []
    out.append(K.page("pests/", "Utah pests", "Common Utah Pests", "How to identify Utah&rsquo;s most common pests and avoid individual pest problems.", "Field guide",
                      "Common Utah Pests: A Field Guide | Pestx, Midvale UT",
                      "A field guide to common Utah pests: mosquitoes, ants, spiders, rodents, wasps, beetles, flies, moths, snails and grasshoppers, and how to prevent them.",
                      '<p class="answer">Ten pests Utah homes and yards see most. Each page covers identification, elimination and prevention.</p>' + home_px.guide_grid("fg-grid in-page"),
                      art=f'<figure class="ph-plate">{img("ink-mountains", "Ink drawing of the Wasatch mountains", priority=True, lazy=False)}</figure>', canonical=EXT["pests"]["canon"]))
    info = f'''<p class="answer">You can contact us by email, by phone, or with the form on this page. We strive to respond promptly and look forward to connecting with you.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18018719233">+1-801-871-9233</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd><address>661 W 7250 S<br>Midvale, UT 84047</address></dd></div><div><dt>Service area</dt><dd>Midvale and the Greater Salt Lake Area</dd></div></dl>
<h2>What happens next</h2><p>Tell us what you&rsquo;re seeing and where: the pest, the room or part of the yard, and how long it&rsquo;s been going on. Our pest pages can help you <a href="@/pests/">identify it</a> first.</p>'''
    out.append(K.page("contact/", "Contact", "Contact Pestx", "Get a quote for pest control in Midvale and the Greater Salt Lake Area.", "Contact us",
                      "Contact Pestx | Pest Control Quote in Midvale, Utah",
                      "Contact Pestx for a pest control quote in Midvale and the Greater Salt Lake Area: call +1-801-871-9233, email office@pestx.org or use the form.",
                      info, canonical=EXT["contact"]["canon"], form_side=True))
    bl = blocks("privacy_policy")
    date = bl[0][1] if re.match(r"\d", bl[0][1]) else ""
    body = (f'<p class="small">Last updated {date}</p>' if date else "") + render([b for b in bl if b[1] != date])
    out.append(K.page("privacy-policy/", "Privacy Policy", "Privacy Policy", "", "Legal", "Privacy Policy | Pestx Pest Control, Midvale, Utah",
                      "Pestx privacy policy: what information we collect on www.pestx.org, how we use and share it, SMS program terms, cookies and your privacy rights.",
                      body, crumbs=[], canonical=EXT["privacy_policy"]["canon"]))
    return out


def make_pages():
    out = [home_px.home()] + pest_pages() + blog_pages() + root_pages() + \
          [K.notfound((("Utah pests", "pests/"), ("Blog", "blogs/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-871-9233.", " Pestx, Midvale.")) for x in out]
