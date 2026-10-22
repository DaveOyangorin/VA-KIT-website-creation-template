"""Home page for the therepairpros.com redesign: "The service manual".
Every fact here is from The Repair Pros' own home page (src/extract.json): products, symptoms, process, prices, warranty, brands,
cities and testimonials (word for word, names as shown)."""
from engine import img, faq_html, faq_ld, crumbs_ld
from cfg import U, COUNTIES
import pagekit as K
from pagekit import ARROW, PHONE, HOME

APPS = [("refrigerator", "Refrigerator", "rp-fridge", ["Not cooling well", "Not making ice", "Not dispensing water", "Making noise"]),
        ("washer", "Washer", "rp-washer-dryer", ["Not working", "Not draining", "Not spinning", "Making noise"]),
        ("dryer", "Dryer", "rp-laundry-pair", ["Not working", "Not spinning", "Not heating up", "Making noise"]),
        ("oven", "Oven", "rp-range", ["Not heating", "Not cooking well", "Burners not working"]),
        ("tv", "Television", "rp-tv-install", ["Dead, no power", "Distorted or faded picture", "Lost sound"]),
        ("dishwasher", "Dishwasher", None, ["Not cleaning the dishes well", "Not draining", "Leaking"]),
        ("microwave", "Microwave", None, ["Something else"]), ("range-hood", "Range hood", None, ["Something else"]), ("air-dresser", "Air dresser", None, ["Something else"])]
STEPS = [("Request online", "You can quickly and easily request service online for any of the products we repair."),
         ("We contact you", "We contact you to discuss service call rates for your product and area."),
         ("Start repair", "Our skilled technicians are ready to tackle your TV or appliance repair."),
         ("Your job done", "You can trust that your job will be done right the first time, with warranteed work.")]
BRANDS = [("Samsung", "Branded engineer", "The highest level of Samsung service provider."),
          ("Sharp", "Master service center", "The highest level of Sharp service provider."),
          ("Philips TV", "Authorized service center", "The only authorized service center for Philips TV in Utah."),
          ("Dacor", "Authorized service center", "High-end luxury kitchen appliances.")]
OTHER = "Whirlpool, Maytag, KitchenAid, Amana, Jenn-Air, GE, Hotpoint, GE Profile, Caf&eacute;, Monogram, Haier, Viking"
QUOTES = [("I had a great experience with the repair pros! Their office staff reached out promptly to schedule my service visit, and on the day of install they were very communicative with the arrival window. The service technician Rodney was friendly, personable, and knowledgeable. My issue was resolved, and we&rsquo;re happy customers!", "Jamison Fox"),
          ("Mark was amazing in getting my TV fixed. He was very polite and explained everything to me that I wanted and needed to know. I highly recommend these guys for all appliance repair", "Scott"),
          ("Rodney came out and fixed up our frozen Samsung ice maker. He was very patient with it even though the repair took twice as long as he expected it would. He did great work and definitely took care of us.", "Mathew Greeson"),
          ("Jason was our technician and he was dispatched for warranty on the touchscreen of my less than one month old Samsung refrigerator. I was incredibly upset about the appliance but the service company called promptly even though I&rsquo;m in Cache Valley, a long drive from Draper. They ordered the parts they thought were applicable after listening to my thoughts and arrived during their scheduled appt window. Jason was able to make the repair and ensure everything was functioning as it should. Given the circumstances, I had a great experience with this repair company.", "Mason Salzetti"),
          ("Wow, I&rsquo;ve never had such an amazing service man! Mark knew exactly what to do and how to quickly get the job done. Our tv is now ready for the all important weekend game. When we heard of all the other items they repair I kept the card and placed it where it could be found quickly for our next repair need. I will ask for Mark each time.", "Nancy Butler"),
          ("Rodney was very informative, nice and friendly. Also, Tara, (office) helped me greatly! She&rsquo;s sweet and helpful and I am very grateful for everyone including the parts department for all they have done to help me as well. Thank you repair pros.", "Jenny penny Barthel"),
          ("Very Profesional. I have had them repair appliances twice now and both times went well. Thank you!", "Russ G")]
WHY = [("Screened technicians", "Licensed, insured, background and drug screened."), ("Factory trained", "Expert factory certified and trained technicians."),
       ("We come to you", "A large service area across four counties."), ("First-visit fixes", "Fast repairs, usually fixed on the first visit."),
       ("Original parts", "Factory original parts with a 90-day parts and labor warranty on the work done.")]
