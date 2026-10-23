"""Pages for the dsihvac.com redesign: "Swing".

A Draper heating and air company whose old site said three things clearly: maintenance, repair ("The Fixer Upper ... those last few years
out of your equipment") and new installations with a 2-year labor / 10-year parts warranty. The signature turns that into the question
every homeowner actually has: maintain, repair or replace? A thermostat-style dial takes the system type, its age and whether it's working,
and points to one of their three services, using ENERGY STAR's published guidance (yearly tune-ups; have a pro evaluate equipment more than
10 years old). No prices, no invented lifespans. The look is Utah's temperature swing: furnace orange and coil blue on slate. Their own
install photos (mini-splits, a floor console, ductwork) and the 2018 Trane award carry the body; the banner is a credited photo of Draper
homes below Corner Canyon. Big Shoulders Display, Public Sans, JetBrains Mono.
Design references: Nest thermostat product pages (one big dial, plain readout), Carrier homeowner pages (system
types as choices), Dwell (headline over a full photo). Same Wix URLs (no trailing slash). One new post."""
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, EMAIL, AREAS
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer

CREDIT = '<p class="small photo-credit">Banner photo: Corner Canyon area, Draper, Utah &middot; Ken Lund, CC BY-SA 2.0, via Wikimedia Commons</p>'
SERV3 = [("Maintenance service", "Keep your equipment running like new for years to come. Regular maintenance prevents premature parts failures.", "01"),
         ("Repair", "The Fixer Upper. Helping you get those last few years out of your equipment!", "02"),
         ("New installations", "Reliability and peace of mind that comes with a 2 year labor warranty and 10 year parts warranties on all new A/C and furnace replacements.", "03")]
WHY = [("Free quotes", "Individualized recommendations."), ("Professional assistance", "Engineering solutions for YOUR home."),
       ("Extended warranty", "Here for you when you need us."), ("Service is the heart of this business", "Making you comfortable in your home is our number one priority.")]
BRANDS = [("Trane", "Our aim is to use original parts in all of the repairs. Our clients trust us with their Trane furnaces and air conditioners, and our careful work does not disappoint."),
          ("Carrier", "Our trained and meticulous specialists can help repair your equipment so it is as good as new. We work with Carrier and other brand names to get them back to their original working status."),
          ("Mitsubishi", "Our repair technicians have been trained to service Mitsubishi equipment. For a repair you can trust, call us about your Mitsubishi ductless air conditioner or heat pump."),
          ("Rheem", "We service all major brands of furnaces, air conditioners, heat pumps, air handlers, space heaters, fireplaces and rooftop equipment."),
          ("All other brands", "We can service all major heating and air conditioning brands.")]
FAQ = [("What areas do you serve?", "<p>We provide HVAC repair and installation services to Bluffdale, Draper, Riverton, South Jordan, Sandy, Herriman and Cottonwood Heights, in the Salt Lake City metro area.</p>"),
       ("What warranty comes with a new furnace or A/C?", "<p>All new A/C and furnace replacements come with a 2 year labor warranty and 10 year parts warranties.</p>"),
       ("Do you charge for quotes?", "<p>No. Quotes are free, with individualized recommendations for your home.</p>"),
       ("Which brands do you work on?", "<p>All major heating and air conditioning brands, including Trane, Carrier, Mitsubishi ductless systems and Rheem.</p>"),
       ("What are your hours?", "<p>Monday to Friday 9am to 6pm, Saturday 10am to 2pm. Closed Sunday.</p>")]


