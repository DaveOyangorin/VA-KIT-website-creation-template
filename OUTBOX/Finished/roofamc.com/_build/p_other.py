from build import (SITE, ARROW, PHONE, img, cta_band, side, page_hero, faq_html, faq_schema,
                   crumbs_schema, service_schema, BIZ_ID)

BLOG = "blog/how-long-do-roofs-last-in-utah/"
U = SITE["url"] + "/"


def layout(article, links):
    return f'<section class="sec"><div class="wrap layout"><article class="prose">{article}</article>{side(links)}</div></section>'


def fig(name, alt, cap):
    return f'<figure class="reveal">{img(name, alt)}<figcaption>{cap}</figcaption></figure>'


# ----------------------------------------------------------------- Park City
PC_FAQ = [
    ("Do you work on homes and commercial buildings in Park City?",
     "Yes. We do residential and commercial roofing and waterproofing in Park City, and Park City residential roofing is a large share of our work. That includes repairs, replacements and maintenance programs that help a roof last longer."),
    ("How is a Park City roof different from one in the valley?",
     "Park City sits much higher than the Salt Lake Valley, so roofs there usually carry more snow for longer and see colder nights. That puts more weight on the structure and more stress on flashing, eaves and drainage. Ventilation and ice-dam protection matter even more."),
    ("Can you keep my business open during roof work in Park City?",
     "We plan commercial roofing work in Park City to have as little impact on your daily operations as possible. Tell us about deliveries, guest access and peak hours, and we'll schedule around them."),
    ("Do you offer roof maintenance in Park City?",
     "Yes. We can set up a maintenance program for your Park City roof so seams, flashing and drains get checked on a schedule and small problems are fixed before they become leaks."),
]

PC_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control provides commercial and residential roofing and waterproofing in Park City, Utah. We repair and replace all types of roofing systems and offer a maintenance program that extends roof life. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> for a free quote.</div>

<p>As a Park City commercial and residential roofing and waterproofing contractor, we're committed to high-quality work and complete customer satisfaction. We believe that focus, and our experienced Park City residential roofers, is what sets us apart and lets us build long relationships with our customers.</p>
<p>We look at each client's needs and look for cost-effective, energy-efficient options that fit them.</p>

<h2>Park City roofing for mountain conditions</h2>
<p>Roofs up the canyon work harder than roofs in the valley. More snow sits on them for longer, nights are colder, and the sun is strong at altitude. That combination is hard on eaves, valleys and flashing, and it makes attic ventilation and ice-dam protection a must.</p>
<p>Our Park City commercial roofers can repair and replace any type of roofing system and set you up with a maintenance program that extends the life of your roof and protects your investment.</p>

<h2>Commercial roofing in Park City without the disruption</h2>
<p>When it comes to Park City commercial roofing, we understand what it takes to deliver quality work with minimal or no impact on your daily operations. For hotels, shops and offices, that means planning around guests, deliveries and busy seasons.</p>

<h2>Park City roofing gallery</h2>
<p>This gallery shows the kind of residential and commercial work we do. Many of these are from our own jobs; see the notes under each photo.</p>
<div class="gallery">
{fig("park-city-shingle-roof-timber-home", "Shingle roof on a timber-sided home in Park City", "Sloped shingle roof on a timber home in Park City")}
{fig("shingle-roof-repair-suburban-home", "Asphalt shingle roof repairs on a two-story home", "Shingle roof repair on a family home")}
{fig("crew-crane-loading-roofing-materials", "Two roofers guiding a crane-lifted pallet of roofing materials", "Our crew loading materials by crane")}
{fig("white-flat-roof-wasatch-mountains", "White flat commercial roof with mountains in the distance", "Flat commercial roof with the Wasatch behind")}
{fig("standing-seam-metal-cupola", "Standing-seam metal roof with a cupola", "Metal roofing sheds heavy snow well (stock photo)")}
{fig("roofer-hard-hat-on-site", "Roofer in a yellow hard hat on a job site", "On site, hard hats on")}
</div>
<p>More work from the valley is in our <a href="@/salt-lake-city-commercial-roofing-and-residential-roofing/">Salt Lake City project gallery</a>. For details on materials, see <a href="@/residential/">residential roofing</a>; for flat roofs, see <a href="@/commercial/">commercial roofing</a> and <a href="@/waterproofing/">waterproofing</a>.</p>

