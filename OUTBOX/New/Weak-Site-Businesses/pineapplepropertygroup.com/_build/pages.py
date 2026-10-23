"""Pages for the pineapplepropertygroup.com redesign: "The owner's ledger".

Pineapple sells property management to investors on numbers: a 5% fee where others charge 10% or more, 90 days free, and monthly
reports on occupancy, repair time, cash on cash and NOI. Their site already has an "Investment Valuation Tool", but its result box is
lorem ipsum. So the signature is that tool, rebuilt and working: enter a rental's price, financing, rent and expenses, and an owner
statement fills in (NOI, cap rate, cash flow, cash on cash) with a side-by-side of a 5% versus a 10% management fee and what 90 fee-free
days are worth. The home page opens on a credited photo of a historic downtown Salt Lake City apartment building, the kind of multi-unit
rental they specialise in. Conifer green and pineapple gold; Instrument Serif, Manrope, JetBrains Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 10 URLs (www, no trailing slash); /Team and /Brokerageservices are empty duplicates, kept noindex. One new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, CITIES
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer
cta = K.cta

KPIS = [("99.2%", "Unit occupancy rate", "Occupancy over the last 12 months, tracked for each property and reported to owners."),
        ("18 hrs", "Repair &amp; issue attendance time", "Our goal is to attend any issue arising from the property in under 24 hours."),
        ("10%", "Cash on cash", "We track this so your cash-on-cash percentage grows."),
        ("32%", "Average net operating income", "An important measure of your property&rsquo;s health, used to determine its market value.")]
INVEST = ["Monthly income &amp; expense reports", "Good Landlord Program certification from the city", "Assistance with obtaining a business license", "Real estate related issues consulting",
          "Monthly NOI &amp; property value analysis", "Monthly cash-on-cash analysis", "1031 exchange analysis &amp; recommendations", "Yearly homeowners insurance bids", "Performance-based compensation", "Property expenses consulting"]
TENANT = ["New tenant finding", "Monthly occupancy rate tracking &amp; reporting", "Collection of rents", "3 different payment options for tenants", "Credit &amp; background checks",
          "New lease signed each year", "Management of delinquent accounts", "Expense payments &amp; tracking", "Independent tenant satisfaction surveys"]
MAINT = ["Repair request management", "Repair turn-around time measured", "Seasonal maintenance", "Remodels &amp; upgrades", "In-house interior designers", "Permit liaison with the city",
         "Semiannual safety audits", "Independent vendor satisfaction surveys", "Installation of security equipment with remote access", "Below-market repair costs"]
PROPS = [("435 S. 400 E.", "Salt Lake City", "6.5", "4.80%", "28%"), ("615 E. 700 S.", "Salt Lake City", "8", "6.30%", "35%"), ("462 E. Granite Ave.", "South Salt Lake", "7", "3.80%", "23%"),
         ("225 E. Kensington Ave", "Salt Lake City", "7", "3.60%", "19%"), ("1110 E. 200 S.", "Salt Lake City", "4", "6.90%", "32%")]
REVIEWS = [("Awesome response time and great properties. Having Sonia as mediator has been awesome in getting things squared away quickly and negotiating. Highly recommend!", "Andie F."),
           ("Had a wonderful experience with PPG! Sonia was so quick to communicate and has a great, bubbly personality. Very pleased with my new rental and feel very confident in my upcoming interactions with them.", "Madie P."),
           ("Quick to get back to us with answers to all of our questions. The process of being able to schedule a viewing, apply, and move in has all been a breeze so far. Looking forward to becoming a tenant!", "Sandi E."),
           ("I had a great experience finding a place with Pineapple Property Group! The showings were great, I was given ample time to look around. When the first place I looked at didn&rsquo;t work out for me, they showed me other places they had to offer.", "Natalie H."),
           ("Super simple and stress free. Easy to work with and on top of everything. Highly recommend!", "Jared K.")]
TEAM = [("pp-jordan", "Jordan Stephens", "CEO &amp; Principal Broker"), ("pp-marthes", "Marthes Solamuthu", "Chairman of the Board"), (None, "Hermann &ldquo;Affi&rdquo; Almas", "Investment Specialist, Realtor"),
        ("pp-byron", "Byron Sisam", "Finance Controller"), ("pp-jeanne", "Jeanne Foster", "H/R Manager"), ("pp-brianne", "Brianne &ldquo;B&rdquo; Burt", "Senior Director of Operations"),
        ("pp-justine", "Justine Seifert", "Office Manager"), ("pp-crystal", "Crystal Cisneros", "Assistant Leasing Manager"), (None, "Siddhi Rajan", "Leasing &amp; Office Assistant"),
        (None, "Bernard Thomsen", "Maintenance Technician"), (None, "Justin Curtis", "Maintenance Technician")]
FAQ = [("How much does Pineapple charge for property management?", "<p>Management fees start at just 5% of gross receipts. Our compensation is performance-based: if we raise your net operating income by 10%, we ask for an additional small commission after the first 12 months.</p>"),
       ("Is there a trial period?", "<p>Yes. 90 days with no management fee. Try our property management risk free and cancel at any time; after 90 days the 5% rate begins.</p>"),
       ("What kinds of properties do you manage?", "<p>Multi-unit apartment buildings, condos, townhomes and single-family homes, in and around the Salt Lake City area.</p>"),
       ("What do owners get each month?", "<p>A report with key performance indicators (occupancy, repair attendance time, cash on cash and NOI) along with our financial reports.</p>")]


def calc():
    f = lambda k, l, v, step="1", pre="", suf="": f'<label class="cf"><span>{l}</span><span class="cf-in">{f"<i>{pre}</i>" if pre else ""}<input type="number" inputmode="decimal" min="0" step="{step}" value="{v}" data-k="{k}" aria-label="{html.escape(html.unescape(l))}">{f"<i>{suf}</i>" if suf else ""}</span></label>'
    return f'''<div class="calc" data-calc>
<div class="calc-in"><p class="mono">Your property &middot; example numbers, replace with yours</p>
<fieldset><legend>Purchase &amp; financing</legend>{f("price", "Purchase price", 450000, "1000", "$")}{f("down", "Down payment", 25, "1", "", "%")}{f("closing", "Closing costs", 9000, "500", "$")}{f("rate", "Interest rate", 6.5, "0.05", "", "%")}{f("years", "Loan term", 30, "1", "", "yrs")}</fieldset>
<fieldset><legend>Income</legend>{f("rent", "Total rent per month", 3200, "25", "$")}{f("vac", "Vacancy / turnover", 5, "0.5", "", "%")}</fieldset>
<fieldset><legend>Expenses</legend>{f("tax", "Property tax per year", 2700, "50", "$")}{f("ins", "Insurance per year", 1500, "50", "$")}{f("rep", "Repairs per month", 150, "10", "$")}{f("util", "Utilities &amp; other per month", 120, "10", "$")}</fieldset></div>
<div class="calc-out" aria-live="polite"><div class="stmt-h"><span class="mono">Owner statement &middot; estimate</span><span class="pine" aria-hidden="true"></span></div>
<div class="stmt-big"><div><span>Cash flow / month</span><b data-o="cf">$0</b></div><div><span>Cash on cash</span><b data-o="coc">0%</b></div><div><span>Cap rate</span><b data-o="cap">0%</b></div></div>
<table class="stmt"><tbody><tr><td>Effective rent / year</td><td data-o="egi">$0</td></tr><tr><td>Operating expenses / year</td><td data-o="opex">$0</td></tr><tr><td>Management at 5%</td><td data-o="mgmt">$0</td></tr>
<tr class="tot"><td>Net operating income</td><td data-o="noi">$0</td></tr><tr><td>Mortgage / year</td><td data-o="debt">$0</td></tr></tbody></table>
<div class="cmp"><div><span>Fee at 5%</span><b data-o="f5">$0</b></div><div><span>Fee at 10%</span><b data-o="f10">$0</b></div><div class="cmp-s"><span>Difference / year</span><b data-o="diff">$0</b></div></div>
<p class="free">First 90 days with no management fee: <b data-o="free">$0</b> kept</p>
<a class="btn accent" href="@/contact-us/">Get a free consultation {ARROW}</a>
<p class="small">Estimates only, for comparison. Management is figured on collected rent; &ldquo;10%&rdquo; is the rate Pineapple says other companies charge. Not financial advice.</p></div>
</div>'''


def home():
    body = f'''
<section class="p-hero"><div class="ph-img" data-parallax="0.08">{img("pp-hero", "The historic Belvedere Apartments building on a downtown Salt Lake City street corner", priority=True)}</div>
<div class="wrap ph-in"><div class="ph-txt"><p class="label">Salt Lake City &middot; Integrity. Professionalism. Real Estate.</p>
<h1>Property management in Salt Lake City, <em>from 5%.</em></h1>
<p class="lede">Pineapple Property Group is the trusted real estate expert for independent real estate investors in Salt Lake City and beyond: property management for multi-unit apartment buildings, condos, townhomes and single-family homes, designed to give owners the most net income.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18012079699">{PHONE} Call or text 801-207-9699</a><a class="btn ghost" href="@/Investment-Valuation-Tool/">Run your numbers {ARROW}</a></div></div>
<div class="ph-tag"><span>No management fee</span><b>90 days</b><span>then just 5%. Cancel any time.</span></div></div>
<p class="credit">Belvedere Apartments, Salt Lake City &middot; Chris Light, CC BY-SA 4.0, via Wikimedia Commons</p></section>

<section class="sec p-kpi"><div class="wrap">
<div class="p-head split-h reveal"><div><p class="label">Pineapple measures key performance indicators</p><h2>Every month, <em>the numbers.</em></h2></div><p class="lede">Owners receive a monthly report with these metrics alongside our financial reports. Below are the company averages Pineapple reports.</p></div>
<div class="kpis">{"".join(f'<div class="kp reveal"><b>{a}</b><h3>{t}</h3><p>{d}</p></div>' for a, t, d in KPIS)}</div>
</div></section>

<section class="sec p-calc" id="calc"><div class="wrap">
<div class="p-head split-h reveal"><div><p class="label">Investment valuation tool</p><h2>What would your rental <em>actually earn?</em></h2></div><p class="lede">Change any number and the owner statement updates, including what a 5% fee saves against the 10% or more other companies charge.</p></div>
{calc()}
</div></section>

<section class="sec p-serv"><div class="wrap">
<div class="p-head reveal"><p class="label">Why choose Pineapple</p><h2>More than <em>rent collection.</em></h2></div>
<div class="lists">{"".join(f'<div class="ls reveal"><h3>{t}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for t, items in (("Investment services", INVEST), ("Tenant services", TENANT), ("Maintenance services", MAINT)))}</div>
</div></section>

<section class="p-band"><div class="band-img" data-parallax="0.1">{img("pp-chapman", "A historic brick apartment building in Salt Lake City")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Your partner in every step</p><p>Acquisition, management and sale. We partner with clients to identify properties with high-return potential, then expertly manage them for best performance.</p><a class="tlink" href="@/Brokerage-Services/">Brokerage services {ARROW}</a></blockquote></div>
<p class="credit">Chapman Place, Salt Lake City &middot; Stephaniet, CC BY-SA 3.0, via Wikimedia Commons</p></section>

<section class="sec p-revs"><div class="wrap">
<div class="p-head reveal"><p class="label">What tenants say</p><h2>&ldquo;Super simple <em>and stress free.&rdquo;</em></h2></div>
<div class="revs">{"".join(f'<blockquote class="rev reveal"><p>&ldquo;{q}&rdquo;</p><cite>{n}</cite></blockquote>' for q, n in REVIEWS)}</div>
</div></section>

<section class="sec p-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card p-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What the federal Fair Housing Act requires of landlords, in plain language, from the statute and the Justice Department.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Property Management Salt Lake City | From 5% | Pineapple",
            "meta": "Pineapple Property Group: property management in Salt Lake City for apartments, condos, townhomes and homes. Fees from 5% and 90 days with no management fee.",
            "body": body, "body_class": "is-home", "og": "pp-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    pm = f'''<p class="answer">Pineapple Property Group offers much more to our clients. Management fees start at just 5% of gross receipts, where other management companies will charge 10% or more, and the first 90 days have no management fee.</p>
<h2>Management plan: 5% of gross receipts</h2><p>Our compensation is performance-based: if we raise your net operating income by 10%, then we ask for an additional small commission after the first 12 months. This ensures we will be the hardworking partner for you and your property.</p>
<h2>Key performance indicators, reported monthly</h2><div class="kpis in-prose">{"".join(f'<div class="kp"><b>{a}</b><h3>{t}</h3><p>{d}</p></div>' for a, t, d in KPIS)}</div><p class="small">Company averages as reported by Pineapple Property Group.</p>
<h2>Investment services</h2><ul>{"".join(f"<li>{i}</li>" for i in INVEST)}</ul><h2>Tenant services</h2><ul>{"".join(f"<li>{i}</li>" for i in TENANT)}</ul><h2>Maintenance services</h2><ul>{"".join(f"<li>{i}</li>" for i in MAINT)}</ul>
<p><a class="btn" href="@/Investment-Valuation-Tool/">Run your property&rsquo;s numbers {ARROW}</a></p>
<p class="small photo-credit">Banner photo: Belvedere Apartments, Salt Lake City &middot; Chris Light, CC BY-SA 4.0, via Wikimedia Commons</p>'''
    out.append(K.page("Property-Management/", "Property management", "Property management in Salt Lake City", "5% of gross receipts. 90 days free.", "Property management",
                      "Property Management in Salt Lake City, from 5% | Pineapple", "Salt Lake City property management from 5% of gross receipts, 90 days with no fee, monthly KPI reports and investment, tenant and maintenance services.",
                      pm, image="pp-hero", alt="Belvedere Apartments, Salt Lake City", canonical=canon("Property-Management/"), schema=[K.svc_schema("Property-Management/", "Property management", "Salt Lake City, UT")]))
    br = '''<p class="answer">Pineapple Property Group agents offer residential real estate services as well as investment property services, so they bring an extra level of understanding to the value of any property.</p>
<h2>Acquiring and cashing out investment properties</h2><p>Most anybody you ask would say they are interested in investing in real estate. The problem is that most people do not know how to begin or are not sure they are buying a good property. Others buy a rental that does not perform as they had hoped. We partner with our clients to identify properties with high-return potential and then expertly manage the property for best performance.</p>
<ul><li>Your partner in every step: acquisition, management and sale</li><li>Proven success with multi-unit rental properties</li><li>1031 exchange analysis and consultation</li><li>Expert valuation analysis and negotiating transactions</li><li>Strong lender relationships for competitive financing</li></ul>
<h2>Residential real estate sales</h2><p>A person&rsquo;s home can be their most important investment. We bring our knowledge of valuing properties to residential real estate, so clients buy a home they&rsquo;re happy with and one with the potential to appreciate over time.</p>
<ul><li>Expert valuation analysis and negotiating transactions</li><li>Home repairs and services available for residential owners</li><li>Strong lender relationships for competitive financing</li><li>Knowledge of market trends and areas</li></ul>
<p class="small photo-credit">Banner photo: Chapman Place, Salt Lake City &middot; Stephaniet, CC BY-SA 3.0, via Wikimedia Commons</p>'''
    out.append(K.page("Brokerage-Services/", "Brokerage services", "Brokerage services", "Investment property and residential sales.", "Brokerage",
                      "Investment &amp; Home Brokerage, Salt Lake City | Pineapple", "Pineapple agents handle investment property acquisitions and sales, 1031 exchange analysis and residential buying and selling in Salt Lake City and beyond.",
                      br, image="pp-chapman", alt="Chapman Place apartments, Salt Lake City", canonical=canon("Brokerage-Services/")))
    inv = '<p class="answer">A sample of properties Pineapple manages, with the years managed and the returns Pineapple reports for each.</p><div class="tbl"><table><thead><tr><th>Property</th><th>City</th><th>Years managed</th><th>Cash on cash</th><th>ROI / yr @ 5% cap rate</th></tr></thead><tbody>' + \
          "".join(f"<tr><td>{a}</td><td>{c}</td><td>{y}</td><td>{cc}</td><td>{r}</td></tr>" for a, c, y, cc, r in PROPS) + '</tbody></table></div><p class="small">Figures as published by Pineapple Property Group. Past results don&rsquo;t guarantee future returns.</p>' + \
          f'<p><a class="btn" href="@/Investment-Valuation-Tool/">Run your property&rsquo;s numbers {ARROW}</a></p><p class="small photo-credit">Banner photo: Salt Lake City &middot; Invictus323, CC BY 4.0, via Wikimedia Commons</p>'
    out.append(K.page("Investments/", "Current investments", "Current investments", "Properties we manage, and how they perform.", "Investments",
                      "Current Investment Properties | Pineapple Property Group", "Salt Lake City and South Salt Lake rentals Pineapple manages, with years managed, cash on cash and ROI per year as published by Pineapple Property Group.",
                      inv, image="pp-skyline", alt="Salt Lake City skyline", canonical=canon("Investments/")))
    out.append(K.page("Investment-Valuation-Tool/", "Valuation tool", "Investment valuation tool", "See what your rental really earns.", "Valuation tool",
                      "Rental Property Valuation Tool | Pineapple Property Group", "Free rental property calculator: NOI, cap rate, cash flow and cash on cash, plus a 5% versus 10% management fee comparison and the value of 90 fee-free days.",
                      '<p class="answer">Enter your property&rsquo;s numbers. The owner statement updates as you type. Estimates only, for comparison.</p>' + calc(), canonical=canon("Investment-Valuation-Tool/")))
    port = f'''<p class="answer">Current owners and tenants: use the owner &amp; tenant portal for statements, payments and requests. Questions? Call or text <a href="tel:+18012079699">801-207-9699</a>.</p>
<h2>Where we serve</h2><p>Pineapple Property Group is headquartered in Salt Lake City and performs property management for all types of single-family homes and multi-unit rental properties in and around the Salt Lake City area. We are proudly serving these cities:</p>
<div class="cities">{"".join(f"<span>{c}</span>" for c in CITIES)}</div>'''
    out.append(K.page("Owner-Tenant-Portal/", "Owner &amp; tenant portal", "Owner &amp; tenant portal", "Statements, payments and requests.", "Portal",
                      "Owner &amp; Tenant Portal | Pineapple Property Group, SLC", "Owner and tenant portal access, and the 40 cities Pineapple manages rentals in, from Salt Lake City and Sandy to Ogden, Provo, Park City, Heber and Midway.",
                      port, canonical=canon("Owner-Tenant-Portal/")))
    tm = '<p class="answer">The people behind Pineapple Property Group, from leasing and operations to maintenance.</p><div class="team">' + \
         "".join(f'<div class="tm">{img(im, html.unescape(re.sub("&[lr]dquo;", "", n))) if im else f'<span class="tm-x" aria-hidden="true">{"".join(w[0] for w in re.sub("&[lr]dquo;[^&]*&[lr]dquo;", "", n).split()[:2])}</span>'}<b>{n}</b><span>{r}</span></div>' for im, n, r in TEAM) + "</div>" + \
         '''<h2>Join the Pineapple team</h2><p>Are you a current real estate agent or looking to become one? Our agents are trained on dealing expertly in residential sales as well as investment property sales, and they build relationships with clients for future buying, selling and investing.</p>
<ul><li>Real estate investment training</li><li>Residual monthly income for agents from helping owners invest</li><li>Dynamic property management to service your clients</li><li>Expansion of your services to clients</li><li>Competitive agent commission splits</li></ul>'''
    out.append(K.page("The-Team/", "The team", "The Pineapple team", "Integrity. Professionalism. Real Estate.", "Team", "Meet the Team | Pineapple Property Group, Salt Lake City",
                      "Meet the Pineapple Property Group team in Salt Lake City, led by CEO and principal broker Jordan Stephens, plus leasing, operations and maintenance staff.",
                      tm, canonical=canon("The-Team/")))
    con = '''<p class="answer">We are available for any questions about property management, real estate investing, or buying and selling your home. Visit our office or schedule your consultation.</p>
<dl class="info"><div><dt>Call or text</dt><dd><a href="tel:+18012079699">801-207-9699</a></dd></div><div><dt>Office</dt><dd><address>433 S 400 E #200<br>Salt Lake City, UT 84111</address></dd></div><div><dt>Hours</dt><dd>Mon&ndash;Fri 9am&ndash;5pm<br>Sat&ndash;Sun closed</dd></div></dl>
<p>Ask about 90 days with no management fee.</p>'''
    out.append(K.page("contact-us/", "Contact", "Contact Pineapple Property Group", "Property management, investing, buying or selling.", "Contact",
                      "Contact Pineapple Property Group | Salt Lake City Office", "Contact Pineapple Property Group at 433 S 400 E in Salt Lake City: call or text 801-207-9699, Monday to Friday 9 to 5, for property management or investing.",
                      con, canonical=canon("contact-us/"), form_side=True))
    for path, h1, canon_to in (("Team/", "The team", "The-Team/"), ("Brokerageservices/", "Brokerage services", "Brokerage-Services/")):
        out.append(K.page(path, h1, h1, "", "Pineapple", f"{h1.capitalize()} | Pineapple Property Group, Salt Lake City",
                          f"{h1.capitalize()} at Pineapple Property Group in Salt Lake City. See the full page for details, or call or text 801-207-9699 Monday to Friday.",
                          f'<p><a class="btn" href="@/{canon_to}">{h1.capitalize()} {ARROW}</a></p>', canonical=canon(canon_to), robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Property management", "Property-Management/"), ("Valuation tool", "Investment-Valuation-Tool/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call or text 801-207-9699.", " Salt Lake City, UT.")) for x in out]
