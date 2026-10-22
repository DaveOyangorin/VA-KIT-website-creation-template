"""mountainwindowcleaning.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: browser crawl (21 Oct 2026) of all six pages: / (also served as /index.html), /window-cleaning.html, /solar-panel-cleaning.html,
/pricing.html, /quote.html, /privacy-policy.html. Same URLs (static .html files) on the www host the live site redirects to.
From the site: call or text 801-518-4062; Pardy LLC, DBA Mountain Window Cleaning (privacy policy); serves Salt Lake and Utah Counties;
residential and commercial; pure-water system and water-fed poles; prices: exterior $4/pane, interior $3/pane, screens $2-3, tracks $5-10,
solar panels $4-6/panel, hard-water stains quoted, $150 minimum per visit, monthly and quarterly plans discounted; the window FAQ; booking
on Housecall Pro; Instagram; Google reviews link. Google listing (report, 15 Oct): Sandy, UT; the street address is not on the site, so it
is not shown (service-area business); schema uses the city only.
Left out until confirmed: the Google rating (5.0 from 390) and any review text.
Photos: the five photos from their own "recent jobs" grid and hero (Utah homes, a storefront) and two Utah scenery photos from their site.
Stock-looking images (UK brick house with a worker, gable-roof solar house, squeegee close-up, modern villa) are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "mountainwindowcleaning.com"
U = "https://www.mountainwindowcleaning.com/"
TRAIL = True
NAME = "Mountain Window Cleaning"
TODAY = "2026-10-21"
HOME_OG = "mw-valley"
THEME_COLOR = "#0f2a3f"
FONTS = "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Manrope:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "mw-logo"
BOOK = "https://book.housecallpro.com/book/Mountain-Window-Cleaning/e08230c121b84cad9fea4f98730bc0cd"
REVIEWS = "https://www.google.com/maps/place/Mountain+Window+Cleaning/@40.5902316,-111.8327845,17z/data=!4m7!3m6!1s0x87527d4aa731d2db:0x9c1d3dd56e09d1ff!8m2!3d40.5902222!4d-111.830564!9m1!1b1"
INSTAGRAM = "https://www.instagram.com/mountain_window_cleaning/"
CTA_PATH = "quote.html"
CTA_LABEL = "Instant Quote"
CTA_TITLE = "Ready for <em>spotless windows?</em>"
CTA_TEXT = "Get your instant quote in about a minute, or call or text 801-518-4062. Free estimates, no pressure."
SIDE_TITLE = "See your price in about a minute."
PHONES = [("Call or text", "801-518-4062", "+18015184062")]
EMAIL = ""
HOURS = ""
ADDRESS = []
AREAS = ["Salt Lake County", "Utah County"]
SOCIAL = [("Instagram", INSTAGRAM), ("Google reviews", REVIEWS), ("Book online", BOOK)]
BLURB = "Streak-free window and solar panel cleaning for homes and businesses across Salt Lake and Utah Counties. Pure water, clear per-pane pricing."
SVC_LABEL = "Services"
SVC = [("window-cleaning.html", "Window cleaning", None), ("window-cleaning.html#commercial", "Commercial windows", None), ("solar-panel-cleaning.html", "Solar panel cleaning", None),
       ("pricing.html", "Screens, tracks &amp; hard water", None)]
NAV = [("Pricing", "pricing.html"), ("Solar panels", "solar-panel-cleaning.html"), ("Instant quote", "quote.html")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME,
         "legalName": "Pardy LLC", "url": U, "telephone": "+18015184062", "logo": U + "assets/img/mw-dark-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "addressLocality": "Sandy", "addressRegion": "UT", "addressCountry": "US"}, "sameAs": [INSTAGRAM],
         "priceRange": "$$"}
    if full:
        n.update({"description": "Mountain Window Cleaning cleans windows, screens, tracks and solar panels for homes and businesses in Salt Lake and Utah Counties, with a pure-water system and per-pane pricing.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", UT"} for c in AREAS],
                  "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s}, "price": p, "priceCurrency": "USD"} for s, p in
                                 (("Exterior window cleaning, per pane", "4.00"), ("Interior window cleaning, per pane", "3.00"))]})
    return [n]
