"""Pages for the abode.cleaning redesign: "Come home to clean."

Abode's best asset is its own brand film: real two-person teams cleaning a real home. And its policies are unusually honest about
what makes a cleaning go well (declutter, clear dishes, tuck the pets away, close doors you don't want cleaned). So the site is bright
and calm, built on stills from that film, in Abode violet, with the signature "Get ready for your clean" checklist: tick each prep
step from their own instructions, the readiness meter fills, and the arrival windows for your booking appear.
References (screenshotted 21 Oct 2026): Branch Basics (warm, human home-care photography, friendly type), Grove (clean editorial
retail, one strong colour), Airbnb (booking-first clarity, soft rounded UI).
Same 6 URLs (no trailing slash); the site had no canonicals, self-canonicals added."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from fx import blocks
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
MARK = open(os.path.join(HERE, "src", "logo.svg"), encoding="utf-8").read()
MARK = re.sub(r'width="63" height="62"', 'aria-hidden="true"', MARK, count=1)
cta = K.cta


def header():
    return re.sub(r'(<a class="brand"[^>]*>)<img[^>]*>(</a>)', lambda m: m.group(1) + MARK + '<span class="wm">abode</span>' + m.group(2), K.header())


def footer():
    return re.sub(r'<span class="flogo"><img[^>]*></span>', '<span class="flogo">' + MARK + '<span class="wm">abode</span></span>', K.footer())


PREP = [("Declutter", "Pick up toys, junk mail, loose change and clothing from floors and counters, so your team can focus on baseboards and surfaces."),
        ("Clear any dishes", "Most house cleaners don&rsquo;t wash dishes. Put them away so your team can clean the sink and the area around it."),
        ("Say what matters", "Dusty blinds driving you crazy? Tell your team or the office ahead of time so it doesn&rsquo;t get missed."),
        ("Secure valuables", "Put away anything that could easily break, and flag anything that needs to be cleaned a special way."),
        ("Tuck the pets away", "Pets can get in the way, and cleaners may have allergies. Pet hair takes extra time, and some may settle after."),
        ("Close doors to skip rooms", "A closed door is the universal sign for cleaners not to enter."),
        ("Leave a way in", "You don&rsquo;t need to be home. Give the office a door code, key location or garage code to keep on file.")]
QUOTES = [("I was so impressed with the cleaning service I received from Abode. The team was professional, efficient, and thorough. They did an amazing job! I will definitely be using them again. I highly recommend them!", "Jasmine"),
          ("This has been a great service cleaning service. The staff are professional and communicative. They do a really good job with both regular cleanings, and the deep cleaning I had for the holidays. Thankfully to be working with this company!", "Eric Baxter"),
          ("Paz and Joseph were incredible. We got the deep cleaning and they went above and beyond for us. I have never considered money better spent on cleaners than this. Five stars!", "Jane Johnson"),
          ("Extremely communicative and kind! I had to organize a cleaning for my sister while I&rsquo;m in another state and it went seamlessly! My sister said her house looks perfect! The ladies were on time, kind and efficient. Will use them again for sure :)", "Taralyn Fischer")]
FAQ = [("Are you licensed and insured?", "<p>Yes and yes. Abode works with small cleaning businesses that are insured, vetted with the Abode quality process, and have been in business for more than 3 years.</p>"),
       ("Am I required to sign a contract?", "<p>No. We&rsquo;re a no-contract company. We don&rsquo;t believe a contract is necessary to build a long relationship with our clients.</p>"),
       ("Do I have to be home when you clean?", "<p>No. You can give the office staff a custom door code, the location of a key, or a garage code to keep on file. If you&rsquo;d rather be home, that&rsquo;s fine too. We&rsquo;re happy to clean while you&rsquo;re there.</p>"),
       ("Do I need to provide supplies and equipment?", "<p>No. Teams of two come with their own equipment and supplies. If you have a product you&rsquo;d like used, leave it out, and the office can add any special requests to the cleaners&rsquo; notes.</p>"),
       ("Do you do dishes or laundry?", "<p>We don&rsquo;t do laundry. Dishes can be done for an additional price.</p>"),
       ("When will the team arrive?", "<p>Appointments start at 9 am, 11:30 am or 2:30 pm, with a one- to two-hour arrival window for traffic, weather and other delays. If a team is running behind, you&rsquo;ll get a call or text.</p>"),
       ("What&rsquo;s the cancellation policy?", "<p>Reschedule or cancel 24&ndash;48 hours ahead. Inside that window, or the same day, there&rsquo;s a $25 cancellation fee; cancellations up to 8 hours before the appointment are subject to a $65 fee. <a href=\"@/cancellation-policy/\">Full policy</a>.</p>")]


def home():
    prep = "".join(f'<li><label class="pr"><input type="checkbox" data-prep><span class="pr-box" aria-hidden="true"></span><span class="pr-t"><b>{t}</b><span>{d}</span></span></label></li>' for t, d in PREP)
    body = f'''
<section class="a-hero"><div class="wrap a-hero-in">
<div class="a-hero-txt"><p class="label">House cleaning &middot; Draper &middot; Roy to Spanish Fork</p>
<h1>House cleaning in Draper, <span>by real people with real results.</span></h1>
<p class="lede">Abode books you a vetted, insured local cleaning team, a team of two with its own equipment and supplies, at a flat rate with no contract. You don&rsquo;t even have to be home.</p>
<div class="btn-row"><a class="btn accent" href="@/our-services/">Book a cleaning {ARROW}</a><a class="btn ghost" href="tel:+18018450297">{PHONE} (801) 845-0297</a></div>
<p class="promo"><b>New here?</b> Take $100 off your first recurring cleaning with promo code <code>VIP100U</code>.</p></div>
<div class="a-hero-art"><figure class="ah1">{img("ab-team-door", "An Abode cleaning team arriving at a home's front door with their supplies", priority=True)}</figure>
<figure class="ah2">{img("ab-hood", "A cleaner wiping down a kitchen range hood")}</figure><figure class="ah3">{img("ab-shower", "A cleaner polishing a glass shower door")}</figure></div>
</div></section>

<section class="sec a-how" id="how"><div class="wrap">
<div class="a-head reveal"><p class="label">How it works</p><h2>Flat rates, <span>two-person teams.</span></h2></div>
<div class="how">
<div class="hw reveal"><span class="hw-n">1</span><h3>Pick a package</h3><p>All packages are flat rates, set at minimum rates for homes up to 3 bedrooms, 2 bathrooms and 2,800 sq ft.</p></div>
<div class="hw reveal"><span class="hw-n">2</span><h3>Choose a start time</h3><p>Appointments start at 9 am, 11:30 am or 2:30 pm, with a 1&ndash;2 hour arrival window.</p></div>
<div class="hw reveal"><span class="hw-n">3</span><h3>A team of two arrives</h3><p>Every team brings its own equipment and supplies. Leave out a favorite product if you want it used.</p></div>
<div class="hw reveal"><span class="hw-n">4</span><h3>Come home to clean</h3><p>No contract. Keep the same schedule, change it, or cancel with 24&ndash;48 hours&rsquo; notice.</p></div>
</div></div></section>

<section class="a-film"><div class="film">
<figure class="f1 reveal">{img("ab-floor", "A cleaner mopping a long wood floor through an open kitchen")}<figcaption>Floors</figcaption></figure>
<figure class="f2 reveal">{img("ab-mirror", "A cleaner wiping a bathroom mirror above the sink")}<figcaption>Bathrooms</figcaption></figure>
<figure class="f3 reveal">{img("ab-oven", "A cleaner wiping out an oven")}<figcaption>Kitchens</figcaption></figure>
<figure class="f4 reveal">{img("ab-fridge", "A cleaner wiping a stainless refrigerator")}<figcaption>Appliances</figcaption></figure>
<figure class="f5 reveal">{img("ab-duo", "Two cleaners wiping door frames")}<figcaption>Details</figcaption></figure>
</div><p class="wrap film-cap">Stills from Abode&rsquo;s own film: real teams, a real home.</p></section>

<section class="sec a-ready" id="ready"><div class="wrap a-ready-in">
<div class="reveal"><p class="label">Get ready for your clean</p><h2>Seven small things <span>before we arrive.</span></h2>
<p class="lede">These come straight from our cleaning policies. Tick them off as you go: the better the prep, the more time your team spends on the clean itself.</p>
<div class="meter" data-meter aria-live="polite"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="m-bg" cx="60" cy="60" r="52"/><circle class="m-fg" cx="60" cy="60" r="52" data-ring/></svg>
<div class="m-in"><b data-pct>0%</b><span data-msg>ready</span></div></div>
<div class="slots" data-slots><p class="label">Your arrival windows</p><div class="sl"><b>9:00 am</b><span>start &middot; arrives within 1&ndash;2 hrs</span></div><div class="sl"><b>11:30 am</b><span>start &middot; arrives within 1&ndash;2 hrs</span></div><div class="sl"><b>2:30 pm</b><span>start &middot; arrives within 1&ndash;2 hrs</span></div></div></div>
<ol class="prep" data-prep-list>{prep}</ol>
</div></section>

<section class="sec a-principles"><div class="wrap">
<div class="a-head split-h reveal"><div><p class="label">Guided by purpose</p><h2>Built on <span>three principles.</span></h2></div>
<blockquote class="mission">&ldquo;Our mission is to build small businesses one 5-star service at a time. Abode works with incredible small businesses close to your neighborhood.&rdquo;</blockquote></div>
<div class="pr3"><div class="reveal"><h3>Keep it simple</h3><p>From booking to cleaning, a straightforward, hassle-free experience.</p></div>
<div class="reveal"><h3>Be transparent</h3><p>Clear communication, detailed information about our services and pricing, and no hidden fees.</p></div>
<div class="reveal"><h3>Keep pricing low</h3><p>Quality cleaning shouldn&rsquo;t come with a hefty price tag. Competitive, affordable pricing for a clean, comfortable home.</p></div></div>
</div></section>

<section class="sec a-quotes"><div class="wrap">
<div class="a-head reveal"><p class="label">Reviews</p><h2>Really happy homes.</h2></div>
<div class="aq">{"".join(f'<blockquote class="reveal"><p>{q}</p><footer>{n}</footer></blockquote>' for q, n in QUOTES)}</div>
</div></section>

<section class="sec a-faq" id="faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">FAQ</p><h2>Frequently asked questions.</h2>{faq_html(FAQ)}</div>
<div class="reveal"><figure class="a-side">{img("ab-arrival", "A homeowner opening the front door for her cleaning team")}</figure>
<a class="post-card a-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>What the EPA says about cleaning products, ventilation and storage, in plain language.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "House Cleaning Draper, UT | Abode House Cleaning, Flat Rates",
            "meta": "Abode House Cleaning in Draper and along the Wasatch Front: vetted, insured two-person cleaning teams, flat-rate packages, no contract. Book online.",
            "body": body, "body_class": "is-home", "og": "ab-team-door", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def render(k, skip_first_h1=True, drop=()):
    out, ul, first = [], [], True
    def flush():
        if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in blocks(k):
        plain = html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        if not plain or any(plain.startswith(d) for d in drop): continue
        if t == "li": ul.append(x); continue
        flush()
        if t == "h1" and first and skip_first_h1: first = False; continue
        tag = "h2" if t in ("h1", "h2", "h3") else ("h3" if t == "h4" else "p")
        out.append(f"<{tag}>{x}</{tag}>")
    flush()
    return "\n".join(out)


def make_pages():
    out = [home()]
    svc = f'''<p class="answer">Book a flat-rate house cleaning with a vetted, insured local team. Pricing plans and booking load in the Abode booking app; call <a href="tel:+18018450297">(801) 845-0297</a> if you&rsquo;d rather book by phone.</p>
<h2>What every cleaning includes</h2><ul><li>A team of two with its own equipment and supplies</li><li>Flat-rate packages set at minimum rates for homes up to 3 bed, 2 bath, 2,800 sq ft</li><li>No contract</li><li>Start times at 9 am, 11:30 am or 2:30 pm, with a 1&ndash;2 hour arrival window</li></ul>
<h2>Good to know</h2>{faq_html(FAQ, open_first=False)}<p>Service area as listed on our pages: Ogden to Payson and the St. George area.</p>'''
    out.append(K.page("our-services/", "Services", "House Cleaning Services &amp; Booking", "Flat-rate packages. Teams of two. No contract.", "Our services",
                      "House Cleaning Services &amp; Booking | Abode, Draper, Utah",
                      "Book Abode house cleaning: flat-rate packages for homes up to 3 bed, 2 bath and 2,800 sq ft, two-person teams with supplies, no contract. Draper, UT.",
                      svc, image="ab-floor", alt="A cleaner mopping a wood floor", canonical=canon("our-services/"), form_side=False))
    out.append(K.page("marketplace/", "Marketplace", "Abode Marketplace", "Browse vetted local cleaning businesses.", "Marketplace", "Abode Marketplace | Vetted Local House Cleaners, Utah",
                      "The Abode marketplace connects you with vetted, insured local house cleaning businesses that have been in business more than 3 years. Draper, Utah.",
                      '<p class="answer">Abode works with incredible small businesses close to your neighborhood. They&rsquo;re insured, vetted with the Abode quality process, and have been in business for more than 3 years.</p><p>The marketplace opens in the Abode booking app. <a class="tlink" href="@/our-services/">See services and booking ' + ARROW + '</a></p>',
                      image="ab-duo", alt="Two Abode cleaners at work", canonical=canon("marketplace/")))
    for k, p, lab, h1, title, meta in (("cancellation_policy", "cancellation-policy/", "Cancellation Policy", "Cancellation Policy", "Cancellation Policy | Abode House Cleaning, Draper UT",
                                        "Abode cancellation policy: reschedule or cancel 24 to 48 hours ahead. Same-day cancellations carry a $25 fee; within 8 hours, a $65 fee applies."),
                                       ("term_and_condition", "term-and-condition/", "Terms &amp; Conditions", "Terms and Conditions", "Terms and Conditions | Abode House Cleaning, Draper, Utah",
                                        "Abode terms and conditions: the agreement for using the Abode platform and booking house cleaning, including promotions, liability and arbitration."),
                                       ("privacy_policy", "privacy-policy/", "Privacy Policy", "Privacy Policy", "Privacy Policy &amp; Cleaning Policies | Abode House Cleaning",
                                        "Abode privacy policy and house cleaning policies: how we handle your data, pre-cleaning instructions, arrival windows and what we cannot clean.")):
        body = render(k, drop=("©", "About", "Pricing", "Faqs", "Terms &", "Privacy", "Cancellation Policy"))
        if k == "cancellation_policy":
            body = re.sub(r"(?s)<h2>Cancellation Fees</h2>.*", "", body)
        out.append(K.page(p, lab, h1, "", "Policies", title, meta, body, canonical=canon(p)))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Book a cleaning", "our-services/"), ("Cancellation policy", "cancellation-policy/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Book online.",)) for x in out]
