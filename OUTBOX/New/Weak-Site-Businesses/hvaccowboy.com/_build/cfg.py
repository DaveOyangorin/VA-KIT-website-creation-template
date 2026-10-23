"""hvaccowboy.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live site rendered in a browser on 22 Oct 2026 (it's a JavaScript app; a plain crawl sees 10 words). One URL; one new post added.
From the site: Cowboy Heating & Air; "Commercial Kitchen Equipment · Heating · Air Conditioning"; "Utah Valley's Award-Winning HVAC Team";
24/7 emergency service available, same-day appointments; 100% licensed & insured; "2025 Best HVAC Award" (plaque photo: "Best of
BusinessRate 2025, HVAC Contractor, Lehi Utah"); Daikin Authorized; Bryant Dealer; services: residential AC (service, refrigerant
charging, diagnostics), heating & furnace (repair, installation, maintenance), commercial HVAC (rooftop unit installation, maintenance and
repair for commercial buildings and restaurants), kitchen equipment (commercial kitchen exhaust fans, ventilation systems, equipment
installation); three Google reviews quoted (Juan R., David C., Carlos D.) naming the technician Ricardo; homeowner / business quote form;
service area: Lehi, Orem, Provo, American Fork, Pleasant Grove, Saratoga Springs, Eagle Mountain, Spanish Fork, Springville, Payson.
NAP: Google listing "Cowboy Heating & Air LLC", 1227 W Bridlewood Lp, Lehi, UT 84043, +1801-940-0420 (used, copied exactly). The site
gives no street address.
Left out until confirmed: the "5.0 Google rating" figure (the listing shows 5 stars from 162; the live schema says 3 reviews).
Kept but flagged: the BusinessRate award (plaque photo on the site), Daikin Authorized and Bryant Dealer.
Photos: all their own (company car, rooftop units, control board, exhaust fan, residential AC and furnace work, award plaque)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "hvaccowboy.com"
U = "https://hvaccowboy.com/"
TRAIL = False
NAME = "Cowboy Heating & Air"
TODAY = "2026-10-22"
HOME_OG = "cb-hero"
THEME_COLOR = "#1e3a8a"
FONTS = "https://fonts.googleapis.com/css2?family=Rye&family=Zilla+Slab:wght@600;700&family=Work+Sans:wght@400;500;600;700&display=swap"
TRACK_HEAD = ""
LOGO = "cb-logo"
CTA_PATH = "#quote"
CTA_LABEL = "Get a free quote"
CTA_TITLE = "Honest pricing. <em>Fast response.</em>"
CTA_TEXT = "Call 801-940-0420. 24/7 emergency service available and same-day appointments across Utah Valley, for homes, businesses and commercial kitchens."
SIDE_TITLE = "24/7 emergency service. Same-day appointments."
PHONES = [("Call", "801-940-0420", "+18019400420")]
EMAIL = ""
HOURS = "24/7 emergency service available"
ADDRESS = [("Lehi", "1227 W Bridlewood Lp<br>Lehi, UT 84043")]
AREAS = ["Lehi", "Orem", "Provo", "American Fork", "Pleasant Grove", "Saratoga Springs", "Eagle Mountain", "Spanish Fork", "Springville", "Payson"]
SOCIAL = []
BLURB = "Heating, air conditioning and commercial kitchen equipment service for homes and businesses across Utah Valley. Licensed and insured, 24/7 emergency service."
SVC_LABEL = "Services"
SVC = [("#services", "Residential AC", None), ("#services", "Heating &amp; furnace", None), ("#services", "Commercial HVAC", None), ("#services", "Kitchen equipment", None)]
NAV = [("Home or business", "#crew"), ("Our work", "#work"), ("Blog", "carbon-monoxide-and-your-furnace/")]


def biz(full=True):
    n = {"@type": "HVACBusiness", "@id": U + "#business", "name": "Cowboy Heating & Air LLC", "alternateName": "Cowboy Heating & Air", "url": U, "telephone": "+18019400420",
         "logo": U + "assets/img/cb-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "1227 W Bridlewood Lp", "addressLocality": "Lehi", "addressRegion": "UT", "postalCode": "84043", "addressCountry": "US"}}
    if full:
        n.update({"description": "Residential and commercial heating, air conditioning and commercial kitchen equipment service in Lehi and across Utah Valley. Licensed and insured, 24/7 emergency service.",
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in AREAS]})
    return [n]
