"""Pages for the roofrepairsaltlakecity.com redesign: "the repair manual".

Home and the blog post are written by hand. The 17 other real pages keep the client's own text (cleaned out of the old theme),
with a new title, meta, H1 and opening paragraph that name Salt Lake City (report, 17 Oct 2026). Paragraphs with unsupported
claims are dropped (see DROP below and the notes): "best/leader/top/most respected", "100 percent satisfaction", "hundreds of
households", the Wall Street Journal and 62% statistics, "certified installers", "licensed as residential, commercial...",
"24/7", guarantees, the Oak Ridge savings estimates, and the theme's sample testimonial.
Not rebuilt (301s in the notes): the theme demo pages /clients/wpml/, /clients/jquery/, /clients/microlancer/, /clients/envato/
and /testimonials/john-doe/.
"""
import json, os, re, html
import engine as E
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, AREAS, NAME, U, HERE
from clean import clean_main
from illus import fig_house, swatch, SPOTS
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CONTACT = "contact-us/"
HOME = ("Home", "")

# key, path, nav label, code, swatch, target phrase, title, meta, h1, opening paragraph
SVC = [
 ("utah_roof_repair", "utah-roof-repair/", "Roof Repair", "RR-01", "shingle", "Roof Repair Services in Salt Lake City | Roof Repair SLC",
  "Residential roof repair in Salt Lake City and across Utah: leaks, storm and hail damage, flashing and worn shingles. Roofing since 2005. Free estimates.",
  "Residential Roof Repair in Salt Lake City", "Roof Repair Salt Lake City repairs home roofs in Salt Lake City and nearby Utah cities: leaks, storm and hail damage, tree damage, worn flashing and damaged shingles. We have been roofing since 2005, and every repair starts with a free evaluation of what caused the problem."),
 ("roof_replacement", "roof-replacement/", "Roof Replacement", "RR-02", "shingle", "Roof Replacement in Salt Lake City | Roof Repair SLC",
  "Roof replacement in Salt Lake City for homes and commercial buildings: tear-offs, re-roofs and new roofs. Free evaluation and quote. Call (385) 355-4849.",
  "Roof Replacement in Salt Lake City", "Roof Repair Salt Lake City replaces roofs on homes and commercial buildings in Salt Lake City: tear-offs, re-roofs and new construction. Below is how to choose a roofing contractor for a replacement, and what to check before you sign."),
 ("utah_metal_roofing", "utah-metal-roofing/", "Metal Roofing", "RR-03", "metal", "Metal Roofing in Salt Lake City, UT | Roof Repair SLC",
  "Metal roofing in Salt Lake City: standing seam and sheet metal roofs installed and repaired for homes and businesses, plus custom sheet metal fabrication.",
  "Metal Roofing in Salt Lake City", "Roof Repair Salt Lake City installs and repairs metal roofing in Salt Lake City for homes and commercial buildings, including standing seam systems and sheet metal roofing, with custom sheet metal fabrication when a job needs it."),
 ("asphalt_shingle_roofing", "asphalt-shingle-roofing/", "Asphalt Shingles", "RR-04", "shingle", "Asphalt Shingle Roofing in Salt Lake City | Roof Repair",
  "Asphalt shingle roofing in Salt Lake City: repair, installation and replacement with 20- to 40-year shingles from major manufacturers. Free estimates.",
  "Asphalt Shingle Roofing in Salt Lake City", "Roof Repair Salt Lake City repairs, installs and replaces asphalt shingle roofs in Salt Lake City. Shingles are the most common roof on homes here, and they come in grades from 20-year to 40-year products."),
 ("commercial_roofing", "commercial-roofing/", "Commercial Roofing", "RR-05", "tpo", "Commercial Roofing in Salt Lake City, UT | Roof Repair",
  "Commercial roofing in Salt Lake City: overlays, tear-offs, repairs and new roofs for commercial buildings, with TPO, metal and ballasted systems.",
  "Commercial Roofing in Salt Lake City", "Roof Repair Salt Lake City handles commercial roofing in Salt Lake City: overlays on existing roofs, tear-offs, repairs and new roofs on commercial buildings."),
 ("flat_roof_repair", "flat-roof-repair/", "Flat Roof Repair", "RR-06", "membrane", "Flat Roof Repair in Salt Lake City | Roof Repair SLC",
  "Flat roof repair in Salt Lake City for homes and commercial buildings: low-slope leaks, membranes and moisture checks before repair or replacement.",
  "Flat Roof Repair in Salt Lake City", "Roof Repair Salt Lake City repairs flat and low-slope roofs in Salt Lake City on homes and commercial buildings. A sound flat roof can often be repaired instead of replaced, once moisture and structure have been checked."),
 ("commercial_roof_repair", "commercial-roof-repair/", "Commercial Roof Repair", "RR-07", "membrane", "Commercial Roof Repair in Salt Lake City | Roof Repair",
  "Commercial roof repair in Salt Lake City for offices, retail and industrial buildings: leaks, membranes, flashing and drains. Call (385) 355-4849.",
  "Commercial Roof Repair in Salt Lake City", "Roof Repair Salt Lake City repairs commercial roofs in Salt Lake City: leaks, membrane damage, flashing, drains and the other problems that put a building and its tenants at risk."),
 ("commercial_roof_replacement", "commercial-roof-replacement/", "Commercial Roof Replacement", "RR-08", "tpo", "Commercial Roof Replacement in Salt Lake City | Roof Repair",
  "Commercial roof replacement in Salt Lake City: re-roofs and new installations for older buildings, new construction, remodels and retrofits.",
  "Commercial Roof Replacement in Salt Lake City", "Roof Repair Salt Lake City replaces and re-roofs commercial buildings in Salt Lake City, on older buildings, new construction, remodels and retrofits."),
 ("commercial_roofing_systems", "commercial-roofing-systems/", "Commercial Roofing Systems", "RR-09", "ballast", "Commercial Roofing Systems in Salt Lake City | Roof Repair",
  "Commercial roofing systems in Salt Lake City for commercial, industrial and institutional buildings: TPO, EPDM, metal, ballasted and more. Free quotes.",
  "Commercial Roofing Systems in Salt Lake City", "Roof Repair Salt Lake City bids and installs roofing systems for commercial, industrial and institutional buildings in Salt Lake City. The right system depends on the building, its use and its budget."),
 ("commercial_tpo_roofing_systems", "commercial-tpo-roofing-systems/", "Commercial TPO", "RR-10", "tpo", "Commercial TPO Roofing in Salt Lake City | Roof Repair SLC",
  "Commercial TPO roofing systems in Salt Lake City: white heat-welded membrane roofs installed, repaired and replaced on commercial buildings.",
  "Commercial TPO Roofing Systems in Salt Lake City", "Roof Repair Salt Lake City installs, repairs and replaces commercial TPO roofing systems in Salt Lake City: white single-ply membranes with heat-welded seams for flat and low-slope commercial roofs."),
 ("tpo_roofing_membrane", "tpo-roofing-membrane/", "TPO Membrane", "RR-11", "tpo", "TPO Roofing Membrane in Salt Lake City | Roof Repair SLC",
  "TPO roofing membrane in Salt Lake City for homes and businesses: white, heat-welded single-ply roofing for flat and low-slope roofs. Free estimate.",
  "TPO Roofing Membrane in Salt Lake City", "Roof Repair Salt Lake City installs and repairs TPO roofing membrane in Salt Lake City on homes and commercial buildings with flat or low-slope roofs."),
 ("waterproof_roofing_services", "waterproof-roofing-services/", "Waterproof Roofing", "RR-12", "membrane", "Waterproof Roofing in Salt Lake City | Roof Repair SLC",
  "Waterproof roofing and roof restoration in Salt Lake City for homes and businesses: sealing, flashing and membranes that keep rain and snowmelt out.",
  "Waterproof Roofing in Salt Lake City", "Roof Repair Salt Lake City provides waterproof roofing and restoration in Salt Lake City for homes and businesses, so rain, hail and winter storms stay on the outside of the roof."),
 ("residential_tile_roofing", "residential-tile-roofing/", "Tile Roofing", "RR-13", "tile", "Tile Roofing in Salt Lake City, UT | Roof Repair SLC",
  "Residential tile roofing in Salt Lake City: clay and concrete tile roofs repaired, installed and replaced. Call Roof Repair Salt Lake City for an estimate.",
  "Residential Tile Roofing in Salt Lake City", "Roof Repair Salt Lake City repairs, installs and replaces residential tile roofs in Salt Lake City, in clay and concrete tile."),
 ("residential_wood_roofing", "residential-wood-roofing/", "Wood Roofing", "RR-14", "wood", "Wood Shake Roofing in Salt Lake City | Roof Repair SLC",
  "Residential wood roofing in Salt Lake City: cedar shake and wood shingle roofs repaired and replaced, with treated wood for longer life. Free estimates.",
  "Residential Wood Roofing in Salt Lake City", "Roof Repair Salt Lake City repairs and replaces wood shake and wood shingle roofs on homes in Salt Lake City."),
 ("roofing_insurance_claims_assistance", "roofing-insurance-claims-assistance/", "Insurance Claims", "RR-15", "shingle", "Roof Insurance Claims Help in Salt Lake City | Roof Repair",
  "Roofing insurance claims assistance in Salt Lake City: a free on-site evaluation, then help documenting storm and hail damage for your insurer.",
  "Roofing Insurance Claims Assistance in Salt Lake City", "Roof Repair Salt Lake City helps Salt Lake City homeowners and property owners with roofing insurance claims, starting with a free on-site evaluation to see whether damage occurred and how much."),
]
DROP = re.compile(r"\bbest\b|leader in|top roofing|most respected|highly qualified|impeccable|stellar|hundreds of|100 percent|Wall Street Journal|62%|astronomical|"
                  r"certified installers|licensed as|licensed and certified|long-term employees|24/7|guarantee|Oak Ridge|for many years|for a long time|nothing that surprises|"
                  r"Sales Representative|perfect blend|extreme satisfaction|top quality|superior", re.I)


