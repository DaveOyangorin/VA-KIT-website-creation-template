"""stgeorgeconcreteleveling.com: facts and settings (20 Oct 2026).
From the client's own contact page: St. George Concrete Leveling, 169 W 2710 S Cir Suite 202-A, St. George, UT 84790; phone
435-466-5545 (tel:4354665545); service area St. George & Southern Utah; Monday to Friday 8:00 AM - 5:00 PM.
Report: no Google profile found; the reviewer notes the name and domain read like a lead-generation site (flagged; confirm who
owns it). Left out until confirmed (no profile to check them against): "Thousands of satisfied customers", "Local and family
owned", "15+ years in business", "certified", "Licensed under Utah's S260 classification", the warranty, and the customer
anecdotes written into the service and town pages (e.g. "a Bloomington Hills client had a 1.25-inch lip"). "Licensed and
insured" is kept as the client states it. No tracking tag found on the live site.
Photos: the live site's only photo is a stock foam-lifting composite (not used). Drawings throughout; one openly licensed
Snow Canyon landscape (pkinney62, CC BY 2.0) for atmosphere, credited."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "stgeorgeconcreteleveling.com"
U = "https://stgeorgeconcreteleveling.com/"
TRAIL = True
NAME = "St. George Concrete Leveling"
TODAY = "2026-10-20"
HOME_OG = "red-rock-st-george"
THEME_COLOR = "#20252b"
FONTS = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Figtree:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap"
TRACK_HEAD = ""
LOGO = "sgcl-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Free Quote"
CTA_TITLE = "Uneven slabs don&rsquo;t fix themselves. Get a free on-site estimate."
CTA_TEXT = "Call 435-466-5545, Monday to Friday, 8 a.m. to 5 p.m., or send the form. We inspect the slab, find the cause of settlement, and give you a written estimate."
SIDE_TITLE = "Free on-site estimate and a written proposal."
PHONES = [("Call", "435-466-5545", "+14354665545")]
EMAIL = ""
HOURS = "Mon&ndash;Fri 8:00 AM&ndash;5:00 PM"
ADDRESS = [("Office", "169 W 2710 S Cir Suite 202-A<br>St. George, UT 84790")]
AREAS = ["St. George", "Washington", "Santa Clara", "Hurricane", "Ivins", "La Verkin", "Toquerville", "Leeds", "Springdale", "Cedar City", "Kanab"]
SOCIAL = []
BLURB = "Concrete leveling and slab lifting with polyurethane foam in St. George and Southern Utah: driveways, sidewalks, patios, garage floors, pool decks and steps. Licensed &amp; insured."
SVC_LABEL = "Services"
SVC = [("polyurethane-foam-injection/", "Polyurethane foam injection", None), ("driveway-leveling/", "Driveway leveling", None), ("sidewalk-leveling/", "Sidewalk leveling", None),
       ("patio-leveling/", "Patio leveling", None), ("garage-floor-leveling/", "Garage floor leveling", None), ("pool-deck-leveling/", "Pool deck leveling", None),
       ("trip-hazard-removal/", "Trip hazard removal", None), ("mudjacking-services/", "Mudjacking", None)]
NAV = [("All services", "concrete-slab-lifting/"), ("Areas", "washington-county/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+14354665545",
         "logo": U + "assets/img/sgcl-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "169 W 2710 S Cir Suite 202-A", "addressLocality": "St. George", "addressRegion": "UT", "postalCode": "84790", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "St. George Concrete Leveling lifts and levels sunken concrete with polyurethane foam injection in St. George and Southern Utah: driveways, sidewalks, patios, garage floors, pool decks, steps and commercial slabs.",
                  "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
