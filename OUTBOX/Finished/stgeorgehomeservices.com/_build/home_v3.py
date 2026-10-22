"""Premium home (v3) for stgeorgehomeservices.com: "The paper trail".
References (screenshotted 20 Oct 2026): Basecamp (a letter on paper, signed by the founder), Everlane "Radical Transparency"
(big photography, the cost laid bare), Stripe Press (editorial serif). Signatures: the quote receipt that prints itself as you
scroll (every line is from the client's Plain Terms), and the eight-town switcher (the first documented fact of four sections
on each town page, with the source it cites). Everything else is the client's own words and photographs."""
import html
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, EMAIL, HOURS
from pagekit import ARROW, PHONE, HOME, cta
import p_blog

TRADES = [("plumbing/", "Plumbing", "The systems that make the house work, and the bath and kitchen work that touches them.", "work-bathroom-remodel-wide", "span-7"),
          ("hvac-st-george-ut/", "Heating and air", "The system that keeps the house liveable in July, and the one thing in it you cannot put off.", "work-ac-condenser-gauges-st-george", "span-5"),
          ("accessible-living/", "Accessible living", "Built so you can stay in the house. Built so it doesn&rsquo;t look built.", "work-shower-conversion-tile", "span-4"),
          ("water-wise-landscape/", "Water-wise landscape", "Lawn out, desert in, with the rebate paperwork handled for you.", "work-water-wise-front-yard-wide-st-george", "span-4"),
          ("epoxy-flooring-st-george-ut/", "Concrete coatings", "The floor you already own, ground back and finished.", "coatings-garage-flake-low-angle-door", "span-4"),
          ("painting-st-george-ut/", "Painting", "Inside, outside, and the wall repair that has to happen before either one.", "painting-accent-wall-after", "span-6"),
          ("permanent-lighting-st-george-ut/", "Permanent lighting", "Put the lights up once. Change them from a remote.", "lighting-permanent-lighting-orange-purple-wide", "span-6")]
RECEIPT = [("Diagnostic fee, standard hours", "$150"), ("Evenings, weekends, holidays", "+$50"), ("Diagnostic fee if you hire us", "credited"), ("Price written", "after we look"),
           ("Price changes you didn&rsquo;t ask for", "none"), ("Work you didn&rsquo;t approve", "none"), ("Floor coverings, boot covers, haul-away", "included"), ("Guarantee on our labor", "1 year")]
FAQ = [("Can it wait until morning?", "Most things can, and the daytime rate is lower. Emergency calls are answered any hour, every day, and what we will tell you on that call is whether the thing you have can wait."),
       ("What does a visit cost?", "One flat fee to find the problem: $150 during standard hours, $50 more in the evening, at weekends and on holidays. If you hire us, that fee comes off the job. You&rsquo;re told which rate applies on the phone, before anyone is dispatched."),
       ("Who will come to the house?", "Before your appointment you&rsquo;ll get a message with the name and photo of the technician coming, and the time window. He&rsquo;ll be in a marked truck and a company shirt."),
       ("How do I check you?", 'Ask for the license number and the insurance certificate. Both come the same day, and you can check the license yourself on the state&rsquo;s public lookup. <a href="@/guides/check-a-utah-contractor/">How to check a Utah contractor</a>.')]


