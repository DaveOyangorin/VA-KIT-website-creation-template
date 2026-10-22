"""All pages for the roofwiseut.com redesign, on the client's current 10 URLs plus a new blog post and a 404.

Facts come only from the client's own site (17 Oct 2026): licensed & insured in Utah; 10-year workmanship warranty on
roof replacement projects; in-house crew with 20+ years of roofing experience; 9+ years serving Utah; 200+ customers
helped; 50+ realtor relationships; itemized proposals; the 4-step inspection process and the 6-step replacement plan;
the services and their bullet lists; the "next step" list; the six counties; the insurance disclaimer, word for word.
Not used: "Utah's most trusted roofing contractors" and "one of the best workmanship warranties in the industry"
(superlatives we can't back up). The 12 AI-looking images are not used; photos are frames from the client's own drone video.
Report (17 Oct 2026): home page targets "roofing company salt lake city"; service pages name Salt Lake City.
"""
import html
from build import (U, S, ARROW, PHONE, CHECK, SCHED, SERVICES, BLOG, COUNTIES, DISCLAIMER, img, phero, cta, faq_html, faq_ld,
                   crumbs_ld, contact_form, notice, report_head, canon)
import p_blog

HOME = ("Home", "")
STAMP = [("Prepared by", "RoofWise"), ("Service area", "6 Northern Utah counties"), ("Warranty", "10-year workmanship on replacements"), ("Crew", "20+ years roofing experience")]
STEPS = [("Schedule", "Book a convenient time for a RoofWise roof inspection."),
         ("Inspect", "Our roofing professionals evaluate the roof and look for visible signs of damage."),
         ("Document &amp; consult", "We explain what we find and help you understand the roofing side of the insurance process when appropriate."),
         ("Repair or replace", "If work is needed, RoofWise provides a clear plan for completing the roofing project.")]
NEXT = [("I just had a storm.", "Schedule an inspection.", SCHED), ("I see missing or damaged shingles.", "Schedule an inspection.", SCHED),
        ("I have a roof leak.", "Contact RoofWise.", "contact"), ("My insurance company already inspected my roof.", "Talk to RoofWise about the roofing scope.", "insurance-claims"),
        ("I&rsquo;m not sure if my roof is damaged.", "Schedule an inspection.", SCHED)]


