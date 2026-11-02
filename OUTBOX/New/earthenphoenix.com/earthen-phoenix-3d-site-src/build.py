"""Builds the Earthen Phoenix 3D ember site: flat .html pages + assets/ + img/.
Usage: python build.py <content.json> <src dir> <image dir> <out dir>
Every word comes from content.json (exported from the Next.js site's lib/content.ts)."""
import json, re, shutil, sys, html, pathlib

C = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
SRC, IMG, OUT = map(pathlib.Path, sys.argv[2:5])
BOOK, PHONE, EMAIL = C["BOOK"], C["PHONE"], C["EMAIL"]
TEL, SMS = "tel:+18016094263", "sms:+18016094263"
SV = {s["key"]: s for s in C["SERVICES"]}
SHAPE = {k: k for k in SV}
e = lambda s: html.escape(s, quote=True)

def link(p):
    if p == "BOOK": return BOOK
    if p.startswith(("http", "tel:", "sms:", "mailto:", "#")): return p
    path, _, frag = p.partition("#")
    base = "index.html" if path in ("/", "") else path.strip("/") + ".html"
    return base + ("#" + frag if frag else "")

def md(s):
    out = e(s)
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{e(link(html.unescape(m.group(2))))}"' + (' target="_blank" rel="noopener"' if m.group(2) == "BOOK" else "") + f">{m.group(1)}</a>", out)

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
def book_btn(label="Book a session", cls="btn btn-fire"): return f'<a class="{cls}" href="{BOOK}" target="_blank" rel="noopener">{label} {ARROW}</a>'
def h1(title):
    w = title.split()
    if len(w) == 1: return f'<h1 aria-label="{e(title)}"><span class="ln"><span><em>{e(title)}</em></span></span></h1>'
    return f'<h1 aria-label="{e(title)}"><span class="ln"><span>{e(" ".join(w[:-1]))}</span></span><span class="ln"><span><em>{e(w[-1])}</em></span></span></h1>'
def stats(pairs): return '<div class="stats rv">' + "".join(f"<div><b>{e(v)}</b><span>{e(k)}</span></div>" for k, v in pairs) + "</div>"
def faqs(items): return "".join(f"<details><summary>{e(q)}</summary><p>{md(a)}</p></details>" for q, a in items)
OFFER = '<p class="offer rv"><b>20% off</b> your first service. Mention you are a first-time client when you book.</p>'

def sec(id, label, shape, pose, inner, cls="", attrs=""):
    return dict(id=id, label=label, html=f'<section id="{id}" class="{cls}" data-shape="{shape}" data-pose="{pose}"{attrs}>{inner}</section>')

def book_section(title="Ground your soul."):
    return sec("book", "Book", "phoenix", "top", f'''<div class="col" style="width:min(760px,100%)">
      <p class="kick rv">Salt Lake City, Utah</p><h2 class="rv">{e(title)}</h2>
      <p class="body rv">Book online, or call or text and Miquelle will help you choose. Mention you are a first-time client for <strong style="color:var(--saffron)">20% off</strong> your first service.</p>
      <div class="ctas rv">{book_btn("Book online")}<a class="btn btn-line" href="{TEL}">Call {PHONE}</a></div>
      <p class="contact rv">Text <a href="{SMS}">{PHONE}</a> · Email <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>''', "book")

NAV = [("sessions", "Sessions"), ("about", "About"), ("products", "Products"), ("faq", "FAQ"), ("contact", "Contact")]