<h2>Park City roofing questions</h2>
{faq_html(PC_FAQ)}
'''

PARKCITY = {
    "path": "park-city-commercial-roofing-and-waterproofing-solutions/",
    "title": "Park City Roofing & Waterproofing | Advanced Roofing",
    "meta": "Park City roofing and waterproofing for homes and commercial buildings. Repairs, replacements and maintenance plans built for mountain snow. Call for a quote.",
    "body": page_hero([("Home", ""), ("Park City Roofing", "park-city-commercial-roofing-and-waterproofing-solutions/")],
                      "Park City Commercial Roofing &amp; Waterproofing",
                      "Residential and commercial roofing and waterproofing for homes, lodges and businesses up the canyon.",
                      "park-city-shingle-roof-timber-home", "Shingle roof on a timber-sided home in Park City", "Park City, Utah")
            + layout(PC_ART, [("Residential roofing", "residential/"), ("Commercial roofing", "commercial/"),
                              ("Waterproofing", "waterproofing/"), ("Utah service area", "utah-commercial-and-residential-roofers/"),
                              ("Get a free quote", "get-a-quote/")])
            + cta_band("Roof work in Park City?", "Call for a free quote on repairs, replacement, waterproofing or a maintenance plan."),
    "og": "park-city-shingle-roof-timber-home",
}
PARKCITY["schema"] = service_schema(PARKCITY, "Roofing and Waterproofing in Park City",
                                    "Commercial and residential roofing, repair, replacement, maintenance and waterproofing in Park City, Utah.",
                                    area=[{"@type": "City", "name": "Park City, UT"}]) + [
    faq_schema(PC_FAQ), crumbs_schema([("Home", ""), ("Park City Roofing", PARKCITY["path"])])]

# ----------------------------------------------------------------- SLC gallery (kept as a project gallery so it doesn't fight the home or commercial page)
SLC_ART = f'''
<p class="lede" style="color:var(--ink-2)">A look at roofing, repair and waterproofing work around Salt Lake City, for homes and commercial buildings.</p>
<p>Our Salt Lake City roofers give clients a maintenance and repair program that helps protect their investment. On commercial jobs, we know how important it is to keep your business running and not be bothered by roof repair or replacement. We plan so the impact on your business is as small as possible.</p>
<p>For homeowners, our residential roofers provide cost-effective waterproofing for any type of roofing system. Waterproofing helps prevent future leaks and protects your roof from further weathering.</p>

<h2>Project photos</h2>
<div class="gallery">
{fig("white-flat-roof-wasatch-mountains", "White flat commercial roof with the Wasatch Mountains in the distance", "Flat commercial roof, Salt Lake Valley")}
{fig("crew-crane-staging-from-above", "Crane staging roofing materials on a commercial job, seen from above", "Staging materials on a commercial job")}
{fig("client-cafe-zupas-building", "Commercial building with Cafe Zupas and NY Pizza storefronts", "Cafe Zupas and NY Pizza building, a commercial client")}
{fig("crew-crane-loading-roofing-materials", "Two roofers guiding a crane-lifted pallet of roofing materials", "Loading the roof by crane")}
{fig("shingle-roof-repair-suburban-home", "Asphalt shingle roof repairs on a two-story home", "Shingle repair on a family home")}
{fig("roofer-hard-hat-on-site", "Roofer in a yellow hard hat on a job site", "Watching a lift on site")}
{fig("park-city-shingle-roof-timber-home", "Shingle roof on a timber-sided home in Park City", "Residential shingle roof, Park City")}
{fig("slc-skyline-summer-mountains", "Salt Lake City skyline with green foothills and mountains behind", "Salt Lake City from Virginia Street (stock photo)")}
</div>

