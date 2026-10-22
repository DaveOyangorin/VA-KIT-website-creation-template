from build import U, S, ARROW, PHONE, img, faq_html, cta, quote_form

LOCK_SVG = '''<svg class="lock" viewBox="0 0 260 260" aria-hidden="true"><defs><linearGradient id="alg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f1f3f5"/><stop offset=".45" stop-color="#b9bfc6"/><stop offset=".55" stop-color="#d9dde1"/><stop offset="1" stop-color="#8d949c"/></linearGradient></defs>
<g class="t t1"><path d="M20 20h104v14h-10v76H20z"/><path class="lip" d="M114 34h10v76h-10z"/></g>
<g class="t t2"><path d="M136 20h104v90h-90V34h-14z"/><path class="lip" d="M136 34h14v76h-14z"/></g>
<g class="t t3"><path d="M20 150h94v-14h10v104H20z"/><path class="lip" d="M114 136h10v14h-10z"/></g>
<g class="t t4"><path d="M136 136h104v104H136v-90h14v-14z"/><path class="lip" d="M136 136h14v14h-14z"/></g>
<circle class="ring" cx="130" cy="130" r="18"/><path class="tick" d="M122 130l6 6 11-12"/></svg>'''

PICK = [("Matte Black", "#43464d", "matte-black-aluminum-shingle-home", "Home with a matte black aluminum shingle roof"),
        ("Brick Red", "#7d2912", "brick-red-aluminum-shingle-stone-cottage", "Stone cottage with a brick-red aluminum shingle roof"),
        ("Brown Stone", "#957271", "brown-stone-aluminum-shingle-home", "Two-story home with a brown aluminum shingle roof"),
        ("Classic Green", "#598979", "green-aluminum-shingle-mountain-home", "Mountain home with a green aluminum shingle roof"),
        ("Copper Penny", "#ad7c55", "copper-aluminum-shingle-a-frame", "A-frame home with a copper-colored aluminum shingle roof"),
        ("Granite Gray", "#747474", "gray-aluminum-shingle-two-story-home", "Two-story home with a gray aluminum shingle roof"),
        ("Sierra Tan", "#9d7c67", "", ""),
        ("Polar White", "#f2f2f0", "", "")]


