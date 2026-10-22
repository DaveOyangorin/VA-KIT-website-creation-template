"""triplejlandscaping.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 7 sitemap pages (Wix, no trailing slash): /, /about-us, /services, /projects, /get-a-quote,
/privacy-policy, /accessibility-statement. Same URLs on the www host, same canonicals.
From the site: Triple J Landscaping, LLC; 385-227-5475; triple.j.landscaping.llc88@gmail.com; 4558 West 3170 South, West Valley City, Utah
84120 (get-a-quote page); office hours Monday-Saturday 7AM-6PM; locally owned and operated; licensed and insured; free estimates; quality
guaranteed; serves homeowners and businesses throughout Salt Lake County; the full services list (design, zeroscape, xeriscape, new sod,
artificial grass, lawn service, mulching and beds, cleanups, tree trimming and removal, sprinkler installation and repair, pavers, flagstone,
retaining walls, fire pits, concrete, snow removal, junk removal) with their one-line descriptions; about-page copy (accountability,
communication). Google listing: +1385-227-5475, no address. The address is on their own site, so it is shown; flagged.
Left out until confirmed: "15+ years of experience", "500+ completed projects", the three short testimonials (no source), "best landscaping
company in the area", Google rating (5.0 from 241). Their privacy and accessibility pages name triplejlandscaping.net; flagged.
Photos: only the ones that are clearly their own phone photos of finished Utah jobs (pavers with the Wasatch behind, flagstone, sod,
xeriscape, concrete, a sprinkler manifold, a tree removal, their truck). The gallery's AI-looking renders and stock images are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "triplejlandscaping.com"
U = "https://www.triplejlandscaping.com/"
TRAIL = False
NAME = "Triple J Landscaping"
TODAY = "2026-10-22"
HOME_OG = "tj-hero"
THEME_COLOR = "#173226"
FONTS = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Outfit:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "tj-logo"
CTA_PATH = "get-a-quote/"
CTA_LABEL = "Free Quote"
CTA_TITLE = "Let&rsquo;s build the yard <em>you&rsquo;ll love.</em>"
CTA_TEXT = "Call 385-227-5475 or request a free estimate. Design, lawn care, irrigation, hardscaping and maintenance across Salt Lake County, Monday to Saturday."
SIDE_TITLE = "Free estimates. Licensed, insured, locally owned."
PHONES = [("Call", "385-227-5475", "+13852275475")]
EMAIL = "triple.j.landscaping.llc88@gmail.com"
HOURS = "Mon&ndash;Sat 7 am&ndash;6 pm"
ADDRESS = [("Office", "4558 West 3170 South<br>West Valley City, Utah 84120")]
AREAS = ["Salt Lake County"]
SOCIAL = []
BLURB = "Locally owned landscaping in Salt Lake County: design, lawn care, irrigation, hardscaping and seasonal service. Licensed and insured, free estimates."
SVC_LABEL = "Services"
SVC = [("services/#design", "Landscape design &amp; install", None), ("services/#lawn", "Lawn care &amp; maintenance", None), ("services/#irrigation", "Sprinklers &amp; irrigation", None),
       ("services/#hardscape", "Hardscaping", None), ("services/#seasonal", "Snow &amp; junk removal", None), ("projects/", "Projects", None)]
NAV = [("Projects", "projects/"), ("About", "about-us/"), ("Get a quote", "get-a-quote/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": "Triple J Landscaping, LLC", "url": U, "telephone": "+13852275475", "email": EMAIL,
         "logo": U + "assets/img/tj-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "4558 West 3170 South", "addressLocality": "West Valley City", "addressRegion": "UT", "postalCode": "84120", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "07:00", "closes": "18:00"}]}
    if full:
        n.update({"description": "Locally owned landscaping company in Salt Lake County: landscape design and installation, xeriscape, sod and artificial grass, lawn care, sprinkler installation and repair, pavers, flagstone, retaining walls and concrete.",
                  "areaServed": {"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}})
    return [n]