<h2>What we work on in Salt Lake City</h2>
<ul class="checks">
<li><a href="@/commercial/">Commercial roofing</a>: flat and pitched roofs, re-roofing and maintenance</li>
<li><a href="@/residential/">Residential roofing</a>: new roofs, re-roofing and materials</li>
<li><a href="@/roof-repair/">Roof repair</a>: leaks, shingles, storm damage and gutters</li>
<li><a href="@/waterproofing/">Waterproofing</a>: flat roofs, balconies and transitions</li>
</ul>
<p>Want project photos of a specific roof type? Ask when you call, and see who we've worked for on the <a href="@/clients/">client list</a>.</p>
'''

SLC = {
    "path": "salt-lake-city-commercial-roofing-and-residential-roofing/",
    "title": "Salt Lake City Roofing Projects & Gallery | Advanced Roofing",
    "meta": "Photos of commercial and residential roofing, repair and waterproofing work around Salt Lake City by Advanced Roofing & Moisture Control. See our projects.",
    "body": page_hero([("Home", ""), ("Salt Lake City Projects", "salt-lake-city-commercial-roofing-and-residential-roofing/")],
                      "Salt Lake City Roofing Projects",
                      "Commercial and residential roofing, repair and waterproofing work from around the valley.",
                      "slc-skyline-summer-mountains", "Salt Lake City skyline with mountains behind", "Project gallery")
            + layout(SLC_ART, [("Commercial roofing", "commercial/"), ("Residential roofing", "residential/"),
                               ("Roof repair", "roof-repair/"), ("Park City projects", PARKCITY["path"]), ("Our clients", "clients/")])
            + cta_band(),
    "og": "white-flat-roof-wasatch-mountains",
    "active": "salt-lake-city-commercial-roofing-and-residential-roofing/",
}
SLC["schema"] = [{"@type": "CollectionPage", "@id": U + SLC["path"] + "#page", "url": U + SLC["path"], "name": "Salt Lake City Roofing Projects",
                  "about": {"@id": BIZ_ID}, "isPartOf": {"@id": U + "#website"}},
                 crumbs_schema([("Home", ""), ("Salt Lake City Projects", SLC["path"])])]

# ----------------------------------------------------------------- Utah service area
AREAS = [
    ("Salt Lake County", "Salt Lake City, South Salt Lake, West Jordan, Sandy, Murray, Midvale, Draper, South Jordan, North Salt Lake, Camp Williams, Alta"),
    ("Summit County", "Park City"),
    ("Davis County", "Centerville, Bountiful, Farmington, Layton"),
    ("Weber County", "Ogden, Wolf Creek"),
    ("Utah County", "Provo, Orem, Mapleton"),
    ("Central Utah", "Emery County"),
    ("Out of state", "Cody, Wyoming; West Yellowstone, Montana"),
]
area_rows = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in AREAS)

UT_FAQ = [
    ("Where in Utah do you work?",
     "Most of our work is Salt Lake City commercial roofing and Park City residential roofing. We also work across Salt Lake County and have done jobs in Davis, Weber and Utah counties and in Emery County. Call to check your location."),
    ("Do you take jobs outside Utah?",
     "Our client list includes a Family Dollar in Cody, Wyoming and the Maddison Hotel in West Yellowstone, Montana. Out-of-state work depends on the project, so call us to talk it through."),
    ("Do your Utah roofers do waterproofing too?",
     "Yes. Our roofers specialize in waterproofing roofing systems, which can extend roof life, save on roof costs, improve energy efficiency and help prevent new leaks, for homeowners and businesses alike."),
]

UT_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control is a team of commercial and residential roofers working across Utah. Most of our work is Salt Lake City commercial roofing and Park City residential roofing, with jobs from Ogden to Emery County. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> to check your area.</div>

<p>Our Utah roofers have the expertise to manage all types of roofing systems around the state. We also specialize in waterproofing, which has real benefits for any homeowner or company: a longer roof life, lower roof costs, better energy efficiency and fewer new leaks.</p>
<p>Our crew covers every part of roof maintenance, from <a href="@/roof-repair/">roof repair</a> to full roof restoration on all roof types, along with Salt Lake City residential repairs and replacements and every part of a Park City commercial roofing system, including maintenance and insulation.</p>

<h2>Where we've worked</h2>
<p>These places come straight from our client list. If you're nearby, we can probably help.</p>
<ul class="client-grid">{area_rows}</ul>

<figure>{img("herriman-winter-aerial", "Aerial view of a Herriman, Utah neighborhood with snowy mountains behind")}<figcaption>Herriman in winter, at the south end of Salt Lake County (stock photo).</figcaption></figure>

<h2>Commercial and residential roofers for Utah weather</h2>
<p>From the valley floor to the mountain towns, Utah roofs deal with heavy snow, freeze-thaw cycles and strong sun. We build and repair roofs with that in mind, and our guide to <a href="@/{BLOG}">how long roofs last in Utah</a> explains why it matters.</p>
<p>See our <a href="@/commercial/">commercial roofing</a> and <a href="@/residential/">residential roofing</a> pages, or the <a href="@/park-city-commercial-roofing-and-waterproofing-solutions/">Park City</a> page if you're up the canyon.</p>

<h2>Service area questions</h2>
{faq_html(UT_FAQ)}
'''

