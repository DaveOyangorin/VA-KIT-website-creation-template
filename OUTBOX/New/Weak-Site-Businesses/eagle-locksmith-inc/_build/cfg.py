"""eagle-locksmith-inc: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Eagle Locksmith inc, no address on the listing (service-area business), +13855577669, category Locksmith.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "eagle-locksmith.example"
U = "https://eagle-locksmith.example/"
TRAIL = True
NAME = "Eagle Locksmith inc"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#121a2a"
FONTS = "https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;600;700&family=Share+Tech+Mono&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "385-557-7669", "+13855577669")]
EMAIL = ""
HOURS = ""
ADDRESS = []
AREAS = ["Salt Lake City"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "Locksmith", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13855577669",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", 
         "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}}
    return [n]
