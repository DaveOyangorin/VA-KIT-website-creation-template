"""Pages for the jsprofinish.com redesign: "Bare studs to finished".

JS ProFinish photographs its jobs at every stage, standing in the same spot each visit (the Clinton basement: drywall hung,
textured, finished). Most contractor sites only show the finished room; this one can show the work. So the site is built
around stages. References (screenshotted 20 Oct 2026): Hammer & Hand (full-bleed craft photography, labelled image tiles,
uppercase captions), Sun Design (warm editorial serif, "a home like yours" room cards), The Basement Sanctuary (basement
category leader: big finished-room photography). Signature: the "same room" stage scrubber on a tape-measure rail.
All 25 live URLs kept (Next.js site, no trailing slash) with their own canonicals; new /blog and one post.
Service pages name Ogden in the title, H1 and first paragraph (report). The home page keeps the client's own focus,
basement finishing (the report's keyword set was pulled for a different business; flagged)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, ST, EMAIL, HOURS
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
PIMG = json.load(open(os.path.join(HERE, "pageimgs.json"), encoding="utf-8"))
ALT = {}
for v in PIMG.values():
    for n, a in v: ALT.setdefault(n, html.unescape(a))
STOP = ("Tell us about your basement", "Planning something like this", "Like what you see")
DROP = re.compile(r"^(Our [\w &;]*work|.* on a real job|Clinton,? |Related services|Photos from|Follow a project|Project gallery)", re.I)
REVIEWS_URL = "https://www.google.com/maps/place/?q=place_id:ChIJIYKoa5IbU4cRxscxPd43Wog"
CITIES = ["Clearfield", "Layton", "Ogden", "Kaysville", "Syracuse", "Farmington", "Bountiful", "Roy", "North Ogden", "South Ogden", "Pleasant View", "Harrisville", "Other / not listed"]
PTYPES = ["Not sure yet", "Full basement finish", "Basement remodel / refresh", "Rec room / family room", "Home theater", "Guest suite / bedroom", "Bathroom remodel", "Painting",
          "Carpentry / trim / built-ins", "Framing or drywall", "Flooring", "Other / not sure yet"]


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def fixsp(s):
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    s = s.replace("ZIP code s", "ZIP codes").replace("&#x27;", "&rsquo;").replace(" →", "")
    s = re.sub(r"\(\s+", "(", s)
    return s


def drop_sections(s):
    out, skip = [], False
    for b in re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s):
        if b.startswith(("<h2>", "<h3>")): skip = bool(DROP.match(txt(b)))
        if not skip: out.append(b)
    return "\n".join(out)


def mig(k, skip=()):
    raw = fixsp(migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x")))
    by = ""
    m = re.search(r"<p>By (Pablo J\. Padilla)[^<]*?Updated\s*</p>\s*(?:<(?:h[23]|p)>((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{4})</(?:h[23]|p)>)?", raw)
    if m:
        by = f"By Pablo J. Padilla, owner &middot; UT Lic. #{ST['license']}" + (f" &middot; Updated {m.group(2).strip()}" if m.group(2) else "")
        raw = raw.replace(m.group(0), "")
    s = drop_sections(tidy(raw, stop=STOP, skip=tuple(skip)))
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    return s.strip(), faqs, by


def strip(names, cap=6):
    names = [n for n in names][:cap]
    if not names: return ""
    figs = "".join(f'<figure class="ps-f reveal-up">{img(n, ALT.get(n, ""))}<figcaption>{ALT.get(n, "")}</figcaption></figure>' for n in names)
    return f'<h2>From our jobs</h2><div class="pstrip">{figs}</div>'


def project_card():
    return f'''<a class="proj-card" href="@/projects/clinton-basement-finish/"><span class="pc-imgs">{img("drywall-hung-clinton-bedroom-closets", "")}{img("finished-clinton-bedroom-bifold-closets", "")}</span>
<span class="pc-t"><span class="label">A real job, every stage</span><b>Clinton basement finish, 900 sq ft</b><span>The same rooms photographed from drywall to done, with who did what spelled out.</span><em>Follow the project {ARROW}</em></span></a>'''


def ttl(k):
    t = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
    t = t if len(t + " | JS ProFinish") <= 60 else t[:60].rsplit(" ", 1)[0]
    return html.escape(t + " | JS ProFinish" if len(t + " | JS ProFinish") <= 60 else t)


def meta_of(k, fb):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    if len(m) < 100: m = fb
    return m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "..."


def jsp_form(title="Get your free estimate"):
    cities = "".join(f"<option>{c}</option>" for c in CITIES)
    pt = "".join(f"<option>{c}</option>" for c in PTYPES)
    return f'''<form class="form" method="post" action="" id="estimate"><h3>{title}</h3><p class="small">We&rsquo;ll call you back within one business day.</p>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label>
<div class="row"><label for="f-city">City *<select id="f-city" name="city" required><option value="">Select your city</option>{cities}</select></label><label for="f-type">Project type<select id="f-type" name="project">{pt}</select></label></div>
<label for="f-msg">Tell us about your basement *<textarea id="f-msg" name="message" required></textarea></label>
<label class="chk"><input type="checkbox" name="agree" required> I agree to be contacted about my project. No spam, no sharing your info.</label>
<button class="btn" type="submit">Get My Free Estimate {ARROW}</button></form>'''


SVCDEF = {"services_basement_remodeling": "Basement Remodeling", "services_framing": "Framing", "services_drywall": "Drywall", "services_carpentry": "Carpentry &amp; Trim",
          "services_painting": "Interior Painting", "services_flooring": "LVP &amp; Flooring", "services_bathroom_remodeling": "Bathroom Remodeling"}
SVCLEAD = {"services_basement_remodeling": "basement remodeling", "services_framing": "basement and interior framing", "services_drywall": "drywall hanging, finishing and texture",
           "services_carpentry": "finish carpentry, trim and built-ins", "services_painting": "interior and cabinet painting", "services_flooring": "LVP, laminate and carpet installs",
           "services_bathroom_remodeling": "bathroom remodels and new basement bathrooms"}


def svc_pages():
    out = []
    for k, lab in SVCDEF.items():
        p = path_of(k); c, f, by = mig(k)
        ims = [n for n, a in PIMG.get(k, [])]
        h1 = f"{lab} in Ogden, Davis &amp; Weber County"
        intro = f"JS ProFinish handles {SVCLEAD[k]} in Ogden, Clearfield, Layton and across Davis and Weber County, with our own licensed crew under one contract."
        t = f"{lab} in Ogden &amp; Davis County, UT | JS ProFinish"
        if len(html.unescape(t)) > 62: t = f"{lab} in Ogden, UT | JS ProFinish"
        m = meta_of(k, f"{html.unescape(lab)} in Ogden, Davis and Weber County from JS ProFinish, a licensed Clearfield crew. Free written estimates.")
        body = c + strip(ims[1:]) + project_card()
        out.append(K.page(p, html.unescape(lab).replace("&", "&amp;"), h1, by or None, "Service", t, m, body, image=ims[0] if ims else "basement3", alt=ALT.get(ims[0], "") if ims else "",
                          intro=intro, crumbs=[("Services", "services/")], faqs=f, canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, html.unescape(lab) + " in Ogden, UT", "Ogden, UT")))
    return out


def place_pages():
    out = []
    keys = [k for k in EXT if k.startswith("cities_")] + ["davis_county", "weber_county"]
    for k in keys:
        p = path_of(k); c, f, by = mig(k)
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        place = t0.replace("Basement Finishing in ", "").replace(", UT", "")
        ims = [n for n, a in PIMG.get(k, [])]
        county = "Weber" if place in ("Ogden", "Roy") else "Davis"
        crumbs = [] if k.endswith("_county") else [(f"{county} County", f"{county.lower()}-county/")]
        hero = ims[0] if ims else ("basement3" if k == "weber_county" else "finished-basement-carpet-open-room")
        out.append(K.page(p, place, html.escape(t0), by or None, "Service area", ttl(k), meta_of(k, f"Basement finishing in {place}, Utah from JS ProFinish in Clearfield."),
                          c + strip(ims[1:] or ["basement4", "finished-basement-bedroom", "builtin-entertainment-center"]) + project_card(), image=hero, alt=ALT.get(hero, ""), crumbs=crumbs, faqs=f,
                          canonical=EXT[k]["canon"] or None,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Basement finishing in {place}, UT", "provider": {"@id": U + "#business"},
                                   "areaServed": {"@type": "AdministrativeArea" if "County" in place else "City", "name": place + ", UT"}}]))
    return out


def services_hub():
    c, f, by = mig("services")
    tiles = ""
    for (k, lab), (n, a) in zip(SVCDEF.items(), PIMG["services"]):
        d = re.search(r"<h3>" + re.escape(lab.split(" ")[0]) + r"[^<]*</h3>\s*<p>(.*?)</p>", c)
        tiles += f'<a class="svc-tile reveal-up" href="@/{path_of(k)}">{img(n, "")}<span class="st-in"><b>{lab}</b><span>{d.group(1) if d else ""}</span><em>{ARROW}</em></span></a>'
    built = re.search(r"<h3>Built into your basement</h3>(.*?)<h3>Something not", c, re.S)
    rooms = re.findall(r"<h3>([^<]+)</h3>\s*<p>(.*?)</p>", built.group(1)) if built else []
    rl = "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in rooms)
    body = f'''<p class="answer">One crew, one contract, start to finish. Basements are our specialty, but we&rsquo;re licensed and insured across our trades, and we take on every one of them as its own job too.</p>
<div class="svc-tiles">{tiles}</div>
<h2>Built into your basement</h2><p>A basement finish is more than four walls. As part of your project, we can build:</p><ul class="rooms">{rl}</ul>
<h2>Something not on the list?</h2><p>We take on remodeling projects beyond these seven trades. If you&rsquo;re not sure whether we do it, call and ask: <a href="tel:{ST["tel"]}">{ST["phone"]}</a>. Not sure what your project needs? We&rsquo;ll walk it with you and tell you straight what it needs. The visit is free.</p>
<p><a class="tlink" href="@/basement-finishing-cost/">What does a basement finish cost in Utah? {ARROW}</a></p>'''
    return K.page("services/", "Services", "Remodeling &amp; Basement Finishing Services", "Seven trades, all our own crew.", "Services", ttl("services"),
                  meta_of("services", "Basement finishing and remodeling services in Northern Utah from JS ProFinish."), body, image="finished-basement-wet-bar", alt=ALT["finished-basement-wet-bar"],
                  canonical=EXT["services"]["canon"] or None)


def raw_sections(k):
    s = open(os.path.join(HERE, "src", "pages", k + ".html"), encoding="utf-8").read()
    s = s[s.find("<main"):]
    out, cur = [], None
    for part in re.split(r"(<h[23][^>]*>.*?</h[23]>)", s, flags=re.S):
        m = re.match(r"<h[23][^>]*>(.*?)</h[23]>", part, re.S)
        if m: cur = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip(); continue
        u = []
        for i in re.findall(r"media%2F([^&\"]+?)\.[a-z0-9_-]{10,16}\.jpg", part):
            if i not in u: u.append(i)
        if u: out.append((cur, u))
    return out


def gallery():
    secs = [(h, ims) for h, ims in raw_sections("gallery") if h and h not in ("Clinton Basement Finish",)]
    keys = {"Finished basements & living spaces": "finished", "Carpentry & built-ins": "carpentry", "Bathrooms, flooring & paint": "finish", "On the job": "job"}
    lede = {"finished": "Complete spaces we&rsquo;ve finished or remodeled: family rooms, kitchenettes, bedrooms, and feature walls.",
            "carpentry": 'Mudroom benches, entertainment centers, closet systems, and barn doors. See our <a href="@/services/carpentry/">carpentry services</a>.',
            "finish": 'The finish trades: <a href="@/services/bathroom-remodeling/">bathrooms</a>, <a href="@/services/flooring/">flooring</a>, and <a href="@/services/painting/">painting</a>.',
            "job": 'What the work looks like before the paint goes on: <a href="@/services/framing/">framing</a> and <a href="@/services/drywall/">drywall</a> in progress. Hard hats and clean job sites are standard on every project.'}
    chips = '<button type="button" class="on" data-filter="all">All</button>' + "".join(f'<button type="button" data-filter="{keys.get(h, "x")}">{html.escape(h)}</button>' for h, ims in secs)
    grid = ""
    for h, ims in secs:
        kk = keys.get(h, "x")
        grid += f'<div class="g-sec" data-cat="{kk}"><h2>{html.escape(h)}</h2><p>{lede.get(kk, "")}</p><div class="masonry">' + \
            "".join(f'<figure class="m-f">{img(n, ALT.get(n, ""))}<figcaption>{ALT.get(n, "")}</figcaption></figure>' for n in ims) + "</div></div>"
    body = f'''<p class="answer">Real photos from real JS ProFinish jobs in Davis and Weber County. No stock images, no renderings. Want to see a project like yours? Give us a call at <a href="tel:{ST["tel"]}">{ST["phone"]}</a>.</p>
{project_card()}<div class="g-chips" role="group" aria-label="Filter photos">{chips}</div>{grid}'''
    return K.page("gallery/", "Gallery", "Project Gallery", "Basement finishing and remodeling photos, all from our own jobs.", "Our work", ttl("gallery"),
                  meta_of("gallery", "Basement finishing and remodeling photos from real JS ProFinish jobs in Davis and Weber County."), body, image="basement4", alt=ALT.get("basement4", ""),
                  canonical=EXT["gallery"]["canon"] or None)


def projects_hub():
    body = f'''<p class="answer">Most contractor photos are the finished room. These pages show what it looked like along the way, so you know what to expect in your own basement.</p>
{project_card()}
<p>A project gets a page here once we have photos of the same rooms at more than one stage. For single photos from other jobs, browse the <a href="@/gallery/">full gallery</a>.</p>'''
    return K.page("projects/", "Projects", "Basement Finishing Projects, Start to Finish", "The same rooms, photographed at every stage.", "Projects", ttl("projects"),
                  meta_of("projects", "Basement finishing projects from JS ProFinish, photographed from start to finish."), body, image="drywall-textured-clinton-rec-room-stairs",
                  alt=ALT.get("drywall-textured-clinton-rec-room-stairs", ""), canonical=EXT["projects"]["canon"] or None)


def clinton():
    secs = dict((h, ims) for h, ims in raw_sections("projects_clinton_basement_finish") if h)
    stages = [("Drywall hung", "Our crew framed the space first (no photos of that stage, a lesson for the next job), then boarded walls and ceilings in the family room, bedroom, laundry, bathroom, and stairwell. Screws set and seams ready for tape. This is the first point where the layout is readable in person."),
              ("Taped, mudded, and textured", "Seams taped and floated, screw holes filled and sanded, ceilings sprayed with texture. This stage decides whether the walls read flat under paint, so it gets the time it needs before primer goes on."),
              ("Paint, trim, doors, and hardware", "Primer, then two-tone paint: warm gray walls against white ceilings, trim, and doors. Two-panel doors hung and cased, baseboard run, bi-fold closet doors with a shelf and rod inside, and matte black hardware on every door. The flooring was installed by others.")]
    sg = ""
    for i, (h, d) in enumerate(stages):
        ims = secs.get(h, [])
        sg += f'''<div class="stage-sec"><p class="st-n">Visit {i + 1} of 3 &middot; {len(ims)} photos</p><h2>{h}</h2><p>{d}</p><div class="masonry">''' + \
            "".join(f'<figure class="m-f">{img(n, ALT.get(n, ""))}<figcaption>{ALT.get(n, "")}</figcaption></figure>' for n in ims) + "</div></div>"
    body = f'''<p class="answer">A 900 square foot basement finish in Clinton, Davis County: an open family room, a bedroom with closets, a laundry area, and a bathroom with a shower. We framed it, hung and finished the drywall, ran the doors and trim, painted it, and set the hardware. Then we photographed the same rooms at three points so you can see what each stage looks like.</p>
<dl class="facts"><div><dt>Finished area</dt><dd>900 sq ft</dd></div><div><dt>Where</dt><dd>Clinton, Davis County</dd></div><div><dt>When</dt><dd>3 visits, July to August 2026</dd></div><div><dt>Our trades</dt><dd>Framing, drywall, carpentry, paint, hardware</dd></div></dl>
<h2>We stood in the same place for each set of photos.</h2><p>That way the stages line up and you can see exactly what changed between visits. Pick a room, then move along the tape.</p>
{home_v3.scrubber(compact=True)}
<h2>About this job</h2><p>The house is a few minutes from our Clearfield shop. The finished lower level runs a two-tone scheme: warm gray walls against white ceilings, trim, and doors, with matte black hardware on every door. The flooring in the finished photos was installed by others, so we don&rsquo;t take credit for it.</p>
<blockquote>Every photo on this page was taken on site by our crew. Nothing is staged and nothing is a rendering.</blockquote>
<h2>What we did</h2><ol class="did"><li>Framed the family room, bedroom, closets, laundry, and bathroom walls</li><li>Drywall hung on walls and ceilings, including the stairwell and under-stair storage</li><li>Seams taped and floated, screw holes filled, full sanding</li><li>Sprayed ceiling texture</li><li>Primer and two-tone paint: gray walls with white ceilings, trim, and doors</li><li>Two-panel interior doors hung and cased</li><li>Bi-fold closet doors with a shelf and hanging rod inside each closet</li><li>Baseboard throughout and a new stair handrail</li></ol>
<h2>Who did what</h2><p>We only take credit for work our own crew did.</p>
<div class="whodid"><div><h3>JS ProFinish</h3><ul><li>Framing</li><li>Drywall, tape, mud, and texture</li><li>Finish carpentry: doors, casing, baseboard, closets</li><li>Paint</li><li>Door hardware</li></ul></div><div><h3>Others</h3><ul><li>Flooring</li></ul></div></div>
<p>Read more about our <a href="@/services/framing/">framing</a>, <a href="@/services/drywall/">drywall</a>, <a href="@/services/carpentry/">carpentry &amp; trim</a>, and <a href="@/services/painting/">painting</a> services.</p>
{sg}'''
    pg = K.page("projects/clinton-basement-finish/", "Clinton basement finish", "Clinton Basement Finish: 900 Sq Ft, Every Stage", "Clinton, Davis County &middot; July to August 2026", "Project",
                ttl("projects_clinton_basement_finish"), meta_of("projects_clinton_basement_finish", "A 900 sq ft basement finish in Clinton, Utah, photographed at every stage."),
                body, image="finished-clinton-bedroom-bifold-closets", alt=ALT.get("finished-clinton-bedroom-bifold-closets", ""), crumbs=[("Projects", "projects/")],
                canonical=EXT["projects_clinton_basement_finish"]["canon"] or None, ogtype="article")
    pg["body"] = pg["body"].replace('<div class="wrap sv-grid"><article class="prose">', '<div class="wrap sv-grid wide-art"><article class="prose">', 1)
    return pg


def cost_page():
    c, f, by = mig("basement_finishing_cost")
    c = re.sub(r"<p>Sources:</p>\s*<p>and ", '<p class="small sources">Sources: <a href="https://www.homeadvisor.com/cost/basements/" rel="nofollow noopener">HomeAdvisor: How Much Does Basement Finishing Cost?</a> and ', c)
    def tier(m): return f'<div class="tier reveal-up"><h3>{m.group(1)}</h3><p class="t-p">{m.group(2)}</p><p class="t-e">{m.group(3)}</p>{m.group(4)}</div>'
    c = re.sub(r"<h3>((?:Basic|Mid-range|Custom) finish)</h3>\s*<p>(.*?)</p>\s*<p>(.*?)</p>\s*(<ul>.*?</ul>)", tier, c, flags=re.S)
    c = re.sub(r'(<div class="tier.*</div>)', r'<div class="tiers">\1</div>', c, count=1, flags=re.S)
    c = c.replace("<p>Typical basement finishing cost ranges in Utah by finish level</p>", "")
    c = re.sub(r"<h3>What a real job looks like</h3>.*?(?=<p>Planning a full finish)", "<h3>What a real job looks like</h3><p>Numbers on a page only go so far. Here is a recent 900 sq ft finish in Clinton, photographed at every stage, with a plain list of which trades were ours.</p>" + project_card(), c, flags=re.S)
    return K.page("basement-finishing-cost/", "Basement finishing cost", "Basement Finishing Cost in Utah: What to Expect", by or None, "Cost guide", ttl("basement_finishing_cost"),
                  meta_of("basement_finishing_cost", "Basement finishing cost in Utah: typical per square foot ranges and what moves the price."), c, image="finished-basement-carpet-open-room",
                  alt=ALT.get("finished-basement-carpet-open-room", ""), faqs=f, canonical=EXT["basement_finishing_cost"]["canon"] or None, ogtype="article")


def about():
    c, f, by = mig("about_us", skip=("About JS ProFinish", "Established 2019"))
    c = re.sub(r"<p>class=\"[^\"]*\">\s*", "<p>", c)
    c = re.sub(r"<p>Licensed &amp; insured &middot;[^<]*</p>|<h3>Finishing basements since 2019</h3>|<h3>Based in Clearfield, serving Davis &amp; Weber Counties</h3>", "", c)
    pre = f'''<dl class="facts"><div><dt>Since</dt><dd>2019</dd></div><div><dt>Based in</dt><dd>Clearfield, UT</dd></div><div><dt>License</dt><dd>UT #{ST["license"]}</dd></div><div><dt>Owner</dt><dd>Pablo J. Padilla</dd></div></dl>'''
    post = f'<figure class="sheet">{img("crew-staging-insulation", ALT.get("crew-staging-insulation", "JS ProFinish crew on site"))}<figcaption>On site, mid-job: staging a framed basement before insulation and drywall.</figcaption></figure>'
    return K.page("about-us/", "About", "About JS ProFinish", "We finish basements the right way. No shortcuts, no surprises.", "About", ttl("about_us"),
                  meta_of("about_us", "About JS ProFinish, a licensed basement finishing contractor in Clearfield, Utah, owned by Pablo J. Padilla, since 2019."),
                  pre + c + post, image="drywall-finishing-crew", alt="JS ProFinish crew finishing drywall in a basement", canonical=EXT["about_us"]["canon"] or None)


def contact():
    info = f'''<p class="answer">Tell us about your basement and we&rsquo;ll call you back within one business day. Or skip the form and call <a href="tel:{ST["tel"]}">{ST["phone"]}</a>.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:{ST["tel"]}">{ST["phone"]}</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Shop</dt><dd>{ST["street"]}<br>Clearfield, UT {ST["zip"]}</dd></div><div><dt>Hours</dt><dd>{HOURS}</dd></div></dl>
<h2>Why homeowners pick us</h2><ul class="ticks"><li>Free, no-pressure estimates</li><li>Licensed &amp; insured in Utah</li><li>Finishing basements since 2019</li><li>We answer our own phone, and it&rsquo;s the people doing the work</li></ul>
<p><a class="tlink" href="{REVIEWS_URL}" rel="noopener">See our reviews on Google {ARROW}</a></p>'''
    pg = K.page("contact-us/", "Contact", "Get a Free Basement Estimate", "Free, written, with the price fixed before work starts.", "Contact", ttl("contact_us"),
                meta_of("contact_us", "Get a free written basement finishing estimate from JS ProFinish in Clearfield, UT. Call (385) 626-3514 or send the form."), info,
                canonical=EXT["contact_us"]["canon"] or None, form_side=True)
    pg["body"] = re.sub(r'<div class="form-col">.*?</form>', lambda m: '<div class="form-col">' + jsp_form("Tell us about your basement"), pg["body"], count=1, flags=re.S)
    return pg


def make_pages():
    out = [home_v3.home(jsp_form)] + svc_pages() + place_pages() + [services_hub(), gallery(), projects_hub(), clinton(), cost_page(), about(), contact()] + p_blog.pages(K, img) + \
          [K.notfound((("Services", "services/"), ("Projects", "projects/"), ("Free estimate", "contact-us/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (385) 626-3514.", " Free written estimates.")) for x in out]