UTAH = {
    "path": "utah-commercial-and-residential-roofers/",
    "title": "Utah Commercial & Residential Roofers | Advanced Roofing",
    "meta": "Commercial and residential roofers serving Utah from Salt Lake City: Salt Lake County, Park City, Davis, Weber and Utah counties. See our service area today.",
    "body": page_hero([("Home", ""), ("Utah Service Area", "utah-commercial-and-residential-roofers/")],
                      "Utah Commercial &amp; Residential Roofers",
                      "Based in Salt Lake City, working across the Wasatch Front, up in Park City and beyond.",
                      "herriman-winter-aerial", "Aerial view of a snowy Utah neighborhood below the mountains", "Service area")
            + layout(UT_ART, [("Park City roofing", PARKCITY["path"]), ("Commercial roofing", "commercial/"),
                              ("Residential roofing", "residential/"), ("Our clients", "clients/"), ("Get a free quote", "get-a-quote/")])
            + cta_band(),
    "og": "herriman-winter-aerial",
}
UTAH["schema"] = service_schema(UTAH, "Commercial and Residential Roofing in Utah",
                                "Commercial and residential roofing, repair and waterproofing across Utah, based in Salt Lake City.",
                                area=[{"@type": "State", "name": "Utah"}]) + [
    faq_schema(UT_FAQ), crumbs_schema([("Home", ""), ("Utah Service Area", UTAH["path"])])]

# ----------------------------------------------------------------- clients
ROOF_CLIENTS = [("ModSpace Properties", "Camp Williams"), ("Flower Patch", "Ogden, Salt Lake"), ("Big “O” Tires", "Centerville"),
    ("A-1 Self Storage", "Centerville"), ("Cedar Park Office Buildings", "Murray"), ("Challenger Schools", "South Jordan"),
    ("Emery Schools", "Emery County"), ("City Centre", "Salt Lake City"), ("Miracle Bowl", "Provo"), ("White Coin Laundry", "Bountiful"),
    ("Schmidt Signs", "Salt Lake"), ("Investment Auto", "Centerville"), ("Valdez Machining", "North Salt Lake"),
    ("Taco Time", "Salt Lake; Bountiful; Farmington"), ("Reynold’s Construction", "Midvale"), ("Staker Parson Offices", "Draper"),
    ("Benchmark Offices", "Salt Lake"), ("Eagle Plaza Offices", "Salt Lake"), ("Chase Building", "Salt Lake"), ("Union Center", "Salt Lake"),
    ("After Hours Medical", "So. Jordan"), ("Wonder Bread", "Layton"), ("Oak Street Plaza", "Salt Lake"), ("Long Life Veggie House", "Salt Lake"),
    ("Germania Lift Center", "Alta"), ("Family Dollar", "Cody, WY"), ("Maddison Hotel", "West Yellowstone, MT"),
    ("Labrum Service Center", "S. Jordan"), ("Granpas Attic", "Salt Lake"), ("Alamo Storage", "Ogden"), ("Storage Plus", "Salt Lake"),
    ("Pentad Properties", "Salt Lake")]
