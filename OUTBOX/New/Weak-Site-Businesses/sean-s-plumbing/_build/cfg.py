"""sean-s-plumbing: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
NO WEBSITE: the Google listing has no website and the business has none to rebuild. This draft uses ONLY the Google listing (pulled 15 Oct
2026, copied exactly): Sean's Plumbing, 10330 S Redwood Rd #5230, South Jordan, UT 84095, +14358506314, category Plumber.
Not used, pending the client: services, hours, years, staff, licenses, prices, photos, the Google rating and review count.
DOMAIN: none yet. U is a reserved .example placeholder; set the real domain before launch (canonicals, sitemap, robots, schema all use it)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "seans-plumbing.example"
U = "https://seans-plumbing.example/"
TRAIL = True
NAME = "Sean's Plumbing"
TODAY = "2026-10-23"
HOME_OG = "hero"
THEME_COLOR = "#0e2c3a"
FONTS = "https://fonts.googleapis.com/css2?family=Outfit:wght@600;800&family=Nunito+Sans:wght@400;600;700&family=JetBrains+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "site-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
PHONES = [("Call", "435-850-6314", "+14358506314")]
EMAIL = ""
HOURS = ""
ADDRESS = [("South Jordan", "10330 S Redwood Rd #5230<br>South Jordan, UT 84095")]
AREAS = ["South Jordan"]
SOCIAL = []
SVC_LABEL = "Help"
from content import CTA_TITLE, CTA_TEXT, SIDE_TITLE, BLURB, SVC, NAV


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+14358506314",
         "logo": U + "assets/img/site-logo.png", "image": U + "assets/img/hero.webp", "address": {"@type": "PostalAddress", "streetAddress": "10330 S Redwood Rd #5230", "addressLocality": "South Jordan", "addressRegion": "UT", "postalCode": "84095", "addressCountry": "US"},
         "areaServed": {"@type": "City", "name": "South Jordan, UT"}}
    return [n]
