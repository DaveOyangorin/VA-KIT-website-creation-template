"""dsihvac.com: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: the live site didn't load on 21 Oct, so content comes from the Internet Archive's most recent captures of each page (Nov 2025 and
Jan 2026; a Wix site, no trailing slashes). Same URLs. The 2016-18 .php pages (index.php, about.php, services.php, contact.php,
clients.php) are years old and not rebuilt.
From the site (as "WWW.DSIHVAC.COM" / "DSI HVAC"): Draper's heating, ventilation and air conditioning installation company; established in
2015; serves Bluffdale, Draper, Riverton, South Jordan, Sandy, Herriman and Cottonwood Heights; services: maintenance, repair ("The Fixer
Upper"), new installations with "a 2 year labor warranty and 10 year parts warranties on all new A/C and furnace replacements"; why choose
us: free quotes, individualized recommendations, professional assistance, extended warranty; brands: Trane, Carrier, Mitsubishi (ductless
air conditioners and heat pumps), Rheem and all major brands; hours Mon-Fri 9am-6pm, Sat 10am-2pm, Sun closed; david@dsihvac.com.
Their own photos: mini-split and ductwork installs, a 2018 Trane "Rookie of the Year Award" presented to DSI HVAC (Trane / Larson), team photos.
NAP: Google listing Proformance Heating and Air, 13525 south Ensign Point Ln, Draper, UT 84020, +1385-226-7667 (used, copied exactly). The
site's phone is the same number (385-226-7667), but the site's name is DSI HVAC: FLAGGED, confirm the rebrand before anything goes live.
The DSI logo is not used; the header is a plain wordmark of the Google name.
Left out: the 5.0 / 191 rating. Banner: credited Wikimedia Commons photo of Draper homes in the Corner Canyon area."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "dsihvac.com"
U = "https://www.dsihvac.com/"
TRAIL = False
NAME = "Proformance Heating and Air"
TODAY = "2026-10-23"
HOME_OG = "pf-hero"
THEME_COLOR = "#161e28"
FONTS = "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "pf-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Get a free quote"
CTA_TITLE = "Too hot, too cold, <em>or just too old?</em>"
CTA_TEXT = "Call 385-226-7667 or email david@dsihvac.com for a free quote. Mon&ndash;Fri 9am&ndash;6pm, Sat 10am&ndash;2pm."
SIDE_TITLE = "Free quotes on heating and air."
PHONES = [("Call", "385-226-7667", "+13852267667")]
EMAIL = "david@dsihvac.com"
HOURS = "Mon&ndash;Fri 9&ndash;6, Sat 10&ndash;2"
ADDRESS = [("Draper", "13525 south Ensign Point Ln<br>Draper, UT 84020")]
AREAS = ["Draper", "Bluffdale", "Riverton", "South Jordan", "Sandy", "Herriman", "Cottonwood Heights"]
SOCIAL = []
BLURB = "Proformance Heating and Air: furnace and air conditioning maintenance, repair and new installations in Draper and the south Salt Lake Valley."
SVC_LABEL = "Services"
SVC = [("services/", "Maintenance", None), ("services/", "Repair", None), ("services/", "New installations", None), ("brands-we-service/", "Brands we service", None)]
NAV = [("Why choose us", "why-choose-us/"), ("About", "about-us/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "HVACBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13852267667", "email": EMAIL,
         "logo": U + "assets/img/pf-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "13525 south Ensign Point Ln", "addressLocality": "Draper", "addressRegion": "UT", "postalCode": "84020", "addressCountry": "US"}}
    if full:
        n.update({"description": "Draper, Utah heating and air conditioning company: maintenance, repair and new furnace and A/C installations, serving the south Salt Lake Valley since 2015.",
                  "foundingDate": "2015",
                  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"},
                                                {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "14:00"}],
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in AREAS]})
    return [n]
