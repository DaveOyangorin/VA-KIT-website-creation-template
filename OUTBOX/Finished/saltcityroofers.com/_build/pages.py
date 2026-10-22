"""Pages for the saltcityroofers.com redesign: "Educate, Plan, Execute, Wrap it up."

The client's own four words for how a job runs become the spine of the site: four numbered chapters (I-IV), a homeowner's manual
tone, and the parts that make a roof drawn as an exploded stack (the eight layers their asphalt page lists). Copper is the accent
because copper chimney caps and custom copper gutters are on their services page; the neutrals are salt white and the navy and
teal of their logo. Real job photos only: the Avenues re-roof (before and finished, with a comparison slider), the Draper
exterior remodel and the Park City metal roof with snow retention, all from the client's own blog.
Home targets "roofing company salt lake city" (report, 17 Oct 2026); service pages name Salt Lake City in title, H1 and first
paragraph. The 22 blog posts keep their URLs and text. Left out (see notes): "Utah's #1", "most complete and trusted",
"finest", "the best roof", certification and supplier-endorsement claims, the 2017 "$10,000 average roof" price, stock photos
(Envato and similar), and the WordPress category, tag, author and slider archive pages.
"""
import html, json, os, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, NAME, LEGAL, U, HERE, DOMAIN, AREAS
from migrate import migrate
from illus import stack, legend
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CONTACT = "contact/"
HOME = ("Home", "")
DROP = re.compile(r"#1|most complete|most trusted|finest|best roof|go with the best|only the best|absolute best|best warranty|premium roofing|\$\s?\d|top industry|class of our own|"
                  r"ShingleMaster|certif|endorsed|prestigious|COVID|Please enter|Message failed|Thanks for your message|Your (name|email|phone|message)$", re.I)
POSTDROP = re.compile(r"\$\s?\d|^admin$|Comments Off|^on |Share This Story|^(Facebook|Twitter|Linkedin|Reddit|Tumblr|Google\+|Pinterest|Vk|Email)$|^\d{4}-\d\d-\d\dT", re.I)
CTA_P = re.compile(r"^(Get|Schedule|Book|Call|Contact|Talk|Learn|Explore|Request|Ask|See|View|Find|Start|Please Contact|Email Us|Read More|Download)\b[^.]{0,48}!?$", re.I)
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))


