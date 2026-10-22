"""utahoneroofing.com: facts and settings (18 Oct 2026).
Brand "Utah One Roofing" (site), legal name "One Roofing LLC" (Google profile and site footer). Phones, emails, address, hours and
counties copied from the client's contact page. The Google profile address is "5536 W Heathrow Cir"; the site says "5546 W
Heathrow Cir" (flagged). No analytics tag on the current site (reCAPTCHA only)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "utahoneroofing.com"
U = "https://utahoneroofing.com/"
TRAIL = True
NAME = "Utah One Roofing"
LEGAL = "One Roofing LLC"
TODAY = "2026-10-18"
HOME_OG = "drone-home-new-roof"
THEME_COLOR = "#121412"
FONTS = "https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@600;700;800&family=Saira:wght@400;500;600&family=Saira+Stencil+One&display=swap"
S = {"phone": "(801) 928-9570", "tel": "+18019289570", "phone2": "(385) 223-9811", "tel2": "+13852239811",
     "email": "info@utahoneroofing.com", "email2": "oneroofingut@gmail.com",
     "street": "5546 W Heathrow Cir", "city": "Salt Lake City", "st": "UT", "zip": "84118",
     "hours": [("Monday &ndash; Friday", "8:00 AM &ndash; 6:00 PM"), ("Saturday", "9:00 AM &ndash; 5:00 PM"), ("Sunday", "Closed")],
     "ig": "https://www.instagram.com/oneroofingut/", "fb": "https://www.facebook.com/profile.php?id=61572720007147"}
COUNTIES = ["Salt Lake", "Utah", "Davis", "Summit", "Tooele", "Weber", "Wasatch"]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "legalName": LEGAL, "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/one-roofing-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"},
                                       {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "17:00"}],
         "sameAs": [S["ig"], S["fb"]]}
    if full:
        n.update({"description": "Utah One Roofing (One Roofing LLC) is a veteran-owned roofing company in Salt Lake City: residential and commercial roofing, roof repair, insurance restoration and Velux skylight installation.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + " County, Utah"} for c in COUNTIES]})
    return [n]
