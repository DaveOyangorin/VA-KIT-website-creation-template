"""gross-family-plumbing-llc: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Gross Family Plumbing LLC, 1750 Research Way #3600, Salt Lake City, UT 84119, +13853311988, category Plumber.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "gross-family-plumbing.example"
U = "https://gross-family-plumbing.example/"
TRAIL = True
NAME = "Gross Family Plumbing LLC"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#1b2a1e"
FONTS = "https://fonts.googleapis.com/css2?family=Sora:wght@600;800&family=Inter:wght@400;600;700&family=Fira+Code:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "385-331-1988", "+13853311988")]
EMAIL = ""
HOURS = ""
ADDRESS = [("Salt Lake City", "1750 Research Way #3600<br>Salt Lake City, UT 84119")]
AREAS = ["Salt Lake City"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13853311988",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "1750 Research Way #3600", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84119", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}}
    return [n]
