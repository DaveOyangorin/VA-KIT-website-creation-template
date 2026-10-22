"""Pages for the actionyardcare.com redesign: "Lineup card".

Action's logo is varsity block lettering over a row of crew silhouettes, and their photos show the crew in hi-vis on real jobs. So the
site dresses like a team: black and safety lime, varsity numerals, a full-bleed photo of a crew member laying sprinkler line. The live site
is four pages and a list, so the signature turns that list into something useful: the lineup card. Pick your services from their three
groups (landscaping, maintenance, sprinklers) and the card fills in like a coach's lineup, then writes a ready-to-send quote request
you can copy or email. Graduate, Barlow Condensed, Barlow.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 4 URLs (www, no trailing slash; /home kept on the site build) plus one new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

GROUPS = [("landscaping", "Landscaping", "New landscapes and renovations, built by the crew.", ["Sod", "Mulch / rocks", "Flagstone", "Planting", "Edging", "New landscaping &amp; renovation"]),
          ("maintenance", "Maintenance", "Weekly care and seasonal work, all year.", ["Weekly lawn mowing with string trimming &amp; edging", "Yard clean ups", "Tree / bush trimming", "Leaf clean up", "Snow removal", "Aeration",
                                                                                     "Fertilizing", "Lawn treatment programs", "Flower bed treatment programs", "Landscape pest treatments", "Weed management"]),
          ("sprinklers", "Sprinklers", "From spring start up to fall shut down.", ["Sprinkler start up &amp; shut down", "New sprinkler system installation", "Sprinkler system check ups", "Sprinkler repair"])]


def lineup():
    cols = "".join(f'''<div class="lu-g"><p class="lu-gh"><span class="varsity">{i + 1:02d}</span>{t}</p><div class="lu-chips">{"".join(f'<button type="button" class="lu-chip" aria-pressed="false" data-s="{html.escape(html.unescape(s))}">{s}</button>' for s in items)}</div></div>'''
                   for i, (k, t, d, items) in enumerate(GROUPS))
    return f'''<div class="lu" data-lu>
<div class="lu-pick">{cols}</div>
<div class="lu-card"><div class="lu-top"><span class="varsity">Action</span><span>Lineup card</span></div>
<ol class="lu-list" data-lu-list aria-live="polite"><li class="lu-empty">Tap services to add them to your lineup.</li></ol>
<label class="lu-l">Your street or neighborhood (optional)<input type="text" data-lu-where placeholder="e.g. near 6400 S in Murray"></label>
<div class="lu-msg"><p class="lu-ml">Your quote request</p><textarea data-lu-msg rows="5" readonly aria-label="Quote request text"></textarea></div>
<div class="lu-act"><button type="button" class="btn accent" data-lu-copy>Copy request</button><a class="btn ghost" data-lu-mail href="mailto:{EMAIL}">Email it</a></div>
<p class="lu-fine">Nothing is sent from this page. Copy the text into a text or email to {EMAIL}, or call 801-244-4035.</p></div>
</div>'''


FAQ = [("What areas do you serve?", "<p>Murray and the Salt Lake Valley.</p>"),
       ("Are you licensed and insured?", "<p>Yes. We are a group of licensed &amp; insured professionals with decades of experience.</p>"),
       ("Do you handle sprinklers too?", "<p>Yes: sprinkler start up and shut down, new system installation, system check ups and repair.</p>"),
       ("Do you do snow removal?", "<p>Yes. Snow removal is part of our maintenance services, along with mowing, clean ups, trimming, aeration and fertilizing.</p>")]


CAL_ROWS = [("Mowing", "March &ndash; November", "Mow at about 3 inches; never cut more than a third of the blade.", "Weekly lawn mowing with string trimming &amp; edging"),
            ("Irrigation", "April &ndash; October", "Water in the early morning, &frac12; to 1 inch per irrigation.", "Sprinkler start up in spring, shut down in fall, check ups and repair"),
            ("Aeration", "March &ndash; May &middot; Sept &ndash; Oct", "Aerate to improve water infiltration and reduce compaction and thatch.", "Aeration"),
            ("Fertilizing", "April &middot; June &middot; October", "Typical home lawns need only 2&ndash;3 lbs of nitrogen per 1,000 sq ft a year.", "Fertilizing and lawn treatment programs"),
            ("Seeding", "Sept &ndash; Oct (best) &middot; April &ndash; May", "Fall is the best window for seeding and overseeding.", "Sod and new landscaping &amp; renovation")]


def home():
    body = f'''
<section class="a-hero"><div class="ah-img" data-parallax="0.08">{img("ay-trench", "An Action Lawn & Yardcare crew member laying white sprinkler pipe in a fresh trench", priority=True)}</div>
<div class="wrap ah-in"><div class="ah-txt"><p class="label">Murray &middot; Salt Lake Valley &middot; Licensed &amp; insured</p>
<h1><span class="varsity">Landscaping</span> in Murray, <em>lawns &amp; sprinklers too.</em></h1>
<p class="lede">Action Lawn &amp; Yardcare is a landscaping company in Murray: experienced, licensed and insured landscape professionals serving the Salt Lake Valley. New landscapes, weekly lawn care, clean ups, snow removal and sprinklers, from one crew.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18012444035">{PHONE} Call 801-244-4035</a><a class="btn ghost" href="#lineup">Build your lineup {ARROW}</a></div></div></div>
<div class="ah-strip"><div class="wrap">{"".join(f'<span><b class="varsity">{len(items)}</b>{t.lower()} services</span>' for k, t, d, items in GROUPS)}<span><b class="varsity">1</b>crew, all seasons</span></div></div></section>

<section class="sec a-lineup" id="lineup"><div class="wrap">
<div class="a-head split-h reveal"><div><p class="label">The lineup card</p><h2>Pick your plays. <em>We&rsquo;ll bring the crew.</em></h2></div><p class="lede">Tap the services you need. Your lineup card writes the quote request for you.</p></div>
{lineup()}
</div></section>

<section class="sec a-cal"><div class="wrap">
<div class="a-head split-h reveal"><div><p class="label">The northern Utah yard calendar</p><h2>When the work <em>should happen.</em></h2></div><p class="lede">Timing from USU Extension&rsquo;s <em>Basic Turfgrass Care</em> for the northern region, and the Action services that line up with it.</p></div>
<div class="cal">{"".join(f'<div class="cr reveal"><b>{a}</b><span class="cr-w">{w}</span><p>{t}</p><em>Action: {s}</em></div>' for a, w, t, s in CAL_ROWS)}</div>
<p class="small">Source: Kelly Kopp and Paul Johnson, USU Extension, Basic Turfgrass Care (2011), northern Utah region.</p>
</div></section>

<section class="sec a-groups"><div class="wrap">
<div class="a-head reveal"><p class="label">What we do</p><h2>Three teams. <em>One crew.</em></h2></div>
<div class="grp">{"".join(f'<div class="gc reveal"><span class="varsity gc-n">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p><ul>{"".join(f"<li>{s}</li>" for s in items)}</ul></div>' for i, (k, t, d, items) in enumerate(GROUPS))}</div>
</div></section>

<section class="a-crew"><div class="wrap a-crew-in">
<figure class="reveal">{img("ay-planting", "Action crew members in hi-vis shirts planting shrubs in a new bed")}</figure>
<figure class="reveal">{img("ay-leaves", "Action crew members hauling leaves on a tarp during a yard clean up")}</figure>
<div class="reveal a-crew-t"><p class="label">About us</p><h2>Licensed. Insured. <em>Decades in.</em></h2><p>We are a group of licensed &amp; insured professionals with decades of experience that are passionate about what we do.</p><a class="tlink" href="@/about/">About Action {ARROW}</a></div>
</div></section>

<section class="sec a-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Quick <em>answers.</em></h2>
<a class="post-card a-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>USU Extension&rsquo;s numbers on mowing height, the one-third rule and leaving clippings.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Landscaping Murray, UT | Lawns &amp; Sprinklers | Action",
            "meta": "Action Lawn & Yardcare: licensed, insured landscaping in Murray and the Salt Lake Valley. Sod, planting, flagstone, lawn care, snow removal and sprinklers.",
            "body": body, "body_class": "is-home", "og": "ay-trench", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    out.append(dict(home(), path="home/", canonical=U, site_only=True, sitemap=False))
    sv = '<p class="answer">Landscaping, maintenance and sprinklers for homes across Murray and the Salt Lake Valley. Pick what you need below and your lineup card writes the quote request.</p>' + lineup() + \
         "".join(f'<h2>{t}</h2><p>{d}</p><ul>{"".join(f"<li>{s}</li>" for s in items)}</ul>' for k, t, d, items in GROUPS) + \
         f'<div class="pgal">{img("ay-trench", "Laying sprinkler pipe")}{img("ay-planting", "Planting a new bed")}{img("ay-leaves", "A leaf clean up")}</div>'
    out.append(K.page("services/", "Services", "Landscaping, lawn &amp; sprinkler services", "Landscaping &middot; Maintenance &middot; Sprinklers", "Services", "Landscaping, Lawn Care &amp; Sprinklers, Murray | Action",
                      "Action Lawn & Yardcare services in Murray: sod, mulch, flagstone, planting, weekly mowing, clean ups, aeration, fertilizing, snow removal and sprinklers.",
                      sv, image="ay-planting", alt="Action crew planting a new bed", canonical=EXT["services"]["canon"], schema=[K.svc_schema("services/", "Landscaping and lawn care", "Murray and the Salt Lake Valley, UT")]))
    ab = f'''<p class="answer">We are a group of licensed &amp; insured professionals with decades of experience that are passionate about what we do.</p>
<p>Action Lawn &amp; Yardcare serves homeowners across Murray and the Salt Lake Valley with three kinds of work: landscaping (sod, mulch and rock, flagstone, planting, edging, new landscapes and renovations), maintenance (weekly mowing with trimming and edging, clean ups, tree and bush trimming, leaves, snow removal, aeration, fertilizing and treatment programs) and sprinklers (start up, shut down, installation, check ups and repair).</p>
<div class="pgal">{img("ay-planting", "Action crew planting shrubs")}{img("ay-leaves", "Action crew hauling leaves")}</div>'''
    out.append(K.page("about/", "About", "About Action Lawn &amp; Yardcare", "Licensed, insured, decades of experience.", "About", "About Action Lawn &amp; Yardcare | Licensed, Insured, Murray",
                      "Action Lawn & Yardcare: a group of licensed and insured landscape professionals with decades of experience, serving Murray and the Salt Lake Valley.",
                      ab, image="ay-leaves", alt="Action crew on a clean up", canonical=EXT["about"]["canon"]))
    con = f'''<p class="answer">Call, email or message us on Facebook or Instagram.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18012444035">801-244-4035</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Based in</dt><dd><address>6501 S Cottonwood St<br>Murray, UT 84107</address></dd></div><div><dt>Social</dt><dd><a href="https://www.facebook.com/actionyardcare" rel="noopener">Facebook</a> &middot; <a href="https://www.instagram.com/actionyardcare/" rel="noopener">Instagram</a></dd></div></dl>'''
    out.append(K.page("contact-us/", "Contact", "Contact Action Lawn &amp; Yardcare", "Call, email or send the form.", "Contact", "Contact Action Lawn &amp; Yardcare | Murray, UT Landscaping",
                      "Contact Action Lawn & Yardcare in Murray: call 801-244-4035 or email info@actionyardcare.com for landscaping, lawn care, snow removal or sprinkler quotes.",
                      con, canonical=EXT["contact_us"]["canon"], form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("About", "about/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-244-4035.", " Murray, UT.")) for x in out]
