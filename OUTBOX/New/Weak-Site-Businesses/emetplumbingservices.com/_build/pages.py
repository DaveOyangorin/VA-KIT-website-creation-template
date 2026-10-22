"""Pages for the emetplumbingservices.com redesign: "Straight answers".

Emet means truth, and the company's whole pitch is honesty: a $59.99 diagnostic that goes toward the repair, no fix no fee, and membership
plans with every rate published. So the home page opens on a full-bleed photo of their real fleet and crew, and the signature is the plan
calculator, laid out like an itemized invoice: enter the plumbing hours, after-hours hours and service calls you expect in a year, and it
totals the cost with no plan and with each of their four plans, using only the figures on their memberships page, then marks the cheapest.
Navy and sunrise orange from the van livery; Bricolage Grotesque, Figtree, Spline Sans Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 14 URLs (no trailing slash; /home kept on the site build) plus one new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

POSTS = [("ourblog/water-heater-season-is-upon-us/", "ourblog_water_heater_season_is_upon_us", "Water heater season is upon us!", "Oct 1, 2026", "2026-10-01",
          "Why fall and winter are hard on water heaters: colder incoming water, more hot water use, sediment, aging tanks and holiday guests. What to watch for."),
         ("ourblog/the-real-cost-of-ignoring-a-small-leak/", "ourblog_the_real_cost_of_ignoring_a_small_leak", "The Real Cost of Ignoring a Small Leak", "Mar 24, 2026", "2026-03-24",
          "A small drip can raise your water bill, rot wood, grow mold and corrode pipes. What a small leak really costs a Utah homeowner, and when to call a plumber."),
         ("ourblog/how-to-prepare-your-ac-unit-for-summer-heat/", "ourblog_how_to_prepare_your_ac_unit_for_summer_heat", "How to Prepare Your AC Unit for Summer Heat", "Mar 23, 2026", "2026-03-23",
          "Get your air conditioner ready before Utah's summer heat: replace the filter, clean the outdoor unit, check the thermostat and airflow, and test it early."),
         ("ourblog/5-signs-your-water-heater-is-about-to-fail/", "ourblog_5_signs_your_water_heater_is_about_to_fail", "5 signs your water heater is about to fail", "Mar 19, 2026", "2026-03-19",
          "No hot water, strange noises, rusty water, leaks around the tank and an old unit: five signs your water heater may be close to failing, and what to do."),
         ("ourblog/sp5seqfckf120har2h03je3p5uvymx/", "ourblog_sp5seqfckf120har2h03je3p5uvymx", "What to Do If Your Pipe Bursts in Salt Lake City", "Mar 17, 2026", "2026-03-17",
          "A burst pipe in a Salt Lake City winter: shut off the main water, drain the lines, cut power near water, clean up fast, and know when to call a plumber.")]
TITLES = {t for _, _, t, _, _, _ in POSTS}
STOP = re.compile(r"^Subscribe to our newsletter|^EMET PLUMBING|^Contact\s*Emet|^Call/Text:|^Website:", re.I)


def ptitle(t):
    n = lambda s: len(html.unescape(s))
    opts = [t + s for s in (" | Emet Plumbing Heating &amp; Air", " | Emet Plumbing, Utah", " | Emet Plumbing", " | Emet")]
    ok = [o for o in opts if 50 <= n(o) <= 60]
    return ok[0] if ok else max((o for o in opts if n(o) <= 60), key=n, default=t)


def blocks(key):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    s = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", s)
    s = s[s.find('role="main"'):]
    out, started = [], False
    for t, x in re.findall(r"(?s)<(h1|h2|h3|h4|p|li)\b[^>]*>(.*?)</\1>", s):
        x = re.sub(r"<(br|/strong|/b)\s*/?>", r"\g<0>&#8203;", x)
        segs = [y for y in (re.sub(r"\s+", " ", html.unescape(z).replace("​", "")).strip() for z in re.split(r"<[^>]+>", x)) if y]
        if not segs: continue
        if t == "h1": started = True; continue
        if not started: continue
        txt = " ".join(segs)
        if STOP.search(txt) or (t == "h2" and txt in TITLES): break
        out.append((t, segs))
    return out


def render(b):
    res, ul = [], []
    def flush():
        if ul: res.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul.clear()
    for t, segs in b:
        if t == "li": ul.append(html.escape(" ".join(segs))); continue
        flush()
        if t == "p":
            m = re.match(r"^(\d+\.|Step \d+:)\s*(.+)$", segs[0])
            if len(segs) > 1 and len(segs[0]) < 90:
                res.append(f"<p><strong>{html.escape(segs[0].rstrip('.').rstrip(':'))}.</strong> {html.escape(' '.join(segs[1:]))}</p>")
            elif m and ". " in segs[0][len(m.group(1)):]:
                head, rest = segs[0].split(". ", 1) if segs[0].startswith("Step") else (segs[0], "")
                res.append(f"<p><strong>{html.escape(head)}.</strong> {html.escape(rest)}</p>" if rest else f"<p>{html.escape(segs[0])}</p>")
            else:
                res.append(f"<p>{html.escape(' '.join(segs))}</p>")
        else:
            res.append(f"<h2>{html.escape(' '.join(segs))}</h2>")
    flush()
    return "\n".join(res)


PLANS = [("none", "No plan", 0, 175, 225, 59, ""),
         ("essential", "Essential", 200, 150, 150, 0, "$20/month or $200/year"),
         ("premium", "Premium", 480, 140, 150, 0, "$40/month or $480/year"),
         ("elite", "Elite", 650, 130, 150, 0, "$60/month or $650/year"),
         ("emet", "The EMET Plan", 1000, 120, 150, 0, "$100/month or $1,000/year ($750 to renew)")]
PERKS = {"essential": ["10% off all plumbing services", "1 free annual plumbing inspection", "Priority scheduling within 48 hours", "5% off HVAC tune-ups", "3-month extended workmanship warranty"],
         "premium": ["Everything in Essential", "15% off all plumbing services", "2 annual plumbing inspections (spring &amp; fall)", "1 free drain cleaning per year", "Water heater flush at 50% off", "10% off HVAC services", "6-month extended workmanship warranty"],
         "elite": ["Everything in Premium", "20% off all plumbing services", "Free water heater flush once a year", "$100 credit toward any major repair", "Annual sewer line camera inspection", "9-month extended workmanship warranty"],
         "emet": ["Everything in Elite", "25% off all plumbing services", "Same-day guaranteed service scheduling", "1 free minor repair (up to $200 in labor a year)", "Free annual HVAC tune-up", "Annual whole-home plumbing checkup with a detailed report", "$250 credit toward water heater or softener replacement"]}


def calculator():
    data = [{"k": k, "n": n, "fee": f, "rate": r, "ah": a, "call": c} for k, n, f, r, a, c, _ in PLANS]
    rows = "".join(f'<li data-row="{k}"><span class="iv-n">{n}<small>{note or "Standard rates"}</small></span><span class="iv-v" data-tot="{k}">$0</span></li>' for k, n, f, r, a, c, note in PLANS)
    return f'''<div class="inv" data-calc>
<div class="inv-in"><p class="label">Your year, roughly</p>
<label class="rng"><span>Plumbing labor <b><i data-out="h">4</i> hrs</b></span><input type="range" min="0" max="20" step="1" value="4" data-in="h" aria-label="Plumbing labor hours per year"></label>
<label class="rng"><span>After-hours emergency <b><i data-out="a">1</i> hrs</b></span><input type="range" min="0" max="8" step="1" value="1" data-in="a" aria-label="After-hours emergency hours per year"></label>
<label class="rng"><span>Service calls <b><i data-out="c">2</i></b></span><input type="range" min="0" max="8" step="1" value="2" data-in="c" aria-label="Service calls per year"></label>
<p class="inv-fine">Uses the rates on our memberships page: $175/hr standard, after-hours +$225/hr (+$150/hr for members), service call fee $59.00 (voided for members). Excludes parts, percentage discounts, credits and free services, so plans usually save more than shown.</p></div>
<div class="inv-out"><div class="inv-head"><span>Estimate</span><span class="mono">EMET &middot; Plan check</span></div><ol class="inv-rows" aria-live="polite">{rows}</ol>
<p class="inv-best" data-best>&nbsp;</p><a class="btn accent" href="@/memberships/">See what each plan includes {ARROW}</a></div>
<script type="application/json" data-calc-data>{json.dumps(data)}</script></div>'''


FAQ = [("What does a service visit cost?", "<p>Our diagnostic is $59.99, and it&rsquo;s always applied toward your repair. If we can&rsquo;t fix your issue, you don&rsquo;t pay.</p>"),
       ("Do you offer emergency plumbing?", "<p>Yes. We&rsquo;re always just a call away with reliable 24/7 emergency response. Extra costs may apply after hours.</p>"),
       ("Do you do heating and air too?", "<p>Yes. We specialize in plumbing and HVAC, from leaky faucets to full heating and air conditioning installations, for homes and businesses.</p>"),
       ("Are you the same company as DrainBuster?", "<p>Yes. Emet Plumbing Heating &amp; Air was formerly known as DrainBuster.</p>")]
SERV = [("Plumbing repair", "From leaky faucets up, for homes and commercial clients."), ("Drains &amp; sewer lines", "Drain cleaning and sewer line repair."),
        ("Main waterline", "Main waterline service and repair."), ("Water heaters", "Water heater service, flushes and replacement."),
        ("Heating &amp; air", "Maintenance, repairs and full heating and AC installations."), ("24/7 emergencies", "Middle-of-the-night emergencies too. Extra costs may apply.")]


def home():
    body = f'''
<section class="m-hero"><div class="mh-img" data-parallax="0.08">{img("em-fleet", "The Emet Plumbing Heating & Air crew kneeling in front of their fleet of blue service vans", priority=True)}</div>
<div class="wrap mh-in"><div class="mh-txt"><p class="label">Taylorsville &middot; Salt Lake Valley &middot; Est. 2018</p>
<h1>Your plumber in Taylorsville, <em>with honest pricing.</em></h1>
<p class="lede">Emet Plumbing Heating &amp; Air is a family-owned plumber in Taylorsville, formerly DrainBuster. Plumbing, drains, sewer and main waterlines, water heaters and HVAC for homes and businesses, with same-day service and 24/7 emergency response.</p>
<div class="btn-row"><a class="btn accent" href="tel:+18014337354">{PHONE} Call or text (801) 433-7354</a><a class="btn ghost" href="@/contact/">Book a service {ARROW}</a></div></div>
<div class="mh-tag" aria-label="No fix, no fee"><span>Diagnostic</span><b>$59.99</b><span>applied to your repair</span><i>Can&rsquo;t fix it? You don&rsquo;t pay.</i></div></div></section>

<section class="sec m-serv" id="plumbing"><div class="wrap">
<div class="m-head split-h reveal"><div><p class="label">What we do</p><h2>Plumbing, heating <em>&amp; air.</em></h2></div><p class="lede">Residential and commercial. Routine maintenance or a middle-of-the-night emergency, one family-owned team.</p></div>
<div class="serv">{"".join(f'<div class="sv reveal"><span class="mono">{i + 1:02d}</span><b>{t}</b><p>{d}</p></div>' for i, (t, d) in enumerate(SERV))}</div>
</div></section>

<section class="sec m-calc" id="plans"><div class="wrap">
<div class="m-head split-h reveal"><div><p class="label">Membership plans, itemized</p><h2>Does a plan <em>pay for itself?</em></h2></div><p class="lede">Every rate is published. Move the sliders to your year and see the total with no plan and with each of our four plans.</p></div>
{calculator()}
</div></section>

<section class="m-crew"><div class="wrap m-crew-in">
<div class="reveal"><p class="label">Where truth meets excellence</p><h2>Family-owned. <em>Community first.</em></h2>
<p>Unlike the bigger corporate companies, we believe quality work shouldn&rsquo;t come with sky-high prices or long wait times. That&rsquo;s why we offer affordable rates and faster response times, getting to our service calls quickly so you&rsquo;re not left waiting.</p>
<p>We believe in more than just fixing problems. We believe in building trust, delivering excellence, and keeping our customers for life.</p>
<a class="tlink" href="@/about/">About Emet {ARROW}</a></div>
<div class="crew-pics"><figure class="reveal">{img("em-crew", "The Emet crew standing in front of a branded service van")}</figure><figure class="reveal">{img("em-install", "Two Emet technicians beside a new water heater installation")}</figure></div>
</div></section>

<section class="sec m-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Straight <em>answers.</em></h2>
<a class="post-card m-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What MERV ratings mean, which filter EPA suggests, and how often to check it, from EPA and ENERGY STAR.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Plumber Taylorsville, UT | Emet Plumbing Heating &amp; Air",
            "meta": "Emet Plumbing Heating & Air: family-owned plumber in Taylorsville. Drains, sewer and waterlines, water heaters, HVAC. $59.99 diagnostic toward your repair.",
            "body": body, "body_class": "is-home", "og": "em-fleet", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    out.append(dict(home(), path="home/", canonical=U, site_only=True, sitemap=False))
    ab = f'''<p class="answer">Welcome to Emet Plumbing, where truth meets excellence. We&rsquo;re a family-owned and operated plumbing and HVAC company serving residential and commercial clients, formerly known as DrainBuster, est. 2018.</p>
<p>At Emet Plumbing, we are proud to be a family-owned and operated business that puts our community first. Serving both residential and commercial clients, we specialize in high-quality plumbing and HVAC services, and we&rsquo;re always just a call away with our reliable 24/7 emergency response (extra costs may apply).</p>
<p>Unlike the bigger corporate companies, we believe quality work shouldn&rsquo;t come with sky-high prices or long wait times. That&rsquo;s why we offer affordable rates and faster response times, getting to our service calls quickly so you&rsquo;re not left waiting. That&rsquo;s why our $59.99 diagnostic is always applied toward your repair, and if we can&rsquo;t fix your issue, you don&rsquo;t pay.</p>
<p>From leaky faucets to full heating and air conditioning installations, our skilled team is equipped to handle it all. Whether it&rsquo;s routine maintenance or a middle-of-the-night emergency, Emet Plumbing is ready to serve with honesty, integrity, and a commitment to doing the job right the first time.</p>
<p>We believe in more than just fixing problems. We believe in building trust, delivering excellence, and keeping our customers for life. Experience the Emet difference: affordable, dependable, and driven by values.</p>
<div class="pgal">{img("em-tech", "An Emet technician at the back of a branded service van")}{img("em-van", "An Emet Plumbing Heating & Air service van")}{img("em-install", "Two Emet technicians beside a water heater installation")}</div>'''
    out.append(K.page("about/", "About", "About Emet Plumbing", "Where truth meets excellence.", "Family-owned &middot; est. 2018", "About Emet Plumbing Heating &amp; Air | Family-Owned Plumber",
                      "Emet Plumbing Heating & Air, formerly DrainBuster: a family-owned plumbing and HVAC company for homes and businesses in Taylorsville and the Salt Lake Valley.",
                      ab, image="em-crew", alt="The Emet crew in front of a service van", canonical=EXT["about"]["canon"]))
    mem = '<p class="answer">Four membership plans for plumbing, HVAC and home maintenance. Every price and rate below is our published rate. Standard rates without a plan: $175/hr, after-hours +$225/hr, service call fee $59.00.</p>' + calculator() + \
          '<div class="plans">' + "".join(f'<div class="plan-c"><p class="label">{note}</p><h3>{n}</h3><dl><div><dt>Hourly rate</dt><dd>${r}/hr</dd></div><div><dt>After-hours</dt><dd>+${a}/hr</dd></div><div><dt>Service call fee</dt><dd>Voided</dd></div></dl><ul>' +
                                          "".join(f"<li>{p}</li>" for p in PERKS[k]) + "</ul></div>" for k, n, f, r, a, c, note in PLANS[1:]) + "</div>" + \
          '<p class="small">The EMET Plan is $1,000 for the first year, then $750 if you renew. After-hours emergency rates are charged on top of the regular hourly rate.</p>'
    out.append(K.page("memberships/", "Memberships", "Membership plans", "Every rate, published.", "Home care plans", "Plumbing &amp; HVAC Membership Plans | Emet Plumbing &amp; Air",
                      "Emet membership plans for plumbing, HVAC and home maintenance: Essential, Premium, Elite and the EMET Plan, with published rates and a plan calculator.",
                      mem, image="em-van", alt="An Emet service van", canonical=EXT["memberships"]["canon"]))
    hv = '''<p class="answer">Reliable HVAC service for homes and businesses: maintenance, repairs and full heating and air conditioning installations. Call or text (801) 433-7354 for same-day service.</p>
<h2>Heating and air, done right</h2><ul><li>HVAC maintenance and tune-ups</li><li>Heating and air conditioning repairs</li><li>Full heating and air conditioning installations</li><li>Filter, airflow and thermostat checks</li></ul>
<h2>Why maintenance matters</h2><p>A clean HVAC system improves indoor air quality, reducing allergens and dust. Your AC doesn&rsquo;t just cool, it dehumidifies, and maintenance keeps it running efficiently. A well-maintained system cools faster and runs quieter, and consistent maintenance protects your home from costly emergency repairs.</p>
<p>ENERGY STAR recommends a contractor check your cooling system in the spring and your heating system in the fall. Members on the EMET Plan get a free annual HVAC tune-up; other plans include HVAC discounts.</p>
<p><a class="tlink" href="@/memberships/">Membership plans</a> &nbsp; <a class="tlink" href="@/''' + p_blog.SLUG + '''">Furnace filters, explained</a></p>'''
    out.append(K.page("hvac/", "HVAC", "Heating &amp; air conditioning", "Maintenance, repairs and installations.", "HVAC", "HVAC Service in Taylorsville &amp; Salt Lake | Emet Plumbing",
                      "Heating and air conditioning service from Emet: HVAC maintenance, repairs and installations for homes and businesses in Taylorsville and the Salt Lake Valley.",
                      hv, image="em-tech", alt="An Emet technician at a service van", canonical=EXT["hvac"]["canon"]))
    con = f'''<p class="answer">Let&rsquo;s work together. Call or text, email, or send the form and we&rsquo;ll get back to you.</p>
<dl class="info"><div><dt>Call or text</dt><dd><a href="tel:+18014337354">(801) 433-7354</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Address</dt><dd><address>5941 S Redwood Rd<br>Taylorsville, UT 84123</address></dd></div><div><dt>Emergencies</dt><dd>24/7 (extra costs may apply)</dd></div></dl>'''
    out.append(K.page("contact/", "Contact", "Contact Emet Plumbing", "Plumbing, heating, air and commercial service.", "Contact", "Contact Emet Plumbing Heating &amp; Air | Taylorsville, UT",
                      "Contact Emet Plumbing Heating & Air in Taylorsville: call or text (801) 433-7354 or email to book plumbing, drain, sewer, water heater or HVAC service.",
                      con, canonical=EXT["contact"]["canon"], form_side=True))
    emp = '''<p class="answer">Our team is quickly growing, and we offer new and exciting employment opportunities in residential and commercial plumbing and HVAC.</p>
<blockquote><p>&ldquo;At Emet Plumbing, we know that every journey starts somewhere, and we&rsquo;re proud to welcome team members from all walks of life. Whether you&rsquo;re just beginning your career, changing paths, or bringing decades of hands-on experience, there&rsquo;s a place for you here. As a family-owned company, we value integrity, hard work, and a team-first mindset. Join us, grow your skills, and become part of a company that treats you like family, because at Emet Plumbing, you&rsquo;re more than an employee, you&rsquo;re part of the crew.&rdquo;</p><cite>The owner</cite></blockquote>
<p>Ready to get started? Fill out the form to begin the hiring process. It&rsquo;s quick, easy, and the first step to joining the Emet Plumbing family.</p>'''
    out.append(K.page("employment/", "Employment", "Careers at Emet", "Join a growing, family-owned crew.", "Employment", "Plumbing &amp; HVAC Jobs in Salt Lake City | Emet Plumbing",
                      "Plumbing and HVAC careers at Emet Plumbing Heating & Air: a growing, family-owned residential and commercial team in the Salt Lake Valley. Apply today.",
                      emp, image="em-crew", alt="The Emet crew", canonical=EXT["employment"]["canon"], form_side=True))
    bl = '<div class="cats">' + f'<a class="cat" href="@/{p_blog.SLUG}"><b>{p_blog.H1}</b><span>Oct 22, 2026</span><em>Read {ARROW}</em></a>' + \
         "".join(f'<a class="cat" href="@/{p}"><b>{t}</b><span>Bj Zelch &middot; {d}</span><em>Read {ARROW}</em></a>' for p, k, t, d, iso, m in POSTS) + "</div>"
    out.append(K.page("ourblog/", "Blog", "Emet Insights", "Plumbing and HVAC tips for Utah homes.", "Blog", "Emet Insights: Plumbing &amp; HVAC Tips | Emet Plumbing",
                      "Emet Insights: plumbing, water heater and HVAC tips for Utah homeowners, from burst pipes and small leaks to furnace filters and getting AC ready for summer.",
                      bl, canonical=EXT["ourblog"]["canon"]))
    for p, k, t, d, iso, m in POSTS:
        out.append(K.page(p, t, t, f"By Bj Zelch &middot; {d}", "Emet Insights", ptitle(t), m, render(blocks(k)) + f'<p>Questions? Call or text <a href="tel:+18014337354">(801) 433-7354</a>.</p>',
                          crumbs=[("Blog", "ourblog/")], canonical=EXT[k]["canon"], ogtype="article",
                          schema=[{"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": t, "datePublished": iso, "author": {"@type": "Person", "name": "Bj Zelch"}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)}]))
    out.append(K.page("clients/", "Clients", "Commercial clients", "", "Clients", "Commercial Clients | Emet Plumbing Heating &amp; Air",
                      "Emet Plumbing Heating & Air works with commercial partners as well as homeowners. Become a partner: call or text (801) 433-7354 or email us today.",
                      '<p>We are proud of the work we&rsquo;ve done for our commercial partners. Interested in becoming a partner? <a href="@/contact/">Contact us</a>.</p>', canonical=EXT["clients"]["canon"], robots="noindex, follow", sitemap=False))
    out.append(K.page("member-site-homepage-1/", "Members", "Members", "", "Memberships", "Members | Emet Plumbing Heating &amp; Air",
                      "Emet Plumbing Heating & Air membership plans for plumbing, HVAC and home maintenance. See every plan and its published rates on our memberships page.",
                      '<p>See our <a href="@/memberships/">membership plans</a>.</p>', canonical=EXT["member_site_homepage_1"]["canon"], robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Memberships", "memberships/"), ("HVAC", "hvac/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call or text (801) 433-7354.", " Taylorsville, UT.")) for x in out]
