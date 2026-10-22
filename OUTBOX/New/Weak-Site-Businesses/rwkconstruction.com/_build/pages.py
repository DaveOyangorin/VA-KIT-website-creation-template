"""Pages for the rwkconstruction.com redesign: "Below grade".

RWK's main work happens below the grade line, in Utah basements. So the site borrows the architect's section drawing: a full-bleed photo
of one of their finished family rooms with a dimensioned grade line running across it, and a signature "Plan your basement" section where
you pick rooms, size and year built and watch a house section fill in, checked live against RWK's own project rules (500 sq ft minimum,
walkouts only with a full finish, homes built 1975 or later). Charcoal and their construction yellow, Archivo (wide for display), Instrument
Serif for the customer's voice, JetBrains Mono for drawing labels.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big interiors), Dwell (editorial headline under a full photo), ArchDaily
(architectural project grid and drawing-sheet labels).
Same URLs (trailing slash) and canonicals, including the six posts at the root."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta


def src(name):
    return open(os.path.join(HERE, "src", "pages", name), encoding="utf-8", errors="ignore").read()


# --- testimonials, exactly as published on /testimonials/
def reviews():
    s = src("testimonials.html")
    out = []
    for q, n in re.findall(r"(?s)<blockquote>(.*?)</blockquote>\s*<small[^>]*>\s*-\s*<i>(.*?)</i>", s):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<br\s*/?>", " ", re.sub(r"(?s)<(?!br)[^>]+>", "", q)))).strip()
        out.append((t, html.unescape(n).strip()))
    return out


REV = reviews()
PICK = ["Ally Knudsen", "Lindsey Castleberry", "Dok Kwon"]

STEPS = [("Consultation", "We meet with you in person to talk through your ideas and needs. Bring your photos, floor plans, Pinterest boards and wish list. We get to know each other, discuss pricing and see if we&rsquo;re the right fit."),
         ("Design", "Already have a design? Great. If not, we&rsquo;ll sit down with you, go through your plans and help you make the most of the space. We&rsquo;ve done numerous projects of all styles."),
         ("Communication", "Once you decide to move forward, you get a login to our online Homeowner Portal: the schedule, progress photos, new requests, expenses and when payments are due, all in one place."),
         ("Construction", "With the design squared away and your portal set up, construction starts. Our team keeps communication open and transparent with everyone involved."),
         ("Finishing up", "As we near the end we meet once more to answer any questions or concerns, and walk you through our warranty process in case anything comes up after we leave."),
         ("Post-completion", "Your space is ready to enjoy, show off, and make memories in for years to come.")]
RULES = [("500+", "sq ft", "Basements must be at least 500 square feet."), ("1975", "or newer", "We&rsquo;re not currently taking on houses older than 1975."),
         ("Walkouts", "with a full finish", "We only build basement walkouts when we&rsquo;re also finishing the whole basement.")]
FAQ = [("What size basement do you take on?", "<p>Basements need to be at least 500 square feet. Below that, we&rsquo;re not the right fit for the project.</p>"),
       ("Can you add a walkout to my basement?", "<p>Yes, when we&rsquo;re also finishing the whole basement. We don&rsquo;t build walkouts as a stand-alone project.</p>"),
       ("Do you work on older homes?", "<p>We&rsquo;re not currently taking on houses older than 1975.</p>"),
       ("How will I know what&rsquo;s happening on my project?", "<p>Every client gets a login to our online Homeowner Portal: the schedule, progress photos, requests, expenses and payment dates, plus a direct line to us.</p>"),
       ("Where do you work?", "<p>Salt Lake, Utah, Davis and Tooele Counties. Our office is in Bluffdale, open Monday to Friday, 9 am to 4 pm.</p>")]
ROOMS = [("family", "Family room"), ("theater", "Theater"), ("bed", "Bedroom"), ("bath", "Bathroom"), ("gym", "Home gym"), ("play", "Playroom"),
         ("office", "Office"), ("bar", "Kitchenette / bar"), ("store", "Storage")]


def rv(t, n, cls=""):
    return f'<blockquote class="rv{cls}"><p>{html.escape(t)}</p><footer>{html.escape(n)}</footer></blockquote>'


def section_svg():
    """The house in section: two floors above grade, the basement below, filled in by concept.js."""
    return '''<svg class="sx" viewBox="0 0 640 430" role="img" aria-labelledby="sx-t"><title id="sx-t">House section showing the basement you are planning</title>
<defs><pattern id="soil" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0v12" stroke="currentColor" stroke-width="1" opacity=".22"/></pattern></defs>
<g class="sx-house" fill="none" stroke="currentColor" stroke-width="2"><path d="M110 196V96l210-72 210 72v100"/><path d="M110 196h420M110 120h420" opacity=".55"/>
<path d="M170 196v-48h40v48M430 150h50v28h-50z" opacity=".55"/></g>
<rect class="sx-soil" x="0" y="196" width="640" height="234" fill="url(#soil)"/>
<path class="sx-grade" d="M0 196H640" stroke="var(--accent)" stroke-width="2.5"/>
<path class="sx-grade-walk" d="M530 196L640 300" stroke="var(--accent)" stroke-width="2.5" fill="none"/>
<text class="sx-lab" x="8" y="188">GRADE &#177;0&#8242;-0&#8243;</text><text class="sx-lab" x="8" y="214">BELOW GRADE</text>
<rect class="sx-base" x="110" y="214" width="420" height="132" fill="var(--sx-bg)" stroke="currentColor" stroke-width="3"/>
<g class="sx-rooms" data-sx-rooms></g>
<rect class="sx-door" x="522" y="276" width="14" height="66" fill="var(--accent)"/>
<g class="sx-dim" stroke="currentColor" stroke-width="1"><path d="M110 372H530M110 364v16M530 364v16"/></g>
<text class="sx-lab sx-dimt" x="320" y="398" text-anchor="middle" data-sx-dim>1,200 SQ FT</text></svg>'''


def planner():
    chips = "".join(f'<label class="chip"><input type="checkbox" name="room" value="{k}"{" checked" if k in ("family", "theater", "bed", "bath") else ""}><span>{l}</span></label>' for k, l in ROOMS)
    return f'''<div class="pl" data-planner>
<form class="pl-form" onsubmit="return false" aria-label="Plan your basement">
<fieldset><legend><span>01</span> Rooms</legend><div class="chips">{chips}</div></fieldset>
<fieldset><legend><span>02</span> Size</legend><label class="pl-range" for="pl-sq"><b data-pl-sqv>1,200</b> sq ft<input id="pl-sq" type="range" min="300" max="3000" step="50" value="1200" data-pl-sq></label></fieldset>
<fieldset class="pl-two"><div><legend><span>03</span> Year built</legend><label class="pl-year" for="pl-yr"><input id="pl-yr" type="number" inputmode="numeric" min="1900" max="2026" value="2005" data-pl-yr></label></div>
<div><legend><span>04</span> Extras</legend><label class="tog"><input type="checkbox" data-pl-walk><span>Add a walkout</span></label><label class="tog"><input type="checkbox" checked data-pl-whole><span>Finish the whole basement</span></label></div></fieldset>
</form>
<div class="pl-out">
<figure class="pl-fig">{section_svg()}</figure>
<ul class="pl-rules" aria-live="polite"><li data-rule="size"><i></i><span><b>500 sq ft minimum</b><small data-r-size>1,200 sq ft. Good to go.</small></span></li>
<li data-rule="year"><i></i><span><b>Built 1975 or later</b><small data-r-year>Built 2005. Good to go.</small></span></li>
<li data-rule="walk"><i></i><span><b>Walkouts with a full finish</b><small data-r-walk>No walkout planned.</small></span></li></ul>
<div class="pl-next"><p data-pl-sum>Family room, theater, bedroom and bathroom in about 1,200 sq ft.</p><a class="btn accent" href="@/contact/" data-pl-cta>Book a free consultation {ARROW}</a></div>
</div></div>'''


def home():
    rv3 = "".join(rv(t, n, f" r{i}") for i, (t, n) in enumerate(r for p in PICK for r in REV if r[1] == p))
    steps = "".join(f'<li><span>{i + 1:02d}</span>{s}</li>' for i, (s, t) in enumerate(STEPS))
    body = f'''
<section class="g-hero"><div class="gh-img" data-parallax="0.08">{img("rw-family", "A finished family room with a blue feature wall, leather sofas and tall windows, built by RWK Construction", priority=True)}</div>
<div class="wrap gh-in"><div class="gh-txt"><p class="label">Bluffdale, Utah &middot; Building since 2001</p>
<h1>Basement finishing and home remodeling in Utah, <em>built the right way.</em></h1>
<p class="lede">RWK Construction is a Bluffdale general contractor that finishes basements, remodels homes and builds home theaters and custom homes across Salt Lake, Utah, Davis and Tooele Counties. It starts with a free consultation at your home.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Free consultation &amp; estimate {ARROW}</a><a class="btn ghost" href="tel:+18018204049">{PHONE} 801-820-4049</a></div></div></div>
<div class="grade" aria-hidden="true"><div class="wrap"><span>GRADE &#177;0&#8242;-0&#8243;</span><span>&#9660; BELOW GRADE</span></div></div>
<div class="wrap"><ol class="gh-steps" aria-label="How a project works">{steps}</ol></div></section>

<section class="sec g-plan" id="plan"><div class="wrap">
<div class="g-head split-h reveal"><div><p class="label">Sheet A-1 &middot; Plan your basement</p><h2>Draw it before <em>we build it.</em></h2></div>
<p class="lede">Pick the rooms you want, set the size and the year your house was built. The section fills in, and we&rsquo;ll check it against the three rules we build by.</p></div>
{planner()}
</div></section>

<section class="sec g-svc"><div class="wrap">
<div class="g-head reveal"><p class="label">What we build</p><h2>Four kinds of project. <em>One way of building.</em></h2></div>
<div class="svc4">
<a class="sv s1 reveal" href="@/services/"><figure>{img("rw-basement", "A finished basement family room with a sectional sofa, recessed lighting and wood-look floors")}</figure><span class="sv-k">01</span><b>Basement finishing</b><p>Designing and finishing basements since 2001, from the plan to the last coat of paint.</p></a>
<a class="sv s2 reveal" href="@/services/#renovations"><figure>{img("rw-kitchen", "A remodeled kitchen with a long island, pendant lights and mountain views")}</figure><span class="sv-k">02</span><b>Home renovations</b><p>A bigger laundry room, a larger kitchen or the whole house.</p></a>
<a class="sv s3 reveal" href="@/galleries/theater-rooms/"><figure>{img("rw-theater", "A home theater with a star ceiling and rows of reclining seats")}</figure><span class="sv-k">03</span><b>Home theaters</b><p>Wall-sized screens, reclining rows and surround sound.</p></a>
<a class="sv s4 reveal" href="@/galleries/928/"><figure>{img("rw-home", "A new custom home with stone accents and a three-car garage in Saratoga Springs")}</figure><span class="sv-k">04</span><b>Custom homes</b><p>New homes built from the ground up.</p></a>
</div></div></section>

<section class="g-band"><div class="band-img" data-parallax="0.1">{img("rw-fireplace", "A living room with a tiled fireplace wall and floor-to-ceiling windows")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Since 2001</p><p>Our mission has been to make your vision a reality: passionate experts, excellent communication, and an honest, timely process.</p><footer>Utah-born. Salt Lake, Utah, Davis &amp; Tooele Counties.</footer></blockquote></div></section>

<section class="sec g-proc"><div class="wrap g-proc-in">
<div class="reveal"><p class="label">Process</p><h2>Six steps, <em>and you can see every one.</em></h2><p class="lede">Every RWK client gets a login to our Homeowner Portal: the schedule, progress photos, requests and payments, in one place.</p><a class="tlink" href="@/process/">The full process {ARROW}</a></div>
<ol class="proc">{"".join(f'<li class="reveal"><span>{i + 1:02d}</span><b>{s}</b><p>{t}</p></li>' for i, (s, t) in enumerate(STEPS))}</ol>
</div></section>

<section class="sec g-rev"><div class="wrap">
<div class="g-head split-h reveal"><div><p class="label">Reviews</p><h2>In our clients&rsquo; <em>own words.</em></h2></div><a class="tlink" href="@/testimonials/">Read all {len(REV)} reviews {ARROW}</a></div>
<div class="rv3">{rv3}</div></div></section>

<section class="sec g-gal"><div class="wrap">
<div class="g-head split-h reveal"><div><p class="label">Galleries</p><h2>Rooms we&rsquo;ve <em>finished.</em></h2></div><a class="tlink" href="@/galleries/">See the galleries {ARROW}</a></div>
<div class="gal">
<figure class="g1 reveal">{img("rw-dining", "A round dining table beside a white kitchen with a tall pantry wall")}</figure>
<figure class="g2 reveal">{img("rw-sauna", "A cedar sauna with a glass door off a finished bathroom")}</figure>
<figure class="g3 reveal">{img("rw-stone-fire", "A sitting room with a stacked-stone fireplace and a wood mantel")}</figure>
<figure class="g4 reveal">{img("rw-shower", "A glass shower and a freestanding tub in a bright bathroom")}</figure>
<figure class="g5 reveal">{img("rw-bunk", "A guest bedroom with built-in shelving and a colorful quilt")}</figure>
<figure class="g6 reveal">{img("rw-hall", "A finished hallway with new carpet, art and a barn door")}</figure>
</div></div></section>

<section class="sec g-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Before you call</p><h2>Three rules <em>we build by.</em></h2>
<div class="rules">{"".join(f'<div class="rule"><b>{a}</b><small>{b}</small><p>{c}</p></div>' for a, b, c in RULES)}</div>
<a class="post-card g-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>What EPA says about testing, the 4 pCi/L action level, and why the time to test is before a renovation.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal"><p class="label">Questions</p>{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": EXT["home"]["canon"] or U, "title": "Basement Finishing Utah | RWK Construction Co., Bluffdale",
            "meta": "RWK Construction finishes basements, remodels homes and builds home theaters and custom homes across Salt Lake, Utah, Davis and Tooele Counties. Since 2001.",
            "body": body, "body_class": "is-home", "og": "rw-family", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def gallery(names, cls="pgal"):
    return f'<div class="{cls}">' + "".join(f'<figure>{img(n, a)}<figcaption>{c}</figcaption></figure>' for n, a, c in names) + "</div>"


ROOMS_G = [("rw-kitchen", "A remodeled kitchen with a long island and pendant lights", "Kitchen with island seating"), ("rw-island", "A kitchen island with leather stools and a double oven wall", "Island and double ovens"),
           ("rw-dining", "A round dining table beside a white kitchen", "Dining nook"), ("rw-living", "A living room with a leather sofa and a framed mirror", "Living room"),
           ("rw-fireplace", "A living room with a tiled fireplace wall and floor-to-ceiling windows", "Fireplace wall"), ("rw-stone-fire", "A sitting room with a stacked-stone fireplace", "Stacked-stone fireplace"),
           ("rw-bed-a", "A bedroom with a patterned rug and mountain-view windows", "Primary bedroom"), ("rw-bed-fire", "A white bedroom with a fireplace and built-in hooks", "Bedroom with fireplace"),
           ("rw-bed-mtn", "A bedroom with a painted mountain mural and a chandelier", "Mountain mural bedroom"), ("rw-bunk", "A guest bedroom with built-in shelving", "Built-in shelving"),
           ("rw-sauna", "A cedar sauna with a glass door", "Cedar sauna"), ("rw-bath-tub", "A bathroom with a tiled tub surround", "Tub and tile surround"),
           ("rw-vanity", "A double vanity with wood cabinets and stone counters", "Double vanity"), ("rw-shower", "A glass shower and a freestanding tub", "Glass shower and soaking tub"),
           ("rw-hall", "A finished hallway with new carpet and a barn door", "Hallway and barn door"), ("rw-family", "A family room with a blue feature wall", "Family room")]


def svc_text():
    t = EXT["services"]["text"]
    a, b, c = t.find("Basement Finishing Since"), t.find("Home Renovations Whether"), t.find("Home Theaters Nothing")
    def paras(x):
        x = x.replace("we can take help you", "we can help you")
        s = re.split(r"(?<=[.!?])\s+", x.strip())
        return "".join(f"<p>{html.escape(' '.join(s[j:j + 3]))}</p>" for j in range(0, len(s), 3))
    return (paras(t[a + len("Basement Finishing "):b]), paras(t[b + len("Home Renovations "):c]), paras(t[c + len("Home Theaters "):]))


def posts():
    out = []
    for f in sorted(os.listdir(os.path.join(HERE, "src", "pages"))):
        if not f.startswith("post_"): continue
        s = src(f); slug = f[5:-5] + "/"
        art = re.search(r'(?s)<article class="post[^"]*">(.*?)</article>', s).group(1)
        h = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"(?s)<h2>(.*?)</h2>", art).group(1))).strip()
        date = re.search(r'"datePublished":"([\d-]+)', s).group(1)
        art = re.sub(r'(?s)^.*?</small>', "", art, count=1)
        art = re.sub(r"(?s)<(script|style|figure|img|iframe)\b.*?(</\1>|/?>)", "", art)
        blocks = []
        for tag, inner in re.findall(r"(?s)<(h1|h2|h3|h4|p|li)\b[^>]*>(.*?)</\1>", art):
            inner = re.sub(r"(?s)<(?!/?(?:strong|b|em|i)\b)[^>]+>", "", inner).strip()
            inner = re.sub(r"<(/?)b>", r"<\1strong>", re.sub(r"<(strong|em|i|b)\b[^>]*>", r"<\1>", inner))
            if not re.sub(r"<[^>]+>|&nbsp;|\s", "", inner): continue
            blocks.append((tag, inner))
        body, ul = [], []
        for tag, inner in blocks:
            if tag == "li": ul.append(inner); continue
            if ul: body.append("<ul>" + "".join(f"<li>{x}</li>" for x in ul) + "</ul>"); ul = []
            body.append(f"<h2>{inner.rstrip(':')}</h2>" if tag in ("h1", "h2") else (f"<h3>{inner}</h3>" if tag in ("h3", "h4") else f"<p>{inner}</p>"))
        if ul: body.append("<ul>" + "".join(f"<li>{x}</li>" for x in ul) + "</ul>")
        canon_m = re.search(r'rel="canonical" href="([^"]+)"', s)
        out.append({"slug": slug, "h1": h, "date": date, "body": "\n".join(body), "canonical": canon_m.group(1) if canon_m else canon(slug)})
    return sorted(out, key=lambda p: p["date"], reverse=True)


POSTS = posts()
PT = {"the-art-of-basement-remodeling/": "The Art of Basement Remodeling | RWK Construction Co.", "basement-remodeling-budget-to-luxury/": "Basement Remodeling: From Budget to Luxury | RWK Blog",
      "creating-a-home-office/": "Creating a Home Office Oasis | RWK Construction Co.", "custom-home-building-process-what-to-expect/": "Custom Home Building Process: What to Expect | RWK",
      "maximizing-your-investment-the-roi-of-home-renovations/": "The ROI of Home Renovations | RWK Construction Co., Utah"}
POST_IMG = {"the-art-of-basement-remodeling/": "rw-basement", "basement-remodeling-budget-to-luxury/": "rw-theater", "creating-a-home-office/": "rw-living",
            "custom-home-building-process-what-to-expect/": "rw-home", "maximizing-your-investment-the-roi-of-home-renovations/": "rw-kitchen",
            "gift-cards-to-support-local-restaurants/": "rw-dining"}


def fmt(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime("%b %-d, %Y") if os.name != "nt" else datetime.date.fromisoformat(d).strftime("%b %#d, %Y")


def post_list(new=True):
    items = ([(p_blog.SLUG, p_blog.H1, "2026-10-21", p_blog.IMG)] if new else []) + [(p["slug"], p["h1"], p["date"], POST_IMG.get(p["slug"], "rw-family")) for p in POSTS]
    return '<div class="plist">' + "".join(f'<a class="pl-item" href="@/{s}"><figure>{img(i, "")}</figure><span class="label">{fmt(d)}</span><b>{h}</b><em>Read {ARROW}</em></a>' for s, h, d, i in items) + "</div>"


def make_pages():
    out = [home()]
    bf, rn, th = svc_text()
    sv = f'''<p class="answer">RWK Construction designs and finishes basements, remodels homes, builds home theaters and builds custom homes across Salt Lake, Utah, Davis and Tooele Counties. Every project starts with a free consultation and estimate at your home.</p>
<h2 id="basements">Basement finishing</h2>{bf}{gallery(ROOMS_G[15:16] + [("rw-basement", "A finished basement family room with a sectional sofa", "Basement family room")], "pgal two")}
<h2 id="renovations">Home renovations</h2>{rn}{gallery([ROOMS_G[0], ROOMS_G[13]], "pgal two")}
<h2 id="theaters">Home theaters</h2>{th}{gallery([("rw-theater", "A home theater with a star ceiling and reclining seats", "Star-ceiling theater room")], "pgal one")}
<h2>Before you call</h2><ul>{"".join(f"<li>{c}</li>" for a, b, c in RULES)}</ul>'''
    out.append(K.page("services/", "Services", "Basement Finishing, Remodels &amp; Home Theaters", "Designing and finishing basements in Utah since 2001.", "Services",
                      "Basement Finishing &amp; Home Remodeling Services | RWK Utah",
                      "Basement finishing, home renovations and home theaters from RWK Construction, building in Salt Lake, Utah, Davis and Tooele Counties since 2001. Free estimates.",
                      sv, image="rw-basement", alt="A finished basement family room", canonical=EXT["services"]["canon"],
                      schema=K.svc_schema("services/", "Basement finishing", "Bluffdale, UT"), faqs=FAQ[:3]))
    ab = EXT["about"]["text"]; ab = ab[ab.find("Since 2001"):].strip()
    about = f'''<p class="answer">{html.escape(ab.split(". ")[0])}.</p>{"".join(f"<p>{html.escape(x.strip())}.</p>" for x in ab.rstrip(".").split(". ")[1:])}
<h2>Where we build</h2><ul class="states">{"".join(f"<li>{c}</li>" for c in K.C.AREAS)}</ul>
<h2>How we work</h2><ol>{"".join(f"<li><strong>{s}.</strong> {t}</li>" for s, t in STEPS)}</ol>{gallery([ROOMS_G[4], ROOMS_G[5]], "pgal two")}'''
    out.append(K.page("about/", "About", "About RWK Construction", "Utah-born. Building since 2001.", "About", "About RWK Construction | Utah Basement &amp; Remodel Builder",
                      "RWK Construction has made Utah homeowners' visions a reality since 2001: a Utah-born builder serving Salt Lake, Utah, Davis and Tooele Counties.",
                      about, image="rw-fireplace", alt="A living room with a tiled fireplace wall", canonical=EXT["about"]["canon"]))
    pr = '<p class="answer">Six steps, from the first conversation at your home to the day the space is yours. You can follow every one of them in our Homeowner Portal.</p>' + \
         "".join(f"<h2>{i + 1:02d}. {s}</h2><p>{t}</p>" for i, (s, t) in enumerate(STEPS)) + '<p>RWK Construction Co. is grateful for the opportunity to work with you, and we thank you for choosing to Build the Right Way.</p>'
    out.append(K.page("process/", "Process", "Our Process: Consultation to Completion", "Free consultation, a custom plan, and a portal to follow it all.", "Process",
                      "Our Remodeling Process | RWK Construction Co., Bluffdale UT",
                      "How RWK Construction works: free in-home consultation, design, an online Homeowner Portal, construction, a final walkthrough with warranty, and completion.",
                      pr, image="rw-hall", alt="A finished hallway with a barn door", canonical=EXT["process"]["canon"]))
    cats = [("galleries/basements/", "Basements", "rw-basement"), ("galleries/theater-rooms/", "Theater rooms", "rw-theater"), ("galleries/928/", "Custom homes", "rw-home")]
    gi = '<p class="answer">A few of the rooms we&rsquo;ve finished: basements, theater rooms, custom homes and remodels.</p><div class="cats">' + \
         "".join(f'<a class="cat" href="@/{p}"><figure>{img(i, "")}</figure><b>{l}</b><em>View {ARROW}</em></a>' for p, l, i in cats) + "</div><h2>Rooms and remodels</h2>" + gallery(ROOMS_G)
    out.append(K.page("galleries/", "Galleries", "Photo Galleries", "Basements, theaters, custom homes and remodels.", "Galleries", "Basement &amp; Remodel Photo Galleries | RWK Construction Utah",
                      "Photos of basements, theater rooms, custom homes and remodels by RWK Construction in Utah: family rooms, kitchens, bedrooms, baths and more. Free estimates.",
                      gi, image="rw-kitchen", alt="A remodeled kitchen with a long island", canonical=EXT["galleries"]["canon"]))
    out.append(K.page("galleries/basements/", "Basements", "Basement Gallery", "Basements we&rsquo;ve finished.", "Galleries", "Finished Basement Photos | RWK Construction Co., Utah",
                      "Finished basement photos from RWK Construction in Utah: family rooms, bedrooms, bathrooms, saunas and theater rooms. Call 801-820-4049 for a free estimate.",
                      '<p class="answer">Basements we&rsquo;ve finished, and rooms from the same kind of work.</p>' + gallery([("rw-basement", "A finished basement family room with a sectional sofa", "Basement family room")], "pgal one") +
                      "<h2>More finished rooms</h2>" + gallery([ROOMS_G[15], ROOMS_G[14], ROOMS_G[9], ROOMS_G[10], ROOMS_G[12], ROOMS_G[13]]),
                      image="rw-basement", alt="A finished basement family room", crumbs=[("Galleries", "galleries/")], canonical=EXT["galleries_basements"]["canon"]))
    out.append(K.page("galleries/theater-rooms/", "Theater rooms", "Theater Room Gallery", "Home theaters we&rsquo;ve built.", "Galleries", "Home Theater Room Photos | RWK Construction Co., Utah",
                      "Home theater rooms built by RWK Construction in Utah: star ceilings, reclining theater seating and surround sound. Call 801-820-4049 for a free estimate.",
                      f'<p class="answer">Nothing brings family and friends together like a night at the movies.</p>{th}' + gallery([("rw-theater", "A home theater with a star ceiling and reclining seats", "Star-ceiling theater room")], "pgal one"),
                      image="rw-theater", alt="A home theater with a star ceiling", crumbs=[("Galleries", "galleries/")], canonical=EXT["galleries_theater_rooms"]["canon"]))
    out.append(K.page("galleries/928/", "Custom homes", "Custom Home Gallery", "New homes, built from the ground up.", "Galleries", "Custom Home Builder Photos | RWK Construction Co., Utah",
                      "Custom homes built by RWK Construction in Utah, including a new home on S Amanda Lane in Saratoga Springs. Call 801-820-4049 today for a free consultation.",
                      '<p class="answer">Custom homes we&rsquo;ve built, including this one on S Amanda Lane in Saratoga Springs.</p>' + gallery([("rw-home", "A new custom home with stone accents and a three-car garage", "S Amanda Lane, Saratoga Springs")], "pgal one"),
                      image="rw-home", alt="A new custom home in Saratoga Springs", crumbs=[("Galleries", "galleries/")], canonical=EXT["galleries_928"]["canon"]))
    tl = f'<p class="answer">{len(REV)} reviews from RWK clients, as they wrote them.</p><div class="rv-all">' + "".join(rv(t, n) for t, n in REV) + "</div>"
    out.append(K.page("testimonials/", "Testimonials", "Client Testimonials", "What RWK clients say about their projects.", "Reviews", "Basement Finishing Reviews | RWK Construction Testimonials",
                      f"Read {len(REV)} reviews from RWK Construction clients about their basement finishing and remodeling projects: communication, project managers, schedules and results.",
                      tl, image="rw-family", alt="A finished family room", canonical=EXT["testimonials"]["canon"]))
    info = f'''<p class="answer">Call or send the form to request a free consultation and estimate.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18018204049">801-820-4049</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd><address>14672 Heritage Crest Way<br>Bluffdale, UT 84065</address></dd></div><div><dt>Office hours</dt><dd>Monday&ndash;Friday: 9am&ndash;4pm</dd></div></dl>
<h2>Before you send</h2><ul>{"".join(f"<li>{c}</li>" for a, b, c in RULES)}</ul>
<h2>What happens next</h2><ol>{"".join(f"<li><strong>{s}.</strong> {t}</li>" for s, t in STEPS[:2])}</ol>'''
    out.append(K.page("contact/", "Contact", "Contact RWK Construction", "Free consultation and estimate.", "Contact", "Contact RWK Construction | Free Basement Estimate, Utah",
                      "Contact RWK Construction in Bluffdale: call 801-820-4049 or send the form for a free consultation and estimate on your basement or remodel. Mon-Fri 9-4.",
                      info, canonical=EXT["contact"]["canon"], form_side=True))
    out.append(K.page("blog/", "Blog", "The RWK Blog", "Notes on basements, remodels and building in Utah.", "Blog", "Basement &amp; Remodeling Blog | RWK Construction Co., Utah",
                      "The RWK Construction blog: basement remodeling ideas, home office design, renovation ROI, the custom home process and radon testing for Utah homeowners.",
                      post_list(), canonical=EXT["blog"]["canon"]))
    out.append(K.page("news/", "News", "News &amp; Articles", "Everything we&rsquo;ve posted.", "Blog", "News &amp; Articles | RWK Construction Co., Bluffdale, Utah",
                      "News and articles from RWK Construction in Bluffdale, Utah: basement remodeling, home offices, renovation ROI, custom homes and radon testing for homeowners.",
                      post_list(), canonical=EXT["news"]["canon"], robots="noindex, follow", sitemap=False))
    for p in POSTS:
        note = '<p class="answer">This promotion closed in October 2020.</p>' if p["slug"].startswith("gift-cards") else ""
        t = html.unescape(p["h1"])
        title = PT.get(p["slug"]) or (t if len(t) <= 44 else t.split(":")[0]) + " | RWK Construction"
        first = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<p>(.*?)</p>", p["body"]).group(1)))
        meta = first[:157].rsplit(" ", 1)[0] + "..." if len(first) > 160 else first
        out.append(K.page(p["slug"], t if len(t) < 40 else t.split(":")[0], p["h1"], f"From the blog &middot; {fmt(p['date'])}", "Blog", html.escape(title), html.escape(meta),
                          note + p["body"], image=POST_IMG.get(p["slug"]), alt="", crumbs=[("Blog", "blog/")], canonical=p["canonical"], ogtype="article",
                          schema=[{"@type": "BlogPosting", "@id": p["canonical"] + "#post", "headline": t, "datePublished": p["date"], "author": {"@type": "Organization", "name": NAME},
                                   "publisher": {"@id": U + "#business"}, "mainEntityOfPage": p["canonical"]}]))
    pp = EXT["privacy_policy"]["text"]; pp = pp[pp.find("RWK Construction respects"):]
    heads = ["Data Collection", "Data Usage", "Data Protection", "Data Sharing", "Opt-Out", "Opting Out", "Non-Sharing Clause", "Message Frequency", "Message and Data Rates"]
    for h in heads: pp = pp.replace(" " + h + " ", f"</p><h2>{h}</h2><p>", 1)
    out.append(K.page("privacy-policy/", "Privacy Policy", "Terms and Conditions / Privacy Policy", "", "Legal", "Privacy Policy &amp; SMS Terms | RWK Construction Co., Utah",
                      "RWK Construction privacy policy and SMS terms: what we collect when you sign up for text updates, how we use and protect it, and how to opt out at any time.",
                      "<p>" + pp + "</p>", canonical=EXT["privacy_policy"]["canon"]))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Galleries", "galleries/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free estimates.", " Call 801-820-4049.")) for x in out]
