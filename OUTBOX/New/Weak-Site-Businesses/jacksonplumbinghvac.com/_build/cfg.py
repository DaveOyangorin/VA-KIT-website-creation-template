"""jacksonplumbinghvac.com: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: the live site is one page titled "Colorado 24/7 Plumbing Call" (68 words, two broken images, no phone number), and the Internet
Archive's captures back to Nov 2024 are the same page. There is no real content to recover. This draft uses ONLY the Google listing:
Jackson Family Plumbing & HVAC, 6959 W 7800 S, West Jordan, UT 84081, +1385-595-5700, category Plumber (copied exactly).
Not used, pending the client: the live page's "#1 Ranked Colorado Plumbing Service Company", "Licensed · Bonded · Insured" and the
"Milliken, CO" metro area; any list of specific services, hours, years in business, staff; the 4.9 / 170 rating.
Banner: credited Wikimedia Commons aerial of West Jordan and Taylorsville. No photos of their own exist."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "jacksonplumbinghvac.com"
U = "https://jacksonplumbinghvac.com/"
TRAIL = True
NAME = "Jackson Family Plumbing & HVAC"
TODAY = "2026-10-23"
HOME_OG = "jk-hero"
THEME_COLOR = "#0e2230"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "jk-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Contact us"
CTA_TITLE = "A plumbing or HVAC problem? <em>Call the family.</em>"
CTA_TEXT = "Call Jackson Family Plumbing &amp; HVAC at 385-595-5700. 6959 W 7800 S, West Jordan, UT 84081."
SIDE_TITLE = "Plumbing and HVAC in West Jordan."
PHONES = [("Call", "385-595-5700", "+13855955700")]
EMAIL = ""
HOURS = ""
ADDRESS = [("West Jordan", "6959 W 7800 S<br>West Jordan, UT 84081")]
AREAS = ["West Jordan"]
SOCIAL = []
BLURB = "Jackson Family Plumbing &amp; HVAC: a plumbing and HVAC company at 6959 W 7800 S in West Jordan, Utah."
SVC_LABEL = "Help"
SVC = [("#meter", "Two-hour leak test", None), (f"how-to-keep-pipes-from-freezing/", "Keep pipes from freezing", None)]
NAV = [("Leak test", "#meter"), ("Frozen pipes", "how-to-keep-pipes-from-freezing/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "Plumber", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13855955700",
         "logo": U + "assets/img/jk-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "6959 W 7800 S", "addressLocality": "West Jordan", "addressRegion": "UT", "postalCode": "84081", "addressCountry": "US"}}
    if full:
        n.update({"description": "Plumbing and HVAC company in West Jordan, Utah.", "areaServed": {"@type": "City", "name": "West Jordan, UT"}})
    return [n]
