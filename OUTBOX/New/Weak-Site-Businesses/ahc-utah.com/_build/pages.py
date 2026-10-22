"""Pages for the ahc-utah.com redesign: "Both seasons".

An HVAC company in Salt Lake City works two opposite seasons: January inversions and snow, July heat. So the home page opens on a full-bleed
photo of a Salt Lake park in snow that becomes the same kind of park in summer when you turn the thermostat card from HEAT to COOL; the set
point, the photo, the colour of the page and the list of services all follow the mode (it starts in the season it is). Slate blue and ember
from their logo, Bricolage Grotesque, Public Sans and DM Mono read-outs.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (editorial headline over a photo), ArchDaily (grid).
Same 17 URLs (no trailing slash, same capitalization) on the www host."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

GROUPS = [("heating", "Heating", "Furnaces and heating", ["Residential furnace installation", "Furnace repairs", "Furnace tune-ups", "Service and maintenance agreements", "Mechanical inspections"]),
          ("cooling", "Cooling", "Air conditioning", ["Residential air conditioning installation", "Central air and split systems", "Ductless systems", "Air conditioning tune-ups and repairs", "Swamp cooler removal"]),
          ("air", "Air", "Indoor air quality", ["Air cleaners", "Humidifiers", "UV lights", "Exhaust fans", "Indoor air quality solutions"]),
          ("commercial", "Commercial", "Commercial HVAC", ["Commercial furnace and air conditioning installation", "Commercial rooftop units and packaged units", "Commercial service and maintenance", "Commercial repairs", "Tenant finish and improvements"]),
          ("construction", "Building", "New construction and remodels", ["Residential new construction", "Commercial new construction", "Home remodels", "Basement finishes"])]
MODELS = {"Carrier": {"Air conditioners": ["24VNA9", "24VNA6", "24TPA7", "24SCA4", "24SCA5"], "Furnaces": ["58TN", "59TN6", "58TP", "59TP6", "58SB", "59SC6"], "Indoor air quality": ["Air purification", "Humidifiers", "UV lights"]},
          "Lennox": {"Air conditioners": ["SL28", "XC21", "EL23", "EL18", "ML18", "ML17"], "Furnaces": ["SLP99", "SL280", "EL280", "EL296", "ML296", "ML196", "ML193", "ML180"], "Indoor air quality": ["Air purification", "Humidifiers", "UV lights"]}}
WHY = [("Customer service", "Professional, reliable and, most of all, affordable."), ("Best value", "No substandard work, craftsmanship or discounted parts. A plan that fits your budget."),
       ("Industry reputation", "Earned the good-old-fashioned way, one relationship at a time.")]
FAQ = [("Do you service all brands?", "<p>Yes. We offer sales, installations and service on all makes and models. We sell Carrier and Lennox equipment.</p>"),
       ("Do you offer emergency service?", "<p>Yes, 24-hour emergency service. Our office is open Monday to Friday, 8 am to 5 pm, at 155 Baird Ave in Salt Lake City.</p>"),
       ("Can I finance a new furnace or air conditioner?", "<p>Yes. We offer financing, on approved credit, through Service Finance Company. You can often get a response the same day.</p>"),
       ("Do you work on commercial buildings?", "<p>Yes: commercial installs, rooftop and packaged units, service and maintenance, repairs, new construction and tenant improvements.</p>")]
CREDITS = {"winter": "Sugar House Park in snow &middot; claralieu, CC BY 2.0", "summer": "Liberty Park, Salt Lake City &middot; Pollardjosephd, CC BY-SA 4.0"}


def thermostat():
    return f'''<div class="tstat" data-tstat role="group" aria-label="Thermostat: switch between heating and cooling">
<div class="ts-modes"><button type="button" data-mode="heat" aria-pressed="true">Heat</button><button type="button" data-mode="cool" aria-pressed="false">Cool</button></div>
<div class="ts-dial"><svg viewBox="0 0 200 200" aria-hidden="true"><circle class="ts-track" cx="100" cy="100" r="84"/><circle class="ts-arc" cx="100" cy="100" r="84" pathLength="100" data-arc/></svg>
<div class="ts-read"><span class="ts-set" data-set>70</span><span class="ts-deg">&deg;F</span><span class="ts-lab" data-lab>Heating to</span></div>
<button type="button" class="ts-btn up" data-step="1" aria-label="Raise set point">+</button><button type="button" class="ts-btn dn" data-step="-1" aria-label="Lower set point">&minus;</button></div>
<p class="ts-note" data-note>Furnace installs, repairs and tune-ups, all makes and models.</p></div>'''


def home():
    tabs = "".join(f'<button type="button" class="sv-tab{" on" if i == 0 else ""}" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}">{s}</button>' for i, (k, s, t, l) in enumerate(GROUPS))
    panels = "".join(f'<div class="sv-panel{" on" if i == 0 else ""}" data-panel="{k}"><h3>{t}</h3><ul>{"".join(f"<li>{x}</li>" for x in l)}</ul><a class="tlink" href="@/services/#{k}">More on {t.lower()} {ARROW}</a></div>' for i, (k, s, t, l) in enumerate(GROUPS))
    brands = "".join(f'<div class="brand-c"><h3>{b}</h3>' + "".join(f'<div class="bc-row"><span>{cat}</span><b>{" &middot; ".join(m)}</b></div>' for cat, m in cats.items()) +
                     f'<a class="tlink" href="@/{"Carrier-Equipment" if b == "Carrier" else "Lennox"}/">{b} products {ARROW}</a></div>' for b, cats in MODELS.items())
    body = f'''
<section class="a-hero mode-heat" data-season><div class="ah-img winter">{img("ahc-winter", "Sugar House Park in Salt Lake City covered in snow below the Wasatch", priority=True)}</div>
<div class="ah-img summer">{img("ahc-summer", "Liberty Park lake in Salt Lake City on a summer day")}</div>
<div class="wrap ah-in"><div class="ah-txt"><p class="label">Salt Lake City &middot; Family owned &middot; Third generation</p>
<h1>HVAC company in Salt Lake City, <em data-h1em>for the coldest mornings.</em></h1>
<p class="lede">Affordable Heating &amp; Cooling sells, installs and services furnaces and air conditioners, all makes and models, for homes and businesses across the Salt Lake Valley. 24-hour emergency service.</p>
<div class="btn-row"><a class="btn accent" href="@/Contact/">Request a free estimate {ARROW}</a><a class="btn ghost" href="tel:+18012610924">{PHONE} 801.261.0924</a></div></div>
{thermostat()}</div>
<p class="ah-credit"><span data-credit>{CREDITS["winter"]}</span>, via Wikimedia Commons</p></section>

<section class="a-why"><div class="wrap why">{"".join(f'<div><b>{t}</b><span>{d}</span></div>' for t, d in WHY)}</div></section>

<section class="sec a-svc" id="services"><div class="wrap a-svc-in">
<div class="reveal"><p class="label">What we do</p><h2>Every season, <em>every system.</em></h2><p class="lede">Sales, installations and service on all makes and models, plus 24-hour emergency service. Pick a season.</p>
<div class="sv-tabs" role="group" aria-label="Service groups">{tabs}</div></div>
<div class="sv-panels reveal">{panels}</div>
</div></section>

<section class="a-air"><div class="band-img" data-parallax="0.1">{img("ahc-inversion", "A winter inversion layer of haze over the Salt Lake Valley")}</div>
<div class="wrap a-air-in"><div class="reveal"><p class="label">Indoor air quality</p><h2>When the valley air turns, <em>your indoor air doesn&rsquo;t have to.</em></h2>
<p>Air cleaners, humidifiers, UV lights and exhaust fans, from Carrier and Lennox, installed and serviced by our team.</p><a class="btn accent" href="@/services/#air">Indoor air quality {ARROW}</a></div></div>
<p class="ah-credit">Salt Lake Valley inversion &middot; Derrellwilliams, CC BY-SA 4.0, via Wikimedia Commons</p></section>

<section class="sec a-fam"><div class="wrap a-fam-in">
<div class="reveal fam-num"><b>3rd</b><span>generation, family owned and operated</span><b>50+</b><span>years of experience</span><b>20+</b><span>years serving the Salt Lake Valley</span></div>
<div class="reveal"><p class="label">About Affordable</p><h2>A plan that fits <em>your budget.</em></h2>
<p>We recognize there are a variety of good and honest competitors in our industry. So our goal is to earn your trust the good-old-fashioned way, with service that is professional, reliable and, most of all, affordable.</p>
<p>We won&rsquo;t be a low-cost leader by furnishing substandard work, craftsmanship or discounted parts. We will promise to do our best and create a plan and service that fits within your budget.</p>
<a class="tlink" href="@/About-Affordable/">About us {ARROW}</a></div>
</div></section>

<section class="sec a-brands"><div class="wrap">
<div class="a-head split-h reveal"><div><p class="label">Equipment</p><h2>Carrier and Lennox, <em>sold and installed.</em></h2></div><a class="tlink" href="@/Products/">All products {ARROW}</a></div>
<div class="brands">{brands}</div></div></section>

<section class="sec a-fin"><div class="wrap a-fin-in reveal"><div><p class="label">Financing</p><h2>A new system, <em>paid over time.</em></h2><p>Financing on approved credit through Service Finance Company. Apply online and get a response as soon as the same day.</p></div>
<a class="btn" href="@/Financing/">See financing {ARROW}</a></div></section>

<section class="sec a-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Good to <em>know.</em></h2>
<a class="post-card a-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>Where carbon monoxide comes from in a home, the symptoms to know, and where CO alarms belong.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "HVAC Company Salt Lake City | Affordable Heating &amp; Cooling",
            "meta": "Affordable Heating &amp; Cooling: family-owned HVAC company in Salt Lake City. Furnace and AC sales, installs and repair, all makes and models, 24-hour service.",
            "body": body, "body_class": "is-home", "og": "ahc-winter", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def models_page(path, brand, cat, title, meta, image=None):
    m = MODELS[brand][cat]
    cards = "".join(f'<div class="mcard"><span class="m-k">{brand}</span><b>{x}</b></div>' for x in m)
    body = f'''<p class="answer">{brand} {cat.lower()} we sell, install and service. Ask us which one fits your home and budget; every install starts with a free estimate.</p>
<div class="mgrid">{cards}</div><h2>Not sure which one?</h2><p>Call <a href="tel:+18012610924">801.261.0924</a> or <a href="@/Contact/">request a free estimate</a>. We service all makes and models, not just the ones we sell.</p>'''
    return K.page(path, f"{brand} {cat}", f"{brand} {cat}", "Sold, installed and serviced in Salt Lake City.", "Products", title, meta, body,
                  crumbs=[("Products", "Products/"), (brand, "Carrier-Equipment/" if brand == "Carrier" else "Lennox/")], canonical=canon(path))


def brand_page(path, brand):
    links = {"Air conditioners": f"{brand}-Air-Conditioners/", "Furnaces": f"{brand}-Furnaces/", "Indoor air quality": f"{brand}-Indoor-Air-Quality/"}
    cards = "".join(f'<a class="cat" href="@/{links[c]}"><b>{c}</b><span>{" &middot; ".join(m)}</span><em>View {ARROW}</em></a>' for c, m in MODELS[brand].items())
    return K.page(path, f"{brand} products", f"{brand} Products", "Air conditioners, furnaces and indoor air quality.", "Products",
                  f"{brand} Furnaces &amp; Air Conditioners | Affordable H&amp;C",
                  f"{brand} air conditioners, furnaces and indoor air quality products, sold, installed and serviced by Affordable Heating &amp; Cooling in Salt Lake City, UT.",
                  f'<p class="answer">{brand} equipment we sell, install and service in the Salt Lake Valley.</p><div class="cats">{cards}</div>', crumbs=[("Products", "Products/")], canonical=canon(path))


def make_pages():
    out = [home()]
    sv = '<p class="answer">We service and install all makes and models. We offer installs, sales and 24-hour emergency service for homes and businesses across the Salt Lake Valley.</p>' + \
         "".join(f'<h2 id="{k}">{t}</h2><ul>{"".join(f"<li>{x}</li>" for x in l)}</ul>' for k, s, t, l in GROUPS) + \
         '<h2>Equipment</h2><p>We sell and install <a href="@/Carrier-Equipment/">Carrier</a> and <a href="@/Lennox/">Lennox</a> furnaces, air conditioners and indoor air quality products.</p>'
    out.append(K.page("services/", "Services", "Heating &amp; Air Conditioning Services", "All makes and models. 24-hour emergency service.", "Services",
                      "HVAC Services in Salt Lake City | Affordable Heating",
                      "Furnace and air conditioning installation, repair, tune-ups and maintenance agreements, plus indoor air quality and commercial HVAC in Salt Lake City.",
                      sv, image="ahc-winter", alt="Sugar House Park in snow", canonical=canon("services/"), faqs=FAQ[:2],
                      schema=K.svc_schema("services/", "Heating and air conditioning", "Salt Lake City, UT")))
    ab = f'''<p class="answer">Servicing the Salt Lake Valley for more than two decades and with over 50 years of experience, Affordable Heating &amp; Cooling, Inc. is a family owned and operated company that offers affordable products and honest services.</p>
<p>In our third generation of family operation, we promise to offer the best quality in high-efficiency products for all your heating, ventilation and air conditioning needs. We offer sales, installations and service on all makes and models.</p>
<h2>Why choose Affordable</h2><p>We recognize there are a variety of good and honest competitors in our industry. Our goal is to earn a relationship the good-old-fashioned way and build your trust with service that is professional, reliable and, most of all, affordable. Because we strive to be better each time, we won&rsquo;t be a low-cost leader by furnishing substandard work, craftsmanship or discounted parts. We will promise to do our best and create a plan and service that fits within your budget.</p>
<h2>Services include</h2><ul>{"".join(f"<li>{x}</li>" for k, s, t, l in GROUPS for x in l)}</ul>'''
    out.append(K.page("About-Affordable/", "About", "About Affordable Heating &amp; Cooling", "Family owned. Third generation. All makes and models.", "About",
                      "About Affordable Heating &amp; Cooling, Inc. | Salt Lake HVAC",
                      "Family owned and operated in its third generation, Affordable Heating &amp; Cooling has served the Salt Lake Valley for over two decades. All makes and models.",
                      ab, image="ahc-summer", alt="Liberty Park in summer", canonical=canon("About-Affordable/")))
    out.append(K.page("About-Us/", "About us", "About Us", "Family owned. Third generation.", "About", "About Us | Affordable Heating &amp; Cooling, Salt Lake City",
                      "About Affordable Heating &amp; Cooling, Inc.: a family-owned, third-generation heating and air conditioning company in Salt Lake City. Read our story today.",
                      ab, image="ahc-summer", alt="Liberty Park in summer", canonical=canon("About-Affordable/"), sitemap=False))
    out.append(K.page("Products/", "Products", "Products", "Carrier and Lennox equipment.", "Products", "Carrier &amp; Lennox HVAC Products | Affordable Heating",
                      "Carrier and Lennox furnaces, air conditioners and indoor air quality products, sold, installed and serviced in Salt Lake City by Affordable Heating &amp; Cooling.",
                      '<p class="answer">We sell and install equipment from two brands, and service all makes and models.</p><div class="cats">' +
                      "".join(f'<a class="cat" href="@/{p}"><b>{b}</b><span>Air conditioners &middot; Furnaces &middot; Indoor air quality</span><em>Check out {b} products {ARROW}</em></a>' for b, p in (("Carrier", "Carrier-Equipment/"), ("Lennox", "Lennox/"))) + "</div>",
                      canonical=canon("Products/")))
    out.append(brand_page("Carrier-Equipment/", "Carrier"))
    out.append(brand_page("Lennox/", "Lennox"))
    for b in ("Carrier", "Lennox"):
        out.append(models_page(f"{b}-Air-Conditioners/", b, "Air conditioners", f"{b} Air Conditioners, Salt Lake City | Affordable H&amp;C",
                               f"{b} central air conditioners sold, installed and serviced in Salt Lake City{' homes' if b == 'Carrier' else ''}: {', '.join(MODELS[b]['Air conditioners'][:4])} and more. Free in-home estimates."))
        out.append(models_page(f"{b}-Furnaces/", b, "Furnaces", f"{b} Gas Furnaces, Salt Lake City | Affordable Heating",
                               f"{b} gas furnaces sold, installed and serviced in Salt Lake City: {', '.join(MODELS[b]['Furnaces'][:4])} and more. Free estimates, all makes serviced."))
        out.append(models_page(f"{b}-Indoor-Air-Quality/", b, "Indoor air quality", f"{b} Indoor Air Quality, Salt Lake City | Affordable H&amp;C",
                               f"{b} indoor air quality products installed in Salt Lake City homes: air purification, humidifiers and UV lights, from Affordable Heating &amp; Cooling today."))
    fin = '''<p class="answer">We know that purchasing a new HVAC unit is a significant investment for any homeowner. That&rsquo;s why we offer financing (on approved credit) through Service Finance Company.</p>
<h2>How to apply</h2><p>Applying is easy: use Service Finance Company&rsquo;s application, fill in your information, and receive a response as soon as the same day. Call us at <a href="tel:+18012610924">801.261.0924</a> and we&rsquo;ll point you to it.</p>
<h2>Current promotions</h2><p>Ask about current promotions on furnaces, high-efficiency furnaces and air conditioners when you request your free estimate.</p>'''
    out.append(K.page("Financing/", "Financing", "HVAC Financing", "On approved credit through Service Finance Company.", "Financing", "Furnace &amp; AC Financing, Salt Lake City | Affordable H&amp;C",
                      "Finance a new furnace or air conditioner on approved credit through Service Finance Company, with a response as soon as the same day. Salt Lake City HVAC.",
                      fin, canonical=canon("Financing/")))
    out.append(K.page("Promotions/", "Promotions", "Current Promotions", "Furnaces, high-efficiency furnaces and air conditioners.", "Financing", "HVAC Promotions | Affordable Heating &amp; Cooling, Salt Lake",
                      "Ask Affordable Heating &amp; Cooling about current promotions and monthly payment options on furnaces and air conditioners in Salt Lake City. Free estimates.",
                      '<p class="answer">We run promotions on furnaces, high-efficiency furnaces and air conditioners, with monthly payments on approved credit. Call 801.261.0924 or request a free estimate for what&rsquo;s available now.</p><p><a class="btn" href="@/Financing/">See financing ' + ARROW + '</a></p>',
                      canonical=canon("Promotions/")))
    car = '''<p class="answer">Interested in joining our team? Apply today.</p><h2>Open positions</h2><ul><li>Service technician</li><li>Maintenance technician</li><li>Install technician</li></ul>
<h2>Certifications we ask about</h2><p>RMGA, EPA and NATE certifications or licenses, and other relevant credentials. Tell us how long you&rsquo;ve worked in the industry and when you could start.</p>'''
    out.append(K.page("Careers/", "Careers", "Careers", "Service, maintenance and install technicians.", "Careers", "HVAC Technician Jobs in Salt Lake City | Affordable Heating",
                      "Join Affordable Heating &amp; Cooling in Salt Lake City: service, maintenance and install technician positions. RMGA, EPA and NATE certifications welcome.",
                      car, canonical=canon("Careers/"), form_side=True))
    con = '''<p class="answer">For a free estimate, complete the form or call us today.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18012610924">801.261.0924</a></dd></div><div><dt>Address</dt><dd><address>155 Baird Ave<br>Salt Lake City, UT 84115</address></dd></div>
<div><dt>Office hours</dt><dd>Monday&ndash;Friday 8am&ndash;5pm</dd></div><div><dt>Emergencies</dt><dd>24-hour emergency service</dd></div></dl>'''
    out.append(K.page("Contact/", "Contact", "Contact Affordable Heating &amp; Cooling", "Free estimates. 24-hour emergency service.", "Contact", "Contact Us | Affordable Heating &amp; Cooling, Salt Lake City",
                      "Contact Affordable Heating &amp; Cooling at 155 Baird Ave, Salt Lake City: call 801.261.0924 or request a free estimate. Office Mon-Fri 8-5, 24-hour service.",
                      con, canonical=canon("Contact/"), form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Products", "Products/"), ("Contact", "Contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free estimates.", " Call 801.261.0924.")) for x in out]
