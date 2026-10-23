"""superior-locksmith: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Superior Locksmith, 7679 S Redwood Rd, West Jordan, UT 84084, +18015650226, category Locksmith.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "superior-locksmith.example"
U = "https://superior-locksmith.example/"
TRAIL = True
NAME = "Superior Locksmith"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#1f1a2c"
FONTS = "https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Manrope:wght@400;600;700&family=Azeret+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "801-565-0226", "+18015650226")]
EMAIL = ""
HOURS = ""
ADDRESS = [("West Jordan", "7679 S Redwood Rd<br>West Jordan, UT 84084")]
AREAS = ["West Jordan"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "Locksmith", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18015650226",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "7679 S Redwood Rd", "addressLocality": "West Jordan", "addressRegion": "UT", "postalCode": "84084", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "West Jordan, UT"}}
    return [n]