def migrate(key):
    d = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))[key]
    raw = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    h, h1, _ = clean_main(raw, d["url"])
    blocks = re.findall(r"<(h2|h3|p|ul|ol|blockquote)>(.*?)</\1>", h, re.S)
    out = []
    for tag, inner in blocks:
        txt = re.sub(r"<[^>]+>", "", inner)
        if DROP.search(txt) or len(txt.strip()) < 3: continue
        if tag in ("h2", "h3"): inner = re.sub(r"</?(strong|b)>", "", inner)
        out.append(f"<{tag}>{inner}</{tag}>")
    s = "\n".join(out)
    s = re.sub(r'href="https?://(?:www\.)?roofrepairsaltlakecity\.com/?([^"#]*?)/?"', lambda m: f'href="@/{m.group(1)}/"' if m.group(1) else 'href="@/"', s)
    s = s.replace('href="@//"', 'href="@/"')
    s = re.sub(r'<a href="(?!@/|https?://|tel:|mailto:)[^"]*">(.*?)</a>', r"\1", s)
    return s


def header():
    nav = "".join(f'<a href="@/{p}"><span class="mono">{c}</span>{n}</a>' for k, p, n, c, *_ in SVC)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home"><span class="bm">RR</span><span class="bt">Roof Repair<br>Salt Lake City</span></a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">{nav}</div></details></li>