def build(r, swatches):
    faqs = [
        ("How does the interlocking roofing system work?",
         "Four-sided interlocks connect each shingle to the surrounding shingles. The shingles work together with underlayment and properly fitted flashings at edges, valleys, walls and roof penetrations. Roof slope and project details determine the installation approach."),
        ("Can aluminum shingles be installed over my existing roof?",
         "A roof-over may be possible on some homes. The condition of the existing roof, the number of roof layers, decking, local requirements and installation instructions determine whether removal is needed. The existing roof needs to be assessed before deciding."),
        ("Do you sell roofing materials to contractors?",
         "Yes. We sell aluminum roofing materials to roofers. Contact us with your project location, the products you are considering and approximate quantities to discuss components and ordering arrangements."),
    ]
    chips = ""
    for i, (n, c, im, alt) in enumerate(PICK):
        if im:
            chips += f'<button type="button" class="pc{" on" if i == 3 else ""}" data-src="@img/{im}.webp" data-alt="{alt}" data-name="{n}" style="--c:{c}"><i></i><span>{n}</span></button>'
        else:
            chips += f'<button type="button" class="pc nophoto" data-name="{n}" style="--c:{c}"><i></i><span>{n}</span></button>'
    first = PICK[3]
    gal = [("green-aluminum-shingle-commercial-mountains", "Building with a green aluminum shingle roof below snow-capped mountains", "Classic Green", "big"),
           ("copper-aluminum-shingle-arched-roof", "Arched roof covered in copper-colored aluminum shingles", "Copper Penny", ""),
           ("red-aluminum-shingle-white-home", "White home with a red aluminum shingle roof", "Brick Red", ""),
           ("copper-aluminum-shingle-log-home", "Log home with a copper-colored aluminum shingle roof", "Copper Penny", ""),
           ("gray-aluminum-shingle-home-aerial", "Home with a gray aluminum shingle roof seen from above", "Granite Gray", "tall"),
           ("gray-aluminum-shingle-bungalow", "Bungalow with a gray aluminum shingle roof", "Granite Gray", ""),
           ("copper-aluminum-shingle-roof-snow", "Copper-colored aluminum shingle roof with snow along the eaves", "Copper Penny", "wide")]
    gallery = "".join(f'<figure class="g {k} reveal">{img(n, a)}<figcaption><span>Nº {i + 1:02d}</span>{c}</figcaption></figure>' for i, (n, a, c, k) in enumerate(gal))
    body = f'''
<section class="hero">{img("aluminum-shingle-home-deep-snow", "Mountain home with an aluminum shingle roof surrounded by deep snow", priority=True)}
<div class="wrap hero-in">
<div class="hero-text">
<p class="label light">Aluminum Lock Roofing &middot; Salt Lake City, Utah</p>
<h1>Salt Lake City roofing company for <span>aluminum shingle roofs.</span></h1>
<p class="lede">Aluminum Lock Roofing is a roofing company in Salt Lake City that manufactures, supplies and installs interlocking aluminum shingle roofs. We give homeowners the classic look of shingles in aluminum, and we sell aluminum roofing materials to roofers.</p>
<div class="btn-row"><a class="btn" href="@/contact-us/">Start Your Project {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
</div>
<div class="lockbox">{LOCK_SVG}<p><b>Four-sided interlock</b><span>Each shingle locks to the ones around it.</span></p></div>
</div></section>

<section class="statband" aria-label="What the roofing system is made of"><div class="wrap">
<div class="stat"><b>4<sup>sides</sup></b><span>Interlocks connect each shingle to its neighbors</span></div>
<div class="stat"><b>0<sup>rust</sup></b><span>Aluminum does not rust like steel</span></div>
<div class="stat"><b>8<sup>colors</sup></b><span>Shingle finishes, from Matte Black to Polar White</span></div>
<div class="stat"><b>2<sup>ways</sup></b><span>We install roofs and supply materials to roofers</span></div>
</div></section>

<section class="sec picker-sec"><div class="wrap">
<div class="head reveal"><p class="label">Shingle colors</p><h2>Eight finishes. <span>Pick one, see a real roof.</span></h2><p class="lede">Every photo is an Aluminum Lock roof. Choose the color that suits your home; colors on screen are approximate, so ask to see the finish options for your project.</p></div>
<div class="picker reveal">
<figure class="pick-view"><img src="@img/{first[2]}.webp" alt="{first[3]}" width="1600" height="1067" loading="lazy" decoding="async"><figcaption><span class="pv-dot" style="--c:{first[1]}"></span><b class="pv-name">{first[0]}</b><span class="pv-note">Aluminum Lock roof</span></figcaption></figure>
<div class="pick-list" role="group" aria-label="Shingle colors">{chips}</div>
</div></div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">Roofers in Salt Lake City</p><h2>Interlocking aluminum roofing <span>built for long-term protection</span></h2>
<p>Aluminum Lock Roofing manufactures and supplies aluminum locking roof systems that combine the appearance of traditional shingles with the durability of aluminum. Our focus is a durable roofing system with lasting visual appeal.</p>
<p>As a roofing contractor in Salt Lake City, we install aluminum shingle roofs for homeowners and help you assess the right installation approach for your property. Performance depends on the complete roof assembly, site conditions and correct installation, so we look at all three.</p>
<a class="tlink" href="@/about-us/">About Aluminum Lock Roofing {ARROW}</a></div>
<div class="duo-who reveal">
<a href="@/services/">{img("gray-aluminum-shingle-two-story-home", "Two-story home with a gray aluminum shingle roof")}<span><small>For homeowners</small><b>Aluminum shingle roof installation</b></span></a>
<a href="@/services/#materials">{img("copper-aluminum-shingle-new-construction", "Copper-colored aluminum shingles going onto a new home")}<span><small>For roofers &amp; builders</small><b>Aluminum roofing materials</b></span></a>
</div>
</div></section>

<section class="sec dark system-sec"><div class="wrap split">
<div class="reveal"><p class="label light">How it works</p><h2>The shingle is one layer. <span>The roof is a system.</span></h2>
<p class="lede">Underlayment and correctly fitted flashings at eaves, rakes, valleys, walls and penetrations work together with the shingles to manage water.</p>
<ul class="spec">
<li><span>01</span><div><b>Four-sided interlocks</b><p>Interlocking edges help form a connected roofing surface.</p></div></li>
<li><span>02</span><div><b>Concealed attachment</b><p>Fewer exposed fasteners across the shingle field.</p></div></li>
<li><span>03</span><div><b>Room to move</b><p>Installation details accommodate expansion and contraction.</p></div></li>
<li><span>04</span><div><b>Perimeter flashings</b><p>Flashings direct water at roof edges and transitions.</p></div></li>
</ul></div>
<div class="explode-wrap reveal"><div class="explode" aria-hidden="true"><div class="ly l4"></div><div class="ly l3"></div><div class="ly l2"></div><div class="ly l1"></div></div>
<ol class="ly-key"><li><i class="k4"></i>Interlocking aluminum shingles</li><li><i class="k3"></i>Perimeter flashing</li><li><i class="k2"></i>Underlayment</li><li><i class="k1"></i>Roof deck</li></ol></div>
</div></section>

<section class="sec archive"><div class="wrap">
<div class="head reveal"><p class="label">From the gallery</p><h2>Aluminum shingle roofs, <span>home by home</span></h2><p class="lede">Log homes, cottages, A-frames, cabins and commercial buildings.</p></div>
<div class="gwall">{gallery}</div>
<a class="tlink" href="@/services/">See more on the services page {ARROW}</a>
</div></section>

<section class="sec white"><div class="wrap ask-grid">
<div class="reveal"><p class="label">Plan for your climate</p><h2>Built around Utah <span>snow, wind and sun</span></h2>
<p>Every roof faces different conditions. We can discuss the roof assembly and installation details appropriate for your location.</p>
<ul class="ticks"><li>Snow loads and safe snow-shedding details</li><li>Local wind requirements and fastening details</li><li>Finish selection and exposure conditions</li><li>Thermal movement and moisture management</li><li>Roof color, ventilation and thermal performance</li></ul></div>
<div class="reveal"><p class="label">Before you choose</p><h2>What to ask <span>before choosing a roof</span></h2>
<ol class="asks">
<li><b>What does the estimate include?</b> Preparation, any necessary removal, materials and finishing details.</li>
<li><b>Can it go over my existing roof?</b> That depends on the roof&rsquo;s condition, the number of layers, the decking, local requirements and the installation instructions.</li>
<li><b>What does the written warranty cover?</b> Review its coverage, exclusions and maintenance requirements, and which terms apply to materials and installation.</li>
<li><b>Which specifications apply to my roof?</b> Snow, wind and slope all shape the installation approach.</li>
</ol></div>
</div></section>

<section class="sec dark"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label light">Getting started</p><h2>Three simple steps <span>to a new roof</span></h2>
<ol class="steps" style="margin-top:24px">
<li><h3>Send us your project details</h3><p>Your location, current roof type, and whether you need installation or materials.</p></li>
<li><h3>Consultation</h3><p>We discuss the property, the existing roof and the result you want, and what your estimate includes.</p></li>
<li><h3>Roof installation</h3><p>Shingles, underlayment and flashings installed as one system.</p></li>
</ol></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">FAQ</p><h2>Questions about <span>aluminum shingles</span></h2><p class="lede">More answers on the <a href="@/faq/">FAQ page</a>, and the full story on roof-overs in our guide.</p>
<a class="btn navy" href="@/blog/can-you-put-a-new-roof-over-an-old-roof/">Can you roof over an old roof? {ARROW}</a></div>
<div class="reveal">{faq_html(faqs)}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company Salt Lake City | Aluminum Lock Roofing",
            "meta": "Aluminum Lock Roofing is a Salt Lake City roofing company installing interlocking aluminum shingle roofs and supplying materials to roofers. Call today.",
            "body": body, "og": "aluminum-shingle-home-deep-snow",
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]}],
            "full_biz": True}
