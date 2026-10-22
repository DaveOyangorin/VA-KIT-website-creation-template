"""greenjanitorialservice.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 11 sitemap URLs plus the 6 blog posts linked from /bloghome (LeadConnector, no trailing slash).
From the site: Green Janitorial Services LLC ("GJS"); family-owned; founded 2018 by a family that moved from Mexico (Our Story);
commercial, residential and specialized cleaning; biodegradable, environmentally friendly products; weekly, bi-weekly or monthly home
maintenance; service areas list; hours Mon-Fri 7:00 AM-7:00 PM, Sat 7:00 AM-5:00 PM, Sun closed; +1 801-577-8703;
greenjanitorialservicesllc@gmail.com; careers details ($13 during 15-day training, $14 regular; transportation from a meeting point);
five client quotes (unnamed, as on the site); six blog posts by Claudia Hinojosa; terms of service.
NAP: Google listing 2685 S W Temple St Suite 6, South Salt Lake, UT 84115, +1801-577-8703 (used, copied exactly). The site writes
"2685 S West Temple Suite 6, South Salt Lake, Utah 84115" (same place).
Left out until confirmed: the 5-star rating and "BestProsInTown" badge; "COVID-19 Disinfection Services" renamed "disinfection with
electrostatic sprayers" in their own words; "over a decade of experience" vs founded 2018 (the story says they started in cleaning 11
years ago, so both can be true; kept as written).
Photos: their two GJS vans are the only photo of their own; the rest of the site is stock. Supporting photos are credited Wikimedia
Commons pictures of South Salt Lake and Salt Lake City."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "greenjanitorialservice.com"
U = "https://greenjanitorialservice.com/"
TRAIL = False
NAME = "Green Janitorial Services"
TODAY = "2026-10-22"
HOME_OG = "gj-vans"
THEME_COLOR = "#123d2c"
FONTS = "https://fonts.googleapis.com/css2?family=Jost:wght@500;600;700&family=Instrument+Sans:wght@400;500;600;700&family=DM+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "gj-logo"
CTA_PATH = "contact-5033/"
CTA_LABEL = "Get a quote"
CTA_TITLE = "A cleaner space, <em>greener products.</em>"
CTA_TEXT = "Call +1 801-577-8703, Monday to Friday 7 to 7 and Saturday 7 to 5, or send the form and the GJS team will get back to you."
SIDE_TITLE = "Commercial, residential and specialized cleaning."
PHONES = [("Call", "+1 801-577-8703", "+18015778703")]
EMAIL = "greenjanitorialservicesllc@gmail.com"
HOURS = "Mon&ndash;Fri 7:00 AM&ndash;7:00 PM &middot; Sat 7:00 AM&ndash;5:00 PM &middot; Sun closed"
ADDRESS = [("Office", "2685 S W Temple St Suite 6<br>South Salt Lake, UT 84115")]
AREAS = ["South Salt Lake", "Salt Lake City", "the Salt Lake Valley"]
SOCIAL = [("Facebook", "https://www.facebook.com/greenjanitoralservices"), ("Instagram", "https://www.instagram.com/greenjanitorialservicesllc/")]
BLURB = "Family-owned commercial, residential and specialized cleaning with biodegradable, environmentally friendly products, from South Salt Lake since 2018."
SVC_LABEL = "Services"
SVC = [("commercial/", "Commercial cleaning", None), ("residential/", "Residential cleaning", None), ("specialized/", "Specialized services", None)]
NAV = [("Our story", "ourstory/"), ("Careers", "join-our-team/"), ("Blog", "bloghome/"), ("Contact", "contact-5033/")]
CITIES = ["Cottonwood Heights", "Millcreek", "South Jordan", "Daybreak", "Murray", "South Salt Lake", "Draper", "North Salt Lake", "Sugar House", "Holladay", "Olympus Cove",
          "Taylorsville", "Kearns", "Oquirrh", "West Valley", "Magna", "Salt Lake City", "Bluffdale", "Midvale", "Sandy", "9th &amp; 9th"]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": "Green Janitorial Services Utah", "legalName": "Green Janitorial Services LLC", "url": U, "telephone": "+18015778703", "email": EMAIL,
         "logo": U + "assets/img/gj-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "2685 S W Temple St Suite 6", "addressLocality": "South Salt Lake", "addressRegion": "UT", "postalCode": "84115", "addressCountry": "US"}}
    if full:
        n.update({"description": "Family-owned janitorial, commercial, residential and specialized cleaning with biodegradable, environmentally friendly products, based in South Salt Lake, Utah.",
                  "foundingDate": "2018", "sameAs": [u for l, u in SOCIAL],
                  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:00", "closes": "19:00"},
                                                {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "07:00", "closes": "17:00"}],
                  "areaServed": [{"@type": "Place", "name": c.replace("&amp;", "&") + ", UT"} for c in CITIES]})
    return [n]