POND_CLIENTS = [("Dave Checket Pond", "Wolf Creek · 60,000 sq ft"), ("Fear Factory", "Salt Lake · 1,000 sq ft"),
    ("Wally Joiner Ponds", "Mapleton · 20,000 sq ft"), ("Assey Pond", "Orem · 100,000 sq ft"),
    ("Lagoon Pond", "Farmington · 2,000 sq ft"), ("Huntsman fishing pond", "Emery County · 4,000 sq ft")]
half = (len(ROOF_CLIENTS) + 1) // 2
def rows(lst): return "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in lst)

CLIENTS_BODY = page_hero([("Home", ""), ("Clients", "clients/")], "Our Clients",
                         "Schools, offices, shops, storage, restaurants and ponds across Utah and beyond. A few of the people who trust us with their roofs.",
                         "client-cafe-zupas-building", "Commercial building with Cafe Zupas and NY Pizza storefronts", "Some of our valued clients") + f'''
<section class="sec"><div class="wrap">
  <div class="sec-head reveal"><p class="eyebrow">Roofs</p><h2>Commercial roofing clients</h2>
    <p class="lede">From a laundromat in Bountiful to a ski lift center in Alta. And many more.</p></div>
  <div class="client-cols reveal"><ul class="client-grid">{rows(ROOF_CLIENTS[:half])}</ul><ul class="client-grid">{rows(ROOF_CLIENTS[half:])}</ul></div>
</div></section>
<section class="sec dark"><div class="wrap split">
  <div class="reveal"><p class="eyebrow light">Ponds</p><h2>Pond liner clients</h2>
    <p class="lede">The same membrane know-how, pointed at keeping water in.</p>
    <ul class="client-grid" style="border-color:var(--line-dark)">{"".join(f'<li style="border-color:var(--line-dark)"><b>{a}</b><span style="color:rgba(255,255,255,.7)">{b}</span></li>' for a, b in POND_CLIENTS)}</ul>
    <a class="textlink" href="@/ponds/" style="margin-top:18px">Pond liners &amp; water features {ARROW}</a></div>
  <div class="frame reveal d1">{img("pond-waterfall-garden", "Garden pond with a small waterfall surrounded by shrubs")}</div>
</div></section>
<section class="sec paper"><div class="wrap split rev">
  <div class="reveal"><p class="eyebrow">Our most recent work</p><h2>See the projects</h2>
    <p>Photos from commercial and residential jobs around the valley and up in Park City.</p>
    <div class="btn-row"><a class="btn dark" href="@/salt-lake-city-commercial-roofing-and-residential-roofing/">Salt Lake City gallery {ARROW}</a><a class="btn dark" href="@/park-city-commercial-roofing-and-waterproofing-solutions/">Park City gallery {ARROW}</a></div>
    <p style="margin-top:22px">Or read what clients say on our <a href="@/testimonials/">testimonials</a> page.</p></div>
  <div class="frame reveal d1">{img("client-cafe-zupas-building", "Commercial building with Cafe Zupas and NY Pizza storefronts, a client of Advanced Roofing")}</div>
</div></section>
''' + cta_band()

CLIENTS = {
    "path": "clients/",
    "title": "Our Roofing Clients in Utah | Advanced Roofing & Moisture",
    "meta": "Commercial roofing and pond liner clients of Advanced Roofing & Moisture Control: schools, offices, retail and storage from Ogden to Emery County. See the list.",
    "body": CLIENTS_BODY, "og": "client-cafe-zupas-building",
    "schema": [{"@type": "CollectionPage", "@id": U + "clients/#page", "url": U + "clients/", "name": "Our Clients", "about": {"@id": BIZ_ID}},
               crumbs_schema([("Home", ""), ("Clients", "clients/")])],
}

