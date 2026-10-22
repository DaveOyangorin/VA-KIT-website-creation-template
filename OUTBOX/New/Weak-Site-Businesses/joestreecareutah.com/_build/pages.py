"""Pages for the joestreecareutah.com redesign: "Heartwood".

A tree crew's best argument is the job site: a crane lifting a log under the Wasatch, a grinder chewing a stump below grade, a bare yard
turned to sod. Joe's has those photos of their own work, so the home page opens full-bleed on their stump grinder at work, and the signature
pairs a drag-to-compare before/after of their own sod job with a tree-care calendar built from their FAQ (dormant oil in April and early
May, fertilizer April through September). Conifer green, heartwood orange, Zilla Slab.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 12 URLs (no trailing slash); /home is the live home URL (site only, since the preview uses home/)."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

FAQ = [("Are you licensed and insured?", "<p>Yes, fully licensed and insured for your peace of mind.</p>"),
       ("How can I get the most work done at the best price?", "<p>Bundle services. When we can handle everything in one visit with all the right equipment on site, it saves time and lowers your overall cost.</p>"),
       ("When is the best time to fertilize trees?", "<p>Fertilizer is most effective from April through September, but earlier in the season (spring and early summer) tends to get the best results.</p>"),
       ("When is the best time for dormant oil sprays?", "<p>Dormant oil sprays work best in April and early May, right before buds open and insects start moving in.</p>"),
       ("Is your machinery yard friendly?", "<p>Yes, we use yard-safe machinery. Some circumstances require mats and protective barriers for safety.</p>"),
       ("What forms of payment do you take?", "<p>Venmo, cash, check, credit card and Apple Pay.</p>")]
WHY = ["We grind deep enough to stop regrowth", "We don&rsquo;t damage your yard or surrounding areas", "We clean up everything before we leave", "Fully licensed, insured and easy to work with"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def svc_text(k):
    t = EXT[k]["text"]; a = t.find("Email * Send"); b = t.find("Why People Call Us"); b = b if b > 0 else t.find("What do your neighbors say")
    return t[a + 12:b].strip()


SERV = [("tree-trimming/", "tree_trimming", "Tree trimming", "From small shaping jobs to full canopy management, we trim with purpose: healthy trees and a sharp yard.", "jt-cut"),
        ("tree-removal/", "tree_removal", "Tree removal", "Removals of all sizes, fast, clean and without damage to your property.", "jt-crane"),
        ("stump-grinding/", "stump_grinding", "Stump grinding", "Ground clean and below grade with pro-grade equipment, so your yard is ready for what&rsquo;s next.", "jt-grinder"),
        ("plant-health-care/", "plant_health_care", "Plant health care", "Dormant oil sprays, slow-release fertilizer and systemic care to prevent disease and boost growth.", "jt-log"),
        ("hoa-service-plans/", "hoa_service_plans", "HOA service plans", "Custom care plans for HOAs and communities: maintained, clean and up to code.", "jt-truck"),
        ("small-landscaping/", "small_landscaping", "Small landscaping", "Weed spraying, grading, tree planting, bracing and cabling, beds, rock and sod.", "jt-mulch")]


def compare(a, b, alt_a, alt_b, i=0):
    return f'''<figure class="ba" data-ba><div class="ba-frame" style="--pos:50%">
<div class="ba-after">{img(b, alt_b, lazy=(i != 0))}</div><div class="ba-before">{img(a, alt_a, lazy=(i != 0))}</div>
<span class="ba-tag b">Before</span><span class="ba-tag a">After</span>
<input type="range" min="0" max="100" value="50" class="ba-range" aria-label="Drag to compare before and after" data-ba-range><span class="ba-handle" aria-hidden="true"><i></i></span></div></figure>'''


def calendar():
    def row(name, months, note, cls):
        cells = "".join(f'<span class="c{" on" if m in months else ""}{" half" if m in months and months[m] == "h" else ""}" title="{MONTHS[m]}"></span>' for m in range(12))
        return f'<div class="cal-row {cls}"><b>{name}</b><div class="cells">{cells}</div><small>{note}</small></div>'
    return f'''<div class="cal"><div class="cal-row cal-head"><b></b><div class="cells">{"".join(f"<span>{m[0]}</span>" for m in MONTHS)}</div><small></small></div>
{row("Dormant oil sprays", {3: "f", 4: "h"}, "April and early May, right before buds open and insects start moving in.", "r-oil")}
{row("Fertilizer", {3: "f", 4: "f", 5: "f", 6: "h", 7: "h", 8: "h"}, "April through September; spring and early summer get the best results.", "r-fert")}</div>'''


def home():
    tiles = "".join(f'<a class="sv reveal" href="@/{p}"><figure>{img(im, "")}</figure><div><b>{n}</b><p>{d}</p><em>Learn more {ARROW}</em></div></a>' for p, k, n, d, im in SERV)
    body = f'''
<section class="j-hero"><div class="jh-img" data-parallax="0.08">{img("jt-grind", "A Joe's Tree Care stump grinder working on a stump in a Utah yard with mountains behind", priority=True)}</div>
<div class="wrap jh-in"><div class="jh-txt"><p class="label">Salt Lake, Utah &amp; Wasatch counties &middot; Family-run since 2018</p>
<h1>Tree service in Salt Lake City, <em>root to tip.</em></h1>
<p class="lede">Trimming, removal and stump grinding with commercial-grade equipment, plus plant health care and small landscaping. Licensed, insured, locally owned, with same-week availability.</p>
<div class="btn-row"><a class="btn accent" href="@/contact-us/">Get a free quote {ARROW}</a><a class="btn ghost" href="tel:+18012896689">{PHONE} (801) 289-6689</a></div></div>
<ul class="jh-stats"><li><b>2018</b><span>family-run since</span></li><li><b>Same week</b><span>availability</span></li><li><b>3</b><span>counties served</span></li></ul></div></section>

<section class="sec j-svc"><div class="wrap">
<div class="j-head split-h reveal"><div><p class="label">Our services</p><h2>Six ways we take care <em>of your trees.</em></h2></div><a class="tlink" href="@/services/">All services {ARROW}</a></div>
<div class="svc6">{tiles}</div></div></section>

<section class="sec j-sig" id="before-after"><div class="wrap j-sig-in">
<div class="reveal"><p class="label">Before &amp; after</p><h2>Bare dirt. <em>Fresh sod.</em></h2><p class="lede">A real Joe&rsquo;s job: a torn-up side yard, graded and finished with fresh sod. Drag the handle.</p>
<ul class="ticks">{"".join(f"<li>{w}</li>" for w in WHY)}</ul><a class="tlink" href="@/our-work/">See our work {ARROW}</a></div>
<div class="reveal">{compare("jt-sod-before", "jt-sod-after", "A side yard before: bare dirt, debris and a new concrete pad", "The same side yard after: graded and finished with fresh green sod")}</div>
</div></section>

<section class="sec j-cal"><div class="wrap">
<div class="j-head split-h reveal"><div><p class="label">Plant health care</p><h2>Time it right. <em>Trees remember.</em></h2></div><a class="tlink" href="@/plant-health-care/">Plant health care {ARROW}</a></div>
<div class="reveal">{calendar()}</div></div></section>

<section class="j-band"><div class="band-img" data-parallax="0.1">{img("jt-crane", "A Joe's Tree Care crane lifting a tree section beside a truck, with the snowy Wasatch behind")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our story</p><p>What started as a small, family-run operation in 2018 has grown on honest work, top-notch equipment, and a deep respect for every property we service.</p></blockquote></div></section>

<section class="sec j-crew"><div class="wrap j-crew-in">
<figure class="reveal">{img("jt-crew", "Two Joe's Tree Care crew members holding chainsaws on a driveway")}</figure>
<div class="reveal"><p class="label">Dependable, start to finish</p><h2>More than <em>tree guys.</em></h2><p>We&rsquo;re your go-to team for safe, clean, reliable outdoor work: stump grinding, trimming, removals or custom HOA plans. We use the right tools, show up when we say we will, and treat your yard like it&rsquo;s our own. Simple as that.</p>
<div class="minis">{img("jt-stump", "A crew member beside a large stump being cut down")}{img("jt-truck", "A crane truck loading a log section")}</div></div>
</div></section>

<section class="sec j-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card j-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>USU Extension on how deep, how often and how to water trees in Utah&rsquo;s dry summers.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Tree Service Salt Lake City | Joe's Tree Care &amp; Stumps",
            "meta": "Family-run tree service in Salt Lake, Utah and Wasatch counties: tree trimming, removal and stump grinding. Licensed and insured, same-week availability.",
            "body": body, "body_class": "is-home", "og": "jt-grind", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    h = home(); out.append(dict(h, path="home/", canonical=U, site_only=True, sitemap=False))
    sv = '<p class="answer">Your yard is more than just space; it&rsquo;s part of your home. From precision stump grinding and tree trimming to landscaping and maintenance, we bring clean, efficient work with long-lasting results.</p><div class="cats">' + \
         "".join(f'<a class="cat" href="@/{p}"><b>{n}</b><span>{d}</span><em>Learn more {ARROW}</em></a>' for p, k, n, d, im in SERV) + "</div><h2>Why people call us</h2><ul class=\"ticks\">" + "".join(f"<li>{w}</li>" for w in WHY) + "</ul>"
    out.append(K.page("services/", "Services", "Our Tree Services", "Trimming, removal, stump grinding and more.", "Services", "Tree Services in Salt Lake &amp; Utah County | Joe's Tree Care",
                      "Joe's Tree Care services: tree trimming, tree removal, stump grinding, plant health care, HOA service plans and small landscaping across northern Utah.",
                      sv, image="jt-crane", alt="A crane lifting a tree section", canonical=canon("services/"), faqs=FAQ[:2]))
    hoa = '<p class="answer">We build custom care plans for HOAs and communities, keeping grounds maintained, clean and up to code.</p><ul class="ticks"><li><strong>Routine maintenance:</strong> trimmed, tidy and always in season</li><li><strong>Custom service schedules:</strong> weekly, monthly or as needed</li><li><strong>Adherence to HOA guidelines:</strong> full compliance with your HOA&rsquo;s standards</li></ul><p>Bundling services into one visit saves time and lowers your overall cost.</p>'
    titles = {"tree_trimming": ("Tree Trimming in Salt Lake &amp; Utah County | Joe's Tree Care", "Tree trimming from Joe's Tree Care: shaping, dead-limb removal and canopy management that keeps trees healthy and your yard sharp. Licensed and insured."),
              "tree_removal": ("Tree Removal in Salt Lake &amp; Utah County | Joe's Tree Care", "Safe tree removal for dead, leaning or overgrown trees of all sizes, with full debris cleanup, from licensed and insured Joe's Tree Care in northern Utah."),
              "stump_grinding": ("Stump Grinding in Salt Lake &amp; Utah County | Joe's Tree Care", "Stump grinding below grade with pro-grade grinders, deep enough to stop regrowth, with full cleanup. Same-week availability from Joe's Tree Care."),
              "plant_health_care": ("Tree Health Care, Dormant Oil &amp; Fertilizer | Joe's Tree Care", "Plant health care from Joe's Tree Care: dormant oil sprays in spring, slow-release fertilizer and systemic care to protect Utah trees from pests and disease."),
              "hoa_service_plans": ("HOA Tree &amp; Grounds Service Plans, Utah | Joe's Tree Care", "Custom HOA service plans from Joe's Tree Care: routine tree and grounds maintenance on weekly, monthly or as-needed schedules, compliant with HOA guidelines."),
              "small_landscaping": ("Small Landscaping, Beds &amp; Sod in Utah | Joe's Tree Care", "Small landscaping from Joe's Tree Care: garden beds, rock, mulch, grading, sod, tree planting, bracing and cabling, and seasonal cleanups in northern Utah.")}
    for p, k, n, d, im in SERV:
        if k == "hoa_service_plans":
            body = hoa
        else:
            t = svc_text(k)
            sents = re.split(r"(?<=[.!?])\s+", t)
            body = f'<p class="answer">{d}</p>' + "".join(f"<p>{html.escape(' '.join(sents[j:j + 3]))}</p>" for j in range(0, len(sents), 3))
            if k == "small_landscaping":
                body += "<h2>Before &amp; after</h2>" + compare("jt-dig-before", "jt-dig-after", "A side yard being regraded beside a new concrete pad", "The same yard finished with sod", 1)
        body += '<h2>Why people call us</h2><ul class="ticks">' + "".join(f"<li>{w}</li>" for w in WHY) + "</ul>"
        ti, me = titles[k]
        out.append(K.page(p, n, n, d, "Services", ti, me, body, image=im, alt=n, crumbs=[("Services", "services/")], canonical=canon(p), faqs=FAQ[:3] if k == "plant_health_care" else FAQ[:2],
                          schema=K.svc_schema(p, n, "Salt Lake City, UT")))
    ab = '''<p class="answer">What started as a small, family-run operation in 2018 has grown into a trusted name in tree care across northern Utah.</p>
<p>Joe&rsquo;s Tree Care was founded with one goal in mind: to deliver reliable, affordable and safe tree services backed by real expertise. From residential backyards to commercial properties and HOA landscapes, we&rsquo;ve built our reputation through honest work, top-notch equipment and a deep respect for every property we service.</p>
<p>Over the years, we&rsquo;ve expanded our services while staying true to our values: integrity, precision and putting the customer first.</p>
<ul class="ticks"><li>100% locally owned and operated</li><li>Licensed and insured</li><li>Serving Utah since 2018</li><li>Commercial-grade equipment</li></ul>'''
    out.append(K.page("about-us/", "About", "About Joe's Tree Care", "Built on trust. Backed by experience.", "About", "About Joe's Tree Care | Family-Run Tree Service Since 2018",
                      "Joe's Tree Care started as a family-run operation in 2018 and grew on honest work, pro-grade equipment and respect for every property in northern Utah.",
                      ab, image="jt-crew", alt="The Joe's Tree Care crew", canonical=canon("about-us/")))
    wk = '<p class="answer">Real results from real jobs.</p><div class="pgal">' + "".join(f"<figure>{img(n, a)}<figcaption>{c}</figcaption></figure>" for n, a, c in (
        ("jt-crane", "A crane lifting a tree section under the Wasatch", "Crane-assisted removal"), ("jt-grinder", "A stump grinder at work", "Stump grinding"), ("jt-log", "A large log section in a yard", "Removal cleanup"),
        ("jt-mulch", "A pile of mulch from a job", "Mulch from the grind"), ("jt-cut", "A cut stump", "Cut below grade"), ("jt-stump", "A large stump being cut", "Big stump, big saw"))) + "</div>" + \
         "<h2>Before &amp; after</h2>" + compare("jt-sod-before", "jt-sod-after", "A side yard before", "The same side yard after, with sod", 1) + compare("jt-dig-before", "jt-dig-after", "A yard being regraded", "The same yard finished", 1)
    out.append(K.page("our-work/", "Our work", "Our Work", "Real results from real jobs.", "Our work", "Our Work: Tree Removal &amp; Landscaping | Joe's Tree Care, Utah",
                      "See real Joe's Tree Care jobs: crane-assisted tree removal, stump grinding, cleanup and before-and-after landscaping across Salt Lake and Utah County.",
                      wk, image="jt-grinder", alt="A stump grinder at work", canonical=canon("our-work/")))
    con = '''<p class="answer">Get a free quote today. Bundle services into one visit to save.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18012896689">(801) 289-6689</a></dd></div><div><dt>Service area</dt><dd>Salt Lake, Utah and Wasatch counties</dd></div>
<div><dt>Payment</dt><dd>Venmo, cash, check, credit card, Apple Pay</dd></div><div><dt>Availability</dt><dd>Same-week</dd></div></dl>'''
    out.append(K.page("contact-us/", "Contact", "Contact Joe's Tree Care", "Free quotes. Same-week availability.", "Contact", "Contact Joe's Tree Care | Free Tree Service Quote, Utah",
                      "Contact Joe's Tree Care at (801) 289-6689 for a free quote on tree trimming, removal or stump grinding in Salt Lake, Utah or Wasatch County. Same week.",
                      con, canonical=canon("contact-us/"), form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Our work", "our-work/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free quotes.", " Call (801) 289-6689.")) for x in out]
