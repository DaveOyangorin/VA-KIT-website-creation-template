"""Pages for the danielswildlife.com redesign: "Field notes".

Daniel works every job himself and documents it: raccoons in traps, chewed entry holes, attic droppings, gopher mounds in the snow. So
the site reads like his inspection notebook. The home page opens on a full-bleed photo of a raccoon he trapped, and the signature is the
clue matcher: tick what you're noticing (noises overhead, droppings, chewed wiring, mounds in the lawn, a smell that won't go away) and it
ranks the likely culprits, using only the signs his own service pages describe, with one of his job photos and a link to that page.
Forest green from the logo on field-guide paper, a marker-yellow highlight; Bitter, Karla, Courier Prime.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 18 URLs (www host, no trailing slash; /home kept on the site build) plus one new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta
STOP = re.compile(r"^(Services|Contact)$")


def blocks(key):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    s = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", s)
    s = s[s.find('role="main"'):]
    out, started = [], False
    for t, x in re.findall(r"(?s)<(h1|h2|h3|h4|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).replace(" ,", ",").replace(" .", ".").strip()
        if not x: continue
        if t == "h1" or (t == "h2" and not started): started = True; continue
        if not started: continue
        if t in ("h3", "h4") and STOP.match(x): break
        if x in ("Contact Today!", "Learn more...", "Call or request a quote today!"): continue
        out.append((t, x))
    return out


def render(b):
    res, ul = [], []
    def flush():
        if ul: res.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, x in b:
        if t == "li": ul.append(x); continue
        if t == "p" and "•" in x:
            head, *items = [i.strip() for i in x.split("•")]
            flush()
            if head: res.append(f"<p>{html.escape(head)}</p>")
            ul.extend(i for i in items if i); continue
        flush()
        res.append(f"<p>{html.escape(x)}</p>" if t == "p" else f"<h2>{html.escape(x)}</h2>")
    flush()
    return "\n".join(res)


# service pages: path key, label, h1 (live), keyword title, meta, photos [(name, alt)]
SVCS = [
    ("raccoons", "Raccoons", "Raccoon Removal in Cottonwood Heights &amp; Salt Lake | Daniel's", "Humane raccoon removal, trapping and exclusion in Cottonwood Heights and the Salt Lake Valley, plus cleanup and minor damage repair. Owner-operated, 24/7.",
     [("dw-raccoon", "A raccoon caught in a live trap by Daniel's Wildlife"), ("dw-raccoon-entry", "A raccoon entry hole torn under siding"), ("dw-raccoon-poop", "Raccoon droppings found in an attic")]),
    ("squirrels", "Squirrels", "Squirrel Removal &amp; Exclusion, Salt Lake Valley | Daniel's", "Squirrel removal, trapping and exclusion in the Salt Lake Valley: entry points sealed, nests and droppings cleaned up, wiring and fire risk stopped. 24/7.",
     [("dw-squirrel", "A squirrel on a roofline near an entry point"), ("dw-squirrel-entry", "A squirrel entry hole at a roof edge"), ("dw-trap", "A squirrel in a trap being removed")]),
    ("bats", "Bats", "Bat Removal &amp; Exclusion in Utah | Daniel's Wildlife &amp; Pest", "Humane bat exclusion in Northern Utah and the Salt Lake Valley, compliant with state rules and federal protections, plus guano cleanup and sanitation.",
     [("dw-bat", "Bat guano piled beneath an attic gable vent")]),
    ("birds", "Birds", "Bird Control &amp; Solar Panel Bird Exclusion | Daniel's", "Bird removal and exclusion in the Salt Lake Valley: solar panel cleanouts and sealing, pigeon control, custom bird netting, gutter and roof cleanup.",
     [("dw-birdnet", "Bird netting installed over a parking structure"), ("dw-solar", "Daniel working on a rooftop solar panel bird exclusion")]),
    ("skunks", "Skunks", "Skunk Removal &amp; Odor Control, Salt Lake Valley | Daniel's", "Humane skunk removal, trapping and exclusion in the Salt Lake Valley, plus odor control and deodorizing for crawlspaces, soil and foundations. Open 24/7.", []),
    ("snakes", "Snakes", "Snake Removal in Northern Utah &amp; Salt Lake | Daniel's", "Fast, legal, humane snake removal in Northern Utah, from garter snakes to rattlesnakes, plus deterrents and sealing around garages and crawlspaces.",
     [("dw-snake", "A snake found near a home's foundation")]),
    ("mice", "Mice", "Mouse Control &amp; Exclusion in the Salt Lake Valley | Daniel's", "Mouse control in the Salt Lake Valley: inspection, trapping and baiting, sealing with chew-resistant materials, and cleanup of droppings and insulation.",
     [("dw-mice", "A tamper-resistant rodent bait station")]),
    ("rats", "Rats", "Rat Control, Exclusion &amp; Sanitization, Utah | Daniel's", "Rat control in Northern Utah and the Salt Lake Valley: nests and burrows found, full seal-up with chew-resistant materials, and sanitization of droppings.",
     [("dw-rats", "A rodent bait station set beside a home's foundation")]),
    ("gophers", "Gophers", "Gopher Control &amp; Yard Protection, Salt Lake | Daniel's", "Gopher control in the Salt Lake Valley that targets active tunnel systems and feeding zones, to protect lawns, landscaping, irrigation and hardscape.",
     [("dw-gopher", "A fresh gopher mound in a snowy lawn")]),
    ("voles", "Voles", "Vole Control &amp; Lawn Protection, Salt Lake | Daniel's", "Vole control in the Salt Lake Valley: active tunnels, surface runways and nesting areas treated to protect lawns, garden beds and young trees year-round.",
     [("dw-vole", "Vole runways and damage across a lawn")]),
    ("insects", "Insects", "Insect &amp; Pest Control, Bed Bugs, Wasps | Daniel's Wildlife", "Insect control for homes and businesses in the Salt Lake Valley: ants, spiders, wasps and stinging insects, cockroaches and bed bugs, plus exclusion.",
     [("dw-wasp", "A wasp nest removed from an eave"), ("dw-spider", "A spider found during an inspection"), ("dw-ants", "Carpenter ants found during an inspection")]),
    ("termites", "Termites", "Termite Inspection &amp; Treatment, Salt Lake | Daniel's", "Termite inspections, targeted liquid treatments and long-term prevention for homes and commercial properties in the Salt Lake Valley and Northern Utah.",
     [("dw-termites", "Termites found in wood"), ("dw-termite-dmg", "Termite damage in wood framing")]),
    ("cleanup_sanitization", "Cleanup &amp; sanitization", "Wildlife Cleanup &amp; Attic Sanitization, Utah | Daniel's", "Attic and crawlspace cleanup and sanitization after wildlife and rodents in the Salt Lake Valley: droppings, nesting material, insulation and odors.",
     [("dw-attic", "Daniel sanitizing an attic after wildlife activity"), ("dw-crawl-before", "A crawlspace before cleanup"), ("dw-crawl-after", "The same crawlspace after cleanup and restoration")]),
    ("dead_animal_removal", "Dead animal removal", "Dead Animal Removal in Cottonwood Heights &amp; Salt Lake", "Dead animal removal in Cottonwood Heights and the Salt Lake Valley: location, safe removal, sanitation and odor elimination for a healthier home.",
     [("dw-cleanup", "Contaminated insulation removed during a cleanup")]),
]

# the clue matcher: signs from their own pages -> animals
CLUES = [("noise", "Noises in the attic or walls"), ("insul", "Torn insulation or damaged ductwork"), ("wire", "Chewed wiring"), ("drop", "Droppings in the attic or crawlspace"),
         ("odor", "A strong odor that won&rsquo;t go away"), ("roof", "Damage at the roofline, soffits or vents"), ("solar", "Nests under solar panels or clogged gutters"),
         ("stain", "Staining around a small gap high on the house"), ("mound", "Mounds of soil in the lawn"), ("runway", "Surface runways or dead patches in the grass"),
         ("burrow", "Burrows under a deck, shed, slab or foundation"), ("snake", "A snake by the garage, rocks or debris"), ("sting", "Wasps or stinging insects around the eaves"),
         ("wood", "Damaged or hollow-sounding wood")]
MATCH = {"raccoons": ["noise", "insul", "wire", "drop", "odor", "roof"], "squirrels": ["noise", "insul", "wire", "drop", "roof"], "bats": ["drop", "odor", "stain"],
         "birds": ["noise", "drop", "roof", "solar"], "skunks": ["odor", "burrow"], "snakes": ["snake"], "mice": ["insul", "wire", "drop"], "rats": ["insul", "wire", "drop", "burrow"],
         "gophers": ["mound"], "voles": ["runway"], "insects": ["sting"], "termites": ["wood"], "dead_animal_removal": ["odor"]}
WHY = {"raccoons": "Raccoon activity often results in torn insulation, damaged ductwork, compromised wiring, and contamination from droppings and urine, with strong odors and noise.",
       "squirrels": "Squirrel activity commonly results in damaged rooflines, compromised soffits, torn insulation, and chewed electrical wiring.",
       "bats": "Bat activity inside structures can lead to guano accumulation, urine saturation, insulation contamination, and persistent odors; inspections look for staining patterns at entry points.",
       "birds": "Birds in attics, soffits, vents or under solar panels leave droppings and nesting material, and can clog gutters completely.",
       "skunks": "Skunk problems often involve odor contamination in crawlspaces, soil and foundation walls, and burrows beneath structures.",
       "snakes": "Rodent activity, bird nesting, debris piles, rock features, and shaded structures can all increase snake activity.",
       "mice": "Mouse activity often results in chewed wiring, damaged insulation, and contamination from droppings and urine.",
       "rats": "Rats chew through wiring and insulation and commonly nest under concrete slabs, sheds, decks, crawlspaces, and within walls or attics.",
       "gophers": "What may begin as isolated mounds can quickly develop into widespread underground networks across a property.",
       "voles": "Voles create tunnels just beneath the soil surface, leading to thinning grass, dead patches, and visible surface runways.",
       "insects": "Wasp and stinging insect nests are often in eaves, rooflines, second stories, attics, walls, and crawlspaces.",
       "termites": "Termites can cause extensive structural damage long before any visible signs appear, so early inspection matters.",
       "dead_animal_removal": "A deceased animal in or around a building quickly leads to strong odors, insect activity, and the spread of bacteria."}


def matcher():
    pics = {k: (ph[0][0] if ph else "dw-raccoon-entry") for k, l, t, m, ph in SVCS}
    labels = {k: l for k, l, t, m, ph in SVCS}
    imgs = "".join(f'<template data-img="{k}">{img(pics[k], labels[k].replace("&amp;", "and") + " job photo")}</template>' for k in MATCH)
    data = {"match": MATCH, "why": WHY, "label": labels, "href": {k: "@/" + k.replace("_", "-") + "/" for k in MATCH}}
    boxes = "".join(f'<label class="clue"><input type="checkbox" value="{k}"><span>{t}</span></label>' for k, t in CLUES)
    return f'''<div class="cm" data-cm>
<div class="cm-l"><p class="note">Field notes &middot; tick what you&rsquo;ve noticed</p><div class="clues">{boxes}</div><button type="button" class="tlink cm-reset" data-cm-reset>Clear</button></div>
<div class="cm-r" aria-live="polite"><div class="cm-empty" data-cm-empty><p class="note">Suspect list</p><p>Tick one or more signs and the likely culprits show up here, ranked by how many of your signs Daniel&rsquo;s own service pages describe.</p></div><ol class="cm-list" data-cm-list></ol></div>
{imgs}<script type="application/json" data-cm-data>{json.dumps(data)}</script></div>'''


FAQ = [("Who will come out to my property?", "<p>Daniel. He is the owner and the technician on every job, so you are not dealing with rotating technicians or sales-driven service plans.</p>"),
       ("Are you licensed and insured?", "<p>Yes. Daniel&rsquo;s Wildlife &amp; Pest is fully licensed and insured, and all work is performed in accordance with applicable state and local requirements.</p>"),
       ("Do you work after hours?", "<p>Yes. We&rsquo;re open 24/7. Call or text (801) 783-9638.</p>"),
       ("Do you clean up after the animals are gone?", "<p>Yes. Cleanup, sanitation and minor damage repair are available, because droppings, nesting material and odors have to be addressed for a job to be truly complete.</p>")]


def home():
    body = f'''
<section class="d-hero"><div class="dh-img" data-parallax="0.08">{img("dw-hero", "A raccoon caught in a live trap on a lawn by Daniel's Wildlife & Pest", priority=True)}</div>
<div class="wrap dh-in"><div class="dh-txt"><p class="note">Case file &middot; Cottonwood Heights &middot; Open 24/7</p>
<h1>Pest control &amp; wildlife removal in Cottonwood Heights, <em>done by the owner.</em></h1>
<p class="lede">Daniel&rsquo;s Wildlife &amp; Pest is an owner-operated pest control and wildlife removal company in Cottonwood Heights, serving the Salt Lake Valley and Northern Utah. Raccoons, squirrels, bats, birds, rodents, insects and more: humane removal, exclusion and cleanup, done right the first time.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18017839638">{PHONE} Call or text (801) 783-9638</a><a class="btn ghost" href="#clues">What&rsquo;s in my attic? {ARROW}</a></div></div></div>
<div class="dh-strip"><div class="wrap"><span><b>8+</b> years hands-on</span><span><b>1</b> technician: the owner</span><span><b>14</b> animals &amp; services</span><span><b>24/7</b> call or text</span></div></div></section>

<section class="sec d-clues" id="clues"><div class="wrap">
<div class="d-head split-h reveal"><div><p class="label">The clue matcher</p><h2>What&rsquo;s making that noise? <em>Check the signs.</em></h2></div><p class="lede">Every job starts with an inspection. Start your own: tick what you&rsquo;re seeing, hearing or smelling.</p></div>
{matcher()}
</div></section>

<section class="sec d-files"><div class="wrap">
<div class="d-head split-h reveal"><div><p class="label">From the job files</p><h2>Real calls. <em>Real photos.</em></h2></div><a class="tlink" href="@/services/">All services {ARROW}</a></div>
<div class="board">{"".join(f'<a class="pin reveal" href="@/{h}"><figure>{img(n, a)}</figure><span class="note">{c}</span></a>' for n, a, c, h in (("dw-raccoon", "A raccoon in a live trap", "Raccoon, trapped", "raccoons/"), ("dw-raccoon-entry", "A torn raccoon entry hole under siding", "Entry point: siding", "raccoons/"), ("dw-squirrel-entry", "A squirrel entry hole at a roof edge", "Squirrel entry: roof edge", "squirrels/"), ("dw-bat", "Bat guano below an attic vent", "Bat guano: gable vent", "bats/"), ("dw-gopher", "A gopher mound in snow", "Gopher mound in January snow", "gophers/"), ("dw-crawl-after", "A cleaned crawlspace", "Crawlspace, after cleanup", "cleanup-sanitization/")))}</div>
</div></section>

<section class="d-owner"><div class="wrap d-owner-in">
<figure class="reveal">{img("dw-attic", "Daniel sanitizing an attic after wildlife activity")}</figure>
<div class="reveal"><p class="label">Why I started Daniel&rsquo;s</p><h2>No rotating technicians. <em>No shortcuts.</em></h2>
<p>Before starting my own company, I helped build and scale established pest and wildlife operations. As those companies expanded, quality declined: services became rushed, problems were patched instead of properly solved, and customers were left dealing with repeat issues.</p>
<p>Daniel&rsquo;s Wildlife and Pest was created to return to high-standard, detail-driven work where accountability and results come first. When you hire me, you are working directly with the person responsible for the outcome of the job.</p>
<a class="tlink" href="@/about/">About Daniel&rsquo;s {ARROW}</a></div></div></section>

<section class="sec d-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight from <em>the owner.</em></h2>
<a class="post-card d-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What CDC and the National Park Service say about hantavirus, and the safe way to clean up a light mouse problem.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Pest Control Cottonwood Heights, UT | Daniel's Wildlife",
            "meta": "Daniel's Wildlife & Pest: owner-operated pest control and wildlife removal in Cottonwood Heights and the Salt Lake Valley. Licensed, insured, open 24/7.",
            "body": body, "body_class": "is-home", "og": "dw-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def svc_cards():
    return '<div class="svc-grid">' + "".join(f'<a class="svc-c" href="@/{k.replace("_", "-")}/">{img(ph[0][0], l.replace("&amp;", "and")) if ph else "<span class=\"svc-blank\"></span>"}<b>{l}</b></a>' for k, l, t, m, ph in SVCS) + "</div>"


def make_pages():
    out = [home()]
    out.append(dict(home(), path="home/", canonical=U, site_only=True, sitemap=False))
    for k, l, t, m, ph in SVCS:
        path = k.replace("_", "-") + "/"
        h1 = html.escape(EXT[k]["title"].split(" | ")[0])
        b = blocks(k)
        live_h1 = re.search(r"(?s)<h1[^>]*>(.*?)</h1>", open(os.path.join(HERE, "src", "pages", k + ".html"), encoding="utf-8").read())
        if not live_h1:
            live_h1 = re.search(r"(?s)<h2[^>]*>(.*?)</h2>", open(os.path.join(HERE, "src", "pages", k + ".html"), encoding="utf-8").read().split('role="main"', 1)[-1])
        if live_h1: h1 = html.escape(re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", live_h1.group(1)))).strip())
        body = render(b)
        if len(ph) > 1:
            body += '<div class="pgal">' + "".join(img(n, a) for n, a in ph[1:]) + "</div>"
        out.append(K.page(path, l, h1, "Northern Utah &amp; the Salt Lake Valley", "Daniel&rsquo;s Wildlife &amp; Pest", t, m, body, image=ph[0][0] if ph else None, alt=ph[0][1] if ph else "",
                          crumbs=[("Services", "services/")], canonical=EXT[k]["canon"], schema=[K.svc_schema(path, html.unescape(l), "Cottonwood Heights, the Salt Lake Valley and Northern Utah")]))
    out.append(K.page("services/", "Services", "Wildlife &amp; pest services", "Fourteen animals and services, one owner-operator.", "Services", "Wildlife Removal &amp; Pest Control Services | Daniel's Wildlife",
                      "Daniel's Wildlife & Pest services: raccoons, squirrels, bats, birds, skunks, snakes, rodents, gophers, voles, insects, termites, cleanup and dead animals.",
                      '<p class="answer">Humane removal, exclusion, treatment and cleanup across Northern Utah and the Salt Lake Valley. Every service begins with a thorough inspection.</p>' + svc_cards(),
                      image="dw-raccoon-entry", alt="A raccoon entry hole under siding", canonical=EXT["services"]["canon"]))
    out.append(K.page("about/", "About", "About Daniel&rsquo;s Wildlife &amp; Pest", "Owner-operated. Licensed. Insured.", "About", "About Daniel's Wildlife &amp; Pest | Owner-Operated, Utah",
                      "Daniel's Wildlife & Pest is owner-operated: over eight years and thousands of pest and wildlife cases, licensed and insured, with an IPM approach. 24/7.",
                      render(blocks("about")) + '<div class="pgal">' + img("dw-birdnet", "Bird netting installed by Daniel's") + img("dw-solar", "Solar panel bird exclusion work") + img("dw-crawl-after", "A crawlspace after cleanup") + "</div>",
                      image="dw-attic", alt="Daniel sanitizing an attic", canonical=EXT["about"]["canon"]))
    con = '''<p class="answer">Call or text any time. Daniel&rsquo;s is open 24/7, and you&rsquo;ll talk to the owner.</p>
<dl class="info"><div><dt>Call or text</dt><dd><a href="tel:+18017839638">(801) 783-9638</a></dd></div><div><dt>Hours</dt><dd>Open 24/7</dd></div>
<div><dt>Based in</dt><dd><address>6870 S Village Green Rd<br>Cottonwood Heights, UT 84121</address></dd></div><div><dt>Serving</dt><dd>Northern Utah &amp; the Salt Lake Valley</dd></div></dl>'''
    out.append(K.page("contact/", "Contact", "Contact Daniel&rsquo;s Wildlife &amp; Pest", "Call, text or request service.", "Contact", "Contact Daniel's Wildlife &amp; Pest | Cottonwood Heights, UT",
                      "Contact Daniel's Wildlife & Pest in Cottonwood Heights: call or text (801) 783-9638, open 24/7, for wildlife removal and pest control across the valley.",
                      con, canonical=EXT["contact"]["canon"], form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Raccoons", "raccoons/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call or text (801) 783-9638.", " Open 24/7.")) for x in out]