def dial():
    ticks = "".join(f'<line class="tk{" tk-l" if a % 5 == 0 else ""}" x1="0" y1="-118" x2="0" y2="{-104 if a % 5 == 0 else -110}" transform="rotate({-135 + a * 10.8:.1f})"/>' for a in range(26))
    nums = "".join(f'<text class="tn" transform="rotate({-135 + a * 10.8:.1f}) translate(0 -88) rotate({135 - a * 10.8:.1f})">{a}</text>' for a in (0, 5, 10, 15, 20, 25))
    return f'''<div class="dial" data-dial>
<div class="dl-face"><svg viewBox="-140 -140 280 280" role="img" aria-labelledby="dl-read">
<defs><linearGradient id="dlg" x1="0" x2="1"><stop offset="0" stop-color="var(--cool)"/><stop offset=".45" stop-color="var(--cool)"/><stop offset=".55" stop-color="var(--accent)"/><stop offset="1" stop-color="var(--accent)"/></linearGradient></defs>
<circle class="dl-bezel" r="132"/><path class="dl-arc" d="M -88.4 88.4 A 125 125 0 1 1 88.4 88.4" stroke="url(#dlg)"/>{ticks}{nums}
<g class="dl-needle" data-needle transform="rotate(-27)"><line x1="0" y1="10" x2="0" y2="-96"/><circle r="9"/></g>
<text class="dl-big" y="58" data-age-out>10</text><text class="dl-unit" y="78">years old</text></svg></div>
<div class="dl-ctrl">
<fieldset><legend class="label">1 &middot; Your system</legend><div class="chips">
{"".join(f'<label class="chip"><input type="radio" name="dl-type" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, (v, t) in enumerate((("furnace", "Furnace"), ("ac", "Central A/C"), ("hp", "Heat pump"), ("mini", "Ductless mini-split"))))}</div></fieldset>
<fieldset><legend class="label"><label for="dl-age">2 &middot; How old is it?</label></legend><input type="range" id="dl-age" min="0" max="25" value="10" data-age><div class="rng"><span>New</span><span>25+ years</span></div></fieldset>
<fieldset><legend class="label">3 &middot; How is it running?</legend><div class="chips">
<label class="chip"><input type="radio" name="dl-run" value="ok" checked><span>Fine for now</span></label><label class="chip"><input type="radio" name="dl-run" value="bad"><span>Not working right</span></label></div></fieldset>
<div class="dl-out" aria-live="polite"><p class="mono" id="dl-read" data-read>Maintenance service</p><h3 data-head>Keep it running like new</h3><p data-text></p>
<a class="btn accent" href="tel:+13852267667">{PHONE} Free quote: 385-226-7667</a></div>
</div>
<p class="small dl-src">Guidance from ENERGY STAR: tune up HVAC equipment yearly, check filters monthly, and have equipment more than 10 years old evaluated by a professional. Every home is different; a free quote is the real answer.</p>
</div>'''