HOME_FAQ = [("How much does an appliance repair cost?", "<p>Repair costs vary a lot with the issue and the product. The average job runs <b>$150&ndash;$400</b>. There&rsquo;s no way to price a repair accurately without diagnosing it first, so we offer an on-site service call for <b>$125</b> to have a technician come and diagnose the problem, or a virtual repairman visit and estimate at a fraction of that cost.</p>"),
            ("What warranty do repairs come with?", "<p>We use only factory original parts, with a 90-day parts and labor warranty on the work done.</p>"),
            ("Do you fix it on the first visit?", "<p>Usually, yes. Our technicians are factory certified and trained, and most repairs are fixed on the first visit.</p>"),
            ("Which brands do you repair?", f"<p>We&rsquo;re a Samsung branded engineer, a Sharp master service center, the only authorized service center for Philips TV in Utah, and a Dacor authorized service center. We also work on all major brands out of warranty, including {OTHER}.</p>"),
            ("Where do you work?", "<p>On site across Salt Lake, Utah, Davis and Weber counties, from Ogden to Santaquin. If you don&rsquo;t see your city listed, ask whether we can service your area.</p>")]


def diag():
    tabs = "".join(f'<button type="button" class="dg-tab{" on" if i == 0 else ""}" data-app="{k}" id="fix-{k}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n, im, sy) in enumerate(APPS))
    data = "".join(f'<div class="dg-sy{" on" if i == 0 else ""}" data-for="{k}">' + "".join(f'<button type="button" data-sym="{s}">{s}</button>' for s in sy) + "</div>" for i, (k, n, im, sy) in enumerate(APPS))
    return f'''<div class="dg" data-diag><div class="dg-in">
<div class="dg-pick"><p class="step-k"><b>1</b> What needs fixing?</p><div class="dg-tabs" role="group" aria-label="Product">{tabs}</div>
<p class="step-k"><b>2</b> What&rsquo;s it doing?</p><div class="dg-syms">{data}</div></div>
<div class="ticket" aria-live="polite"><div class="tk-paper" data-tk>
<div class="tk-head"><span>The Repair Pros</span><span>Work order</span></div>
<dl><div><dt>Product</dt><dd data-tk-app>Refrigerator</dd></div><div><dt>Complaint</dt><dd data-tk-sym>Pick a symptom</dd></div>
<div><dt>Step 1</dt><dd>On-site diagnosis: <b>$125 service call</b>. Or a virtual repairman visit and estimate at a fraction of the cost.</dd></div>
<div><dt>Typical job</dt><dd><b>$150&ndash;$400</b> average. Costs vary with the issue and the product.</dd></div>
<div><dt>Parts</dt><dd>Factory original</dd></div><div><dt>Warranty</dt><dd>90 days, parts and labor, on the work done</dd></div></dl>
<div class="tk-foot"><a class="btn accent" href="#book" data-tk-book>Book this repair {ARROW}</a><a class="tk-call" href="tel:+18012686868">{PHONE} (801) 268-6868</a></div>
<div class="tk-tear" aria-hidden="true"></div></div></div>
</div></div>'''


def area():
    tabs = "".join(f'<button type="button" class="ar-tab{" on" if i == 0 else ""}" data-c="{i}">{c}<small>{len(t)} cities</small></button>' for i, (c, t) in enumerate(COUNTIES))
    lists = "".join(f'<ul class="ar-list{" on" if i == 0 else ""}" data-cl="{i}">' + "".join(f"<li>{x}</li>" for x in t) + "</ul>" for i, (c, t) in enumerate(COUNTIES))
    return f'<div class="ar" data-area><div class="ar-tabs">{tabs}</div><div class="ar-lists">{lists}</div></div>'


def home():
    n_cities = sum(len(t) for c, t in COUNTIES)
    opts = "".join(f"<option>{n} repair</option>" for k, n, im, sy in APPS if k != "air-dresser") + "<option>Air dresser repair</option><option>Other/misc repair</option>"
    body = f'''
<section class="m-hero"><div class="wrap m-hero-in">
<div class="m-hero-txt"><p class="label"><span class="dot"></span>On-site service &middot; Salt Lake, Utah, Davis &amp; Weber counties</p>
<h1>Appliance repair in Salt Lake City, <span>and flat panel TVs too.</span></h1>
<p class="lede">The Repair Pros fixes refrigerators, washers, dryers, ovens, dishwashers, microwaves, range hoods and TVs at your home. Factory-trained technicians, factory original parts, and most repairs done on the first visit.</p>
<div class="btn-row"><a class="btn accent" href="#diagnose">Start a work order {ARROW}</a><a class="btn ghost" href="tel:+18012686868">{PHONE} (801) 268-6868</a></div>
<dl class="spec"><div><dt>Service call</dt><dd>$125</dd></div><div><dt>Average job</dt><dd>$150&ndash;400</dd></div><div><dt>Warranty</dt><dd>90 days</dd></div><div><dt>Cities</dt><dd>{n_cities}</dd></div></dl></div>
<figure class="m-van">{img("rp-van", "The Repair Pros service van, lettered with the company name and phone number", priority=True)}<figcaption><span>Fig. 1</span> The van that comes to you</figcaption></figure>
</div>
<div class="brandline" aria-label="Factory authorized brands"><div class="wrap"><span>Factory authorized</span><b>Samsung</b><b>Sharp</b><b>Philips TV</b><b>Dacor</b><span class="bl-more">+ all major brands out of warranty</span></div></div></section>

<section class="sec m-diag" id="diagnose"><div class="wrap">
<div class="m-head reveal"><p class="label">01 &middot; Diagnose</p><h2>Tell us what it&rsquo;s doing. <span>We&rsquo;ll write it up.</span></h2>
<p class="lede">Pick the product and the symptom. You&rsquo;ll get the work order we&rsquo;d start with: what the visit costs, what a typical job runs, and what&rsquo;s covered.</p></div>
{diag()}
</div></section>

<section class="sec m-work"><div class="wrap">
<div class="m-head split-h reveal"><div><p class="label">02 &middot; What we repair</p><h2>All types of appliances, <span>and flat panel TVs.</span></h2></div><p class="lede">Nine product lines, fixed in your kitchen, laundry room or living room. These are our own jobs.</p></div>
<div class="m-gal">
<a class="g g1 reveal" href="#fix-refrigerator"><figure>{img("rp-fridge", "A French-door refrigerator after a repair visit")}</figure><span class="g-n">Fig. 2</span><b>Refrigerators</b><p>Not cooling well, not making ice or dispensing water, making noise.</p></a>
<a class="g g2 reveal" href="#fix-washer"><figure>{img("rp-washer-dryer", "A front-load washer and dryer pair in a laundry room")}</figure><span class="g-n">Fig. 3</span><b>Washers</b><p>Not working, not draining or spinning, making noise.</p></a>
<a class="g g3 reveal" href="#fix-oven"><figure>{img("rp-range", "A stainless steel range after an oven repair")}</figure><span class="g-n">Fig. 4</span><b>Ovens &amp; ranges</b><p>Not heating, not cooking well, burners not working.</p></a>
<a class="g g4 reveal" href="#fix-dryer"><figure>{img("rp-laundry-pair", "A top-load washer and dryer next to a water heater")}</figure><span class="g-n">Fig. 5</span><b>Dryers</b><p>Not working, not spinning or heating up, making noise.</p></a>
<a class="g g5 reveal" href="#fix-tv"><figure>{img("rp-tv-install", "A wall-mounted flat panel TV in a living room")}</figure><span class="g-n">Fig. 6</span><b>Televisions</b><p>Dead, no power, distorted or faded picture, lost sound.</p></a>
<div class="g g6 reveal"><span class="g-n">Also</span><b>Dishwashers, microwaves, range hoods &amp; air dressers</b><p>Dishwasher not cleaning well, not draining, leaking? We fix those too.</p><a class="tlink" href="#fix-dishwasher">Start a work order {ARROW}</a></div>
</div></div></section>

<section class="sec m-brands" id="brands"><div class="wrap">
<div class="m-head reveal"><p class="label">03 &middot; Factory authorized</p><h2>Authorized by the brands <span>we repair.</span></h2></div>
<div class="br-grid">{"".join(f'<div class="br reveal"><span class="br-k">{k}</span><b>{n}</b><p>{t}</p></div>' for n, k, t in BRANDS)}</div>
<p class="br-other"><b>Out of warranty, all major brands:</b> {OTHER} and more.</p>
</div></section>

<section class="sec m-how"><div class="wrap">
<div class="m-head reveal"><p class="label">04 &middot; How it works</p><h2>Four steps, <span>start to done.</span></h2></div>
<ol class="steps">{"".join(f'<li class="reveal"><span class="st-n">{i + 1:02d}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))}</ol>
</div></section>

<section class="sec m-price" id="pricing"><div class="wrap m-price-in">
<div class="reveal"><p class="label">05 &middot; Pricing</p><h2>How much does a repair cost?</h2>
<p>Repair costs vary a lot depending on the issue and the product, and there&rsquo;s no way to price a repair accurately without diagnosing it first. So the first step is a diagnosis: an on-site service call, or a virtual repairman visit and estimate at a fraction of the cost. Contact us for pricing and availability.</p>
<a class="btn" href="#book">Request service {ARROW}</a></div>
<div class="gauge reveal"><div class="gg"><small>On-site service call</small><b>$125</b><span>A technician comes and diagnoses the issue</span></div>
<div class="gg"><small>Average cost per job</small><b>$150<i>&ndash;</i>$400</b><span>Depends on the issue and the product</span></div>
<div class="gg"><small>Parts and labor warranty</small><b>90<i> days</i></b><span>Factory original parts, on the work done</span></div></div>
</div></section>

<section class="sec m-why"><div class="wrap">
<div class="m-head reveal"><p class="label">06 &middot; Why us</p><h2>Reasons customers <span>keep calling.</span></h2></div>
<ul class="why">{"".join(f'<li class="reveal"><b>{t}</b><p>{d}</p></li>' for t, d in WHY)}</ul>
<div class="quotes" data-quotes>{"".join(f'<blockquote class="q{" on" if i == 0 else ""}"><p>&ldquo;{q}&rdquo;</p><footer>{n}</footer></blockquote>' for i, (q, n) in enumerate(QUOTES))}
<div class="q-nav"><button type="button" data-q-prev aria-label="Previous review">&larr;</button><span data-q-n>1 / {len(QUOTES)}</span><button type="button" data-q-next aria-label="Next review">&rarr;</button></div></div>
</div></section>

<section class="sec m-area" id="area"><div class="wrap">
<div class="m-head split-h reveal"><div><p class="label">07 &middot; Service area</p><h2>{n_cities} cities, <span>four counties.</span></h2></div><p class="lede">If you don&rsquo;t see your city listed, ask whether we can service your area.</p></div>
{area()}
</div></section>

<section class="sec m-book" id="book"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">08 &middot; Book</p><h2>Request service online.</h2><p class="lede">Send the form and we&rsquo;ll contact you to go over service call rates for your product and area. Or call <a href="tel:+18012686868">(801) 268-6868</a>.</p>
<h3 class="faq-h">Common questions</h3>{faq_html(HOME_FAQ)}</div>
<div class="reveal"><form class="form" method="post" action=""><h3>Request service</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label>
<label for="f-prod">Product type<select id="f-prod" name="product" data-prod>{opts}</select></label>
<label for="f-msg">What&rsquo;s it doing?<textarea id="f-msg" name="message" data-msg></textarea></label>
<p class="sms">By providing your mobile phone number, you are agreeing to receive SMS Notifications and Status Updates from The Repair Pros. Message frequency may vary. Standard Message and Data rates may apply. You will be able to Opt-Out of SMS text messages by replying &ldquo;STOP&rdquo; to any message you receive. Help is available by replying &ldquo;HELP&rdquo;. Consent is not a condition of purchase. Your mobile information will not be shared or sold with third parties for promotional or marketing purposes. <a href="@/sms-privacy-and-terms/">SMS Terms</a></p>
<button class="btn" type="submit">Submit {ARROW}</button></form></div>
</div></section>

<section class="sec m-blog"><div class="wrap"><a class="post-band reveal" href="@/blog/repair-or-replace-appliance-lifespan/"><span class="label">From the shop</span><b>Repair or replace? How long appliances actually last</b><em>Read the guide {ARROW}</em></a></div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": "Appliance Repair Salt Lake City | The Repair Pros, TV Repair",
            "meta": "Appliance repair in Salt Lake City and across Utah, Davis and Weber counties: refrigerators, washers, dryers, ovens and TVs. $125 service call, 90-day warranty.",
            "body": body, "body_class": "is-home", "og": "rp-van", "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}