<li><a href="@/about-us/">About</a></li><li><a href="@/manufacturers/">Manufacturers</a></li><li><a href="@/articles/">Articles</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call for a free estimate</small>{S["phone"]}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{nav}</div>
<a href="@/about-us/">About</a><a href="@/manufacturers/">Manufacturers</a><a href="@/articles/">Articles</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>'''


def footer():
    res = [s for s in SVC if s[0] in ("utah_roof_repair", "roof_replacement", "utah_metal_roofing", "asphalt_shingle_roofing", "flat_roof_repair", "residential_tile_roofing", "residential_wood_roofing", "tpo_roofing_membrane")]
    com = [s for s in SVC if s not in res]
    li = lambda xs: "".join(f'<li><a href="@/{p}">{n}</a></li>' for k, p, n, *_ in xs)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Find the cause.<br><span>Fix it once.</span></p><div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a></div></div>
<div class="foot">
<div><p class="fname">{NAME}</p><address>{S["street"]}<br>{S["city"]}, {S["state"]} {S["zip"]}</address><p class="mono small">{S["hours"]}</p><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div><h3>Residential</h3><ul>{li(res)}</ul></div>
<div><h3>Commercial</h3><ul>{li(com)}</ul></div>
<div><h3>Serving</h3><p class="areas">{", ".join(AREAS)} &amp; more</p></div>
</div><div class="fbottom"><span>&copy; 2026 {NAME} &middot; Roofing since {S["since"]}</span><span class="mono">Service manual &middot; rev. 2026</span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call {S["phone"]}</a><a href="@/{CONTACT}">Estimate</a></div>'''


