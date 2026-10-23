"""conrad-s-roofing-construction: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Conrad's Roofing & Construction, 1650 Digital Dr, Lehi, UT 84043, +14353753396, category Roofing contractor.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "conrads-roofing-construction.example"
U = "https://conrads-roofing-construction.example/"
TRAIL = True
NAME = "Conrad's Roofing & Construction"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#142232"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Karla:wght@400;600;700&family=DM+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "435-375-3396", "+14353753396")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Lehi", "1650 Digital Dr<br>Lehi, UT 84043")]
AREAS = ["Lehi"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+14353753396",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "1650 Digital Dr", "addressLocality": "Lehi", "addressRegion": "UT", "postalCode": "84043", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "Lehi, UT"}}
    return [n]