def home(X, towns):
    tiles = "".join(f'<a class="tile {sp} reveal-up" href="@/{p}">{img(im, "")}<span class="t-go">{ARROW}</span><span class="t-in"><b>{t}</b><span>{d}</span></span></a>' for p, t, d, im, sp in TRADES)
    rec = "".join(f'<li class="r-line" style="--i:{i}"><span>{a}</span><i></i><b>{b}</b></li>' for i, (a, b) in enumerate(RECEIPT))
    tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-town="{i}">{html.escape(n)}</button>' for i, (n, p, c, f) in enumerate(towns))
    panels = ""
    for i, (n, p, c, facts) in enumerate(towns):
        fl = "".join(f'<li><span class="tf-k">{lab}</span><p>{html.escape(t)}<a class="cite" href="@/{src}" title="{html.escape(st)}">{j + 1}</a></p></li>' for j, (lab, t, src, st) in enumerate(facts))
        panels += f'<div class="tp" data-town="{i}"{"" if i == 0 else " hidden"}><div class="tp-head"><b>{html.escape(n)}</b><span>{c} checkable facts, each with its source</span></div><ol class="tfacts">{fl}</ol><a class="tlink" href="@/{p}">Everything true of {html.escape(n)} {ARROW}</a></div>'
    guides = [("guides/hard-water-and-water-heaters/", "What St. George water does to a water heater"), ("guides/condo-pipe-who-pays/", "A pipe broke in the wall of your condo. Who pays?"),
              ("guides/artificial-turf-heat/", "Artificial turf, measured: 200 degrees on a 98 degree day"), ("guides/what-counts-as-an-emergency/", "What counts as a plumbing emergency"),
              ("guides/curbless-shower-guide/", "Curbless walk-in showers: the complete guide")]
    gl = "".join(f'<li><a href="@/{p}"><span class="g-n">{i + 1:02d}</span><b>{t}</b>{ARROW}</a></li>' for i, (p, t) in enumerate(guides))
    body = f'''
<section class="lh"><div class="wrap lh-grid">
<div class="lh-text"><p class="label">St. George &amp; Washington County, Utah</p>
<h1>Plumbing, AC repair and the rest of the house in St. George. <em>One quote that doesn&rsquo;t change.</em></h1>
<p class="lede">St. George Home Services does plumbing and heating and air repair in St. George, plus kitchens, baths and the rest of the inside, accessible living, water-wise yards, concrete coatings and painting. One number, one crew, one quote.</p>
<div class="btn-row"><a class="btn accent" href="tel:+14358500053">{PHONE} Call (435) 850-0053</a><a class="btn ghost" href="@/contact/">Ask for a visit {ARROW}</a></div>
<p class="lh-hours">A person answers, 7 a.m. to 5 p.m. weekdays. Emergency calls answered any hour, every day.</p></div>
<div class="letter reveal-up"><figure class="l-photo">{img("work-ryan-nunez-st-george-flag", "Ryan Nunez on a residential street, in a St. George Home Services polo shirt, beside an American flag", priority=True)}</figure>
<div class="l-body"><p class="l-hi">&ldquo;Around here, a lot of people say they do everything, but when it comes down to specific situations, they may not.&rdquo;</p>
<p>&ldquo;I started all this when I was 16. I got into plumbing and specialized in that, and then that kind of moved me towards HVAC, air conditioning. And through that, over the years, I was able to focus on one trade at a time. And then I started rolling into the entire home.&rdquo;</p>
<p class="l-sig"><span class="sig">Ryan Nunez</span><small>Owner, and the Utah license this company works under</small></p></div></div>
</div></section>

<div class="promises"><div class="wrap pr-in"><div><b>A person answers.</b><span>We tell you whether it can wait.</span></div><div><b>You meet them first.</b><span>Name and photo of whoever is coming, before the knock.</span></div><div><b>Nothing starts until you say yes.</b><span>Not one part, not one hour.</span></div><div><b>The quote is the number.</b><span>There is no second number.</span></div></div></div>

<section class="sec rcpt-sec" data-receipt><div class="wrap rcpt-grid">
<div class="rcpt-text"><p class="label">Plain Terms</p><h2>Most people have been handed <em>a second number.</em></h2>
<p>The job opens up, something is &ldquo;worse than we thought,&rdquo; and the price moves. We write the price after we&rsquo;ve looked at the work, not before, and then we hold it. If we missed something, that&rsquo;s our miss to eat, not your bill to absorb.</p>
<p>Same promise on an emergency call.</p><p><a class="tlink" href="@/plain-terms/">Read all of Plain Terms {ARROW}</a></p></div>
<div class="rcpt-wrap"><div class="receipt"><div class="r-head"><b>St. George Home Services</b><span>Plain Terms &middot; every job</span></div><ol class="r-lines">{rec}</ol>
<div class="r-total"><span>Second number</span><b>none</b></div><p class="r-foot">The quote is the number.</p><span class="stamp">Approved by you</span></div></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">What we do</p><h2>One company for the plumbing, <em>the inside and the yard.</em></h2></div>
<div class="bento sg-bento">{tiles}</div>
<p class="note">Not sure which of those it is? Browse by where the work is instead: <a href="@/indoors/">everything indoors</a> or <a href="@/outdoors/">everything outdoors</a>.</p>
</div></section>

<section class="sec ba-sec"><div class="wrap ba-grid">
<div class="reveal-up"><p class="label">What it looks like when we leave</p><h2>The photographs are ours. <em>Nobody in them is a model.</em></h2>
<p>And no job in them belongs to somebody else. Drag across a living-room wall we painted: before, and after the rug and furniture went back.</p>
<p><a class="tlink" href="@/painting-st-george-ut/">Painting in St. George {ARROW}</a></p></div>
<div class="compare reveal-up"><div class="cmp-stage" data-compare>{img("painting-accent-wall-after", "A living room accent wall finished in near-black under a tray ceiling, with the rug and furniture back in place")}<div class="cmp-before">{img("painting-accent-wall-before", "The same living room wall before painting")}</div><span class="cmp-handle" aria-hidden="true"></span><span class="cmp-tag l">Before</span><span class="cmp-tag r">After</span><input class="cmp-range" type="range" min="0" max="100" value="50" aria-label="Drag to compare the wall before and after"></div></div>
</div></section>

<section class="sec town-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Where we work</p><h2>Eight towns, and the rules change <em>at every city line.</em></h2>
<p>The plumbing code is the same across Utah. The lawn cap, the watering hours, the lighting rule, the power company and what is in the water are not. Pick a town.</p></div>
<div class="towns" data-towns><div class="t-tabs" role="tablist" aria-label="Choose a town">{tabs}</div><div class="t-panels">{panels}</div></div>
<p class="note">We don&rsquo;t cover Mesquite. It is in Nevada, and our licenses are Utah licenses. <a href="@/research/">Every number on this site, and the document it came from</a>.</p>
</div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.14">{img("lighting-permanent-lighting-orange-purple-wide", "")}</div><div class="wrap"><blockquote class="reveal-up">Put the lights up once. <em>Change them from a remote.</em></blockquote><footer>Small LED lights in a track under the eaves, up all year, set to your town&rsquo;s lighting rules before we leave. <a href="@/permanent-lighting-st-george-ut/">Permanent lighting</a></footer></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Read before you decide</p><h2>You shouldn&rsquo;t have to take <em>anyone&rsquo;s word for it.</em></h2><ol class="glist">{gl}</ol>
<p><a class="tlink" href="@/guides/">All the guides {ARROW}</a> &nbsp; <a class="tlink" href="@/{p_blog.POST[1]}">New: {p_blog.POST[0]} {ARROW}</a></p></div>
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": "https://stgeorgehomeservices.com", "title": "Plumbing & AC Repair in St. George, UT | St. George Home Services", "og": "work-bathroom-remodel-wide",
            "meta": "Plumbing and AC repair in St. George, Utah, plus baths, accessible living, water-wise yards, coatings and painting. One crew, one quote that doesn&rsquo;t change.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
