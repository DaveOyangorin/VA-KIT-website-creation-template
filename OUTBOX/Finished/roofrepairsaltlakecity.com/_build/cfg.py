"""roofrepairsaltlakecity.com: facts and settings (18 Oct 2026).
NAP: name from the Google profile and the site. Phone and address shown the way the client's own site shows them; the Google
profile differs (phone +1385-213-7368, address "1760 2100 S") and both are flagged in the notes. Hours and service area
copied from the site footer. Email from the contact page. No analytics tag on the current site."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "roofrepairsaltlakecity.com"
U = "https://www.roofrepairsaltlakecity.com/"
TRAIL = True
NAME = "Roof Repair Salt Lake City"
TODAY = "2026-10-18"
HOME_OG = "og-card"
THEME_COLOR = "#16161a"
FONTS = "https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@75..150,500..900&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap"
S = {"phone": "(385) 355-4849", "tel": "+13853554849", "email": "steveadambdc@gmail.com",
     "street": "1760 w 2100 s", "city": "Salt Lake City", "state": "Utah", "zip": "84119",
     "hours": "Monday &ndash; Sunday, 9:00AM &ndash; 5:00PM", "since": "2005"}
AREAS = ["Salt Lake City", "Draper", "Sandy", "Cottonwood Heights", "Murray", "Millcreek", "Park City", "South Jordan", "Taylorsville",
         "West Jordan", "Holladay", "Herriman", "Midvale", "Riverton", "West Valley City", "Alta", "Bluffdale", "Bountiful", "Lehi", "Alpine", "Highland"]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/og-card.webp", "image": U + "assets/img/og-card.webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": "UT", "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "09:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Roof Repair Salt Lake City is a roofing contractor in Salt Lake City, Utah, roofing since 2005: residential and commercial roof repair, replacement, flat roofs, TPO, metal, shingle, tile and wood roofing.",
                  "foundingDate": "2005", "areaServed": [{"@type": "City", "name": a} for a in AREAS[:12]]})
    return [n]
