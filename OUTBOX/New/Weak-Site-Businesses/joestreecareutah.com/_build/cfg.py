"""joestreecareutah.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 12 sitemap pages (no trailing slash): /home, /about-us, /services, /tree-trimming, /stump-grinding,
/plant-health-care, /tree-removal, /hoa-service-plans, /small-landscaping, /our-work, /contact-us. Same URLs; the root serves the home page.
From the site: Joe's Tree Care; (801) 289-6689; family-run, started in 2018; licensed and insured; locally owned and operated; same-week
availability; commercial-grade (pro-grade) equipment; services: tree trimming, stump grinding, plant health care (dormant oil sprays,
slow-release fertilizer, systemic care), tree removal, HOA service plans, small landscaping (beds, rock, cleanups, sod); serving Utah,
Salt Lake and Wasatch counties; the six-question FAQ (bundling, fertilizer April-September, dormant oil April-early May, yard-safe machinery,
payments: Venmo, cash, check, credit card, Apple Pay). Google listing: "Joe's Stump Grinding", +1801-289-6689, no address (service area).
The site's brand and logo are "Joe's Tree Care"; that is used, with the Google name in schema. Flagged for the client.
Left out: leftover lawn-care template text on their site ("40+ years of excellence", mowing, aeration, lawn FAQ), "1000+ happy homeowners",
"150+ five-star Google reviews" (Google shows 5.0 from 292; neither shown until confirmed), "Utah's best", "Utah's premier".
Photos: their own job photos (crane removal under the Wasatch, stump grinding, the crew, mulch, before/after sod) at original size from
their media storage. Stock images on their site (gardening, lawn mower, arborist stock) are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "joestreecareutah.com"
U = "https://joestreecareutah.com/"
TRAIL = False
NAME = "Joe's Tree Care"
TODAY = "2026-10-22"
HOME_OG = "jt-grind"
THEME_COLOR = "#123d2a"
FONTS = "https://fonts.googleapis.com/css2?family=Zilla+Slab:ital,wght@0,600;0,700;1,600&family=Work+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap"
TRACK_HEAD = ""
LOGO = "jt-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Free Quote"
CTA_TITLE = "One visit. <em>The whole yard.</em>"
CTA_TEXT = "Call (801) 289-6689 for a free quote. Bundle your trimming, removal and stump grinding into one visit and save. Same-week availability."
SIDE_TITLE = "Same-week availability. Licensed and insured."
PHONES = [("Call", "(801) 289-6689", "+18012896689")]
EMAIL = ""
HOURS = ""
ADDRESS = []
AREAS = ["Salt Lake County", "Utah County", "Wasatch County"]
SOCIAL = []
BLURB = "Family-run tree care since 2018: trimming, removal, stump grinding, plant health care and small landscaping. Licensed, insured and locally owned."
SVC_LABEL = "Services"
SVC = [("tree-trimming/", "Tree trimming", None), ("tree-removal/", "Tree removal", None), ("stump-grinding/", "Stump grinding", None), ("plant-health-care/", "Plant health care", None),
       ("hoa-service-plans/", "HOA service plans", None), ("small-landscaping/", "Small landscaping", None)]
NAV = [("Our work", "our-work/"), ("About", "about-us/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "alternateName": "Joe's Stump Grinding", "url": U, "telephone": "+18012896689",
         "logo": U + "assets/img/jt-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "foundingDate": "2018",
         "address": {"@type": "PostalAddress", "addressRegion": "UT", "addressCountry": "US"}, "paymentAccepted": "Venmo, cash, check, credit card, Apple Pay"}
    if full:
        n.update({"description": "Family-run, licensed and insured tree care in Salt Lake, Utah and Wasatch counties: tree trimming, tree removal, stump grinding, plant health care, HOA plans and small landscaping.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", UT"} for c in AREAS]})
    return [n]