# ----------------------------------------------------------------- testimonials
T_BODY = page_hero([("Home", ""), ("Testimonials", "testimonials/")], "Testimonials &amp; Praise",
                   "Words from homeowners and a commercial property manager who've worked with us.",
                   "shingle-roof-repair-suburban-home", "Asphalt shingle roof on a two-story home", "Your input is important to us") + f'''
<section class="sec"><div class="wrap">
  <div class="quotes">
    <figure class="quote feature reveal"><blockquote>
      <p>Advanced Moisture Control replaced our roof on our house last October and we were very impressed with their outstanding work from start to finish, as well as with follow-up afterwards.</p>
      <p>The bid was very detailed and included pictures of specific areas that needed repair. We had some other bids as well. The price on Advanced Moisture Control's bid was competitive, detailed and complete compared to the other bids. We understood the work that needed to be done and that the price was fair. There were details and suggestions about adding some vents and why they were necessary, as well as a lot of other details about our roof.</p>
      <p>The crew doing the work was polite, competent, and they left the yard clean. One of the owners of the business came by several times during the installation to check on progress and confer with the crew.</p>
      <p>We were happy with the finished roof. Also, this was the first winter we did not need to use a space heater in one particular room of the house. We've used a space heater in that room for 20 years. Last winter was colder so we think it was due to the roof being vented properly now; it certainly wasn't due to a mild winter!</p>
      <p>We had some leakage around a balcony into the garage this spring. Advanced Moisture Control came by and repaired it at no expense and in a professional, no-hassle manner for us.</p>
      <p>We highly recommend Advanced Moisture Control to anyone who needs a roof or a moisture control system.</p>
    </blockquote><figcaption>Tammy Radice<span>Residential roof replacement</span></figcaption></figure>
    <figure class="quote reveal d1"><blockquote><p>I just wanted to take a few minutes and write you to let you know I greatly appreciate the great work you, Mickey and your fellow employees did with the entire reroofing of my home from start to finish and then some additional help you generously provided subsequently. I couldn't be happier with the quality and timeliness with the workmanship. Everything was as promised and then some. I wish you continued success. Many thanks.</p></blockquote>
      <figcaption>Doug Foster, ChFC, CLU<span>Residential re-roof</span></figcaption></figure>
    <figure class="quote reveal d2"><blockquote>
      <p>I have been involved in the management of Commercial Properties for over 30 years. During this time I have used and worked with numerous Roofing Companies. However since becoming acquainted with Kelly Beck and using his company Advanced Moisture Control, Inc, for major roofing projects as well as numerous roof repairs the level of service is beyond compare with all the other companies I have used in my management career.</p>
      <p>Kelly Beck is a professional who knows roofing and his vast experience has provided quality roofing repairs and replacements at reasonable cost. When asked for bids, he provides them in a timely manner with attention to detail as to the materials that will be used and how the materials will be applied.</p>
      <p>Because of my experience with Kelly, I have found him to be extremely honest and especially responsive when repairs are needed to stop damage to Tenant spaces and buildings. I highly recommend Kelly and his company because he will provide quality products at a very competitive price. If there happens to be a problem after he has completed a job, he will get right on it to correct the situation.</p>
      <p>In today's world it is hard to find vendors who are honest, do quality work, and that you can depend on. Kelly, and his company can fill all these requirements and therefore I would recommend them and ask that you call me with any questions you may have concerning Kelly, his company, or bids.</p>
    </blockquote><figcaption>Vincent E. Webb, ChFC, CLU<span>Commercial property management</span></figcaption></figure>
  </div>
</div></section>
<section class="sec paper"><div class="wrap split">
  <div class="reveal"><p class="eyebrow">Penny for your thoughts?</p><h2>Leave us a testimonial</h2>
    <p>Worked with us? We'd love to hear how it went, good or bad. Your feedback helps us get better and helps your neighbors choose a roofer.</p>
    <p>You can also find us on <a href="{SITE["yelp"]}" rel="noopener">Yelp</a> and <a href="{SITE["facebook"]}" rel="noopener">Facebook</a>.</p></div>
  <form class="form reveal d1" method="post" action="">
    <div class="row"><label>First name *<input name="first" autocomplete="given-name" required></label><label>Last name *<input name="last" autocomplete="family-name" required></label></div>
    <label>Email *<input type="email" name="email" autocomplete="email" required></label>
    <label>Your comments *<textarea name="comments" required></textarea></label>
    <button class="btn" type="submit">Send testimonial {ARROW}</button>
  </form>
</div></section>
''' + cta_band()

