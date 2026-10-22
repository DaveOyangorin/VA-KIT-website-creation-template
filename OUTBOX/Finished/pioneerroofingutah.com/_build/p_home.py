import re, html
from build import U, S, ARROW, PHONE, CHECK, HEX, SEAL, IMG, IMGMAP, INSPECT, CONTACT, ESTIMATE, img, faq_html, faq_ld, quotes_html, cta, quote_form
import p_blog

# Main keyword: roofing company salt lake city (+ roofers / roofing contractor salt lake city), per the 14 Oct report.
# Every fact is from the client's own pages (home, pricing, certification & warranty, roof type pages, gallery), 17 Oct 2026.
# "Since 1980" comes from the logo ("Est. 1980"); the pages disagree on years (nearly 40 / over 40 / 45 / 45+), see notes.

POOL = ["asphalt-background-1", "pioneer-roofs-0803-scaled-1", "rec", "pioneer-highland-tower", "pioneer-roofs-0810-scaled-1", "2016-pioneer-roofing-2",
        "metal-roof-1", "16-2016-pioneer-roofing-0072", "pioneer-next-door-2", "2016-pioneer-roofing-4-scaled-1", "asphalt-shingles-2"]  # the client's own project photos, from the contact-sheet review


def HERO_POOL():
    names = [n for n in POOL if n in IMG]
    if not names:  # fallback before the review: widest landscape photos
        names = sorted((n for n in IMG if IMG[n][0] >= 900 and IMG[n][0] > IMG[n][1] and "logo" not in n), key=lambda n: -IMG[n][0])
    return names


PROJECTS = [("Cottonwood Heights", "Asphalt roofing"), ("Draper", "Asphalt roofing"), ("North Salt Lake", "Asphalt roofing"),
            ("Highland Tower", "Commercial TPO membrane"), ("Cottonwood Heights Rec Center", "Commercial TPO membrane"),
            ("TPO West Jordan Warehouse", "Commercial TPO membrane"), ("TPO South Jordan", "Commercial TPO membrane"),
            ("TPO Industrial Building SLC", "Commercial TPO membrane"), ("TPO Warehouse Riverton", "Commercial TPO membrane")]

FAQS = [
    ("How much does a new roof cost in Salt Lake City?",
     "Our real price ranges for a typical 2,000 sq. ft. home in Salt Lake City and the Wasatch Front over the last 12 months: $9,100&ndash;$12,600 for a straightforward asphalt replacement, $13,400&ndash;$16,600 for a complex or premium asphalt roof, and $13,100&ndash;$16,300 for a TPO or flat membrane roof. See the <a href=\"@/pricing/\">pricing page</a> for what moves the price."),
    ("Who answers when I call?",
     "Our service number goes directly to our owner, John. No recordings or outsourced answering services."),
    ("Do you help with insurance claims?",
     "Yes. After a major storm, insurance companies will often require an inspection by a roofing professional. We&rsquo;re fully licensed and insured, and we can help with the claims process by assessing your home after the damage."),
    ("What warranty do you offer?",
     "We offer a 10-year labor warranty in addition to the lifetime warranty on the materials we use, and we stand by every job. Ask us about the warranty for your specific roof type."),
    ("Do you do commercial roofs?",
     "Yes. For flat roofs we specialize in membrane roofing such as TPO and PVC. For pitched roofs we install asphalt shingles, metal panels and wood shake shingles, and we remove and dispose of existing roof layers."),
]