def home():
    body = f'''
<section class="p-hero"><div class="ph-img" data-parallax="0.08">{img("pf-hero", "Homes on the hillside of the Corner Canyon area in Draper, Utah, with the Salt Lake Valley behind", priority=True)}</div>
<div class="wrap ph-in"><div class="ph-txt"><p class="label"><span class="dot-h"></span>Draper, Utah &middot; since 2015</p>
<h1>HVAC company in Draper, <em>heating and air done right.</em></h1>
<p class="lede">Proformance Heating and Air is an HVAC company in Draper, Utah: furnace and air conditioning maintenance, repair and new installations for homes in Bluffdale, Draper, Riverton, South Jordan, Sandy, Herriman and Cottonwood Heights. Whatever you need, we can fix.</p>
<div class="btn-row"><a class="btn accent" href="tel:+13852267667">{PHONE} Call 385-226-7667</a><a class="btn ghost" href="#dial">Maintain, repair or replace? {ARROW}</a></div></div></div>
<div class="ph-read"><div class="wrap"><span><b>2 yr</b>labor warranty on new A/C &amp; furnaces</span><span><b>10 yr</b>parts warranties</span><span><b>Free</b>quotes</span><span><b>2015</b>established</span></div></div>
<p class="credit">Corner Canyon area, Draper &middot; Ken Lund, CC BY-SA 2.0, via Wikimedia Commons</p></section>

<section class="sec p-serv"><div class="wrap">
<div class="p-head split-h reveal"><div><p class="label">Our services</p><h2>Three ways <em>we keep you comfortable</em></h2></div><p class="lede">Making you comfortable in your home is our number one priority. Here are the services we offer, for furnaces, air conditioners, heat pumps and ductless systems.</p></div>
<div class="sv3">{"".join(f'<a class="sv reveal" href="@/services/"><span class="mono">{n}</span><h3>{t}</h3><p>{d}</p><em>{ARROW}</em></a>' for t, d, n in SERV3)}</div>
</div></section>

<section class="sec p-eq"><div class="wrap">
<div class="p-head split-h reveal"><div><p class="label">What we work on</p><h2>Every box <em>that heats or cools</em></h2></div><p class="lede">We service all major brands of furnaces, air conditioners, heat pumps, air handlers, space heaters, fireplaces and rooftop equipment.</p></div>
<div class="eq reveal">
<div><span class="mono heat">Heat</span><h3>Furnaces</h3><p>Repair, yearly maintenance and replacement. On the heating side, a tune-up includes checking gas connections, gas pressure, burner combustion and the heat exchanger.</p></div>
<div><span class="mono cool">Cool</span><h3>Air conditioners</h3><p>Repair, maintenance and new installs. Cooling maintenance covers cleaning the evaporator and condenser coils, checking refrigerant and adjusting the blower for proper airflow.</p></div>
<div><span class="mono both">Both</span><h3>Heat pumps</h3><p>One system for heating and cooling, serviced on all major brands.</p></div>
<div><span class="mono both">Both</span><h3>Ductless mini-splits</h3><p>Mitsubishi ductless air conditioners and heat pumps, wall units and floor consoles, like the installs pictured below.</p></div>
</div></div></section>

<section class="sec p-dial" id="dial"><div class="wrap">
<div class="p-head reveal"><p class="label">Maintain, repair or replace?</p><h2>Set the dial <em>on your system</em></h2><p class="lede">Tell us what you have, how old it is and how it&rsquo;s running. The dial points to the service that usually fits, the same way we&rsquo;d talk it through on a free quote.</p></div>
{dial()}
</div></section>

<section class="sec p-work"><div class="wrap">
<div class="p-head split-h reveal"><div><p class="label">Our work</p><h2>Installs <em>around the valley</em></h2></div><p class="lede">All our repairs are completed with meticulous detail, resulting in a product that is as good as new. A few of our own jobs: ductless wall units, a floor console and ductwork in new construction.</p></div>
<div class="wk">
<figure class="wk-a reveal">{img("pf-minisplit", "A ductless mini-split wall unit installed above a window in a bedroom")}<figcaption>Ductless wall unit, bedroom</figcaption></figure>
<figure class="wk-b reveal">{img("pf-console", "A ductless floor console unit installed below a shuttered window")}<figcaption>Floor console</figcaption></figure>
<figure class="wk-c reveal">{img("pf-kitchen", "A ductless unit installed high on the wall of an open kitchen")}<figcaption>Open kitchen</figcaption></figure>
<figure class="wk-d reveal">{img("pf-duct", "Exposed spiral ductwork in a home under construction")}<figcaption>Ductwork, new construction</figcaption></figure>
</div></div></section>

<section class="sec p-award"><div class="wrap split" style="align-items:center">
<figure class="aw-img reveal">{img("pf-award", "A crystal 2018 Rookie of the Year Award from Trane and Larson, presented to DSI HVAC")}</figure>
<div class="reveal"><p class="label">Our history</p><h2>Since 2015, <em>one mission</em></h2>
<p>We were established in 2015 with one mission: to bring a reliable, high quality furnace and air conditioning repair service to the Salt Lake City area. Our passion for excellence is what inspired us to open up our shop, and continues to drive us to this day.</p>
<p>What started out as a repair service has become our passion. We&rsquo;re a team of dedicated technicians with a genuine desire to make sure your experience with us is easy, convenient and satisfying.</p>
<p class="small">Pictured: the 2018 Rookie of the Year Award from Trane and Larson, presented to DSI HVAC.</p>
<a class="tlink" href="@/about-us/">About us {ARROW}</a></div>
</div></section>

<section class="sec p-area"><div class="wrap">
<div class="p-head reveal"><p class="label">Service area</p><h2>Draper and <em>the south valley</em></h2></div>
<ul class="areas reveal">{"".join(f'<li>{a}</li>' for a in AREAS)}</ul>
<div class="why reveal">{"".join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in WHY[:3])}</div>
<p class="brands-line reveal"><b>Brands we service:</b> Trane, Carrier, Mitsubishi, Rheem and all other major heating and air conditioning brands. <a href="@/brands-we-service/">Brands {ARROW}</a></p>
</div></section>

<section class="sec p-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Quick <em>answers</em></h2>
<a class="post-card p-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>What EPA and ENERGY STAR say about MERV ratings, fit and how often to check your filter.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": "HVAC Company Draper, UT | Furnace &amp; A/C | Proformance",
            "meta": "Proformance Heating and Air: HVAC company in Draper, Utah. Furnace and A/C maintenance, repair and new installs with 2-year labor and 10-year parts warranties.",
            "body": body, "body_class": "is-home", "og": "pf-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    sv = f'''<p class="answer">Proformance Heating and Air offers three services for furnaces, air conditioners, heat pumps and ductless systems in Draper and the south Salt Lake Valley: maintenance, repair and new installations. Quotes are free.</p>
