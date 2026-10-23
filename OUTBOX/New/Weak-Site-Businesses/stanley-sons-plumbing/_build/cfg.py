"""stanley-sons-plumbing: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Stanley & Sons Plumbing, 2346 E Fort Union Blvd #7100, Salt Lake City, UT 84121, +13853337488, category Plumber.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "stanley-sons-plumbing.example"
U = "https://stanley-sons-plumbing.example/"
TRAIL = True
NAME = "Stanley & Sons Plumbing"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#2a1b1a"
FONTS = "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Libre+Franklin:wght@400;600;700&family=Martian+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "385-333-7488", "+13853337488")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Salt Lake City", "2346 E Fort Union Blvd #7100<br>Salt Lake City, UT 84121")]
AREAS = ["Salt Lake City"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13853337488",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "2346 E Fort Union Blvd #7100", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84121", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}}
    return [n]
