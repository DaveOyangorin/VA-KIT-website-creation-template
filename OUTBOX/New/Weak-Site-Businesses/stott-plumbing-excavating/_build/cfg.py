"""stott-plumbing-excavating: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Stott Plumbing & Excavating, 165 Gregson Ave S, Salt Lake City, UT 84115, +18014672432, category Plumber &amp; excavating.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "stott-plumbing-excavating.example"
U = "https://stott-plumbing-excavating.example/"
TRAIL = True
NAME = "Stott Plumbing & Excavating"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#1e1c18"
FONTS = "https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&family=Work+Sans:wght@400;600;700&family=Roboto+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "801-467-2432", "+18014672432")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Salt Lake City", "165 Gregson Ave S<br>Salt Lake City, UT 84115")]
AREAS = ["Salt Lake City"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18014672432",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "165 Gregson Ave S", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84115", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}}
    return [n]
