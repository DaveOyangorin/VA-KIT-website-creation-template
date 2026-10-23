"""Pages for the hvaccowboy.com redesign: "Home or business".

Cowboy works two very different jobs: a family's furnace on a January night, and a restaurant's rooftop unit and kitchen exhaust fan.
Their own quote form already asks "Homeowner or Business". So the signature is a rope switch at the top of the page: flip it and the whole
page re-saddles: headline, the services shown first, the job photos (residential AC and furnaces vs rooftop units, control boards and
exhaust fans) and the quote form's mode. It opens on their branded car under a Utah Valley sunset. Navy and amber from the logo on
leather cream; Zilla Slab, Work Sans, and Rye for the big words.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same single URL plus one new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, AREAS
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer
cta = K.cta

SERV = {"home": [("Residential AC", "Air conditioning service, refrigerant charging, and system diagnostics for your home.", "cb-ac-svc", "Residential AC refrigerant service with gauges connected"),
                 ("Heating &amp; furnace", "Furnace repair, installation, and maintenance to keep your home warm all winter.", "cb-furnace", "Bryant furnace diagnostics with a meter")],
        "biz": [("Commercial HVAC", "Rooftop unit installation, maintenance, and repair for commercial buildings and restaurants.", "cb-rtu1", "A commercial rooftop HVAC unit installation"),
                ("Kitchen equipment", "Commercial kitchen exhaust fans, ventilation systems, and equipment installation.", "cb-exhaust", "A commercial kitchen exhaust fan installed on a roof")]}
WORK = {"home": [("cb-condenser", "New residential condenser installation"), ("cb-daikin", "Daikin mini-split service"), ("cb-ac-unit", "Residential AC unit service"), ("cb-furnace", "Bryant furnace diagnostics")],
        "biz": [("cb-rtu2", "Commercial rooftop HVAC unit"), ("cb-board", "HVAC control board and wiring"), ("cb-rtu-svc", "Commercial rooftop unit refrigerant service"), ("cb-exhaust", "Commercial exhaust fan installation")]}
REVIEWS = [("Ricardo did an amazing job replacing our furnace. He showed up quickly when we were freezing due to a faulty furnace. He was super honest and gave us a great price. He explained everything clearly and kept us in the loop the whole time. The work was done efficiently and professionally, with no stress or the classic &ldquo;final price surprise&rdquo;. Highly recommend!", "Juan R."),
           ("Ricardo arrived right on time, super professional and courteous the whole visit. He clearly knows HVAC systems inside out and explained the issue in plain English. He diagnosed the problem fast, fixed my furnace efficiently, and did a thorough, clean job. No pushy upsells at all. What really stood out was his honesty: fair pricing with zero surprise charges.", "David C."),
           ("My air conditioner stopped working, and I texted Ricardo after 6 PM. Even though it was late, he quickly replied and came to my house in less than an hour. Ricardo is extremely friendly, attentive, and reliable. Every time I reached out to him, he responded promptly and with great care. I highly recommend his services.", "Carlos D.")]
FAQ = [("Do you work on both homes and businesses?", "<p>Yes. Residential AC and furnaces, plus commercial HVAC, rooftop units and commercial kitchen equipment for buildings and restaurants.</p>"),
       ("Do you offer emergency service?", "<p>Yes. 24/7 emergency service is available, and same-day appointments. Call 801-940-0420.</p>"),
       ("Are you licensed and insured?", "<p>Yes. Cowboy Heating &amp; Air is licensed and insured.</p>"),
       ("What areas do you serve?", "<p>Utah Valley: Lehi, Orem, Provo, American Fork, Pleasant Grove, Saratoga Springs, Eagle Mountain, Spanish Fork, Springville and Payson.</p>")]


def svc_cards(mode):
    return "".join(f'<div class="sv" data-only="{mode}"><figure>{img(im, alt)}</figure><div><h3>{t}</h3><p>{d}</p></div></div>' for t, d, im, alt in SERV[mode])


def home():
    form = K.form("Get a free quote", fields=[("type", "Homeowner or business")], msg_label="What&rsquo;s going on with your system?")
    body = f'''
<div class="crew" data-crew data-mode="home">
<section class="c-hero"><div class="ch-img" data-parallax="0.08">{img("cb-hero", "Cowboy Heating & Air's branded service car parked in the desert below a mountain at sunset", priority=True)}</div>
<div class="wrap ch-in"><div class="ch-txt">
<div class="rope" id="crew" role="group" aria-label="Show services for"><button type="button" data-set="home" aria-pressed="true">Homeowner</button><button type="button" data-set="biz" aria-pressed="false">Business</button></div>
<p class="label">Lehi &middot; Utah Valley &middot; 24/7 emergency service</p>
<h1>HVAC company in Lehi, <em class="west"><span data-only="home">for your home.</span><span data-only="biz">for your business.</span></em></h1>
<p class="lede" data-only="home">Cowboy Heating &amp; Air is an HVAC company in Lehi serving Utah Valley: air conditioning service and furnace repair, installation and maintenance, with honest pricing and fast response.</p>
<p class="lede" data-only="biz">Cowboy Heating &amp; Air is an HVAC company in Lehi serving Utah Valley businesses: rooftop units for commercial buildings and restaurants, and commercial kitchen exhaust fans, ventilation and equipment.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18019400420">{PHONE} Call 801-940-0420</a><a class="btn ghost" href="#quote">Get a free quote {ARROW}</a></div></div></div>
<div class="ch-strip"><div class="wrap"><span><b>24/7</b> emergency service</span><span><b>Same-day</b> appointments</span><span><b>Licensed</b> &amp; insured</span><span><b>Daikin</b> authorized &middot; Bryant dealer</span></div></div></section>

<section class="sec c-serv" id="services"><div class="wrap">
<div class="c-head split-h reveal"><div><p class="label">Our services</p><h2>Heating, air &amp; <em>commercial kitchens.</em></h2></div><p class="lede"><span data-only="home">Showing home services first.</span><span data-only="biz">Showing business services first.</span> Flip the switch up top to change.</p></div>
<div class="serv">{svc_cards("home")}{svc_cards("biz")}</div>
<div class="also"><p><b data-only="home">Also for businesses:</b><b data-only="biz">Also for homeowners:</b> <span data-only="home">commercial HVAC, rooftop units and kitchen exhaust and ventilation.</span><span data-only="biz">residential AC service and furnace repair, installation and maintenance.</span></p></div>
</div></section>

<section class="sec c-work" id="work"><div class="wrap">
<div class="c-head reveal"><p class="label">Our work</p><h2>Real jobs. <em>Real gauges.</em></h2></div>
<div class="gal">{"".join(f'<figure data-only="{m}">{img(n, a)}<figcaption>{a}</figcaption></figure>' for m in ("home", "biz") for n, a in WORK[m])}</div>
</div></section>
</div>

<section class="c-award"><div class="wrap c-award-in">
<figure class="reveal">{img("cb-plaque", "Best of BusinessRate 2025 plaque: Cowboy Heating & Air LLC, HVAC Contractor, Lehi, Utah")}</figure>
<div class="reveal"><p class="label">Award-winning service</p><h2>Best of BusinessRate 2025, <em class="west">HVAC contractor, Lehi.</em></h2>
<p>Utah Valley&rsquo;s award-winning HVAC team: licensed and insured, a Daikin authorized and Bryant dealer, and available 24/7 for emergencies.</p></div>
</div></section>

<section class="sec c-revs"><div class="wrap">
<div class="c-head reveal"><p class="label">What our customers say</p><h2>&ldquo;No pushy upsells <em>at all.</em>&rdquo;</h2></div>
<div class="revs">{"".join(f'<blockquote class="rev reveal"><p>&ldquo;{q}&rdquo;</p><cite>{n} &middot; Google review</cite></blockquote>' for q, n in REVIEWS)}</div>
</div></section>

<section class="sec c-quote" id="quote"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Get a free quote</p><h2>Tell us what&rsquo;s going on.</h2><p class="lede">Call or text <a href="tel:+18019400420">801-940-0420</a>, or send the form. Homeowner or business, we&rsquo;ll get back to you.</p>
<p class="label" style="margin-top:22px">Serving Utah Valley</p><div class="towns">{"".join(f"<span>{a}</span>" for a in AREAS)}</div></div>
<div class="reveal form-col">{form}</div>
</div></section>

<section class="sec c-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card c-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What EPA and NFPA say about carbon monoxide, furnaces and CO alarms, before heating season.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "HVAC Company Lehi, UT | Heating, AC &amp; Kitchens | Cowboy",
            "meta": "Cowboy Heating & Air: HVAC company in Lehi serving Utah Valley. Residential AC and furnaces, commercial rooftop units and kitchen equipment. 24/7 service.",
            "body": body, "body_class": "is-home", "og": "cb-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home(), p_blog.page(K), K.notfound((("Home", ""), ("Get a quote", "#quote"), ("Blog", p_blog.SLUG)))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-940-0420.", " Lehi, UT.")) for x in out]
