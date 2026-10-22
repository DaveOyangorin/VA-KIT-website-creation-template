"""Pages for the 5starkb.com redesign: "Before / After".

A remodeler's whole argument is the difference between the old room and the new one, and 5 Star has the photos to prove it: before/after
composites and dozens of iPhone shots of finished kitchens and baths. So the home page opens on a full-bleed photo of their own finished
kitchen, and the signature is a draggable before/after slider built from their composites, set in a gallery-like frame. Charcoal and
their gold star, a high-contrast Bodoni for a showroom feel, generous photography throughout.
References (screenshotted 21 Oct 2026): Houzz (photo-led project pages), Rejuvenation (warm editorial home goods), Studio McGee
(design-studio restraint, big interiors).
Same 16 URLs and canonicals; /home is the live home URL (written to the site only, since the preview uses home/ for the home page)."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from fx import blocks
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
cta = K.cta
header, footer = K.header, K.footer
PAIRS = [("k4", "Cabinet refacing", "From honey oak to bright white, with new floors and counters."), ("k1", "White kitchen", "New white cabinets, farmhouse sink and stainless appliances."),
         ("k2", "Galley kitchen", "Dark wood and white appliances, reworked in white and stainless."), ("k3", "Warm wood kitchen", "Red counters and white cabinets, redone in cherry and stone.")]
CONSULT = ["Evaluate your space and discuss your goals for the project.", "Review design options, materials and layout possibilities.", "Provide a clear, written estimate for the work."]
DIFF = ["Quality and process driven", "Excellent customer service", "Family operated and locally owned", "Free estimates", "Friendly, knowledgeable and trustworthy",
        "High-quality materials", "Quick turnaround time", "Reasonable rates", "Dependable, reliable and honest"]
FAQ = [("Is the in-home estimate really free?", "<p>Yes. We come to your home, evaluate your space and talk through your goals, review design options, materials and layouts, and leave you with a clear, written estimate. No pressure, no guesswork.</p>"),
       ("What do you remodel?", "<p>Kitchens and bathrooms: cabinets and cabinet refacing, countertops, showers and tub-to-shower conversions, walk-in tubs, and windows.</p>"),
       ("What are your hours?", "<p>Monday to Friday, 9 am to 6 pm, and Saturday, 10 am to 3 pm. We&rsquo;re closed Sunday. Our showroom is at 6951 S 300 W, Suite A, in Midvale.</p>"),
       ("Where do you work?", "<p>Midvale, Salt Lake City and surrounding Utah communities.</p>")]


def slider(key, title, note, i):
    return f'''<figure class="ba{" on" if i == 0 else ""}" data-ba="{i}"><div class="ba-frame" data-ba-frame style="--pos:50%">
<div class="ba-after">{img("kb-" + key + "-after", f"{title}: after the 5 Star remodel", priority=(i == 0), lazy=(i != 0))}</div>
<div class="ba-before">{img("kb-" + key + "-before", f"{title}: before the remodel", lazy=(i != 0))}</div>
<span class="ba-tag b">Before</span><span class="ba-tag a">After</span>
<input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare before and after: {title}" data-ba-range>
<span class="ba-handle" aria-hidden="true"><i></i></span></div><figcaption><b>{title}</b> {note}</figcaption></figure>'''


def home():
    tabs = "".join(f'<button type="button" class="ba-tab{" on" if i == 0 else ""}" data-ba-tab="{i}">{t}</button>' for i, (k, t, n) in enumerate(PAIRS))
    body = f'''
<section class="s-hero"><div class="s-hero-img" data-parallax="0.08">{img("kb-hero", "A bright white kitchen with a large island, remodeled by 5 Star Kitchen and Bath", priority=True)}</div>
<div class="wrap s-hero-in"><div class="s-hero-txt"><p class="label"><span class="stars" aria-hidden="true">&#9733;</span> Midvale showroom &middot; Kitchens &amp; baths</p>
<h1>Kitchen and bathroom remodeling in Midvale. <em>Experience the ultimate remodel.</em></h1>
<p class="lede">5 Star Kitchen and Bath is a family-operated, locally owned remodeling company serving Salt Lake City and surrounding Utah communities: kitchens, bathrooms, showers, walk-in tubs and windows, done on time and within budget.</p>
<div class="btn-row"><a class="btn accent" href="@/contact_us/">Free in-home estimate {ARROW}</a><a class="btn ghost" href="tel:+18019994548">{PHONE} 801-999-4548</a></div></div>
<ol class="s-steps" aria-label="How a remodel works"><li><span>01</span>Appointment</li><li><span>02</span>Design</li><li><span>03</span>Planning</li><li><span>04</span>Remodeling</li></ol></div></section>

<section class="sec s-ba" id="before-after"><div class="wrap">
<div class="s-head split-h reveal"><div><p class="label">Before &amp; after</p><h2>Drag the line. <em>See the difference.</em></h2></div><p class="lede">Real 5 Star projects, photographed before and after. Pull the handle across each room.</p></div>
<div class="ba-wrap" data-ba-wrap><div class="ba-tabs" role="group" aria-label="Choose a project">{tabs}</div><div class="ba-stage">{"".join(slider(k, t, n, i) for i, (k, t, n) in enumerate(PAIRS))}</div></div>
</div></section>

<section class="sec s-rooms"><div class="wrap">
<div class="s-head reveal"><p class="label">What we remodel</p><h2>Kitchens. Baths. <em>The details in between.</em></h2></div>
<div class="rooms">
<a class="rm r1 reveal" href="@/kitchens/"><figure>{img("kb-navy-kitchen", "A kitchen with navy lower cabinets, open shelves and white subway tile")}</figure><span class="rm-k">01</span><b>Kitchens</b><p>Cabinets, refacing, countertops and full kitchen remodels.</p></a>
<a class="rm r2 reveal" href="@/bathrooms/"><figure>{img("kb-blue-bath", "A bathroom with a new shower, pedestal sinks and blue walls")}</figure><span class="rm-k">02</span><b>Bathrooms</b><p>Showers, tub-to-shower conversions and full bathroom renovations.</p></a>
<a class="rm r3 reveal" href="@/walk_in_tubs/"><figure>{img("kb-corner-tub", "A renovated bathroom with a corner tub and stone-look surround")}</figure><span class="rm-k">03</span><b>Walk-in tubs</b><p>Acrylic walk-in tubs with dual gravity drains and auto-cleansing systems.</p></a>
<a class="rm r4 reveal" href="@/windows/"><figure>{img("kb-white-kitchen", "A white kitchen with a range hood and natural light")}</figure><span class="rm-k">04</span><b>Windows</b><p>Window replacement, with the same in-home estimate.</p></a>
</div></div></section>

<section class="s-band"><div class="band-img" data-parallax="0.1">{img("kb-blue-bath", "A remodeled bathroom with a new shower and pedestal sinks")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our mission</p><p>To elevate kitchen and bathroom remodeling in Utah by delivering innovative, durable, beautifully designed spaces that improve everyday living.</p></blockquote></div></section>

<section class="sec s-consult"><div class="wrap s-consult-in">
<figure class="reveal">{img("kb-dark-kitchen", "A remodeled kitchen with dark cabinets, a center island and stainless appliances")}</figure>
<div class="reveal"><p class="label">No pressure. No guesswork.</p><h2>What happens at your <em>free in-home consultation.</em></h2>
<ol class="cons">{"".join(f"<li><span>{i + 1:02d}</span>{c}</li>" for i, c in enumerate(CONSULT))}</ol>
<p>Our goal is to help you create a space that&rsquo;s beautiful, functional and thoughtfully designed for the way you live.</p>
<a class="btn accent" href="@/contact_us/">Book your estimate {ARROW}</a></div>
</div></section>

<section class="sec s-gal"><div class="wrap">
<div class="s-head split-h reveal"><div><p class="label">Gallery</p><h2>Rooms we&rsquo;ve <em>finished.</em></h2></div><span class="gl-links"><a class="tlink" href="@/kitchen_gallery/">Kitchens {ARROW}</a> <a class="tlink" href="@/bath_gallery/">Baths {ARROW}</a></span></div>
<div class="gal">
<figure class="g1 reveal">{img("kb-wood-kitchen", "A kitchen with wood cabinets, an island with stools and stainless appliances")}</figure>
<figure class="g2 reveal">{img("kb-glass-shower", "A glass-enclosed shower with stone-look walls")}</figure>
<figure class="g3 reveal">{img("kb-marble-sink", "A marble countertop with an undermount sink")}</figure>
<figure class="g4 reveal">{img("kb-subway-shower", "A white subway tile shower")}</figure>
<figure class="g5 reveal">{img("kb-island-bar", "A breakfast bar island with pendant seating")}</figure>
<figure class="g6 reveal">{img("kb-vessel-sinks", "Double vessel sinks on a granite vanity")}</figure>
</div></div></section>

<section class="sec s-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">What makes us different</p><h2>Built the way <em>you&rsquo;d want it.</em></h2><ul class="diff">{"".join(f"<li>{d}</li>" for d in DIFF)}</ul></div>
<div class="reveal"><p class="label">Questions</p>{faq_html(FAQ)}<a class="post-card s-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>What the EPA says about moisture, ventilation and humidity, and the signs it&rsquo;s time to remodel.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": EXT["home"]["canon"] or U, "title": "Kitchen &amp; Bathroom Remodeling Midvale | 5 Star Kitchen &amp; Bath",
            "meta": "5 Star Kitchen and Bath: kitchen and bathroom remodeling in Midvale and Salt Lake City. Cabinets, countertops, showers, walk-in tubs. Free in-home estimates.",
            "body": body, "body_class": "is-home", "og": "kb-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def gallery(names):
    return '<div class="pgal">' + "".join(f'<figure>{img(n, a)}<figcaption>{c}</figcaption></figure>' for n, a, c in names) + "</div>"


KIT = [("kb-navy-kitchen", "Navy and white kitchen with subway tile", "Navy lowers, open shelving"), ("kb-wood-kitchen", "Wood kitchen with island", "Island with seating"),
       ("kb-dark-kitchen", "Dark cabinet kitchen", "Dark cabinets, stone counters"), ("kb-white-kitchen", "White kitchen with range hood", "White shaker cabinets"),
       ("kb-gray-kitchen", "Gray and white kitchen", "Two-tone cabinets"), ("kb-island-bar", "Kitchen island bar", "Breakfast bar"),
       ("kb-granite-island", "Granite island top", "Granite island"), ("kb-waterfall", "Waterfall countertop", "Waterfall edge"), ("kb-wine-rack", "Cabinet wine rack detail", "Built-in wine rack"),
       ("kb-built-in", "Custom built-in cabinetry", "Custom built-in")]
BATH = [("kb-blue-bath", "Bathroom with new shower and pedestal sinks", "New shower, pedestal sinks"), ("kb-tan-bath", "Bathroom with glass shower", "Glass shower, pedestal sink"),
        ("kb-corner-tub", "Corner tub with stone-look surround", "Corner tub surround"), ("kb-glass-shower", "Glass shower enclosure", "Glass enclosure"),
        ("kb-subway-shower", "White subway tile shower", "Subway tile shower"), ("kb-vessel-sinks", "Double vessel sink vanity", "Double vessel sinks"), ("kb-marble-sink", "Marble vanity top", "Marble top")]


def render(k, drop=()):
    out, ul = [], []
    def flush():
        if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul.clear()
    started = False
    for t, x in blocks(k):
        plain = html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        if t == "h1": started = True; continue
        if not started or not plain or any(d in plain for d in drop): continue
        if t == "li": ul.append(x); continue
        flush()
        tag = "h2" if t == "h2" else ("h3" if t in ("h3", "h4") else "p")
        out.append(f"<{tag}>{x}</{tag}>")
    flush()
    return "\n".join(out)


TUB_HEADS = ["Acrylic VS Gelcoat.", "Gravity Driven 2” Dual Drain Technology vs single electrical 1 ½” drains by competitors.", "Unique exclusive designs for maximum interior space, comfort, and seat width.",
             "Multiple cleansing mechanisms to ensure the cleanliness and longevity of your walk-in bathtub.", "Select models offer independent foot massage, enjoy a foot massage without having to fully bathe.",
             "Strategically placed jetting to maximize therapeutic effects.", "Wide variety of optional equipment, fixtures, and accessories.", "Unique designs and fixtures."]
TUB_DROP = re.compile(r"Patented|A\+ BBB|shipping|Chicago|California Company|competition because|competitors typically|than our competition", re.I)


def tub_body():
    t = EXT["why_choose_our_walk_in_tubs"]["text"]
    t = t[t.find(TUB_HEADS[0]):t.find("Our Walk In Bathtubs stand out")]
    out, pos = [], 0
    marks = [(t.find(h), h) for h in TUB_HEADS if t.find(h) > -1]
    marks.sort()
    for i, (at, h) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(t)
        chunk = t[at + len(h):end].strip()
        sents = [x for x in re.split(r"(?<=[.!?])\s+", chunk) if x and not TUB_DROP.search(x)]
        title = h.rstrip(".").replace("Gravity Driven 2” Dual Drain Technology vs single electrical 1 ½” drains by competitors", "Dual 2” gravity-driven drains")
        out.append(f"<h2>{html.escape(title)}</h2>" + "".join(f"<p>{html.escape(' '.join(sents[j:j + 3]))}</p>" for j in range(0, len(sents), 3)))
    return "".join(out)


def text_paras(k, start, stop):
    t = EXT[k]["text"]; t = t[t.find(start) + len(start):t.find(stop)].strip()
    sents = re.split(r"(?<=[.!?])\s+", t)
    return "".join(f"<p>{html.escape(' '.join(sents[j:j + 4]))}</p>" for j in range(0, len(sents), 4))


def svc(p, lab, h1, im, alt, intro, gal, title, meta, extra=""):
    diff = '<h2>What makes us different</h2><ul class="diff in">' + "".join(f"<li>{d}</li>" for d in DIFF) + "</ul>"
    cons = "<h2>Your free in-home consultation</h2><ol>" + "".join(f"<li>{c}</li>" for c in CONSULT) + "</ol>"
    body = f'<p class="answer">{intro}</p>{extra}{gallery(gal) if gal else ""}{diff}{cons}'
    return K.page(p, lab, h1, "Free in-home estimate &middot; 801-999-4548", "Remodeling", title, meta, body, image=im, alt=alt, canonical=EXT[p.strip("/")]["canon"] if p.strip("/") in EXT else canon(p),
                  schema=K.svc_schema(p, html.unescape(lab), "Midvale, UT"))


def make_pages():
    out = [home()]
    h = home(); out.append(dict(h, path="home/", canonical=EXT["home"]["canon"] or U, site_only=True, sitemap=False))
    out.append(svc("kitchens/", "Kitchens", "Kitchen Remodeling in Midvale &amp; Salt Lake City", "kb-wood-kitchen", "A remodeled kitchen with wood cabinets and an island",
                   "From new cabinets and countertops to a complete kitchen remodel, we handle every stage of the project, whether you&rsquo;re at the rough-draft stage or the materials are already bought, on time and within budget.",
                   KIT[:6], "Kitchen Remodeling Midvale, UT | 5 Star Kitchen and Bath",
                   "Kitchen remodeling in Midvale and Salt Lake City by 5 Star Kitchen and Bath: cabinets, refacing, countertops and full remodels. Free in-home estimates."))
    out.append(svc("bathrooms/", "Bathrooms", "Bathroom Remodeling in Midvale &amp; Salt Lake City", "kb-blue-bath", "A remodeled bathroom with a new shower",
                   "Showers, tub-to-shower conversions and full bathroom renovations, designed around how you use the room and built with high-quality materials.",
                   BATH[:6], "Bathroom Remodeling Midvale, UT | 5 Star Kitchen and Bath",
                   "Bathroom remodeling in Midvale and Salt Lake City by 5 Star Kitchen and Bath: showers, tub-to-shower conversions and full renovations. Free in-home estimates."))
    wit = '<p class="answer">A wide variety of high-quality acrylic walk-in bathtubs, over 900 SKUs and 20+ models, in many shapes, styles and sizes, with customizable packaging and jetting options.</p>' + tub_body()
    out.append(svc("walk_in_tubs/", "Walk-in tubs", "Walk-In Tubs in Midvale &amp; Salt Lake City", "kb-corner-tub", "A renovated bathroom with a tub surround",
                   "A wide variety of high-quality acrylic walk-in bathtubs, over 900 SKUs and 20+ models, in a range of shapes, styles and sizes, with customizable packaging and jetting options.",
                   None, "Walk-In Tubs Midvale, UT | 5 Star Kitchen and Bath",
                   "Acrylic walk-in tubs from 5 Star Kitchen and Bath in Midvale: 20+ models, dual 2-inch gravity drains, ozone and autopurge cleansing. Free in-home estimates.",
                   '<p><a class="tlink" href="@/why_choose_our_walk_in_tubs/">Why choose our walk-in tubs ' + ARROW + '</a></p>'))
    out.append(K.page("why_choose_our_walk_in_tubs/", "Why our walk-in tubs", "Why Choose Our Walk-In Tubs?", "Acrylic, dual gravity drains, automatic cleansing.", "Walk-in tubs",
                      "Why Choose Our Walk-In Tubs? | 5 Star Kitchen and Bath, Utah",
                      "Why 5 Star walk-in tubs: solid acrylic vs gelcoat, stainless frames, dual 2-inch gravity drains, roomy seats, and ozone and autopurge cleansing systems.",
                      wit, crumbs=[("Walk-in tubs", "walk_in_tubs/")], canonical=EXT["why_choose_our_walk_in_tubs"]["canon"]))
    out.append(svc("windows/", "Windows", "Window Replacement in Midvale &amp; Salt Lake City", "kb-white-kitchen", "A kitchen with natural light from new windows",
                   "Replacement windows from the same local, family-operated team, with the same free in-home estimate and a clear, written quote.",
                   None, "Window Replacement Midvale, UT | 5 Star Kitchen and Bath",
                   "Window replacement in Midvale and Salt Lake City from 5 Star Kitchen and Bath: a local, family-operated team with free in-home estimates and written quotes."))
    out.append(K.page("kitchen_gallery/", "Kitchen gallery", "Kitchen Gallery", "Kitchens we&rsquo;ve remodeled.", "Gallery", "Kitchen Remodel Gallery | 5 Star Kitchen and Bath, Midvale",
                      "Photos of kitchens remodeled by 5 Star Kitchen and Bath in Midvale and the Salt Lake area: cabinets, refacing, islands, countertops and before-and-afters.",
                      '<p class="answer">Kitchens we&rsquo;ve finished around the Salt Lake area, including before-and-afters.</p>' + gallery(KIT) + gallery([("kb-" + k + "-after", t + " after", t + ": after") for k, t, n in PAIRS]),
                      image="kb-navy-kitchen", alt="A remodeled navy and white kitchen", canonical=EXT["kitchen_gallery"]["canon"]))
    out.append(K.page("bath_gallery/", "Bath gallery", "Bath Gallery", "Bathrooms we&rsquo;ve remodeled.", "Gallery", "Bathroom Remodel Gallery | 5 Star Kitchen and Bath, Midvale",
                      "Photos of bathrooms remodeled by 5 Star Kitchen and Bath in Midvale and the Salt Lake area: showers, tub surrounds, tub-to-shower conversions and vanities.",
                      '<p class="answer">Bathrooms we&rsquo;ve finished around the Salt Lake area.</p>' + gallery(BATH), image="kb-tan-bath", alt="A remodeled bathroom with a glass shower",
                      canonical=EXT["bath_gallery"]["canon"]))
    about = render("about_us", drop=("national dealer network", "you've always wanted", "200 locations"))
    out.append(K.page("about_us/", "About", "About 5 Star Kitchen &amp; Bath", "Family operated. Locally owned.", "About", "About 5 Star Kitchen and Bath | Remodeling in Midvale, Utah",
                      "About 5 Star Kitchen and Bath: a family-operated, locally owned kitchen and bathroom remodeler in Midvale with clear values and free in-home estimates.",
                      about, image="kb-dark-kitchen", alt="A remodeled kitchen", canonical=EXT["about_us"]["canon"]))
    info = f'''<p class="answer">Call, email or stop by the Midvale showroom. Or send the form for a free in-home estimate.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18019994548">801-999-4548</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Showroom</dt><dd><address>6951 S 300 W Ste a<br>Midvale, UT 84047</address></dd></div><div><dt>Hours</dt><dd>Monday&ndash;Friday 9:00 am&ndash;6:00 pm<br>Saturday 10:00 am&ndash;3:00 pm<br>Sunday closed</dd></div></dl>
<h2>What happens next</h2><ol>{"".join(f"<li>{c}</li>" for c in CONSULT)}</ol>'''
    for p, k in (("contact_us/", "contact_us"), ("contact2/", "contact2")):
        out.append(K.page(p, "Contact", "Contact 5 Star Kitchen &amp; Bath", "Free in-home estimates.", "Contact", "Contact 5 Star Kitchen and Bath | Free Estimate, Midvale UT" if k == "contact_us" else "Contact Us | 5 Star Kitchen and Bath, Midvale, Utah",
                          "Contact 5 Star Kitchen and Bath in Midvale: call 801-999-4548, email sales@5starkb.com, or book a free in-home estimate for your kitchen or bath remodel.",
                          info, canonical=EXT[k]["canon"], form_side=True))
    out.append(K.page("designmybath/", "Design your bathroom", "Design Your Bathroom", "Start with a free in-home consultation.", "Bathrooms", "Design Your Bathroom | 5 Star Kitchen and Bath, Midvale UT",
                      "Design your bathroom with 5 Star Kitchen and Bath: a free in-home consultation to review layouts, materials and options, with a clear written estimate.",
                      '<p class="answer">Every bathroom design starts in your home. We&rsquo;ll look at the space, talk through how you use it, and review layouts and materials together.</p><ol>' + "".join(f"<li>{c}</li>" for c in CONSULT) + "</ol>" + gallery(BATH[:3]),
                      canonical=EXT["designmybath"]["canon"], form_side=True))
    out.append(K.page("now_hiring/", "Now hiring", "Now Hiring", "Join a family-operated remodeling team.", "Careers", "Now Hiring | 5 Star Kitchen and Bath Careers, Midvale, Utah",
                      "Now hiring at 5 Star Kitchen and Bath in Midvale: inside sales, sales and design consultants, door-to-door marketers and installation team members.",
                      '<p class="answer">We&rsquo;re hiring for these roles:</p><ul><li>Inside sales</li><li>Sales and design consultants</li><li>Door-to-door marketers</li><li>Installation team members</li></ul><p>Call <a href="tel:+18019994548">801-999-4548</a> or email <a href="mailto:sales@5starkb.com">sales@5starkb.com</a>.</p>',
                      canonical=EXT["now_hiring"]["canon"], form_side=True))
    out.append(K.page("testimonials/", "Testimonials", "Testimonials", "", "Reviews", "Testimonials | 5 Star Kitchen and Bath, Midvale, Utah",
                      "Customer testimonials for 5 Star Kitchen and Bath in Midvale are being collected. Call 801-999-4548 to talk about your kitchen or bathroom remodel today.",
                      '<p class="answer">We&rsquo;re gathering customer stories for this page. In the meantime, see our <a href="@/kitchen_gallery/">kitchen</a> and <a href="@/bath_gallery/">bath</a> galleries.</p>',
                      canonical=EXT["testimonials"]["canon"], robots="noindex, follow", sitemap=False))
    pp = text_paras("privacy_policy", "PRIVACY POLICY 5 Star", "FREE IN HOME ESTIMATE Are")
    pp = "<p>5 Star" + pp[3:] if pp.startswith("<p> ") else pp
    out.append(K.page("privacy_policy/", "Privacy Policy", "Privacy Policy", "", "Legal", "Privacy Policy | 5 Star Kitchen and Bath of Utah, Midvale",
                      "5 Star Kitchen and Bath privacy policy: what information we collect through 5starkb.com, how we use it, SMS messaging terms and how to contact us.",
                      pp, canonical=EXT["privacy_policy"]["canon"]))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Kitchens", "kitchens/"), ("Bathrooms", "bathrooms/"), ("Contact", "contact_us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free estimates.",)) for x in out]
