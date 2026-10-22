"""emetplumbingservices.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 14 sitemap URLs (Squarespace, no trailing slash; the home page also answers at /home).
From the site: Emet Plumbing Heating & Air, formerly DrainBuster; family-owned and operated; est. 2018 (the about meta says "over 8 years");
residential and commercial plumbing and HVAC; main waterline and sewer line repair; 24/7 emergency response ("extra costs may apply");
$59.99 diagnostic applied toward the repair, "if we can't fix your issue, you don't pay"; (801) 433-7354 call/text; emet@emetplumbingservices.com;
four membership plans with their published prices and rates (memberships page); five blog posts by Bj Zelch; employment page.
NAP: Google listing 5941 S Redwood Rd, Taylorsville, UT 84123, +1801-433-7354 (used, copied exactly). The site lists 50 Broadway Ste. 300,
Salt Lake City, UT 84101 (flagged).
Left out until confirmed: "A+ BBB Accredited" badge, "Google Guaranteed" badge, the HVAC page's unsourced statistics (30%, 90%, 5-10 years),
anonymous "Local Home Owner" quotes, the clients page's logo collage (an illustration of retailer logos).
Fee conflict: $59.99 diagnostic (about page) vs "Voided Service Call Fee (normally $59.00)" (memberships page); the plan calculator uses the
memberships page's own figures. Photos: their own fleet, crew and install photos only (stock, AI illustrations and badges not used)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "emetplumbingservices.com"
U = "https://emetplumbingservices.com/"
TRAIL = False
NAME = "Emet Plumbing Heating & Air"
TODAY = "2026-10-22"
HOME_OG = "em-fleet"
THEME_COLOR = "#0a1630"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&family=Spline+Sans+Mono:wght@500;600&display=swap"
TRACK_HEAD = ""
LOGO = "em-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Book service"
CTA_TITLE = "Honest pricing. <em>Fast service.</em>"
CTA_TEXT = "Call or text (801) 433-7354. Our $59.99 diagnostic goes toward your repair, and if we can't fix it, you don't pay."
SIDE_TITLE = "Same-day plumbing &amp; HVAC. Call or text."
PHONES = [("Call or text", "(801) 433-7354", "+18014337354")]
EMAIL = "emet@emetplumbingservices.com"
HOURS = "24/7 emergency response (extra costs may apply)"
ADDRESS = [("Taylorsville", "5941 S Redwood Rd<br>Taylorsville, UT 84123")]
AREAS = ["Taylorsville", "Salt Lake City", "the Salt Lake Valley"]
SOCIAL = [("Facebook", "https://www.facebook.com/people/Emet-Plumbing/61558431725858/"), ("Instagram", "https://www.instagram.com/emetplumbing/")]
BLURB = "Family-owned plumbing, heating and air for homes and businesses in Taylorsville and the Salt Lake Valley. Formerly DrainBuster, est. 2018."
SVC_LABEL = "Services"
SVC = [("#plumbing", "Plumbing &amp; drains", None), ("#plumbing", "Sewer &amp; main waterline", None), ("hvac/", "Heating &amp; air (HVAC)", None), ("memberships/", "Membership plans", None)]
NAV = [("Memberships", "memberships/"), ("About", "about/"), ("Blog", "ourblog/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18014337354", "email": EMAIL,
         "logo": U + "assets/img/em-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "5941 S Redwood Rd", "addressLocality": "Taylorsville", "addressRegion": "UT", "postalCode": "84123", "addressCountry": "US"}}
    if full:
        n.update({"description": "Family-owned plumbing, drain, sewer and main waterline, water heater and HVAC service for homes and businesses in Taylorsville and the Salt Lake Valley. Formerly DrainBuster.",
                  "foundingDate": "2018", "sameAs": [u for l, u in SOCIAL], "areaServed": {"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}})
    return [n]
