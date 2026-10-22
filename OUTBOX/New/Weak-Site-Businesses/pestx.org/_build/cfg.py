"""pestx.org: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 18 pages (21 Oct 2026), same URLs (no trailing slash) and canonicals.
From the site's own pages: phone +1-801-871-9233, office@pestx.org, "Serving the Greater Salt Lake Area", founded by two brothers
(family owned), eco-friendly targeted treatments, year-round month-to-month protection, satisfaction guarantee ("our technicians will
return as often as necessary to ensure you are satisfied"), pet-friendly practices. The site shows no street address.
From the Google profile (audit report, 21 Oct 2026), copied exactly: Pestx, 661 W 7250 S, Midvale, UT 84047, +1801-871-9233.
Shown as the office address (the report's home target is "pest control midvale" and no page named Midvale); confirm with the client.
Google rating (4.9 from 1,003 reviews) is NOT shown or marked up: ratings change, and self-served review markup isn't allowed.
FAQ answers on the old home page are hidden in a widget and weren't in the HTML, so those questions are not reused; the home Q&A
is built only from the site's own blog posts and home copy.
Tracking kept as on the live site: Google Analytics 4 G-41HFW67EXT.
Images: the live site's photos are AI-generated scenes (technicians, families, dogs) and AI specimen renders, so none are used.
The brand's own ink-wash drawings (pests, house, family, mountains, leaf) are used as illustrations, which is what they are."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "pestx.org"
U = "https://www.pestx.org/"
TRAIL = False
NAME = "Pestx"
TODAY = "2026-10-21"
HOME_OG = "ink-house"
THEME_COLOR = "#f2f3f0"
FONTS = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Manrope:wght@400;500;600;700;800&family=Fragment+Mono&display=swap"
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-41HFW67EXT"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-41HFW67EXT');</script>"""
LOGO = "pestx-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Get a Quote"
CTA_TITLE = "Protect what matters most."
CTA_TEXT = "Safe, effective solutions designed for lasting peace of mind. Call 801-871-9233, email office@pestx.org, or send the form and we&rsquo;ll get back to you promptly."
SIDE_TITLE = "Smart. Trusted. Protected."
PHONES = [("Call", "801-871-9233", "+18018719233")]
EMAIL = "office@pestx.org"
HOURS = ""
STREET = "661 W 7250 S"
CITY = "Midvale"
ZIP = "84047"
ADDRESS = [("Office", "661 W 7250 S<br>Midvale, UT 84047")]
AREAS = ["Midvale", "the Greater Salt Lake Area"]
SOCIAL = []
BLURB = "Family-owned pest control in Midvale, Utah, founded by two brothers. Eco-friendly, targeted treatments and year-round protection across the Greater Salt Lake Area."
SVC_LABEL = "Pests"
PESTS = [("mosquito", "Mosquito", "Culicidae"), ("ants", "Ants", "Formicidae"), ("spiders", "Spiders", "Araneae"), ("rodents", "Rodents", "Rodentia"),
         ("wasps", "Wasps", "Vespidae"), ("beetles", "Beetles", "Seasonal invaders"), ("flies", "Flies", "Diptera"), ("moths", "Moths", "Lepidoptera"),
         ("snails-and-slugs", "Snails and Slugs", "Gastropoda"), ("grasshopper", "Grasshopper", "Orthoptera")]
INK = {"mosquito": "ink-mosquito", "ants": "ink-ants", "spiders": "ink-spiders", "rodents": "ink-rodents", "wasps": "ink-wasps", "beetles": "ink-beetles",
       "flies": "ink-flies", "moths": "ink-moths", "snails-and-slugs": "ink-snails", "grasshopper": "ink-grasshopper"}
SVC = [(f"pests/{s}/", n, None) for s, n, t in PESTS]
NAV = [("Field guide", "pests/"), ("Blog", "blogs/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "PestControl", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18018719233", "email": EMAIL,
         "logo": U + "assets/img/pestx-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY, "addressRegion": "UT", "postalCode": ZIP, "addressCountry": "US"}}
    if full:
        n.update({"description": "Pestx is a family-owned pest control company in Midvale, Utah, offering eco-friendly, targeted treatments and year-round protection for homes and businesses across the Greater Salt Lake Area.",
                  "slogan": "Smart. Trusted. Protected.",
                  "areaServed": [{"@type": "City", "name": "Midvale, UT"}, {"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}]})
    return [n]