<div class="sv3 in-prose">{"".join(f'<div class="sv"><span class="mono">{n}</span><h3>{t}</h3><p>{d}</p></div>' for t, d, n in SERV3)}</div>
<h2>Maintenance service</h2>
<p>Keep your equipment running like new for years to come. Regular maintenance prevents premature parts failures. ENERGY STAR recommends a yearly tune-up, and its pre-season checklist is a good picture of what a visit covers:</p>
<ul><li>Checking thermostat settings</li><li>Tightening electrical connections and measuring motor voltage and current</li><li>Lubricating moving parts</li><li>Checking the condensate drain</li><li>Checking the system&rsquo;s controls, startup cycle and shutoff</li>
<li>For cooling: cleaning the evaporator and condenser coils, checking the refrigerant level, and cleaning and adjusting blower components</li><li>For heating: checking gas connections, gas pressure, burner combustion and the heat exchanger</li></ul>
<p>Between visits, ENERGY STAR suggests checking your filter every month. See our guide to <a href="@/{p_blog.SLUG}">furnace filters and MERV ratings</a>.</p>
<h2>Repair</h2>
<p>The Fixer Upper. Helping you get those last few years out of your equipment. Whatever you need, we can fix: furnaces, air conditioners, heat pumps, air handlers and ductless systems from all major brands. All our repairs are completed with meticulous detail, resulting in a product that is as good as new.</p>
<h2>New installations</h2>
<p>Reliability and peace of mind that comes with a 2 year labor warranty and 10 year parts warranties on all new A/C and furnace replacements. When it&rsquo;s time to replace, we give individualized recommendations and engineering solutions for your home, not a one-size-fits-all system.</p>
<h2>Brands</h2><p>We service and install equipment for all major heating and air conditioning manufacturers, including Trane, Carrier, Mitsubishi and Rheem. <a href="@/brands-we-service/">Brands we service</a>.</p>
<figure>{img("pf-console", "A ductless floor console unit installed below a window")}<figcaption>A ductless floor console we installed.</figcaption></figure>
<p class="small">Maintenance checklist: ENERGY STAR, &ldquo;Maintenance Checklist&rdquo; (energystar.gov).</p>''' + CREDIT
    out.append(K.page("services/", "Services", "Heating &amp; air conditioning services in Draper", "Maintenance &middot; Repair &middot; New installations", "Services",
                      "Furnace &amp; A/C Repair &amp; Installs, Draper | Proformance",
                      "Furnace and air conditioning maintenance, repair and new installations in Draper, UT. Free quotes; new systems carry 2-year labor and 10-year parts warranties.",
                      sv, image="pf-hero", alt="Corner Canyon area, Draper", canonical=canon("services/"), schema=[K.svc_schema("services/", "Heating and air conditioning services", "Draper, UT")]))
    ab = f'''<p class="answer">Since 2015 we have become a well-known air conditioning and furnace repair service in the Draper area.</p>
