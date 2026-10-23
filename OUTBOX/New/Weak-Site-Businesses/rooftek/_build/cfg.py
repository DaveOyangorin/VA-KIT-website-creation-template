"""rooftek: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): RoofTek, 4080 S W Temple St, Millcreek, UT 84107, +18014712054, category Roofing contractor.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "rooftek.example"
U = "https://rooftek.example/"
TRAIL = True
NAME = "RoofTek"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#18191d"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;600;700&family=Space+Mono:wght@400;700&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "801-471-2054", "+18014712054")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Millcreek", "4080 S W Temple St<br>Millcreek, UT 84107")]
AREAS = ["Millcreek"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18014712054",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "4080 S W Temple St", "addressLocality": "Millcreek", "addressRegion": "UT", "postalCode": "84107", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "Millcreek, UT"}}
    return [n]
