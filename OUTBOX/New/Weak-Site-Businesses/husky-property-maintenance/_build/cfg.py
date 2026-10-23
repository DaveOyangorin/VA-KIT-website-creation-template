"""husky-property-maintenance: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Husky Property Maintenance, 101 7200 S, Midvale, UT 84047, +18017425282, category Handyman.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "husky-property-maintenance.example"
U = "https://husky-property-maintenance.example/"
TRAIL = True
NAME = "Husky Property Maintenance"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#1a222e"
FONTS = "https://fonts.googleapis.com/css2?family=Rubik:wght@600;800&family=Mulish:wght@400;600;700&family=Spline+Sans+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "801-742-5282", "+18017425282")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Midvale", "101 7200 S<br>Midvale, UT 84047")]
AREAS = ["Midvale"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18017425282",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "101 7200 S", "addressLocality": "Midvale", "addressRegion": "UT", "postalCode": "84047", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "Midvale, UT"}}
    return [n]