def cta(title="Tell us what you&rsquo;re seeing.", text="Call for a free evaluation and quote. There&rsquo;s no obligation, and the evaluation stays on record in case you need it for insurance later."):
    return f'''<section class="cta"><div class="wrap"><div class="cta-ticket reveal">
<div class="ct-l"><p class="label">Free evaluation &amp; quote</p><h2>{title}</h2><p>{text}</p></div>
<div class="ct-r"><span class="mono">Call</span><a class="cta-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Request an Estimate {ARROW}</a><span class="mono small">{S["hours"]}</span></div>
</div></div></section>'''


def phero(trail, h1, lede, code, sw=None):
    art = f'<div class="ph-sw">{swatch(sw)}<span class="mono">Material: {sw}</span></div>' if sw else ""
    return f'''<section class="phero"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="code mono">Section {code}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}
<div class="btn-row"><a class="btn" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a><a class="btn ghost" href="@/{CONTACT}">Free Estimate {ARROW}</a></div></div>{art}</div></section>'''


def quote_form(title="Request a free estimate"):
    # Same fields as the current contact form. Needs a form handler before go-live.
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<label for="f-name">Your name *<input id="f-name" name="name" autocomplete="name" required></label>
<div class="row"><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-msg">Your message<textarea id="f-msg" name="message" placeholder="Where is the roof, and what are you seeing?"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button><p class="note">* Required</p></form>'''


# symptom finder: symptom -> likely causes, spots on Fig. 1, where to go
SYMPTOMS = [
 ("stain", "Water stain on a ceiling", "Water usually travels before it shows. The most common sources are flashing at a chimney, skylight or wall, a cracked pipe boot, or a valley.", [1, 3, 4, 2], "utah-roof-repair/"),
 ("shingles", "Missing or lifted shingles", "Wind, hail and age loosen shingles, most often along the ridge, the rakes and the eaves. Exposed felt lets water in quickly.", [6, 5], "asphalt-shingle-roofing/"),
 ("ice", "Icicles and ice at the eaves", "Ice dams form when roof snow melts and refreezes at the cold eaves, backing water up under the shingles.", [5], "waterproof-roofing-services/"),
 ("ponding", "Water pooling on a flat roof", "Ponding points to sagging, blocked drains or worn membrane. Standing water finds seams and punctures.", [], "flat-roof-repair/"),
 ("hail", "Damage after a hail or wind storm", "Bruised or cracked shingles, dented metal and torn membrane are common after storms. Document it before you call your insurer.", [6, 2], "roofing-insurance-claims-assistance/"),
 ("old", "An old roof that keeps leaking", "When leaks keep moving and repairs keep adding up, the roof may be at the end of its life.", [1, 2, 3, 4, 5, 6], "roof-replacement/"),
]


