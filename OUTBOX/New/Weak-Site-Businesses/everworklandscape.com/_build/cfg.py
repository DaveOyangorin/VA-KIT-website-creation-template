"""everworklandscape.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 41 sitemap URLs (Next.js, no trailing slash; canonicals on the bare domain, the host redirects to www).
The live site was rebuilt after the 21 Oct audit (the report saw 18 pages, no meta descriptions and 17/17 images without alt text); this draft
works from the new live site. Same URLs, same canonicals.
From the site: Everwork Property Maintenance & Landscaping; family-owned and local; open 24 hours, 7 days; call or text (801) 875-8109;
jaredrayweeksjrw@gmail.com; 10 services; 27 cities in Salt Lake County and Utah County; startup timing "mid to late April"; blowouts "early
October through early November"; plows dispatched at the plan's trigger depth, "typically one to two inches"; seasonal snow contracts and
per-visit; same-day and next-day sprinkler repair in most of the area; five customer reviews (names as on the site).
NAP: Google listing 446 E Mountain View Dr, Sandy, UT 84070, +1801-875-8109 (used, copied exactly). The site gives the same street without ZIP.
Left out: "5.0 / 5-star rated on Google" (the Google listing shows 4.9 from 210 reviews on 15 Oct; flagged).
Photos: their own job photos from /images/work (lawns, night repairs, branded plow truck, before/afters). Not used: the service-card and
hero images under /images/*.png (illustration-like, sizes typical of generated images) and the 141 px thumbnails."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "everworklandscape.com"
U = "https://everworklandscape.com/"
TRAIL = False
NAME = "Everwork Property Maintenance & Landscaping"
TODAY = "2026-10-22"
HOME_OG = "ew-hero"
THEME_COLOR = "#12171b"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500;62..125,700;62..125,800;62..125,900&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap"
TRACK_HEAD = ""
LOGO = "ew-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Free quote"
CTA_TITLE = "Whatever the season, <em>we're already on it.</em>"
CTA_TEXT = "Call or text (801) 875-8109, day or night, or send the quote form. Family-owned, local, and open 24 hours, 7 days a week."
SIDE_TITLE = "Open 24/7. Call or text anytime."
PHONES = [("Call or text", "(801) 875-8109", "+18018758109")]
EMAIL = "jaredrayweeksjrw@gmail.com"
HOURS = "Open 24 hours, 7 days a week"
ADDRESS = [("Based in Sandy", "446 E Mountain View Dr<br>Sandy, UT 84070")]
AREAS = ["Sandy", "Salt Lake County", "Utah County"]
SOCIAL = []
BLURB = "Family-owned sprinkler repair, landscaping, lawn care, yard cleanup, commercial and HOA maintenance, and 24/7 snow removal, based in Sandy and serving Salt Lake and Utah County."
SVC_LABEL = "Services"
SVC = [("services/sprinkler-repair/", "Sprinkler repair", None), ("services/sprinkler-installation/", "Sprinkler installation", None), ("services/sprinkler-startup/", "Sprinkler startup", None),
       ("services/sprinkler-winterization/", "Sprinkler winterization", None), ("services/lawn-maintenance/", "Lawn maintenance", None), ("services/yard-cleanup/", "Yard cleanup", None),
       ("services/landscape-installation/", "Landscape installation", None), ("services/commercial-maintenance/", "Commercial maintenance", None),
       ("services/hoa-landscape-maintenance/", "HOA maintenance", None), ("services/snow-removal/", "Snow removal", None)]
NAV = [("Service areas", "service-areas/"), ("All services", "services/"), ("Contact", "contact/")]
CITIES = ["North Salt Lake", "Salt Lake City", "South Salt Lake", "Millcreek", "Holladay", "Murray", "Cottonwood Heights", "Midvale", "Taylorsville", "West Valley City", "Magna", "Kearns",
          "West Jordan", "South Jordan", "Sandy", "Draper", "Riverton", "Herriman", "Bluffdale", "Lehi", "Saratoga Springs", "Eagle Mountain", "American Fork", "Pleasant Grove", "Orem", "Vineyard", "Provo"]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18018758109", "email": EMAIL,
         "logo": U + "assets/img/ew-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "446 E Mountain View Dr", "addressLocality": "Sandy", "addressRegion": "UT", "postalCode": "84070", "addressCountry": "US"}}
    if full:
        n.update({"description": "Family-owned landscaping, sprinkler repair and installation, lawn maintenance, yard cleanup, commercial and HOA grounds care, and 24/7 snow removal in Sandy and across Salt Lake and Utah County.",
                  "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"},
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in CITIES]})
    return [n]
