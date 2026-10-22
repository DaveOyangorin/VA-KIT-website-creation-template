"""Home page for the ezelectric.com redesign: "Flip it on".
The breaker list is EZ Electric's own "We specialize in installation, repairs, and upgrades for" list (home page), each matched to the
service page that describes it; the sentences come from those pages."""
from engine import img, faq_html, faq_ld, crumbs_ld
from cfg import U
import pagekit as K
from pagekit import ARROW, PHONE, HOME

R, C, O = "residential-services/", "commercial-services/", "outdoor-specialty-electrical-services/"
BREAKERS = [("Light fixtures", "15A", "Light fixtures that set the perfect mood.", "Under-cabinet, recessed and security lighting inside, energy-efficient LED upgrades, and landscape lighting outside.", R),
            ("Outlets &amp; switches", "20A", "Outlets and switches to keep things running smoothly.", "An outlet that&rsquo;s not working, a breaker that keeps tripping, wires or outlets warmer than they should be: we diagnose and repair it.", R),
            ("Pool, spa &amp; hot tub", "50A", "Pool, spa and hot tub electrical, because relaxation shouldn&rsquo;t come with a short circuit.", "Dedicated circuits, bonding and grounding to local code and manufacturer specs, plus troubleshooting and repairs.", O),
            ("Smoke &amp; smart home", "15A", "Smoke detectors and smart home devices for modern safety.", "Smoke and carbon monoxide detectors are essential for protecting your home and family.", R),
            ("Panels &amp; meters", "200A", "Electrical panels, meters and breaker boxes for efficient power distribution.", "An outdated panel or frequent power surges? We install and replace panels and meters, and work with the city to keep it up to code.", R),
            ("EV chargers", "40A", "EV chargers to keep your ride charged and ready.", "All levels of EV chargers, in the garage, the driveway or a custom spot, with a panel upgrade if your system needs the capacity.", O),
            ("Surge &amp; generators", "30A", "Whole-house surge protectors and generators for backup power.", "Backup generators keep refrigerators, lights and medical devices running when the grid goes down. We size, install and service them.", O),
            ("Room remodels", "20A", "Room remodels (kitchen, bath and more) to power up your renovations.", "Adding a room or finishing the basement? New outlets, lighting and system upgrades, safe and up to code. Whole-home rewiring too.", R),
            ("Outdoor lighting", "15A", "Outdoor lighting to keep your space bright and secure.", "Landscape, pathway, security and patio lighting, from concept to installation.", O),
            ("Machine power", "60A", "Commercial machine power, because business can&rsquo;t run on empty.", "Dedicated power for heavy machinery and specialized commercial equipment.", C)]
MORE = ["New construction wiring", "Full home or business rewiring", "Custom electrical design solutions", "Preventative maintenance to keep everything in check"]
QUOTES = [("These guys are great!! Called them and made an appointment and they sent Lance out two different times for more technical stuff. He was awesome! Nice lady who took my calls was very nice and professional. I would highly recommend them to anyone who needs electrical work!! Thank you EZ Electric!", "Todd Andrews"),
          ("EZ Electric was a great company to work with. The electrician we worked with, Andrew, was very knowledgeable, helpful, and kind. He made sure each of the four projects we had done were done well. I am very impressed with their work and their pricing was fantastic. We will definitely be using this company again!", "Jessica Larsen"),
          ("I love working with Lance at EZ Electric. He&rsquo;s always on time and works efficiently. Professional, knowledgeable and makes suggestions if needed. I done a huge project with him and would refer him to anyone that could use a great electrician!", "Stephanie Fordham")]
HOME_FAQ = [("Do you give free quotes?", "<p>Yes. Give us a call for a free quote. We also offer a free in-person consultation: an on-site inspection of your current system or project, including a safety check and load analysis, and a detailed outline of the service options that suit you. No matter what, the consult is on us.</p>"),
            ("Where do you work?", "<p>Homes and businesses throughout Salt Lake County and Utah County.</p>"),
            ("Do you do commercial work?", "<p>Yes: repairs, installations, remodels, lighting, inspections and code-violation correction, panels and meters, EV charging stations, new construction, generators, machine power and tenant improvements. See <a href=\"@/commercial-services/\">commercial services</a>.</p>"),
            ("What are your hours?", "<p>Monday to Friday, 8 AM to 6 PM. We&rsquo;re closed Saturdays and Sundays.</p>")]


