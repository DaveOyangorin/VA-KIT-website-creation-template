"""foundationrepairogden.com: facts and settings (20 Oct 2026).
SOURCE: the live site sits behind a Cloudflare challenge that blocks every crawler, so pages are rebuilt from the Internet Archive:
the home page from its December 2024 capture, and the other 11 linked pages from their September 2020 captures (the 2024 home page
links to exactly the same pages). The report (5 Oct 2026) counts 23 pages, so some newer pages are missing (flagged).
"Check first" (report): no Google profile, and the domain is the keyword itself. The site runs on a lead-generation template (a
quote funnel on quotes.foundationrepairogden.com, an /opt-out page, review badges with vote counts). Angelo must confirm who the
real business is before any outreach.
From the site itself: name "Fortified Foundations"; phone (385) 213-2324; hours every day 07:00 am - 11:00 pm; no street address;
cities near Ogden: Roy, Hill AFB, Clearfield, Layton, Hooper, Syracuse, Eden, Kaysville.
Left out (unverifiable or template): "licensed, insured, and bonded" plus "structural and geotechnical engineers", "certified
experts", "latest equipment", the review badges and vote counts, the three initial-only testimonials, the $5,000-$15,000 price
range, "monthly special", and the "available 24/7" line (the hours shown are 7 am to 11 pm).
No tracking tag found. No photos of their own (the template images are stock): everything is drawn."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "foundationrepairogden.com"
U = "https://www.foundationrepairogden.com/"
TRAIL = False
NAME = "Fortified Foundations"
TODAY = "2026-10-20"
HOME_OG = "og-card"
THEME_COLOR = "#23201c"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500..900&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap"
TRACK_HEAD = ""
LOGO = "ff-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Cracks, heaving or a wet basement? Call for a free estimate."
CTA_TEXT = "Call (385) 213-2324, any day from 7 a.m. to 11 p.m., or send the form. An estimator looks at the foundation on site and gives you a price quote and a repair plan."
SIDE_TITLE = "An on-site evaluation, a quote and a repair plan."
PHONES = [("Call", "(385) 213-2324", "+13852132324")]
EMAIL = ""
HOURS = "Every day, 7:00 am&ndash;11:00 pm"
ADDRESS = []
AREAS = ["Ogden", "Roy", "Hill AFB", "Clearfield", "Layton", "Hooper", "Syracuse", "Eden", "Kaysville"]
SOCIAL = []
BLURB = "Foundation repair, concrete, basement waterproofing and foundation inspections in Ogden and nearby Weber and Davis County towns."
SVC_LABEL = "Services"
SVC = [("services/", "All services", None), ("foundation-repair-roy-weber-county/", "Foundation repair, Roy", None), ("layton-84040-concrete-company/", "Concrete, Layton", None),
       ("clearfield-foundation/", "Clearfield", None), ("foundation-kaysville-ut/", "Kaysville", None), ("foundation-experts-syracuse-utah/", "Syracuse", None)]
NAV = [("About", "about/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13852132324",
         "image": U + "assets/img/" + HOME_OG + ".webp",
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "07:00", "closes": "23:00"}]}
    if full:
        n.update({"description": "Fortified Foundations: foundation repair, concrete services, basement waterproofing and foundation inspections in Ogden, Utah and nearby towns.",
                  "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