def steps_html(steps):
    return '<ol class="steps">' + "".join(f'<li class="reveal"><span class="n">{i+1:02d}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(steps)) + "</ol>"


def findings(items, status="Included"):
    return '<ul class="findings">' + "".join(f'<li><i>{CHECK}</i><span>{x}</span>{f"<em>{status}</em>" if status else ""}</li>' for x in items) + "</ul>"


def next_table():
    """'Find your situation' as a selector: pick what's going on, see the next step."""
    tabs = "".join(f'<button type="button" role="tab" id="sit-t{i}" aria-controls="sit-p{i}" aria-selected="{"true" if i == 0 else "false"}"{"" if i == 0 else " tabindex=\"-1\""}><span class="n">{i + 1:02d}</span>{s}</button>' for i, (s, a, p) in enumerate(NEXT))
    panels = "".join(f'<div class="sit-panel" role="tabpanel" id="sit-p{i}" aria-labelledby="sit-t{i}"{"" if i == 0 else " hidden"}><p class="label light">Your next step</p><p class="sit-a">{a}</p><a class="btn" href="@/{p}">{a.rstrip(".")} {ARROW}</a></div>' for i, (s, a, p) in enumerate(NEXT))
    return f'<div class="sit"><div class="sit-tabs" role="tablist" aria-label="What&rsquo;s going on with your roof?">{tabs}</div><div class="sit-out">{panels}</div></div>'


def svc_ld(path, name, desc):
    return {"@type": "Service", "@id": canon(path) + "#service", "name": name, "serviceType": name, "description": desc, "provider": {"@id": U + "/#business"},
            "areaServed": {"@type": "City", "name": "Salt Lake City", "containedInPlace": {"@type": "State", "name": "Utah"}}}


def related(cur):
    items = [(p, n, d) for p, n, d in SERVICES if p != cur]
    return '<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">Other services</p><h2>More from RoofWise</h2></div><div class="cards">' + "".join(
        f'<a class="card reveal" href="@/{p}"><span class="n">{[x[0] for x in SERVICES].index(p) + 1:02d}</span><b>{n}</b><span>{d}</span><em>Read more {ARROW}</em></a>' for p, n, d in items) + "</div></div></section>"


def service_page(path, label, h1, title, meta, lede, body, side_items, faqs, image=None, alt="", steps=None):
    trail = [HOME, (label, path)]
    st = f'<section class="sec dark"><div class="wrap"><div class="head reveal"><p class="label light">The plan</p><h2>{steps[0]}</h2></div>{steps_html(steps[1])}</div></section>' if steps else ""
    page_body = phero(trail, h1, lede, "Salt Lake City &amp; Northern Utah", [("Service", label), ("Area", "Salt Lake City &amp; 6 counties"), ("Warranty", "10-year workmanship on replacements")], image, alt) + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{body}</div>
<aside class="side reveal"><div class="panel report"><p class="label">What RoofWise can help with</p>{findings(side_items, "Covered")}</div>
<div class="panel dark"><p class="label light">Next step</p><h3>Start with an inspection</h3><a class="btn" href="@/{SCHED}">Schedule Inspection {ARROW}</a><p class="small">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a></p></div></aside></div></section>
{st}
<section class="sec"><div class="wrap split top"><div class="reveal"><p class="label">Questions</p><h2>Common questions</h2></div><div class="reveal">{faq_html(faqs)}</div></div></section>''' + related(path) + cta()
    return {"path": path, "title": title, "meta": meta, "body": page_body, "og": image, "full_biz": False,
            "schema": [crumbs_ld(path, trail), svc_ld(path, html.unescape(label), lede), faq_ld(faqs)]}


# Marked-up drone frame: only things that can be seen in the frame are labelled.
PINS = [(51, 45, "New underlayment", "The white surface is underlayment going down on this roof section, before shingles."),
        (46, 40, "Shingle bundles staged", "Bundles of new shingles set out along the roof, ready for the crew."),
        (18, 50, "Skylights", "Skylights are a detail to flash and seal carefully on any re-roof."),
        (50, 60, "Ladder access", "The crew&rsquo;s ladder up to the lower roof edge."),
        (66, 52, "Crew trailer", "Truck and trailer with ladders, parked in the drive.")]
SVC_IMG = {"roof-replacement": "drone-reroof-hillside-home", "roof-repair": "drone-reroof-full-property", "insurance-claims": "drone-reroof-underlayment",
           "commercial-roofing": "drone-reroof-crew-on-roof", "gutters": "drone-reroof-full-property"}


def home():
    rows = "".join(f'<li data-img="{SVC_IMG[p]}"><a href="@/{p}"><span class="n">{i+1:02d}</span><span class="t"><b>{n}</b><span>{d}</span></span><i>{ARROW}</i></a></li>' for i, (p, n, d) in enumerate(SERVICES))
    rows += f'<li data-img="drone-reroof-underlayment"><a href="@/{SCHED}"><span class="n">06</span><span class="t"><b>Roof Inspection</b><span>Start with a professional evaluation when you aren&rsquo;t sure what&rsquo;s happening with your roof.</span></span><i>{ARROW}</i></a></li>'
    shots = "".join(f'<div class="svc-shot{" on" if i == 0 else ""}" data-img="{n}">{img(n, "")}</div>' for i, n in enumerate(["drone-reroof-hillside-home", "drone-reroof-full-property", "drone-reroof-underlayment", "drone-reroof-crew-on-roof"]))
    pins = "".join(f'<button type="button" class="pin" data-k="{i}" style="left:{x}%;top:{y}%" aria-label="{t}"><span>{i + 1:02d}</span></button>' for i, (x, y, t, d) in enumerate(PINS))
    plist = "".join(f'<li data-k="{i}"><span class="n">{i + 1:02d}</span><span><b>{t}</b><span>{d}</span></span></li>' for i, (x, y, t, d) in enumerate(PINS))
    faqs = [("Do I need to know what&rsquo;s wrong before I call?", "No. You don&rsquo;t need to know whether the issue is age, storm damage, a leak or an insurance matter. Start with a roof inspection and a clear explanation."),
            ("Can RoofWise help with an insurance claim?", f"RoofWise can inspect your roof, document visible damage, and help you understand the roofing side of the insurance process. {DISCLAIMER}"),
            ("What warranty comes with a new roof?", "Roof replacement projects include a 10-year workmanship warranty."),
            ("How is the price presented?", "You get an itemized breakdown of the project proposal, so you can see what you&rsquo;re paying for."),
            ("Where does RoofWise work?", "Salt Lake City and Northern Utah: Weber, Davis, Salt Lake, Utah, Tooele and Wasatch counties.")]
    body = f'''
<section class="hero"><div class="hero-bg"><video class="hero-video" autoplay muted loop playsinline preload="metadata" poster="@img/drone-reroof-crew-on-roof.webp" aria-hidden="true"><source src="@img/roofwise-drone-reroof.mp4" type="video/mp4"></video></div>
<div class="vf" aria-hidden="true"><span class="rec">REC</span><span class="tc" data-tc>00:00:00</span><span class="vf-cap">RoofWise drone footage &middot; re-roof in progress</span></div>
<div class="wrap hero-in">
<div class="hero-text"><p class="label light">RoofWise &middot; roofing contractor &middot; Salt Lake City</p>
<h1>Roofing company in Salt Lake City, <em>with clear answers first.</em></h1>
<p class="lede">A licensed and insured roofing company for Salt Lake City and Northern Utah: inspections, repairs, replacements, insurance-related roofing, commercial roofing and gutters. It starts with an inspection and a plain explanation of what we find.</p>
<div class="btn-row"><a class="btn" href="@/{SCHED}">Schedule Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="hero-stamp"><p class="label light">Report summary</p>{report_head(STAMP)}</div>
</div></section>

<section class="facts-band"><div class="wrap"><dl class="figures big"><div><dt>10<small>yr</small></dt><dd>workmanship warranty on roof replacements</dd></div><div><dt>20<small>+</small></dt><dd>years of roofing experience in the in-house crew</dd></div><div><dt>200<small>+</small></dt><dd>customers helped</dd></div><div><dt>6</dt><dd>Northern Utah counties served</dd></div></dl></div></section>

<section class="sec markup"><div class="wrap markup-grid">
<div class="reveal"><p class="label">Inspect. Document. Understand.</p><h2>A roof explained, <em>point by point</em></h2>
<p class="lede">A frame from RoofWise&rsquo;s drone footage of a re-roof in progress, marked up the way a report points things out. You get the same kind of plain explanation after an inspection.</p>
<ol class="plist">{plist}</ol></div>
<figure class="reveal shot"><div class="shot-in">{img("drone-reroof-crew-on-roof", "Drone view of a RoofWise re-roof in progress, with underlayment, staged shingle bundles, skylights, a ladder and the crew trailer marked")}{pins}</div>
<figcaption><span class="mono">Frame 02 &middot; drone</span> Re-roof in progress on a hillside home</figcaption></figure>
</div></section>

<section class="sec dark"><div class="wrap"><div class="head row reveal"><div><p class="label light">How it works</p><h2>Four steps, explained as we go</h2></div><a class="more light" href="@/{SCHED}">Start with step one {ARROW}</a></div>{steps_html(STEPS)}</div></section>

<section class="sec situation"><div class="wrap split top">
<div class="reveal"><p class="label">Not sure what your next step is?</p><h2>Find your situation</h2><p class="lede">You don&rsquo;t need to know whether it&rsquo;s age, storm damage or an insurance matter before calling. Pick what&rsquo;s going on.</p></div>
<div class="reveal">{next_table()}</div></div></section>

<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">Roofers in Salt Lake City</p><h2>Roofing services for Northern Utah homes and properties</h2></div>
<div class="svc-grid"><div class="svc-shots reveal">{shots}</div><ul class="svc-rows">{rows}</ul></div></div></section>

<section class="sec dark insure"><div class="wrap split">
<div class="reveal"><p class="label light">Storm damage</p><h2>Could your roof damage be covered by insurance?</h2>
<p class="lede">Not every roof problem is an insurance claim, and not every claim is covered the same way. RoofWise can inspect your roof, document visible damage, and help you understand whether an insurance conversation may make sense.</p>
<div class="btn-row"><a class="btn" href="@/insurance-claims">How insurance claims work {ARROW}</a><a class="btn ghost light" href="@/{BLOG[1]}">What hail damage looks like</a></div>
{notice(DISCLAIMER)}</div>
<figure class="reveal frame">{img("drone-reroof-underlayment", "Drone view of a hillside home mid re-roof, with new underlayment on part of the roof")}<div class="vf small" aria-hidden="true"></div><figcaption><span class="mono">Frame 03</span> Same job, another angle</figcaption></figure>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">About RoofWise</p><h2>Cost-effective roofing <em>without cutting corners</em></h2>
<p class="lede">Northern Utah homeowners choose RoofWise for the balance between cost-effective solutions and high-quality outcomes: quality materials, an in-house crew with more than 20 years of roofing experience, itemized proposals and straightforward communication.</p>
<a class="more" href="@/about">About RoofWise {ARROW}</a></div>
<dl class="figures reveal"><div><dt>200+</dt><dd>customers helped</dd></div><div><dt>50+</dt><dd>realtor relationships</dd></div><div><dt>9+</dt><dd>years serving Utah</dd></div><div><dt>20+</dt><dd>years roofing experience</dd></div></dl>
</div></section>

<section class="sec paper"><div class="wrap split top">
<div class="reveal"><p class="label">Questions</p><h2>Before you call</h2><p class="lede">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div>
<div class="reveal">{faq_html(faqs)}</div></div></section>
''' + cta()
    return {"path": "", "title": "Roofing Company Salt Lake City, UT | RoofWise Roofing",
            "meta": "RoofWise is a licensed roofing company in Salt Lake City and Northern Utah: inspections, roof repair, replacement, insurance claims help and gutters.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(faqs)]}


def replacement():
    body = '''<h2>When repair isn&rsquo;t the right answer</h2>
<p>A roof replacement is a big decision, so RoofWise starts by helping you understand the condition of the roof, the replacement options and the project scope before any work begins. If a repair will do, the inspection will show it.</p>
<h2>Quality materials, experienced labor, straightforward pricing</h2>
<p>RoofWise uses high quality roofing materials selected for long-term performance. The work is done by an in-house crew with more than 20 years of roofing experience.</p>
<p>You get an itemized proposal, so the cost of each part of the project is clear before you agree to anything.</p>
<h2>A 10-year workmanship warranty</h2>
<p>Roof replacement projects include a 10-year workmanship warranty. Material warranties come from the shingle manufacturer and depend on the product you choose; ask about them when you review the proposal.</p>
<h2>Storm damage and insurance</h2>
<p>If the roof was damaged by hail or wind, a replacement may be part of an insurance claim. RoofWise can document the damage and explain the roofing scope. See <a href="@/insurance-claims">insurance claims help</a>.</p>'''
    steps = ("From inspection to final check", [("Inspection", "A professional evaluation of the roof&rsquo;s condition."), ("Material selection", "Choose the roofing materials for your home."),
             ("Detailed proposal", "An itemized breakdown of the project."), ("Preparation", "The site and roof are prepared for the work."),
             ("Installation", "The in-house crew installs the new roof."), ("Final inspection", "A last check of the finished roof.")])
    faqs = [("Does a new roof come with a warranty?", "Yes. RoofWise roof replacement projects include a 10-year workmanship warranty."),
            ("Will I see a price breakdown?", "Yes. You receive an itemized breakdown of the project proposal."),
            ("Who does the work?", "RoofWise&rsquo;s in-house crew, which brings more than 20 years of roofing experience.")]
    return service_page("roof-replacement", "Roof Replacement", "Roof Replacement in Salt Lake City", "Roof Replacement in Salt Lake City, UT | RoofWise Roofing",
                        "Roof replacement in Salt Lake City and Northern Utah: a clear plan, quality materials, itemized proposal and a 10-year workmanship warranty.",
                        "RoofWise replaces roofs in Salt Lake City and across Northern Utah, with a clear replacement plan, quality materials, an experienced in-house crew, an itemized proposal and a 10-year workmanship warranty.",
                        body, ["Full replacement plan", "Material selection", "Itemized proposal", "In-house installation crew", "Final inspection", "10-year workmanship warranty"], faqs,
                        "drone-reroof-hillside-home", "Drone view of a RoofWise re-roof in progress, with materials staged by the house", steps)


def repair():
    body = f'''<h2>Small problems turn into bigger ones</h2>
<p>Leaks and damaged roofing materials can turn into bigger problems. If you see damage or notice water inside, schedule an inspection before the problem spreads. RoofWise will inspect the issue and explain the practical repair options.</p>
<h2>What we inspect and repair</h2>
<ul><li><strong>Leaks</strong>, including water stains on ceilings and walls</li><li><strong>Damaged shingles</strong>: missing, cracked or lifted</li><li><strong>Storm damage</strong> from hail and heavy weather</li><li><strong>Wind damage</strong></li><li><strong>Flashing issues</strong> around chimneys, vents and walls</li><li><strong>Other roofing problems</strong> you&rsquo;re not sure about</li></ul>
<h2>Repair or replace?</h2>
<p>Sometimes a repair is all a roof needs; sometimes the damage or the age of the roof means replacement makes more sense. The inspection is how you find out, and you&rsquo;ll get a straight explanation either way. <a href="@/roof-replacement">Roof replacement &rarr;</a></p>
<h2>After a hail storm</h2>
<p>Hail damage isn&rsquo;t always obvious from the ground. Our guide explains what to look for: <a href="@/{BLOG[1]}">{BLOG[0]}</a></p>'''
    faqs = [("I have a leak. What should I do first?", "Contact RoofWise and, if you can do it safely, protect the area inside from water. An inspection will find where the water is getting in."),
            ("Can you tell if damage is from a storm?", "RoofWise inspects the roof for visible signs of damage and explains what we find. Whether damage is covered by insurance is decided by your insurance carrier.")]
    return service_page("roof-repair", "Roof Repair", "Roof Repair in Salt Lake City", "Roof Repair in Salt Lake City, UT | RoofWise Roofing",
                        "Roof repair in Salt Lake City and Northern Utah: leaks, damaged shingles, storm and wind damage, flashing issues. Schedule a roof inspection with RoofWise.",
                        "RoofWise repairs roofs in Salt Lake City and across Northern Utah: leaks, damaged shingles, storm and wind damage, flashing issues and other roofing problems. It starts with an inspection and a clear explanation of the repair options.",
                        body, ["Leaks", "Damaged shingles", "Storm damage", "Wind damage", "Flashing issues", "Other roofing problems"], faqs,
                        "drone-reroof-full-property", "Drone view of a RoofWise roofing job on a hillside property")


def commercial():
    body = '''<h2>Straightforward roofing guidance for property owners</h2>
<p>RoofWise supports commercial roofing needs in Salt Lake City and across Northern Utah with inspections, clear communication and practical project planning.</p>
<h2>How it works</h2>
<ul><li><strong>Commercial roof inspections:</strong> start with a professional evaluation of the roofing condition.</li>
<li><strong>Clear project scope:</strong> RoofWise explains its findings and provides a practical plan when work is needed.</li>
<li><strong>Northern Utah properties:</strong> service for commercial roofing needs across the RoofWise service area.</li></ul>
<p>Tell us about the building, the roof and any problems you&rsquo;ve noticed when you schedule the inspection.</p>'''
    faqs = [("Do you inspect commercial roofs?", "Yes. Commercial work starts with a professional evaluation of the roofing condition, followed by a clear explanation and a practical plan if work is needed."),
            ("Which areas do you cover for commercial roofing?", "The whole RoofWise service area: Weber, Davis, Salt Lake, Utah, Tooele and Wasatch counties.")]
    return service_page("commercial-roofing", "Commercial Roofing", "Commercial Roofing in Salt Lake City", "Commercial Roofing in Salt Lake City, UT | RoofWise",
                        "Commercial roofing in Salt Lake City and Northern Utah from RoofWise: roof inspections, a clear project scope and practical planning for property owners.",
                        "RoofWise supports commercial roofing in Salt Lake City and across Northern Utah: commercial roof inspections, a clear project scope and practical planning for property owners.",
                        body, ["Commercial roof inspections", "Clear project scope", "Practical project planning", "Northern Utah properties"], faqs)


def gutters():
    body = '''<h2>A clean finish for the roofing system</h2>
<p>Gutters move water off the roof edge and away from the walls and foundation. RoofWise handles gutter installation and repair in Salt Lake City and across Northern Utah, so water moves where it should and your roofline has the support it needs.</p>
<h2>Gutter installation</h2>
<p>Clean gutter installation that supports the roofline and the home&rsquo;s exterior water management.</p>
<h2>Gutter repair</h2>
<p>Repair when gutters are damaged, leaking, detached or not draining correctly.</p>
<h2>Why it matters</h2>
<p>A working gutter system helps move water away from the roof edge and foundation. Overflowing or sagging gutters are worth looking at before the next storm.</p>'''
    faqs = [("Do you install new gutters or only repair them?", "Both. RoofWise handles gutter installation and gutter repair."),
            ("What gutter problems can you fix?", "Gutters that are damaged, leaking, detached or not draining correctly.")]
    return service_page("gutters", "Gutters", "Gutter Installation &amp; Repair in Salt Lake City", "Gutter Installation &amp; Repair, Salt Lake City | RoofWise".replace("&amp;", "&"),
                        "Gutter installation and repair in Salt Lake City and Northern Utah: new gutters, plus fixes for leaking, detached or clogged gutters. Call RoofWise.",
                        "RoofWise installs and repairs gutters in Salt Lake City and across Northern Utah, so water moves off the roof and away from the foundation.",
                        body, ["Gutter installation", "Gutter repair", "Detached or leaking gutters", "Roofline protection"], faqs)


def insurance():
    trail = [HOME, ("Insurance Claims", "insurance-claims")]
    utah = "https://insurance.utah.gov/consumers/home-insurance/home-claims-info/"
    causes = ["Hail", "Wind", "Storm damage", "Missing shingles", "Damaged flashing", "Leaks"]
    faqs = [("Do I need to know whether I have a claim before calling?", "No. RoofWise can inspect the roof and explain the roofing-side findings so you can make a more informed decision."),
            ("I already filed a claim. Can RoofWise still help?", "Yes. RoofWise works with homeowners who have already started the insurance process, helping them understand the roofing scope, visible roof conditions and project steps if roofing work is needed."),
            ("Who decides whether the damage is covered?", DISCLAIMER)]
    body = phero(trail, "Roof Insurance Claim Help in Salt Lake City", "Think your roof damage may be an insurance claim? RoofWise helps homeowners in Salt Lake City and Northern Utah understand roof damage, document what we find, and navigate the roofing side of the insurance process.",
                 "Insurance claims", [("Role", "Roofing-side findings and documentation"), ("Decides coverage", "Your insurance carrier"), ("First step", "Roof inspection")]) + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">
{notice(DISCLAIMER)}
<h2>What can cause roof damage?</h2>
<p>Visible roof damage may come from weather, age, installation issues or other conditions. An inspection helps clarify what is actually happening before you decide what to do next.</p>
<div class="tags">{"".join(f"<span>{c}</span>" for c in causes)}</div>
<h2>Already filed a claim?</h2>
<p>RoofWise can work with homeowners who have already started the insurance process and help them understand the roofing scope, visible roof conditions and project steps if roofing work is needed.</p>
<h2>Not sure whether to file?</h2>
<p>You don&rsquo;t have to know whether you have a claim before scheduling an inspection. RoofWise can inspect the roof and explain the roofing-side findings so you can make a more informed decision.</p>
<h2>What Utah&rsquo;s Insurance Department tells homeowners</h2>
<p>The Utah Insurance Department&rsquo;s guidance on home claims (<a href="{utah}" rel="noopener">insurance.utah.gov</a>) includes these steps:</p>
<ul><li>Call your insurance company or agent with your policy number as soon as possible, and ask what documents they need.</li>
<li>Take photos or video of the damage.</li>
<li>Make temporary repairs to prevent further damage, such as covering a leaking roof, but don&rsquo;t have permanent repairs made until your insurer has inspected the property and you&rsquo;ve agreed on repair costs.</li>
<li>Keep all receipts, including for temporary repairs.</li>
<li>If you have a dispute over the claim, you can contact the state insurance department for help.</li></ul>
<p>Our guide to spotting storm damage: <a href="@/{BLOG[1]}">{BLOG[0]}</a></p>
</div><aside class="side reveal"><div class="panel dark"><p class="label light">Next step</p><h3>Have the roof inspected</h3><a class="btn light" href="@/{SCHED}">Schedule Inspection {ARROW}</a><p class="small">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a></p></div></aside></div></section>
<section class="sec paper"><div class="wrap split top"><div class="reveal"><p class="label">Questions</p><h2>Insurance questions</h2></div><div class="reveal">{faq_html(faqs)}</div></div></section>''' + cta()
    return {"path": "insurance-claims", "title": "Roof Insurance Claim Help, Salt Lake City | RoofWise",
            "meta": "RoofWise inspects roof damage, documents what we find and explains the roofing side of insurance claims for Salt Lake City and Northern Utah homeowners.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("insurance-claims", trail), faq_ld(faqs)]}


def service_area():
    trail = [HOME, ("Service Area", "service-area")]
    cards = "".join(f'<div class="county reveal{" main" if c == "Salt Lake County" else ""}"><b>{c}</b><span>Roof inspections, roof repair, roof replacement, commercial roofing, gutters, and insurance-related roofing consultation.</span></div>' for c in COUNTIES)
    body = phero(trail, "Roofing Services Across Salt Lake City &amp; Northern Utah", "RoofWise serves Salt Lake City and cities across six Northern Utah counties with roof inspections, repairs, replacements, commercial roofing, gutters and insurance-related roofing support.",
                 "Service area", [("Counties", "6"), ("Based around", "Salt Lake City"), ("Services", "All, in every county")]) + f'''
<section class="sec"><div class="wrap"><div class="head reveal"><p class="label">Local roofing help close to home</p><h2>Six Northern Utah counties</h2></div><div class="counties">{cards}</div>
<p class="small" style="margin-top:22px">Not sure if your address is covered? Call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div></section>''' + cta()
    return {"path": "service-area", "title": "Service Area: Salt Lake City & Northern Utah | RoofWise",
            "meta": "RoofWise serves Salt Lake City and six Northern Utah counties, Weber, Davis, Salt Lake, Utah, Tooele and Wasatch, with roof repair, replacement and inspections.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("service-area", trail)]}


def about():
    trail = [HOME, ("About", "about")]
    stands = ["Cost-effective solutions", "High-quality outcomes", "Clear inspection findings", "No-pressure next steps", "Local Northern Utah service"]
    pillars = [("Quality materials", "High quality roofing materials selected for long-term performance."), ("Great warranties", "Roof replacement projects include a 10-year workmanship warranty."),
               ("Experienced labor", "The in-house crew brings more than 20 years of roofing experience."), ("Transparent pricing", "Homeowners receive an itemized breakdown of the project proposal."),
               ("Licensed &amp; insured", "RoofWise is a fully licensed and insured roofing contractor in Utah."), ("Local service", "The team serves counties across Northern Utah with practical roofing guidance.")]
    pil = "".join(f'<div class="pillar reveal"><b>{t}</b><p>{d}</p></div>' for t, d in pillars)
    body = phero(trail, "A Local Roofing Company Built Around Clear Answers", "RoofWise provides high quality, cost-effective roofing solutions to homeowners and property owners in Salt Lake City and Northern Utah.", "About RoofWise",
                 None, "drone-reroof-full-property", "Drone view of a RoofWise roofing job on a hillside property") + f'''
<section class="sec"><div class="wrap split top"><div class="prose reveal">
<h2>Professional roofing guidance for Northern Utah homeowners</h2>
<p>RoofWise exists to help homeowners understand what&rsquo;s happening with their roof and what their next step may be. The team handles roof replacement, roof repair, insurance-related roofing, commercial roofing, and gutter installation and repair.</p>
<p>The company focuses on quality materials, good warranties, experienced labor, transparent pricing and straightforward communication.</p>
<h3>What RoofWise stands for</h3>{findings(stands, "")}</div>
<dl class="figures reveal"><div><dt>200+</dt><dd>customers helped</dd></div><div><dt>50+</dt><dd>realtor relationships</dd></div><div><dt>9+</dt><dd>years serving Utah</dd></div><div><dt>20+</dt><dd>years roofing experience</dd></div></dl>
</div></section>
<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">How we work</p><h2>Cost-effective roofing without cutting corners</h2></div><div class="pillars">{pil}</div></div></section>''' + cta()
    return {"path": "about", "title": "About RoofWise | Roofing Company in Salt Lake City, UT",
            "meta": "RoofWise is a licensed, insured Northern Utah roofing company: 20+ years of crew experience, itemized proposals and a 10-year workmanship warranty.",
            "body": body, "full_biz": True, "og": "drone-reroof-full-property",
            "schema": [crumbs_ld("about", trail), {"@type": "AboutPage", "@id": canon("about") + "#webpage", "url": canon("about"), "name": "About RoofWise", "about": {"@id": U + "/#business"}}]}


def contact():
    trail = [HOME, ("Contact", "contact")]
    body = phero(trail, "Call RoofWise or Schedule an Inspection", "Have a roof leak, missing shingles, storm damage concerns or a roofing project in mind? RoofWise serves Salt Lake City and Northern Utah.", "Contact", buttons=False) + f'''
<section class="sec"><div class="wrap split top">
<div class="reveal"><dl class="contact-list"><div><dt>Call RoofWise</dt><dd><a class="big" href="tel:{S["tel"]}">{S["phone"]}</a></dd></div>
<div><dt>Email RoofWise</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd></div>
<div><dt>Service area</dt><dd>{", ".join(COUNTIES[:-1])} and {COUNTIES[-1]}</dd></div></dl>
<p><a class="btn" href="@/{SCHED}">Schedule an inspection instead {ARROW}</a></p></div>
<div class="reveal">{contact_form()}</div></div></section>'''
    return {"path": "contact", "title": "Contact RoofWise | Salt Lake City Roofing Contractor",
            "meta": "Contact RoofWise at (435) 655-1246 or roofwisesaltlake@gmail.com about roof leaks, storm damage or a roofing project in Salt Lake City and Northern Utah.",
            "body": body, "full_biz": True,
            "schema": [crumbs_ld("contact", trail), {"@type": "ContactPage", "@id": canon("contact") + "#webpage", "url": canon("contact"), "name": "Contact RoofWise", "about": {"@id": U + "/#business"}}]}


def schedule():
    trail = [HOME, ("Schedule Inspection", SCHED)]
    opts = "".join(f'<label><input type="radio" name="property_type" value="{v}"{" checked" if i == 0 else ""}> {v}</label>' for i, v in enumerate(["My home", "Rental property", "Commercial property", "Other"]))
    sits = "".join(f'<label><input type="checkbox" name="situation" value="{html.unescape(s)}"> {s.rstrip(".")}</label>' for s, _, _ in NEXT)
    form = f'''<form class="form" method="post" action="">
<h3>Request a roof inspection</h3>
<fieldset class="radios"><legend>What type of property is this?</legend>{opts}</fieldset>
<fieldset class="radios col"><legend>What&rsquo;s going on? (choose any)</legend>{sits}</fieldset>
<label for="s-addr">Property address *<input id="s-addr" name="address" autocomplete="street-address" required></label>
<div class="row"><label for="s-name">Name *<input id="s-name" name="name" autocomplete="name" required></label><label for="s-phone">Phone *<input id="s-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="s-email">Email<input id="s-email" type="email" name="email" autocomplete="email"></label><label for="s-time">Preferred day or time<input id="s-time" name="preferred_time"></label></div>
<label for="s-notes">Anything else we should know?<textarea id="s-notes" name="notes"></textarea></label>
<button class="btn" type="submit">Request Inspection {ARROW}</button></form>'''
    body = phero(trail, "Schedule a Roof Inspection in Salt Lake City", "Let us take a look, explain what we find, and help you understand your options. Start with a professional roof evaluation and clear, no-pressure next steps.", "Roof inspection", buttons=False) + f'''
<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="label">What you get</p><h2>Let&rsquo;s get your roof checked out</h2>
{findings(["Professional roof evaluation", "Clear explanation of findings", "Insurance-related consultation when appropriate", "No-pressure next steps"], "")}
{notice(DISCLAIMER)}</div>
<div class="reveal">{form}</div></div></section>'''
    return {"path": SCHED, "title": "Schedule a Roof Inspection, Salt Lake City | RoofWise",
            "meta": "Request a RoofWise roof inspection in Salt Lake City or Northern Utah: a professional evaluation, a clear explanation of findings and no-pressure next steps.",
            "body": body, "full_biz": False, "schema": [crumbs_ld(SCHED, trail)]}


def notfound():
    body = f'''<section class="phero dim"><div class="ph-bg">{img("drone-reroof-hillside-home", "")}</div><div class="vf" aria-hidden="true"></div><div class="wrap ph-in"><div class="ph-text"><p class="label light">404</p><h1>Nothing to inspect here.</h1>
<p class="lede">That page isn&rsquo;t on the RoofWise site. Try the <a href="@/">home page</a>, <a href="@/roof-repair">roof repair</a> or <a href="@/{SCHED}">schedule an inspection</a>, or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div></div></section>'''
    return {"path": "404.html", "title": "Page Not Found | RoofWise", "meta": "This page isn't on the RoofWise site. Try the home page or roof repair, schedule an inspection, or call (435) 655-1246.",
            "body": body, "robots": "noindex, follow", "sitemap": False, "full_biz": False}


def make_pages():
    return [home(), replacement(), repair(), commercial(), gutters(), insurance(), service_area(), about(), contact(), schedule(), p_blog.page(), notfound()]
