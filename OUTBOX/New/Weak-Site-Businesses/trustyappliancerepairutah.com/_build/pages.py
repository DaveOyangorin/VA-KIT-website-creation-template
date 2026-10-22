"""Pages for the trustyappliancerepairutah.com redesign: "Control panel".

An appliance repairer lives in front of control panels: dials, buttons and LED read-outs. So the home page opens on a full-bleed kitchen photo
with their 90-day warranty and licensed-and-insured promise up front, and the signature is a control panel: turn the dial to your appliance and
the amber read-out shows the problems they fix on it (from their own service descriptions) and a "try this first" tip from their own
maintenance articles, with one button to book. Graphite and the safety orange of their logo, Chakra Petch for the panel lettering.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 11 URLs (trailing slash) and canonicals, including the six tip posts."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta
BRANDS = ["Cove", "Crosley", "Electrolux", "Estate", "Jenn-Air", "Kenmore", "Kirkland Signature", "Magic Chef", "Maytag", "Sub-Zero", "Viking", "InSinkErator", "Thermador", "Whirlpool"]
POSTS = [("refrigerator-maintenance-tips/", "refrigerator_maintenance_tips", "Refrigerator"), ("dryer-maintenance-tips/", "dryer_maintenance_tips", "Dryer"),
         ("washing-machine-tips/", "washing_machine_tips", "Washing machine"), ("dishwasher-maintenance-tips/", "dishwasher_maintenance_tips", "Dishwasher"),
         ("range-maintenance-tips/", "range_maintenance_tips", "Range"), ("microwave-maintenance-tips/", "microwave_maintenance_tips", "Microwave")]


def article(key):
    """[(h2, paragraph)] from one of their tip posts, as published."""
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8", errors="ignore").read()
    s = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", s)
    blocks = [(t, re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", x))).strip()) for t, x in re.findall(r"(?s)<(h2|h3|p|li)\b[^>]*>(.*?)</\1>", s)]
    start = next(i for i, (t, x) in enumerate(blocks) if t == "h2" and ":" in x and len(x) > 20)
    out, title = [], blocks[start][1]
    for t, x in blocks[start + 1:]:
        if not x or x.startswith(("Connect With Us", "Contact Us", "Related", "Leave a")):
            if out: break
            continue
        if x in ("Read More",): continue
        out.append((t, x))
    return title, out


ART = {k: article(k) for p, k, n in POSTS}


def tips(key, n=3):
    t, b = ART[key]
    pairs = []
    for i, (tag, x) in enumerate(b):
        if tag == "h2" and i + 1 < len(b) and b[i + 1][0] == "p":
            pairs.append((x.rstrip(":"), b[i + 1][1]))
    return pairs[:n]


SV = EXT["services"]["text"]


def svc_par(start, stop):
    a = SV.find(start); b = SV.find(stop, a + 10) if stop else len(SV)
    t = SV[a + len(start):b].replace("Contact Us", "").replace("Connect With Us", "").strip()
    return t


APPS = [("refrigerator", "Refrigerator", "REFRIGERATOR REPAIR", "WASHING MACHINE REPAIR", "temperature inconsistencies to unusual noises", "refrigerator_maintenance_tips"),
        ("dryer", "Dryer", "DRYER REPAIR", "GARBAGE DISPOSAL REPAIR", "overheating to ineffective drying", "dryer_maintenance_tips"),
        ("washer", "Washer", "WASHING MACHINE REPAIR", "Oven Repair", "diagnosing issues with precision, genuine parts", "washing_machine_tips"),
        ("dishwasher", "Dishwasher", "DISHWASHER REPAIR", "DRYER REPAIR", "leaks to poor cleaning performance", "dishwasher_maintenance_tips"),
        ("oven", "Oven &amp; range", "Oven Repair", "Range Repair", "precise diagnostics and factory replacement parts", "range_maintenance_tips"),
        ("microwave", "Microwave", "MICROWAVE REPAIR", "REFRIGERATOR REPAIR", "heating problems to electrical glitches", "microwave_maintenance_tips"),
        ("disposal", "Disposal", "GARBAGE DISPOSAL REPAIR", "MICROWAVE REPAIR", "jamming to unusual noises", None)]
FAQ = [("Do you offer a warranty?", "<p>Yes. We offer a 90-day warranty on all repairs, and we&rsquo;re licensed and insured.</p>"),
       ("Which brands do you work on?", "<p>Some of the brands we work on: " + ", ".join(BRANDS) + ".</p>"),
       ("What appliances do you repair?", "<p>Refrigerators, dryers, washing machines, dishwashers, ovens, ranges, microwaves and garbage disposals.</p>"),
       ("Do you use genuine parts?", "<p>Yes. We use genuine parts and industry-best practices, so repairs are effective and enduring.</p>")]


def panel():
    knob = "".join(f'<button type="button" class="kn" data-app="{k}" aria-pressed="{"true" if i == 0 else "false"}" style="--i:{i}"><span>{n}</span></button>' for i, (k, n, *_r) in enumerate(APPS))
    reads = ""
    for i, (k, n, a, b, issue, art) in enumerate(APPS):
        tp = tips(art, 1) if art else []
        tip = f'<p class="rd-tip"><b>Try this first:</b> {html.escape(tp[0][0])}. {html.escape(tp[0][1].split(". ")[0])}.</p>' if tp else '<p class="rd-tip"><b>Good to know:</b> we bring genuine parts and give you an honest assessment before any work.</p>'
        link = next((p for p, kk, nn in POSTS if kk == art), None)
        reads += f'''<div class="rd" data-read="{k}"{"" if i == 0 else " hidden"}><p class="rd-l">{n.upper()} &middot; REPAIR</p>
<p class="rd-main">{"From " + issue + "." if issue[0].islower() and " to " in issue else issue[0].upper() + issue[1:] + "."}</p>{tip}
<p class="rd-links"><a href="@/services/#{k}">{re.sub("&amp;", "&", n)} repair {ARROW}</a>{f' <a href="@/{link}">All {n.lower()} tips {ARROW}</a>' if link else ""}</p></div>'''
    return f'''<div class="cp" data-panel><div class="cp-face"><div class="cp-dial" role="group" aria-label="Choose your appliance">{knob}<div class="cp-hub" aria-hidden="true"><i data-needle></i></div></div>
<div class="cp-screen" aria-live="polite">{reads}</div></div>
<div class="cp-foot"><span class="led on" aria-hidden="true"></span><span>Licensed &amp; insured</span><span class="led on" aria-hidden="true"></span><span>90-day warranty on all repairs</span><a class="btn accent" href="@/contact-us/">Schedule a repair {ARROW}</a></div></div>'''


def home():
    body = f'''
<section class="t-hero"><div class="th-img" data-parallax="0.08">{img("tr-kitchen", "A modern white kitchen with a built-in oven, cooktop and dining table", priority=True)}</div>
<div class="wrap th-in"><div class="th-txt"><p class="label">Sandy, Utah &middot; Licensed &amp; insured</p>
<h1>Appliance repair in Sandy, <em>done honestly.</em></h1>
<p class="lede">Trusty Appliance Repair restores your refrigerator, washer, dryer, dishwasher, oven and more, swiftly and professionally, with genuine parts, transparent pricing and a 90-day warranty on every repair.</p>
<div class="btn-row"><a class="btn accent" href="@/contact-us/">Schedule an appointment {ARROW}</a><a class="btn ghost" href="tel:+18012559063">{PHONE} (801) 255-9063</a></div></div>
<div class="th-badge"><b>90</b><span>day warranty<br>on all repairs</span></div></div>
<p class="credit">Kitchen photo &middot; Shixart1985, CC BY 2.0, via Wikimedia Commons</p></section>

<section class="t-strip"><div class="wrap strip">{"".join(f"<span>{b}</span>" for b in BRANDS)}</div></section>

<section class="sec t-panel" id="panel"><div class="wrap">
<div class="t-head split-h reveal"><div><p class="label">Turn the dial</p><h2>What&rsquo;s your appliance <em>doing?</em></h2></div><p class="lede">Pick the appliance. The read-out shows what we fix on it and one thing to try before you call.</p></div>
{panel()}
</div></section>

<section class="sec t-int"><div class="wrap t-int-in">
<figure class="reveal">{img("tr-laundry", "A front-load washer and dryer side by side in a laundry room")}<figcaption>Laundry room &middot; Infrogmation of New Orleans, CC BY 2.0, via Wikimedia Commons</figcaption></figure>
<div class="reveal"><p class="label">Our integrity</p><h2>An honest assessment. <em>No surprises.</em></h2>
<p>From the moment you reach out, expect a genuine, forthright experience. Our technicians approach each repair with dedication to accuracy: an honest assessment of your appliance&rsquo;s condition, transparent pricing that leaves no room for surprises, and repairs that stand the test of time.</p>
<ul class="ticks"><li>Genuine parts and industry-best practices</li><li>Timely service that respects your schedule</li><li>If we make a mistake, we fix it promptly</li><li>90-day warranty on all repairs</li></ul>
<a class="tlink" href="@/about-us/">About us {ARROW}</a></div>
</div></section>

<section class="sec t-svc"><div class="wrap">
<div class="t-head reveal"><p class="label">Repairs</p><h2>Seven appliances. <em>One trusted team.</em></h2></div>
<div class="svc7">{"".join(f'<a class="sv reveal" href="@/services/#{k}"><span class="sv-n">{i + 1:02d}</span><b>{n} repair</b><p>{"From " + iss if " to " in iss else iss[0].upper() + iss[1:]}.</p></a>' for i, (k, n, a, b, iss, art) in enumerate(APPS))}</div>
</div></section>

<section class="t-band"><div class="band-img" data-parallax="0.1">{img("tr-steel", "Brushed stainless steel door of a refrigerator")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our mission</p><p>To restore the functionality of your appliances swiftly, efficiently, and with the utmost professionalism.</p></blockquote></div>
<p class="credit">Refrigerator door &middot; Tony Webster, CC BY 2.0, via Wikimedia Commons</p></section>

<section class="sec t-tips"><div class="wrap">
<div class="t-head split-h reveal"><div><p class="label">Maintenance tips</p><h2>Make it <em>last longer.</em></h2></div><a class="tlink" href="@/blogs/">All tips {ARROW}</a></div>
<div class="tips">{"".join(f'<a class="tp reveal" href="@/{p}"><span>{n}</span><b>{html.escape(ART[k][0])}</b><em>Read {ARROW}</em></a>' for p, k, n in POSTS)}</div></div></section>

<section class="sec t-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Before you <em>call.</em></h2>
<a class="post-card t-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>The temperatures FDA recommends, why an appliance thermometer matters, and what to keep or toss after an outage.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": EXT["home"]["canon"] or U, "title": "Appliance Repair Sandy, UT | Trusty Appliance Repair",
            "meta": "Appliance repair in Sandy, UT: refrigerators, washers, dryers, dishwashers, ovens and more. Licensed and insured, genuine parts, 90-day warranty on all repairs.",
            "body": body, "body_class": "is-home", "og": "tr-kitchen", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    secs = ""
    for k, n, a, b, iss, art in APPS:
        t = svc_par(a, b)
        sents = re.split(r"(?<=[.!?])\s+", t)
        tp = tips(art, 2) if art else []
        secs += f'<h2 id="{k}">{n} repair</h2>' + "".join(f"<p>{html.escape(' '.join(sents[j:j + 3]))}</p>" for j in range(0, len(sents), 3))
        if tp:
            secs += '<div class="tipbox"><p class="label">From our tips</p><ul>' + "".join(f"<li><b>{html.escape(h)}.</b> {html.escape(p.split('. ')[0])}.</li>" for h, p in tp) + "</ul></div>"
    sv = '<p class="answer">We repair refrigerators, dryers, washing machines, dishwashers, ovens, ranges, microwaves and garbage disposals in Sandy and nearby, with genuine parts and a 90-day warranty on all repairs.</p>' + secs + \
         "<h2>Brands we work on</h2><ul class=\"states\">" + "".join(f"<li>{b}</li>" for b in BRANDS) + "</ul>"
    out.append(K.page("services/", "Services", "Appliance Repair Services", "Seven appliances, one trusted team.", "Repairs", "Appliance Repair Services in Sandy, UT | Trusty Appliance",
                      "Refrigerator, dryer, washer, dishwasher, oven, range, microwave and garbage disposal repair in Sandy, UT. Genuine parts and a 90-day warranty on repairs.",
                      sv, image="tr-laundry", alt="A washer and dryer in a laundry room", canonical=EXT["services"]["canon"], faqs=FAQ,
                      schema=K.svc_schema("services/", "Appliance repair", "Sandy, UT")))
    ab = '''<p class="answer">Our mission is to restore the functionality of your appliances swiftly, efficiently, and with the utmost professionalism.</p>
<p>We understand the importance of well-functioning appliances in your daily life, and our commitment is to ensure that you can trust us to deliver top-notch repair solutions. With a focus on integrity, transparency and technical expertise, we aim to exceed your expectations and build lasting relationships.</p>
<h2>Our integrity</h2><p>Our integrity is not just a business practice; it&rsquo;s a guiding philosophy that influences every decision we make. We take pride in using only genuine parts and industry-best practices, so the repairs we perform are effective and enduring. Our timeliness reflects our respect for your time.</p>
<p>In the event that an error occurs, we hold ourselves accountable and rectify any mistakes promptly and without hesitation. We believe in open communication, active listening, and a willingness to learn and improve.</p>
<h2>Beyond repairs</h2><p>We are active members of the communities we serve, and our commitment to integrity drives us to be environmentally conscious and socially responsible. We understand that integrity is earned, not claimed.</p>
<ul class="ticks"><li>Licensed and insured</li><li>90-day warranty on all repairs</li><li>Genuine parts</li></ul>'''
    out.append(K.page("about-us/", "About", "About Trusty Appliance Repair", "Integrity, transparency, technical expertise.", "About", "About Trusty Appliance Repair | Sandy, Utah Appliance Repair",
                      "Trusty Appliance Repair in Sandy restores appliances swiftly and professionally, with genuine parts, honest assessments and a 90-day warranty on repairs.",
                      ab, image="tr-steel", alt="A stainless steel refrigerator door", canonical=EXT["about_us"]["canon"]))
    con = f'''<p class="answer">Get in touch to schedule an appointment. We are licensed and insured, and we offer a 90-day warranty on all repairs.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18012559063">(801) 255-9063</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Address</dt><dd><address>8223 S 1000 E<br>Sandy, UT 84094</address></dd></div></dl>'''
    out.append(K.page("contact-us/", "Contact", "Contact Trusty Appliance Repair", "Licensed, insured, 90-day warranty.", "Contact", "Contact Trusty Appliance Repair | Sandy, UT (801) 255-9063",
                      "Contact Trusty Appliance Repair in Sandy: call (801) 255-9063 or email to schedule an appliance repair today. Licensed and insured, 90-day repair warranty.",
                      con, canonical=EXT["contact_us"]["canon"], form_side=True))
    bl = '<div class="tips">' + f'<a class="tp" href="@/{p_blog.SLUG}"><span>Refrigerator &middot; Food safety</span><b>{p_blog.H1}</b><em>Read {ARROW}</em></a>' + \
         "".join(f'<a class="tp" href="@/{p}"><span>{n}</span><b>{html.escape(ART[k][0])}</b><em>Read {ARROW}</em></a>' for p, k, n in POSTS) + "</div>"
    out.append(K.page("blogs/", "Tips", "Appliance Maintenance Tips", "Make your appliances last longer.", "Blog", "Appliance Maintenance Tips | Trusty Appliance Repair, Sandy",
                      "Appliance maintenance tips from Trusty Appliance Repair in Sandy: refrigerators, washers, dryers, dishwashers, ranges and microwaves, plus fridge food safety.",
                      bl, canonical=EXT["blogs"]["canon"]))
    for p, k, n in POSTS:
        t, b = ART[k]
        body, ul = [], []
        for tag, x in b:
            if tag == "li": ul.append(x); continue
            if ul: body.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>"); ul = []
            body.append(f"<h2>{html.escape(x.rstrip(':'))}</h2>" if tag in ("h2", "h3") else f"<p>{html.escape(x)}</p>")
        if ul: body.append("<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in ul) + "</ul>")
        first = next(x for tag, x in b if tag == "p")
        meta = first[:157].rsplit(" ", 1)[0] + "..." if len(first) > 160 else first
        title = f"{n} Maintenance Tips | Trusty Appliance" + (" Repair, Sandy" if len(n) <= 9 else ", Sandy")
        import datetime
        dm = re.search(r"ramiz (\w+ \d+, \d{4})", EXT[k]["text"])
        dt = datetime.datetime.strptime(dm.group(1), "%B %d, %Y").date() if dm else datetime.date(2023, 9, 2)
        dp, dl = dt.isoformat(), dt.strftime("%b %d, %Y").replace(" 0", " ")
        out.append(K.page(p, f"{n} tips", html.escape(t), f"From the blog &middot; {dl}", "Blog", title, html.escape(meta), "\n".join(body) +
                          f'<p>Need a hand? Call <a href="tel:+18012559063">(801) 255-9063</a> or <a href=@/contact-us/>schedule a repair</a>. 90-day warranty on all repairs.</p>',
                          crumbs=[("Tips", "blogs/")], canonical=EXT[k]["canon"], ogtype="article",
                          schema=[{"@type": "BlogPosting", "headline": t, "datePublished": dp, "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": EXT[k]["canon"]}]))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Repairs", "services/"), ("Tips", "blogs/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (801) 255-9063.", " 90-day warranty.")) for x in out]
