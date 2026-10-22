"""trustyappliancerepairutah.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 15 sitemap URLs: /, /about-us/, /services/, /contact-us/, /blogs/ and six maintenance-tip posts at
the root. Same URLs (trailing slash) and canonicals; Elementor header/footer templates, the category and author archives are not pages.
From the site: (801) 255-9063, trustyrepairutah@gmail.com; licensed and insured; 90-day warranty on all repairs; genuine parts; services:
dishwasher, dryer, garbage disposal, microwave, refrigerator, washing machine, oven and range repair; brands listed: Cove, Crosley, Electrolux,
Estate, Jenn-Air, Kenmore, Kirkland Signature, Magic Chef, Maytag, Sub-Zero, Viking, InSinkErator, Thermador, Whirlpool.
NAP: the Google listing (report, 15 Oct) has 8223 S 1000 E, Sandy, UT 84094 with the same phone; the site's contact page says
255 W Amanda Lynn Ln, Midvale, UT 84047. The Google NAP is used, copied exactly; the difference is flagged for the client.
Left out until confirmed: Google rating (4.9 from 311), "years of expertise", "second to none".
Photos: every photo on the site is stock (and the brand row is manufacturer logos), so none are used. Banners are credited Wikimedia Commons
photos: a modern kitchen and a laundry pair (both CC BY 2.0)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "trustyappliancerepairutah.com"
U = "https://trustyappliancerepairutah.com/"
TRAIL = True
NAME = "Trusty Appliance Repair"
TODAY = "2026-10-22"
HOME_OG = "tr-kitchen"
THEME_COLOR = "#141414"
FONTS = "https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Inter+Tight:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "tr-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Schedule a Repair"
CTA_TITLE = "Fixed right. <em>Backed for 90 days.</em>"
CTA_TEXT = "Call (801) 255-9063 to schedule an appointment. Licensed and insured, genuine parts, and a 90-day warranty on all repairs."
SIDE_TITLE = "Licensed, insured, and a 90-day warranty on every repair."
PHONES = [("Call", "(801) 255-9063", "+18012559063")]
EMAIL = "trustyrepairutah@gmail.com"
HOURS = ""
ADDRESS = [("Address", "8223 S 1000 E<br>Sandy, UT 84094")]
AREAS = ["Sandy", "the Salt Lake Valley"]
SOCIAL = []
BLURB = "Appliance repair in Sandy with integrity, transparency and technical expertise. Licensed and insured, with a 90-day warranty on all repairs."
SVC_LABEL = "Repairs"
SVC = [("services/#refrigerator", "Refrigerator repair", None), ("services/#dryer", "Dryer repair", None), ("services/#washer", "Washing machine repair", None), ("services/#dishwasher", "Dishwasher repair", None),
       ("services/#oven", "Oven &amp; range repair", None), ("services/#microwave", "Microwave repair", None), ("services/#disposal", "Garbage disposal repair", None)]
NAV = [("Tips", "blogs/"), ("About", "about-us/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18012559063", "email": EMAIL,
         "logo": U + "assets/img/tr-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "8223 S 1000 E", "addressLocality": "Sandy", "addressRegion": "UT", "postalCode": "84094", "addressCountry": "US"}}
    if full:
        n.update({"description": "Licensed and insured appliance repair in Sandy, Utah: refrigerators, dryers, washers, dishwashers, ovens, ranges, microwaves and garbage disposals, with a 90-day warranty on all repairs.",
                  "areaServed": {"@type": "City", "name": "Sandy, UT"}})
    return [n]