TESTIMONIALS = {
    "path": "testimonials/",
    "title": "Roofing Testimonials & Reviews | Advanced Roofing & Moisture",
    "meta": "Read what homeowners and a commercial property manager say about Advanced Roofing & Moisture Control's roofing, repairs and follow-up in Salt Lake City.",
    "body": T_BODY, "og": "shingle-roof-repair-suburban-home",
    "schema": [crumbs_schema([("Home", ""), ("Testimonials", "testimonials/")])],
}

# ----------------------------------------------------------------- contact
C_BODY = page_hero([("Home", ""), ("Contact", "contact/")], "Contact Us",
                   "Call, email or send the form. We'll get back to you at the time that suits you.",
                   "slc-skyline-summer-mountains", "Salt Lake City skyline with mountains behind", "Let's get in touch") + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
  <div class="reveal">
    <div class="contact-cards">
      <div class="ccard"><h3>Phone</h3><a href="tel:{SITE["tel"]}">{SITE["phone"]}</a></div>
      <div class="ccard" style="background:var(--ember);color:var(--pine)"><h3 style="color:var(--pine)">Emergencies</h3><a href="tel:{SITE["emerg_tel"]}" style="color:var(--pine)">{SITE["emerg"]}</a></div>
      <div class="ccard"><h3>Email</h3><a href="mailto:{SITE["email"]}" style="font-size:1.25rem">{SITE["email"]}</a></div>
      <div class="ccard"><h3>Hours</h3><p>Mon–Sat</p><p class="small">9:00 am – 5:00 pm</p></div>
    </div>
    <div class="card-list" style="margin-top:16px"><h3>Find us</h3>
      <address style="font-style:normal;font-size:1.1rem;line-height:1.6"><strong>{SITE["name"]}</strong><br>{SITE["street"]}<br>{SITE["city"]}, {SITE["state"]} {SITE["zip"]}</address>
      <p style="margin:14px 0 0"><a class="textlink" href="{SITE["maps"]}" rel="noopener">Get directions {ARROW}</a></p></div>
  </div>
  <div class="reveal d1"><p class="eyebrow">Send a message</p><h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">Tell us about your project</h2>
  <form class="form" method="post" action="">
    <div class="row"><label>First name *<input name="first" autocomplete="given-name" required></label><label>Last name *<input name="last" autocomplete="family-name" required></label></div>
    <div class="row"><label>Phone *<input type="tel" name="phone" autocomplete="tel" required></label><label>Email *<input type="email" name="email" autocomplete="email" required></label></div>
    <div class="row"><label>Best time to contact you *<select name="time" required><option value="">--</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></label>
    <label>How did you hear about us? *<select name="source" required><option value="">--</option><option>Google</option><option>Family</option><option>Friend</option><option>Social Media</option><option>Other</option></select></label></div>
    <label>Tell us about your project *<textarea name="project" required></textarea></label>
    <button class="btn" type="submit">Send message {ARROW}</button>
    <p class="note">* Required. We only use your details to reply to you.</p>
  </form></div>
</div></section>
<section class="sec tight sage"><div class="wrap">
  <div class="sec-head reveal" style="margin-bottom:24px"><p class="eyebrow">Before you call</p><h2>Helpful pages</h2></div>
  <p class="reveal"><a href="@/roof-repair/">Roof repair</a> &middot; <a href="@/residential/">Residential roofing</a> &middot; <a href="@/commercial/">Commercial roofing</a> &middot; <a href="@/waterproofing/">Waterproofing</a> &middot; <a href="@/{BLOG}">How long roofs last in Utah</a></p>
