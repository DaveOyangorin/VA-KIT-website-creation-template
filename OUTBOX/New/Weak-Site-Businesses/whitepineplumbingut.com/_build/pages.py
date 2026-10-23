"""Pages for the whitepineplumbingut.com redesign: "Rooted & flowing".

White Pine's tagline is "Rooted in Quality, Flowing in Trust", and its best asset is its people: two co-owner plumbers, two plumbers and an
office lead, photographed together by a mountain stream. The page opens on a credited Commons sunset over South Jordan (their own photos
are too small for a banner) and puts the team right under it. The signature is the pipeline: their five-step process drawn as a copper
pipe with five valves; open a valve and water flows to that step and its card opens, in their own words.
Pine green, water blue and copper; Fraunces, DM Sans, DM Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 4 URLs and canonicals; /blank/ (an empty "Blog Page") becomes the blog index. One new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

STEPS = [("Contact us", "Reach out to our friendly team by phone, text, or online form to get started. We&rsquo;ll listen carefully to your concerns and schedule a convenient time to discuss your plumbing needs. Whether it&rsquo;s an emergency or a planned project, we&rsquo;re ready to help."),
         ("Assessment", "Our licensed plumber arrives to evaluate the issue in detail. We&rsquo;ll diagnose the problem, explain what&rsquo;s happening in clear terms, and answer your questions. No confusing jargon, just straightforward communication you can trust!"),
         ("Planning", "Once we understand your situation, we&rsquo;ll create a tailored solution proposal. This includes clear pricing, available options, and an estimated timeline. You&rsquo;ll always know exactly what to expect before we begin."),
         ("Implementation", "Our expert team gets to work, completing the repair or installation with precision and care. We use quality materials, industry-best practices, and take every precaution to protect your home while we work."),
         ("Follow-up", "After the job is complete, we&rsquo;ll walk you through the results, test everything, and make sure you&rsquo;re fully satisfied. We&rsquo;ll also share maintenance tips to help you avoid future issues.")]
SERV = [("Drain cleaning", "Backed-up drains cleared and flowing again."), ("General plumbing", "Everyday plumbing for your home, done right."), ("Water softeners", "Water softeners for homes with hard water."),
        ("Water heaters", "Water heater installs and urgent water heater issues."), ("Plumbing repairs", "Repairs done with precision and care, including burst pipes."), ("Leak locating &amp; repair", "Find the leak, then fix it.")]
TEAM = [("wp-jake", "Jake Winward", "Owner &middot; Expert Plumber", "Co-founder and owner with over a decade of hands-on experience. He leads the team with a commitment to quality craftsmanship, integrity and care, and his goal is that every customer feels taken care of from start to finish."),
        ("wp-rett", "Rett Speidel", "Co-owner &middot; Expert Plumber", "Co-founder and owner who brings precision, reliability, and leadership to every project. Known for his problem-solving skills, he oversees complex plumbing installations and helps refine company processes."),
        ("wp-brady", "Brady Winward", "Plumber", "A skilled plumber with a focus on detail and long-lasting results, whether it&rsquo;s a new installation or a repair, with a friendly, positive attitude and dependable work ethic."),
        ("wp-sebastian", "Sebastian Rivera", "Plumber", "Combines technical expertise with a positive, customer-focused approach. He enjoys tackling challenging projects and takes pride in representing the White Pine standard."),
        ("wp-brooke", "Brooke Stratton", "Office Administrator &middot; Customer Care", "The heart of White Pine&rsquo;s daily operations: scheduling, client communication, marketing, and the systems that keep every project flowing efficiently.")]
FAQ = [("How do I reach White Pine Plumbing?", "<p>By phone, text or the online form, whichever works best for you. Call or text 435-357-5862.</p>"),
       ("Do you handle plumbing emergencies?", "<p>Yes. We know plumbing emergencies can happen at any time, so our team responds quickly and reliably: burst pipes, backed-up drains or urgent water heater issues.</p>"),
       ("Will I know the price before you start?", "<p>Yes. After the assessment we create a tailored proposal with clear pricing, available options and an estimated timeline, so you always know what to expect before we begin.</p>"),
       ("When is the job done?", "<p>Not until you&rsquo;re completely satisfied. We walk you through the results, test everything, and share maintenance tips.</p>")]


def pipeline():
    n = len(STEPS)
    valves = "".join(f'<button type="button" class="vlv" data-step="{i}" aria-pressed="{"true" if i == 0 else "false"}" aria-label="Step {i + 1}: {html.escape(html.unescape(t))}" style="--x:{(i + .5) / n * 100:.1f}%"><span class="vlv-w" aria-hidden="true"></span><span class="vlv-n">{i + 1}</span><span class="vlv-t">{t}</span></button>' for i, (t, d) in enumerate(STEPS))
    cards = "".join(f'<div class="pc" data-card="{i}"{"" if i == 0 else " hidden"}><p class="mono">Step {i + 1} of {n}</p><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(STEPS))
    return f'''<div class="pipe" data-pipe>
<div class="pipe-run"><div class="pipe-tube" aria-hidden="true"><div class="pipe-water" data-water></div></div>{valves}</div>
<div class="pipe-cards" aria-live="polite">{cards}</div>
<div class="pipe-nav"><button type="button" class="btn ghost" data-prev>Previous</button><button type="button" class="btn accent" data-next>Next step {ARROW}</button></div>
</div>'''


def home():
    body = f'''
<section class="w-hero"><div class="wh-img" data-parallax="0.08">{img("wp-hero", "Sunset over South Jordan, Utah, with snowy Wasatch peaks and city lights", priority=True)}</div>
<div class="wrap wh-in"><div class="wh-txt"><p class="label">South Jordan &middot; Rooted in Quality, Flowing in Trust</p>
<h1>Your plumber in South Jordan, <em>you can rely on.</em></h1>
<p class="lede">White Pine Plumbing is a plumber in South Jordan. From drain cleaning to water heater installs, water softeners and leak repair, we deliver expert care for every client, with fast communication and honest pricing.</p>
<div class="btn-row"><a class="btn accent" href="tel:+14353575862">{PHONE} Call or text 435-357-5862</a><a class="btn ghost" href="@/getaquote/">Get a quote {ARROW}</a></div></div></div>
<p class="credit">South Jordan &middot; Jeremy Taylor, CC BY 2.0, via Wikimedia Commons</p></section>

<section class="w-team-band"><div class="wrap w-tb-in">
<figure class="reveal">{img("wp-team", "The White Pine Plumbing team standing together on a boardwalk by a mountain stream in fall")}</figure>
<div class="reveal"><p class="label">Meet the crew</p><h2>Five people. <em>One standard.</em></h2>
<p>Our dedicated team brings experience, craftsmanship, and care to every project, led by co-owners and expert plumbers Jake Winward and Rett Speidel.</p>
<div class="faces">{"".join(f'<span title="{n}">{img(im, n)}</span>' for im, n, r, d in TEAM)}</div>
<a class="tlink" href="@/team/">Meet our team {ARROW}</a></div>
</div></section>

<section class="sec w-serv" id="services"><div class="wrap">
<div class="w-head split-h reveal"><div><p class="label">Plumbing services</p><h2>From drains <em>to water heaters.</em></h2></div><p class="lede">Expert care for every client, for planned projects and emergencies alike.</p></div>
<div class="serv">{"".join(f'<div class="sv reveal"><span class="mono">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(SERV))}</div>
<div class="jobs">{img("wp-tub", "White Pine plumbers installing fixtures on a clawfoot tub")}{img("wp-drain", "A White Pine plumber working on a floor drain")}</div>
</div></section>

<section class="sec w-proc" id="process"><div class="wrap">
<div class="w-head split-h reveal"><div><p class="label">How we work</p><h2>Five steps, <em>no surprises.</em></h2></div><p class="lede">Open each valve to follow a job from the first call to the follow-up.</p></div>
{pipeline()}
</div></section>

<section class="sec w-promise"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Why choose us</p><h2>There when you <em>need us most.</em></h2>
<p>At White Pine Plumbing, we know plumbing emergencies can happen at any time, that&rsquo;s why our team responds quickly and reliably. Whether it&rsquo;s a burst pipe, backed-up drain, or urgent water heater issue, you can count on us to be there when you need us most.</p></div>
<div class="reveal"><p class="label">Our promise to you</p><p>When you hire White Pine Plumbing, you can expect fast communication, honest pricing, and expert solutions. We treat your home like our own, and we don&rsquo;t consider the job done until you&rsquo;re completely satisfied.</p>
<p>Reaching us is easy: phone, text or email, whichever works best for you. With White Pine Plumbing, you&rsquo;ll have peace of mind knowing your home is protected by experts who are Rooted in Quality, Flowing in Trust.</p></div>
</div></section>

<section class="sec w-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card w-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What USGS says hard water does to pipes and water heaters, and how to find your own water&rsquo;s numbers.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Plumber South Jordan, UT | Drains &amp; Heaters | White Pine",
            "meta": "White Pine Plumbing: plumber in South Jordan, UT. Drain cleaning, water heaters, water softeners, repairs and leak locating. Fast communication, honest pricing.",
            "body": body, "body_class": "is-home", "og": "wp-team", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    tm = '<p class="answer">Our dedicated team brings experience, craftsmanship, and care to every project!</p>' + f'<figure class="pfig">{img("wp-team", "The White Pine Plumbing team")}</figure>' + \
         '<div class="team">' + "".join(f'<div class="tm">{img(im, n)}<div><h3>{n}</h3><p class="mono">{r}</p><p>{d}</p></div></div>' for im, n, r, d in TEAM) + "</div>" + \
         '<h2>Plumber education</h2><ul><li>Mountainland Technical College</li><li>Salt Lake Tech / SLCC</li></ul>'
    out.append(K.page("team/", "Team", "Meet our team", "Rooted in Quality, Flowing in Trust.", "Team", "Meet the White Pine Plumbing Team | South Jordan Plumbers",
                      "Meet White Pine Plumbing in South Jordan: co-owners Jake Winward and Rett Speidel, plumbers Brady Winward and Sebastian Rivera, and office lead Brooke Stratton.",
                      tm, image="wp-team", alt="The White Pine Plumbing team", canonical=EXT["team"]["canon"]))
    q = '''<p class="answer">Reach out by phone, text, or the form to get started. We&rsquo;ll listen carefully and schedule a convenient time to discuss your plumbing needs.</p>
<dl class="info"><div><dt>Call or text</dt><dd><a href="tel:+14353575862">435-357-5862</a></dd></div><div><dt>Office</dt><dd><address>489 South Jordan Pkwy Ste 239<br>South Jordan, UT 84095</address></dd></div></dl>'''
    out.append(K.page("getaquote/", "Get a quote", "Get in touch", "Emergencies and planned projects.", "Get a quote", "Get a Plumbing Quote in South Jordan | White Pine Plumbing",
                      "Get a quote from White Pine Plumbing in South Jordan: call or text 435-357-5862 or send the form for drain cleaning, water heaters, softeners or repairs.",
                      q, canonical=EXT["getaquote"]["canon"], form_side=True))
    bl = f'<div class="cats"><a class="cat" href="@/{p_blog.SLUG}"><b>{p_blog.H1}</b><span>Oct 22, 2026</span><em>Read {ARROW}</em></a></div>'
    out.append(K.page("blank/", "Blog", "Blog", "Plumbing notes for South Jordan homes.", "Blog", "Plumbing Blog for South Jordan Homes | White Pine Plumbing",
                      "The White Pine Plumbing blog: practical plumbing notes for South Jordan and Salt Lake Valley homeowners, starting with hard water and what it does to pipes.",
                      bl, canonical=EXT["blank"]["canon"]))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Team", "team/"), ("Get a quote", "getaquote/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call or text 435-357-5862.", " South Jordan, UT.")) for x in out]
