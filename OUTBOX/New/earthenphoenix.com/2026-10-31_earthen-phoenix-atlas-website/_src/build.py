"""THE EARTHEN ATLAS — builds the Earthen Phoenix website. All words live here; run  python _src/build.py  from the site folder.
Facts come only from earthenphoenix.com and its booking page (/appointment-8682), as gathered 30 Oct 2026. Nothing is invented."""
import json, os, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://earthenphoenix.com/'
BOOK = 'https://earthenphoenix.com/appointment-8682'   # live GoHighLevel calendar: see README before moving domains
PHONE, TEL, SMS, EMAIL = '801-609-4263', 'tel:+18016094263', 'sms:+18016094263', 'info@earthenphoenix.com'
STORE = {'aurora': 'https://earthenphoenix.com/product-details/product/67916113fbd2be1e2cb402bd',
         'sailing': 'https://earthenphoenix.com/product-details/product/67916315fbd2be5dd0b40c2f',
         'butter': 'https://earthenphoenix.com/product-details/product/6791441ef36f6cdd3681daa7'}
FONTS = 'https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;500;600&family=Gloock&family=Martian+Mono:wdth,wght@87.5,500&display=swap'
COORDS = '40.76° N · 111.89° W'
AR = '<span class="ar" aria-hidden="true">→</span>'

IMG = {'yoga-assisted-fold': (800, 533, 1600, 1067), 'mountain-meadow': (800, 533, 1600, 1067), 'massage-head-neck': (800, 1200, 1200, 1800),
       'reiki-crystals-candles': (800, 450, 1600, 900), 'sound-tuning-forks': (800, 450, 1600, 900), 'sarga-barefoot-strap': (750, 1334, None, None),
       'miquelle-portrait': (360, 640, None, None), 'ms-secret-body-butter': (800, 796, 1070, 1064), 'armature-aurora-body-oil': (800, 1067, 1350, 1800),
       'armature-smooth-sailing-face-oil': (800, 600, 1600, 1200), 'earthen-phoenix-logo': (800, 467, 1600, 933)}
def img(n, alt, sizes='100vw', eager=False, style=''):
    w1, h1, w2, h2 = IMG[n]; src = f'assets/img/{n}-800.webp'
    ss = f' srcset="{src} {w1}w, assets/img/{n}-1600.webp {w2}w" sizes="{sizes}"' if w2 else ''
    return f'<img src="{src}"{ss} alt="{html.escape(alt)}" width="{w1}" height="{h1}"' + (' fetchpriority="high"' if eager else ' loading="lazy" decoding="async"') + (f' style="{style}"' if style else '') + '>'
def strip(s): return html.unescape(re.sub(r'<[^>]+>', '', s))

# ---------- the sessions: one source for menu, atlas, tables, schema ----------
SV = {
 'swedish': dict(name='Swedish massage', href='swedish-massage.html', price='$140 / $170', lens='60 / 90 min', offers=[('140', '60 minutes'), ('170', '90 minutes')], line='Long strokes and essential oils, light to medium pressure', how='A long stroke passes; the peaks it crosses soften.'),
 'deep': dict(name='Deep tissue massage', href='deep-tissue-massage.html', price='$150 / $180', lens='60 / 90 min', offers=[('150', '60 minutes'), ('180', '90 minutes')], line='Deep pressure, breathwork and stretching. Never painful', how='One slow point sinks on each out-breath.'),
 'thai': dict(name='Thai bodywork', href='thai-bodywork.html', price='$150 / $170', lens='60 / 90 min', offers=[('150', '60 minutes'), ('170', '90 minutes')], line='Full-body stretching and rhythmic compressions', how='Presses on a beat, then the ground is drawn long.'),
 'lymph': dict(name='Lymphatic firming', full='Lymphatic firming body treatment', href='lymphatic-firming-treatment.html', price='$180', lens='90 min', offers=[('180', '90 minutes')], line='Dry brushing, lymphatic massage, a heated wrap', how='Swelling drains along the paths toward the collarbone.'),
 'sarga': dict(name='Sarga bodywork', href='sarga-bodywork.html', price='$180', lens='90 min', offers=[('180', '90 minutes')], line='Barefoot, with a fabric strap, for old injuries', how='Bare footprints press deep, and the pressure spreads.'),
 'reiki': dict(name='Reiki', href='reiki.html', price='$130', lens='60 min', offers=[('130', '60 minutes')], line='Hands on or near the clothed body', how='No pressing at all: the whole field evens out.'),
 'zen': dict(name='Zen mountain session', href='zen-mountain-session.html', price='$200', lens='90 min', offers=[('200', '90 minutes')], line='A private massage beside a mountain river', how='Real mountains; the river slows the longer you stay.'),
 'yoga': dict(name='Private yoga', href='private-yoga.html', price='$140', lens='60 min', offers=[('140', '60 minutes, private or split between a group')], line='Vinyasa flow, then slow Yin holds', how='Waves while you flow, stillness in the hold.'),
 'astro': dict(name='Astrology & tarot', href='astrology-tarot.html', price='$2 / min', lens='by the minute', offers=[('2', 'per minute')], line='Birth-chart, tarot and oracle readings', how='The sky above your horizon, from your birthday.'),
 'herbs': dict(name='Herbalism', full='Herbalism consultation', href='herbalism.html', price='about $40–$100', lens='varies', offers=[], line='Custom teas, rollies and tinctures', how='An infusion spreading: tea, drops, or a rollie.'),
}
for v in SV.values(): v.setdefault('full', v['name'])
PIC = {'swedish': 'massage-head-neck', 'deep': 'massage-head-neck', 'thai': 'yoga-assisted-fold', 'lymph': 'reiki-crystals-candles', 'sarga': 'sarga-barefoot-strap', 'reiki': 'sound-tuning-forks', 'zen': 'mountain-meadow', 'yoga': 'mountain-meadow', 'astro': 'reiki-crystals-candles', 'herbs': 'armature-smooth-sailing-face-oil'}
PICALT = {'massage-head-neck': 'Miquelle’s hands at a client’s neck and shoulders', 'yoga-assisted-fold': 'Miquelle assisting a forward bend on a grassy hillside', 'reiki-crystals-candles': 'Candles and crystals around a client resting on the table',
          'sarga-barefoot-strap': 'Miquelle barefoot on a client’s back, holding an overhead bar', 'sound-tuning-forks': 'Tuning forks beside a client on the massage table', 'mountain-meadow': 'A mountain meadow below snow-streaked peaks', 'armature-smooth-sailing-face-oil': 'An amber dropper bottle beside rosemary and crystals'}

BUSINESS = {'@type': 'HealthAndBeautyBusiness', '@id': SITE + '#business', 'name': 'Earthen Phoenix', 'url': SITE, 'slogan': 'Ground your soul',
            'telephone': '+1-' + PHONE, 'email': EMAIL, 'image': SITE + 'assets/img/mountain-meadow-1600.webp', 'logo': SITE + 'assets/img/earthen-phoenix-logo-800.webp',
            'address': {'@type': 'PostalAddress', 'addressLocality': 'Salt Lake City', 'addressRegion': 'UT', 'addressCountry': 'US'}, 'areaServed': {'@type': 'City', 'name': 'Salt Lake City'},
            'founder': {'@type': 'Person', 'name': 'Miquelle', 'jobTitle': 'Master Reiki practitioner, massage therapist and yoga teacher', 'alumniOf': {'@type': 'CollegeOrUniversity', 'name': 'Utah College of Massage Therapy'}}}
def faq_ld(qa): return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in qa]}
def crumbs_ld(trail): return {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + ('' if h == 'index.html' else h)} for i, (n, h) in enumerate(trail)]}
def service_ld(k, desc):
    s = SV[k]; d = {'@type': 'Service', 'name': s['full'], 'serviceType': s['full'], 'description': desc, 'provider': {'@id': SITE + '#business'}, 'areaServed': {'@type': 'City', 'name': 'Salt Lake City'}, 'url': SITE + s['href']}
    if s['offers']: d['offers'] = [{'@type': 'Offer', 'price': p, 'priceCurrency': 'USD', 'description': l} for p, l in s['offers']]
    return d

# ---------- shell ----------
def head(p):
    canon = SITE + ('' if p['slug'] == 'index.html' else p['slug'])
    graph = [BUSINESS, {'@type': 'WebPage', 'url': canon, 'name': strip(p['title']), 'description': p['desc'], 'inLanguage': 'en-US'}] + p.get('ld', [])
    if p.get('trail'): graph.append(crumbs_ld(p['trail']))
    robots = 'noindex' if p['slug'] == '404.html' else 'index, follow, max-image-preview:large'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Earthen Phoenix"><meta property="og:title" content="{p['title']}"><meta property="og:description" content="{html.escape(p['desc'])}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}assets/img/{p.get('og', 'mountain-meadow')}-800.webp"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1a1612">