def build(r, rec, posts, tests):
    pool = HERO_POOL()
    hero = pool[0]
    reasons = [("Quick response", "Our service number goes directly to our owner, John. No recordings or outsourced answering services, guaranteed."),
               ("Trusted", "Thousands of jobs completed to our customers&rsquo; satisfaction."),
               ("Trained workers", "Every job has workers with 10+ years of experience."),
               ("Quality materials", "Only the highest quality materials on our roofs."),
               ("Warranties", "We offer warranties on every roof."),
               ("Transparent pricing", "100% transparent quotes, and real price ranges published on our site.")]
    rs = "".join(f'<li><i>{CHECK}</i><div><b>{a}</b><small>{b}</small></div></li>' for a, b in reasons)
    specs = [("01", "Asphalt shingles", "asphalt-shingles/", "Economical, easy to install and quick to finish. The go-to for pitched roofs.", [("Typical replacement", "$9,100&ndash;$12,600"), ("Best for", "Pitched roofs")]),
             ("02", "TPO membrane", "tpo-membrane/", "We&rsquo;ve installed TPO for over 15 years. A white, reflective single-ply membrane that&rsquo;s easy to repair.", [("Typical roof", "$13,100&ndash;$16,300"), ("Best for", "Flat roofs")]),
             ("03", "Metal roofing", "metal-roofing/", "Stands up to wind, snow and ice, reflects heat, and resists fire for mountain homes and cabins.", [("Price", "Free quote"), ("Best for", "Long life")]),
             ("04", "Roof repairs", "roofing-repairs/", "Leak detection, shingle replacement, flashing repair, evaporative cooler removal, roof and gutter cleaning.", [("Basic repair", "$250&ndash;$1,000"), ("Advanced", "$1,100&ndash;$2,000")])]
    spec_html = ""
    for no, name, p, d, rows in specs:
        dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
        spec_html += f'<a class="spec-card reveal" href="@/{p}"><span class="no">No. {no}</span><b>{name}</b><p>{d}</p><dl>{dl}</dl><em>Learn more &rarr;</em></a>'
    gal = "".join(f'<figure class="snap reveal">{img(n, "Roofing project by Pioneer Roofing in Utah")}</figure>' for n in pool[1:7])
    proj = "".join(f'<li><i>{CHECK}</i><div><b>{a}</b><small>{b}</small></div></li>' for a, b in PROJECTS)
    cities = sorted(((p, rr) for p, rr in rec.items() if p.startswith("areas-") and p != "areas-we-serve/" or p in ("salt-lake-city/", "sandy/", "south-jordan/", "herriman/", "riverton/", "taylorsville/", "tooele/", "eagle-mountain/")),
                    key=lambda x: x[0].replace("areas-", ""))
    chips = "".join(f'<a href="@/{p}">{html.escape(re.sub(r"^areas-", "", p).strip("/").replace("-", " ").title())}</a>' for p, rr in cities)
    latest = [(p_blog.PATH, "What Is the 25% Rule for Roofing?")] + [(pp, re.sub(r"<[^>]+>", "", pr["h1"] or pp)) for pp, pr in posts[:2]]
    post_html = "".join(f'<li><a href="@/{pp}">{html.escape(t)}</a></li>' for pp, t in latest)
    tags = ""
    for no, name, p, d, rows in specs:
        dl = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows)
        tags += f'<a class="hangtag reveal" href="@/{p}"><span class="hole" aria-hidden="true"></span><span class="no">No. {no}</span><b>{name}</b><p>{d}</p><dl>{dl}</dl><em>Learn more {ARROW}</em></a>'
    body = f'''
<section class="hero"><div class="hero-bg">{img(hero, "Roof completed by Pioneer Roofing in the Salt Lake City area", priority=True)}</div><span class="ghost-year" aria-hidden="true">1980</span>
<div class="wrap hero-in">
<div class="hero-text"><p class="label light">Pioneer Roofing Co &middot; Salt Lake City, Utah</p>
<h1>Salt Lake City roofing company. <span>Since 1980.</span></h1>
<p class="lede">Pioneer Roofing is a family run roofing company in Salt Lake City, roofing homes and businesses along the Wasatch Front and throughout Utah since 1980. Repairs or a complete replacement, in asphalt shingles, TPO, PVC or metal.</p>
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Book an Inspection {ARROW}</a><a class="btn ghost light" href="@/{ESTIMATE}">Get an Instant Estimate</a></div></div>
<div class="hero-seal reveal">{SEAL}</div>
</div></section>

<section class="patches" aria-label="Pioneer Roofing at a glance"><div class="wrap patch-row">
<div class="patch"><b>1980</b><span>Established. Family run and operated.</span></div>
<div class="patch"><b>10+<sup>yrs</sup></b><span>Experience on every crew, on every job</span></div>
<div class="patch"><b>10<sup>yr</sup></b><span>Labor warranty, plus lifetime materials warranty</span></div>
<div class="patch"><b>$250<sup>+</sup></b><span>Basic roof repairs start at $250, with published price ranges</span></div>
</div></section>

<section class="sec tags-sec"><div class="wrap">
<div class="head row reveal"><div><p class="label">Roofers in Salt Lake City</p><h2>Four ways we keep <span>a roof over you</span></h2></div><p class="head-note">As a roofing contractor in Salt Lake City, we specialize in roof removal, disposal, cleanup and installation of pitched and flat roofs. Prices are our real ranges for a typical 2,000 sq. ft. home.</p></div>
<div class="hangtags">{tags}</div>
<p class="tlink-row"><a class="tlink" href="@/pricing/">See all prices and what changes them {ARROW}</a></p>
</div></section>

<section class="sec dark"><div class="wrap split">
<div class="reveal"><p class="label light">Call the owner</p><h2>Your call goes straight to John</h2>
<p class="lede">No recordings. No outsourced answering service. When you call Pioneer Roofing, you talk to the owner.</p>
<a class="phone-big" href="tel:{S["tel"]}">{S["phone"]}</a>
<figure class="owner">{img("pioneer-roofing-john-and-linda-stout-4-5-ratio-photo", "John and Linda Stout of Pioneer Roofing") if "pioneer-roofing-john-and-linda-stout-4-5-ratio-photo" in IMG else ""}<figcaption>John and Linda Stout, Pioneer Roofing</figcaption></figure>
<p style="margin-top:18px;color:rgba(255,255,255,.75)">Or email <a href="mailto:{S["email"]}" style="color:#fff">{S["email"]}</a></p></div>
<div class="reveal"><p class="label light">Six reasons to choose us</p><ol class="checklist">{rs}</ol></div>
</div></section>

<section class="sec canvas"><div class="wrap split rev">
<div class="reveal"><p class="label">Transparent pricing</p><h2>What new roofs actually cost</h2>
<p>Most roofs don&rsquo;t have a fixed price, because cost depends on size, material, condition, access and what turns up during inspection. That doesn&rsquo;t mean you should be left guessing.</p>
<div class="tablebox price-table ledger"><table><thead><tr><th>Typical 2,000 sq. ft. home</th><th>Last 12 months</th></tr></thead><tbody>
<tr><td>Asphalt replacement, straightforward</td><td>$9,100&ndash;$12,600</td></tr>
<tr><td>Asphalt replacement, complex or premium</td><td>$13,400&ndash;$16,600</td></tr>
<tr><td>TPO / flat membrane roof</td><td>$13,100&ndash;$16,300</td></tr>
<tr><td>Roof repair, basic</td><td>$250&ndash;$1,000</td></tr>
<tr><td>Roof repair, advanced</td><td>$1,100&ndash;$2,000</td></tr>
</tbody></table></div>
<a class="btn navy" href="@/pricing/">Full pricing guide {ARROW}</a></div>
<div class="reveal frame-ez">{img(pool[7] if len(pool) > 7 else hero, "Roof replacement by Pioneer Roofing")}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Project gallery</p><h2>Roofs we&rsquo;ve built around the valley</h2><p class="lede">Homes, warehouses, apartment buildings and a rec center. <a href="@/project-gallery/">See the gallery</a>.</p></div>
<div class="snaps">{gal}</div>
<div class="reveal" style="margin-top:34px"><ol class="checklist projects-list">{proj}</ol></div>
</div></section>
''' + quotes_html(tests, "What our customers say") + f'''
<section class="sec white"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Areas we serve</p><h2>Salt Lake, the Wasatch Front and beyond</h2>
<p>We work in Salt Lake, along the Wasatch Front and throughout the state of Utah, from our offices in Salt Lake City and Price.</p>
<p><strong>{S["slc"]["street"]}, {S["slc"]["city"]}, {S["slc"]["st"]} {S["slc"]["zip"]}</strong><br><strong>{S["price"]["street"]}, {S["price"]["city"]}, {S["price"]["st"]} {S["price"]["zip"]}</strong></p>
<div class="chips" style="margin-top:18px">{chips}</div></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight answers</h2><p class="lede">From the blog:</p><ul class="checks" style="padding-left:1.1em">{post_html}</ul>
<a class="btn navy" href="@/{CONTACT}">Contact us {ARROW}</a></div>
<div class="reveal">{faq_html(FAQS)}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company Salt Lake City | Pioneer Roofing Since 1980",
            "meta": "Pioneer Roofing is a family run roofing company in Salt Lake City since 1980: roof repair, replacement and inspections. Real prices online. Call (801) 943-7663.",
            "body": body, "og": hero,
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]},
                       faq_ld(FAQS)],
            "full_biz": True}