LINKFIX = [("@/roofing-blog/consume-less-roofing-contractor-utah/", "@/do-your-best-consume-less-a-roofing-contractor-helps-clean-utah-air/"),
           ("@/infographic-7-questions-to-ask-when-hiring-a-utah-roofing-contractor/", "@/blog/2017/05/13/infographic-7-questions-to-ask-when-hiring-a-utah-roofing-contractor/"),
           ("@/portfolio/", "@/roofing-blog/")]


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def tidy(s):
    out = []
    for blk in re.findall(r"<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s, re.S):
        txt = html.unescape(re.sub(r"<[^>]+>", "", blk)).strip()
        if txt.startswith("About the Author"): break
        if blk.startswith("<p>") and CTA_P.match(txt): continue
        blk = re.sub(r'<a href="@/blog/(?:author|category|tag|slide)[^"]*">(.*?)</a>', r"\1", blk)
        blk = re.sub(r"<br>\s*\n?<p>", "<br>", blk).replace("<p></strong>", "<p>")
        for a, b in LINKFIX: blk = blk.replace(a, b)
        out.append(blk)
    def minor(b): return b.startswith("<h3>") or re.fullmatch(r"<p><strong>[^<]{0,70}</strong></p>", b) is not None
    def head(b): return b.startswith("<h2>") or minor(b)
    out = [b for i, b in enumerate(out) if not (i + 1 < len(out) and ((minor(b) and head(out[i + 1])) or (b.startswith("<h2>") and out[i + 1].startswith("<h2>"))))]
    while out and head(out[-1]): out.pop()
    return "\n".join(out)


def mig(key, skip=(), drop=DROP):
    return tidy(migrate(HERE, key, DOMAIN, drop, skip_heads=skip))


CHAPTERS = [("I", "Educate", "A 15-minute look on the roof, then a 15-minute conversation about what we found: age, condition, damage, ventilation. You learn what your roof needs before anyone talks price."),
            ("II", "Plan", "Our estimator writes the quote and emails it, so you can read it on your own time: the scope, the system, options most contractors don&rsquo;t mention, and the warranty."),
            ("III", "Execute", "Tarps and plywood go down to protect the yard, the old roof comes off, soft decking is re-sheeted, and the new system goes on to the manufacturer&rsquo;s specification."),
            ("IV", "Wrap it up", "Debris raked and picked up, a heavy-duty magnet pass for nails, a blower for loose granules, and your labor and material warranty paperwork.")]
QUOTES = [("A very positive experience. Thank you for doing exactly what you said you would do in a timely and professional manner. I am very please with the work and would not hesitate to recommend you to friends and relatives.", "Pat B.", "Salt Lake City remodel client"),
          ("Brock was honest, informative, and very friendly throughout the entire process. The crew was on time, cleaned up, was friendly and did a good job. We will definitely recommend Salt City Roofers to others.", "Kody B.", "Cottonwood Heights roofing client"),
          ("We interviewed six different contractors for our roof and hands down wanted Salt City Roofers to do the job! SCR was the recommended choice of the local roofing supply co. They have a great + kind crew + did an awesome job.", "Brandon &amp; Sharon M.", "Federal Heights roofing client")]
HOME_FAQ = [("How long does a new roof take?", "About a week from start to finish for most homes, give or take a day or two for weather. It starts with the tear-off and disposal of the old roof; if the decking needs it, we re-sheet before the new system goes on."),
            ("What roofing materials suit Utah&rsquo;s climate?", "Properly installed asphalt shingles are durable and versatile. On low-slope roofs, TPO and PVC membranes are reliable. Metal costs more than asphalt but is a beautiful choice on mountain homes and cabins. We advise against concrete tile here, because freeze-thaw cycles crack it."),
            ("Do I get a written estimate?", "Yes. You get a detailed, written explanation of the work, including ventilation, maintenance, gutters and flashing details, plus information on our standard warranties and the manufacturer warranties available."),
            ("How far do you travel?", "Usually up to about 45 minutes from Salt Lake City. We&rsquo;ve worked along the Wasatch Front from Provo and Lehi to Park City and Ogden."),
            ("How do you protect my yard?", "We talk through your landscaping concerns first, lay tarps, move what we can, and use plywood to divert debris away from plants and shrubs.")]


def header():
    return Q(f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{img("salt-city-roofers-logo", NAME, lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Roofing</summary><div class="drop"><a href="@/services/">All services</a><a href="@/asphalt-shingle-systems/">Asphalt shingle systems</a><a href="@/slate-roofing-system/">Synthetic slate</a><a href="@/roof-warranty-information/">Warranties</a></div></details></li>
<li><a href="@/roofing-q-a/">Roofing Q&amp;A</a></li><li><a href="@/roofing-blog/">Blog</a></li><li><a href="@/about/">About</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Inspection</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/services/">Services</a><a href="@/asphalt-shingle-systems/">Asphalt shingle systems</a><a href="@/slate-roofing-system/">Synthetic slate</a><a href="@/roof-warranty-information/">Warranties</a>
<a href="@/roofing-q-a/">Roofing Q&amp;A</a><a href="@/roofing-blog/">Blog</a><a href="@/about/">About</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>''')


def footer():
    return Q(f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say"><span class="mono">I &middot; II &middot; III &middot; IV</span>Educate, plan, execute, <em>wrap it up.</em></p><div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Request a Free Inspection {ARROW}</a></div></div>
<div class="foot">
<div><span class="flogo">{img("salt-city-roofers-logo", NAME + " logo")}</span><p>{NAME}, a {LEGAL} company. Roofing and exterior remodeling in Salt Lake City since 2007.</p><p><a href="{S["fb"]}" rel="noopener">Facebook</a></p></div>
<div><h3>Roofing</h3><ul><li><a href="@/services/">Services</a></li><li><a href="@/asphalt-shingle-systems/">Asphalt shingle systems</a></li><li><a href="@/slate-roofing-system/">Synthetic slate</a></li><li><a href="@/roof-warranty-information/">Warranty information</a></li><li><a href="@/neighbors/">For neighbors</a></li></ul></div>
<div><h3>Learn</h3><ul><li><a href="@/roofing-q-a/">Roofing Q&amp;A</a></li><li><a href="@/roofing-blog/">Blog</a></li><li><a href="@/about/">About</a></li><li><a href="@/employment/">Employment</a></li></ul></div>
<div><h3>Contact</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p><p class="small">Serving {", ".join(AREAS[:3])} and the Wasatch Front, from Provo and Lehi to Park City and Ogden.</p></div>
</div><div class="fbottom"><span>&copy; 2026 {NAME}</span><span>Salt Lake City, Utah</span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{CONTACT}">Free Inspection</a></div>''')


def cta(title="Today&rsquo;s inspection, tomorrow&rsquo;s protection.", text="A no-cost roofing inspection and quote: fifteen minutes on the roof, fifteen minutes explaining what we found, and a written quote in your inbox."):
    return f'''<section class="cta"><div class="wrap cta-in">
<div><p class="label">No-cost inspection &amp; quote</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call</small><b>{S["phone"]}</b></a><a class="btn" href="@/{CONTACT}">Request an Inspection {ARROW}</a><p class="small"><a href="mailto:{S["email"]}">{S["email"]}</a></p></div></div></section>'''


def phero(trail, h1, lede, tag, image=None, alt="", buttons=True):
    art = f'<figure class="ph-img">{img(image, alt, priority=True)}</figure>' if image else ""
    btn = f'<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else ""}"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btn}</div>{art}</div></section>'''


def quote_form(title="Request a no-cost inspection"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Your name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Your phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Your email<input id="f-email" type="email" name="email" autocomplete="email"></label>
<label for="f-msg">Your message<textarea id="f-msg" name="message" placeholder="Address, and what you&rsquo;d like us to look at"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button><p class="note">We&rsquo;ll be in touch soon.</p></form>'''


def side(extra=""):
    return f'''<aside class="sv-side"><div class="side-card"><p class="label">No-cost inspection</p><h3>Talk to an estimator</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a><p class="small"><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>{extra}</aside>'''


def chapters_html():
    return "".join(f'<li class="reveal"><span class="rn">{r}</span><h3>{t}</h3><p>{d}</p></li>' for r, t, d in CHAPTERS)


def compare(before, after, b_alt, a_alt, cap):
    return f'''<figure class="pair"><div class="pair-in"><div>{img(before, b_alt)}<span class="tag tb">Before</span></div><div>{img(after, a_alt)}<span class="tag ta">After</span></div></div><figcaption>{cap}</figcaption></figure>'''


STORY = [("I", "Educate", "roof-vents-shingles", "Shingles and roof vents, looked at up close"),
         ("II", "Plan", "draper-roof-aerial", "A Draper roof from above, the way an estimator plans it"),
         ("III", "Execute", "park-city-snow-guards", "Snow guards going onto a standing seam roof in Park City"),
         ("IV", "Wrap it up", "avenues-finished-a", "The finished Avenues re-roof from the street")]
CASES = [("01", "The Avenues, Salt Lake City", "2021", "Membrane and asphalt re-roof", "A low-slope membrane section and a new asphalt roof on an Avenues bungalow.", "AVE",
          [("avenues-finished-c", "Finished Avenues roof from the corner"), ("avenues-finished-d", "Finished Avenues home from the street"), ("avenues-before-flat", "The low-slope section before the re-roof")]),
         ("02", "Draper", "2022", "Exterior remodel", "A covered porch, craftsman details, new doors and a wood soffit ceiling with skylights on a Draper home.", "DRAPER",
          [("draper-craftsman-remodel", "The Draper home after its craftsman-style remodel"), ("draper-front-door", "New front door on the Draper remodel"), ("draper-soffit-ceiling", "Wood soffit ceiling with skylights")]),
         ("03", "Park City", "2022", "Snow retention on a metal roof", "Snow guards installed on a standing seam metal roof on a Park City home.", "PARK",
          [("park-city-metal-aerial", "A Park City metal roof from above"), ("park-city-metal-wing", "Metal roof wing on a Park City home"), ("park-city-snow-guards", "Snow guards on the standing seam")])]


def home():
    story_f = "".join(f'<figure class="st-f{" on" if i == 0 else ""}" data-f="{i}">{img(n, a)}<figcaption>{a}</figcaption></figure>' for i, (r, t, n, a) in enumerate(STORY))
    story_s = "".join(f'<div class="st-step" data-s="{i}"><span class="st-rn">{r}</span><h3>{t}</h3><p>{d}</p></div>' for i, ((r, t, n, a), (_, _, d)) in enumerate(zip(STORY, CHAPTERS)))
    cases = ""
    for i, (no, place, yr, what, d, key, ims) in enumerate(CASES):
        post = getattr(p_blog, key)[1]
        cases += f'''<article class="spread{" flip" if i % 2 else ""} reveal"><a class="sp-main" href="@/{post}">{img(ims[0][0], ims[0][1])}</a>
<div class="sp-side"><div class="sp-txt"><p class="folio">Case file {no} &middot; {yr}</p><h3>{place}</h3><p class="sp-what">{what}</p><p>{d}</p><a class="tlink" href="@/{post}">Read the project notes {ARROW}</a></div>
<div class="sp-thumbs">{img(ims[1][0], ims[1][1])}{img(ims[2][0], ims[2][1])}</div></div></article>'''
    body = f'''
<section class="ed-hero"><div class="wrap ed-hero-in">
<div class="ed-hero-text"><p class="folio">No. 01 &middot; Salt Lake City &middot; Since 2007</p>
<h1>A roofing company in Salt Lake City <em>that explains before it quotes.</em></h1>
<p class="lede">Salt City Roofers is a roofing company in Salt Lake City for homeowners who want to understand their roof: asphalt shingle, synthetic slate and metal roofs, tear-offs and re-sheeting, roof conversions, gutters and copper chimney caps, with labor and material warranties on every project.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Request a No-Cost Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
<ol class="ed-index" aria-label="How a job runs">{"".join(f'<li><span>{r}</span>{t}</li>' for r, t, d in CHAPTERS)}</ol></div>
<div class="ed-hero-art"><figure class="ed-main">{img("draper-porch-mountains", "A Draper home after its exterior remodel, with the Wasatch Mountains behind", priority=True)}</figure>
<figure class="ed-inset">{img("slate-roof-stone-home", "Slate-look roof on a stone home with a copper dome")}<figcaption>Synthetic slate &middot; stone home</figcaption></figure>
<p class="ed-cap">Exterior remodel &middot; Draper, Utah</p></div>
</div></section>

<section class="pano" aria-label="A finished roof in the Avenues"><div class="pano-img" data-par="0.1">{img("avenues-finished-b", "A finished roof on an Avenues home in Salt Lake City")}</div><p class="pano-cap">Finished re-roof &middot; the Avenues, Salt Lake City &middot; 2021</p></section>

<section class="story-sec"><div class="wrap">
<div class="ed-head reveal"><p class="folio">Chapter guide</p><h2>Four chapters, <em>in this order.</em></h2>
<p class="lede">&ldquo;Educate, plan, execute, wrap it up&rdquo; is how we&rsquo;ve described our work for years. Scroll through what each part means on your roof.</p></div>
<div class="story" data-story><div class="st-vis"><div class="st-frames">{story_f}</div><div class="st-bar"><i data-bar></i></div><p class="st-count"><b data-n>I</b> / IV</p></div>
<div class="st-steps">{story_s}</div></div>
</div></section>

<section class="sec layers-sec"><div class="wrap split">
<div class="reveal"><p class="folio light">Inside the roof</p><h2>Eight layers, <em>not just shingles.</em></h2>
<p>Every roofing system is built from the deck up: plywood, drip edge, ice and water membrane, underlayment, flashings, the visible roof, the nails that hold it, and the ventilation that lets the attic breathe. Each manufacturer has its own installation practices, and whether the complete system is used affects the warranty.</p>
<a class="tlink light" href="@/asphalt-shingle-systems/">Asphalt shingle systems {ARROW}</a></div>
<div class="reveal">{stack()}</div></div></section>

<section class="sec"><div class="wrap">
<div class="ed-head split-head reveal"><div><p class="folio">The work</p><h2>What we <em>do.</em></h2></div><p class="lede">Steep-slope roofing in asphalt, synthetic slate and metal, plus the exterior work around it: conversions, soffit and fascia, gutters and copper chimney caps.</p></div>
<div class="svc2">
<a class="s2 s2a reveal" href="@/asphalt-shingle-systems/"><figure>{img("brick-home-new-roof", "Brick two-story home with a new dark shingle roof")}</figure><span class="folio">Steep slope</span><b>Asphalt shingle systems</b></a>
<a class="s2 s2b reveal" href="@/slate-roofing-system/"><figure>{img("slate-roof-stone-home", "Slate-look roof on a stone home with a copper dome")}</figure><span class="folio">Steep slope</span><b>Synthetic slate</b></a>
<a class="s2 s2c reveal" href="@/{p_blog.PARK[1]}"><figure>{img("park-city-metal-top", "A metal roof in Park City from above")}</figure><span class="folio">Metal</span><b>Metal roofs &amp; snow retention</b></a>
<a class="s2 s2d reveal" href="@/services/"><figure>{img("draper-covered-porch", "Covered porch built during an exterior remodel in Draper")}</figure><span class="folio">Exterior</span><b>Remodels, gutters &amp; copper caps</b></a>
</div></div></section>

<section class="sec cases-sec"><div class="wrap">
<div class="ed-head reveal"><p class="folio">Case files</p><h2>Three jobs, <em>three neighborhoods.</em></h2></div>
{cases}
</div></section>

<section class="sec quotes-sec"><div class="wrap">
<div class="ed-head reveal"><p class="folio">Letters</p><h2>In their <em>words.</em></h2></div>
<div class="letters">{"".join(f'<blockquote class="reveal"><p>{q}</p><footer><b>{n}</b><span>{w}</span></footer></blockquote>' for q, n, w in QUOTES)}</div>
</div></section>

<section class="sec faq-sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="folio">Roofing Q&amp;A</p><h2>Questions homeowners ask.</h2>{faq_html(HOME_FAQ)}<p class="more"><a class="tlink" href="@/roofing-q-a/">All roofing questions {ARROW}</a></p>
<a class="guide2" href="@/{p_blog.POST[1]}"><span class="folio">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal">{quote_form()}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company Salt Lake City | Salt City Roofers",
            "meta": "Salt City Roofers is a roofing company in Salt Lake City: asphalt shingle, synthetic slate and metal roofs, tear-offs and remodels, with written quotes.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def simple(key, path, label, h1, lede, tag, title, meta, image=None, alt="", intro="", extra="", skip=(), drop=DROP, crumbs=None, form=False, after=""):
    trail = [HOME] + (crumbs or []) + [(label, path)]
    content = (f'<p class="answer">{intro}</p>' if intro else "") + (mig(key, skip=skip + (h1, label), drop=drop) if key else "") + extra
    right = f'<div class="reveal">{quote_form()}</div>' if form else side()
    body = phero(trail, h1, lede, tag, image, alt) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">{content}</article>{right}</div></section>''' + after + ("" if form else cta())
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "og": image, "schema": [crumbs_ld(path, trail)]}


def pages_main():
    svc = [("Roofing services", "services/")]
    return [
        simple("services", "services/", "Services", "Roofing Services in Salt Lake City", "Steep-slope roofing, upgrades and remodeling, siding, gutters and chimney caps.", "Services",
               "Roofing Services in Salt Lake City | Salt City Roofers",
               "Roofing services in Salt Lake City: asphalt shingle, synthetic slate, shake, tile and metal roofs, roof conversions, siding, gutters and copper chimney caps.",
               image="two-story-home-roof", alt="Two-story home with a new roof",
               intro="Salt City Roofers offers roofing and exterior services in Salt Lake City and along the Wasatch Front: steep-slope roofing systems in asphalt shingle, synthetic slate, cedar shake, tile and metal; roof conversions, framing and remodeling; and soffit, fascia, aluminum gutters and copper chimney caps.",
               skip=("SERVICES", "Services")),
        simple("asphalt_shingle_systems", "asphalt-shingle-systems/", "Asphalt shingle systems", "Asphalt Shingle Roofing Systems in Salt Lake City", "The most widely used roof in the US, and the one we install most often.", "Steep slope",
               "Asphalt Shingle Roofs in Salt Lake City | Salt City Roofers",
               "Asphalt shingle roofing in Salt Lake City, installed as a complete system: decking, drip edge, underlayment, flashing, shingles and ventilation.",
               image="brick-home-new-roof", alt="Brick home with a new asphalt shingle roof",
               intro="Salt City Roofers installs asphalt shingle roofing systems on homes in Salt Lake City and across the Wasatch Front. We primarily install CertainTeed products as a complete system, following the manufacturer&rsquo;s installation specifications from the deck up.",
               extra=f'<h2>The system, layer by layer</h2><figure class="stackfig">{stack()}</figure>{legend()}', crumbs=svc),
        simple("slate_roofing_system", "slate-roofing-system/", "Synthetic slate", "Synthetic Slate Roofing in Salt Lake City", "The look of natural slate at a fraction of the weight.", "Steep slope",
               "Synthetic Slate Roofs in Salt Lake City | Salt City Roofers",
               "Synthetic slate roofing in Salt Lake City: CertainTeed Symphony composite slate, lighter than natural slate and Class 4 impact resistant, in three widths.",
               image="slate-roof-stone-home", alt="Slate-look roof on a stone home",
               intro="For Salt Lake City homes that want the look of slate without its weight, Salt City Roofers installs synthetic slate. Symphony&trade; from CertainTeed is an engineered polymer composite shingle that resembles natural slate, is lighter and shatter-resistant, and costs a fraction of the real thing.",
               skip=("Slate Roof Systems",), crumbs=svc),
        simple("roof_warranty_information", "roof-warranty-information/", "Warranty information", "Roof Warranty Information", "What the warranty packages cover, and how they transfer when you sell.", "Warranties",
               "Roof Warranty Information | Salt City Roofers, Utah",
               "Roof warranty information from Salt City Roofers in Salt Lake City: material and workmanship coverage, non-prorated and transferable options, and how to ask.",
               image="roof-vents-shingles", alt="Shingle roof with vents",
               intro="Every Salt City Roofers project in Salt Lake City comes with a labor and material warranty. Beyond that, extended manufacturer warranty packages can add non-prorated, transferable coverage, which is a selling point when you sell the home. Ask your estimator which package fits your roof.",
               crumbs=svc),
        simple("roofing_q_a", "roofing-q-a/", "Roofing Q&amp;A", "Roofing Q&amp;A", "Straight answers to the questions we hear most from Salt Lake City homeowners.", "Q&amp;A",
               "Roofing Questions and Answers | Salt City Roofers, SLC",
               "Roofing Q&A from Salt City Roofers in Salt Lake City: signs you need a new roof, how long it takes, materials for Utah, written bids, travel and cleanup.",
               skip=("Roofing Q & A",)),
        simple("about", "about/", "About", "About Salt City Roofers", "A Salt City Builders, Inc. company, roofing and remodeling in Utah since 2007.", "About",
               "About Salt City Roofers | Salt Lake City Roofers Since 2007",
               "About Salt City Roofers, a Salt City Builders, Inc. company: roofing and remodeling in Salt Lake City since 2007, led by Brock A. Horton and Asenath Horton.",
               image="chamber-ribbon-cutting", alt="The Salt City Roofers team at a chamber of commerce ribbon cutting",
               intro="Salt City Roofers, a Salt City Builders, Inc. company, is a roofing and general contracting company in Salt Lake City, in business since 2007. Brock A. Horton is CEO and project manager; Asenath Horton is the owner.",
               skip=("About Us",)),
        simple("contact", CONTACT, "Contact", "Contact Salt City Roofers", "Call, email, or send a message. We&rsquo;ll be in touch soon.", "Contact",
               "Contact Salt City Roofers | Roofing Quotes, Salt Lake City",
               "Contact Salt City Roofers in Salt Lake City: call 801-835-1868 or email SaltCityRoofers@gmail.com for a no-cost roofing inspection and a written quote.",
               intro=f"Call <a href=\"tel:{S['tel']}\">{S['phone']}</a> or email <a href=\"mailto:{S['email']}\">{S['email']}</a>. We work in Salt Lake City and along the Wasatch Front, usually within about 45 minutes, from Provo and Lehi to Park City and Ogden.",
               skip=("Salt City Roofers: Utah’s #1 Roofing Contractor",), form=True),
        simple("neighbors", "neighbors/", "Neighbors", "Hello, From Salt City Roofers", "A short introduction for our neighbors: what we do and how a quote works.", "Neighbors",
               "Hello, Neighbors | Salt City Roofers in Salt Lake City",
               "An introduction to Salt City Roofers for Salt Lake City neighbors: roof repair and installation, conversions, cold roofs, metal roofs and how a quote works.",
               image="draper-craftsman-remodel", alt="Craftsman-style home after an exterior remodel"),
        simple("employment", "employment/", "Employment", "Work With Salt City Roofers", "Roofing and construction jobs in Salt Lake City.", "Employment",
               "Employment | Salt City Roofers, Salt Lake City Roofing Jobs",
               "Employment at Salt City Roofers in Salt Lake City: we choose team members for their willingness to work hard and their construction background. Call to apply.",
               intro=f"Salt City Roofers chooses team members for their willingness to work hard and their background and training in construction. To ask about openings and get a job application, call <a href=\"tel:{S['tel']}\">{S['phone']}</a> or email <a href=\"mailto:{S['email']}\">{S['email']}</a>."),
        simple("do_your_best_consume_less_a_roofing_contractor_helps_clean_utah_air", "do-your-best-consume-less-a-roofing-contractor-helps-clean-utah-air/", "Do your best, consume less",
               "Do Your Best, Consume Less: A Roofing Contractor Helps Clean Utah Air", None, "News",
               "Do Your Best, Consume Less: Cleaner Utah Air | Salt City",
               "Salt City Roofers and the Do Your Best, Consume Less campaign: how a Salt Lake City roofing contractor took part in efforts to help clean Utah's air.", drop=POSTDROP),
    ]


def make_pages():
    p_blog.setup(phero, cta, side, ARROW, HOME, CONTACT, tidy, compare)
    out = [home()] + pages_main() + p_blog.pages() + [notfound()]
    return [_fit(dict(x, body=Q(x["body"]))) for x in out]


def _fit(pg):
    for add in (" No-cost inspection.", " Written quotes.", " Call 801-835-1868."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", "It may have been an old blog archive page. Try the blog, the services, or call us.", "404") + f'<section class="sec"><div class="wrap"><p><a class="tlink" href="@/roofing-blog/">Roofing blog {ARROW}</a> &nbsp; <a class="tlink" href="@/services/">Services {ARROW}</a></p></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Salt City Roofers", "meta": "This page was not found. See the Salt City Roofers roofing services and blog, or call 801-835-1868 for a no-cost roofing inspection in Salt Lake City, Utah.",
            "body": body, "robots": "noindex, follow", "sitemap": False}
