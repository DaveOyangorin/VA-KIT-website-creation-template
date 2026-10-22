"""rasmussenlandscapes.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 94 sitemap pages (21 Oct 2026), same URLs (no trailing slash, mixed case kept: /Services, /Contact,
/DesignBuild, /Projects, /aerate6eed311a ...) and canonicals.
From the site: phone (801) 466-0303, rllinfo@rasmussenlandscapes.com, address shown as "3446 S West Temple, Salt Lake City, UT 84115".
Google listing (report), copied exactly: Rasmussen Landscapes, 3446 S W Temple St, South Salt Lake, UT 84115, +1801-466-0303, 4.5 stars
from 629 reviews. The report's home target is "landscaping south salt lake", so the Google NAP is shown (city differs from the site:
flagged). Quotes over the phone using satellite imaging; free consultations; service-area city pages as on the site.
Left out until confirmed: "Utah's premier/premiere", "best in the business", "after 50 years / for more than 50 years" (the History
page keeps the owner's own story as written). Google rating not shown.
Tracking kept as on the live site: Universal Analytics UA-162917173-1 (note: Universal Analytics stopped collecting in 2023; flagged).
Photos: only their own (the P10... camera series of their jobs, the Barrett rock steps, crew photos in Rasmussen shirts). Stock files
(spreader, snowblower, gloves, sprayers, leaves, snow, tea and website mockups left from the template) are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "rasmussenlandscapes.com"
U = "https://www.rasmussenlandscapes.com/"
TRAIL = False
NAME = "Rasmussen Landscapes"
TODAY = "2026-10-21"
HOME_OG = "ras-rock-steps"
THEME_COLOR = "#1d3328"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=Work+Sans:wght@400;500;600;700&family=Azeret+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google Analytics (as on the live site) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-162917173-1"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','UA-162917173-1');</script>"""
LOGO = "ras-logo"
CTA_PATH = "Contact/"
CTA_LABEL = "Get a Quote"
CTA_TITLE = "Your yard. Our work."
CTA_TEXT = "Call (801) 466-0303 for a quote over the phone: one call gets you a price, answers, and your service on the schedule. Or send us a note and we&rsquo;ll set up a free consultation."
SIDE_TITLE = "Quotes over the phone, or a free consultation."
PHONES = [("Call", "(801) 466-0303", "+18014660303")]
EMAIL = "rllinfo@rasmussenlandscapes.com"
HOURS = ""
STREET, CITY, ZIP = "3446 S W Temple St", "South Salt Lake", "84115"
ADDRESS = [("Office", "3446 S W Temple St<br>South Salt Lake, UT 84115")]
AREAS = ["South Salt Lake", "Salt Lake City", "the Avenues", "Millcreek", "Holladay", "Sandy", "Draper", "West Jordan", "Herriman", "Bountiful", "Layton", "Syracuse",
         "Ogden", "Tooele", "Park City", "Alpine", "Highland", "Orem", "Provo"]
SOCIAL = []
BLURB = "Landscape design, building and yard maintenance from South Salt Lake: sprinklers, sod, rock walls, patios, mowing, fertilizing, aeration, cleanups and snow removal."
SVC_LABEL = "Services"
SVC = [("DesignBuild/", "Design &amp; Build", None), ("Services/", "Maintenance", None), ("other-services/", "Other services", None), ("sprinklers/", "Sprinklers", None),
       ("mow/", "Mowing", None), ("fertilize/", "Fertilizing", None), ("aerate6eed311a/", "Aeration", None), ("snow-removal/", "Snow removal", None)]
NAV = [("Portfolio", "portfolio/"), ("About", "about-us/"), ("Service areas", "serivce-areas/"), ("Contact", "Contact/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18014660303", "email": EMAIL,
         "logo": U + "assets/img/ras-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY, "addressRegion": "UT", "postalCode": ZIP, "addressCountry": "US"}}
    if full:
        n.update({"description": "Rasmussen Landscapes designs, builds and maintains residential and commercial landscapes across the Salt Lake Valley and beyond: sprinklers, sod, rock walls, patios, water features, mowing, fertilizing, aeration, cleanups and snow removal.",
                  "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS if a != "the Avenues"]})
    return [n]
