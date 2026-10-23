"""Pages for the jacksonplumbinghvac.com redesign: "Main line".

The live site is a one-page "Colorado" template with no phone number, so there is almost nothing true to say beyond the Google listing:
the name, a West Jordan address, a phone number and the trade. The draft says exactly that, and earns the rest of the page by being
useful. The signature is EPA WaterSense's two-hour water-meter leak test, turned into a meter you type into: it does the gallons-per-day
and per-year math and compares it with WaterSense's published leak figures. Deep water navy, copper pipe, frost blue; meter digits in mono.
Banner: a credited aerial of West Jordan's neighborhoods. Bricolage Grotesque, Source Sans 3, IBM Plex Mono.
Design references: utility-bill and smart-meter dashboards (one big readout), Dwell (headline over a full photo).
Same home URL; a contact page and one new post. No services, hours, licenses, years or ratings until the client confirms them."""
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer
CREDIT = '<p class="small photo-credit">Banner photo: West Jordan and Taylorsville from the air &middot; formulanone, CC BY-SA 2.0, via Wikimedia Commons</p>'
FAQ = [("Where is Jackson Family Plumbing &amp; HVAC?", "<p>6959 W 7800 S, West Jordan, UT 84081.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+13855955700">385-595-5700</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("How can I tell if I have a hidden leak?", "<p>EPA WaterSense suggests reading your water meter before and after a two-hour period when no water is being used. If the reading changes, you probably have a leak. The meter test above does the math for you.</p>"),
       ("Is a running toilet really a leak?", "<p>Often, yes. WaterSense&rsquo;s test: put a few drops of food coloring in the toilet tank. If color shows up in the bowl within 10 minutes without flushing, the toilet is leaking. Flush afterward so the tank doesn&rsquo;t stain.</p>")]


def meter():
    return '''<div class="meter" data-meter>
<div class="mt-face" aria-hidden="true"><span class="mt-lbl">Gallons</span><div class="mt-digits" data-digits>0000000</div><div class="mt-dial"><i data-sweep></i></div><span class="mt-lbl">Leak indicator</span></div>
<form class="mt-form" data-mform novalidate>
<ol class="mt-steps">
<li><b>Turn off every tap,</b> and don&rsquo;t run the dishwasher, washer, sprinklers or ice maker.</li>
<li><label for="mt-a">Read the meter and type it here</label><input id="mt-a" inputmode="decimal" autocomplete="off" placeholder="e.g. 45213.4" data-a></li>
<li><label for="mt-b">Two hours later, with no water used, read it again</label><input id="mt-b" inputmode="decimal" autocomplete="off" placeholder="e.g. 45214.1" data-b></li>
<li><label for="mt-h">Hours between readings</label><input id="mt-h" inputmode="decimal" value="2" data-h></li>
</ol>
<div class="mt-unit" role="radiogroup" aria-label="Meter units"><label><input type="radio" name="mt-u" value="gal" checked> Meter reads gallons</label><label><input type="radio" name="mt-u" value="cf"> Meter reads cubic feet</label></div>
</form>
<div class="mt-out" aria-live="polite" data-mout><p class="mono">Waiting for two readings</p><h3>Type both readings to see the result.</h3><p>Most water meters sit in a box near the curb. If the readings match, there&rsquo;s no sign of a leak while the house was quiet.</p></div>
<p class="small mt-src">Test method and figures: EPA WaterSense, Fix a Leak Week (updated March 13, 2026). The average household&rsquo;s leaks can waste more than 9,300 gallons a year, and nine percent of homes have leaks wasting 50 gallons or more a day. Nothing you type leaves this page.</p>
</div>'''


def home():
    body = f'''
<section class="j-hero"><div class="jh-img" data-parallax="0.08">{img("jk-hero", "Aerial view of the neighborhoods of West Jordan and Taylorsville, Utah", priority=True)}</div>
<div class="wrap jh-in"><div class="jh-txt"><p class="label">West Jordan, Utah &middot; 7800 South</p>
<h1>Plumber in West Jordan, <em>plumbing &amp; HVAC.</em></h1>
<p class="lede">Jackson Family Plumbing &amp; HVAC is a plumber and HVAC company in West Jordan, Utah, at 6959 W 7800 S. Water where it shouldn&rsquo;t be, no hot water, a furnace or air conditioner acting up: call and talk to the family.</p>
<div class="btn-row"><a class="btn accent" href="tel:+13855955700">{PHONE} Call 385-595-5700</a><a class="btn ghost" href="#meter">Test for a hidden leak {ARROW}</a></div></div></div>
<p class="credit">West Jordan from the air &middot; formulanone, CC BY-SA 2.0, via Wikimedia Commons</p></section>

<section class="sec j-intro"><div class="wrap j-in2">
<div class="reveal"><p class="label">Plumbing &amp; HVAC</p><h2>One call for the water <em>and the air.</em></h2></div>
<div class="reveal"><p class="lede">The pipes that carry water through your house and the system that heats and cools it share the same walls, the same basement and often the same emergency. Jackson Family Plumbing &amp; HVAC handles both, from West Jordan.</p>
<p>Tell us what&rsquo;s going on when you call. A photo of the problem, the age of the water heater or furnace if you know it, and where your main water shutoff is all help us help you faster.</p></div>
</div></section>

<section class="sec j-meter" id="meter"><div class="wrap">
<div class="j-head split-h reveal"><div><p class="label">The two-hour leak test</p><h2>Is your house leaking <em>while you sleep?</em></h2></div><p class="lede">Some leaks never show up as a puddle: a toilet flapper, a slab line, an irrigation valve. EPA WaterSense&rsquo;s simplest check uses the meter you already have. Type in two readings and we&rsquo;ll do the math.</p></div>
{meter()}
</div></section>

<section class="sec j-freeze"><div class="wrap">
<div class="j-head split-h reveal"><div><p class="label">Before the first hard freeze</p><h2>Four things to do <em>this week</em></h2></div><a class="tlink" href="@/{p_blog.SLUG}">The full frozen-pipe guide {ARROW}</a></div>
<div class="fz">
<div class="reveal"><span class="mono">01</span><h3>Find the main shutoff</h3><p>Know where your home&rsquo;s water shut-off valve is and how to operate it, and show the rest of the household. It&rsquo;s the difference between a wet floor and a flooded basement.</p></div>
<div class="reveal"><span class="mono">02</span><h3>Deal with outdoor faucets</h3><p>IBHS: shut off and insulate the valves if you don&rsquo;t have frost-proof outdoor faucets, noting that homes built before 2010 typically don&rsquo;t. Disconnect garden hoses.</p></div>
<div class="reveal"><span class="mono">03</span><h3>Insulate the cold spots</h3><p>Pipes in attics, crawl spaces and along exterior walls are the ones at risk. Pipe insulation tubes or wraps help, but insulation alone won&rsquo;t protect pipes in prolonged cold without some heat.</p></div>
<div class="reveal"><span class="mono">04</span><h3>Keep the heat at 55&deg;F</h3><p>IBHS and the National Weather Service both say to keep the thermostat at least 55&deg;F, even when no one is home. On the coldest nights, open sink cabinets on outside walls.</p></div>
</div></div></section>

<section class="sec j-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Good <em>to know</em></h2>
<div class="addr-card"><p class="mono">Jackson Family Plumbing &amp; HVAC</p><address>6959 W 7800 S<br>West Jordan, UT 84081</address><a class="btn accent" href="tel:+13855955700">{PHONE} 385-595-5700</a></div></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": "Plumber in West Jordan, UT | Jackson Family Plumbing &amp; HVAC",
            "meta": "Jackson Family Plumbing &amp; HVAC: plumber and HVAC company at 6959 W 7800 S, West Jordan, Utah. Call 385-595-5700. Try the two-hour water meter leak test.",
            "body": body, "body_class": "is-home", "og": "jk-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    con = '''<p class="answer">Call Jackson Family Plumbing &amp; HVAC at <a href="tel:+13855955700">385-595-5700</a>, or send the form and we&rsquo;ll get back to you.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13855955700">385-595-5700</a></dd></div><div><dt>Address</dt><dd><address>6959 W 7800 S<br>West Jordan, UT 84081</address></dd></div></dl>
<h2>Before you call</h2><ul><li>If water is actively leaking, turn off the main water shutoff first.</li><li>Have the approximate age of your water heater, furnace or air conditioner handy if you know it.</li><li>A photo of the problem helps.</li></ul>'''
    out.append(K.page("contact/", "Contact", "Contact Jackson Family Plumbing &amp; HVAC", "West Jordan, Utah.", "Contact", "Contact Us | Jackson Family Plumbing &amp; HVAC, West Jordan",
                      "Contact Jackson Family Plumbing &amp; HVAC at 6959 W 7800 S, West Jordan, UT 84081. Call 385-595-5700 or send the form for plumbing and HVAC help at home.",
                      con, canonical=canon("contact/"), form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 385-595-5700.", " West Jordan, Utah.")) for x in out]
