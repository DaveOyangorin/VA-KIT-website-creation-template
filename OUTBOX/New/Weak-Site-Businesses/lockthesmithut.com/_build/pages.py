"""Pages for the lockthesmithut.com redesign: "Brass & steel".

A locksmith sells one moment: the click when the pins line up and the lock turns. Lockthesmith's own logo is a key, and the site had no
real photos, so the design is drawn: graphite and brushed steel with brass for anything that opens, a heavy condensed grotesque like
stamped key blanks, and the signature pin-tumbler lock. Pick what you need, the five pins rise to the shear line, the plug turns, and
the matching service and how to reach them (mobile or storefront, open now or not, computed from their real hours) appear.
References (screenshotted 21 Oct 2026): Abloy / ASSA-style security branding (precise engineering drawings), Teenage Engineering
(technical type, spec readouts), Leica (black, brass-like restraint, one object on a dark ground).
Same 10 URLs and canonicals; the sample and leftover WordPress pages are noindex and point to the real content."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL, SERVICES, COUNTIES
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
TEL = "tel:+18014624094"


def telify(s):
    return re.sub(r'href="[^"]*#call"', f'href="{TEL}"', s)


def header():
    return telify(K.header())


def footer():
    return telify(K.footer())


def cta(title=None, text=None):
    return telify(K.cta(title, text))


SITS = [("car", "Locked out of my car", "Car Lockout Service", "Automotive locksmith help where your car is, with mobile service seven days a week.", "mobile"),
        ("home", "Locked out of my home", "Residential Lockout Service", "Residential lockouts, handled at your door by a mobile locksmith.", "mobile"),
        ("biz", "Locked out of my business", "Commercial Lockout Service", "Commercial lockouts and commercial locksmith solutions for offices and shops.", "mobile"),
        ("lost", "Lost my car key", "Lost Key Replacement", "Lost key replacement and car key duplication, including Chevy, Dodge, Honda, Lexus, Nissan and Toyota.", "mobile"),
        ("fob", "Need a key or fob programmed", "Key Programming", "Key programming and smart key programming for vehicles.", "either"),
        ("copy", "Need a spare key", "Key Duplication and Replacement", "Key duplication and replacement for home, business and car.", "either"),
        ("secure", "Want stronger locks", "High-Security Lock Setup", "High-security lock setup, lock upgrades and smart lock installation.", "either"),
        ("safe", "Safe won&rsquo;t open, or I need one", "Safe Installation and Repair", "Safe installation and repair.", "either")]
HOME_FAQ = [("What are your hours?", "<p>Our storefront at 2852 S Redwood Rd B14 in West Valley City is open Monday to Friday, 9 AM to 4 PM. Mobile service runs every day, Monday to Sunday, 8 AM to 8 PM, and we bring the work to your door.</p>"),
            ("Do you come to me?", "<p>Yes. Mobile locksmith service covers Salt Lake, Davis, Utah, Weber and Summit counties: lockouts, key replacements and lock installations where you are.</p>"),
            ("Which car keys can you replace?", "<p>Car key duplication, lost key replacement, key programming and smart key programming, including Chevy, Dodge, Honda, Lexus, Nissan and Toyota keys.</p>"),
            ("Is there a deal for new customers?", "<p>Our site offers a complimentary service call and savings for new customers. Ask when you call 801-462-4094.</p>")]


def keypath():
    cuts = [34, 52, 22, 46, 30]
    pts = [(14, 236), (118, 236), (118, 212)]
    for i, c in enumerate(cuts):
        x = 150 + i * 62; y = 150 + c
        pts += [(x - 22, 212 if i == 0 else pts[-1][1]), (x - 10, y), (x + 10, y), (x + 22, 212)]
    pts += [(436, 212), (452, 226), (452, 252), (14, 252)]
    return "M" + " L".join(f"{x} {y}" for x, y in pts) + " Z"


def lock_svg():
    pins = ""
    for i in range(5):
        x = 150 + i * 62
        cut = [34, 52, 22, 46, 30][i]
        pins += f'''<g class="pin" style="--drop:{cut}px"><rect class="spring" x="{x - 9}" y="20" width="18" height="44" rx="3"/><rect class="driver" x="{x - 11}" y="64" width="22" height="46" rx="4"/>
<rect class="keypin" x="{x - 11}" y="{110}" width="22" height="{40 + cut}" rx="4"/></g>'''
    return f'''<svg class="lock" viewBox="0 0 560 320" role="img" aria-label="A pin-tumbler lock: when the right key is in, the pins line up at the shear line and the plug turns">
<defs><linearGradient id="brass" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#e3c46a"/><stop offset="1" stop-color="#a8822a"/></linearGradient>
<linearGradient id="steel" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4a525c"/><stop offset="1" stop-color="#262b31"/></linearGradient></defs>
<rect class="housing" x="90" y="10" width="380" height="290" rx="22"/>
<g class="plug-g"><circle class="plug" cx="280" cy="210" r="0"/><rect class="plugbar" x="110" y="110" width="340" height="140" rx="14"/><line class="shear" x1="100" x2="460" y1="110" y2="110"/></g>
{pins}
<path class="key" d="{keypath()}"/><circle class="keybow" cx="-6" cy="222" r="0"/>
<text class="shear-l" x="104" y="102">SHEAR LINE</text></svg>'''


def home():
    sits = "".join(f'<button type="button" class="sit{" on" if i == 0 else ""}" data-sit="{k}" aria-pressed="{"true" if i == 0 else "false"}">{t}</button>' for i, (k, t, s, d, w) in enumerate(SITS))
    outs = "".join(f'<div class="lk-out{" on" if i == 0 else ""}" data-out="{k}"><p class="lk-k">Unlocked &middot; <b data-mode="{w}"></b></p><h3>{s}</h3><p>{d}</p></div>' for i, (k, t, s, d, w) in enumerate(SITS))
    svc = "".join(f'<div class="sv reveal"><h3>{g}</h3><ul>{"".join(f"<li>{x}</li>" for x in ss)}</ul></div>' for g, ss in SERVICES)
    areas = "".join(f'<div class="ar-c reveal"><h3>{c}</h3><p>{" &middot; ".join(t)}</p></div>' for c, t in COUNTIES)
    body = f'''
<section class="k-hero"><div class="kh-img" data-parallax="0.08">{img("lk-carlock", "A locksmith working on a car door lock", priority=True)}</div><div class="wrap k-hero-in">
<div class="k-hero-txt"><p class="label"><span class="live" data-live-dot></span><span data-live-txt>Mobile service &middot; Mon&ndash;Sun 8 AM&ndash;8 PM</span></p>
<h1>Locksmith in West Valley City <span>and across the Salt Lake area.</span></h1>
<p class="lede">Lockthesmith offers mobile emergency locksmith service, including lockouts, key replacements and high-security lock installations, from a storefront on Redwood Road. Call 801-462-4094 for fast, reliable help when you need it most.</p>
<div class="btn-row"><a class="btn accent" href="{TEL}">{PHONE} Call 801-462-4094</a><a class="btn ghost" href="#lock">What do you need? {ARROW}</a></div></div>
<div class="k-badge" aria-hidden="true">{img("lk-logo", "", lazy=False)}</div>
</div><p class="credit">Atmosphere photo: Maxime Rossignol, CC0, via Wikimedia Commons</p>
<div class="k-strip"><div class="wrap"><span><b>Storefront</b> Mon&ndash;Fri 9 AM&ndash;4 PM</span><span><b>Mobile</b> Mon&ndash;Sun 8 AM&ndash;8 PM</span><span><b>Address</b> 2852 S Redwood Rd B14, West Valley City</span><span><b>New customers</b> Complimentary service call</span></div></div></section>

<section class="sec k-lock" id="lock"><div class="wrap">
<div class="k-head reveal"><p class="label">How can we help?</p><h2>Pick your problem. <span>We&rsquo;ll turn the key.</span></h2></div>
<div class="lk" data-lock><div class="lk-sits" role="group" aria-label="What do you need?">{sits}</div>
<div class="lk-stage"><div class="lk-svg">{lock_svg()}</div><div class="lk-outs" aria-live="polite">{outs}
<div class="lk-cta"><a class="btn accent" href="{TEL}">{PHONE} 801-462-4094</a><span class="lk-hours" data-hours-note></span></div></div></div></div>
</div></section>

<section class="sec k-svc" id="services"><div class="wrap">
<div class="k-head split-h reveal"><div><p class="label">Services</p><h2>The full ring <span>of keys.</span></h2></div><p class="lede">Residential, commercial and automotive locksmith work, following industry best practice and recommendations from organizations like the Associated Locksmiths of America.</p></div>
<div class="sv-photos"><figure>{img("lk-smartlock", "A smart lock on a door, controlled from a phone")}<figcaption>Smart lock installation &middot; <span class="credit-in">Photo: Sebastian Scholz (Nuki), CC BY-SA 4.0, via Wikimedia Commons</span></figcaption></figure><figure>{img("lk-antique", "An antique rim lock with its key")}<figcaption>Locks old and new &middot; <span class="credit-in">Photo: Amherst College Museum, CC BY 4.0, via Wikimedia Commons</span></figcaption></figure></div>
<div class="sv-grid">{svc}</div>
</div></section>

<section class="sec k-hours" id="hours"><div class="wrap k-hours-in">
<div class="reveal"><p class="label">Hours</p><h2>Two ways to reach us.</h2><p>Our shop is open Monday to Friday, 9 AM to 4 PM. Mobile service runs every day from 8 AM to 8 PM, so we bring the work to your door when you need it.</p></div>
<div class="hrs reveal" data-hours><div class="hr" data-h="store"><small>Storefront</small><b>Mon&ndash;Fri &middot; 9 AM&ndash;4 PM</b><span class="st" data-st>&nbsp;</span><p>2852 S Redwood Rd B14, West Valley City, UT 84119</p></div>
<div class="hr" data-h="mobile"><small>Mobile service</small><b>Mon&ndash;Sun &middot; 8 AM&ndash;8 PM</b><span class="st" data-st>&nbsp;</span><p>Lockouts, keys and lock installs where you are</p></div></div>
</div></section>

<section class="sec k-why"><div class="wrap">
<div class="k-head reveal"><p class="label">Why Lockthesmith</p><h2>Built around <span>getting you back in.</span></h2></div>
<div class="why3"><div class="reveal"><span>01</span><h3>Rapid response</h3><p>Lock problems happen at the worst times. We work to reach you promptly, whether it&rsquo;s an emergency lockout, key duplication or a security upgrade.</p></div>
<div class="reveal"><span>02</span><h3>Modern security</h3><p>From high-security locks to smart lock systems, our locksmiths carry the tools to handle locks old and new.</p></div>
<div class="reveal"><span>03</span><h3>Trained technicians</h3><p>Our technicians keep up with current industry standards and techniques, and bring that to every job.</p></div></div>
</div></section>

<section class="sec k-areas" id="areas"><div class="wrap">
<div class="k-head split-h reveal"><div><p class="label">Areas we serve</p><h2>Five counties, <span>44 towns.</span></h2></div><p class="lede">Mobile locksmith service from West Valley City to Ogden, Park City and Spanish Fork.</p></div>
<div class="ar-grid">{areas}</div>
</div></section>

<section class="sec k-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal"><a class="post-card k-post" href="@/{p_blog.SLUG}"><span class="label">Safety</span><b>{p_blog.H1}</b><p>Utah has had two child hot-car deaths this year. What to do in the first minutes, and how to keep it from happening.</p><em>Read it {ARROW}</em></a>
<div class="k-mail"><p class="label">Email</p><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Locksmith West Valley City, UT | Lockthesmith Mobile Service",
            "meta": "Lockthesmith: mobile locksmith in West Valley City and the Salt Lake area. Lockouts, car key replacement and programming, high-security locks. 801-462-4094.",
            "body": body, "body_class": "is-home", "og": "lk-logo", "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def make_pages():
    out = [home()]
    about = f'''<p class="answer">Lockthesmith is a locksmith with a storefront in West Valley City and mobile service across the Salt Lake area. We offer mobile emergency locksmith services, including lockouts, key replacements and high-security lock installations.</p>
<p>We understand the stress of being locked out or needing a lock replaced. That&rsquo;s why our team provides professional locksmith services in West Valley City and the Salt Lake City area, including Sandy, Draper, Cottonwood Heights and more. Whether it&rsquo;s a broken lock or a new security system, we&rsquo;re here to help.</p>
<h2>Storefront and mobile</h2><p>Our shop operates Monday to Friday from 9 AM to 4 PM, and our mobile service runs daily from 8 AM to 8 PM, so we bring the work directly to your door when you need it most.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="{TEL}">801-462-4094</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Storefront</dt><dd><address>2852 S Redwood Rd B14<br>West Valley City, UT 84119</address></dd></div></dl>
<h2>What we do</h2><ul class="chips">{"".join(f"<li>{s}</li>" for g, ss in SERVICES[:4] for s in ss)}</ul>'''
    out.append(K.page("about/", "About", "About Lockthesmith", "Storefront in West Valley City. Mobile service across the Salt Lake area.", "About", "About Lockthesmith | Locksmith in West Valley City, Utah",
                      "About Lockthesmith: a West Valley City locksmith with a Redwood Road storefront and daily mobile service for lockouts, keys and high-security locks.",
                      about, art=f'<div class="ph-key">{img("lk-logo", "Lockthesmith logo", lazy=False)}</div>', canonical=EXT["about"]["canon"]))
    leftover = '<p class="answer">This page isn&rsquo;t used anymore. You&rsquo;re probably looking for Lockthesmith&rsquo;s locksmith services in West Valley City and the Salt Lake area.</p>' + \
               f'<p><a class="tlink" href="@/">Go to the home page {ARROW}</a> &nbsp; <a class="tlink" href="@/about/">About Lockthesmith {ARROW}</a></p>'
    for k in EXT:
        if k in ("home", "about"): continue
        p = EXT[k]["url"].split(".com/", 1)[1]
        out.append(K.page(p, "Lockthesmith", "Lockthesmith", "", "Lockthesmith", "Lockthesmith | Locksmith in West Valley City, UT",
                          "This page is no longer used. Lockthesmith offers mobile and storefront locksmith service in West Valley City and across the Salt Lake area.",
                          leftover, canonical=EXT[k]["canon"], robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("About", "about/"))))
    return [dict(x, body=Q(telify(x["body"]))) for x in out]
