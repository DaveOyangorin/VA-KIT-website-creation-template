"""Pages for the utahbluechipcarpetcleaning.com redesign: "Spotless".

Blue Chip started out restoring antique Persian and oriental rugs, and still prices carpet cleaning per room, online. So the home page opens on
a full-bleed photo of a navy-and-madder Persian carpet (credited), with their organic, no-residue promise, and the signature is a floor plan:
tap the rooms you want cleaned, add a duct package or pet treatment, and the ticket shows their published online price. Their logo navy and
teal with the rug's madder red, Fraunces for an heirloom feel, Figtree for text.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 16 URLs (no trailing slash) and canonicals."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

ROOM_PRICES = [89.95, 99.95, 129.95, 159.95, 189.95, 219.95, 249.95, 279.95, 319.95, 349.95]
DUCTS = [("2,000 sq ft", "10 vents, 2 returns", 179.95), ("2,500 sq ft", "12 vents, 3 returns", 225), ("3,000 sq ft", "15 vents, 3 returns", 270), ("3,500 sq ft", "17 vents, 4 returns", 315),
         ("4,000 sq ft", "20 vents, 4 returns", 360), ("5,000 sq ft", "25 vents, 5 returns", 450), ("8,000 sq ft", "40 vents, 8 returns", 720)]
BOOK = [("1-room-and-hallway", "1 Room and Hallway", "$89.95"), ("2-rooms-and-hallway", "2 Rooms and Hallway", "$99.95"), ("3-rooms-and-hallway", "3 Rooms and Hallway", "$129.95"),
        ("4-rooms-and-hallway", "4 Rooms and Hallway", "$159.95"), ("5-rooms-and-hallway", "5 Rooms and Hallway", "$189.95"), ("6-rooms-and-hallway", "6 Rooms and Hallway", "$219.95"),
        ("7-rooms-and-hallway", "7 Rooms and Hallway", "$249.95"), ("8-rooms-and-hallway", "8 Rooms and Hallway", "$279.95"), ("9-rooms-and-hallway", "9 Rooms and Hallway", "$319.95"),
        ("10-rooms-and-hallway", "10 Rooms and Hallway", "$349.95"), ("24-hour-emergency-carpet-cleaning", "24 Hour Emergency Carpet Cleaning", "Starting at $350")]
REV = [("They arrived early and did fabulous work. Friendly and very efficient. Our carpet is 20 (yes, 20) years old and they really made it look great! Thank you!! I recommend this service.", "Robin W."),
       ("We had the best experience with Blue Chip. They cleaned our air ducts and serviced our dryer vents. They really know their stuff. We 5-star pleased with the service, recommend them and will use them again.", "Garen P."),
       ("I had a great experience with Blue Chip Carpet Cleaning. They did an excellent job and took their time and made sure we were satisfied with the results. Very professional and even got me in on a same day call.", "Lisa K.")]
STEPS = [("Pre-treat", "We pre-treat all the carpet to break up spots, stains and heavily soiled areas."), ("Organic enzyme", "A non-residue, organic enzyme with a little hot water cleans all the way down to the backing."),
         ("No soap, no soak", "No soaps, chemicals or harsh detergents, and no over-soaking."), ("Dry in 1&ndash;3 hours", "Safe for kids, pets and anyone with allergies or breathing problems.")]
FAQ = [("How long until my carpet is dry?", "<p>Usually within 1 to 3 hours. Upholstery dries within 90 minutes.</p>"),
       ("Do I need to move furniture or vacuum first?", "<p>No. There&rsquo;s no prep work, no need to move furniture and no need to pre-clean or vacuum.</p>"),
       ("Is it safe for kids and pets?", "<p>Yes. We don&rsquo;t use soaps, chemicals or harsh detergents. Our organic formula is safe for kids, pets and anyone with breathing problems.</p>"),
       ("When do I pay?", "<p>Payment is collected when the service is complete. We accept all major credit cards, checks, cash and cashier&rsquo;s checks.</p>"),
       ("Do you guarantee your work?", "<p>Yes. All technicians are background checked, and all workmanship is guaranteed for up to 15 days. We also offer a 100% satisfaction guarantee.</p>")]
ROOMS = [("Living", 20, 20, 210, 150), ("Dining", 230, 20, 140, 150), ("Family", 390, 20, 190, 150), ("Bed 1", 20, 230, 150, 130), ("Bed 2", 180, 230, 130, 130),
         ("Office", 320, 230, 120, 130), ("Bed 3", 450, 230, 130, 130), ("Bed 4", 20, 370, 170, 110), ("Bonus", 200, 370, 200, 110), ("Basement", 410, 370, 170, 110)]


def m(v):
    return f"${v:,.2f}"


def planner():
    rooms = "".join(f'''<g class="rm" tabindex="0" role="checkbox" aria-checked="{"true" if i < 3 else "false"}" aria-label="{n}" data-room="{i}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>
<text x="{x + w / 2}" y="{y + h / 2 + 5}" text-anchor="middle">{n}</text></g>''' for i, (n, x, y, w, h) in enumerate(ROOMS))
    plan = f'''<svg class="fp" viewBox="0 0 600 500" aria-label="Floor plan: choose rooms to clean"><rect class="fp-out" x="8" y="8" width="584" height="484" rx="8"/>
<g class="hall"><rect x="20" y="180" width="560" height="40" rx="4"/><text x="300" y="206" text-anchor="middle">HALLWAY &middot; INCLUDED</text></g>{rooms}</svg>'''
    duct = '<option value="0">No duct cleaning</option>' + "".join(f'<option value="{p}">{s} ({d}): {m(p)}</option>' for s, d, p in DUCTS)
    return f'''<div class="pl" data-plan data-prices="{",".join(str(p) for p in ROOM_PRICES)}">
<div class="pl-l">{plan}<p class="pl-hint">Tap rooms to add or remove them. Up to 10 rooms, plus the hallway.</p></div>
<div class="tk"><p class="tk-h">Your online price</p><p class="tk-rooms"><b data-n>3</b> rooms &amp; hallway</p><p class="tk-price" data-carpet>$129.95</p>
<label class="tk-row" for="pl-duct"><span>Air ducts</span><select id="pl-duct" data-duct>{duct}</select></label>
<label class="tk-chk"><input type="checkbox" data-pet value="100"><span>Pet treatment <b>$100</b></span></label>
<div class="tk-tot"><span>Estimated total</span><b data-total>$129.95</b></div>
<p class="tk-note">Pay when the job is done. Exact appointment time, and a call if we&rsquo;re running more than 15 minutes late.</p>
<a class="btn accent" href="@/booking-calendar/3-rooms-and-hallway/" data-book>Book this package {ARROW}</a></div></div>'''


def rv(t, n, cls=""):
    return f'<blockquote class="rv{cls}"><p>{html.escape(t)}</p><footer>{html.escape(n)}</footer></blockquote>'


def home():
    body = f'''
<section class="b-hero"><div class="bh-img" data-parallax="0.08">{img("bc-rug", "Detail of an antique Persian carpet with a cream medallion on a deep navy and madder red field", priority=True)}</div>
<div class="wrap bh-in"><div class="bh-txt"><p class="label">Organic carpet cleaning &middot; Salt Lake, Utah, Summit &amp; Tooele counties</p>
<h1>Carpet cleaning in Salt Lake City, <em>spotless and organic.</em></h1>
<p class="lede">Call today, we&rsquo;ll be there tomorrow. A family company that started out restoring antique Persian and oriental rugs, now cleaning carpets, rugs, upholstery and air ducts with no soaps, no harsh chemicals and no over-soaking.</p>
<div class="btn-row"><a class="btn accent" href="@/services/">See prices &amp; book online {ARROW}</a><a class="btn ghost" href="tel:+18017857385">{PHONE} 801-785-7385</a></div></div>
<ul class="bh-why"><li>Background-checked technicians</li><li>100% satisfaction guaranteed</li><li>Evenings &amp; weekends</li><li>Dry in 1&ndash;3 hours</li></ul></div>
<p class="credit">Persian carpet detail &middot; A.Davey, CC BY 2.0, via Wikimedia Commons</p></section>

<section class="sec b-plan" id="price"><div class="wrap">
<div class="b-head split-h reveal"><div><p class="label">Online prices</p><h2>Tap your rooms. <em>See your price.</em></h2></div><p class="lede">Our room prices are the same online as on the phone. Pick the rooms, add ducts or pet treatment, and book the package.</p></div>
{planner()}
</div></section>

<section class="sec b-steps"><div class="wrap b-steps-in">
<div class="reveal"><p class="label">Our four-step process</p><h2>Clean to the backing. <em>Nothing left behind.</em></h2>
<p class="lede">We use the hot-water method recommended by carpet manufacturers and taught by the IICRC, with a non-residue organic process that restores your carpet to its natural beauty.</p></div>
<ol class="steps">{"".join(f'<li class="reveal"><span>{i + 1}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))}</ol>
</div></section>

<section class="sec b-svc"><div class="wrap">
<div class="b-head reveal"><p class="label">What we clean</p><h2>Carpet, rugs, upholstery, <em>air ducts.</em></h2></div>
<div class="svc">
<a class="sv s-rug reveal" href="@/services/#rugs"><figure>{img("bc-rug-blue", "A blue-field Persian carpet with a red border")}</figure><div><b>Area &amp; oriental rugs</b><p>Where we started. Free estimates on oriental and area rugs, and no need to pre-vacuum or pre-clean.</p></div></a>
<a class="sv reveal" href="@/services/#carpet"><span class="sv-n">01</span><b>Residential carpet</b><p>Four-step organic cleaning, dry in 1&ndash;3 hours.</p></a>
<a class="sv reveal" href="@/services/#upholstery"><span class="sv-n">02</span><b>Upholstery</b><p>Vacuumed, pre-treated and hand cleaned. Dries within 90 minutes.</p></a>
<a class="sv reveal" href="@/services/#ducts"><span class="sv-n">03</span><b>Air ducts</b><p>Cleaning and sanitizing, priced per vent or by home size.</p></a>
<a class="sv reveal" href="@/services/#pet"><span class="sv-n">04</span><b>Pet odor</b><p>Deodorize, sterilize and disinfect to prevent mold, mildew and viruses like parvo.</p></a>
<a class="sv reveal" href="@/services/#commercial"><span class="sv-n">05</span><b>Commercial carpet &amp; tile</b><p>Pre-treated and cleaned to the backing. Free quotes.</p></a>
</div></div></section>

<section class="b-band"><div class="band-img" data-parallax="0.1">{img("bc-carpet", "Close-up of clean beige carpet pile")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our story</p><p>We started out as a small operation restoring antique Persian and oriental rugs. Our commitment to customer service grew us into the carpet cleaners we are today: reliable, honest and thorough.</p></blockquote></div>
<p class="credit">Carpet texture &middot; Kurt Kaiser, CC0, via Wikimedia Commons</p></section>

<section class="sec b-rev"><div class="wrap">
<div class="b-head reveal"><p class="label">What people say</p><h2>Twenty-year-old carpet, <em>looking great.</em></h2></div>
<div class="rv3">{"".join(rv(t, n, f" r{i}") for i, (t, n) in enumerate(REV))}</div></div></section>

<section class="sec b-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Easy, simple, <em>quick.</em></h2>
<a class="post-card b-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>EPA&rsquo;s 24&ndash;48 hour rule for drying carpet and pad after a leak, and when wet carpet can&rsquo;t be saved.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Carpet Cleaning Salt Lake City | Blue Chip Organic Cleaning",
            "meta": "Organic carpet, rug, upholstery and air duct cleaning in Salt Lake City and Utah County. No soaps or harsh chemicals, dry in 1-3 hours, rooms from $89.95.",
            "body": body, "body_class": "is-home", "og": "bc-rug", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def legal(k, start):
    t = EXT[k]["text"]; t = t[t.find(start) + len(start):].strip()
    sents = re.split(r"(?<=[.!?])\s+", t)
    return "".join(f"<p>{html.escape(' '.join(sents[j:j + 4]))}</p>" for j in range(0, len(sents), 4))


def make_pages():
    out = [home()]
    rows = "".join(f'<tr><th scope="row">{n}</th><td>{p}</td><td><a href="@/booking-calendar/{s}/">Book</a></td></tr>' for s, n, p in BOOK)
    drows = "".join(f'<tr><th scope="row">{s} <small>{d}</small></th><td>{m(p)}</td></tr>' for s, d, p in DUCTS)
    sv = f'''<p class="answer">Simple, easy and quick: no prep work, no moving furniture, no pre-cleaning or vacuuming. You get an exact appointment time, and we&rsquo;ll call if we&rsquo;re running more than 15 minutes late.</p>
{planner()}
<h2 id="carpet">Residential carpet cleaning</h2><p>Our four-step guaranteed cleaning process is quick and effective. We don&rsquo;t use soaps, chemicals or harsh detergents, and there&rsquo;s no over-soaking. Our organic formula is safe for kids, pets and anyone with breathing problems, and your carpet is dry within 1 to 3 hours.</p>
<div class="tbl"><table class="price"><caption>Carpet cleaning, online prices</caption><thead><tr><th>Package</th><th>Price</th><th></th></tr></thead><tbody>{rows}</tbody></table></div>
<h2 id="commercial">Commercial carpet &amp; tile cleaning</h2><p>We pre-treat all the carpet to remove spots, stains and heavily soiled areas, then use a non-residue organic enzyme with a little hot water that cleans all the way down to the backing. Commercial carpet and tile cleaning prices vary; call for a free quote.</p>
<h2 id="ducts">Air duct cleaning &amp; sanitizing</h2><p>Residential air duct cleaning is $15.00 per vent and $15.00 per cold air return, or choose a package by home size. We provide free estimates for commercial air duct cleaning.</p>
<div class="tbl"><table class="price"><caption>Air duct packages</caption><thead><tr><th>Home size</th><th>Price</th></tr></thead><tbody>{drows}</tbody></table></div>
<h2 id="upholstery">Upholstery cleaning</h2><p>We vacuum and pre-treat the entire piece, then hand clean every inch of the furniture. Our non-residue process dries within 90 minutes. Sofa, loveseat and chair prices vary.</p>
<h2 id="pet">Pet odor removal</h2><p>We deodorize, sterilize and disinfect to eliminate and prevent mold, mildew and viruses like parvo. Pet treatment: $100.</p>
<h2 id="rugs">Area &amp; oriental rug cleaning</h2><p>We started out restoring antique Persian and oriental rugs. We provide free estimates for oriental and area rugs, and there&rsquo;s no need to pre-vacuum or pre-clean.</p>
<h2>Payment</h2><p>Payment is collected when the service is complete. We accept all major credit cards, checks, cash and cashier&rsquo;s checks.</p>'''
    out.append(K.page("services/", "Services", "Services &amp; Online Prices", "Rooms from $89.95. Pay when it&rsquo;s done.", "Services", "Carpet Cleaning Prices &amp; Services | Blue Chip, Salt Lake",
                      "Blue Chip carpet cleaning prices: 1 room and hallway $89.95 to 10 rooms $349.95, air ducts $15 per vent, pet treatment $100, and rug and upholstery cleaning.",
                      sv, image="bc-rug-blue", alt="A blue-field Persian carpet", canonical=EXT["services"]["canon"], faqs=FAQ[:2],
                      schema=K.svc_schema("services/", "Carpet cleaning", "Salt Lake City, UT")))
    ab = '''<p class="answer">With many years in the carpet and upholstery cleaning industry, Blue Chip Carpet Cleaning has become a reliable standard for people in Utah looking for quality carpet cleaning at a cost-effective price.</p>
<p>We started out as a relatively small operation committed to the restoration of antique Persian and oriental rugs. Our commitment to customer service and our love of the industry allowed us to grow into the multifaceted carpet cleaners we are today.</p>
<h2>A family company</h2><p>As a family company, we understand that your home is one of the most important investments you&rsquo;ll ever make. Your home is your sanctuary, and no one likes living with musty, dirty upholstery or carpet that has lost its appeal. Keeping carpets and fabrics free of dirt and bacteria matters for your family, and for any business that cares about its employees and clients.</p>
<h2>Our promise</h2><ul class="ticks"><li>Free estimates for any job, large or small</li><li>We guarantee our work</li><li>Referrals from previous clients, on request</li><li>Same-day appointments and spot removal for important events</li></ul>
<p class="pull">Blue Chip Carpet Cleaning: reliable, honest and thorough.</p>'''
    out.append(K.page("about-us/", "About", "About Blue Chip Carpet Cleaning", "Reliable, honest and thorough.", "About", "About Blue Chip Carpet Cleaning | Family-Owned, Utah",
                      "Blue Chip Carpet Cleaning began restoring antique Persian and oriental rugs and grew into a family-owned carpet, rug, upholstery and duct cleaner in Utah.",
                      ab, image="bc-carpet", alt="Clean carpet pile", canonical=EXT["about_us"]["canon"]))
    out.append(K.page("privacy-policy/", "Privacy Policy", "Privacy Policy", "", "Legal", "Privacy Policy | Blue Chip Carpet Cleaning, Utah",
                      "Blue Chip Carpet Cleaning privacy policy: personal information is not shared or sold for marketing, and how SMS messages for appointments work.",
                      legal("privacy_policy", "Privacy Policy"), canonical=EXT["privacy_policy"]["canon"]))
    out.append(K.page("terms-of-service/", "Terms of Service", "Terms of Service", "", "Legal", "Terms of Service | Blue Chip Carpet Cleaning, Utah",
                      "Terms of Service for the Blue Chip Carpet Cleaning website: use of the site, bookings, content and the terms that apply when you use the site.",
                      legal("terms_of_service", "Terms of Service"), canonical=EXT["terms_of_service"]["canon"]))
    for s, n, p in BOOK:
        k = "booking_calendar_" + s.replace("-", "_")
        out.append(K.page(f"booking-calendar/{s}/", n, f"Book: {n}", p, "Book online", f"{n} | Book Online, Blue Chip"[:60],
                          f"Book {n.lower()} with Blue Chip Carpet Cleaning: {p}. Pick a date and time that works for you, or call 801-785-7385 to schedule."[:160],
                          f'<p class="answer">Schedule your service: check our availability and book the date and time that works for you.</p><p class="pull">{n}: {p}</p><p>Online booking happens on the live site. Prefer to talk? Call <a href="tel:+18017857385">801-785-7385</a>. Payment is collected when the service is complete.</p><p><a class="tlink" href="@/services/">All prices {ARROW}</a></p>',
                          crumbs=[("Services", "services/")], canonical=EXT[k]["canon"] if k in EXT else canon(f"booking-calendar/{s}/"), robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Prices", "services/"), ("About", "about-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-785-7385.", " Book online.")) for x in out]