def home():
    chips = "".join(f'<button type="button" class="sym{" on" if i == 0 else ""}" data-sym="{k}" aria-pressed="{"true" if i == 0 else "false"}"><span class="mono">{i + 1:02d}</span>{t}</button>' for i, (k, t, *_) in enumerate(SYMPTOMS))
    panes = "".join(f'''<div class="pane{" on" if i == 0 else ""}" data-pane="{k}" data-spots="{",".join(map(str, sp))}"><p class="mono">Diagnosis {i + 1:02d}</p><h3>{t}</h3><p>{why}</p>
<p class="spots">{("Check on Fig. 1: " + ", ".join(f"<b>{n}</b> {next(l for m, l, *_ in SPOTS if m == n)}" for n in sp)) if sp else "Flat roofs: see the membrane and drains."}</p><a class="tlink" href="@/{go}">Go to the fix {ARROW}</a></div>''' for i, (k, t, why, sp, go) in enumerate(SYMPTOMS))
    systems = [("shingle", "Asphalt shingles", "asphalt-shingle-roofing/"), ("metal", "Standing seam metal", "utah-metal-roofing/"), ("tile", "Clay &amp; concrete tile", "residential-tile-roofing/"),
               ("wood", "Wood shakes", "residential-wood-roofing/"), ("tpo", "TPO membrane", "tpo-roofing-membrane/"), ("ballast", "Ballasted roofing", p_blog.POST[1]), ("membrane", "Flat &amp; low-slope", "flat-roof-repair/")]
    sysg = "".join(f'<a class="mat reveal" href="@/{p}">{swatch(k)}<b>{n}</b><span class="mono">{["SH", "MT", "TL", "WD", "TP", "BL", "FL"][i]}-{i + 1:02d}</span></a>' for i, (k, n, p) in enumerate(systems))
    idx = "".join(f'<li><a href="@/{p}"><span class="mono">{c}</span><b>{n}</b><i>{ARROW}</i></a></li>' for k, p, n, c, *_ in SVC)
    faqs = [("Is the estimate free?", "Yes. Call for a free evaluation and quote. There&rsquo;s no obligation, and it stays on record in case you need it for an insurance claim later."),
            ("Do you work on commercial roofs?", "Yes. We repair, replace and install roofs on homes and on commercial buildings, including flat roofs, TPO, metal and ballasted systems."),
            ("How long have you been roofing?", f"Roof Repair Salt Lake City has been roofing since {S['since']}."),
            ("Do you do roof inspections?", "Yes. A roof inspection is part of every free evaluation, and we also inspect roofs on request."),
            ("Which areas do you serve?", f"Salt Lake City and nearby cities including {', '.join(AREAS[1:9])} and more.")]
    body = f'''
<section class="hero"><div class="wrap hero-in">
<div class="hero-text"><p class="code mono">Service manual &middot; Salt Lake City, Utah &middot; Since {S["since"]}</p>
<h1>Roof repair in Salt Lake City, <span>done like a manual.</span></h1>
<p class="lede">Roof Repair Salt Lake City repairs and replaces roofs for homeowners and commercial builders across the Salt Lake Valley, roofing since {S["since"]}. Tell us the symptom; we find the cause and fix it.</p>
<div class="btn-row"><a class="btn" href="tel:{S["tel"]}">{PHONE} Call {S["phone"]}</a><a class="btn ghost" href="@/{CONTACT}">Free Estimate {ARROW}</a></div>
<dl class="specs"><div><dt>Since</dt><dd>{S["since"]}</dd></div><div><dt>Work</dt><dd>Residential &amp; commercial</dd></div><div><dt>Estimates</dt><dd>Free</dd></div><div><dt>Hours</dt><dd>7 days, 9&ndash;5</dd></div></dl></div>
<figure class="hero-fig reveal">{fig_house()}</figure>
</div></section>

<section class="sec finder-sec"><div class="wrap">
<div class="head reveal"><p class="label">Symptom finder</p><h2>What are you seeing <span>on your roof?</span></h2><p class="lede">Pick a symptom. The manual shows the likely causes on Fig. 1 and the page with the fix.</p></div>
<div class="finder reveal"><div class="syms" role="group" aria-label="Symptoms">{chips}</div><div class="panes">{panes}</div></div>
</div></section>

<section class="sec dark"><div class="wrap split">
<div class="reveal"><p class="label light">Roofers in Salt Lake City</p><h2>Residential and commercial, <span>repair and replacement.</span></h2>
<p>Roof Repair Salt Lake City is a roofing contractor in Salt Lake City, Utah, in operation since {S["since"]}. We work for homeowners and commercial builders: repairs, re-roofs, roof replacement, flat roof repair, inspections, new construction and gutters.</p>
<p>We also offer custom sheet metal fabrication and ballasted roofing, and we work hand in hand with you so the roof is built or repaired to your specifications.</p>
<a class="tlink light" href="@/about-us/">About us {ARROW}</a></div>
<div class="reveal"><ol class="index">{idx}</ol></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Materials</p><h2>Seven roof systems, <span>one crew.</span></h2><p class="lede">Steep-slope and low-slope: the systems we install and repair, from shingles to stone-ballasted membranes.</p></div>
<div class="mats">{sysg}</div>
</div></section>

<section class="sec paper"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">How it works</p><h2>Three steps, <span>no obligation.</span></h2>
<ol class="steps"><li><b>Call or send the form</b><p>Tell us where the roof is and what you&rsquo;re seeing.</p></li>
<li><b>Free evaluation and quote</b><p>We inspect the roof, find the cause and give you a quote. It stays on record for insurance if you need it.</p></li>
<li><b>Repair or replacement</b><p>Done to your specifications, with the products that suit the roof.</p></li></ol>
<p class="small">{S["hours"]}</p></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Before <span>you call.</span></h2>
<a class="guide" href="@/{p_blog.POST[1]}"><span class="mono">From the articles</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(faqs)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roof Repair Salt Lake City | Residential & Commercial Roofing",
            "meta": "Roof Repair Salt Lake City: residential and commercial roof repair, replacement and flat roofs in Salt Lake City, roofing since 2005. Free estimates.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(faqs)]}


def service(row):
    key, path, nav, code, sw, title, meta, h1, intro = row
    trail = [HOME, (nav, path)]
    rel = [s for s in SVC if s[0] != key][:5]
    body = phero(trail, h1, None, code, sw) + f'''