def page(slug, title, desc, sections, current=None):
    cur = lambda s: ' aria-current="page"' if s == current else ""
    nav = "".join(f'<a href="{s}.html"{cur(s)}>{t}</a>' for s, t in NAV)
    dots = "".join(f'<a href="#{s["id"]}" aria-label="{e(s["label"])}"></a>' for s in sections)
    svc = "".join(f'<li><a href="{s["slug"]}.html">{e(s["name"])}</a></li>' for s in C["SERVICES"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#000000">
<link rel="icon" href="img/ep-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<canvas id="stage" aria-hidden="true"></canvas>
<div class="glow" aria-hidden="true"></div>
<div id="labels" aria-hidden="true"></div>
<header class="hdr">
  <a class="logo" href="index.html" aria-label="Earthen Phoenix home"><img src="img/ep-mark.png" alt="" width="34" height="34"><span>Earthen Phoenix</span></a>
  <nav class="top" aria-label="Main">{nav}</nav>
  <div class="hdr-r">{book_btn("Book a session", "btn btn-fire sm")}
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Menu">
      <svg class="bars" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg>
      <svg class="x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
  </div>
</header>
<nav id="menu" aria-label="Menu" hidden><a href="index.html"{cur("index")}>Home</a>{nav}{book_btn("Book a session")}</nav>
<nav class="progress" aria-label="Page sections">{dots}</nav>
<main id="main">
{"".join(s["html"] for s in sections)}
</main>
<footer>
  <div class="foot">
    <div><a class="logo" href="index.html"><img src="img/ep-mark.png" alt="" width="34" height="34"><span>Earthen Phoenix</span></a>
      <p class="slogan">Ground your soul.</p><p>Massage, bodywork, Reiki, yoga, readings and herbal remedies with Miquelle in Salt Lake City, Utah.</p></div>
    <div><h4>Sessions</h4><ul>{svc}</ul></div>
    <div><h4>Visit</h4><ul><li><a href="sessions.html">Sessions &amp; prices</a></li><li><a href="about.html">About Miquelle</a></li><li><a href="products.html">Products</a></li><li><a href="faq.html">Questions</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h4>Contact</h4><ul><li><a href="{BOOK}" target="_blank" rel="noopener">Book online</a></li><li><a href="{TEL}">Call {PHONE}</a></li><li><a href="{SMS}">Text {PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
  </div>
  <div class="legal"><span>© 2026 Earthen Phoenix · Salt Lake City, Utah</span><span>Concept site, prepared for review.</span></div>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script type="importmap">{{ "imports": {{ "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js" }} }}</script>
<script type="module" src="assets/ember.js"></script>
</body>
</html>
'''

pages = {}

# ---------- home ----------
def svc_card(k, text=None):
    s = SV[k]
    return f'<a class="card" href="{s["slug"]}.html"><h3>{e(s["name"])} <small>{e(s["price"])}</small></h3><p>{e(text or s["line"])}</p><span class="go">How it works →</span></a>'
home = [
  sec("hero", "Intro", "phoenix", "right", f'''<div class="col"><p class="kick rv">Earthen Phoenix · Salt Lake City</p>{h1("Ground your soul.")}
    <p class="lede rv">Massage, Thai and Sarga bodywork, Reiki, private yoga, astrology, tarot and herbal remedies with <strong>Miquelle</strong>, from light and relaxing to deep fascial work.</p>
    <div class="ctas rv">{book_btn()}<a class="btn btn-line" href="#reiki">Explore the sessions</a></div>{OFFER}</div><div class="scrollcue" aria-hidden="true">Scroll<i></i></div>''', "hero"),
  sec("reiki", "Hands near", "reiki", "left", f'''<div class="col"><p class="kick rv">01 · Hands near</p><h2 class="rv">Attention,<br>not pressure.</h2>
    <p class="body rv"><strong>Reiki.</strong> Hands rest gently on or near your clothed body, to support balance and healing. Nothing is pushed or kneaded. With a Master Reiki practitioner, practising since 2011.</p>
    {stats([("Length", "60 min"), ("Price", "$130"), ("You stay dressed", "Clothed")])}<div class="ctas rv"><a class="btn btn-line" href="reiki.html">About Reiki</a></div></div>''', "right"),
  sec("glide", "Hands that glide", "swedish", "right", f'''<div class="col"><p class="kick rv">02 · Hands that glide</p><h2 class="rv">Warm oil,<br>steady hands.</h2>
    <p class="body rv">Light to medium, long and slow.</p><div class="rv">{svc_card("swedish", "Long strokes and essential oils at light to medium pressure, for stress relief and relaxation. 60 or 90 minutes.")}{svc_card("lymph", "Six slow steps, from dry brushing and lymphatic massage to a heated wrap and firming cream. 90 minutes.")}</div></div>'''),
  sec("press", "Hands that press", "deep", "left", f'''<div class="col"><p class="kick rv">03 · Hands that press</p><h2 class="rv">Deep, rhythmic,<br>never painful.</h2>
    <div class="rv">{svc_card("deep", "Deep pressure at the depth you ask for, with breathwork, stretching and movement. 60 or 90 minutes.")}{svc_card("thai", "Full-body stretching combined with rhythmic compressions. 60 or 90 minutes.")}</div></div>''', "right",
    ' data-labels="Deep pressure|deep tissue;Breathwork|deep tissue;Stretching|deep tissue · Thai;Movement|deep tissue;Rhythmic compressions|Thai bodywork"'),
  sec("sarga", "Full weight", "sarga", "right", f'''<div class="col"><p class="kick rv">04 · Full weight</p><h2 class="rv">Her whole weight,<br>placed with care.</h2>
    <p class="body rv"><strong>Sarga bodywork.</strong> Miquelle works barefoot, holding a strap overhead so she controls exactly how much weight goes into each step. It reaches into the fascia, for old injuries.</p>
    {stats([("Length", "90 min"), ("Price", "$180"), ("Pressure", "Deepest")])}<p class="warn rv">It can be somewhat uncomfortable. For people very comfortable with deep pressure.</p>
    <div class="ctas rv"><a class="btn btn-line" href="sarga-bodywork.html">About Sarga</a></div></div>'''),
  sec("beyond", "Beyond the table", "zen", "left", f'''<div class="col" style="width:min(580px,100%)"><p class="kick rv">05 · Beyond the table</p><h2 class="rv">Place, movement,<br>readings, plants.</h2>
    <div class="cards4 rv">''' + "".join(f'<a class="card" href="{SV[k]["slug"]}.html"><h3>{t} <small>{p}</small></h3><p>{d}</p></a>' for k, t, p, d in [
      ("zen", "Zen mountain session", "$200 · 90 min", "A private massage beside a peaceful mountain river, for relaxation and a reset."),
      ("yoga", "Private yoga", "$140 · 60 min", "Schole yoga: Vinyasa flow, then slow Yin holds, moving with your own breath."),
      ("astro", "Astrology &amp; tarot", "$2 / min", "Birth-chart readings, and tarot and oracle readings about the present moment."),
      ("herbs", "Herbalism", "about $40–$100", "A consultation, then teas, rollies or tinctures made for you.")]) + '</div></div>', "right"),
  sec("prices", "Prices", "field", "bg", '''<div class="inner"><p class="kick rv">06 · Sessions &amp; prices</p><h2 class="rv">Ten ways in.<br>One practitioner.</h2><div class="grid rv">''' +
    "".join(f'<a href="{s["slug"]}.html"><span class="n">{e(s["name"])}</span><b>{e(s["price"])}</b><span>{e(s["length"])}</span></a>' for s in C["SERVICES"]) +
    f'''</div><p class="offer rv"><b>20% off</b> your first service. Not sure which to choose? Call or text <a href="{TEL}">{PHONE}</a> and Miquelle will help you choose. <a href="sessions.html">See every price</a>.</p></div>''', "wide"),
  sec("miquelle", "Miquelle", "field", "bg", f'''<div class="inner"><p class="kick rv">07 · Your practitioner</p><h2 class="rv">Meet Miquelle.</h2>
    <div class="about"><img class="portrait rv" src="img/miquelle-portrait-800.webp" alt="Miquelle smiling on a boat at sunset" width="360" height="640" loading="lazy">
    <div><blockquote class="rv">“I base my work off individual needs; and can accommodate anything from light and relaxing to deep fascial work.”</blockquote>
    <p class="body rv">{e(C["ABOUT_WORDS"][0])}</p><div class="chips rv">''' + "".join(f'<a href="{link(c["path"])}">{e(c["name"])}</a>' if c.get("path") else f'<span>{e(c["name"])}</span>' for c in C["CERTS"]) +
    f'''</div><div class="ctas rv"><a class="btn btn-line" href="about.html">More about Miquelle</a></div></div></div>
    <div class="voices">''' + "".join(f'<figure class="rv"><blockquote>{e(v["quote"])}</blockquote><figcaption>{e(v["name"])}</figcaption></figure>' for v in C["VOICES"]) + "</div></div>", "wide"),
  book_section(),
]
pages["index"] = page("index", "Massage, Yoga & Reiki in Salt Lake City | Earthen Phoenix", "Earthen Phoenix in Salt Lake City: massage, Thai and Sarga bodywork, Reiki, private yoga, astrology, tarot and herbal remedies with Miquelle. Ground your soul.", home, "index")

# ---------- one page per session ----------
SKIP = ("photograph", "Scroll", "scroll", "Tap ", "Draw a", "Watch ", "Here the light", "Switch", "Choose a")
for s in C["SERVICES"]:
    k, H, G = s["key"], s["hero"], s["signature"]
    body = [p for p in G["body"] if not any(w in p for w in SKIP)]
    offers = "".join(f'<div><span class="n">{e(o["label"][0].upper() + o["label"][1:])}</span><b>{"$" + e(o["price"]) + (" / min" if o["label"] == "per minute" else "")}</b><span>{e(s["full"])}</span></div>' for o in s["offers"]) \
      or f'<div><span class="n">Consultation and remedies</span><b>{e(s["price"])}</b><span>Varies with time and herb prices</span></div>'
    rel = "".join(svc_card(r) for r in s["related"])
    secs = [
      sec("hero", "Intro", SHAPE[k], "right", f'''<div class="col"><p class="crumb rv"><a href="sessions.html">Sessions</a> / {e(s["name"])}</p><p class="kick rv">{e(H["kicker"])}</p>{h1(H["title"])}
        <p class="lede rv">{e(H["answer"])}</p>{stats(H["spec"])}<div class="ctas rv">{book_btn("Book this session")}<a class="btn btn-line" href="sessions.html">All sessions &amp; prices</a></div>{OFFER}</div>''', "hero sub"),
      sec("how", "How it works", SHAPE[k], "left-near", f'''<div class="col"><p class="kick rv">{e(G["kicker"])}</p><h2 class="rv">{e(G["title"])}</h2>''' + "".join(f'<p class="body rv">{md(p)}</p>' for p in body) +
        f'''<figure class="photo rv" style="margin-top:34px"><img src="img/{s["img"]}-800.webp" alt="{e(s["alt"])}" style="object-position:{e(s["pos"])}" loading="lazy"></figure></div>''', "right"),
      sec("details", "Price and questions", "field", "bg", f'''<div class="inner"><p class="kick rv">{e(s["touch"])} · {e(s["line"])}</p><h2 class="rv">Price &amp; questions.</h2>
        <div class="grid rv" style="grid-template-columns:repeat({max(1, min(3, len(s["offers"]) or 1))},minmax(0,1fr));max-width:{380 * max(1, len(s["offers"]))}px">{offers}</div>
        <div class="faq rv">{faqs(s["faqs"])}</div></div>''', "wide"),
      sec("related", "Related sessions", "field", "bg", f'''<div class="inner"><p class="kick rv">You might also like</p><h2 class="rv">Sessions close<br>to this one.</h2>
        <div class="cards4 four rv">{rel}</div></div>''', "wide"),
      book_section(),
    ]
    pages[s["slug"]] = page(s["slug"], s["seo"]["title"], s["seo"]["desc"], secs, "sessions")

# ---------- sessions & prices ----------
rows = "".join(f'''<div class="pgroup rv"><h3>{e(g["title"])} <small>{e(g["note"])}</small></h3>''' + "".join(
  f'<a class="prow" href="{SV[k]["slug"]}.html"><b>{e(SV[k]["full"])}</b><span>{e(SV[k]["line"])} · {e(SV[k]["length"])}</span><em>{e(SV[k]["price"])}</em></a>' for k in g["keys"]) + "</div>" for g in C["REGISTER"])
pages["sessions"] = page("sessions", "Sessions & Prices: Massage, Bodywork, Reiki, Yoga | Earthen Phoenix",
  "Every Earthen Phoenix session and price in Salt Lake City: Reiki $130, Swedish from $140, deep tissue and Thai from $150, lymphatic and Sarga $180, Zen mountain $200, yoga $140, readings $2/min.", [
  sec("hero", "Intro", "thai", "right", f'''<div class="col"><p class="kick rv">Sessions &amp; prices</p>{h1("Every price, one list.")}
    <p class="lede rv">Ten kinds of session with Miquelle, from $130 Reiki to the $200 Zen mountain massage. Readings are $2 a minute.</p>
    <div class="ctas rv"><a class="btn btn-fire" href="#list">See every price {ARROW}</a>{book_btn("Book online", "btn btn-line")}</div>{OFFER}</div>''', "hero sub"),
  sec("list", "Every price", "field", "bg", f'''<div class="inner"><p class="kick rv">As listed on the booking page</p><h2 class="rv">From hands near<br>to full weight.</h2>
    <p class="body rv">Ordered from hands that hover to her full body weight, then the sessions beyond the table. Open any one to see how it works. New clients: mention it when you book for 20% off your first service.</p>
    <div class="plist">{rows}</div><p class="offer rv">Herbal remedy prices vary with the consultation and the cost of herbs at the time of purchase.</p></div>''', "wide"),
  sec("ask", "Before you book", "field", "bg", f'''<div class="inner"><p class="kick rv">Before you book</p><h2 class="rv">Asked and answered.</h2><div class="faq rv">{faqs(C["SESSIONS_FAQ"])}</div></div>''', "wide"),
  book_section()], "sessions")

# ---------- about ----------
certs = "".join(f'<a href="{link(c["path"])}">{e(c["name"])}</a>' if c.get("path") else f'<span>{e(c["name"])}</span>' for c in C["CERTS"])
pages["about"] = page("about", "About Miquelle, Massage Therapist & Reiki Master | Earthen Phoenix",
  "Meet Miquelle of Earthen Phoenix: Reiki since 2011, Utah College of Massage Therapy graduate 2012, Master Reiki practitioner, yoga teacher, certified in Sarga, Thai, lymphatic and more.", [
  sec("hero", "Intro", "reiki", "right", f'''<div class="col"><p class="kick rv">About Miquelle</p>{h1("Everyone is extremely unique.")}
    <p class="lede rv">Miquelle founded Earthen Phoenix in Salt Lake City. She started with Reiki in 2011, graduated from the Utah College of Massage Therapy in 2012 and is now a Master Reiki practitioner.</p>
    {stats([("Reiki since", "2011"), ("Utah College of Massage Therapy", "2012"), ("Reiki", "Master")])}<div class="ctas rv">{book_btn("Get an appointment")}<a class="btn btn-line" href="sessions.html">Her sessions</a></div></div>''', "hero sub"),
  sec("words", "In her words", "field", "bg", f'''<div class="inner"><p class="kick rv">In her words</p><h2 class="rv">Mind, body<br>and spirit.</h2>
    <div class="about"><img class="portrait rv" src="img/miquelle-portrait-800.webp" alt="Miquelle, founder of Earthen Phoenix, smiling at sunset on the water" width="360" height="640" loading="lazy">
    <div>''' + "".join(f'<p class="body rv">{e(p)}</p>' for p in C["ABOUT_WORDS"]) + f'''</div></div></div>''', "wide"),
  sec("training", "Training", "field", "bg", f'''<div class="inner"><p class="kick rv">Certified in</p><h2 class="rv">Ten disciplines,<br>one practice.</h2>
    <div class="chips rv" style="margin-top:40px">{certs}</div>
    <div class="voices">''' + "".join(f'<figure class="rv"><blockquote>{e(v["quote"])}</blockquote><figcaption>{e(v["name"])}</figcaption></figure>' for v in C["VOICES"]) + "</div></div>", "wide"),
  book_section()], "about")

# ---------- FAQ ----------
groups = "".join(f'<h3 class="rv">{e(g["title"])}</h3>' + f'<div class="faq rv" style="margin-top:6px">{faqs(g["items"])}</div>' for g in C["ALL_FAQ"])
pages["faq"] = page("faq", "Questions about Massage, Reiki & Yoga | Earthen Phoenix",
  "Answers about Earthen Phoenix in Salt Lake City: booking, the 20% first-visit discount, massage, Sarga, Reiki, yoga, readings, herbal remedies and Miquelle’s training.", [
  sec("hero", "Intro", "astro", "right", f'''<div class="col"><p class="kick rv">Questions</p>{h1("Asked and answered.")}
    <p class="lede rv">Short answers about booking, prices, what each session feels like, and Miquelle’s training.</p>
    <div class="ctas rv">{book_btn("Get an appointment")}<a class="btn btn-line" href="{TEL}">Ask your own</a></div></div>''', "hero sub"),
  sec("answers", "Answers", "field", "bg", f'<div class="inner"><div class="faq" style="margin-top:0">{groups}</div></div>', "wide"),
  book_section()], "faq")

# ---------- products ----------
shelf = "".join(f'<a class="prod rv" href="{C["STORE"][p["store"]]}" target="_blank" rel="noopener"><img src="img/{p["img"]}-800.webp" alt="{e(p["alt"])}" loading="lazy"><div><b>{e(p["name"])}</b><em>{e(p["price"])}</em><span>Buy in the online store →</span></div></a>' for p in C["PRODUCTS"])
pages["products"] = page("products", "Body Oil, Face Oil & Body Butter | Earthen Phoenix",
  "Take the care home: Armature Aurora Signature Body Oil ($44), Armature Smooth Sailing Face Oil ($55) and M’s Secret Body Butter ($44) from Earthen Phoenix in Salt Lake City.", [
  sec("hero", "Intro", "bottle", "right", f'''<div class="col"><p class="kick rv">Products</p>{h1("Take the care home.")}
    <p class="lede rv">Two Armature oils and M’s Secret Body Butter, from $44. Checkout happens in the Earthen Phoenix online store.</p>
    <div class="ctas rv"><a class="btn btn-fire" href="#shelf">See the shelf {ARROW}</a><a class="btn btn-line" href="{TEL}">Need help choosing?</a></div></div>''', "hero sub"),
  sec("shelf", "The shelf", "field", "bg", f'<div class="inner"><p class="kick rv">The shelf</p><h2 class="rv">Oils and butter.</h2><div class="shelf">{shelf}</div></div>', "wide"),
  book_section()], "products")

# ---------- contact ----------
ways = "".join(f'<a class="card rv" href="{h}"{t}><p class="kick">{k}</p><b>{v}</b><p>{d}</p></a>' for k, v, h, t, d in [
  ("Book online", "Get an appointment", BOOK, ' target="_blank" rel="noopener"', "Pick a session and a time on the booking page."),
  ("Call or text", PHONE, TEL, "", "Not sure which session? Miquelle will help you choose."),
  ("Write", EMAIL, f"mailto:{EMAIL}", "", "Feel free to contact me with any questions anytime.")])
pages["contact"] = page("contact", "Contact & Booking | Earthen Phoenix, Salt Lake City",
  "Book Earthen Phoenix online, call or text 801-609-4263, or email info@earthenphoenix.com. Massage, Reiki, yoga and readings in Salt Lake City. 20% off your first service.", [
  sec("hero", "Intro", "phoenix", "right", f'''<div class="col"><p class="kick rv">Contact &amp; booking</p>{h1("Call, text, or write.")}
    <p class="lede rv">Feel free to contact me with any questions anytime. Book online, call or text {PHONE}, or email {EMAIL}.</p>
    <div class="ctas rv">{book_btn("Get an appointment")}<a class="btn btn-line" href="{TEL}">Call or text</a></div>{OFFER}</div>''', "hero sub"),
  sec("ways", "Ways to reach her", "field", "bg", f'<div class="inner"><p class="kick rv">Three ways in</p><h2 class="rv">However suits you.</h2><div class="ways">{ways}</div></div>', "wide"),
  sec("where", "Where", "zen", "right", f'''<div class="col"><p class="kick rv">Where</p><h2 class="rv">Salt Lake City,<br>and a river.</h2>
    <p class="body rv">Earthen Phoenix is in Salt Lake City, Utah. The Zen mountain session happens outdoors beside a mountain river; ask Miquelle about its location and season.</p>
    <div class="ctas rv"><a class="btn btn-line" href="zen-mountain-session.html">The Zen mountain session</a></div></div>''')], "contact")

# ---------- write ----------
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "assets").mkdir(exist_ok=True); (OUT / "img").mkdir(exist_ok=True)
for f in ("ember.js", "site.css"): shutil.copy(SRC / f, OUT / "assets" / f)
imgs = {"ep-mark.png", "miquelle-portrait-800.webp"} | {s["img"] + "-800.webp" for s in C["SERVICES"]} | {p["img"] + "-800.webp" for p in C["PRODUCTS"]}
for i in imgs: shutil.copy(IMG / i, OUT / "img" / i)
for slug, h in pages.items(): (OUT / f"{slug}.html").write_text(h, encoding="utf-8")
print(len(pages), "pages,", len(imgs), "images")
