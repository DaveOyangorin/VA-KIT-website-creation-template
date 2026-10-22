"""Page content for customroofs.biz. Every fact comes from the client's current pages (fetched 17 Oct 2026).
Left out on purpose (see notes): "75 years", "15+ years", "20 years" (they contradict each other), "700+ projects",
"1000+ clients", "24/7 emergency repairs", "certified professionals", and the copper-siding energy-savings claim."""
from build import (U, BIZ_ID, S, ARROW, PHONE, MAIL, CONTACT, img, crumbs_ld, faq_ld, faq_html, cta, side, phero, quote_form, patina_bar)
import p_home, p_blog


def service_ld(url, name, desc, area="Utah"):
    return {"@type": "Service", "@id": url + "#service", "name": name, "url": url, "provider": {"@id": BIZ_ID},
            "description": desc, "areaServed": {"@type": "State" if area == "Utah" else "City", "name": area}}


def article(trail, url, links, prose):
    return f'<section class="sec"><div class="wrap layout"><article class="prose">{prose}</article>{side(links)}</div></section>'


def make_pages():
    pages = []
    home = {"path": "", "canonical": U, "modified": None}
    home.update(p_home.build())
    pages.append(home)

    # ---- copper roofing utah (main copper service page)
    url = U + "copper-roofing-utah/"
    trail = [("Home", ""), ("Copper Roofing in Utah", "copper-roofing-utah/")]
    faqs = [("Does a copper roof need maintenance?",
             "Less than most roofs, but some. Copper resists mildew, mold and insect damage. Inspections and debris removal still help it last, and we offer both."),
            ("Can you add copper to the roof I already have?",
             "Yes. Copper valleys, dormers and chimney caps can go on an existing roof, and copper gutters pair well with them."),
            ("Will my copper roof turn green?",
             "Over time copper weathers from bright metal through browns toward a blue-green patina. In a dry climate like Utah&rsquo;s, that last stage can take a very long time. Read <a href=\"@/blog/why-does-copper-turn-green/\">why copper turns green</a>.")]
    prose = f'''
<div class="answer">Custom Roofing installs, replaces and maintains copper roofs in Utah. Copper is our specialty: full copper roofs, complete overhauls, and copper accents for the roof you already have. Call <a href="tel:{S["tel"]}">{S["phone"]}</a> for a consultation.</div>
<p>Your roof does more than cover the house. It protects your family and adds value and character to the property. Copper does both jobs well, and it&rsquo;s the material we know best.</p>
<h2>Copper roof installation and replacement</h2>
<p>Copper is striking to look at and built to stand up to Utah&rsquo;s weather. Whether you&rsquo;re building a new home or replacing the roof you have, we bring the same care to both: precise panels, tight seams and clean details at every edge.</p>
<figure>{img("copper-roof-aerial", "Aerial view of a large home with a full copper roof")}<figcaption>A full copper roof from above.</figcaption></figure>
<h2>Why homeowners choose copper</h2>
<p>Three things bring people to copper, and they usually want all three:</p>
<ul>
<li><strong>The look.</strong> Copper gives any home a distinctive, premium finish that people notice from the street.</li>
<li><strong>Durability.</strong> Copper roofs are known for long life, resisting corrosion and handling Utah&rsquo;s varied climate.</li>
<li><strong>Less upkeep.</strong> Copper naturally resists mildew, mold and insect damage, so it needs fewer repairs than many materials.</li>
</ul>
<h2>Complete copper roof overhauls</h2>
<p>When a roof needs more than a patch, a full copper renovation is the long-term answer. We start with a detailed inspection of the existing roof to see the damage and decide on the best approach. Then our team rebuilds the roof in high-quality copper.</p>
<h2 id="accents">Copper accents for an existing roof</h2>
<p>Not ready for a full copper roof? Copper valleys, dormers and chimney caps add the same character to the roof you already have. Copper gutters finish the look and handle drainage.</p>
<div class="duo">{img("copper-curved-dormer", "Curved copper dormer with an arched window on a slate roof")}{img("copper-chimney-cap", "Copper chimney cap with standing seams")}</div>
<h2>Copper roofing designed around your home</h2>
<p>Every project is different. From small copper accents to a full replacement, we work with you to design a roof that suits your home&rsquo;s architecture and your own taste.</p>
<h2>Keeping a copper roof in shape</h2>
<p>Copper lasts a long time, and a little care helps it last longer. Our preventive maintenance includes inspections and debris removal, and our <a href="@/custom-roofing-maintenance-utah/">copper roof maintenance and repair</a> page covers the rest.</p>
<h2>Copper roofing questions</h2>
{faq_html(faqs)}
<p style="margin-top:26px">Ready to talk about a copper roof in Utah? Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or <a href="@/{CONTACT}">request a quote</a>.</p>'''
    pages.append({"path": "copper-roofing-utah/", "canonical": url, "es": True,
                  "title": "Copper Roofing Utah | Installation & Repair | Custom Roofing",
                  "meta": "Copper roofing in Utah from Custom Roofing: copper roof installation, full overhauls, copper accents and maintenance. Call 801-889-4220 for a consultation.",
                  "og": "copper-roof-aerial",
                  "body": phero(trail, "Copper Roofing in Utah", "Installation, replacement, overhauls and copper accents from a team that specializes in copper.",
                                "copper-roof-home", "Two-story home with a copper roof and curved copper dormers", "Copper roofing")
                          + article(trail, url, [("Copper roof maintenance", "custom-roofing-maintenance-utah/"), ("Copper siding", "lehi-custom-siding-home-value/"), ("Why copper turns green", "blog/why-does-copper-turn-green/"), ("Request a quote", CONTACT)], prose) + cta(),
                  "schema": [crumbs_ld(url, trail), service_ld(url, "Copper Roofing", "Copper roof installation, replacement, complete overhauls and copper accents in Utah."), faq_ld(faqs)]})

    # ---- maintenance & repair
    url = U + "custom-roofing-maintenance-utah/"
    trail = [("Home", ""), ("Roof Repair & Maintenance", "custom-roofing-maintenance-utah/")]
    prose = f'''
<div class="answer">Custom Roofing maintains and repairs copper roofs in Lehi and throughout Utah: regular inspections, debris removal, resealing, panel and seam repairs, and patina care. We recommend inspections once or twice a year.</div>
<p>Your home is one of your biggest investments. Copper roofing is known for its beauty and durability, but like any roof, it performs best with regular care.</p>
<h2>Why copper roofs still need maintenance</h2>
<p><strong>A longer life.</strong> Copper is one of the most durable roofing materials there is, and with proper care it can last for generations. Regular inspections catch minor issues before they become major ones.</p>
<p><strong>Less damage from debris.</strong> Leaves and branches collect on a roof. Copper resists corrosion, but debris holds moisture against the surface and can cause localized wear. Keeping the roof clear prevents it.</p>
<p><strong>An even patina.</strong> Copper weathers naturally, and that patina helps protect it. Good maintenance helps the patina form evenly, without streaks or stains from dirt and runoff.</p>
<p><strong>Problems found early.</strong> Severe weather or an unexpected event can still damage a strong roof. Inspections find loose panels, cracked seams and pooling water before they cause leaks or structural problems.</p>
<figure>{img("copper-roof-ladder-trees", "Copper standing-seam roof with a domed cupola, seen from above")}<figcaption>Seams, joints and flashing all get checked on an inspection.</figcaption></figure>
<h2>What our maintenance and repair covers</h2>
<h3>Regular inspections</h3>
<p>We recommend an inspection once or twice a year. We check every part of the roof: seams, joints, flashing, and how the patina is developing.</p>
<h3>Preventive maintenance</h3>
<p>Cleaning debris off the roof, making sure it drains properly, resealing vulnerable areas, and fixing minor issues like loose panels or weather-worn sections.</p>
<h3>Copper roof repair</h3>
<p>Storms, falling branches and accidents happen. We repair damaged panels, reseal seams and address water damage to the materials underneath, restoring the roof without spoiling its looks.</p>
<h3>Patina management</h3>
<p>If you want to control how your roof weathers, or restore areas that have weathered unevenly, we offer specialized cleaning and treatments that help the roof age evenly while keeping its protective layer. Curious how patina forms? Read <a href="@/blog/why-does-copper-turn-green/">why copper turns green</a>.</p>
<h2>More copper services</h2>
<p>Maintenance is one part of what we do. We also install:</p>
<ul>
<li><a href="@/copper-roofing-utah/">Copper roofs</a>, custom-fitted panel by panel</li>
<li>Copper accents such as valleys, dormers and chimney caps</li>
<li>Seamless copper gutters that drain well and match a copper roof</li>
</ul>
<div class="duo">{img("copper-chimney-cap", "Copper chimney cap with standing seams")}{img("copper-curved-dormer", "Curved copper dormer with an arched window")}</div>
<h2>Why owners trust us with copper</h2>
<p>Copper takes specialized knowledge to maintain and repair properly. Our team has years of experience working with it and understands how it behaves.</p>
<p>We build maintenance plans around your roof&rsquo;s needs, from routine inspections to preventive repairs, and we use high-quality materials on every repair so the roof keeps performing and looking right.</p>
<h2>Start with a free consultation</h2>
<p>We&rsquo;ll assess your roof&rsquo;s condition, give you clear recommendations, and put together a maintenance or repair plan. Call <a href="tel:{S["tel"]}">{S["phone"]}</a> to talk about copper roof maintenance and repair in Lehi and throughout Utah.</p>'''
    pages.append({"path": "custom-roofing-maintenance-utah/", "canonical": url, "es": True,
                  "title": "Custom Roofing Maintenance Utah | Copper Roof Repair",
                  "meta": "Copper roof maintenance and repair in Utah: inspections, debris removal, resealing, panel and seam repair, and patina care from Custom Roofing. Call today.",
                  "og": "copper-roof-ladder-trees",
                  "body": phero(trail, "Custom Roofing Maintenance in Utah", "Inspections, repairs and patina care that keep a copper roof protecting your home for decades.",
                                "copper-standing-seam-over-old-roof", "Copper standing-seam roof panels on a roof", "Repair &amp; maintenance")
                          + article(trail, url, [("Copper roofing in Utah", "copper-roofing-utah/"), ("Copper siding", "lehi-custom-siding-home-value/"), ("Why copper turns green", "blog/why-does-copper-turn-green/"), ("Request a quote", CONTACT)], prose)
                          + cta("Is your copper roof due for a check?"),
                  "schema": [crumbs_ld(url, trail), service_ld(url, "Copper Roof Maintenance and Repair", "Inspections, preventive maintenance, copper roof repair and patina management in Utah.")]})

    # ---- siding
    url = U + "lehi-custom-siding-home-value/"
    trail = [("Home", ""), ("Lehi Custom Siding", "lehi-custom-siding-home-value/")]
    prose = f'''
<div class="answer">Custom Roofing installs, repairs and replaces copper siding in Lehi. We help you choose a finish, from new copper&rsquo;s shine to a weathered look, and install each panel for durability and appearance.</div>
<p>Your home&rsquo;s exterior should protect it as well as it looks. Copper siding does both: an elegant finish that ages gracefully, and a tough skin against the weather.</p>
<h2>Why choose copper siding in Lehi</h2>
<p>Copper suits modern and traditional homes alike. It&rsquo;s the kind of exterior that turns a house into the one people slow down to look at.</p>
<ul>
<li><strong>Curb appeal.</strong> A copper exterior makes any home stand out.</li>
<li><strong>Property value.</strong> Copper&rsquo;s look and long life help a home stand out to buyers.</li>
<li><strong>Low upkeep.</strong> Occasional cleaning keeps it bright, and as it weathers it needs even less.</li>
<li><strong>Protection.</strong> Copper resists corrosion and moisture, and it doesn&rsquo;t burn.</li>
</ul>
<figure>{img("copper-arched-roof-building", "Arched building covered in copper shingles")}<figcaption>Copper shingles wrapping an arched building.</figcaption></figure>
<h2>Our copper siding services</h2>
<h3>Custom installation</h3>
<p>Our team installs every copper panel for durability and appearance, and helps you pick the finish that suits your home.</p>
<h3>Design options</h3>
<p>Choose from sleek modern panels to traditional designs. Prefer the shine of new copper, or the patinated look? We&rsquo;ll build either.</p>
<h3>Repair and replacement</h3>
<p>If your copper siding is damaged, we repair or replace it to restore both its looks and its protection.</p>
<h3>Expert consultation</h3>
<p>Not sure copper siding is right for you? We&rsquo;ll look at your home, talk through what you like, and help you choose copper siding that fits your budget.</p>
<div class="duo">{img("copper-siding-install", "Copper siding panels being installed around a window")}{img("cedar-shake-siding-gable", "Gable end finished with cedar shake siding")}</div>
<p style="font-size:.92rem;color:var(--muted)">Copper isn&rsquo;t the only option: the gable above was finished in shake-style siding, and our <a href="@/home/roofing-services-lehi-quality-guaranteed/">newest work</a> includes red and black metal siding on a barn.</p>
<h2>Why Lehi homeowners choose Custom Roofing</h2>
<p>Our team has years of experience installing, repairing and maintaining copper siding. Every project is personal, from choosing the design to the last panel, and we use high-quality copper that protects your home for decades.</p>
<h2>Schedule a free consultation</h2>
<p>Call <a href="tel:{S["tel"]}">{S["phone"]}</a> to talk about copper siding for your Lehi home. We&rsquo;ll guide you from choosing a style to the finished installation.</p>'''
    pages.append({"path": "lehi-custom-siding-home-value/", "canonical": url, "es": True,
                  "title": "Lehi Custom Siding | Copper Siding | Custom Roofing",
                  "meta": "Lehi custom siding in copper from Custom Roofing: installation, design options, repair and replacement. Boost curb appeal and protection. Call 801-889-4220.",
                  "og": "copper-siding-install",
                  "body": phero(trail, "Lehi Custom Siding in Copper", "Copper siding that adds character outside and protection that lasts.",
                                "copper-arched-roof-building", "Arched building covered in copper shingles", "Siding")
                          + article(trail, url, [("Copper roofing in Utah", "copper-roofing-utah/"), ("Repair &amp; maintenance", "custom-roofing-maintenance-utah/"), ("Our newest work", "home/roofing-services-lehi-quality-guaranteed/"), ("Request a quote", CONTACT)], prose)
                          + cta("Thinking about copper siding?"),
                  "schema": [crumbs_ld(url, trail), service_ld(url, "Copper Siding", "Copper siding installation, repair and replacement in Lehi, Utah.", "Lehi, UT")]})

    # ---- services overview (keeps the current URL and the client's 5-year workmanship warranty)
    url = U + "home/roofing-services-lehi-quality-guaranteed/"
    trail = [("Home", ""), ("Roofing Services in Lehi", "home/roofing-services-lehi-quality-guaranteed/")]
    work = [("red-black-metal-siding-barn", "Barn with red and black metal siding", "Red and black barn siding"),
            ("red-black-metal-siding-barn-sunset", "The same barn at sunset", "Same barn, at sunset"),
            ("roof-in-progress-mountain-view", "Roof in progress with the mountains behind it", "Roof in progress"),
            ("copper-flashing-on-truck", "Fabricated copper piece loaded on a truck for delivery", "Copper piece, ready to install"),
            ("copper-standing-seam-over-old-roof", "Copper standing-seam panels being installed", "Copper going on")]
    gallery = "".join(f'<figure class="snap reveal">{img(n, a)}<figcaption>{c}</figcaption></figure>' for n, a, c in work)
    body = f'''
<section class="sec"><div class="wrap split">
<div class="reveal prose"><p class="label">Roofing services in Lehi</p><h2>High-quality roofing, built to your needs</h2>
<p>Whether you&rsquo;re a homeowner after a fresh look or a business owner who needs a roof that lasts, we have the right option. Our specialty is copper roofing in Lehi: the lasting look and strength of copper, done with precision.</p>
<p>We also handle roof repairs and replacements, with the same attention to detail. High-quality materials and careful technique mean your roof looks right and stands up to the elements.</p></div>
<div class="frame reveal">{img("dark-roof-homes-aerial", "Aerial view of two homes with dark roofs")}<span class="cap">Residential &amp; commercial</span></div>
</div></section>
<section class="sec white"><div class="wrap">
<div class="head reveal"><p class="label">Commercial &amp; residential</p><h2>Our roofing services in Lehi</h2></div>
<div class="numlist">
<a class="reveal" href="@/copper-roofing-utah/"><span>01</span><b>Custom roofs</b><small>Copper roofs, overhauls and copper accents</small></a>
<div class="reveal"><span>02</span><b>Gutters</b><small>Including seamless copper gutters</small></div>
<a class="reveal" href="@/lehi-custom-siding-home-value/"><span>03</span><b>Siding</b><small>Copper siding plus other materials</small></a>
<a class="reveal" href="@/custom-roofing-maintenance-utah/"><span>04</span><b>Maintenance &amp; repair</b><small>Inspections, cleaning, panel and seam repair</small></a>
</div></div></section>
<section class="sec dark"><div class="wrap split">
<div class="reveal"><p class="label light">Our promise</p><h2>A 5-year workmanship warranty on all of our services</h2>
<p class="lede">We care about you and your project. Every service we provide comes with a 5-year workmanship warranty.</p>
<a class="tlink" href="@/{CONTACT}">Ask about your project {ARROW}</a></div>
<div class="reveal">{patina_bar("tall")}</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Newest work</p><h2>Check out our newest work</h2><p class="lede">Recent jobs from the Custom Roofing crew.</p></div>
<div class="snaps">{gallery}</div>
</div></section>'''
    pages.append({"path": "home/roofing-services-lehi-quality-guaranteed/", "canonical": url, "es": True,
                  "title": "Roofing Services Lehi | 5-Year Workmanship Warranty",
                  "meta": "Roofing services in Lehi from Custom Roofing: copper roofs, gutters, siding, and repair and maintenance, all with a 5-year workmanship warranty. Call today.",
                  "og": "red-black-metal-siding-barn",
                  "body": phero(trail, "Roofing Services in Lehi", "Copper roofing, gutters, siding, and maintenance and repair, for homes and businesses.",
                                "copper-dome-roof-installer", "Installer standing on top of a copper dome under construction", "Services")
                          + body + cta(),
                  "schema": [crumbs_ld(url, trail),
                             {"@type": "OfferCatalog", "@id": url + "#services", "name": "Roofing services in Lehi", "itemListElement": [
                                 {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in ("Custom copper roofs", "Gutters", "Siding", "Roof maintenance and repair")]}]})

    # ---- copper roofing lehi (the client's contact / request-a-quote page)
    url = U + "copper-roofing-lehi/"
    trail = [("Home", ""), ("Copper Roofing in Lehi", "copper-roofing-lehi/")]
    body = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">
<div class="answer">Need copper roofing in Lehi? Call <a href="tel:{S["tel"]}">{S["phone"]}</a>, email <a href="mailto:{S["email"]}">{S["email"]}</a>, or fill out the form. We&rsquo;ll create a project plan and get your approval before we start.</div>
<h2>Contact Custom Roofing about your copper roof</h2>
<p>Have a question, or ready to schedule a consultation? We&rsquo;re glad to help with any roofing need. Our specialty is <a href="@/home/roofing-services-lehi-quality-guaranteed/">copper roofing services in Lehi</a>.</p>
<p>Copper gives a home or business a striking, durable roof. If you&rsquo;re after a new look or need an upgrade, we&rsquo;ll show you what copper can do for your property.</p>
<h2>What happens after you reach out</h2>
<ol class="steps light">
<li><h3>Fill out the form</h3><p>About two minutes. Our team will be in contact with you shortly.</p></li>
<li><h3>We build your plan</h3><p>Once the project plan is ready, we get your approval and get started.</p></li>
<li><h3>We do the work</h3><p>Sit back and relax while we take care of your project.</p></li>
</ol>
<h2>How to reach us</h2>
<div class="pillars" style="grid-template-columns:1fr">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Phones</h3><p>Primary: <a href="tel:{S["tel"]}">{S["phone"]}</a><br>Secondary: <a href="tel:{S["tel2"]}">{S["phone2"]}</a></p></div></div>
<div class="pillar"><span class="ic">{MAIL}</span><div><h3>Email</h3><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div></div>
<div class="pillar"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg></span><div><h3>Service area</h3><p>Located in Lehi, UT, serving all of Utah.</p></div></div>
</div>
</div><div class="sticky-form">{quote_form("Request a quote")}</div></div></section>'''
    pages.append({"path": "copper-roofing-lehi/", "canonical": url, "es": True,
                  "title": "Copper Roofing in Lehi | Request a Quote | Custom Roofing",
                  "meta": "Need copper roofing in Lehi? Contact Custom Roofing to start your project. We'll create a project plan and get your approval first. Call 801-889-4220.",
                  "og": "copper-curved-dormer",
                  "body": phero(trail, "Copper Roofing in Lehi: Request a Quote", "Tell us about your project. We&rsquo;ll plan it with you, then build it.",
                                "copper-curved-dormer", "Curved copper dormer with an arched window", "Contact") + body,
                  "schema": [crumbs_ld(url, trail), {"@type": "ContactPage", "@id": url + "#page", "url": url, "name": "Contact Custom Roofing", "about": {"@id": BIZ_ID}},
                             service_ld(url, "Copper Roofing in Lehi", "Copper roofing consultations, project plans and installation in Lehi, Utah.", "Lehi, UT")]})

    pages += p_blog.pages()
    pages.append({"path": "404.html", "title": "Page Not Found | Custom Roofing", "meta": "That page doesn't exist.", "canonical": None,
                  "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn&rsquo;t here", "Try the home page or give us a call.",
                                "copper-roof-aerial", "Copper roof", "Error 404")})
    # links on the current site that redirect: point straight at the final page
    redirects = {"lehi-custom-roofing/roofing-services-lehi-quality-guaranteed/": "home/roofing-services-lehi-quality-guaranteed/",
                 "home/contact": CONTACT, "home/contact/": CONTACT}
    return pages, redirects