<section class="sec"><div class="wrap sv-grid">
<article class="prose"><p class="answer">{intro}</p>
{migrate(key)}
</article>
<aside class="sv-side">
<div class="side-card"><p class="label light">Free estimate</p><h3>Call the shop</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Request an Estimate {ARROW}</a><p class="mono small">{S["hours"]}</p></div>
<div class="side-rel"><p class="label">Other sections</p><ul>{"".join(f'<li><a href="@/{p}"><span class="mono">{c}</span>{n}</a></li>' for k, p, n, c, *_ in rel)}</ul></div>
</aside></div></section>''' + cta()
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body,
            "schema": [{"@type": "Service", "@id": canon(path) + "#service", "name": nav, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": "Salt Lake City"}}, crumbs_ld(path, trail)]}


def about():
    trail = [HOME, ("About Us", "about-us/")]
    body = phero(trail, "About Roof Repair Salt Lake City", f"Roofing in Salt Lake City since {S['since']}.", "AB-00") + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">
<p class="answer">Roof Repair Salt Lake City is a roofing contractor in Salt Lake City, Utah, roofing since {S["since"]}. Our business is built on providing quality roofing solutions to homeowners and builders.</p>
{migrate("about_us")}
</article><aside class="sv-side"><div class="side-card"><p class="label light">Talk to us</p><h3>Call the shop</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Contact Us {ARROW}</a></div></aside></div></section>''' + cta()
    return {"path": "about-us/", "canonical": canon("about-us/"), "title": "About Roof Repair Salt Lake City | Roofing Since 2005",
            "meta": "About Roof Repair Salt Lake City, a roofing contractor in Salt Lake City since 2005: residential and commercial repair, re-roofs, tear-offs and more.",
            "body": body, "schema": [crumbs_ld("about-us/", trail), {"@type": "AboutPage", "@id": canon("about-us/") + "#page", "url": canon("about-us/")}]}