def panel():
    brk = "".join(f'''<button type="button" class="brk" data-b="{i}" aria-pressed="false"><span class="brk-n">{i + 1:02d}</span><span class="brk-sw" aria-hidden="true"><i></i></span><span class="brk-l">{n}</span></button>'''
                  for i, (n, a, l1, l2, p) in enumerate(BREAKERS))
    outs = "".join(f'<div class="ld" data-ld="{i}"><p class="ld-k">Circuit {i + 1:02d} &middot; <b>On</b></p><h3>{n}</h3><p class="ld-1">{l1}</p><p>{l2}</p><a class="tlink light" href="@/{p}">See the service {ARROW}</a></div>'
                   for i, (n, a, l1, l2, p) in enumerate(BREAKERS))
    return f'''<div class="pnl" data-panel><div class="pnl-box"><div class="pnl-top"><span>EZ Electric</span><span>Service panel</span></div>
<div class="pnl-main"><button type="button" class="brk main" data-main aria-pressed="false"><span class="brk-sw" aria-hidden="true"><i></i></span><span class="brk-l">Main</span></button></div>
<div class="pnl-grid">{brk}</div><p class="pnl-label">Label: what EZ installs, repairs &amp; upgrades</p></div>
<div class="pnl-out" aria-live="polite"><div class="bulb" aria-hidden="true"><svg viewBox="0 0 64 96"><path class="glass" d="M32 6C17 6 7 17 7 31c0 10 6 16 11 22 3 4 4 8 4 12h20c0-4 1-8 4-12 5-6 11-12 11-22C57 17 47 6 32 6z"/><path class="fil" d="M24 44l4-8 4 8 4-8 4 8"/><rect class="base" x="22" y="68" width="20" height="6" rx="2"/><rect class="base" x="23" y="77" width="18" height="6" rx="2"/><path class="base" d="M27 86h10l-2 5h-6z"/></svg></div>
<div class="ld on" data-ld="idle"><p class="ld-k">All circuits off</p><h3>Flip a breaker.</h3><p>Ten circuits, ten things we do every week. Flip one to see the job, or throw the main to light them all.</p></div>{outs}</div></div>'''


