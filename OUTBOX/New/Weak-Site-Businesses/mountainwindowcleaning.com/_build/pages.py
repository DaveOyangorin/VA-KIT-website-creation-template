"""Pages for the mountainwindowcleaning.com redesign: "Pure water".

A window cleaner sells one thing: the view. So the home page opens on a full-bleed photo of the Salt Lake Valley under the Wasatch, seen
through glass that is fogged with hard-water spots, and the signature is the glass itself: drag a squeegee across it and the view comes
clear (one stroke plays on load; reduced motion gets a "Clean the glass" button instead). Below it, a tap-water vs pure-water drop diagram
explains their system, a rate card carries their real per-pane prices, and the quote page gets a working estimator built on the same prices
and the $150 visit minimum. Their navy, pine and glacier blue with the amber quote button; Sora, Manrope, IBM Plex Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (clean grid).
Same six URLs (static .html files) on the www host; /index.html is the same file as the home page."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, BOOK, REVIEWS, INSTAGRAM
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

PRICES = [("Exterior window cleaning", "Per pane, pure-water rinse", "$4.00"), ("Interior window cleaning", "Per pane, hand detailed", "$3.00"),
          ("Screen cleaning", "Per screen, washed and rinsed", "$2&ndash;3"), ("Window track deep cleaning", "Per track, vacuumed and wiped", "$5&ndash;10"),
          ("Solar panel cleaning", "Per panel, pure water only", "$4&ndash;6"), ("Hard-water stain removal", "Depends on buildup", "Quoted")]
FAQ = [("How much does window cleaning cost?", "<p>Exterior panes are $4 each and interior panes are $3 each. Screens and tracks are extra, and every visit has a $150 minimum. <a href=@/quote.html>Get an instant quote</a> for an exact price for your home.</p>"),
       ("Do I need to be home?", "<p>Only for interior cleaning. For exterior-only visits, just leave gates unlocked and we&rsquo;ll text you when we&rsquo;re done.</p>"),
       ("What if it rains after my clean?", "<p>Pure-water cleaning leaves no soap residue for rain to stick to, so light rain usually dries without spotting.</p>"),
       ("How often should I clean my windows?", "<p>Most homes look best with two to four cleans a year. Monthly and quarterly plans are discounted.</p>")]
SOLAR_FAQ = [("Why pure water on solar panels?", "<p>No detergents to leave film or void panel warranties. Pure water rinses dust and pollen off and dries clear.</p>"),
             ("Do you walk on the panels?", "<p>Most panels are cleaned safely without walking on them, using soft brushes and water-fed poles.</p>"),
             ("When should solar panels be cleaned?", "<p>Spring pollen and summer dust are the best times to clean.</p>"),
             ("How much does solar panel cleaning cost?", "<p>$4&ndash;6 per panel. Tell us how many panels you have and we&rsquo;ll send a quote. Every visit has a $150 minimum.</p>")]
STEPS = [("Get your instant quote", "Tell us about your home or building. We reply with a clear price, usually the same day."),
         ("We clean, top to bottom", "Our crew arrives on time, protects your floors and landscaping, and details every pane."),
         ("Enjoy the view", "Walk the job with us before we leave. Set up monthly or quarterly service to save.")]
JOBS = [("mw-stone-home", "A Utah home with stone columns and tall windows"), ("mw-modern-home", "A modern stone and glass home with a long front walk"),
        ("mw-log-home", "A log home lit up at dusk above the valley"), ("mw-storefront", "A storefront with floor-to-ceiling glass")]


def rate_card(cls=""):
    rows = "".join(f'<tr><th scope="row">{s}<small>{d}</small></th><td>{p}</td></tr>' for s, d, p in PRICES)
    return f'''<div class="rate{cls}"><div class="rate-h"><span>Rate card</span><span>Salt Lake &amp; Utah Counties</span></div>
<table><caption class="sr">Mountain Window Cleaning prices</caption><thead><tr><th scope="col">Service</th><th scope="col">Price</th></tr></thead><tbody>{rows}</tbody></table>
<p class="rate-min"><b>$150 minimum</b> per visit. Most homes land above it. Monthly and quarterly plans are discounted.</p></div>'''


def drops():
    return '''<svg class="drops" viewBox="0 0 520 250" role="img" aria-labelledby="dr-t"><title id="dr-t">Tap water dries into mineral spots; pure water dries clear</title>
<g class="dr tap"><path d="M130 30c28 40 50 70 50 98a50 50 0 0 1-100 0c0-28 22-58 50-98z"/><g class="min"><circle cx="112" cy="128" r="4"/><circle cx="140" cy="112" r="3.2"/><circle cx="150" cy="142" r="4.6"/><circle cx="124" cy="152" r="3"/><circle cx="104" cy="104" r="2.6"/><circle cx="160" cy="122" r="2.4"/></g>
<path class="arrow" d="M130 192v20M122 205l8 8 8-8"/><ellipse class="spot" cx="130" cy="232" rx="44" ry="9"/><text x="130" y="20" text-anchor="middle">TAP WATER</text></g>
<g class="dr pure"><path d="M390 30c28 40 50 70 50 98a50 50 0 0 1-100 0c0-28 22-58 50-98z"/><path class="arrow" d="M390 192v20M382 205l8 8 8-8"/><ellipse class="clear" cx="390" cy="232" rx="44" ry="9"/><text x="390" y="20" text-anchor="middle">PURE H&#8322;O</text></g></svg>'''


def home():
    jobs = "".join(f'<figure class="j{i} reveal">{img(n, a)}</figure>' for i, (n, a) in enumerate(JOBS))
    body = f'''
<section class="w-hero" data-glass><div class="wh-img">{img("mw-valley", "The Salt Lake Valley and downtown skyline below the snow-capped Wasatch Range", priority=True)}</div>
<canvas class="wh-haze" aria-hidden="true" data-haze></canvas>
<div class="wh-frame" aria-hidden="true"><i></i><i></i></div>
<div class="wrap wh-in"><div class="wh-txt"><p class="label">Window &amp; solar panel cleaning &middot; Sandy, Salt Lake &amp; Utah County</p>
<h1>Window cleaning in Salt Lake &amp; Utah County. <em>Spotless, inside and out.</em></h1>
<p class="lede">Streak-free glass for homes and businesses across Salt Lake and Utah Counties. Pure-water rinse, screens and tracks done right, and simple per-pane pricing.</p>
<div class="btn-row"><a class="btn accent" href="@/quote.html">Get an instant quote {ARROW}</a><a class="btn ghost" href="tel:+18015184062">{PHONE} Call or text 801-518-4062</a></div></div>
<p class="wh-hint"><span data-hint>Drag across the glass</span><button type="button" class="wh-btn" data-clean>Clean the glass</button></p></div></section>

<section class="w-facts"><div class="wrap facts">
<div><b>Pure water</b><span>Filtered water dries spot-free. No soap film.</span></div>
<div><b>$4<small>/pane</small></b><span>Exterior windows. Interior $3.</span></div>
<div><b>$150</b><span>Visit minimum. No hidden fees.</span></div>
<div><b>2 counties</b><span>Salt Lake &amp; Utah, homes and businesses.</span></div></div></section>

<section class="sec w-water"><div class="wrap w-water-in">
<div class="reveal"><p class="label">Our pure-water system</p><h2>Utah tap water is hard. <em>Ours isn&rsquo;t.</em></h2>
<p class="lede">Clean glass with tap water and the minerals dry into spots. We filter the water down to pure H&#8322;O, so it rinses dirt away and dries clear.</p>
<ul class="ticks"><li><b>Spot-free drying.</b> Nothing left behind on the glass to attract dust.</li><li><b>Gentle on frames and panels.</b> No harsh chemicals on seals, screens or solar coatings.</li><li><b>Reaches second stories safely.</b> Water-fed poles clean high glass from the ground.</li></ul></div>
<figure class="reveal drops-fig">{drops()}</figure>
</div></section>

<section class="sec w-svc"><div class="wrap">
<div class="w-head reveal"><p class="label">What we clean</p><h2>Clean glass, <em>done properly.</em></h2><p class="lede">Every visit includes a careful hand clean, detailed edges and sills, and a final check before we leave.</p></div>
<div class="svc3">
<a class="sv sv1 reveal" href="@/window-cleaning.html"><figure>{img("mw-stone-home", "A Utah home with stone columns and tall windows")}</figure><div><span class="sv-p">From $3/pane</span><b>Window cleaning</b><p>Inside and out for homes, condos and storefronts. Hard-to-reach glass handled with water-fed poles.</p><em>Details {ARROW}</em></div></a>
<a class="sv sv2 reveal" href="@/solar-panel-cleaning.html"><figure class="sv-solar" aria-hidden="true"><i></i></figure><div><span class="sv-p">$4&ndash;6/panel</span><b>Solar panel cleaning</b><p>Dust, pollen and canyon grime cut output. We rinse panels with pure water. No soap, no scratches.</p><em>Details {ARROW}</em></div></a>
<a class="sv sv3 reveal" href="@/pricing.html"><figure>{img("mw-storefront", "A storefront with floor-to-ceiling glass")}</figure><div><span class="sv-p">From $2/screen</span><b>Screens, tracks &amp; hard water</b><p>Screens washed, tracks deep cleaned, and hard-water spots treated so the whole window looks new.</p><em>See pricing {ARROW}</em></div></a>
</div></div></section>

<section class="sec w-price"><div class="wrap w-price-in">
<div class="reveal"><p class="label">Pricing</p><h2>Simple, per-pane pricing. <em>No hidden fees.</em></h2><p class="lede">Your instant quote shows the exact total before we schedule.</p>
<ol class="steps">{"".join(f'<li><span>{i + 1}</span><b>{s}</b><p>{t}</p></li>' for i, (s, t) in enumerate(STEPS))}</ol>
<div class="btn-row"><a class="btn accent" href="@/quote.html">Get an instant quote {ARROW}</a><a class="tlink" href="{BOOK}" rel="noopener">Book online {ARROW}</a></div></div>
<div class="reveal">{rate_card()}</div>
</div></section>

<section class="sec w-jobs"><div class="wrap">
<div class="w-head split-h reveal"><div><p class="label">Recent jobs</p><h2>Clear glass, <em>clear views.</em></h2></div><a class="tlink" href="{INSTAGRAM}" rel="noopener">More on Instagram {ARROW}</a></div>
<div class="jobs">{jobs}</div></div></section>

<section class="w-band"><div class="band-img" data-parallax="0.1">{img("mw-canyon", "Autumn color on the mountains above a Utah neighborhood")}</div>
<div class="wrap"><div class="reveal band-in"><p class="label">Service area</p><p class="band-t">Serving Salt Lake &amp; Utah Counties.</p><ul class="areas"><li>Salt Lake County</li><li>Utah County</li></ul>
<p>Not sure if we cover your home? Call or text <a href="tel:+18015184062">801-518-4062</a>.</p></div></div></section>

<section class="sec w-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Window cleaning <em>FAQ.</em></h2><p><a class="tlink" href="{REVIEWS}" rel="noopener">Read our Google reviews {ARROW}</a></p>
<a class="post-card w-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>Why almost half of all bird-window collisions happen at homes, and the 2-inch rule that prevents most of them.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Window Cleaning Sandy, Salt Lake &amp; Utah County | Mountain",
            "meta": "Streak-free window and solar panel cleaning in Sandy, Salt Lake and Utah Counties. Pure-water system, $4 per exterior pane, free instant quotes. 801-518-4062.",
            "body": body, "body_class": "is-home", "og": "mw-valley", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def estimator():
    svc = [("ext", "Outside windows", "$4 per pane", 4, 4, True), ("int", "Inside windows", "$3 per pane", 3, 3, True), ("scr", "Screens", "$2&ndash;3 each", 2, 3, False),
           ("trk", "Window tracks", "$5&ndash;10 each", 5, 10, False), ("sol", "Solar panels", "$4&ndash;6 per panel", 4, 6, False)]
    rows = "".join(f'<label class="es-svc"><input type="checkbox" data-es="{k}" data-lo="{lo}" data-hi="{hi}"{" checked" if on else ""}><span><b>{l}</b><small>{p}</small></span></label>' for k, l, p, lo, hi, on in svc)
    cnt = [("panes", "Window panes", "Count once; we apply it to inside and outside", 25), ("scr", "Screens", "Removable window screens", 0), ("trk", "Tracks", "Sliding window and door tracks", 0), ("sol", "Solar panels", "Total panels on the roof", 0)]
    cr = "".join(f'<div class="es-cnt" data-cnt="{k}"><span><b>{l}</b><small>{d}</small></span><div class="es-step"><button type="button" aria-label="Fewer {l.lower()}" data-dec>&minus;</button><input type="number" min="0" max="400" value="{v}" aria-label="{l}" inputmode="numeric"><button type="button" aria-label="More {l.lower()}" data-inc>+</button></div></div>' for k, l, d, v in cnt)
    return f'''<div class="es" data-est><div class="es-in">
<fieldset><legend><span>1</span> What do you need cleaned?</legend><div class="es-svcs">{rows}<p class="es-note">Hard-water stains are quoted after a look.</p></div></fieldset>
<fieldset><legend><span>2</span> How many?</legend><p class="es-help">Count each separate piece of glass. A window with a top and bottom section is 2 panes. A best guess is fine.</p>{cr}</fieldset></div>
<aside class="es-out" aria-live="polite"><p class="label">Your estimate</p><p class="es-total" data-total>$175</p><p class="es-range" data-range>Estimate for a one-time clean</p><ul class="es-lines" data-lines></ul>
<p class="es-min" data-min>Every visit has a $150 minimum.</p><a class="btn accent" href="{BOOK}" rel="noopener">Book online {ARROW}</a><p class="es-call">Prefer to talk? Call or text <a href="tel:+18015184062">801-518-4062</a>. We confirm the final price before we schedule.</p></aside></div>'''


def privacy():
    s = open(os.path.join(HERE, "src", "pages", "privacy_policy_html.html"), encoding="utf-8", errors="ignore").read()
    s = re.sub(r"(?s)<(script|style|svg|header|footer|nav)\b.*?</\1>", "", s)
    out, ul, started = [], [], False
    for t, x in re.findall(r"(?s)<(h1|h2|h3|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"(?s)<(?!/?(?:strong|b|em|a)\b)[^>]+>", "", x).strip()
        x = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>', r'<a href="\1">', x)
        if t == "h1": started = True; continue
        if not started or not x or x.startswith("How Mountain Window Cleaning handles"): continue
        if "Get your instant quote in about a minute" in x or x.startswith("Ready for spotless"): break
        if t == "li": ul.append(x); continue
        if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul = []
        out.append(f"<h2>{x}</h2>" if t == "h2" else (f"<h3>{x}</h3>" if t == "h3" else f"<p>{x}</p>"))
    if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>")
    return "\n".join(out)


def make_pages():
    out = [home()]
    wc = f'''<p class="answer">Spotless windows for homes and businesses: inside, outside, screens and tracks. We treat your home like our own and leave every pane clear.</p>
<h2>Residential: every visit includes</h2><ul class="ticks"><li><b>Hand-detailed glass.</b> Squeegee finish inside, pure-water rinse outside.</li><li><b>Frames and sills wiped.</b> We clean the edges, not just the middle of the pane.</li>
<li><b>Floors and plants protected.</b> Drop cloths inside, care around landscaping outside.</li><li><b>Final walk-through.</b> We check the job with you before we leave.</li></ul>
<div class="pgal two"><figure>{img("mw-stone-home", "A Utah home with stone columns and tall windows")}<figcaption>Residential</figcaption></figure><figure>{img("mw-modern-home", "A modern stone and glass home")}<figcaption>Large glass, water-fed poles</figcaption></figure></div>
<h2 id="commercial">Commercial: storefronts and offices that look open for business</h2><p>Recurring service on a schedule that fits your hours. Monthly and quarterly plans come with a discount, and we invoice simply.</p>
<div class="pgal one"><figure>{img("mw-storefront", "A storefront with floor-to-ceiling glass")}<figcaption>Storefront glass</figcaption></figure></div>
<p><a class="btn" href="@/quote.html">Request a commercial quote {ARROW}</a></p>
<h2>Pricing</h2>{rate_card(" in")}'''
    out.append(K.page("window-cleaning.html", "Window cleaning", "Window Cleaning in Salt Lake &amp; Utah County", "Inside, outside, screens and tracks. Pure-water finish.", "Window cleaning",
                      "Window Cleaning in Salt Lake &amp; Utah County | Mountain Window",
                      "Residential and commercial window cleaning in Salt Lake and Utah Counties. Inside and out, screens and tracks, pure-water finish. $4 per exterior pane.",
                      wc, image="mw-modern-home", alt="A modern stone and glass home", canonical=canon("window-cleaning.html"), faqs=FAQ,
                      schema=K.svc_schema("window-cleaning.html", "Window cleaning", "Salt Lake County, UT")))
    sc = f'''<p class="answer">Clean panels make more power. Dust, pollen and hard-water film block sunlight. We rinse panels with pure water, so there is no soap and no scratching.</p>
<h2>How we clean panels</h2><ul class="ticks"><li><b>Pure water only.</b> No detergents to leave film or void panel warranties.</li><li><b>Soft brushes, water-fed poles.</b> Most panels are cleaned safely without walking on them.</li>
<li><b>Seasonal schedules.</b> Spring pollen and summer dust are the best times to clean.</li></ul>
<div class="solar-band" aria-hidden="true"><i></i></div>
<h2>$4&ndash;6 per panel</h2><p>Get more from your solar. Tell us how many panels you have and we&rsquo;ll send a quote. Every visit has a $150 minimum.</p>'''
    out.append(K.page("solar-panel-cleaning.html", "Solar panel cleaning", "Solar Panel Cleaning in Salt Lake &amp; Utah County", "Pure water, soft brushes, no scratches.", "Solar panels",
                      "Solar Panel Cleaning in Salt Lake &amp; Utah County | Mountain",
                      "Pure-water solar panel cleaning in Salt Lake and Utah Counties. No soap, no scratches, $4-6 per panel, cleaned without walking on panels. Free instant quotes.",
                      sc, image="mw-canyon", alt="Autumn color on the mountains above a Utah neighborhood", canonical=canon("solar-panel-cleaning.html"), faqs=SOLAR_FAQ,
                      schema=K.svc_schema("solar-panel-cleaning.html", "Solar panel cleaning", "Salt Lake County, UT")))
    pr = f'''<p class="answer">Simple, per-pane pricing with no hidden fees. Your instant quote shows the exact total before we schedule.</p>{rate_card(" in")}
<h2>Save more</h2><p>Monthly and quarterly service plans are discounted. Ask when you get your quote.</p><p><a class="btn" href="@/quote.html">Get an instant quote {ARROW}</a> <a class="tlink" href="{BOOK}" rel="noopener">Book online {ARROW}</a></p>'''
    out.append(K.page("pricing.html", "Pricing", "Window Cleaning Prices", "From $3 per pane. $150 visit minimum.", "Pricing", "Window Cleaning Prices, Salt Lake &amp; Utah County | Mountain",
                      "Window cleaning from $3 per pane in Salt Lake and Utah Counties: screens, tracks, solar panels and hard-water removal, with a $150 minimum for every visit.",
                      pr, image="mw-stone-home", alt="A Utah home with tall windows", canonical=canon("pricing.html"),
                      schema=[{"@type": "OfferCatalog", "name": "Window cleaning prices", "itemListElement": [{"@type": "Offer", "name": html.unescape(s), "description": d} for s, d, p in PRICES]}]))
    qb = '<p class="answer">Pick your services, count your windows, and see your estimate right away. We confirm the final price before we schedule.</p>' + estimator()
    q = K.page("quote.html", "Instant quote", "Instant Window Cleaning Quote", "Your price in about a minute.", "Instant quote", "Instant Window Cleaning Quote | Mountain Window Cleaning",
               "Get an instant window cleaning estimate: pick your services, count your panes and see your price, with a $150 minimum. Serving Salt Lake and Utah Counties.",
               qb, image="mw-valley", alt="The Salt Lake Valley below the Wasatch", canonical=canon("quote.html"), form_side=True)
    q["body"] = q["body"].replace('<div class="wrap sv-grid">', '<div class="wrap sv-grid es-grid">', 1)
    out.append(q)
    out.append(K.page("privacy-policy.html", "Privacy Policy", "Terms &amp; Conditions and Privacy Policy", "How Mountain Window Cleaning handles your information and communications.", "Legal",
                      "Terms &amp; Privacy Policy | Mountain Window Cleaning, Utah",
                      "Mountain Window Cleaning (Pardy LLC) terms and privacy policy: text, email and call programs, opting out, the information we collect, cookies and your choices.",
                      privacy(), canonical=canon("privacy-policy.html")))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Window cleaning", "window-cleaning.html"), ("Pricing", "pricing.html"), ("Instant quote", "quote.html"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free instant quotes.", " Call 801-518-4062.")) for x in out]