def manufacturers():
    trail = [HOME, ("Manufacturers", "manufacturers/")]
    makers = ["Entegra Roof Tile", "Ludowici", "Firestone", "Drexel Metals Inc.", "Eagle", "Neogard", "Kemper System", "Solatube", "Redland", "Creaton", "Monier", "Santa Ana", "Hanson", "EverGreen", "Polyglass", "Tremco", "NB Handy"]
    grid = "".join(f'<li><span class="mono">{i + 1:02d}</span>{m}</li>' for i, m in enumerate(makers))
    body = phero(trail, "Roofing Manufacturers We Work With in Salt Lake City", "Tile, metal, membrane, coating and skylight makers we buy from.", "MF-00") + f'''
<section class="sec"><div class="wrap"><p class="answer">These are some of the roofing supply companies Roof Repair Salt Lake City works with on jobs in Salt Lake City, as listed on our site.</p>
<ol class="makers">{grid}</ol><p class="small">Listing a manufacturer here means we buy and install its products; it is not a certification claim.</p></div></section>''' + cta()
    return {"path": "manufacturers/", "canonical": canon("manufacturers/"), "title": "Roofing Manufacturers We Use | Roof Repair Salt Lake City",
            "meta": "The roofing manufacturers Roof Repair Salt Lake City works with: tile, metal, single-ply, coatings and skylights from Ludowici, Firestone, Tremco and more.",
            "body": body, "schema": [crumbs_ld("manufacturers/", trail)]}


def contact():
    trail = [HOME, ("Contact Us", CONTACT)]
    body = phero(trail, "Contact Roof Repair Salt Lake City", "Have questions about roof repair? Call, email or send the form.", "CT-00") + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><dl class="card-info">
<div><dt>Call</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd></div>
<div><dt>Address</dt><dd>{S["street"]}<br>{S["city"]}, {S["state"]} {S["zip"]}</dd></div>
<div><dt>Hours</dt><dd>{S["hours"]}</dd></div>
<div><dt>Serving</dt><dd>{", ".join(AREAS)} &amp; more</dd></div></dl></div>
<div class="reveal">{quote_form("Send us a question")}</div></div></section>'''
    return {"path": CONTACT, "canonical": canon(CONTACT), "title": "Contact Roof Repair Salt Lake City | (385) 355-4849",
            "meta": "Contact Roof Repair Salt Lake City for a free roofing estimate: call (385) 355-4849, email, or send the form. Open Monday to Sunday, 9:00AM to 5:00PM.",
            "body": body, "schema": [crumbs_ld(CONTACT, trail), {"@type": "ContactPage", "@id": canon(CONTACT) + "#page", "url": canon(CONTACT)}]}


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t in the manual.", "Try a section below or call us.", "404") + f'<section class="sec"><div class="wrap"><ol class="index light">{"".join(f"<li><a href=\"@/{p}\"><span class=\"mono\">{c}</span><b>{n}</b><i>{ARROW}</i></a></li>" for k, p, n, c, *_ in SVC)}</ol></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Roof Repair Salt Lake City", "meta": "Page not found. Browse roof repair, replacement and commercial roofing sections, or call Roof Repair Salt Lake City at (385) 355-4849 for a free estimate.",
            "body": body, "robots": "noindex, follow", "sitemap": False}


def _fit(pg):
    # pad short meta descriptions toward 150-160 characters with real, useful text
    for add in (" Free estimates.", " Call (385) 355-4849.", " Roofing since 2005."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip() not in pg["meta"]:
            pg["meta"] += add
    return pg


def make_pages():
    p_blog.setup(phero, cta, ARROW, HOME, CONTACT)
    return [_fit(x) for x in _pages()]


def _pages():
    return [home()] + [service(r) for r in SVC] + [about(), manufacturers(), contact()] + p_blog.pages() + [notfound()]
