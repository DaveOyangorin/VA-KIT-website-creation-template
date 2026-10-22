"""Pages for the acs-hoa.com redesign: "The board's desk".

An HOA runs on requests: a broken sprinkler in the common area, a fence that breaks the CC&Rs, a water shutoff owners must hear about.
ACS's best idea is its "Community Action Items" forum, where homeowners report issues and the board and manager track them. So the
signature is that board made tangible: pick a request and watch it move across Reported, On the board's list, Manager on it and Closed,
with the ACS service that handles each step (all from their own service lists). Plum-navy from their logo, a confident geometric sans,
and the calm order of a well-run board meeting.
References (screenshotted 21 Oct 2026): Linear (issue tracking as calm design), Notion (structured, friendly docs), Basecamp
(plain-spoken project management for groups).
Same URLs (static .html pages) with self-canonicals; no stock photos."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL, AREAS, OFFICES
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
cta = K.cta
header = K.header


def footer():
    return re.sub(r'<span class="flogo"><img[^>]*></span>', '<span class="flogo">' + img("acs-white-logo", "Advanced Community Services logo") + '</span>', K.footer())


MGMT = ["Supervise on-site maintenance crews", "Collect association monthly dues", "Address violations of association rules and regulations",
        "Multiple ways to pay: paper bills, credit card processing and bill pay", "Monthly association reports", "Available 24 hours a day, 7 days a week for emergencies",
        "Custom quotes for lawn care, snow removal, sprinkler maintenance and other property maintenance", "Consultant during board and membership meetings",
        "Help developing rules, regulations, policies and procedures", "Agendas for board and membership meetings", "Bi-weekly inspections, or as determined by the board",
        "Collect homeowner information and requests"]
ONLINE = ["An interactive website developed for each association", "Board member list and board meeting minutes", "Easy access to the association&rsquo;s monthly records",
          "Distribute and store important association documents", "Board access to financial records and meeting follow-ups", "Association emails and mailings",
          "A monthly community newsletter", "Homeowner access to CC&amp;Rs and bylaws", "A homeowner recommendation and complaint database", "Online ownership records and a map of the development",
          "Online payment of dues", "Automated welcome packets for new owners and move-ins", "Friendly late-fee notices for monthly dues"]
PRO = ["Process architectural compliance forms", "Coordinate corporate reports and IRS filings", "Resale and refinancing documents for lenders and title companies",
       "Transparency and accountability for all community financials", "Manage insurance claims", "Review rules, regulations and CC&amp;Rs for recommended amendments",
       "Education and legal training for the board and committees", "Coordinate legal services at a discounted rate", "Separate bank accounts for each community",
       "Reserve analysis to plan for maintenance and growth"]
TICKETS = [("sprinkler", "Sprinklers are broken in the common area", ["A homeowner posts it in Community Action Items.", "The board sees it on the action list between meetings.", "Your Community Manager gets custom quotes for sprinkler maintenance and supervises the crew.", "Closed, and noted in the monthly report to the board."]),
           ("fence", "A new fence doesn&rsquo;t follow the CC&amp;Rs", ["A neighbor reports it through the private forum.", "The board reviews it against the governing documents.", "ACS addresses the violation and processes the architectural compliance form.", "Resolved and on record."]),
           ("water", "The water will be shut off tomorrow", ["The utility notice comes in to ACS.", "The board is told right away.", "A broadcast goes to every owner about the shutoff.", "Owners knew in time. Closed."]),
           ("sale", "An owner is selling their unit", ["The owner or their agent asks for documents.", "Routine. No board vote needed.", "ACS provides resale and refinancing documents to the lender and title company.", "Closed. A welcome packet is automated for the new owner."]),
           ("dues", "Dues are past due", ["The account shows unpaid dues.", "The board sees it in the monthly financial report.", "A friendly late-fee notice goes out; if needed, ACS coordinates legal services at a discounted rate.", "Paid, or handed to the board&rsquo;s attorney."]),
           ("reserve", "The roof will need replacing in a few years", ["A board member raises long-term repairs.", "It goes on the next board meeting agenda.", "ACS starts with a reserve analysis that makes clear what needs to be planned for now.", "A plan the board can fund. Closed."])]
STAGES = ["Reported", "On the board&rsquo;s list", "Manager on it", "Closed"]
QUOTES = [("Countryside Square Condominiums", "We were previously self-managed and hiring ACS has done wonders for our community. They have helped us through redoing our rules and making sure we are up-to-date on new rules and laws that affect HOAs. They have also helped us with negotiating vendor contracts to ensure we are getting the best deals. In fact, they noticed a discrepancy in our Comcast billing right away and not only did they get our monthly bulk bill reduced by $300 per month, but they also got the HOA a refund of over $13,000.00 by reviewing our initial contract. The refund alone will pay for their management fees for the next 2 years! These are just a couple highlights of many benefits we receive from ACS. I strongly recommend their services for any community."),
          ("Silverlake Master HOA", "After changing management companies to ACS our HOA has seen a dramatic increase in service while saving the HOA tens of thousands of dollars. We went from barely having funds to pay the HOA bills to having a healthy reserve all without changing our dues. Their website provides a great communication tool for our homeowners to report issues and provides an easy way to keep track of all of the tasks they are accomplishing for us. The website keeps all of the HOA information in one spot which makes it easy for board members to keep track of everything that is going on in the community at a quick glance. With their patented communication tools we are confident that ACS will take care of every homeowner as they interact with the HOA regarding their largest investment."),
          ("Jeremy Ranch Owners Association", "ACS was there for us when our in house manager of 13 years quit without notice. Our Board was new and over whelmed. ACS helped us to put our HOA back on track. It&rsquo;s been 10 months since we hired ACS and our HOA has accomplished so much with Jeremy Johnson&rsquo;s help and guidance."),
          ("Condominiums At Camelot Owners Association", "Our board has been very pleased with the management of our community by ACS. They are responsive to our needs and our finances have improved substantially since we hired them. For example, after reviewing our trash removal contract, they were able to negotiate our monthly bill down to almost half of the previous total. They provide training to board members on our duties and responsibilities and explain the new laws and how they affect us. Managing our property is more than just a job for ACS. They definitely go above and beyond the regular expectation of a property management company. They genuinely care about the well-being of our community, just as they would treat their own property, and we truly get an advanced service. We highly recommend their services.")]
MISSION = "Our mission is to be the trusted partner every HOA deserves; driven by innovation and integrity, we communicate clearly, manage finances with expertise and transparency, complete projects in a timely manner, and serve as a strong, reliable industry expert wholly committed to increasing the value of every community we serve."
FAQ = [("What does a Community Manager do?", "<p>Your Community Manager helps the board, and every member, handle the HOA&rsquo;s day-to-day needs: paying bills, working with vendors, beautifying the property and keeping the community in compliance with its governing documents.</p>"),
       ("How do board members see the finances?", "<p>ACS prepares a transparent monthly report that is presented at each board meeting. Reports are customizable and always available to board members, and each community has its own separate bank account.</p>"),
       ("What do homeowners get online?", "<p>Each association gets its own website. Homeowners can pay dues, read the CC&amp;Rs and bylaws, review meeting minutes and send ideas or complaints. Board members get a second level of access to financial records, action items and meeting follow-ups.</p>"),
       ("What happens in an emergency?", "<p>An HOA is a 24/7/365 operation. ACS and your Community Manager are available at any time of day for emergencies, and ACS contact information is printed on every newsletter, mailing and website.</p>"),
       ("Where do you manage communities?", "<p>ACS serves all of Utah, plus Washington, Idaho and Arizona, from its corporate office in Lehi.</p>")]


def tracker():
    tabs = "".join(f'<button type="button" class="tk{" on" if i == 0 else ""}" data-t="{k}" aria-pressed="{"true" if i == 0 else "false"}">{t}</button>' for i, (k, t, s) in enumerate(TICKETS))
    cols = "".join(f'<div class="col" data-col="{j}"><p class="col-h"><span>{j + 1:02d}</span>{st}</p><div class="slot" data-slot="{j}"></div></div>' for j, st in enumerate(STAGES))
    data = "".join(f'<template data-tpl="{k}">' + "".join(f"<p>{x}</p>" for x in steps) + "</template>" for k, t, steps in TICKETS)
    return f'''<div class="board" data-board><div class="tk-list" role="group" aria-label="Pick a request">{tabs}</div>
<div class="cols">{cols}<div class="card-tk" data-card aria-live="polite"><span class="ct-k">Action item</span><b data-card-t></b><p data-card-step></p><span class="ct-who" data-card-stage></span></div></div>{data}</div>'''


def home():
    body = f'''
<section class="h-hero"><div class="hh-img" data-parallax="0.08">{img("acs-daybreak", "A lakeside planned community in Utah below the Wasatch Mountains", priority=True)}</div><div class="wrap h-hero-in">
<div><p class="label">HOA management &middot; Lehi, Utah &middot; UT, WA, ID, AZ</p>
<h1>HOA management in Lehi <span>that keeps the board in charge.</span></h1>
<p class="lede">Advanced Community Services manages homeowners associations and condominium communities: a Community Manager for your day-to-day needs, transparent monthly reporting at every board meeting, and an online portal for your board and homeowners.</p>
<div class="btn-row"><a class="btn accent" href="@/request-a-quote.html">Request a bid {ARROW}</a><a class="btn ghost" href="tel:+18778444227">{PHONE} 1-877-844-4227</a></div></div>
<div class="h-agenda reveal"><p class="label">Tonight&rsquo;s board meeting</p><ol>
<li><span>7:00</span><b>Monthly financial report</b><small>Prepared by ACS, presented to the board</small></li>
<li><span>7:15</span><b>Open action items</b><small>From the homeowner forum</small></li>
<li><span>7:30</span><b>Inspections &amp; vendors</b><small>Bi-weekly inspection notes, maintenance quotes</small></li>
<li><span>7:45</span><b>Reserve planning</b><small>What needs funding now</small></li></ol></div>
</div><p class="credit">Atmosphere photo: Daybreak, South Jordan, Utah &middot; Dean Derhak, CC BY-SA 3.0, via Wikimedia Commons</p></section>

<section class="sec h-board" id="action-items"><div class="wrap">
<div class="h-head reveal"><p class="label">Community Action Items</p><h2>Every request, <span>from reported to closed.</span></h2><p class="lede">Homeowners report issues in a private forum. The board oversees them. Your Community Manager works them, and nothing falls through the cracks between meetings. Pick a request and follow it.</p></div>
{tracker()}
</div></section>

<section class="sec h-three"><div class="wrap">
<div class="h-head split-h reveal"><div><p class="label">What we do</p><h2>Three kinds of help <span>for your HOA.</span></h2></div><figure class="h-photo">{img("acs-street", "A tree-lined street of homes in a Utah community")}<figcaption>Atmosphere photo: Skykingcarter, CC BY-SA 4.0, via Wikimedia Commons</figcaption></figure></div>
<div class="three">
<a class="t3 reveal" href="@/management-services.html"><span class="t-n">01</span><h3>Management services</h3><p>A Community Manager, dues collection, rule enforcement, maintenance crews and 24/7 emergency availability.</p><ul>{"".join(f"<li>{x}</li>" for x in MGMT[:5])}</ul><em>All management services {ARROW}</em></a>
<a class="t3 reveal" href="@/online-services.html"><span class="t-n">02</span><h3>Online services</h3><p>A full-service website for every association, with separate access for board members and homeowners.</p><ul>{"".join(f"<li>{x}</li>" for x in ONLINE[:5])}</ul><em>All online services {ARROW}</em></a>
<a class="t3 reveal" href="@/professional-services.html"><span class="t-n">03</span><h3>Professional services</h3><p>Reserve analysis, transparent financials, compliance, insurance claims and legal coordination.</p><ul>{"".join(f"<li>{x}</li>" for x in PRO[:5])}</ul><em>All professional services {ARROW}</em></a>
</div></div></section>

<section class="sec h-mission"><div class="wrap"><blockquote class="reveal"><p class="label">Our mission</p><p>{MISSION}</p></blockquote></div></section>

<section class="sec h-quotes"><div class="wrap">
<div class="h-head split-h reveal"><div><p class="label">What boards say</p><h2>From the communities <span>we manage.</span></h2></div><a class="tlink" href="@/testimonials.html">All testimonials {ARROW}</a></div>
<div class="hq">{"".join(f'<blockquote class="reveal"><p>{q}</p><footer>{n}</footer></blockquote>' for n, q in QUOTES[2:] + QUOTES[:1])}</div>
</div></section>

<section class="sec h-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>For board members.</h2>{faq_html(FAQ)}</div>
<div class="reveal"><div class="h-where"><p class="label">Where we work</p><ul class="states">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul>
<p class="label" style="margin-top:20px">Offices listed on our site</p><p>{" &middot; ".join(OFFICES)}</p><p class="small">Corporate: 2940 W Maple Loop Dr #102, Lehi, UT 84043</p></div>
<a class="post-card h-post" href="@/{p_blog.SLUG}"><span class="label">For boards</span><b>{p_blog.H1}</b><p>Sprinkler blowouts, snow contracts, shutoff notices and frozen pipes: a checklist for your HOA before the first freeze.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "HOA Management Lehi, UT | Advanced Community Services (ACS)",
            "meta": "Advanced Community Services: HOA management in Lehi and across Utah, Washington, Idaho and Arizona. Community Managers, monthly reports, online portals.",
            "body": body, "body_class": "is-home", "og": "acs-logo", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def svc_page(p, lab, h1, lede, intro, items, title, meta, extra=""):
    body = f'<p class="answer">{intro}</p><h2>Here are a few of our services</h2><ul class="ticks">{"".join(f"<li>{x}</li>" for x in items)}</ul>{extra}'
    return K.page(p, lab, h1, lede, "Services", title, meta, body, canonical=canon(p), schema=K.svc_schema(p, html.unescape(lab), "Utah"))


def make_pages():
    out = [home()]
    out.append(svc_page("management-services.html", "Management services", "HOA Management Services", "Increasing the value of your community.",
                        "ACS&rsquo;s main priority in managing your HOA is to help increase the value of your community. A key asset is the Community Manager assigned to your HOA, who helps board members, and all members, handle day-to-day needs: paying bills, working with vendors, beautifying the property and maintaining compliance with governing documents.",
                        MGMT, "HOA Management Services | Advanced Community Services, Utah",
                        "ACS HOA management services: a Community Manager, dues collection, rule enforcement, maintenance crews, monthly reports and 24/7 emergency availability.",
                        "<h2>A 24/7/365 operation</h2><p>An HOA never closes, and neither do emergencies. ACS and your Community Manager are available at any time of day, and ACS contact information is published on every newsletter, mailing and website, so it&rsquo;s easy to find when it matters.</p><h2>Harmony matters</h2><p>Our Community Managers work to build a social structure that involves everyone, dealing with misunderstandings before they cause strife in an otherwise well-run community. An enjoyable, sociable community does wonders for the value of your property.</p>"))
    out.append(svc_page("online-services.html", "Online services", "Online Services for HOA Boards", "Supporting managers and boards with online functionality.",
                        "Board members and homeowners both have ongoing questions and needs. ACS gives every client a full-service website as another line of communication, with two levels of access: board members get transparent access to financial records, activity follow-ups, meeting agendas and membership records; homeowners can pay dues, view the CC&amp;Rs, review meeting minutes and suggest new ideas.",
                        ONLINE, "Online HOA Portal &amp; Services | Advanced Community Services",
                        "Every ACS association gets its own website: online dues, CC&amp;Rs and minutes for homeowners, financial records and action items for board members.",
                        "<h2>Action items between meetings</h2><p>ACS also provides an online structure that organizes board members&rsquo; duties. It records action items, schedules reminders on urgent tasks and keeps property managers in sync with board members.</p>"))
    out.append(svc_page("professional-services.html", "Professional services", "Professional HOA Services", "Exceptional professional services.",
                        "With all the demands placed on HOA boards, the obstacles can be overwhelming. ACS professionals put proven, flexible systems in place. We begin with a Reserve Analysis that makes clear the maintenance and growth issues that need planning now, and a transparent monthly reporting cycle that is presented to the board at each meeting.",
                        PRO, "Professional HOA Services &amp; Reserve Analysis | ACS, Utah",
                        "ACS professional services for HOAs: reserve analysis, transparent financials, compliance forms, IRS filings, resale documents and legal coordination.",
                        "<h2>Collections, covenants and legal issues</h2><p>The most expensive and troubling challenges an HOA can face are collection matters, covenant violations and other legal issues. ACS has relationships with HOA attorneys that let us coordinate experienced legal services at better rates, and an in-house attorney who researches HOA issues affecting our communities.</p>"))
    about = f'''<p class="answer">Advanced Community Services (ACS) was created because of a recognized need in the property management industry for more professional and efficient service. ACS is founded on basic managerial principles that are often lost within associations.</p>
<h2>Our mission</h2><blockquote class="pull">{MISSION}</blockquote>
<h2>What makes us different</h2><p>Five key elements keep our focus on the communities we work with: communication, transparency, enforcement, training and accounting.</p>
<ul class="ticks"><li><b>Communication.</b> Community calendars and newsletters kept up to date, and phone lines open.</li><li><b>Transparency.</b> Monthly financial reports presented at every board meeting.</li><li><b>Enforcement.</b> Consistent handling of rule and CC&amp;R violations.</li><li><b>Training.</b> Education and legal training for boards and committees.</li><li><b>Accounting.</b> Separate bank accounts for each community, and dues collection with easy payment options.</li></ul>
<h2>Philosophy</h2><p>The main idea of our philosophy is to give accurate, good information and direction to the Board of Directors and association members. After all, communication is the key to satisfied homeowners.</p>
<h2>Why use ACS?</h2><p>A third party can help resolve problems. Why take a do-it-yourself approach to non-payment problems when a trained staff of professionals can handle them for you?</p>
<h2>Easy to do business with</h2><p>We take the time to understand the community we serve. We build relationships, and that is what makes doing business together easy.</p>'''
    out.append(K.page("about.html", "About", "About Advanced Community Services", "Professional, efficient HOA management.", "About", "About Advanced Community Services | HOA Management, Lehi",
                      "About Advanced Community Services: our mission, the five elements that set us apart, and our philosophy of clear communication for HOA boards and owners.",
                      about, canonical=canon("about.html")))
    tq = "".join(f'<blockquote class="tq"><p>{q}</p><footer>{n}</footer></blockquote>' for n, q in QUOTES)
    out.append(K.page("testimonials.html", "Testimonials", "Testimonials", "From the HOA boards we work with.", "Testimonials", "HOA Management Testimonials | Advanced Community Services",
                      "What HOA boards say about Advanced Community Services: Countryside Square, Silverlake Master HOA, Jeremy Ranch and Condominiums at Camelot. Utah HOA management.",
                      '<p class="answer">In their own words, from four communities ACS manages.</p>' + tq, canonical=canon("testimonials.html")))
    areas = f'''<p class="answer">To better serve each community, we want to be right in your neighborhood. ACS serves all of Utah, plus Washington, Idaho and Arizona.</p>
<h2>States we serve</h2><ul class="states">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul>
<h2>Offices</h2><p>Our site lists offices in {", ".join(OFFICES[:-1])} and {OFFICES[-1]}, with continued expansion planned.</p>
<dl class="info"><div><dt>Corporate</dt><dd><address>2940 W Maple Loop Dr #102<br>Lehi, UT 84043</address></dd></div><div><dt>Toll-free</dt><dd><a href="tel:+18778444227">1-877-844-4227</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div></dl>'''
    out.append(K.page("service-areas.html", "Service areas", "Service Areas", "Utah, Washington, Idaho and Arizona.", "Service areas", "HOA Management Service Areas | ACS: Utah, WA, ID &amp; AZ",
                      "Advanced Community Services manages HOAs across Utah, Washington, Idaho and Arizona, with offices in Clearfield, Lehi, Eagle Mountain, St. George and Park City.",
                      areas, canonical=canon("service-areas.html")))
    rq = f'''<p class="answer">Tell us about your community and we&rsquo;ll prepare a bid. Prefer to talk? Call <a href="tel:+18778444227">1-877-844-4227</a> or email <a href="mailto:sales@acs-hoa.com">sales@acs-hoa.com</a>.</p>
<dl class="info"><div><dt>Corporate</dt><dd><address>2940 W Maple Loop Dr #102<br>Lehi, UT 84043</address></dd></div><div><dt>Toll-free</dt><dd><a href="tel:+18778444227">1-877-844-4227</a></dd></div><div><dt>Lehi office</dt><dd><a href="tel:+18016411844">801-641-1844</a></dd></div></dl>'''
    out.append(K.page("request-a-quote.html", "Request a bid", "Request a Bid", "For HOA boards and self-managed associations.", "Request a bid", "Request an HOA Management Bid | Advanced Community Services",
                      "Request an HOA management bid from Advanced Community Services in Lehi, Utah. Call 1-877-844-4227 or send your community's details for a custom proposal.",
                      rq, canonical=canon("request-a-quote.html"), form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Management services", "management-services.html"), ("Request a bid", "request-a-quote.html"))))
    return [dict(x, body=Q(x["body"])) for x in out]
