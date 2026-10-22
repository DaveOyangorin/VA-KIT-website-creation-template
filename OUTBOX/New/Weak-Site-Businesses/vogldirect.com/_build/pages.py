"""Pages for the vogldirect.com redesign: "Direct".

Their whole pitch is the name: up-front, transparent, no added fluff, from a veteran-owned shop in Eagle Mountain. So the design is plain-spoken
and confident: a full-bleed photo of Mount Timpanogos at dusk over Utah County, heavy condensed caps, and a service-tag amber. The signature is
the Comfort Club builder: pick a plan, add the monthly add-ons, and see exactly what you get and what it costs per month and per year, using
their own published prices. No upsell, the way their filter page talks.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 22 URLs (trailing slash) and canonicals."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

REV = [("We recently had central air installed in our home. Zach gave us a very fair price and was extremely easy to work with. He was very helpful and able to answer any questions we had concerning the install. He went above and beyond in getting us scheduled quickly and completing the job in a very timely manner. I highly recommend Vogl Direct to anyone with heating and cooling needs.", "William M."),
       ("Great service and professionalism. Came out to my house late at night on a holiday to diagnose the problem. Completed the service quickly and I would recommend him to family and friends.", "Scott E."),
       ("Oh my is all I have to say. Vogl is the best. I called when my air started to make some weird noise. I explained what it was doing over the phone and he came out the same day to look at it. It was fixed the next day. Best service ever!!", "C. Smith"),
       ("Great company. Called to have him come look at my furnace. He was able to come out the same day and was able to resolve the issue. He is very honest and only fixed what needed to be fixed.", "Adam F."),
       ("Zach was awesome. He kept us in the loop at all times and was fantastic to work with. Very accommodating. I highly recommend Vogl Direct for all your HVAC needs.", "Andrea F.")]
PLANS = [("basic", "Basic", 8.99, "24%", ["1 AC tune-up", "1 furnace tune-up", "5% off repairs", "Guaranteed service within 48 hours"]),
         ("preferred", "Preferred", 15.99, "40%", ["1 AC tune-up", "1 furnace tune-up", "10% off repairs", "Guaranteed service within 24 hours", "1 combustion efficiency test", "1 additional high-end filter per visit", "50% off after-hours or weekend rates", "Preferred pricing"]),
         ("plus", "Preferred Plus", 34.99, "50%", ["1 AC tune-up", "1 furnace tune-up", "15% off repairs", "Guaranteed same-day service", "Diagnostic fee waived with repair on service calls", "1 in-place coil cleaning and sanitation", "1 combustion efficiency test", "1-year supply of high-end filters (2 additional per visit)", "$50 credit per year of membership toward a replacement system", "Never pay after-hours or weekend rates", "Preferred Plus pricing", "Lifetime warranty on repairs"])]
ADDONS = [("salt", "Water softener salt", 9, "Twice a year we deliver and fill salt to the optimal level (additional bags left by the unit)."),
          ("dryer", "Dryer vent cleaning", 4, "Twice a year we clean out your dryer vents."),
          ("wh", "Water heater", 6, "Annually inspect and drain your water heater to remove sediment."),
          ("smoke", "Smoke detectors", 4, "Annually replace the batteries in up to 5 smoke or carbon monoxide detectors.")]
WHY = [("Veteran owned", "Our owners are proud veterans of the U.S. armed forces."), ("Locally owned", "Big-brand quality with locally owned customer service."),
       ("24-hour service", "Available at any hour for emergency repairs (fees apply)."), ("American Standard", "Quality equipment and tools on every job.")]
FAQ = [("Do you offer free estimates?", "<p>Yes. We offer professional, on-site estimates at no cost, and a free second opinion. Call or text (385) 352-3285.</p>"),
       ("What areas do you serve?", "<p>All of Utah County, Salt Lake County and Tooele. We&rsquo;re based in Eagle Mountain.</p>"),
       ("Are you available after hours?", "<p>Yes. Our regular hours are 8 am to 5 pm, Monday to Sunday, and we offer 24-hour emergency service (fees apply).</p>"),
       ("Why do I need regular maintenance?", "<p>All furnace and AC manufacturers require regular maintenance to keep their warranties valid. Every Comfort Club plan qualifies as that required maintenance.</p>"),
       ("What brands do you install?", "<p>American Standard and Mitsubishi, for new construction, remodels, basement finishes and retrofits. Every installation includes a Lifetime Workmanship Guarantee.</p>")]


def money(v):
    return f"${v:,.2f}"


def builder():
    plans = "".join(f'''<label class="pl-card" data-plan="{k}"><input type="radio" name="plan" value="{k}" data-price="{p}"{" checked" if k == "preferred" else ""}>
<span class="pc-in"><span class="pc-save">{s} instant savings</span><b>{n}</b><span class="pc-price">{money(p)}<small>/mo</small></span></span></label>''' for k, n, p, s, f in PLANS)
    feats = "".join(f'<ul class="pf" data-feats="{k}"{"" if k == "preferred" else " hidden"}>{"".join(f"<li>{x}</li>" for x in f)}</ul>' for k, n, p, s, f in PLANS)
    adds = "".join(f'<label class="ad"><input type="checkbox" value="{k}" data-add="{v}"><span><b>{n} <i>+${v}/mo</i></b><small>{d}</small></span></label>' for k, n, v, d in ADDONS)
    return f'''<div class="cc" data-cc>
<div class="cc-l"><p class="cc-step"><span>1</span> Pick a plan</p><div class="pl-cards" role="radiogroup" aria-label="Comfort Club plan">{plans}</div>
<p class="cc-step"><span>2</span> Add what you want</p><div class="ads">{adds}</div></div>
<div class="cc-r" aria-live="polite"><div class="tag"><div class="tag-h"><span>Comfort Club</span><span data-cc-name>Preferred</span></div>
<p class="tag-total"><b data-cc-mo>$15.99</b><small>per month</small></p><p class="tag-yr"><span data-cc-yr>$191.88</span> a year &middot; 1-year commitment</p>
<div class="tag-feats">{feats}<ul class="pf adds" data-cc-adds></ul></div>
<p class="tag-note">Every plan qualifies as the regular maintenance manufacturers require to keep warranties valid.</p>
<a class="btn accent" href="@/contact-us/">Sign up by phone or text {ARROW}</a></div></div></div>'''


def rv(t, n, cls=""):
    return f'<blockquote class="rv{cls}"><p>{html.escape(t)}</p><footer>{html.escape(n)}</footer></blockquote>'


def home():
    body = f'''
<section class="d-hero"><div class="dh-img" data-parallax="0.08">{img("vg-timp", "Mount Timpanogos under snow, glowing pink at dusk above Utah County", priority=True)}</div>
<div class="wrap dh-in"><div class="dh-txt"><p class="label">Veteran owned &middot; Eagle Mountain &middot; Utah County, Salt Lake County &amp; Tooele</p>
<h1>HVAC company for Salt Lake City and Utah County. <em>Day or night.</em></h1>
<p class="lede">Up-front, transparent, honest heating and air work with no added fluff. Quick response, superior service and top-quality systems, wherever you need us.</p>
<div class="btn-row"><a class="btn accent" href="@/contact-us/">Schedule an appointment {ARROW}</a><a class="btn ghost" href="tel:+13853523285">{PHONE} Call or text (385) 352-3285</a></div></div>
<div class="ticket"><p class="tk-h">Free second opinion</p><p>Got a quote that doesn&rsquo;t sit right? Call or text and we&rsquo;ll take a look. Professional, on-site estimates at no cost.</p>
<dl><div><dt>Hours</dt><dd>Mon&ndash;Sun 8&ndash;5</dd></div><div><dt>Emergency</dt><dd>24 hours*</dd></div></dl><small>*Fees applicable</small></div></div>
<p class="credit">Mount Timpanogos &middot; Eric Ward, CC BY-SA 2.0, via Wikimedia Commons</p></section>

<section class="d-why"><div class="wrap why">{"".join(f'<div><b>{t}</b><span>{d}</span></div>' for t, d in WHY)}</div></section>

<section class="sec d-svc"><div class="wrap">
<div class="d-head split-h reveal"><div><p class="label">Our specialties</p><h2>Heat. Cool. <em>Done right.</em></h2></div><a class="tlink" href="@/services/">All services {ARROW}</a></div>
<div class="svc-grid">
<a class="sv big reveal" href="@/heating/"><span class="sv-n">01</span><b>Heating &amp; furnaces</b><p>Furnace repair, inspections, new installs, leaks and gas lines. We answer calls 24/7 so you&rsquo;re never left in the cold.</p><em>Heating {ARROW}</em></a>
<a class="sv big reveal" href="@/cooling/"><span class="sv-n">02</span><b>Cooling &amp; mini splits</b><p>AC repair, routine inspections, new central air, and ductless mini splits for hard-to-cool rooms.</p><em>Cooling {ARROW}</em></a>
<a class="sv reveal" href="@/installations/"><span class="sv-n">03</span><b>Installations</b><p>American Standard and Mitsubishi, sized to your home, with a Lifetime Workmanship Guarantee.</p></a>
<a class="sv reveal" href="@/duct-work-2/"><span class="sv-n">04</span><b>Duct work</b><p>Custom duct work for basement finishes: supply and return runs, exhaust fans, dryer vents.</p></a>
<a class="sv reveal" href="@/commercial/"><span class="sv-n">05</span><b>Commercial</b><p>Quarterly maintenance for furnaces, ACs, rooftop units and exhaust fans.</p></a>
<a class="sv reveal" href="@/reclaim/"><span class="sv-n">06</span><b>Refrigerant reclaim</b><p>Certified, licensed refrigerant removal before demolition or equipment removal.</p></a>
</div></div></section>

<section class="sec d-cc" id="comfort-club"><div class="wrap">
<div class="d-head split-h reveal"><div><p class="label">Comfort Club</p><h2>Build your plan. <em>See the real price.</em></h2></div><p class="lede">Three maintenance plans and four add-ons, at the prices we publish. Pick yours and the tag adds it up.</p></div>
{builder()}
</div></section>

<section class="d-band"><div class="band-img" data-parallax="0.1">{img("vg-lake", "Looking west over Utah Lake toward the Lake Mountains from Pleasant Grove")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Direct, by definition</p><p>Direct means up-front, transparent, honest work with no added fluff. We look forward to earning your business and exceeding your expectations.</p></blockquote></div>
<p class="credit">Utah Lake from Pleasant Grove &middot; Don LaVange, CC BY-SA 2.0, via Wikimedia Commons</p></section>

<section class="sec d-rev"><div class="wrap">
<div class="d-head split-h reveal"><div><p class="label">Reviews</p><h2>What neighbors <em>say.</em></h2></div><a class="tlink" href="@/our-reviews/">All reviews {ARROW}</a></div>
<div class="rv3">{"".join(rv(t, n, f" r{i}") for i, (t, n) in enumerate(REV[:3]))}</div></div></section>

<section class="sec d-deal"><div class="wrap"><div class="deals reveal">
<div class="deal"><span>Service</span><b>$25 off</b><p>any service when you mention this ad</p></div>
<div class="deal"><span>Filters</span><b>65% off</b><p>a year supply of air filters</p></div>
<div class="deal"><span>Rebates</span><b>Call</b><p>for current rebates on system replacements and installs</p></div>
<a class="btn accent" href="@/current-deals/">Current deals {ARROW}</a></div></div></section>

<section class="sec d-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card d-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>What EPA says about R-22 systems, the refrigerant you should never put in your AC, and why venting is illegal.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": EXT["home"]["canon"] or U, "title": "HVAC Company Salt Lake City &amp; Utah County | Vogl Direct",
            "meta": "Veteran-owned HVAC company serving Salt Lake City, Utah County and Tooele: furnace and AC repair and installs, 24-hour emergency service and free estimates.",
            "body": body, "body_class": "is-home", "og": "vg-timp", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def cl(k):
    return EXT[k]["canon"] or canon(k.replace("_", "-") + "/")


def make_pages():
    out = [home()]
    def P(path, k, label, h1, lede, title, meta, body, **kw):
        return K.page(path, label, h1, lede, kw.pop("tag", "Services"), title, meta, body, canonical=EXT[k]["canon"] if k in EXT and EXT[k]["canon"] else canon(path), **kw)
    sv = '<p class="answer">Heating, cooling, installations, duct work, air quality, commercial maintenance and refrigerant reclaim, across Utah County, Salt Lake County and Tooele.</p><div class="cats">' + \
         "".join(f'<a class="cat" href="@/{p}"><b>{l}</b><em>Learn more {ARROW}</em></a>' for p, l, i in K.C.SVC) + "</div>" + \
         "<h2>Free second opinion</h2><p>Call or text today to set up an appointment. We offer professional, on-site estimates at no cost.</p>"
    out.append(P("services/", "services", "Services", "HVAC Services", "Heating, cooling and everything in between.", "HVAC Services in Utah County &amp; Salt Lake | Vogl Direct",
                 "Vogl Direct HVAC services: heating, cooling, mini splits, installations, duct work, air quality, commercial maintenance and refrigerant reclaim.", sv, image="vg-lake", alt="Utah Lake and the Lake Mountains"))
    heat = '''<p class="answer">Furnace repair, inspections, new installations, leak calls and gas lines. We answer calls 24/7 for HVAC service, so you never have to worry about being left in the cold.</p>
<h2>Furnace repair in Utah</h2><p>Homeowners regularly call us for emergency furnace service. Whether your furnace is starting up and shutting down, blowing cold air, or just won&rsquo;t turn on, we can be at your home quickly to provide the necessary repairs.</p>
<h2>Furnace inspections</h2><p>Routine furnace maintenance will prolong the life of your system. Our technicians inspect your furnace, clean and lubricate the parts, test for gas leaks, and identify worn parts. We recommend seasonal tune-ups, and manufacturers require them to maintain their warranties. <a href=@/comfort-club/>Join the Comfort Club</a> for better deals on routine service.</p>
<h2>New furnace installation</h2><p>When it&rsquo;s time to upgrade to a new energy-efficient heating and cooling system, we&rsquo;ve helped hundreds of Utah homeowners choose the right system for their household and budget, including heat pumps. Every new furnace includes a free Aprilaire 4&Prime; filtration box with filter.</p>
<h2>Furnace leaks need immediate attention</h2><p>A puddle under your furnace, or a foul smell when it kicks on, needs an experienced technician. Water can be as simple as condensation, or a sign of a bigger problem. <strong>If you smell gas when your furnace blows air, shut it off immediately and call us.</strong></p>
<h2>Gas lines</h2><p>We install gas lines for dryers, stove tops, ranges, outdoor barbecues and more, using TracPipe flexible gas line. It&rsquo;s &ldquo;strike-proof&rdquo; and can be installed under and above ground.</p>'''
    out.append(P("heating/", "heating", "Heating", "Heating &amp; Furnace Repair and Installs", "24/7 furnace repair across Utah County and Salt Lake.", "Furnace Repair &amp; Heating, Utah County &amp; SLC | Vogl Direct",
                 "Furnace repair, inspections, new furnace installation and gas lines from veteran-owned Vogl Direct. 24/7 calls in Utah County, Salt Lake County and Tooele.", heat, image="vg-timp", alt="Mount Timpanogos in winter",
                 schema=K.svc_schema("heating/", "Furnace repair and installation", "Eagle Mountain, UT")))
    cool = '''<p class="answer">AC repair, routine inspections, new central air and ductless mini splits. We&rsquo;re up-front about which option is right for you, and we won&rsquo;t push the most expensive equipment.</p>
<h2>AC leaks need immediate attention</h2><p>Water on the floor may simply be condensation, but depending on your unit it can be a sign of a bigger problem. If you smell rotten eggs, or a carbon monoxide alarm goes off when your AC kicks on, <strong>shut it off and call us right away</strong>. Ignoring leaks leads to bigger, more expensive problems.</p>
<h2>Routine AC inspections</h2><p>Routine maintenance prolongs the life of your system. Our technician inspects your central air, cleans and lubricates the parts, and identifies worn parts. We recommend seasonal tune-ups for furnaces and air conditioners.</p>
<h2>New central air installation</h2><p>We&rsquo;ve helped hundreds of Utah homeowners choose the right central air system for their household and budget, with many units and cooling options to choose from.</p>
<h2>Mini splits</h2><p>A ductless system that can be installed just about anywhere, and usually more efficient than a traditional AC. Great for hard-to-cool or hard-to-heat spaces like offices, garages and bonus rooms, on new construction, basement finishes, remodels and retrofits.</p>
<h2>Why our cooling systems</h2><ul><li><strong>Cost-effective.</strong> We aren&rsquo;t going to push the most expensive equipment on you.</li><li><strong>American Standard.</strong> We work with reputable brands.</li><li><strong>Modern technology.</strong> We stay current, so you don&rsquo;t get an outdated AC.</li><li><strong>Built to last.</strong> Top-of-the-line equipment.</li></ul>'''
    out.append(P("cooling/", "cooling", "Cooling", "Air Conditioning Repair &amp; Installs", "Central air and mini splits, without the upsell.", "AC Repair &amp; Installation, Utah County &amp; SLC | Vogl Direct",
                 "AC repair, inspections, new central air and ductless mini splits from veteran-owned Vogl Direct, serving Utah County, Salt Lake County and Tooele, Utah.", cool, image="vg-lake", alt="Utah Lake in summer",
                 schema=K.svc_schema("cooling/", "Air conditioning repair and installation", "Eagle Mountain, UT")))
    out.append(P("installations/", "installations", "Installations", "HVAC Installations", "American Standard and Mitsubishi, sized right.", "Furnace &amp; AC Installation, Utah County | Vogl Direct",
                 "American Standard and Mitsubishi installs for new construction, remodels, basement finishes and retrofits, sized right, with a lifetime workmanship guarantee.",
                 '''<p class="answer">We install American Standard and Mitsubishi products for new construction, remodels, basement finishes and retrofits.</p>
<h2>Our process</h2><ol><li><strong>System sizing.</strong> We take the total square footage of the space and the number of vents into load calculations to properly size the equipment.</li><li><strong>Installation.</strong> We install the equipment to all local and federal codes.</li><li><strong>Start-up and balancing.</strong> Each system is run through the proper start-ups and balanced as needed for gas, refrigerant and air flow.</li></ol>
<p class="pull">All of our installations include a Lifetime Workmanship Guarantee.</p>''', image="vg-eagle", alt="The valley around Eagle Mountain from the air"))
    out.append(P("duct-work-2/", "duct_work_2", "Duct work", "Duct Work", "Custom duct work for basements and more.", "Duct Work &amp; Basement HVAC, Utah County | Vogl Direct",
                 "Finishing your basement? Vogl Direct adds supply and return runs to any home, plus flexible duct for exhaust fans and dryer vents. Free quotes: (385) 352-3285.",
                 '<p class="answer">Finishing your basement and need duct work? We have lots of experience with custom duct work for basements.</p><ul><li>Supply and return runs added to any home</li><li>Flexible duct for exhaust fans and dryer vents</li><li>HVAC supply and returns</li></ul><p>Basically any duct work you might need, we&rsquo;ve got your back.</p>'))
    out.append(P("air-quality/", "air_quality", "Air quality", "Air Quality &amp; Filters", "Change filters often. Skip the upsell.", "Air Quality &amp; Furnace Filters, Utah County | Vogl Direct",
                 "Why dirty filters cause HVAC breakdowns and higher bills, which filters actually work, and air cleaners like the Halo and air scrubber from Vogl Direct.",
                 '''<p class="answer">Dirty, old air filters are the number one cause of HVAC system malfunctions. Change them often, and you don&rsquo;t need the most expensive one.</p>
<h2>Why change your filter regularly</h2><ul><li><strong>System malfunctions.</strong> A dirty filter can damage heating and cooling equipment.</li><li><strong>Contaminated air.</strong> Dirty filters can&rsquo;t remove dust, pollen, animal fur, mold, lint, hair and bacteria.</li><li><strong>Higher energy bills.</strong> A clogged filter makes the system work harder.</li><li><strong>Ductwork buildup.</strong> Contaminants accumulate in the ducts and may require duct cleaning.</li></ul>
<h2>Air filters, honestly</h2><p>We won&rsquo;t try to upsell you. We know what works, and honestly, the cheaper options usually work just great. Many $20+ filters restrict air flow and can damage your system&rsquo;s components in both heating and cooling season. We recommend changing filters every 1.5 to 2 months.</p>
<p class="pull">A year supply of 1&Prime; pleated filters: $39.95. And a free air filter when you give us a call.</p>
<h2>Filtration systems</h2><p>For cleaner air we also offer the Halo air cleaner, ion sweeper and air scrubber. Every new furnace we install includes a free Aprilaire 4&Prime; filtration box with filter.</p>''', image="vg-lake", alt="Utah Lake"))
    out.append(P("filters/", "filters", "Filters", "Is It Time to Change Your Filter?", "Call us to schedule a filter replacement.", "Furnace Filter Replacement, Utah County | Vogl Direct",
                 "Time to change your furnace filter? Vogl Direct replaces filters and sells a year supply of 1-inch pleated filters for $39.95. Call or text (385) 352-3285.",
                 '<p class="answer">Call us today to schedule a filter replacement. We recommend changing filters every 1.5 to 2 months.</p><p>A year supply of 1&Prime; pleated filters is $39.95, and right now we have 65% off a year supply of air filters. <a href=@/air-quality/>Why filters matter</a>.</p>'))
    out.append(P("commercial/", "commercial", "Commercial maintenance", "Commercial HVAC Maintenance", "Quarterly maintenance for your building.", "Commercial HVAC Maintenance, Utah County | Vogl Direct",
                 "Quarterly commercial HVAC maintenance for furnaces, ACs, rooftop units and exhaust fans: belts, filters, coil cleaning and seasonal start-ups. Vogl Direct.",
                 '''<p class="answer">We&rsquo;d love to be the HVAC service contractor for your commercial building: furnaces, ACs, rooftop units, exhaust fans and more.</p>
<h2>Quarterly maintenance includes</h2><ul><li>Changing belts and filters</li><li>Cleaning coils and evaporators</li><li>Proper start-up of seasonal components</li><li>Your other maintenance needs</li></ul>
<h2>Furnace and AC inspections</h2><p>Our technicians inspect, clean and lubricate parts, test for gas leaks and identify worn parts. Seasonal tune-ups extend equipment life and keep manufacturer warranties valid.</p>''', image="vg-eagle", alt="The valley around Eagle Mountain"))
    out.append(P("reclaim/", "reclaim", "Reclaim", "Refrigerant Removal &amp; Reclaim", "Certified, licensed, properly recycled.", "Refrigerant Removal &amp; Reclaim in Utah | Vogl Direct",
                 "Demolishing a building or removing HVAC equipment? Vogl Direct has the equipment, certifications and licenses to remove and recycle refrigerant properly.",
                 '<p class="answer">When a building is demolished or HVAC equipment is removed, the refrigerant in those units needs to be properly removed and recycled.</p><p>We have the equipment, certifications and licenses to properly remove refrigerant from equipment being removed for a remodel or demolition. Federal rules make it illegal to knowingly vent refrigerant; <a href=@/' + p_blog.SLUG + '>here&rsquo;s what homeowners should know</a>.</p>'))
    out.append(P("solar/", "solar", "Solar", "Solar for Your Home", "Through our trusted partner.", "Home Solar Consultation, Utah | Vogl Direct Partner",
                 "Thinking about solar? Vogl Direct works with trusted partner Red Stone Clean Energy, who offers a free consultation for Utah homeowners going solar today.",
                 '<p class="answer">Thinking about going solar but don&rsquo;t know where to start? Red Stone Clean Energy is one of our trusted partners for helping make your home solar, and they offer a free consultation.</p>'))
    deals = '''<p class="answer">Mention these deals when you schedule.</p><div class="deals in"><div class="deal"><span>Service</span><b>$25 off</b><p>any service if you mention this ad</p></div>
<div class="deal"><span>Filters</span><b>65% off</b><p>a year supply of air filters</p></div><div class="deal"><span>Rebates</span><b>Call</b><p>for current rebates on system replacements and installations</p></div></div>'''
    out.append(P("current-deals/", "current_deals", "Current deals", "Current Deals", "Mention these when you schedule.", "HVAC Deals &amp; Rebates in Utah County, UT | Vogl Direct",
                 "Current Vogl Direct deals: $25 off any service, 65% off a year supply of air filters, and rebates on system replacements. Call or text (385) 352-3285.", deals, tag="Deals"))
    out.append(P("comfort-club/", "comfort_club", "Comfort Club", "Comfort Club Maintenance Plans", "Three plans. Real prices. Warranty-qualifying.", "Comfort Club HVAC Maintenance Plans, Utah | Vogl Direct",
                 "Vogl Direct Comfort Club: Basic $8.99, Preferred $15.99 and Preferred Plus $34.99 a month, with tune-ups, repair discounts and priority service.",
                 '<p class="answer">All furnace and AC manufacturers require regular maintenance to keep warranties valid. All of these plans qualify. One-year commitment.</p>' + builder(), tag="Comfort Club"))
    out.append(P("financing/", "financing", "Financing", "Financing", "Build a plan that works for your family.", "HVAC Financing, Utah County &amp; Salt Lake | Vogl Direct",
                 "Bigger HVAC project? Vogl Direct offers financing options so you don't have to pay everything up front. Call (385) 352-3285 for a free quote and a plan.",
                 '<p class="answer">Don&rsquo;t stress if you have a larger project and can&rsquo;t pay for it all up front. There are financing options available.</p><p>Give us a call and let&rsquo;s build a plan that works for you and your family. Call or text <a href="tel:+13853523285">(385) 352-3285</a>.</p>', tag="Financing"))
    out.append(P("resources/", "resources", "Resources", "Resources", "Plans and financing.", "HVAC Resources: Comfort Club &amp; Financing | Vogl Direct",
                 "Vogl Direct resources: Comfort Club maintenance plans that save you money and financing options for bigger heating and air conditioning projects in Utah County.",
                 f'<div class="cats"><a class="cat" href="@/comfort-club/"><b>Join the Comfort Club</b><span>Discounts on your maintenance needs.</span><em>See plans {ARROW}</em></a><a class="cat" href="@/financing/"><b>Financing options</b><span>Things break when you aren&rsquo;t prepared.</span><em>Learn more {ARROW}</em></a></div>'))
    ab = f'''<p class="answer">Vogl Direct is a locally owned and operated, veteran-owned heating and air conditioning company based in Eagle Mountain.</p>
<h2>Why choose Vogl Direct</h2><ul><li><strong>Experienced technicians</strong> who provide service we can be proud of.</li><li><strong>Locally owned and operated:</strong> big-brand quality with locally owned customer service.</li><li><strong>24-hour service</strong> for emergency repairs and fixes.</li><li><strong>Veteran owned:</strong> our owners are proud veterans of the U.S. armed forces.</li><li><strong>Competitive pricing</strong> for the quality of service we provide.</li><li><strong>American Standard equipment</strong> and quality tools on site.</li></ul>
<h2>Hours and area</h2><p>Regular hours: 8:00 am&ndash;5:00 pm, Monday&ndash;Sunday. Emergency service: 24 hours (fees applicable). We serve all of Utah County, Salt Lake County and Tooele.</p><h2>Reviews</h2><div class="rv-all">{"".join(rv(t, n) for t, n in REV)}</div>'''
    out.append(P("about/", "about", "About", "About Vogl Direct", "Veteran owned. Locally owned. Direct.", "About Vogl Direct | Veteran-Owned HVAC, Eagle Mountain UT",
                 "Vogl Direct is a veteran-owned, locally owned heating and air company in Eagle Mountain serving Utah County, Salt Lake County and Tooele, day or night.", ab, image="vg-eagle", alt="The valley around Eagle Mountain", tag="About"))
    out.append(P("our-reviews/", "our_reviews", "Reviews", "Our Reviews", "What our customers say.", "Vogl Direct Reviews | Heating &amp; Air in Utah County",
                 "Read what Vogl Direct customers say about same-day furnace and AC service, honest pricing and central air installs in Utah County and Salt Lake County.",
                 '<div class="rv-all">' + "".join(rv(t, n) for t, n in REV) + "</div>", tag="Reviews"))
    info = '''<p class="answer">Call or text us with any questions or to schedule an appointment. We&rsquo;re quick to respond.</p>
<dl class="info"><div><dt>Call or text</dt><dd><a href="tel:+13853523285">(385) 352-3285</a></dd></div><div><dt>Hours</dt><dd>Monday&ndash;Sunday 8:00 am&ndash;5:00 pm</dd></div>
<div><dt>Emergency</dt><dd>24 hours (fees applicable)</dd></div><div><dt>Area</dt><dd>Utah County, Salt Lake County and Tooele</dd></div></dl>'''
    out.append(P("contact-us/", "contact_us", "Contact", "Contact Vogl Direct", "Free estimates. Free second opinions.", "Contact Vogl Direct | HVAC, Utah County &amp; Salt Lake",
                 "Contact Vogl Direct: call or text (385) 352-3285 for a free on-site estimate or second opinion. Open 8 to 5 every day, 24-hour emergency HVAC service.", info, form_side=True, tag="Contact"))
    for path, k, h1 in (("recent-projects/", "recent_projects", "Recent Projects"), ("direct-news/", "direct_news", "Direct News"), ("energy-efficiency/", "energy_efficiency", "Energy Efficiency"), ("hello-world/", "hello_world", "Hello world!")):
        out.append(P(path, k, h1, h1, "", f"{h1} | Vogl Direct Heating and Air, Utah"[:60], "This page is being updated. See Vogl Direct's heating, cooling and Comfort Club pages, or call or text (385) 352-3285 for a free estimate.",
                     f'<p class="answer">This page is being updated.</p><p><a class="tlink" href="@/services/">Our services {ARROW}</a> &nbsp; <a class="tlink" href="@/{p_blog.SLUG}">From the blog {ARROW}</a></p>', robots="noindex, follow", sitemap=False, tag="Vogl Direct"))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Comfort Club", "comfort-club/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free estimates.", " Call (385) 352-3285.")) for x in out]
