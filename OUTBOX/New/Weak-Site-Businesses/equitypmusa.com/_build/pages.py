"""Pages for the equitypmusa.com redesign: "The owner's ledger".

Property management is a numbers business, and Equity publishes its numbers: placement 50-100% of one month's rent, full service 8-10%
monthly, a $65 application, income at 3x rent, payout within 5 business days. So the site reads like a well-kept ledger: navy and paper,
a serif for trust and tabular figures, ruled lines, and the signature "Rent math" calculator. Toggle Owner or Renter, set a monthly rent,
and every figure recalculates from Equity's own published rules.
References (screenshotted 21 Oct 2026): Stripe (numbers as the hero, calm navy), Mercury (banking clarity, generous white space),
Compass (real-estate editorial restraint). Same 21 URLs and canonicals; Wix template leftovers are noindex."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL, AREAS
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from fx import blocks
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CLAIMS = re.compile(r"1\.2%|75% of renters|one of the most established", re.I)
cta = K.cta


def footer():
    return re.sub(r'<span class="flogo"><img[^>]*></span>', '<span class="flogo">' + img("eq-white-logo", "Equity Real Estate Property Management logo") + '</span>', K.footer())


header = K.header
PROGRAMS = [("Marketing &amp; showing", 1, 1), ("Application processing", 1, 1), ("Lease signing", 1, 1), ("Monthly rent collection", 0, 1), ("Maintenance coordination", 0, 1),
            ("Evictions", 0, 1), ("Tenant communication", 0, 1), ("Lease enforcement", 0, 1)]


def faqs():
    out, q, a = [], None, []
    for t, x in blocks("copy_of_contact_us"):
        if t == "li": continue
        if t == "h3":
            if q and a: out.append((q, "".join(a)))
            q, a = x, []
        elif q and t == "p":
            plain = html.unescape(re.sub(r"<[^>]+>", "", x))
            sents = [s for s in re.split(r"(?<=[.!?])\s+", plain) if not CLAIMS.search(s)]
            if sents: a.append("<p>" + html.escape(" ".join(sents)) + "</p>")
    if q and a: out.append((q, "".join(a)))
    return out


def home():
    prog = "".join(f'<tr><td>{n}</td><td class="c">{"<span class=y>Included</span>" if a else "<span class=n>&mdash;</span>"}</td><td class="c">{"<span class=y>Included</span>" if b else "<span class=n>&mdash;</span>"}</td></tr>' for n, a, b in PROGRAMS)
    fq = faqs()
    pick = [x for x in fq if re.search(r"fees\?|choose tenants|inspections|accounting schedule|turnaround", html.unescape(x[0]))][:5]
    body = f'''
<section class="e-hero"><div class="eh-img" data-parallax="0.08">{img("eq-sandy", "Homes in Sandy, Utah, below the Wasatch Mountains", priority=True)}</div><div class="wrap e-hero-in">
<div><p class="label">Property management &middot; Sandy, Utah</p>
<h1>Property management in Sandy, <em>kept like a ledger.</em></h1>
<p class="lede">Equity Real Estate&rsquo;s property management division handles rentals for owners from tenant placement to full-service management, now in Utah, Florida, New Mexico, Oregon, Idaho, California and Hawaii.</p>
<div class="btn-row"><a class="btn accent" href="@/copy-of-landlords/">Request a rental analysis {ARROW}</a><a class="btn ghost" href="tel:+18015454302">{PHONE} 801-545-4302</a></div></div>
<aside class="e-card"><p class="label">At a glance</p><dl>
<div><dt>Full-service management</dt><dd>8&ndash;10%<small>of monthly rent, typically</small></dd></div>
<div><dt>Tenant placement</dt><dd>50&ndash;100%<small>of one month&rsquo;s rent</small></dd></div>
<div><dt>Owner payout</dt><dd>5 days<small>business days after full rent</small></dd></div>
<div><dt>Interior inspections</dt><dd>2&times;<small>per year, with photo report</small></dd></div></dl></aside>
</div>
<p class="credit">Atmosphere photo: Sandy, Utah &middot; Scott Catron, CC BY 2.5, via Wikimedia Commons</p>
<nav class="e-doors wrap" aria-label="How can we help?"><a href="@/copy-of-landlords/"><small>Owner</small><b>Owner information</b><span>Request a rental analysis</span></a><a href="@/copy-of-tenants/"><small>Tenant</small><b>Available rentals</b><span>Submit an application</span></a><a href="@/join-equity-pm/"><small>Agent</small><b>Join us</b><span>Submit a referral</span></a></nav></section>

<section class="sec e-calc" id="rent-math"><div class="wrap">
<div class="e-head reveal"><p class="label">Rent math</p><h2>Set a rent. <em>See the numbers.</em></h2><p class="lede">Every figure below is worked out from Equity&rsquo;s own published fees and rental criteria. Your management agreement or lease is what actually governs.</p></div>
<div class="calc" data-calc>
<div class="c-top"><div class="seg" role="tablist" aria-label="I am"><button type="button" class="on" data-mode="owner" aria-pressed="true">I&rsquo;m an owner</button><button type="button" data-mode="renter" aria-pressed="false">I&rsquo;m a renter</button></div>
<label class="rent"><span>Monthly rent</span><span class="rent-in"><b>$</b><input type="number" inputmode="numeric" min="300" max="20000" step="25" value="2000" data-rent aria-label="Monthly rent in dollars"></span></label>
<input class="slider" type="range" min="500" max="6000" step="25" value="2000" data-slider aria-label="Monthly rent slider"></div>
<div class="c-rows" data-rows="owner">
<div class="row"><span>Tenant placement (one-time leasing fee)</span><b data-f="place"></b><small>50&ndash;100% of one month&rsquo;s rent</small></div>
<div class="row"><span>Full-service management (monthly)</span><b data-f="mgmt"></b><small>Typically 8&ndash;10% of monthly rent, plus a one-time set-up fee that varies by location and manager</small></div>
<div class="row"><span>Security deposit (held in trust)</span><b data-f="dep"></b><small>Typically equal to one month&rsquo;s rent; you have no liability for it</small></div>
<div class="row"><span>Your rent payout</span><b>5 business days</b><small>After Equity receives full rent and pays any expenses, by direct deposit</small></div></div>
<div class="c-rows" data-rows="renter" hidden>
<div class="row"><span>Combined gross income needed</span><b data-f="inc"></b><small>At least 3&times; the monthly rent, across everyone in the rental</small></div>
<div class="row"><span>Or savings on hand</span><b data-f="sav"></b><small>A savings statement showing 12 months of rent</small></div>
<div class="row"><span>Application fee</span><b>$65 per adult</b><small>Non-refundable; each person 18+ applies separately</small></div>
<div class="row"><span>Security deposit</span><b data-f="dep2"></b><small>Typically one month&rsquo;s rent</small></div>
<div class="row"><span>If pets are allowed</span><b>$350 + $50/mo</b><small>Typical pet deposit and monthly pet fee; approved assistance animals are exempt</small></div></div>
</div></div></section>

<section class="sec e-prog"><div class="wrap e-prog-in">
<div class="reveal"><p class="label">Our programs</p><h2>Two ways <em>to work with us.</em></h2><p>Leave your investment worries to the pros. From basic tenant placement to full-service management, you decide how much involvement you want.</p><a class="tlink" href="@/copy-of-landlords/">Owner information {ARROW}</a><figure class="e-photo">{img("eq-street", "A tree-lined residential street in a Utah neighborhood")}<figcaption>Atmosphere photo: Skykingcarter, CC BY-SA 4.0, via Wikimedia Commons</figcaption></figure></div>
<div class="tbl reveal"><table class="ledger"><thead><tr><th>Service provided</th><th class="c">Tenant placement<small>One-time leasing fee</small></th><th class="c">Full service<small>Set-up fee + monthly fee</small></th></tr></thead><tbody>{prog}</tbody></table></div>
</div></section>

<section class="sec e-quote"><div class="wrap"><blockquote class="reveal"><p>&ldquo;I have trusted my rental homes in Salt Lake City, Sandy, and Stansbury Park with Equity Property Management for over 10 years, and they have done everything a homeowner could ever ask for! They are professional, hardworking, and extremely competent at what they do.&rdquo;</p><footer>SFH Properties &middot; Landlord</footer></blockquote></div></section>

<section class="sec e-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Owner FAQ</p><h2>The questions owners ask first.</h2>{faq_html(pick)}<p class="more"><a class="tlink" href="@/copy-of-contact-us/">All {len(fq)} questions {ARROW}</a></p></div>
<div class="reveal"><div class="e-office"><p class="label">Visit or call</p><p class="eo-ph"><a href="tel:+18015454302">801-545-4302</a></p><address>1218 E 7800 S Suite 150<br>Sandy, UT 84094</address><p>Monday &ndash; Friday, 9:00 AM &ndash; 5:00 PM MST</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="label" style="margin-top:22px">Now servicing</p><ul class="states">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul></div>
<a class="post-card e-post" href="@/{p_blog.SLUG}"><span class="label">For renters</span><b>{p_blog.H1}</b><p>The warning signs the FTC lists, and how to check a listing before you pay anything.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": EXT["home"]["canon"] or U, "title": "Property Management Sandy, UT | Equity Real Estate PM",
            "meta": "Equity Real Estate's property management division in Sandy, Utah: tenant placement and full-service rental management for owners. Call 801-545-4302.",
            "body": body, "body_class": "is-home", "og": "eq-logo", "schema": [crumbs_ld("", [HOME]), faq_ld(pick)]}


def render(k, drop=()):
    out, ul = [], []
    def flush():
        if ul: out.append("<ul>" + "".join(f"<li>{i}</li>" for i in ul) + "</ul>"); ul.clear()
    seen = False
    for t, x in blocks(k):
        plain = html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        if t == "li" and not seen: continue
        if not plain or any(d in plain for d in drop) or CLAIMS.search(plain): continue
        if t == "li": ul.append(x); continue
        flush(); seen = True
        if t == "h1": continue
        tag = "h2" if t in ("h2",) else ("h3" if t in ("h3", "h4") else "p")
        out.append(f"<{tag}>{x}</{tag}>")
    flush()
    return "\n".join(out)


def make_pages():
    out = [home()]
    P = lambda k: EXT[k]["url"].split(".com/", 1)[1] + "/"
    fq = faqs()
    out.append(K.page(P("copy_of_contact_us"), "FAQs", "Frequently Asked Questions", "For owners: fees, tenants, maintenance, accounting and more.", "FAQs",
                      "Property Management FAQs for Owners | Equity PM, Sandy UT",
                      "Equity Property Management FAQs: fees, tenant screening, maintenance, inspections, evictions, deposits, accounting, insurance, pets and vacancies.",
                      '<p class="answer">Straight answers to the questions rental owners ask most, from fees to what happens if a tenant doesn&rsquo;t pay.</p>' + faq_html(fq, open_first=True),
                      canonical=EXT["copy_of_contact_us"]["canon"], schema=[faq_ld(fq)]))
    land = render("copy_of_landlords", drop=("Request Rental Analysis", "Owner Log In", "Frequently Asked Questions", "Please take a moment", "First name", "Submit", "If you&rsquo;d like more"))
    land += '<h2>Our programs</h2><div class="tbl"><table class="ledger"><thead><tr><th>Service provided</th><th class="c">Tenant placement</th><th class="c">Full service</th></tr></thead><tbody>' + \
            "".join(f'<tr><td>{n}</td><td class="c">{"Included" if a else "&mdash;"}</td><td class="c">{"Included" if b else "&mdash;"}</td></tr>' for n, a, b in PROGRAMS) + \
            '</tbody></table></div><p>Tenant placement is a one-time leasing fee. Full service is a one-time set-up fee plus a monthly management fee. <a href="@/copy-of-contact-us/">See fees in the FAQ</a>.</p>'
    out.append(K.page(P("copy_of_landlords"), "Owner information", "Owner Information", "Leave your investment worries to the pros.", "Landlords",
                      "Owner Information &amp; Rental Analysis | Equity PM, Sandy UT",
                      "Rental owners: choose tenant placement or full-service management with Equity Property Management in Sandy, Utah, and request a free rental analysis.",
                      land, canonical=EXT["copy_of_landlords"]["canon"], form_side=True))
    out.append(K.page(P("copy_of_tenants"), "Application criteria", "Application Criteria", "For current and future tenants.", "Tenants",
                      "Rental Application Criteria | Equity Property Management",
                      "Equity Property Management rental application criteria: $65 fee, photo ID, employment, income of 3x rent, rental and credit history, co-applicants.",
                      render("copy_of_tenants", drop=("VIEW AVAILABLE RENTALS", "SUBMIT AN APPLICATION", "Log In")), canonical=EXT["copy_of_tenants"]["canon"]))
    out.append(K.page(P("join_equity_pm"), "Join Equity PM", "Interested in Joining EPM?", "Expand your real estate business.", "Agents", "Join Equity PM | Property Management for Real Estate Agents",
                      "Agents: sell real estate and manage properties under Equity Real Estate's broker-supported model, with systems, low brokerage fees and a referral program.",
                      render("join_equity_pm", drop=("Fill out the form", "First name", "Submit")), canonical=EXT["join_equity_pm"]["canon"], form_side=True))
    out.append(K.page(P("submit_a_referral"), "Submit a referral", "Submit a Referral", "Referrals welcome from all brokerages.", "Agents", "Submit a Property Management Referral | Equity PM, Sandy UT",
                      "Refer a property management client to Equity PM and receive a referral fee on successful signing and leasing, with a non-compete promise. All brokerages.",
                      render("submit_a_referral", drop=("Refer your client by completing", "Client's", "Your First", "Your Brokerage", "Your Email", "Submit", "Thanks for submitting")),
                      canonical=EXT["submit_a_referral"]["canon"], form_side=True))
    info = f'''<p class="answer">Questions about managing your rental, applying for a home, or joining Equity PM? Call, email or stop by the Sandy office.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18015454302">801-545-4302</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd><address>1218 E 7800 S Suite 150<br>Sandy, UT 84094</address></dd></div><div><dt>Hours</dt><dd>Monday &ndash; Friday, 9:00 AM &ndash; 5:00 PM MST</dd></div></dl>'''
    out.append(K.page(P("contact_us"), "Contact", "Contact Us", "Sandy office &middot; Monday to Friday, 9 to 5.", "Contact", "Contact Equity Property Management | Sandy, Utah Office",
                      "Contact Equity Real Estate Property Management in Sandy, Utah: call 801-545-4302, email info@equitypmusa.com, or visit 1218 E 7800 S Suite 150.",
                      info, canonical=EXT["contact_us"]["canon"], form_side=True))
    leftover = '<p class="answer">This page isn&rsquo;t in use. Looking for a rental, or for help managing one?</p>' + \
               f'<p><a class="tlink" href="@/copy-of-tenants/">Tenants: application criteria {ARROW}</a> &nbsp; <a class="tlink" href="@/copy-of-landlords/">Owners: rental analysis {ARROW}</a></p>'
    for k in EXT:
        if k.startswith("properties_") or k in ("groups", "current_agents"):
            out.append(K.page(P(k), "Equity PM", "Equity Property Management", "", "Equity PM", "Equity Real Estate Property Management | Sandy, Utah",
                              "This page is not in use. Equity Real Estate Property Management offers tenant placement and full-service rental management from Sandy, Utah.",
                              leftover, canonical=EXT[k]["canon"], robots="noindex, follow", sitemap=False))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Owners", "copy-of-landlords/"), ("Tenants", "copy-of-tenants/"), ("Contact", "contact-us/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-545-4302.",)) for x in out]
