"""Pages for the anyandallservices.com redesign: "Breaker panel".

Any & All Electric became Any & All Services, and the site now says what they do in one line: "Need an electrician, not a salesman?" They
connect Utah homeowners with trusted local electricians and handle the shopping around. So the page is direct, black and red like their
hexagon logo, and opens on Salt Lake City lit up at night (credited Commons photo; they have no photos of their own). The signature is the
breaker panel: flip a breaker for each part of your project (lighting, outlets, panel, EV charger, troubleshooting, HVAC...) and the
switch lights amber while the panel writes your project description straight into their estimate form, the one thing the site asks for.
Oswald, Inter, Share Tech Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 6 URLs (www, no trailing slash) plus one new post. The four legal pages are unedited Wix templates: kept, noindex."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

# project categories for describing the job (not a list of guaranteed services: see notes)
BREAKERS = [("light", "Lighting", "lighting (new fixtures, replacements or dimmers)"), ("fan", "Ceiling fans", "ceiling fan installation or replacement"), ("outlet", "Outlets &amp; switches", "outlets or switches (adding, moving or replacing)"),
            ("panel", "Panel / breakers", "the electrical panel or breakers (trips, upgrade, inspection)"), ("ev", "EV charger", "an EV charger"), ("trouble", "Troubleshooting", "troubleshooting a problem (flickering, warm outlets, dead circuits)"),
            ("remodel", "Remodel / addition", "wiring for a remodel or addition"), ("hvac", "Heating &amp; cooling", "heating or cooling (HVAC)")]


def panel():
    brk = "".join(f'''<button type="button" class="brk" data-b="{k}" data-t="{html.escape(html.unescape(t))}" aria-pressed="false"><span class="brk-n">{i + 1:02d}</span><span class="brk-sw" aria-hidden="true"><i></i></span><span class="brk-l">{l}</span></button>''' for i, (k, l, t) in enumerate(BREAKERS))
    return f'''<div class="pnl" data-pnl>
<div class="pnl-box"><div class="pnl-top"><span class="mono">MAIN &middot; YOUR PROJECT</span><span class="pnl-bulb" data-pnl-bulb aria-hidden="true"></span></div>
<div class="pnl-grid" role="group" aria-label="Project parts">{brk}</div>
<p class="pnl-foot mono" data-pnl-count>0 circuits on</p></div>
<div class="pnl-out"><p class="label">Your project, in one line</p><p class="pnl-line" data-pnl-line aria-live="polite">Flip a breaker for each part of the job.</p>
<label class="pnl-l">Anything else? (optional)<input type="text" data-pnl-extra placeholder="e.g. 1970s home, panel is in the garage"></label>
<a class="btn accent" href="#estimate" data-pnl-go>Put this in my estimate request {ARROW}</a>
<p class="small">This only fills in the estimate form below. Nothing is sent from this page.</p></div>
</div>'''


STEPS = [("01", "Tell us about the project", "Use the breaker panel or the estimate form: what you need, where, and anything we should know."),
         ("02", "We do the shopping around", "With over 14 years of local electrical experience, we know how to help you find the right professional for your project."),
         ("03", "Move forward with confidence", "You get connected with a trusted local electrician, without the sales pitch.")]
FAQ = [("Are you the same company as Any &amp; All Electric?", "<p>Yes. Any &amp; All Electric is now Any &amp; All Services.</p>"),
       ("Do you do the electrical work yourselves?", "<p>We connect Utah homeowners with trusted local electricians. We handle the shopping around, saving you time and helping you find the right professional for your project.</p>"),
       ("Can I get an estimate for HVAC too?", "<p>Yes. You can request an estimate for electrical and HVAC projects.</p>"),
       ("Where do you work?", "<p>Salt Lake and Utah Counties.</p>")]


SIGNS = ["Frequent problems with blowing fuses or tripping circuit breakers", "A tingling feeling when you touch an electrical appliance", "Discolored or warm wall outlets",
         "A burning or rubbery smell coming from an appliance", "Flickering or dimming lights", "Sparks from an outlet"]


def home():
    form = K.form("Request an estimate", fields=[("address", "Address *")], msg_label="Please describe the project you would like an estimate for *")
    body = f'''
<section class="x-hero"><div class="xh-img" data-parallax="0.08">{img("aa-night", "Salt Lake City lit up at night, seen from the foothills", priority=True)}</div>
<div class="wrap xh-in"><div class="xh-txt"><p class="label">Salt Lake &amp; Utah Counties &middot; Formerly Any &amp; All Electric</p>
<h1>Need an electrician in Salt Lake City, <em>not a salesman?</em></h1>
<p class="lede">At Any &amp; All Services we connect Salt Lake City and Utah homeowners with trusted local electricians. With over 14 years of local electrical experience, we know how to help you find the right professional for your project, and we handle the shopping around.</p>
<div class="btn-row"><a class="btn accent" href="#estimate">Request an estimate {ARROW}</a><a class="btn ghost" href="tel:+18017179125">{PHONE} 801-717-9125</a></div></div></div>
<p class="credit">Salt Lake City &middot; 888emmanuelc888, CC BY 4.0, via Wikimedia Commons</p></section>

<section class="sec x-how" id="how"><div class="wrap">
<div class="x-head reveal"><p class="label">How it works</p><h2>Three steps. <em>No sales pitch.</em></h2></div>
<div class="steps3">{"".join(f'<div class="st3 reveal"><span class="mono">{n}</span><h3>{t}</h3><p>{d}</p></div>' for n, t, d in STEPS)}</div>
</div></section>

<section class="sec x-signs"><div class="wrap">
<div class="x-head split-h reveal"><div><p class="label">When to call</p><h2>Six signs <em>not to ignore.</em></h2></div><p class="lede">From the National Fire Protection Association&rsquo;s electrical safety tip sheet: call a qualified electrician if you have any of these.</p></div>
<div class="signs">{"".join(f'<div class="sg reveal"><span class="mono">{i + 1:02d}</span><p>{s}</p></div>' for i, s in enumerate(SIGNS))}</div>
<p class="small">Source: NFPA Electrical Safety tip sheet. More in our post on <a href="@/{p_blog.SLUG}">signs you need an electrician</a>.</p>
</div></section>

<section class="sec x-panel" id="panel"><div class="wrap">
<div class="x-head split-h reveal"><div><p class="label">Your project</p><h2>Flip the breakers <em>for your job.</em></h2></div><p class="lede">Every part you switch on lights up and goes into your project description. Then send it with the estimate form.</p></div>
{panel()}
</div></section>

<section class="sec x-est" id="estimate"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Request an estimate</p><h2>Electrical or HVAC, <em>tell us the job.</em></h2>
<p class="lede">Fill in the form, or call <a href="tel:+18017179125">801-717-9125</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18017179125">801-717-9125</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Serving</dt><dd>Salt Lake &amp; Utah Counties</dd></div></dl>
<p class="small">New or returning customer? Mention it in the description.</p></div>
<div class="reveal form-col">{form}</div>
</div></section>

<section class="sec x-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card x-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>NFPA&rsquo;s warning signs and UL&rsquo;s advice: flickering lights, warm outlets, buzzing, tripping breakers.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Electrician Salt Lake City | Trusted Local Pros | Any &amp; All",
            "meta": "Need an electrician in Salt Lake City, not a salesman? Any & All Services connects Utah homeowners with trusted local electricians. Request an estimate.",
            "body": body, "body_class": "is-home", "og": "aa-night", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


LEGAL = [("blank-1/", "blank_1", "Accessibility Statement"), ("blank-2/", "blank_2", "Terms &amp; Conditions"), ("blank-3/", "blank_3", "Refund Policy"), ("blank/", "blank", "Privacy Policy")]


def make_pages():
    out = [home()]
    for path, key, h1 in LEGAL:
        body = f'<p class="answer">This page is being updated. For questions about our {h1.lower()}, email <a href="mailto:{EMAIL}">{EMAIL}</a> or call 801-717-9125.</p>'
        out.append(K.page(path, h1, h1, "Any &amp; All Services", "Legal", f"{h1} | Any &amp; All Services, Salt Lake City, Utah",
                          f"{html.unescape(h1)} for Any & All Services (formerly Any & All Electric), Salt Lake and Utah Counties. Questions? Email office@anyandallservices.com.",
                          body, canonical=EXT[key]["canon"], robots="noindex, follow", sitemap=False))
    out.append(K.page("book-online/", "Book online", "Book online", "Request an estimate instead.", "Booking", "Book Online | Any &amp; All Services, Salt Lake City, Utah",
                      "Online booking isn't open right now. Request an estimate from Any & All Services for electrical or HVAC work, or call 801-717-9125 in Salt Lake City.",
                      f'<p class="answer">Nothing to book right now. Please request an estimate instead.</p><p><a class="btn" href="@/#estimate">Request an estimate {ARROW}</a></p>',
                      canonical=EXT["book_online"]["canon"], robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Request an estimate", "#estimate"), ("Blog", p_blog.SLUG))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-717-9125.", " Salt Lake City, UT.")) for x in out]
