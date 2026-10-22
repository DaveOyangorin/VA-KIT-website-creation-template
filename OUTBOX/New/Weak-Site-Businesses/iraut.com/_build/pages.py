"""Pages for the iraut.com redesign: "Ecosystem".

IRA's pitch is that one firm covers the whole life of an investment property: buy it, lease it, manage it, improve it, exchange it, sell it.
So the home page opens on a full-bleed aerial of a commercial property they handle under the Wasatch, and the signature is the ecosystem
wheel: six services around the IRA mark; pick one and the panel shows what that team does, in their words, with one of their real properties
and the figure that goes with it ($380M under management, 1,600+ units, both legs of a 1031). Teal and olive from the logo, owner-report cream,
Newsreader for an editorial, trustworthy voice.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 48 URLs (no trailing slash); Wix placeholder and duplicate pages are kept noindex."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta
STOP = ("Have a question? Shoot us a note", "Contact Us Have a question", "Mailing: 869", "©", "Investment Realty Advisors is a full-service")
JUNK = re.compile(r"This is a Paragraph|placeholder text|Edit Text|double click|Click Here to Log In|^Send$|^Thanks!|^Submit$|^Apply$|^Read More$|^Click Here$|^Learn More$|^Get a Quote$|^View Listings$", re.I)


def blocks(key):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8", errors="ignore").read()
    i = s.find("PAGES_CONTAINER"); s = s[i:] if i > 0 else s
    s = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", s)
    out, started, seen = [], False, set()
    for t, x in re.findall(r"(?s)<(h1|h2|h3|h4|h5|h6|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", x))).replace("​", "").strip()
        if not x: continue
        if t.startswith("h"): started = True
        if not started: continue
        if any(x.startswith(st) for st in STOP): break
        if JUNK.search(x) or x in seen: continue
        seen.add(x); out.append((t, x))
    return out


def render(key, skip_first=True, drop=()):
    b = blocks(key)
    if skip_first and b and b[0][0] in ("h1", "h2"): b = b[1:]
    res, ul, para = [], [], []
    def flush_p():
        if para: res.append("<p>" + html.escape(" ".join(para)) + "</p>"); para.clear()
    def flush_ul():
        if ul: res.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in b:
        if any(d in x for d in drop): continue
        if t == "li": flush_p(); ul.append(x); continue
        flush_ul()
        if t == "p":
            para.append(x)
            if re.search(r"[.!?:]\s*$", x) or len(" ".join(para)) > 420: flush_p()
            continue
        flush_p()
        if len(x) < 2: continue
        tag = "h2" if t in ("h1", "h2") else "h3"
        res.append(f"<{tag}>{html.escape(x[:1] + x[1:].lower() if x.isupper() and len(x) > 4 else x)}</{tag}>")
    flush_p(); flush_ul()
    return "\n".join(res)


WHEEL = [("brokerage", "Commercial brokerage", "Investors, family offices, corporate tenants and owner-users: buying, selling, leasing, value-add, development and financial analysis. IRA transacted on over $103M in volume in 2021.", "$103M", "transacted in 2021", "commercial-real-estate/", "ira-office"),
         ("pm", "Property management", "Rent collection, maintenance, tenant relations, equity evaluations and quarterly reports, with management fees as low as 3%.", "$380M", "in assets under management", "pm/", "ira-strip"),
         ("residential", "Residential investing", "One- to four-unit properties: buy, value, professionally manage and grow your portfolio.", "1&ndash;4", "door properties", "residential/", "ira-house"),
         ("exchange", "1031 exchange", "IRA represents the brokerage side of both legs: selling the relinquished property and securing and closing on the exchange property.", "2 legs", "of the exchange, one team", "post/1031-exchange-rules-for-utah-investors/", "ira-aerial"),
         ("value", "Value-add &amp; development", "Full development and value-add services, from site and plans to stabilized operations.", "$40M+", "in leases over 24 months", "use-cases/", "ira-render"),
         ("storage", "Self storage", "Seven self-storage communities from Clearfield to Taylorsville, managed by IRA.", "7", "storage communities", "selfstorage/", "ira-midcentury")]
STATS = [("$380M", "assets under management"), ("1,600+", "units on the Wasatch Front"), ("2008", "brokerage since"), ("100+", "combined years of experience")]
FAQ = [("What does Investment Realty Advisors do?", "<p>IRA combines a brokerage firm with property management, so investors can buy, lease, manage, improve, exchange and sell property with one team.</p>"),
       ("How much does property management cost?", "<p>Property management is only part of our business, and our management fee can be as low as 3%. See our fee schedule or call (801) 528-4557.</p>"),
       ("Can you help with a 1031 exchange?", "<p>Yes. Our agents can assist with both legs of a 1031 exchange: selling the relinquished property and securing the replacement property.</p>"),
       ("How do tenants reach maintenance?", "<p>Call (801) 528-4557, extension 4 for maintenance, or extension 6 for maintenance emergencies. Tenants can also submit requests in the tenant portal.</p>")]
STORAGE = [("54 Storage", "3850 West 5400 South, Taylorsville"), ("Brickyard Self Storage", "1066 East 3300 South, Salt Lake City"), ("Haven Ave Storage", "185 W Haven Ave, Salt Lake City"),
           ("Heritage Secure Storage", "159 E Gordon Lane, Murray"), ("Classic Storage", "2087 North Main Street, Sunset City"), ("Garden Storage", "260 W Antelope Dr, Clearfield"), ("Sweetwater Storage", "2984 S Sweetwater Park Dr, Garden City")]


def wheel():
    n = len(WHEEL)
    segs = ""
    import math
    for i, (k, t, d, fig, cap, href, im) in enumerate(WHEEL):
        a0, a1 = (i / n) * 2 * math.pi - math.pi / 2, ((i + 1) / n) * 2 * math.pi - math.pi / 2
        r1, r2, cx, cy = 92, 190, 200, 200
        p = lambda r, a: (cx + r * math.cos(a), cy + r * math.sin(a))
        (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p(r2, a0), p(r2, a1), p(r1, a1), p(r1, a0)
        am = (a0 + a1) / 2; lx, ly = p(141, am)
        lab = re.sub("&amp;", "&", t).split(" ")
        lines = []
        for w in lab:
            if lines and len(lines[-1] + " " + w) <= 12: lines[-1] += " " + w
            else: lines.append(w)
        tspans = "".join(f'<tspan x="{lx:.1f}" dy="{0 if j == 0 else 14}">{html.escape(l)}</tspan>' for j, l in enumerate(lines))
        segs += f'''<g class="seg" tabindex="0" role="button" aria-pressed="{"true" if i == 0 else "false"}" data-seg="{k}" aria-label="{html.escape(re.sub("&amp;", "&", t))}">
<path d="M{x1:.1f} {y1:.1f} A{r2} {r2} 0 0 1 {x2:.1f} {y2:.1f} L{x3:.1f} {y3:.1f} A{r1} {r1} 0 0 0 {x4:.1f} {y4:.1f} Z"/><text x="{lx:.1f}" y="{ly + 4 - 7 * (len(lines) - 1):.1f}" text-anchor="middle">{tspans}</text></g>'''
    svg = f'<svg class="wh" viewBox="0 0 400 400" aria-label="IRA services"><circle cx="200" cy="200" r="86" class="hub"/><text x="200" y="196" text-anchor="middle" class="hub-t">IRA</text><text x="200" y="218" text-anchor="middle" class="hub-s">one firm</text>{segs}</svg>'
    panels = "".join(f'''<div class="wp" data-wp="{k}"{"" if i == 0 else " hidden"}><figure>{img(im, re.sub("&amp;", "and", t) + " property")}</figure><div><p class="label">{t}</p><p class="wp-fig"><b>{fig}</b> <span>{cap}</span></p><p>{d}</p><a class="tlink" href="@/{href}">Learn more {ARROW}</a></div></div>''' for i, (k, t, d, fig, cap, href, im) in enumerate(WHEEL))
    return f'<div class="eco" data-eco><div class="eco-l">{svg}<p class="eco-hint">Choose a service on the wheel.</p></div><div class="eco-r" aria-live="polite">{panels}</div></div>'


def home():
    body = f'''
<section class="i-hero"><div class="ih-img" data-parallax="0.08">{img("ira-hero", "Aerial view of a commercial property and parking lot with snow-capped mountains behind, on Utah's Wasatch Front", priority=True)}</div>
<div class="wrap ih-in"><div class="ih-txt"><p class="label">Midvale &middot; Salt Lake metro &middot; Since 2008</p>
<h1>Property management and real estate brokerage in Midvale, <em>under one roof.</em></h1>
<p class="lede">Investment Realty Advisors is a one-stop real estate brokerage and property management firm in Utah. Instead of working with several companies, investors get one real estate ecosystem: simplify, streamline, satisfy.</p>
<div class="btn-row"><a class="btn accent" href="@/contactus/">Talk to IRA {ARROW}</a><a class="btn ghost" href="tel:+18015284557">{PHONE} (801) 528-4557</a></div></div></div>
<div class="ih-stats"><div class="wrap stats">{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in STATS)}</div></div></section>

<section class="sec i-eco" id="ecosystem"><div class="wrap">
<div class="i-head split-h reveal"><div><p class="label">The IRA ecosystem</p><h2>Buy it, run it, grow it. <em>One team.</em></h2></div><p class="lede">Six services that usually take six firms. Pick one to see what that team does and a property it&rsquo;s worked on.</p></div>
{wheel()}
</div></section>

<section class="sec i-paths"><div class="wrap">
<div class="i-head reveal"><p class="label">Where to start</p><h2>Owner, investor <em>or tenant?</em></h2></div>
<div class="paths">
<a class="pth reveal" href="@/pm/"><figure>{img("ira-apts", "A two-story apartment building with parking")}</figure><div><span>Owners</span><b>Property management</b><p>Quarterly reports, rent collection, maintenance and tenant relations, with fees as low as 3%.</p><em>Property management {ARROW}</em></div></a>
<a class="pth reveal" href="@/commercial-real-estate/"><figure>{img("ira-twostory", "A two-story retail and office building")}</figure><div><span>Investors</span><b>Commercial &amp; residential</b><p>Sourcing, buying, selling, leasing, 1031 exchanges and value-add, from 1-4 doors to commercial assets.</p><em>Investing {ARROW}</em></div></a>
<a class="pth reveal" href="@/portal/"><figure>{img("ira-kitchen", "A remodeled kitchen with a white island")}</figure><div><span>Tenants</span><b>Tenant portal &amp; FAQ</b><p>Pay rent, submit maintenance requests and access records online.</p><em>Tenant portal {ARROW}</em></div></a>
</div></div></section>

<section class="i-band"><div class="band-img" data-parallax="0.1">{img("ira-aerial", "Aerial view of a mixed-use street with parking and mountains beyond")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our focus</p><p>Property management is only part of our business. Our focus is growing your wealth: analyzing cash flow and market rates, then growing your asset pool or selling through a 1031 exchange to reach your goals.</p></blockquote></div></section>

<section class="sec i-port"><div class="wrap">
<div class="i-head split-h reveal"><div><p class="label">Portfolio</p><h2>Retail, office, multifamily, <em>industrial.</em></h2></div><a class="tlink" href="@/use-cases/">Current &amp; past performance {ARROW}</a></div>
<div class="gal">{"".join(f'<figure class="g{i} reveal">{img(n, a)}</figure>' for i, (n, a) in enumerate([("ira-tower", "A modern glass office building"), ("ira-mixed", "A stone and stucco mixed-use building"), ("ira-retail", "A retail center with parking"), ("ira-brick", "A brick office building"), ("ira-stone", "A stone-faced office and retail building")]))}</div>
</div></section>

<section class="sec i-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card i-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>What IRS rules say about like-kind property, the 45- and 180-day deadlines, qualified intermediaries and Form 8824.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Property Management Midvale, UT | Investment Realty Advisors",
            "meta": "Investment Realty Advisors: property management and real estate brokerage in Midvale and the Salt Lake metro. $380M managed, fees as low as 3%, 1031 support.",
            "body": body, "body_class": "is-home", "og": "ira-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


PAGES = [  # path, key, label, h1, lede, title, meta, image, extra
    ("pm/", "pm", "Property management", "Property Management Services", "Salt Lake area property management.", "Property Management, Midvale &amp; Salt Lake | IRA Utah",
     "IRA property management: quarterly reports, rent collection, maintenance, tenant relations and equity evaluations, with management fees as low as 3% in Utah.", "ira-apts", "report"),
    ("commercial-real-estate/", "commercial_real_estate", "Commercial real estate", "Utah Commercial Real Estate Investments", "Brokerage and portfolio management since 2008.", "Utah Commercial Real Estate Investing &amp; Brokerage | IRA",
     "Full-service commercial brokerage in the Salt Lake metro since 2008: investors, owner-users, 1031 exchanges, value-add, development and leasing. $103M in 2021.", "ira-office", None),
    ("services-4/", "services_4", "Commercial brokerage", "Commercial Real Estate Brokerage Services", "Source, lease and operate your assets.", "Commercial Real Estate Brokerage Services, Utah | IRA",
     "A one-stop solution for commercial and investment real estate in Utah: IRA's brokerage team sources, leases and operates your assets so you can focus on growth.", "ira-tower", None),
    ("residential/", "residential", "Residential investing", "Residential Real Estate Investment", "1-4 unit properties, from purchase to management.", "Residential Real Estate Investing in Utah | IRA Utah",
     "Residential real estate investing in Utah with IRA: buy 1-4 unit properties, value what you own, get professional property management and grow your portfolio.", "ira-house", None),
    ("lux/", "lux", "IRA Lux", "Remodel and House Flip", "Remodel, design, stage, list.", "Remodel, Staging &amp; House Flip Services in Utah | IRA Lux",
     "IRA Lux manages remodeling, design, listing, staging and photography to help Utah homeowners and investors create, sell or find the best home for them.", "ira-living", "lux"),
    ("bank-owned-services/", "bank_owned_services", "REO &amp; bank owned", "REO &amp; Bank-Owned Property Disposition", "Evaluate, maximize, market, close.", "REO &amp; Bank-Owned Property Disposition in Utah | IRA Utah",
     "REO and bank-owned property disposition and liquidation in Utah: IRA evaluates value and equity, prepares the property, markets for full exposure and closes.", "ira-midcentury", None),
    ("sellerfinance/", "sellerfinance", "Seller finance", "Seller Finance", "How seller financing works.", "Seller Financing for Utah Real Estate Explained | IRA",
     "How seller financing works for Utah real estate: the seller finances part or all of the price and the buyer pays the seller directly, on negotiated terms.", "ira-stone", None),
    ("use-cases/", "use_cases", "Performance", "Current &amp; Past Performance", "What IRA manages and has brokered.", "Current &amp; Past Performance | Investment Realty Advisors",
     "Investment Realty Advisors manages commercial and residential real estate in Utah and provides third-party property management, leasing and brokerage services.", "ira-render2", None),
    ("benefits/", "benefits", "Resident benefits", "Resident Benefits Package", "What tenants get for $45/month.", "Resident Benefits Package | Investment Realty Advisors",
     "IRA's Resident Benefits Package for tenants: liability insurance coverage and the other benefits included for $45 a month, explained in plain language.", "ira-kitchen2", None),
    ("portal/", "portal", "Tenant portal", "Tenant Portal &amp; Renter FAQ", "Pay rent, request maintenance, find answers.", "Tenant Portal &amp; Renter FAQ | Investment Realty Advisors",
     "IRA tenant portal and renter FAQ: pay rent online, submit maintenance requests, access records, and find answers to common renter questions in Utah.", "ira-exterior", None),
    ("ownerportal/", "ownerportal", "Owner portal", "Owner Portal &amp; Asset Management", "Be an investor, not a landlord.", "Owner Portal &amp; Asset Management | Investment Realty Advisors",
     "IRA asset management for owners: tenants, vacancies, rent collection, maintenance and HOA requirements handled, so you can be an investor, not a landlord.", "ira-twostory", None),
    ("siterequirements/", "siterequirements", "Site requirements", "Commercial Site Requirements", "Tell us what space you need.", "Commercial Site Requirements &amp; Tenant Rep | IRA Utah",
     "Looking for commercial space in Utah? IRA's agents lease hundreds of thousands of square feet and place tenants daily. Submit your space and site requirements.", "ira-retail", None),
    ("about/", "about", "About", "Why Investment Realty Advisors?", "Full-service brokerage and property management.", "About Investment Realty Advisors | Utah Brokerage &amp; PM",
     "Why Investment Realty Advisors: brokerage plus property management in one ecosystem, deal sourcing, 1031 exchange help and 19+ years in the Salt Lake market.", "ira-aerial", None),
    ("elliot/", "elliot", "Elliot Abel", "Elliot Abel, Associate Broker", "Commercial leasing and brokerage.", "Elliot Abel, Associate Broker | Investment Realty Advisors",
     "Elliot Abel, associate broker at Investment Realty Advisors and co-founder of IRVA Development: commercial leasing, brokerage and development in Utah.", None, None),
    ("privacypolicy/", "privacypolicy", "Privacy Policy", "Privacy Policy", "", "Privacy Policy | Investment Realty Advisors, LLC, Utah",
     "Investment Realty Advisors privacy policy: what information our website collects, how we use it, SMS consent when you share your phone number, and your choices.", None, None),
    ("post/manage-your-blog-from-your-live-site/", "post_manage_your_blog_from_your_live_site", "First property", "I Bought My First Property! Now What?!", "By Joseph Mills &middot; Jan 13, 2022", "I Bought My First Property! Now What? | IRA Utah Blog",
     "Getting started in real estate investing is exciting, but what comes after closing? Joseph Mills on finding tenants and your first steps as a landlord.", "ira-ranch", "post"),
]
NOINDEX = [("listings/", "listings", "Commercial Listings"), ("utahlistings/", "utahlistings", "Utah Residential Listings"), ("investment-properties-for-sale/", "investment_properties_for_sale", "Investment Properties For Sale"),
           ("brokerage/", "brokerage", "For Sale in Utah"), ("residential-search/", "residential_search", "Residential Property Search"), ("utahmarket/", "utahmarket", "On the Market"),
           ("forrent/", "forrent", "For Rent in Utah"), ("copy-of-for-rent/", "copy_of_for_rent", "For Rent"), ("partners/", "partners", "Affiliate Companies"),
           ("contactcre/", "contactcre", "Contact Our CRE Leasing Team"), ("contactiramaintanance/", "contactiramaintanance", "Maintenance Requests"), ("contactresidentialleasing/", "contactresidentialleasing", "Residential Leasing"),
           ("contactstorage/", "contactstorage", "Storage Contact"), ("commercialclientcontact/", "commercialclientcontact", "Commercial Tenants"), ("residentialtenantcontact/", "residentialtenantcontact", "Residential Tenants"),
           ("teamscallwithelliot/", "teamscallwithelliot", "Contact CRE"), ("team/", "team", "Team"), ("team/brian-chung/", "team_brian_chung", "Team"), ("team/ashley-amerson/", "team_ashley_amerson", "Team"),
           ("team/brad-grecco/", "team_brad_grecco", "Team"), ("general-7/", "general_7", "General"), ("copy-of-thank-you/", "copy_of_thank_you", "Thank You"), ("thankyou/", "thankyou", "Thank You"),
           ("applicationrequest/", "applicationrequest", "Application Request"), ("about-3/", "about_3", "Careers"), ("about-3-1/", "about_3_1", "Vendor Application"), ("about-3-2/", "about_3_2", "We're Hiring"),
           ("copy-of-property-management/", "copy_of_property_management", "Owner Portal")]


def make_pages():
    out = [home()]
    for path, key, label, h1, lede, title, meta, im, extra in PAGES:
        body = render(key)
        if extra == "report":
            body = re.sub(r"(?s)<h2>Owner portal</h2>\s*", "", re.sub(r"(?s)<h2>Our resume</h2>.*?(?=<h2>Why hire)", "", body))
            body = '<p class="answer">Our property managers take care of your properties so you can focus on being an investor. Questions? Contact Porter Criddle, Business Development, at <a href="tel:+13852840123">385-284-0123</a>.</p>' + \
                   f'<div class="kpis">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in STATS)}</div>' + body + \
                   f'<figure class="report">{img("ira-report", "An example IRA property report chart comparing estimated and actual net operating income and distributions by month")}<figcaption>From an example IRA owner report.</figcaption></figure>'
        elif extra == "lux":
            body += '<div class="pgal">' + "".join(f"<figure>{img(n, a)}</figure>" for n, a in (("ira-kitchen", "A remodeled kitchen with a large island"), ("ira-kitchen2", "A remodeled kitchen with pendant lights"), ("ira-living", "A staged living room"), ("ira-exterior", "A remodeled home exterior"), ("ira-deck", "A covered deck at sunset"), ("ira-ranch", "A remodeled ranch home"))) + "</div>"
        elif extra == "post":
            body = re.sub(r"<p>All Posts Search.*?</p>", "", body)
        if key == "about":
            body = '<p class="answer">IRA combines property management with a brokerage firm. Instead of working with several companies, we take care of everything in one real estate investment ecosystem.</p>' + body
        if key == "use_cases":
            body = '<p class="answer">Investment Realty Advisors currently manages $400M+ of commercial and residential real estate in Utah, brokering $120M+ in sales transactions and $40M+ in leases over the past 24 months.</p>' + body
        if key == "portal":
            body = '<p class="answer">Tenants: pay rent online, submit maintenance requests and access records through the tenant portal. Maintenance: (801) 528-4557 ext. 4. Emergencies: ext. 6.</p>' + body
        if key == "elliot":
            body = '<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13852557300">385-255-7300</a></dd></div><div><dt>Email</dt><dd><a href="mailto:elliot@iraut.com">elliot@iraut.com</a></dd></div><div><dt>License</dt><dd>UT #9416637-AB00</dd></div></dl>' + body
        crumbs = [("Blog", "blog/")] if extra == "post" else None
        out.append(K.page(path, label, h1, lede, "Investment Realty Advisors" if extra != "post" else "Blog", title, meta, body or f"<p>{lede}</p>", image=im, alt=re.sub("&amp;", "and", label),
                          crumbs=crumbs, canonical=EXT[key]["canon"] or canon(path), ogtype="article" if extra == "post" else None))
    st = '<p class="answer">Seven self-storage communities across the Wasatch Front. Storage questions: <a href="mailto:storage@iraut.com">storage@iraut.com</a> or (801) 528-4557 ext. 2.</p><div class="cats">' + \
         "".join(f'<div class="cat"><b>{n}</b><span>{a}</span></div>' for n, a in STORAGE) + "</div>"
    out.append(K.page("selfstorage/", "Self storage", "Self Storage Communities", "Seven communities on the Wasatch Front.", "Self storage", "Self Storage Communities, Utah | Investment Realty Advisors",
                      "IRA self-storage communities in Taylorsville, Salt Lake City, Murray, Sunset, Clearfield and Garden City. Call (801) 528-4557 ext. 2 for availability.",
                      st, image="ira-midcentury", alt="A storage and office property", canonical=EXT["selfstorage"]["canon"]))
    con = f'''<p class="answer">Have a question? Reach the right IRA team directly.</p>
<dl class="info"><div><dt>Main</dt><dd><a href="tel:+18015284557">(801) 528-4557</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd><address>411 W 7200 S<br>Midvale, UT 84047</address></dd></div><div><dt>Mailing</dt><dd>869 East 4500 South, PMB 224<br>SLC, UT 84107</dd></div></dl>
<h2>Extensions</h2><ul><li>Storage units: ext. 2</li><li>Residential leasing: ext. 3</li><li>Maintenance: ext. 4</li><li>Tenant relations: ext. 5</li><li>Maintenance emergencies: ext. 6</li></ul>
<p>Commercial leasing: <a href="tel:+14354857070">(435) 485-7070</a>, <a href="mailto:creleasing@iraut.com">creleasing@iraut.com</a>.</p>'''
    out.append(K.page("contactus/", "Contact", "Contact Investment Realty Advisors", "Leasing, management, maintenance and brokerage.", "Contact", "Contact Investment Realty Advisors | Midvale, Utah Office",
                      "Contact Investment Realty Advisors in Midvale: (801) 528-4557 with extensions for storage, leasing, maintenance and tenant relations, or email info@iraut.com.",
                      con, canonical=EXT["contactus"]["canon"], form_side=True))
    bl = '<div class="cats">' + f'<a class="cat" href="@/{p_blog.SLUG}"><b>{p_blog.H1}</b><span>Oct 22, 2026</span><em>Read {ARROW}</em></a>' + \
         f'<a class="cat" href="@/post/manage-your-blog-from-your-live-site/"><b>I bought my first property! Now what?!</b><span>Joseph Mills &middot; Jan 13, 2022</span><em>Read {ARROW}</em></a></div>'
    out.append(K.page("blog/", "Blog", "The IRA Blog", "Notes for Utah real estate investors.", "Blog", "Real Estate Investing Blog | Investment Realty Advisors",
                      "The Investment Realty Advisors blog for Utah real estate investors: 1031 exchange rules, first-property tips, property management and the local market.",
                      bl, canonical=EXT["blog"]["canon"]))
    for path, key, h1 in NOINDEX:
        body = render(key, skip_first=False) if key.startswith(("contact", "commercialclient", "residentialtenant")) or key in ("listings", "forrent", "partners") else ""
        body = (body or "") + f'<p><a class="tlink" href="@/contactus/">Contact IRA {ARROW}</a> &nbsp; <a class="tlink" href="@/pm/">Property management {ARROW}</a></p>'
        canonical = canon("ownerportal/") if key == "copy_of_property_management" else (EXT[key]["canon"] or canon(path))
        out.append(K.page(path, h1, h1, "", "Investment Realty Advisors", f"{h1} | Investment Realty Advisors"[:60], f"{h1}: Investment Realty Advisors, property management and real estate brokerage in Utah. Call (801) 528-4557 or email info@iraut.com."[:160],
                          body, canonical=canonical, robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Property management", "pm/"), ("Commercial", "commercial-real-estate/"), ("Contact", "contactus/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (801) 528-4557.", " Midvale, Utah.")) for x in out]