def home():
    body = f'''
<section class="z-hero"><div class="z-hero-in">
<div class="z-hero-txt wrap-l"><p class="label"><span class="spark"></span>Residential &middot; Commercial &middot; Outdoor</p>
<h1>Electricians in Salt Lake City <span>and Utah County.</span></h1>
<p class="lede">EZ Electric handles installations, repairs and upgrades for homes and businesses throughout Salt Lake and Utah counties, from a flickering light to a full rewire. Fast responses, upfront pricing, and free quotes.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Request an Estimate {ARROW}</a><a class="btn ghost" href="tel:+13852840394">{PHONE} (385) 284-0394</a></div>
<ul class="z-facts"><li><b>Free</b>quotes &amp; in-person consults</li><li><b>Upfront</b>pricing</li><li><b>Mon&ndash;Fri</b>8 AM &ndash; 6 PM</li></ul></div>
<figure class="z-photo">{img("ez-landscape-lighting", "Landscape lighting on a stone retaining wall at dusk, with the Wasatch Mountains behind", priority=True)}<figcaption>Landscape lighting &middot; Utah County</figcaption></figure>
</div></section>

<section class="sec z-panel" id="panel"><div class="wrap">
<div class="z-head reveal"><p class="label">What we do</p><h2>Flip it on.</h2><p class="lede">Installation, repairs and upgrades, one circuit at a time. This panel is labeled with the work we specialize in.</p></div>
{panel()}
<p class="z-more reveal"><b>Need more?</b> {" &middot; ".join(MORE)}, and so much more.</p>
</div></section>

<section class="sec z-doors"><div class="wrap">
<div class="z-head split-h reveal"><div><p class="label">Three ways in</p><h2>From repairs to remodels, <span>EZ does it.</span></h2></div><p class="lede">No project is too big, too small or too complex. Not sure what you need? We&rsquo;ll troubleshoot, diagnose and deliver a solution that keeps your home or business running.</p></div>
<div class="doors">
<a class="door d1 reveal" href="@/residential-services/"><figure>{img("ez-panel-brick", "EZ Electric electricians working on the electrical panel of a brick home")}</figure><span class="d-k">01</span><b>Residential</b><p>Reliable, code-compliant repairs, upgrades and installations for homes across Salt Lake and Utah counties.</p><em>View services {ARROW}</em></a>
<a class="door d2 reveal" href="@/commercial-services/"><span class="d-k">02</span><b>Commercial</b><p>Maintenance, tenant improvements and new construction wiring for Utah businesses, from storefronts to warehouses.</p><em>View services {ARROW}</em>
<svg class="d-art" viewBox="0 0 200 120" aria-hidden="true"><path d="M0 100h200M20 100V40h50v60M90 100V20h60v80M165 100V60h25v40M30 50h10v10H30zM50 50h10v10H50zM100 30h12v12H100zM126 30h12v12H126zM100 54h12v12H100zM126 54h12v12H126z"/><path class="hot" d="M0 112h60l10-12h40l10 12h80"/></svg></a>
<a class="door d3 reveal" href="@/outdoor-specialty-electrical-services/"><figure>{img("ez-conduit-af", "An EZ Electric technician running conduit under an eave in American Fork")}</figure><span class="d-k">03</span><b>Outdoor &amp; specialty</b><p>Outdoor lighting, spa wiring, EV chargers, generators and specialty projects, installed safely.</p><em>View services {ARROW}</em></a>
</div></div></section>

<section class="sec z-consult"><div class="wrap z-consult-in">
<div class="reveal"><p class="label">How we start</p><h2>The consult is on us.</h2><p>Before any work, a licensed electrician meets you in person to answer your questions and understand your needs, concerns and goals.</p><a class="btn accent" href="@/contact/">Book a free consultation {ARROW}</a></div>
<ol class="cs-steps"><li class="reveal"><span>01</span><b>In-person discussion</b><p>Talk it through with an electrician: questions, needs, concerns and goals.</p></li>
<li class="reveal"><span>02</span><b>Free on-site inspection</b><p>We assess your current system or project, including a safety check and load analysis.</p></li>
<li class="reveal"><span>03</span><b>Zero-cost evaluation</b><p>A detailed outline of the service options that suit you best. No matter what, the consult is on us.</p></li></ol>
</div></section>

<section class="sec z-quotes"><div class="wrap">
<div class="z-head reveal"><p class="label">Google reviews</p><h2>Why you&rsquo;ll love us.</h2><p class="lede">Fast, friendly and fully charged. Here&rsquo;s what homeowners and businesses say.</p></div>
<div class="zq">{"".join(f'<blockquote class="reveal"><p>{q}</p><footer><b>{n}</b><span>Google review</span></footer></blockquote>' for q, n in QUOTES)}</div>
</div></section>

<section class="sec z-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Good to know</p><h2>Questions, answered.</h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal"><a class="post-card z-post" href="@/blog/winter-electrical-safety-utah/"><span class="label">From the blog</span><b>Winter electrical safety in Utah: space heaters, holiday lights and extension cords</b><p>Heating fires peak in December, January and February. What the NFPA and CPSC recommend.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": "Electrician Salt Lake City & Utah County | EZ Electric",
            "meta": "EZ Electric: licensed electricians in Salt Lake City and Utah County for residential, commercial and outdoor electrical work. Free quotes, upfront pricing.",
            "body": body, "body_class": "is-home", "og": "ez-landscape-lighting", "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}