<p>We were established in 2015 with one mission: to bring a reliable, high quality furnace and air conditioning repair service to the Salt Lake City area. Our passion for excellence is what inspired us to open up our shop, and continues to drive us to this day. All our repairs are completed with meticulous detail, resulting in a product that is as good as new.</p>
<h2>This is our story</h2>
<p>What started out as a repair service has now become our passion, and we&rsquo;re glad to share it with you. We&rsquo;re a team of dedicated repair technicians with a genuine desire to make sure that your experience with us is easy, convenient and satisfying. Restoring heating and cooling to your home!</p>
<figure>{img("pf-award", "A crystal 2018 Rookie of the Year Award from Trane and Larson, presented to DSI HVAC")}<figcaption>2018 Rookie of the Year Award from Trane and Larson, presented to DSI HVAC.</figcaption></figure>
<h2>Where we work</h2><p>We provide HVAC repair and installation services to {", ".join(AREAS[1:-1])} and {AREAS[-1]}, from our base in Draper.</p>
<figure>{img("pf-team", "Team members cooking together at a company get-together")}<figcaption>The team at a get-together.</figcaption></figure>''' + CREDIT
    out.append(K.page("about-us/", "About", "About Proformance Heating and Air", "Draper heating and air since 2015.", "About", "About Us | Draper Heating &amp; Air Since 2015 | Proformance",
                      "Proformance Heating and Air has served Draper and the south Salt Lake Valley since 2015 with careful furnace and air conditioning repair and installs.",
                      ab, image="pf-hero", alt="Corner Canyon area, Draper", canonical=canon("about-us/")))
    wy = '<p class="answer">Service is the heart of this business: free quotes, individualized recommendations, professional assistance and an extended warranty.</p>' + \
         "".join(f"<h2>{t}</h2><p>{d}</p>" for t, d in WHY[:3]) + \
         "<p>Free quotes come with individualized recommendations: we look at your home and your equipment before suggesting anything. New A/C and furnace replacements carry a 2 year labor warranty and 10 year parts warranties.</p>" + \
         '<h2>Here for you when you need us</h2><p>Monday to Friday 9am to 6pm and Saturday 10am to 2pm. Call <a href="tel:+13852267667">385-226-7667</a>.</p>' + CREDIT
    out.append(K.page("why-choose-us/", "Why choose us", "Why choose Proformance?", "Service is the heart of this business.", "Why us", "Why Choose Us | Free Quotes, Extended Warranty | Proformance",
                      "Why Draper homeowners choose Proformance Heating and Air: free quotes, individualized recommendations, professional help and an extended warranty on new units.",
                      wy, image="pf-hero", alt="Corner Canyon area, Draper", canonical=canon("why-choose-us/")))
    br = '<p class="answer">We service and install equipment for all major heating and air conditioning manufacturers. Our technicians have been highly trained to work with specific brands.</p>' + \
         "".join(f"<h2>{t}</h2><p>{d}</p>" for t, d in BRANDS) + f'<figure>{img("pf-minisplit", "A ductless mini-split wall unit in a bedroom")}<figcaption>A ductless wall unit we installed.</figcaption></figure>' + CREDIT
    out.append(K.page("brands-we-service/", "Brands", "Brands we service", "Trane, Carrier, Mitsubishi, Rheem and more.", "Brands", "Trane, Carrier &amp; Mitsubishi Service, Draper | Proformance",
                      "Proformance Heating and Air services and installs all major brands in Draper, UT: Trane, Carrier, Mitsubishi ductless systems, Rheem and more. Free quotes.",
                      br, image="pf-hero", alt="Corner Canyon area, Draper", canonical=canon("brands-we-service/")))
    con = f'''<p class="answer">Would you like additional information about our repairs and other related services? Reach out, we&rsquo;d be happy to hear from you.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13852267667">385-226-7667</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Address</dt><dd><address>13525 south Ensign Point Ln<br>Draper, UT 84020</address></dd></div>
<div><dt>Hours</dt><dd>Mon&ndash;Fri 9am&ndash;6pm<br>Sat 10am&ndash;2pm<br>Sun closed</dd></div></dl>
<p>Serving {", ".join(AREAS[:-1])} and {AREAS[-1]}.</p>'''
    out.append(K.page("contact-us/", "Contact", "Contact Proformance Heating and Air", "Free quotes on heating and air.", "Contact", "Contact Us | Free HVAC Quotes in Draper, UT | Proformance",
                      "Contact Proformance Heating and Air in Draper, UT: call 385-226-7667 or email david@dsihvac.com for a free quote. Mon-Fri 9-6, Sat 10-2.",
                      con, canonical=canon("contact-us/"), form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Services", "services/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 385-226-7667.", " Draper, Utah.")) for x in out]
