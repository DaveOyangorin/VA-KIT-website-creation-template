from build import SITE, ARROW, PHONE, img, cta_band

CLIENTS = ["ModSpace Properties", "Challenger Schools", "Big O Tires", "Taco Time", "Wonder Bread",
           "Staker Parson Offices", "Chase Building", "Miracle Bowl", "Cedar Park Office Buildings",
           "After Hours Medical", "Germania Lift Center", "Union Center", "Oak Street Plaza",
           "Schmidt Signs", "Emery Schools", "A-1 Self Storage"]


def ticker():
    lis = "".join(f"<li>{c}</li>" for c in CLIENTS)
    return f'''<section class="ticker" aria-label="Some of our commercial roofing clients">
<div class="ticker-track"><ul>{lis}</ul><ul aria-hidden="true">{lis}</ul></div></section>'''


def tile(cls, n, title, text, href, image, alt):
    return f'''<a class="tile {cls} reveal" href="@/{href}">{img(image, alt)}
<div class="tile-body"><span class="num">{n}</span><h3>{title}</h3><p>{text}</p><span class="go">Learn more {ARROW}</span></div></a>'''


BODY = f'''
<section class="hero">
  <div class="hero-media">{img("slc-skyline-snowy-wasatch", "Downtown Salt Lake City under the snow-covered Wasatch Mountains", priority=True)}
    <span class="hero-tag">Salt Lake City from the East Bench</span></div>
  <div class="wrap">
    <div class="hero-copy">
      <p class="kicker">Advanced Roofing &amp; Moisture Control</p>
      <h1><span class="line">Salt Lake City</span><span class="line">Roofing Company</span><span class="line accent">Built for Winter.</span></h1>
      <p class="lede">Advanced Roofing and Moisture Control is a roofing company in Salt Lake City that repairs, replaces and waterproofs roofs on homes and commercial buildings. We work across the Salt Lake Valley and up in Park City, and every quote is free.</p>
      <div class="btn-row"><a class="btn" href="tel:{SITE["tel"]}">{PHONE} {SITE["phone"]}</a><a class="btn ghost" href="@/get-a-quote/">Get a Free Quote {ARROW}</a></div>
      <ul class="trust"><li>BBB A+ rating</li><li>Licensed &amp; insured</li><li>Homes &amp; businesses</li><li>Free quotes</li></ul>
    </div>
  </div>
</section>

{ticker()}

<section class="sec paper">
  <div class="wrap intro">
    <div class="reveal"><p class="eyebrow">Roofers in Salt Lake City</p>
      <h2>Your roof is the first line of defense</h2></div>
    <div class="reveal d1">
      <p class="big">The airport alone averages <em>about 65 inches of snow</em> a year, and the benches get closer to 100. Add July sun at 4,300 feet and storms that roll off the Great Salt Lake, and you can see why roofs here wear out the way they do.</p>
      <p>Salt Lake City has harsh winters. Without a sound roof you aren't protected, so it has to be taken care of properly: the right shingles or membrane, real waterproofing, and drainage that moves snowmelt off the roof instead of under it.</p>
      <p>That's the work we do. As a roofing contractor in Salt Lake City we handle <a href="@/roof-repair/">roof repair</a>, new roofs and re-roofing for <a href="@/residential/">homes</a> and <a href="@/commercial/">commercial buildings</a>, plus <a href="@/waterproofing/">waterproofing</a> and even <a href="@/ponds/">pond liners</a>. Same crew, same standard, whether it's a family home or a flat roof downtown.</p>
      <p class="muted" style="font-size:.85rem">Snowfall figures: University of Utah, <a href="https://www.inscc.utah.edu/~steenburgh/utah_climo/snowstorms.html" rel="noopener">Salt Lake Valley Snowstorms</a>.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><p class="eyebrow">What we do</p><h2>Roofing services for<br>homes &amp; commercial buildings</h2>
      <p class="lede">Pick the job you've got. Each page explains how we handle it, what it involves and what to ask before you hire anyone.</p></div>
    <div class="mosaic">
      {tile("lg", "01", "Roof Repair", "Leaks, missing shingles, storm and tree damage, flashing, gutters. We find where the water's really getting in and fix that.", "roof-repair/", "rain-dripping-shingle-edge", "Rainwater running off the edge of a shingle roof")}
      {tile("md", "02", "Commercial Roofing", "Flat and pitched roofs, re-roofing, new construction and a maintenance program for property owners.", "commercial/", "white-flat-roof-wasatch-mountains", "White flat commercial roof with the Wasatch Mountains in the distance")}
      {tile("md", "03", "Residential Roofing", "New roofs, re-roofing and repairs in asphalt, metal, tile or wood, with the ventilation done right.", "residential/", "shingle-roof-homes", "Gabled asphalt shingle roofs on two-story homes")}
      {tile("sm", "04", "Waterproofing", "Stops leaks, cuts energy loss and adds years to the roof you already have.", "waterproofing/", "gutter-storm-clouds", "Metal gutter and downspout under dark storm clouds")}
      {tile("sm", "05", "Ponds &amp; Water Features", "EPDM, PVC and other liners for ponds, catchments and reservoirs.", "ponds/", "pond-waterfall-garden", "Garden pond with a small waterfall surrounded by shrubs")}
      {tile("sm", "06", "Park City Roofing", "Residential and commercial roofing and waterproofing up the canyon.", "park-city-commercial-roofing-and-waterproofing-solutions/", "park-city-shingle-roof-timber-home", "Shingle roof on a timber-sided home in Park City")}
    </div>
  </div>
</section>

<section class="sec dark">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow light">Proof, not promises</p>
      <h2>Roofs and liners from Cody to Emery County</h2>
      <p class="lede">These numbers come straight from our client list: real buildings, real ponds, real places.</p>
      <div class="stats" style="margin-top:34px">
        <div class="stat"><b>32</b><span>commercial roofing clients named on our list, and many more</span></div>
        <div class="stat"><b>100K<small>sq ft</small></b><span>pond liner at the Assey Pond in Orem, our largest listed</span></div>
        <div class="stat"><b>3</b><span>states: Utah, Wyoming (Cody) and Montana (West Yellowstone)</span></div>
        <div class="stat"><b>A+</b><span>rating with the Better Business Bureau</span></div>
      </div>
      <a class="textlink" href="@/clients/" style="margin-top:22px">See the client list {ARROW}</a>
    </div>
    <div class="frame reveal d1">{img("crew-crane-loading-roofing-materials", "Two roofers in hard hats guiding a crane-lifted pallet of roofing materials")}
      {img("roofer-hard-hat-on-site", "Roofer in a yellow hard hat watching a lift on a job site", cls="inset")}</div>
  </div>
</section>

<section class="sec paper">
  <div class="wrap split rev">
    <div class="reveal">
      <p class="eyebrow">Why people call us back</p>
      <h2>A crew with the right gear and a plan</h2>
      <p>We're fully licensed, insured and certified for both residential and commercial roofing. Our roofers show up with the tools, equipment and materials to finish the job, not to come back next week for parts.</p>
      <ul class="checks">
        <li>Fast response when a roof is leaking</li>
        <li>Written bids that list the materials and how they'll be applied</li>
        <li>Work scheduled around your routine or your business hours</li>
        <li>A clean site when we leave, and follow-up after</li>
      </ul>
      <p>One homeowner told us the bid "included pictures of specific areas that needed repair." That's how we like to work: you should see what we see before you spend a dollar.</p>
      <a class="textlink" href="@/testimonials/">Read the full reviews {ARROW}</a>
    </div>
    <div class="frame green reveal d1">{img("crew-crane-staging-from-above", "Crane staging roofing materials on a commercial job, seen from above")}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><p class="eyebrow">Roofing materials we install</p><h2>Four materials that work in Utah</h2>
      <p class="lede">The right pick depends on your home, your budget and how long you plan to stay. Here's the short version.</p></div>
    <div class="rail">
      <article class="mat reveal"><div class="ph">{img("material-asphalt-shingles", "Close-up of asphalt shingles on a sloped roof")}</div><div class="body"><span class="tag">Most common</span><h3>Asphalt shingles</h3><p>Dozens of colors, fits almost any house and costs less than the others. Warranties usually run 20 to 30 years.</p></div></article>
      <article class="mat reveal d1"><div class="ph">{img("standing-seam-metal-cupola", "Standing-seam metal roof with a small cupola")}</div><div class="body"><span class="tag">Longest life</span><h3>Metal panels &amp; tiles</h3><p>The fastest-growing home roofing material. Goes up quickly, needs little care and may carry a lifetime warranty.</p></div></article>
      <article class="mat reveal d2"><div class="ph">{img("material-clay-tile", "Roofer setting red clay tiles in place on a sloped roof")}</div><div class="body"><span class="tag">Heavy duty</span><h3>Concrete &amp; clay tile</h3><p>Lasts like metal and can mimic wood or slate. It's heavy, so the framing has to be checked first.</p></div></article>
      <article class="mat reveal d3"><div class="ph">{img("cedar-shake-roof", "Cedar shake roof under a clear blue sky")}</div><div class="body"><span class="tag">Classic look</span><h3>Wood shakes</h3><p>Thick shakes take hail well and look great. Fire concerns have made them less common.</p></div></article>
    </div>
    <p style="margin-top:56px"><a class="textlink" href="@/residential/">Compare materials for your home {ARROW}</a></p>
  </div>
</section>

<section class="bleed">
  {img("snow-on-roof-edge", "Thick layer of snow hanging over the edge of a roof")}
  <div class="wrap"><div class="copy reveal">
    <p class="eyebrow light">Winter in the valley</p>
    <h2>Snow isn't the problem. Meltwater is.</h2>
    <p class="lede">Heat leaking into the attic melts the snow on top. The water runs down, freezes again at the cold eaves and builds an ice dam that pushes water up under the shingles.</p>
    <p style="color:rgba(255,255,255,.82)">The fix starts inside: air sealing, insulation and venting that keeps the roof deck cold. Then good flashing, clear gutters and drains that work. Lake-effect snowbands hit the valley several times a winter, so this isn't a once-in-a-decade problem here.</p>
    <a class="btn" href="@/blog/how-long-do-roofs-last-in-utah/">How Utah weather ages a roof {ARROW}</a>
  </div></div>
</section>

<section class="sec paper">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">How a job runs</p>
      <h2>From first call to final walk-through</h2>
      <p class="lede">No pressure, no mystery. Here's what happens after you call.</p>
      <div class="btn-row" style="margin-top:26px"><a class="btn dark" href="@/get-a-quote/">Start with a free quote {ARROW}</a></div>
    </div>
    <ol class="steps reveal d1">
      <li><div><h3>You call or send a request</h3><p>Phone, the quote form or email. Tell us what's going on and when you're around.</p></div></li>
      <li><div><h3>We inspect the roof</h3><p>We get up there, find the cause and take photos so you can see it too.</p></div></li>
      <li><div><h3>You get a written bid</h3><p>Materials, method and price in writing. Compare it with anyone else's.</p></div></li>
      <li><div><h3>We do the work and clean up</h3><p>Scheduled around you, finished clean, and we're a phone call away after.</p></div></li>
    </ol>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><p class="eyebrow">What clients say</p><h2>Words from our clients</h2></div>
    <div class="quotes">
      <figure class="quote feature reveal"><blockquote><p>The bid was very detailed and included pictures of specific areas that needed repair. The crew doing the work was polite, competent, and they left the yard clean. This was the first winter we did not need to use a space heater in one particular room of the house.</p></blockquote>
        <figcaption>Tammy Radice<span>Roof replacement on their home</span></figcaption></figure>
      <figure class="quote reveal d1"><blockquote><p>I couldn't be happier with the quality and timeliness with the workmanship. Everything was as promised and then some.</p></blockquote>
        <figcaption>Doug Foster, ChFC, CLU<span>Re-roof of their home</span></figcaption></figure>
      <figure class="quote reveal d2"><blockquote><p>Extremely honest and especially responsive when repairs are needed to stop damage to tenant spaces and buildings.</p></blockquote>
        <figcaption>Vincent E. Webb, ChFC, CLU<span>Commercial property manager, 30+ years</span></figcaption></figure>
    </div>
    <p style="margin-top:28px"><a class="textlink" href="@/testimonials/">More testimonials {ARROW}</a></p>
  </div>
</section>

<section class="sec tight sage">
  <div class="wrap split">
    <div class="reveal"><p class="eyebrow">Where we work</p><h2>Salt Lake County, Park City &amp; beyond</h2>
      <p>Most of our work is Salt Lake City commercial roofing and Park City residential roofing. We also cover West Jordan, Sandy, South Salt Lake and the rest of Salt Lake County, and our client list stretches from Ogden and Layton down to Provo and Emery County.</p>
      <a class="textlink" href="@/utah-commercial-and-residential-roofers/">See our Utah service area {ARROW}</a></div>
    <div class="frame reveal d1">{img("herriman-winter-aerial", "Aerial view of a Herriman, Utah neighborhood with snowy mountains behind")}</div>
  </div>
</section>

{cta_band()}
'''

PAGE = {
    "path": "",
    "title": "Roofing Company Salt Lake City, UT | Advanced Roofing",
    "meta": "Advanced Roofing & Moisture Control is a licensed, insured roofing company in Salt Lake City for homes and businesses: repairs, new roofs and waterproofing.",
    "body": BODY,
    "og": "slc-skyline-snowy-wasatch",
    "schema": [],
}