</div></section>
'''

CONTACT = {
    "path": "contact/",
    "title": "Contact Advanced Roofing & Moisture Control | Salt Lake City",
    "meta": "Contact Advanced Roofing & Moisture Control in Salt Lake City. Call (801) 326-9708, emergencies (801) 671-2282, or send a message about your roofing project.",
    "body": C_BODY, "og": "slc-skyline-summer-mountains",
    "schema": [{"@type": "ContactPage", "@id": U + "contact/#page", "url": U + "contact/", "name": "Contact Us", "about": {"@id": BIZ_ID}},
               crumbs_schema([("Home", ""), ("Contact", "contact/")])],
}

# ----------------------------------------------------------------- get a quote
Q_BODY = page_hero([("Home", ""), ("Get a Quote", "get-a-quote/")], "Get Your Free Quote",
                   "Tell us about the job. Then let's schedule a consultation that works around your routine.",
                   "crew-crane-loading-roofing-materials", "Two roofers guiding a crane-lifted pallet of roofing materials", "Let's get started") + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
  <div class="reveal"><p class="eyebrow">Free, no pressure</p><h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">What happens next</h2>
    <ol class="steps">
      <li><div><h3>We read your request</h3><p>Photos help. Upload one if you can (max 2 MB).</p></div></li>
      <li><div><h3>We call to set a time</h3><p>We work around your schedule so we don't interfere with your day.</p></div></li>
      <li><div><h3>We inspect and quote</h3><p>You get a written bid with the materials and the method.</p></div></li>
    </ol>
    <div class="contact-cards" style="margin-top:28px">
      <div class="ccard"><h3>Phone</h3><a href="tel:{SITE["tel"]}">{SITE["phone"]}</a></div>
      <div class="ccard" style="background:var(--ember);color:var(--pine)"><h3 style="color:var(--pine)">Emergencies</h3><a href="tel:{SITE["emerg_tel"]}" style="color:var(--pine)">{SITE["emerg"]}</a></div>
    </div></div>
  <form class="form reveal d1" method="post" action="" enctype="multipart/form-data">
    <div class="row"><label>First name *<input name="first" autocomplete="given-name" required></label><label>Last name *<input name="last" autocomplete="family-name" required></label></div>
    <div class="row"><label>Phone *<input type="tel" name="phone" autocomplete="tel" required></label><label>Email *<input type="email" name="email" autocomplete="email" required></label></div>
    <div class="row"><label>Business name *<input name="business" autocomplete="organization" required></label>
    <label>Project type *<select name="type" required><option value="">--</option><option>Roof repair</option><option>Residential roofing</option><option>Commercial roofing</option><option>Waterproofing</option><option>Pond / water feature</option><option>Other</option></select></label></div>
    <label>Project description *<textarea name="description" required></textarea></label>
    <label>Upload an image of your project (max 2 MB)<input type="file" name="photo" accept="image/*"></label>
    <button class="btn" type="submit">Request my quote {ARROW}</button>
    <p class="note">* Required. Homeowners can put "Home" as the business name.</p>
  </form>
</div></section>
'''

QUOTE = {
    "path": "get-a-quote/",
    "title": "Free Roofing Quote in Salt Lake City | Advanced Roofing",
    "meta": "Request a free roofing quote in Salt Lake City for repairs, new roofs, commercial roofing, waterproofing or pond liners. Upload a photo and we'll call you back.",
    "body": Q_BODY, "og": "crew-crane-loading-roofing-materials",
    "schema": [{"@type": "WebPage", "@id": U + "get-a-quote/#page", "url": U + "get-a-quote/", "name": "Get a Quote", "about": {"@id": BIZ_ID}},
               crumbs_schema([("Home", ""), ("Get a Quote", "get-a-quote/")])],
}

# ----------------------------------------------------------------- 404
NF = {
    "path": "404.html", "title": "Page Not Found | Advanced Roofing & Moisture Control",
    "meta": "This page doesn't exist. Head back to Advanced Roofing & Moisture Control's home page, our roofing services or the contact page to find what you need.",
    "robots": "noindex, follow", "canonical": False, "sitemap": False, "full_biz": False,
    "body": f'''<section class="page-hero">{img("snow-on-roof-edge", "Snow hanging over the edge of a roof", priority=True)}<div class="wrap">
<p class="eyebrow light">Error 404</p><h1>This page slid off the roof</h1><p class="lede">The page you wanted isn't here. Try one of these instead.</p>
<div class="btn-row" style="margin-top:28px"><a class="btn" href="@/">Home {ARROW}</a><a class="btn ghost" href="@/roof-repair/">Roof repair</a><a class="btn ghost" href="@/contact/">Contact</a></div></div></section>''',
    "schema": [],
}

PAGES = [PARKCITY, SLC, UTAH, CLIENTS, TESTIMONIALS, CONTACT, QUOTE, NF]