<link rel="icon" href="assets/img/ep-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/atlas.css">
<script>try{{if(sessionStorage.getItem('ep-atlas')&&!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('arriving');sessionStorage.removeItem('ep-atlas')}}catch(e){{}}</script>
<script type="application/ld+json">{json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="sweep" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>'''

def header(p):
    cur = p['slug']
    nav = ''.join(f'<a href="{h}"' + (' aria-current="page"' if h == cur else '') + f'>{t}</a>' for h, t in [('sessions.html', 'Sessions'), ('about.html', 'About'), ('products.html', 'Products'), ('faq.html', 'FAQ'), ('contact.html', 'Contact')])
    rows = ''.join(f'<li><a href="{v["href"]}">{v["name"]}<small>{v["price"]}</small></a></li>' for v in SV.values())
    return f'''
<header class="hdr">
  <a class="mark" href="index.html"><img src="assets/img/ep-mark.png" alt="" width="38" height="38"><span>Earthen Phoenix</span></a>
  <nav class="nav" aria-label="Main">{nav}</nav>
  <a class="btn" href="{BOOK}">Book {AR}</a>
  <button class="burger" type="button" aria-expanded="false" aria-controls="menu"><span>Menu</span><i aria-hidden="true"></i></button>
</header>
<div class="menu" id="menu" aria-hidden="true">
  <nav aria-label="All sessions"><ol>{rows}</ol></nav>
  <aside><a href="index.html">Home</a><a href="sessions.html">Sessions &amp; prices</a><a href="about.html">About Miquelle</a><a href="products.html">Products</a><a href="faq.html">Questions</a><a href="contact.html">Contact</a>
    <a class="btn sun" href="{BOOK}" style="align-self:flex-start;margin-top:16px">Get an appointment {AR}</a>
    <p>Salt Lake City · <a href="{TEL}" style="display:inline;font-size:inherit;padding:0">{PHONE}</a><br>First time? Mention it for 20% off your first service.</p></aside>
</div>
<main id="main">
'''

def footer(p, title='Mention it when you book: <em>20% off your first service.</em>'):
    sess = ''.join(f'<a href="{SV[k]["href"]}">{SV[k]["name"]}</a>' for k in ['swedish', 'deep', 'thai', 'lymph', 'sarga', 'zen'])
    more = ''.join(f'<a href="{SV[k]["href"]}">{SV[k]["name"]}</a>' for k in ['reiki', 'yoga', 'astro', 'herbs'])
    return f'''<section class="finale">
  <div class="wrap">
    <p class="kicker" style="justify-content:center" data-r>First time with us?</p>
    <h2 data-split>{title}</h2>
    <div class="row" data-r style="--d:2"><a class="btn sun" href="{BOOK}">Get an appointment {AR}</a><a class="btn ghost" href="{TEL}">Call or text {PHONE}</a></div>
  </div>
  <div class="ground"><div class="terrain" data-terrain="ground" aria-hidden="true"></div></div>
  <div class="foot">
    <div><p class="big">Ground<br><em>your soul.</em></p><p style="margin-top:16px;color:var(--on-2);max-width:36ch">Massage, bodywork, Reiki, yoga, readings and herbal remedies with Miquelle in Salt Lake City, Utah.</p></div>
    <div><h4>Massage &amp; bodywork</h4>{sess}</div>
    <div><h4>More sessions</h4>{more}<a href="sessions.html">All sessions &amp; prices</a><a href="products.html">Products</a></div>
    <div><h4>Visit</h4><a href="about.html">About Miquelle</a><a href="faq.html">Questions</a><a href="contact.html">Contact</a><a href="{TEL}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
  <div class="legal"><span>&copy; <span id="yr">2026</span> Earthen Phoenix · Salt Lake City, Utah · {COORDS}</span><span>All photographs are Earthen Phoenix&rsquo;s own.</span></div>
</section>
</main>
<script src="assets/terrain.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
'''

def phero(p, image, alt, kicker, h1, answer, spec, pos='50% 50%', ctas=None):
    trail = p.get('trail') or []
    cr = ''.join(f'<li><a href="{h}">{n}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{n}</li>' for i, (n, h) in enumerate(trail))
    sp = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in spec) if spec else ''
    ctas = ctas or f'<a class="btn sun" href="{BOOK}">Book this session {AR}</a><a class="btn ghost" href="{TEL}">Call or text</a>'
    return f'''<section class="phero" style="--pos:{pos}">
  <div class="ph">{img(image, alt, '100vw', eager=True)}</div>
  <div class="ph-in">
    <ol class="crumbs" aria-label="Breadcrumb">{cr}</ol>
    <p class="kicker">{kicker}</p>
    <h1 data-split>{h1}</h1>
    <p class="ans" data-r>{answer}</p>
    {f'<dl class="spec" data-r style="--d:1">{sp}</dl>' if sp else ''}
    <div class="row" data-r style="--d:2">{ctas}</div>
  </div>
</section>
'''

def terrain(mode, label, mini=False, tid=True):
    a = f' id="t-{mode}" data-read="r-{mode}"' if tid else ''
    return f'<div class="terrain{" mini" if mini else ""}" data-terrain="{mode}"{a} role="img" aria-label="{html.escape(label)}"></div>'

def study(mode, label, kicker, h2, body, controls='', hint='', rev=False, wide=False):
    cap = f'<figcaption><span class="read" id="r-{mode}" aria-hidden="true"></span>{f"<span class=\"hint\">{hint}</span>" if hint else ""}</figcaption>'
    return f'''<section class="sec dark">
  <div class="wrap study{' rev' if rev else ''}">
    <figure class="fig{' wide' if wide else ''}" data-r style="margin:0">{terrain(mode, label)}{cap}</figure>
    <div data-r style="--d:1"><p class="kicker">{kicker}</p><h2>{h2}</h2><div style="margin-top:24px">{body}</div>{f'<div data-for="t-{mode}">{controls}</div>' if controls else ''}</div>
  </div>
</section>
'''

def tags(k): return '<div class="tags" data-r>' + ''.join(f'<div><b>${p}</b><span>{l}</span></div>' for p, l in SV[k]['offers']) + '</div>'
def route(items, n=None): return f'<ol class="route" style="--n:{n or len(items)}">' + ''.join(f'<li><b>{i + 1:02d}</b><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(items)) + '</ol>'
def faq(qa, title='Asked and <em style="font-style:normal;color:var(--cta)">answered.</em>'):
    items = ''.join(f'<details><summary>{q}<i aria-hidden="true"></i></summary><div class="a">{a}</div></details>' for q, a in qa)
    return f'<section class="sec"><div class="narrow"><p class="kicker" data-r>Before you book</p><h2 data-split>{title}</h2><div class="faq" data-r>{items}</div></div></section>\n'
def more(keys, title='Other ways to ground.'):
    cards = ''.join(f'<a href="{SV[k]["href"]}" data-r style="--d:{i}"><div class="im">{img(PIC[k], PICALT[PIC[k]], "(max-width: 900px) 45vw, 300px")}</div><h3>{SV[k]["name"]}</h3><p>{SV[k]["price"]} · {SV[k]["lens"]}</p></a>' for i, k in enumerate(keys))
    return f'<section class="sec paper2"><div class="wrap"><p class="kicker" data-r>Keep exploring</p><h2 data-split>{title}</h2><div class="more">{cards}</div></div></section>\n'
def plate(k, i):
    v = SV[k]
    return f'<a class="plate" href="{v["href"]}"><div class="top"><span>PLATE {i + 1:02d}</span><span>{v["price"]} · {v["lens"]}</span></div>{terrain(k, v["how"], mini=True, tid=False)}<div class="bot"><h3>{v["name"]}</h3><p>{v["how"]}</p><span class="go">OPEN THE PLATE →</span></div></a>'

PAGES = []
def page(**p): PAGES.append(p)

# ===================================================================== HOME
gallery = [('c1', 'yoga-assisted-fold', 'An assisted fold on the hillside', .05), ('c2', 'massage-head-neck', 'Hands at the neck and shoulders', .12), ('c3', 'sarga-barefoot-strap', 'Sarga: barefoot, holding the bar', -.06),
           ('c4', 'reiki-crystals-candles', 'Crystals, sage and candlelight', .08), ('c5', 'sound-tuning-forks', 'Tuning forks beside the table', .16)]
LEG = [('var(--y)', 'Peak', 'Where it is held hardest.'), ('var(--o)', 'Ridge', 'Tension you have learned to carry.'), ('var(--r)', 'Slope', 'Starting to give.'), ('var(--b)', 'Foothill', 'Settling.'), ('var(--g)', 'Ground', 'Where every session is heading.')]
VOICES = [('This is not your typical spa massage where you leave feeling underwhelmed and overcharged.', 'Sylvie'),
          ('Miquelle is like the Thanos of massage, she&rsquo;s has collected all of the massage techniques in existence.', 'V'),
          ('I was pregnant and it was the first time I was pain free the entire pregnancy.', 'Megan')]
PROD = [('Armature Aurora Signature Body Oil', '$44', 'armature-aurora-body-oil', 'Two amber bottles of Armature Aurora body oil on a white shell dish', STORE['aurora']),
        ('Armature Smooth Sailing Face Oil', '$55', 'armature-smooth-sailing-face-oil', 'Armature Smooth Sailing face oil beside fresh rosemary and tumbled crystals', STORE['sailing']),
        ('M&rsquo;s Secret Body Butter', '$44', 'ms-secret-body-butter', 'A jar of Miquelle’s Secret body butter in front of a glowing salt lamp', STORE['butter'])]
def shelf(store=False):
    return '<div class="shelf">' + ''.join(f'<a href="{u if store else "products.html"}" data-r style="--d:{i}"><div class="im">{img(im, a, "(max-width: 900px) 90vw, 400px")}</div><h3>{n}</h3><p class="pr">{pr}{" · BUY IN THE STORE →" if store else ""}</p></a>' for i, (n, pr, im, a, u) in enumerate(PROD)) + '</div>'

home = f'''<section class="hero" aria-labelledby="h1">
  <div class="ph">{img('mountain-meadow', 'Miquelle and a student in a mountain meadow under snow-streaked peaks', eager=True)}</div>
  {terrain('hero', 'A map of tension: peaks over the shoulders and lower back soften to level ground as a long stroke passes')}
  <p class="meta">SALT LAKE CITY, UTAH<br>{COORDS}<br>SHEET 00 · THE BODY</p>
  <div class="hero-in">
    <div><p class="kicker">Massage · Bodywork · Reiki · Yoga</p><h1 id="h1" data-split>Ground <em>your soul.</em></h1></div>
    <div class="hero-side" data-r style="--d:3">
      <p>Tension has a shape. Miquelle reads it with her hands, then brings it back to level ground, through massage, bodywork, Reiki, yoga, readings and herbal remedies in Salt Lake City.</p>
      <div class="row"><a class="btn sun" href="{BOOK}">Get an appointment {AR}</a><a class="btn ghost" href="sessions.html">See every session</a></div>
    </div>
    <div class="readout mono"><span class="read" id="r-hero" aria-hidden="true">TENSION</span><span class="key" aria-hidden="true">PEAK <i style="background:var(--y)"></i><i style="background:var(--o)"></i><i style="background:var(--r)"></i><i style="background:var(--b)"></i><i style="background:var(--g)"></i> GROUND</span></div>
  </div>
</section>

<section class="sec">
  <div class="wrap legend" data-r>
    <div class="disc">{'<img src="assets/img/ep-mark.png" alt="The Earthen Phoenix mark: a phoenix over five bands of colour" width="158" height="160">'}</div>
    <div>
      <p class="kicker">How to read this site</p>
      <h2 style="max-width:16ch">Her mark is <em style="font-style:normal;color:var(--r)">a map key.</em></h2>
      <p class="lede" style="margin:22px 0 30px">The five bands in the Earthen Phoenix circle run like the colours of a relief map. Here, height is tension. Every session on this site is drawn as a terrain, and each one brings the ground level in its own way.</p>
      <ol>{''.join(f'<li style="--i:{i}"><i style="background:{c}"></i><div><b>{n}</b><span>{d}</span></div></li>' for i, (c, n, d) in enumerate(LEG))}</ol>
    </div>
  </div>
</section>

<section class="atlas" aria-labelledby="atlas-h">
  <div class="stick">
    <div class="atlas-track">
      <div class="intro"><p class="kicker">The atlas · ten plates</p><h2 id="atlas-h">Ten sessions. <em style="font-style:normal;color:var(--y)">Ten ways to level the ground.</em></h2><p class="lede" style="margin-top:22px">Each plate is live. Watch how the work meets the body, then open a plate to try it yourself.</p></div>
      {''.join(plate(k, i) for i, k in enumerate(SV))}
    </div>
    <div class="prog" aria-hidden="true"></div>
  </div>
</section>

<section class="sec paper2">
  <div class="wrap">
    <p class="kicker" data-r>Miquelle, in her words</p>
    <p class="state" data-split>I believe in all modalities that work for you. By working with the practitioner and modalities that call to you, <em>you innately empower your own ability to heal.</em></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="row" style="justify-content:space-between;align-items:end;margin-bottom:60px"><div><p class="kicker" data-r>Field photographs</p><h2 data-split>Her rooms, her mountains.</h2></div><p class="mono" data-r style="color:var(--ink-2)">ALL PHOTOGRAPHS: EARTHEN PHOENIX</p></div>
    <div class="collage">{''.join(f'<figure class="{c}"><div class="reveal-img" data-par="{s}">{img(n, a, "(max-width: 900px) 90vw, 40vw")}</div><figcaption>{a}</figcaption></figure>' for c, n, a, s in gallery)}</div>
  </div>
</section>

<section class="sec paper2">
  <div class="wrap meet">
    <div class="por reveal-img">{img('miquelle-portrait', 'Miquelle, founder of Earthen Phoenix, smiling at sunset on the water', '(max-width: 900px) 90vw, 420px')}</div>
    <div>
      <p class="kicker" data-r>Meet Miquelle</p>
      <h2 data-split>Everyone is extremely unique.</h2>
      <p class="lede" data-r style="margin-top:24px">&ldquo;I have worked with many different people, backgrounds, and bodies. I base my work off individual needs; and can accommodate anything from light and relaxing to deep fascial work.&rdquo;</p>
      <div class="trail" aria-label="Miquelle’s path: Reiki from 2011, Utah College of Massage Therapy in 2012, thirteen years of practice">
        <svg viewBox="0 0 1000 230" role="img" aria-hidden="true"><path class="base" d="M0 210 C80 206 100 160 130 150 S230 128 330 108 S560 96 640 78 S820 46 930 34 L1000 30"/><path class="draw" pathLength="1" d="M0 210 C80 206 100 160 130 150 S230 128 330 108 S560 96 640 78 S820 46 930 34 L1000 30"/>
          <g class="wp" style="--at:.15"><circle cx="130" cy="150" r="7"/><text class="big" x="110" y="200">2011</text><text x="110" y="222">STARTED WITH REIKI</text></g>
          <g class="wp" style="--at:.35"><circle cx="330" cy="108" r="7"/><text class="big" x="310" y="160">2012</text><text x="310" y="182">UTAH COLLEGE OF MASSAGE THERAPY</text></g>
          <g class="wp" style="--at:.7"><circle cx="930" cy="34" r="7"/><text class="big" x="760" y="90">13+ years</text><text x="760" y="112">MASTER REIKI PRACTITIONER</text></g></svg>
      </div>
      <p data-r style="margin-top:20px"><a class="uline" href="about.html">Her story and training →</a></p>
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="wrap">
    <p class="kicker" data-r>Your first visit</p>
    <h2 data-split>Three waypoints, no guesswork.</h2>
    {route([('Choose, or ask', f'Pick a plate from the atlas. Not sure? Call or text <a class="uline" href="{TEL}">{PHONE}</a> and Miquelle will help you choose.'), ('Book online or by phone', f'Use the <a class="uline" href="{BOOK}">booking page</a>, or call or text. First time? Mention it for 20% off your first service.'), ('A session built around you', 'Anything from light and relaxing to deep fascial work, based on your individual needs.')])}
    <div style="margin-top:110px">
      <p class="kicker" data-r>Client words</p>
      <div class="voices" data-r aria-live="polite">{''.join(f'<blockquote><p>&ldquo;{q}&rdquo;</p><cite>{c}</cite></blockquote>' for q, c in VOICES)}</div>
      <div class="vnav">{''.join(f'<button type="button" aria-label="Show words from {c}"></button>' for _, c in VOICES)}</div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap"><div class="row" style="justify-content:space-between;align-items:end"><div><p class="kicker" data-r>Take the care home</p><h2 data-split>Oils and butter.</h2></div><a class="uline" href="products.html" data-r>All products →</a></div>{shelf()}</div>
</section>
'''
page(slug='index.html', title='Massage, Yoga &amp; Reiki in Salt Lake City | Earthen Phoenix', desc='Earthen Phoenix in Salt Lake City: massage, Thai and Sarga bodywork, Reiki, private yoga, astrology, tarot and herbal remedies with Miquelle. Ground your soul.', body=home)

# ===================================================================== SESSIONS
rows = ''.join(f'<tr><td><a href="{v["href"]}">{v["full"]}</a></td><td class="p">{v["lens"]}</td><td class="p">{v["price"]}</td><td class="d">{v["line"]}</td></tr>' for v in SV.values())
ses_faq = [('How much is a massage at Earthen Phoenix?', '<p>Swedish massage starts at $140 for 60 minutes. Deep tissue is $150 / $180 and Thai bodywork $150 / $170 (60 / 90 minutes). The lymphatic firming treatment and Sarga are $180 for 90 minutes, and the Zen mountain session is $200 for 90 minutes.</p>'),
           ('Is there a first-time discount?', '<p>Yes. Mention you are a first-time client when you book for 20% off your first service.</p>'),
           ('Which session is right for me?', f'<p>For no pressure at all, Reiki. For relaxation, Swedish. For deep work, deep tissue or Sarga. Still unsure? Call or text {PHONE} and Miquelle will help you choose.</p>')]
page(slug='sessions.html', title='Sessions &amp; Prices: Massage, Bodywork, Reiki, Yoga | Earthen Phoenix', og='yoga-assisted-fold',
     desc='Every Earthen Phoenix session and price in Salt Lake City: Reiki $130, Swedish from $140, deep tissue and Thai from $150, lymphatic and Sarga $180, Zen mountain $200, yoga $140, readings $2/min.',
     trail=[('Home', 'index.html'), ('Sessions & prices', 'sessions.html')],
     ld=[{'@type': 'ItemList', 'name': 'Earthen Phoenix sessions', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': SITE + v['href'], 'name': v['full']} for i, v in enumerate(SV.values())]}, faq_ld(ses_faq)],
     body=lambda p: phero(p, 'yoga-assisted-fold', 'Miquelle guiding a student into a forward bend on a grassy hillside', 'The atlas', 'Sessions and prices.',
        'Ten kinds of session with Miquelle, from $130 Reiki to the $200 Zen mountain massage. Readings are $2 a minute.', [('From', '$130'), ('Sessions', '10'), ('First visit', '20% off')], pos='60% 45%',
        ctas=f'<a class="btn sun" href="#prices">See every price {AR}</a><a class="btn ghost" href="{BOOK}">Book</a>') +
     f'''<section class="sec dark"><div class="wrap"><p class="kicker" data-r>Ten plates</p><h2 data-split>Watch how each one works.</h2><p class="lede" data-r style="margin-top:20px">Height is tension. Each plate shows how that session brings it down. Open one to try it.</p>
  <div class="plates">{''.join(plate(k, i) for i, k in enumerate(SV))}</div></div></section>
<section class="sec" id="prices"><div class="wrap"><p class="kicker" data-r>As listed on the booking page</p><h2 data-split>Every price, one table.</h2>
  <table class="ptab" data-r><thead><tr><th>Session</th><th>Length</th><th>Price</th><th>What it is</th></tr></thead><tbody>{rows}</tbody></table>
  <p data-r style="margin-top:24px;color:var(--ink-2)">Herbal remedy prices vary with the consultation and the cost of herbs at the time of purchase. New clients: mention it when you book for 20% off your first service.</p></div></section>
''' + faq(ses_faq))

# ===================================================================== SERVICE PAGES
def svc(k, title, desc, og, body, faqs, ld_desc):
    page(slug=SV[k]['href'], title=title, desc=desc, og=og, trail=[('Home', 'index.html'), ('Sessions', 'sessions.html'), (SV[k]['name'], SV[k]['href'])], ld=[service_ld(k, ld_desc), faq_ld(faqs)], body=body)
def light(inner): return f'<section class="sec"><div class="wrap">{inner}</div></section>'

# Swedish
f_sw = [('How much is a Swedish massage in Salt Lake City?', '<p>$140 for 60 minutes or $170 for 90 minutes.</p>'),
        ('What pressure is a Swedish massage?', '<p>Light to medium. For deeper work, see <a href="deep-tissue-massage.html">deep tissue massage</a>.</p>'),
        ('Can it include more than massage?', '<p>Yes: sound therapy, meditation and breathwork, for stress relief and relaxation.</p>')]
svc('swedish', 'Swedish Massage in Salt Lake City, from $140 | Earthen Phoenix', 'Swedish massage in Salt Lake City: long strokes and essential oils at light to medium pressure. $140 for 60 minutes, $170 for 90. Sound therapy and breathwork can be added.', 'massage-head-neck',
  lambda p: phero(p, 'massage-head-neck', 'Miquelle supporting a client’s head and neck during a massage', 'Plate 01 · Massage', 'Swedish massage.',
     'Long strokes and essential oils at light to medium pressure, for stress relief and relaxation. $140 for 60 minutes or $170 for 90.', [('Length', '60 / 90 min'), ('Price', '$140 / $170'), ('Pressure', 'Light–medium')], pos='50% 30%') +
  study('swedish', 'A long stroke travels the length of the back and the peaks of tension it crosses soften', 'How it works', 'One long stroke at a time.',
     '<p>A stroke travels the full length of the back, then returns. Every peak it crosses softens a little, the way warm oil and steady hands work through tension without forcing it. Press and drag across the terrain to make a stroke of your own.</p>',
     '<p class="ctrl-label">Pressure</p><div class="ctrl" role="group" aria-label="Pressure"><button type="button" data-set="pressure:light" aria-pressed="true">Light</button><button type="button" data-set="pressure:medium" aria-pressed="false">Medium</button></div>'
     '<p class="ctrl-label">Can be folded in</p><div class="ctrl"><button type="button" data-add="sound" aria-pressed="false">Sound therapy</button><button type="button" data-add="still" aria-pressed="false">Meditation</button><button type="button" data-add="breath" aria-pressed="false">Breathwork</button></div>',
     hint='Drag across the terrain') +
  light(f'<p class="kicker" data-r>Choose your length</p><h2 data-split>An hour, or ninety minutes.</h2>{tags("swedish")}<div class="note" data-r><strong>Want more pressure?</strong>Swedish stays light to medium. For deep pressure with stretching, book <a class="uline" href="deep-tissue-massage.html">deep tissue</a>.</div>') +
  faq(f_sw) + more(['deep', 'reiki', 'lymph', 'thai']), f_sw, 'Swedish massage: long strokes and essential oils at light to medium pressure; can include sound therapy, meditation and breathwork.')

# Deep tissue
f_dt = [('How much is a deep tissue massage in Salt Lake City?', '<p>$150 for 60 minutes or $180 for 90 minutes.</p>'),
        ('Is deep tissue massage painful?', '<p>No. It is therapeutic and never painful. Tell Miquelle how much pressure you want and she adjusts.</p>'),
        ('What else happens besides pressure?', '<p>Breathwork, stretching and movement to restore balance, plus stretching guidance to take home so the results last.</p>'),
        ('Is there anything deeper?', '<p><a href="sarga-bodywork.html">Sarga bodywork</a> goes deep into the fascia and suits old injuries. You need to be very comfortable with deep pressure.</p>')]
svc('deep', 'Deep Tissue Massage in Salt Lake City, from $150 | Earthen Phoenix', 'Deep tissue massage in Salt Lake City: deep pressure with breathwork, stretching and movement. Therapeutic, never painful. $150 for 60 minutes, $180 for 90.', 'massage-head-neck',
  lambda p: phero(p, 'massage-head-neck', 'Miquelle’s hands working at a client’s neck and shoulders', 'Plate 02 · Massage', 'Deep tissue.',
     'Deep pressure, breathwork, stretching and movement to restore balance. Therapeutic, and never painful. $150 for 60 minutes or $180 for 90.', [('Length', '60 / 90 min'), ('Price', '$150 / $180'), ('Pressure', 'Deep')], pos='50% 12%') +
  study('deep', 'A single point of pressure sinks into one knot as you breathe out and eases as you breathe in, until the knot comes down', 'Deeper on the out-breath', 'Slow, deep, and with you.',
     '<p>One point of pressure settles into one knot at a time. It sinks as you breathe out and eases as you breathe in, and the peak comes down a little with every breath. When it has softened, the work moves on. Choose how deep, the way you would tell Miquelle on the table.</p>',
     '<div class="range"><label for="depth">How deep? <output id="depthOut" for="depth">Deep</output></label><input type="range" id="depth" data-range="depth" min="0" max="2" step="1" value="2"></div>', rev=True) +
  light('<p class="kicker" data-r>In the session</p><h2 data-split>Pressure is one part of it.</h2>' + route([('Deep pressure', 'At the depth you ask for.'), ('Breathwork', 'The work follows your breathing.'), ('Stretching and movement', 'To restore balance.'), ('Take-home stretches', 'Guidance so the results last.')]) + tags('deep')) +
  faq(f_dt) + more(['sarga', 'thai', 'swedish', 'yoga']), f_dt, 'Deep tissue massage: deep pressure, breathwork, stretching and movement to restore balance, with stretching guidance to take home.')

# Thai
f_th = [('How much is Thai massage in Salt Lake City?', '<p>Thai bodywork is $150 for 60 minutes or $170 for 90 minutes.</p>'),
        ('What happens in Thai bodywork?', '<p>Full-body stretching combined with rhythmic compressions. Miquelle is certified in Thai bodywork.</p>'),
        ('How is it different from deep tissue?', '<p>Thai is built on stretching and rhythmic compressions; <a href="deep-tissue-massage.html">deep tissue</a> uses deep pressure with breathwork and stretching.</p>')]
svc('thai', 'Thai Bodywork in Salt Lake City, from $150 | Earthen Phoenix', 'Thai bodywork in Salt Lake City: full-body stretching and rhythmic compressions with Miquelle, certified in Thai bodywork. $150 for 60 minutes, $170 for 90.', 'yoga-assisted-fold',
  lambda p: phero(p, 'yoga-assisted-fold', 'Miquelle assisting a student’s stretch on a grassy hillside', 'Plate 03 · Bodywork', 'Thai bodywork.',
     'Full-body stretching combined with rhythmic compressions. $150 for 60 minutes or $170 for 90.', [('Length', '60 / 90 min'), ('Price', '$150 / $170'), ('Style', 'Rhythm + stretch')], pos='68% 50%') +
  study('thai', 'Palms press on a steady beat from the feet toward the hips, then the whole terrain is stretched long', 'Rhythm, then reach', 'Pressed on a beat, then drawn long.',
     '<p>Palms press on a steady beat, alternating sides, from the feet toward the hips. Then the whole body is drawn out in a long stretch and the ground widens and settles. Her booking page describes it as supporting the lymphatic, immune and nervous systems, muscles, tendons and joints. Tap the terrain to add a press.</p>',
     '<div class="ctrl"><button type="button" data-act="tap">Add a press</button></div>', hint='Tap to press') +
  light(f'<div class="study rev" style="align-items:start"><div class="reveal-img">{img("mountain-meadow", "Miquelle and a student in a mountain meadow", "(max-width: 900px) 90vw, 45vw", style="aspect-ratio:4/5;object-fit:cover;object-position:28% 50%")}</div><div><p class="kicker" data-r>Certified</p><h2 data-split>One of many ways she works.</h2><p class="lede" data-r style="margin-top:22px">Miquelle is certified in Thai bodywork, alongside Sarga, lymphatic work, cupping, cranial-sacral therapy, sound therapy, reflexology, yoga, Reiki and breath-work.</p>{tags("thai")}</div></div>') +
  faq(f_th) + more(['yoga', 'deep', 'sarga', 'swedish']), f_th, 'Thai bodywork: full-body stretching and rhythmic compressions.')

# Lymphatic
f_ly = [('How much is the lymphatic firming body treatment?', '<p>$180 for 90 minutes.</p>'),
        ('What is included?', '<p>Dry brushing, manual lymphatic massage, a heated body wrap, a hot towel cleanse and a head and neck treatment, finished with Eminence Coconut Firming cream.</p>'),
        ('What is it for?', '<p>The booking page describes it as a treatment for skin firming and for reducing bloating, water retention and inflammation. Choose it for a slow, full-body treatment rather than a pressure-focused massage.</p>')]
svc('lymph', 'Lymphatic Drainage &amp; Firming Treatment in Salt Lake City, $180 | Earthen Phoenix', 'A 90-minute lymphatic firming body treatment in Salt Lake City for $180: dry brushing, lymphatic massage, heated wrap, hot towel cleanse, head and neck, firming cream.', 'reiki-crystals-candles',
  lambda p: phero(p, 'reiki-crystals-candles', 'A client resting on the table with candles and crystals around her', 'Plate 04 · Body treatment', 'Lymphatic firming.',
     'A slow, 90-minute full-body treatment in six steps, from dry brushing to a firming cream. $180.', [('Length', '90 min'), ('Price', '$180'), ('Steps', '6')], pos='40% 50%') +
  study('lymph', 'A broad swelling drains away as light dots flow along dotted paths from the hands, feet and head toward the collarbone', 'Following the flow', 'Toward the collarbone.',
     '<p>This is not about peaks. It is about a broad, soft swelling. Light, manual lymphatic massage follows the body&rsquo;s own drainage paths: from the hands, feet and head toward the nodes, and on to the collarbone. The dotted lines are those paths. As the flow arrives, the whole field lowers.</p>') +
  light('<p class="kicker" data-r>The 90 minutes</p><h2 data-split>Six steps, one slow treatment.</h2>' + route([('Dry brushing', 'Long sweeps toward the heart.'), ('Lymphatic massage', 'Light and manual.'), ('Heated body wrap', 'Wrapped and warmed.'), ('Hot towel cleanse', 'The wrap comes off.'), ('Head and neck', 'A head and neck treatment.'), ('Firming cream', 'Eminence Coconut Firming.')], 3) + tags('lymph')) +
  faq(f_ly) + more(['swedish', 'reiki', 'zen', 'herbs']), f_ly, 'Lymphatic firming body treatment: dry brushing, manual lymphatic massage, heated body wrap, hot towel cleanse, head and neck treatment, Eminence Coconut Firming cream.')

# Sarga
f_sa = [('How much is Sarga bodywork in Salt Lake City?', '<p>$180 for 90 minutes.</p>'),
        ('Is Sarga uncomfortable?', '<p>It can be somewhat uncomfortable during the session. You must be very comfortable with deep pressure to receive it.</p>'),
        ('What is Sarga good for?', '<p>It is a barefoot method using a fabric strap for myofascial and deep tissue work, intended for old injuries.</p>')]
svc('sarga', 'Sarga Barefoot Bodywork in Salt Lake City, $180 | Earthen Phoenix', 'Sarga bodywork in Salt Lake City: a barefoot method with a fabric strap for deep myofascial work and old injuries. 90 minutes, $180. For people very comfortable with deep pressure.', 'sarga-barefoot-strap',
  lambda p: phero(p, 'sarga-barefoot-strap', 'Miquelle standing barefoot on a client’s back while holding an overhead bar', 'Plate 05 · Barefoot bodywork', 'Sarga.',
     'A barefoot method with a fabric strap, for myofascial and deep tissue work on old injuries. 90 minutes, $180.', [('Length', '90 min'), ('Price', '$180'), ('Pressure', 'Deepest')], pos='50% 28%') +
  study('sarga', 'Bare footprints step up the back one at a time, each pressing a deep hollow that spreads wide', 'Step by step', 'Bare feet, deep into the fascia.',
     '<p>Miquelle works barefoot, holding a strap overhead so she controls exactly how much weight goes into each step. Each footprint presses a deep hollow, and the pressure spreads wider than the foot, into the fascia around it. Tap the terrain to place a step yourself.</p>',
     '<div class="ctrl"><button type="button" data-act="tap">Take a step</button></div>', hint='Tap to step', rev=True) +
  light(f'<div class="study" style="align-items:start"><div><p class="kicker" data-r>Honest about intensity</p><h2 data-split>Is it for you?</h2><div class="note" data-r><strong>&ldquo;Must be very comfortable with deep pressure to receive this.&rdquo;</strong>Sarga can be somewhat uncomfortable during the session. If you would like deep work with less intensity, try <a class="uline" href="deep-tissue-massage.html">deep tissue</a>.</div>{tags("sarga")}</div><div class="reveal-img">{img("sarga-barefoot-strap", "Miquelle barefoot on a client’s back, holding the bar", "(max-width: 900px) 90vw, 40vw", style="aspect-ratio:4/5;object-fit:cover;object-position:50% 30%")}</div></div>') +
  faq(f_sa) + more(['deep', 'thai', 'zen', 'reiki']), f_sa, 'Sarga bodywork: a barefoot method using a fabric strap for myofascial and deep tissue work, intended for old injuries.')

# Reiki
f_re = [('How much does Reiki cost in Salt Lake City?', '<p>A 60-minute Reiki session is $130.</p>'),
        ('Do I stay clothed for Reiki?', '<p>Yes. Hands are placed gently on or near your clothed body.</p>'),
        ('What is Reiki?', '<p>A practitioner channels universal energy by gently placing hands on or near the clothed body to support balance and healing.</p>'),
        ('How long has Miquelle practised Reiki?', '<p>She started with Reiki in 2011 and is now a Master Reiki practitioner, also trained in sound therapy and breath-work.</p>')]
svc('reiki', 'Reiki in Salt Lake City, $130 for 60 Minutes | Earthen Phoenix', 'Reiki in Salt Lake City with Miquelle, a Master Reiki practitioner since 2011. 60 minutes, $130. Hands rest on or near your clothed body.', 'sound-tuning-forks',
  lambda p: phero(p, 'sound-tuning-forks', 'A client resting on a massage table with tuning forks beside her head', 'Plate 06 · Energy work', 'Reiki.',
     'Hands rest gently on or near your clothed body, to support balance and healing. 60 minutes with a Master Reiki practitioner, $130.', [('Length', '60 min'), ('Price', '$130'), ('Clothing', 'Stay clothed')], pos='45% 50%') +
  study('reiki', 'Two hands rest on or hover above the terrain; nothing presses down, yet the whole field slowly evens out', 'No pressure at all', 'Balance, not pressure.',
     '<p>Every other plate pushes the peaks down. This one does not press at all. Her hands rest on the body, or just above it, and the whole field slowly evens out: high places lower, low places lift, toward balance. Switch to &ldquo;near&rdquo; to lift the hands. Tap to move them.</p>',
     '<div class="ctrl" role="group" aria-label="Hands"><button type="button" data-set="reiki:on" aria-pressed="true">Hands on</button><button type="button" data-set="reiki:near" aria-pressed="false">Hands near</button></div>', hint='Tap to move the hands') +
  light('<p class="kicker" data-r>Her training</p><h2 data-split>Since 2011.</h2><p class="lede" data-r style="margin-top:22px">Miquelle started with Reiki in 2011 and is now a Master Reiki practitioner. Sound therapy and breath-work are part of her training too.</p>' + tags('reiki')) +
  faq(f_re) + more(['swedish', 'yoga', 'lymph', 'astro']), f_re, 'Reiki: hands gently on or near the clothed body to support balance and healing, 60 minutes.')

# Zen mountain
f_zn = [('What is the Zen mountain session?', '<p>A private massage beside a peaceful mountain river, combining therapeutic massage with nature for relaxation and a reset. 90 minutes.</p>'), ('How much is it?', '<p>$200 for 90 minutes.</p>'),
        ('Where is it, and when can I book it?', f'<p>Call or text {PHONE} and ask Miquelle about the location and the season.</p>')]
svc('zen', 'Zen Mountain Massage Session, $200 | Earthen Phoenix', 'The Zen mountain session: a private 90-minute massage beside a peaceful mountain river, $200. Therapeutic massage and nature together for relaxation and a reset.', 'mountain-meadow',
  lambda p: phero(p, 'mountain-meadow', 'A green meadow below steep, snow-streaked mountains', 'Plate 07 · Outdoors', 'Zen mountain.',
     'A private massage beside a peaceful mountain river: therapeutic massage and nature, for relaxation and a reset. 90 minutes, $200.', [('Length', '90 min'), ('Price', '$200'), ('Where', 'By a river')], pos='62% 40%',
     ctas=f'<a class="btn sun" href="{TEL}">Ask about location and season {AR}</a><a class="btn ghost" href="{BOOK}">Booking page</a>') +
  study('zen', 'Mountain ridges with a river winding through the meadow; the water rushes at first and grows still the longer you stay', 'The one real map', 'Stay. The river slows.',
     '<p>On this plate the mountains are real mountains, and the line through the meadow is a river. It starts out rushing. Stay with it and it settles; move fast across it and it stirs again. That is roughly the idea of ninety minutes outside, by the water.</p>', hint='Stay a while', wide=True) +
  light(f'<p class="kicker" data-r>One private session</p><h2 data-split>Ninety minutes outside.</h2>{tags("zen")}<div class="note" data-r><strong>Location and season</strong>Call or text <a class="uline" href="{TEL}">{PHONE}</a> and ask Miquelle where and when.</div>') +
  faq(f_zn) + more(['yoga', 'swedish', 'sarga', 'reiki']), f_zn, 'A private 90-minute massage beside a peaceful mountain river, for relaxation and reset.')

# Yoga
f_yo = [('How much is private yoga in Salt Lake City?', '<p>$140 for 60 minutes, private or split between group participants.</p>'),
        ('What style of yoga is it?', '<p>Schole yoga: traditional asanas guided to move with your own breath and natural abilities. Vinyasa flow, then slow Yin holds at the end.</p>'),
        ('Do I need experience?', f'<p>The practice guides you to use your own intuition to get into your body and flow, rather than being told exactly how and when to move. Call or text {PHONE} with any questions.</p>')]
svc('yoga', 'Private Yoga in Salt Lake City, $140 | Earthen Phoenix', 'Private yoga in Salt Lake City with Miquelle: Schole yoga, Vinyasa flow then slow Yin holds, guided by your own breath. $140 for 60 minutes, private or split between a group.', 'yoga-assisted-fold',
  lambda p: phero(p, 'mountain-meadow', 'Miquelle and a student practising yoga in a mountain meadow', 'Plate 08 · Schole yoga', 'Private yoga.',
     'Traditional asanas, moving with your own breath: fun Vinyasa flow, then slow Yin holds. $140 for 60 minutes, for you or split with a group.', [('Length', '60 min'), ('Price', '$140'), ('Who', 'You, or a group')], pos='28% 50%') +
  study('yoga', 'The terrain moves in waves during the Vinyasa flow, then goes almost still and breathes slowly during the Yin hold', 'Flow, then hold', 'Moving ground, then still ground.',
     '<p>While you flow through Vinyasa, the ground moves in waves with the breath. In the Yin hold it goes quiet and simply breathes. Tap during the hold to flow again.</p><p style="margin-top:16px">&ldquo;This practice is to guide you into using your own intuition to get into your body and flow verse being told exactly how and when to move.&rdquo;</p>', hint='Tap to flow again') +
  light(f'''<div class="study" style="align-items:center"><div><p class="kicker" data-r>Private or split</p><h2 data-split>One price, shared how you like.</h2><p class="lede" data-r style="margin-top:22px">Book the hour for yourself, or split it between group participants. The session is $140 either way.</p>
  <div class="range" data-r><label for="people">People <output id="peopleOut" for="people">Just you</output></label><input type="range" id="people" min="1" max="6" step="1" value="1"></div><output class="big-out" id="share" aria-live="polite" data-r>$140 for your private hour</output></div>
  <div class="reveal-img">{img("yoga-assisted-fold", "Miquelle guiding a student into a forward bend on the grass", "(max-width: 900px) 90vw, 45vw", style="aspect-ratio:4/5;object-fit:cover;object-position:62% 50%")}</div></div>''') +
  faq(f_yo) + more(['thai', 'reiki', 'zen', 'deep']), f_yo, 'Private Schole yoga: Vinyasa flow followed by slow Yin holds, guided by your own breath; private or split between group participants.')

# Astrology & tarot
f_as = [('How much is an astrology or tarot reading?', '<p>$2 per minute. A 30-minute reading comes to $60.</p>'),
        ('What does an astrology reading cover?', '<p>It works with your birth chart to explore your personality and desires, toward greater self-appreciation, acceptance and acknowledgment.</p>'),
        ('Tarot or oracle?', '<p>Both are about the present moment. Tarot helps you consider a problem, give a voice to it, work it through and see where the blocks might be. Oracle can provide guidance in a light-hearted way.</p>')]
months = ''.join(f'<option value="{i + 1}">{m}</option>' for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']))
svc('astro', 'Astrology &amp; Tarot Readings in Salt Lake City, $2/min | Earthen Phoenix', 'Astrology birth-chart readings and tarot or oracle card readings with Miquelle in Salt Lake City, $2 per minute.', 'reiki-crystals-candles',
  lambda p: phero(p, 'reiki-crystals-candles', 'Crystals, a sage bundle and lit candles around a client resting on the table', 'Plate 09 · Readings', 'Astrology and tarot.',
     'Birth-chart readings, and tarot and oracle readings about the present moment. $2 per minute.', [('Price', '$2 / min'), ('30 min', '$60'), ('Kinds', 'Chart · Tarot · Oracle')], pos='60% 50%') +
  study('astro', 'A night sky over a low horizon, with the stars of your sun sign joined one by one', 'The sky over your horizon', 'Your sun, above the map.',
     '<p>Astrology offers us a unique understanding of our conscious and subconscious selves, primarily through our birth charts. By exploring our birth chart, we can better understand our personalities and desires, leading to greater self-appreciation, acceptance, and acknowledgment.</p>',
     f'<div class="sel"><label class="vh" for="month">Birth month</label><select id="month">{months}</select><label class="vh" for="day">Birth day</label><select id="day"></select></div><p id="signOut" aria-live="polite" style="margin-top:16px;color:var(--y)"></p><p style="font-size:.9rem;margin-top:6px">Star patterns are stylised. A reading uses your full birth chart, not only your sun sign.</p>') +
  light(f'''<div class="study" style="align-items:start"><div><p class="kicker" data-r>Tarot and oracle</p><h2 data-split>About the present moment.</h2><p class="lede" data-r style="margin-top:22px">Tarot empowers you to consider a problem, give a voice to it, work it through and see where the blocks might be. Oracle can provide guidance in a light hearted way.</p>
  {route([('Consider a problem', 'Bring the question you are carrying.'), ('Give a voice to it', 'Say it out loud, with the cards.'), ('Work it through', 'Together, at your pace.'), ('See the blocks', 'Where things might be stuck.')], 2)}</div>
  <div><p class="kicker" data-r>Priced by the minute</p><h2 data-split>$2 a minute.</h2><div class="ctrl" data-r style="color:var(--ink)">{''.join(f'<button type="button" data-mins="{m}" aria-pressed="{"true" if m == 30 else "false"}">{m} min</button>' for m in (15, 30, 45, 60))}</div><p class="cost" id="cost" aria-live="polite" data-r style="color:var(--cta);margin-top:20px">$60</p><p class="mono" id="costNote" style="color:var(--ink-2)">30 minutes at $2 a minute</p></div></div>''') +
  faq(f_as) + more(['herbs', 'reiki', 'yoga', 'zen']), f_as, 'Astrology readings using birth charts, and tarot or oracle card readings focused on the present moment, at $2 per minute.')

# Herbalism
f_hb = [('How much is an herbalism consultation?', '<p>About $40 to $100. Customization, consultation and pricing vary with time and herb prices at the time of purchase.</p>'), ('What kind of remedies?', '<p>Customized herbal remedies: teas, rollies and tinctures.</p>'),
        ('How long do the herbs take?', '<p>Allow one to two weeks. The herbs come from Mountain Rose Herbs in Oregon.</p>')]
svc('herbs', 'Herbalism Consultations &amp; Custom Herbal Remedies, Salt Lake City | Earthen Phoenix', 'Herbalism consultations in Salt Lake City with custom teas, rollies and tinctures made for you. About $40 to $100; herbs arrive from Mountain Rose Herbs in Oregon in 1 to 2 weeks.', 'armature-smooth-sailing-face-oil',
  lambda p: phero(p, 'armature-smooth-sailing-face-oil', 'An amber dropper bottle beside fresh rosemary and tumbled crystals', 'Plate 10 · “Plants — those who take care of us.”', 'Herbalism.',
     'A consultation, then remedies made for you: teas, rollies or tinctures. About $40 to $100.', [('Price', '~$40–$100'), ('Forms', '3'), ('Herbs arrive', '1–2 weeks')], pos='50% 50%', ctas=f'<a class="btn sun" href="{BOOK}">Book a consultation {AR}</a><a class="btn ghost" href="contact.html">Ask about herbs</a>') +
  study('herbs', 'Green rings spreading through still water: a slow wide steep for tea, small drops for a tincture, a rolling line for a rollie', 'Made for you', 'Three ways a remedy spreads.',
     '<p>Customized herbal remedies: teas, rollies, and tinctures balance the mind-body and spirit. Each one meets you differently: a tea steeps slowly and spreads wide, a tincture works a few drops at a time, a rollie goes exactly where you put it. Choose one, or tap to add a drop.</p>',
     '<div class="ctrl" role="group" aria-label="Remedy"><button type="button" data-set="vessel:tea" aria-pressed="true">Teas</button><button type="button" data-set="vessel:tincture" aria-pressed="false">Tinctures</button><button type="button" data-set="vessel:rollie" aria-pressed="false">Rollies</button></div>', hint='Tap to add a drop') +
  light('<p class="kicker" data-r>How it works</p><h2 data-split>From a conversation to a remedy.</h2>' + route([('A consultation', 'You and Miquelle talk through what you need.'), ('Herbs are ordered', 'From Mountain Rose Herbs in Oregon.'), ('One to two weeks', 'Allow that long for the herbs to arrive.'), ('Your remedy', 'Made for you: a tea, a rollie or a tincture.')]) +
        '<div class="tags" data-r><div style="max-width:520px"><b>$40–$100</b><span>Approx. Customization, consultation and pricing vary with time and herb prices at the time of purchase.</span></div></div>') +
  faq(f_hb) + more(['astro', 'reiki', 'lymph', 'yoga']), f_hb, 'Herbalism consultation and customized herbal remedies (teas, rollies and tinctures), approximately $40 to $100.')

# ===================================================================== ABOUT
certs = [('Sarga', 'sarga-bodywork.html'), ('Lymphatic', 'lymphatic-firming-treatment.html'), ('Thai Bodywork', 'thai-bodywork.html'), ('Cupping', None), ('Cranial-Sacral Therapy', None), ('Sound Therapy', 'reiki.html'), ('Reflexology', None), ('Yoga', 'private-yoga.html'), ('Reiki', 'reiki.html'), ('Breath-Work', None)]
page(slug='about.html', title='About Miquelle, Massage Therapist &amp; Reiki Master | Earthen Phoenix', og='miquelle-portrait', trail=[('Home', 'index.html'), ('About', 'about.html')], ld=[{'@type': 'AboutPage', 'name': 'About Miquelle'}],
     desc='Meet Miquelle of Earthen Phoenix: Reiki since 2011, Utah College of Massage Therapy graduate 2012, Master Reiki practitioner, yoga teacher, certified in Sarga, Thai, lymphatic and more.',
     body=lambda p: phero(p, 'mountain-meadow', 'Mountains above the meadow where Miquelle teaches', 'Meet Miquelle', 'Individual needs.',
        'Miquelle founded Earthen Phoenix in Salt Lake City. She started with Reiki in 2011, graduated from the Utah College of Massage Therapy in 2012 and is now a Master Reiki practitioner.', [('Since', '2011'), ('Years', '13+'), ('Certified in', '10')], pos='62% 40%', ctas=f'<a class="btn sun" href="{BOOK}">Get an appointment {AR}</a><a class="btn ghost" href="sessions.html">Her sessions</a>') +
     f'''<section class="sec"><div class="wrap meet" style="align-items:start">
  <div class="por reveal-img" style="position:sticky;top:100px">{img('miquelle-portrait', 'Miquelle smiling at sunset on the water', '(max-width: 900px) 90vw, 420px')}</div>
  <div><p class="kicker" data-r>In her words</p><h2 data-split>Everyone is extremely unique.</h2>
  <div class="words" data-r style="margin-top:30px">
  <p>I have spent the last thirteen years learning the integrative aspects that include the mind, body, and spirit. I started with Reiki in 2011 and am now a Master Reiki practitioner. I graduated from the Utah College of Massage Therapy in 2012.</p>
  <p>I have worked with many different people, backgrounds, and bodies. Everyone is extremely unique. I base my work off individual needs; and can accommodate anything from light and relaxing to deep fascial work.</p>
  <p>I believe in all modalities that work for you. I have learned through my own experiences that by working with the practitioner and modalities that call to you, you innately empower your own ability to heal.</p>
  <p>I teach and practice yoga as well as meditation. I am grateful to facilitate space for anyone who is looking to heal. Thank you for your time and I look forward to working together.</p></div>
  <p class="kicker" data-r style="margin-top:50px">Certified in</p><div class="certs" data-r>{''.join(f'<a href="{h}">{n} →</a>' if h else f'<span>{n}</span>' for n, h in certs)}</div></div></div></section>
<section class="sec dark"><div class="wrap"><p class="kicker" data-r>The name</p><p class="state" data-split>&ldquo;In the face of adversity, remember that you are <em>a phoenix rising from the ashes.</em>&rdquo;</p></div></section>
''')

# ===================================================================== PRODUCTS
page(slug='products.html', title='Body Oil, Face Oil &amp; Body Butter | Earthen Phoenix', og='armature-aurora-body-oil', trail=[('Home', 'index.html'), ('Products', 'products.html')],
     desc='Take the care home: Armature Aurora Signature Body Oil ($44), Armature Smooth Sailing Face Oil ($55) and M’s Secret Body Butter ($44) from Earthen Phoenix in Salt Lake City.',
     ld=[{'@type': 'Product', 'name': strip(n), 'image': SITE + f'assets/img/{im}-800.webp', 'offers': {'@type': 'Offer', 'price': pr[1:], 'priceCurrency': 'USD', 'url': u, 'seller': {'@id': SITE + '#business'}}} for n, pr, im, a, u in PROD],
     body=lambda p: phero(p, 'armature-aurora-body-oil', 'Amber bottles of body oil on a white shell dish', 'Oils and butter', 'Take it home.',
        'Two Armature oils and M’s Secret Body Butter, from $44. Checkout happens in the Earthen Phoenix online store.', [('From', '$44'), ('Products', '3'), ('Checkout', 'Online store')], pos='50% 60%', ctas=f'<a class="btn sun" href="#shelf">See the shelf {AR}</a>') +
     f'<section class="sec" id="shelf"><div class="wrap"><p class="kicker" data-r>The shelf</p><h2 data-split>Oils and butter.</h2>{shelf(True)}<p data-r style="margin-top:40px;color:var(--ink-2)">Need help choosing? <a class="uline" href="contact.html">Contact us</a> or call {PHONE}.</p></div></section>')

# ===================================================================== FAQ
ALLFAQ = [('Booking and visiting', [('Where is Earthen Phoenix?', '<p>In Salt Lake City, Utah. The Zen mountain session takes place outdoors beside a mountain river; ask Miquelle about its location and season.</p>'),
            ('How do I book?', f'<p>Use the <a href="{BOOK}">online booking page</a>, call or text {PHONE}, or email {EMAIL}.</p>'), ('Is there a first-time discount?', '<p>Yes. Mention you are a first-time client for 20% off your first service.</p>'),
            ('Which session should I choose?', '<p>See how each one works on <a href="sessions.html">Sessions &amp; prices</a>. Still unsure? Call or text and Miquelle will help you choose.</p>')]),
          ('Massage and bodywork', [('How much does a massage cost?', '<p>Swedish $140 / $170, deep tissue $150 / $180, Thai bodywork $150 / $170 (60 / 90 minutes). Lymphatic firming and Sarga are $180 for 90 minutes; the Zen mountain session is $200 for 90 minutes.</p>'),
            ('Is deep tissue painful?', '<p>No. It is therapeutic and never painful.</p>'), ('Is Sarga uncomfortable?', '<p>It can be somewhat uncomfortable. You must be very comfortable with deep pressure to receive it.</p>'),
            ('What is in the lymphatic firming treatment?', '<p>Dry brushing, manual lymphatic massage, a heated body wrap, a hot towel cleanse and a head and neck treatment, finished with Eminence Coconut Firming cream.</p>')]),
          ('Reiki and yoga', [('Do I stay clothed for Reiki?', '<p>Yes. Hands are placed gently on or near the clothed body. $130 for 60 minutes.</p>'), ('Can I share a yoga session?', '<p>Yes. $140 for 60 minutes, private or split between group participants.</p>')]),
          ('Readings and remedies', [('How are readings priced?', '<p>Astrology, tarot and oracle readings are $2 per minute.</p>'), ('How long do herbal remedies take?', '<p>Allow one to two weeks for herbs to arrive from Mountain Rose Herbs in Oregon. Consultations are about $40 to $100.</p>')]),
          ('About Miquelle', [('What is Miquelle’s training?', '<p>Reiki since 2011, now a Master Reiki practitioner; Utah College of Massage Therapy, 2012; certified in Sarga, lymphatic, Thai bodywork, cupping, cranial-sacral therapy, sound therapy, reflexology, yoga, Reiki and breath-work.</p>')])]
page(slug='faq.html', title='Questions about Massage, Reiki &amp; Yoga | Earthen Phoenix', og='sound-tuning-forks', trail=[('Home', 'index.html'), ('Questions', 'faq.html')], ld=[faq_ld([qa for _, g in ALLFAQ for qa in g])],
     desc='Answers about Earthen Phoenix in Salt Lake City: booking, the 20% first-visit discount, massage, Sarga, Reiki, yoga, readings, herbal remedies and Miquelle’s training.',
     body=lambda p: phero(p, 'sound-tuning-forks', 'Tuning forks resting beside a client on the massage table', 'Questions', 'Good questions.', 'Short answers about booking, prices, what each session feels like, and Miquelle’s training.', None, pos='40% 50%',
        ctas=f'<a class="btn sun" href="{BOOK}">Get an appointment {AR}</a><a class="btn ghost" href="contact.html">Ask your own</a>') +
     '<section class="sec"><div class="narrow">' + ''.join(f'<div data-r style="margin-bottom:70px"><p class="kicker">{t}</p><div class="faq" style="margin-top:0">' + ''.join(f'<details><summary>{q}<i aria-hidden="true"></i></summary><div class="a">{a}</div></details>' for q, a in g) + '</div></div>' for t, g in ALLFAQ) + '</div></section>')

# ===================================================================== CONTACT
opts = ''.join(f'<option>{v["full"]}</option>' for v in SV.values()) + '<option>Products</option><option>Something else</option>'
page(slug='contact.html', title='Contact &amp; Booking | Earthen Phoenix, Salt Lake City', og='reiki-crystals-candles', trail=[('Home', 'index.html'), ('Contact', 'contact.html')], ld=[{'@type': 'ContactPage', 'name': 'Contact Earthen Phoenix'}],
     desc='Book Earthen Phoenix online, call or text 801-609-4263, or email info@earthenphoenix.com. Massage, Reiki, yoga and readings in Salt Lake City. 20% off your first service.',
     body=lambda p: phero(p, 'reiki-crystals-candles', 'Lit candles and crystals around a client on the massage table', 'Contact and booking', 'Reach out.',
        'Feel free to contact me with any questions anytime. Book online, call or text 801-609-4263, or email info@earthenphoenix.com.', [('Phone', PHONE), ('Office', 'Salt Lake City'), ('First visit', '20% off')], pos='45% 50%',
        ctas=f'<a class="btn sun" href="{BOOK}">Get an appointment {AR}</a><a class="btn ghost" href="{TEL}">Call or text</a>') +
     f'''<section class="sec dark"><div class="wrap study" style="align-items:start">
  <div data-r><p class="kicker">Ways in</p><h2>Call, text, or write.</h2>
    <ul class="ways"><li><a href="{BOOK}"><small>Book online</small><span>Booking page →</span></a></li><li><a href="{TEL}"><small>Call</small><span>{PHONE}</span></a></li><li><a href="{SMS}"><small>Text</small><span>{PHONE}</span></a></li><li><a href="mailto:{EMAIL}"><small>Email</small><span>{EMAIL}</span></a></li></ul></div>
  <form class="f" id="note" novalidate data-r style="--d:1">
    <p class="kicker" style="margin:0;color:var(--ink-2)">Send a note</p>
    <div class="two"><label>Your name<input name="name" autocomplete="name" required></label><label>Phone or email<input name="reply" autocomplete="email" required></label></div>
    <label>Asking about<select name="service"><option value="">Choose one (optional)</option>{opts}</select></label>
    <label>Message<textarea name="message" required></textarea></label>
    <label class="chk"><input type="checkbox" name="first" value="1"> This will be my first visit (20% off my first service)</label>
    <div class="pick" role="radiogroup" aria-label="Send it by"><label><input type="radio" name="how" value="email" checked> Email</label><label><input type="radio" name="how" value="text"> Text</label></div>
    <p class="err" role="alert"></p>
    <button class="btn" type="submit" style="justify-self:start">Write my message {AR}</button>
    <p class="fine">This opens your own email or text app with your message filled in, ready for you to send. Nothing is stored on this website.</p>
    <p class="fine sent" hidden>Your message should now be open in your email or text app. If nothing opened, call or text {PHONE}.</p>
  </form></div></section>''')

page(slug='404.html', title='Page not found | Earthen Phoenix', desc='This page has moved or no longer exists.',
     body=lambda p: f'<section class="err404"><div><p class="kicker" style="justify-content:center">404 · Off the map</p><h1 data-split>Off the map.</h1><p class="lede" style="margin:24px auto 34px">This page has moved or no longer exists.</p><div class="row" style="justify-content:center"><a class="btn sun" href="index.html">Home {AR}</a><a class="btn ghost" href="sessions.html">Sessions</a></div></div></section>')

# ===================================================================== WRITE
for p in PAGES:
    body = p['body'](p) if callable(p['body']) else p['body']
    out = head(p) + header(p) + body + footer(p)
    with open(os.path.join(ROOT, p['slug']), 'w', encoding='utf-8', newline='\n') as f: f.write(out)
    print('wrote', p['slug'], len(out) // 1024, 'KB')
with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}{"" if p["slug"] == "index.html" else p["slug"]}</loc><lastmod>2026-10-31</lastmod></url>\n' for p in PAGES if p['slug'] != '404.html') + '</urlset>\n')
with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8') as f: f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
with open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8') as f:
    f.write('# Earthen Phoenix\n\n> Massage, bodywork, Reiki, private yoga, astrology, tarot and herbal remedies with Miquelle in Salt Lake City, Utah. "Ground your soul."\n\n'
            f'- Phone / text: {PHONE}\n- Email: {EMAIL}\n- Booking: {BOOK}\n- First-time clients: 20% off the first service\n- Miquelle: Reiki since 2011 (Master Reiki practitioner); Utah College of Massage Therapy 2012.\n\n## Sessions\n\n' +
            ''.join(f'- [{v["full"]}]({SITE}{v["href"]}): {v["price"]}, {v["lens"]}. {v["line"]}.\n' for v in SV.values()))
with open(os.path.join(ROOT, '_redirects'), 'w', encoding='utf-8') as f:
    f.write('/home  /  301\n/about-us  /about.html  301\n/classes  /private-yoga.html  301\n/products-list  /products.html  301\n/shop  /products.html  301\n/services.html  /sessions.html  301\n/contact  /contact.html  301\n/thankyou-8490  /contact.html  301\n/*  /404.html  404\n')
print('done')
