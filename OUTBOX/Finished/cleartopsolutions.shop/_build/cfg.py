"""cleartopsolutions.shop: facts and settings (20 Oct 2026).
From the client's own site: ClearTop Solutions, water damage restoration, St. George, UT; (435) 288-1334 (tel:4352881334),
24/7 emergency line; info@cleartopsolutions.shop; "2505 S River Road, Ste 2" (contact page); licensed & insured (site text).
Google profile (report): +1435-220-4296 (a different number: flagged), 2505 S River Rd, St. George, UT 84790 (ZIP from Google),
no reviews found. Left out until confirmed: "98% Client Satisfaction", "100+ Projects Supported", the five-star row,
"certified professionals", "years of experience" (no evidence on the site or Google).
Photos: the site has one photo and it looks AI-generated, so it is not used. Services are drawn; atmosphere photos are openly
licensed (Openverse) and credited, never presented as the client's work. No tracking tag on the live site."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "cleartopsolutions.shop"
U = "https://cleartopsolutions.shop/"
TRAIL = True
NAME = "ClearTop Solutions"
TODAY = "2026-10-20"
HOME_OG = "summer-storm"
THEME_COLOR = "#0c1a2b"
FONTS = "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "ct-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Request an Assessment"
CTA_TITLE = "Water where it shouldn&rsquo;t be? Call now."
CTA_TEXT = "Our 24/7 emergency line is answered day and night. We assess on site, explain what&rsquo;s needed in plain language, and give an upfront estimate before work begins."
SIDE_TITLE = "24/7 emergency line. Upfront estimate before work begins."
PHONES = [("24/7 emergency line", "(435) 288-1334", "+14352881334")]
EMAIL = "info@cleartopsolutions.shop"
HOURS = "24/7 emergency line"
ADDRESS = [("Office", "2505 S River Road, Ste 2<br>St. George, UT 84790")]
AREAS = ["St. George", "Washington", "Santa Clara", "Ivins"]
SOCIAL = []
BLURB = "Water damage restoration in St. George, Washington, Santa Clara and Ivins: extraction, drying, mold, sewage and leak repair. Licensed &amp; insured. 24/7 emergency line."
SVC_LABEL = "Services"
SVC = [("services/water-extraction/", "Water extraction", None), ("services/emergency-water-removal/", "Emergency water removal", None),
       ("services/basement-flood-cleanup/", "Basement flood cleanup", None), ("services/ceiling-water-damage-repair/", "Ceiling water damage", None),
       ("services/kitchen-water-damage-repair/", "Kitchen water damage", None), ("services/toilet-overflow-cleanup/", "Toilet overflow cleanup", None),
       ("services/sewage-cleanup/", "Sewage cleanup", None), ("services/mold-remediation-after-water-damage/", "Mold remediation", None)]
NAV = [("All Services", "services/"), ("Areas", "st-george/"), ("About", "about/"), ("Contact", "contact/")]
ST = {"street": "2505 S River Road, Ste 2", "city": "St. George", "zip": "84790", "tel": "+14352881334", "phone": "(435) 288-1334"}


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": ST["tel"], "email": EMAIL,
         "logo": U + "assets/img/ct-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": ST["street"], "addressLocality": "St. George", "addressRegion": "UT", "postalCode": ST["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}]}
    if full:
        n.update({"description": "ClearTop Solutions provides water damage restoration in St. George, Utah: water extraction, drying and mitigation, flood and basement cleanup, sewage cleanup, leak and ceiling repair, and mold remediation, with a 24/7 emergency line.",
                  "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
