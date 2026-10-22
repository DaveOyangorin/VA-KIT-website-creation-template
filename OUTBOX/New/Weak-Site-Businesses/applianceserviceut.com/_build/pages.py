"""Pages for the applianceserviceut.com redesign: "Service ticket".

ASI is an old-school, family-owned repair shop: more than 25 years in business, nearly 40 in the trade, same or next-day service, a 30-day
guarantee and a printed list of holidays they close. So the home page opens on a full-bleed photo of the Salt Lake skyline (credited), and the
signature is a carbon-copy service ticket: pick your area, appliance and brand, and the ticket confirms they cover it and works out your next
service day from their real hours and holiday list. ASI blue, enamel white, canary ticket yellow, Courier Prime for the typed fields.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 4 URLs (no trailing slash) and canonicals."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

APPS = ["Dishwashers", "Dryers", "Electric appliances", "Freezers", "Garbage disposals", "Gas appliances", "Microwaves", "Refrigerators", "Ranges", "Trash compactors", "Washing machines"]
BRANDS = ["Danby", "Frigidaire", "GE", "Gibson", "Hotpoint", "Kenmore", "KitchenAid", "Magic Chef", "Maytag", "Speed Queen", "Tappan", "Westinghouse", "Whirlpool", "White"]
AREAS = ["Salt Lake City metro", "Ogden metro", "Provo metro", "Tooele metro"]
HOLIDAYS = ["New Year&rsquo;s Day", "Memorial Day", "4th of July", "24th of July", "Labor Day", "Thanksgiving", "Christmas"]
FAQ = [("How fast can you come out?", "<p>We offer same or next-day service, Monday through Friday, 8 am to 5 pm.</p>"),
       ("Do you guarantee your repairs?", "<p>Yes. There&rsquo;s a 30-day guarantee on all service calls, and we guarantee and warranty all work.</p>"),
       ("Who will come to my home?", "<p>Friendly, expert technicians who are drug-free and background approved. We&rsquo;re fully licensed, registered and insured.</p>"),
       ("Where do you work?", "<p>All areas across metro Salt Lake City, plus the Ogden, Provo and Tooele metro areas.</p>"),
       ("How can I pay?", "<p>Visa, Mastercard, Discover, American Express, cash, check and debit.</p>"),
       ("When are you closed?", "<p>Weekends, and on New Year&rsquo;s Day, Memorial Day, the 4th of July, the 24th of July, Labor Day, Thanksgiving and Christmas.</p>")]


def ticket():
    opt = lambda xs, ph: f'<option value="">{ph}</option>' + "".join(f'<option>{x}</option>' for x in xs)
    return f'''<div class="tk" data-ticket><div class="tk-form"><p class="tk-h">Service request</p>
<label>Where are you?<select data-t="area">{opt(AREAS, "Choose your area")}<option value="other">Somewhere else</option></select></label>
<label>What needs fixing?<select data-t="app">{opt(APPS, "Choose an appliance")}</select></label>
<label>What brand is it?<select data-t="brand">{opt(BRANDS, "Choose a brand")}<option value="other">Another brand</option></select></label></div>
<div class="tk-card" aria-live="polite"><div class="tk-top"><span>A.S.I. APPLIANCE SERVICE, INC.</span><span class="tk-no">No. <b data-t-no>0000</b></span></div>
<dl><div><dt>AREA</dt><dd data-t-out="area">&mdash;</dd></div><div><dt>APPLIANCE</dt><dd data-t-out="app">&mdash;</dd></div><div><dt>BRAND</dt><dd data-t-out="brand">&mdash;</dd></div>
<div><dt>NEXT SERVICE</dt><dd data-t-day>&mdash;</dd></div></dl>
<p class="tk-status" data-t-status>Fill in the three fields to check coverage.</p>
<p class="tk-foot">30-DAY GUARANTEE ON ALL SERVICE CALLS &middot; (801) 487-8591</p><span class="tk-stamp" data-t-stamp>COVERED</span></div></div>'''


def home():
    body = f'''
<section class="a-hero"><div class="ah-img" data-parallax="0.08">{img("asi-slc", "Downtown Salt Lake City and the Wasatch foothills under a summer sky", priority=True)}</div>
<div class="wrap ah-in"><div class="ah-txt"><p class="label">Salt Lake City &middot; Family owned &middot; 25+ years in business</p>
<h1>Appliance repair in Salt Lake City, <em>same or next day.</em></h1>
<p class="lede">Has your dryer left your clothes damp, despite running all day? ASI Appliance Service has repair technicians all over the valley, with reasonable rates, trustworthy service and a 30-day guarantee on every call.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Schedule service {ARROW}</a><a class="btn ghost" href="tel:+18014878591">{PHONE} (801) 487-8591</a></div></div>
<div class="ah-badge"><b>30</b><span>day guarantee<br>on all service calls</span></div></div>
<p class="credit">Salt Lake City &middot; Garrett, CC BY 2.0, via Wikimedia Commons</p></section>

<section class="a-why"><div class="wrap why"><div><b>25+ years</b><span>of continued professional service</span></div><div><b>~40 years</b><span>of experience in the industry</span></div>
<div><b>Drug-free</b><span>background-approved technicians</span></div><div><b>Licensed</b><span>registered &amp; insured</span></div></div></section>

<section class="sec a-tk" id="ticket"><div class="wrap">
<div class="a-head split-h reveal"><div><p class="label">Check coverage</p><h2>Fill out the ticket. <em>We&rsquo;ll take it from there.</em></h2></div><p class="lede">Pick your area, appliance and brand. The ticket checks what we cover and when you could see a technician, based on our real hours and holidays.</p></div>
{ticket()}
</div></section>

<section class="sec a-svc"><div class="wrap a-svc-in">
<div class="reveal"><p class="label">What we repair</p><h2>Eleven kinds of appliance. <em>Most brand names.</em></h2><p class="lede">Repair and maintenance for homeowners, landlords and apartment complexes. There&rsquo;s no need to spend money on a new appliance.</p><a class="tlink" href="@/services/">All services {ARROW}</a></div>
<div class="reveal"><ul class="apps">{"".join(f"<li>{a}</li>" for a in APPS)}</ul><p class="label" style="margin-top:22px">Brands we service</p><ul class="brands">{"".join(f"<li>{b}</li>" for b in BRANDS)}</ul></div>
</div></section>

<section class="a-band"><div class="band-img" data-parallax="0.1">{img("asi-mtn", "Downtown Salt Lake City in front of the snowy Wasatch Range")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our promise</p><p>Quality work and personalized service you can rely on. We fit your schedule, and our service is guaranteed, so we can keep earning your business year after year.</p></blockquote></div>
<p class="credit">Salt Lake City &middot; Streamline1989, public domain, via Wikimedia Commons</p></section>

<section class="sec a-area"><div class="wrap a-area-in">
<div class="reveal"><p class="label">Where we work</p><h2>Repair people <em>all over the valley.</em></h2><ul class="areas">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul>
<p>Come visit our Salt Lake City shop or call <a href="tel:+18014878591">(801) 487-8591</a> for service.</p></div>
<div class="reveal hrs"><p class="label">Hours</p><dl><div><dt>Monday&ndash;Friday</dt><dd>8:00 AM &ndash; 5:00 PM</dd></div><div><dt>Saturday &amp; Sunday</dt><dd>Closed</dd></div></dl>
<p class="label" style="margin-top:18px">Closed on</p><ul class="hol">{"".join(f"<li>{h}</li>" for h in HOLIDAYS)}</ul></div>
</div></section>

<section class="sec a-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Good to <em>know.</em></h2>
<a class="post-card a-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>Why failure to clean is the leading cause of dryer fires, and the habits NFPA and the U.S. Fire Administration recommend.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Appliance Repair Salt Lake City | ASI Appliance Service",
            "meta": "Family-owned appliance repair in Salt Lake City, Ogden, Provo and Tooele for 25+ years. Same or next-day service and a 30-day guarantee. (801) 487-8591.",
            "body": body, "body_class": "is-home", "og": "asi-slc", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    sv = f'''<p class="answer">Serving residential customers, ASI Appliance Service, Inc. offers repair and maintenance for all major appliances in most brand names, with a 30-day guarantee on all service calls.</p>
<h2 id="appliances">Appliances we repair</h2><ul class="apps in">{"".join(f"<li>{a}</li>" for a in APPS)}</ul>
<h2 id="brands">Brands we service</h2><ul class="brands in">{"".join(f"<li>{b}</li>" for b in BRANDS)}</ul>
<h2>Check your coverage</h2>{ticket()}'''
    out.append(K.page("services/", "Services", "Appliance Repair Services", "Repair and maintenance for all major appliances.", "Services", "Appliance Repair Services, Salt Lake City | ASI Appliance",
                      "ASI repairs dishwashers, dryers, washers, refrigerators, freezers, ranges, microwaves, disposals and more, from GE to Whirlpool, with a 30-day guarantee.",
                      sv, image="asi-mtn", alt="Salt Lake City and the Wasatch", canonical=EXT["services"]["canon"], faqs=FAQ[:2],
                      schema=K.svc_schema("services/", "Appliance repair", "Salt Lake City, UT")))
    ab = '''<p class="answer">Locally owned ASI Appliance Service, Inc. has more than 25 years of continued professional service, and nearly 40 years of experience in the industry.</p>
<p>Our friendly, expert technicians, drug-free and background approved, will be on site promptly, using the latest tools and technology to get your appliance running like new again. There&rsquo;s no need to spend money on a new appliance. Whether you&rsquo;re a homeowner, landlord or apartment complex, we&rsquo;ll be there to repair all major appliances in most brand names.</p>
<ul class="ticks"><li>Fully licensed, registered and insured</li><li>We guarantee and warranty all work</li><li>30-day guarantee on all service calls</li><li>Same or next-day service</li></ul>
<p>We&rsquo;re an experienced team of dedicated professionals who will fix your appliances promptly and cheerfully. We offer quality work and personalized service you can rely on, fit your schedule, and keep earning your repeat business year after year.</p>'''
    out.append(K.page("about-us/", "About", "About ASI Appliance Service", "Family owned for more than 25 years.", "About", "About ASI Appliance Service | Salt Lake City, 25+ Years",
                      "ASI Appliance Service is a family-owned Salt Lake City repair company: 25+ years in business, drug-free technicians, licensed and insured, 30-day guarantee.",
                      ab, image="asi-slc", alt="Salt Lake City", canonical=EXT["about_us"]["canon"]))
    con = f'''<p class="answer">We look forward to getting your appliances running like new again. We offer same or next-day service.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18014878591">(801) 487-8591</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Address</dt><dd><address>2755 S 300 W<br>Salt Lake City, UT 84115</address></dd></div><div><dt>Hours</dt><dd>Monday&ndash;Friday 8:00 AM&ndash;5:00 PM<br>Saturday &amp; Sunday closed</dd></div></dl>
<h2>Holidays we are closed</h2><ul>{"".join(f"<li>{h}</li>" for h in HOLIDAYS)}</ul>
<h2>Areas we serve</h2><ul>{"".join(f"<li>{a}</li>" for a in AREAS)}</ul>
<h2>Payment options</h2><p>Visa, Mastercard, Discover, American Express, cash, check and debit.</p>'''
    out.append(K.page("contact/", "Contact", "Contact ASI Appliance Service", "Same or next-day service.", "Contact", "Contact ASI Appliance Service | Salt Lake City Repair",
                      "Contact ASI Appliance Service in Salt Lake City: call (801) 487-8591 or email for same or next-day appliance repair, Monday to Friday, 8 am to 5 pm today.",
                      con, canonical=EXT["contact"]["canon"], form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (801) 487-8591.", " 30-day guarantee.")) for x in out]
