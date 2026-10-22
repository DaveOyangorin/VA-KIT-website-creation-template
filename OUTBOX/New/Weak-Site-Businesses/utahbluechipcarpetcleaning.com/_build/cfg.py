"""utahbluechipcarpetcleaning.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 17 sitemap URLs: /, /about-us, /services, /privacy-policy, /terms-of-service and 11 booking pages
under /booking-calendar/. Same URLs (no trailing slash, Wix) on the www host, same canonicals.
From the site: family company that started out restoring antique Persian and oriental rugs; four-step organic, non-residue cleaning (no soaps,
chemicals or harsh detergents, no over-soaking), dry in 1-3 hours, safe for kids, pets and people with breathing problems; IICRC-taught method;
technicians background checked; 100% satisfaction guaranteed; workmanship guaranteed up to 15 days; evenings and weekends; exact appointment
times, next-day and same-day most days; no prep or furniture moving; services: residential and commercial carpet, tile, air duct cleaning and
sanitizing, upholstery (dries within 90 minutes), pet odor removal, area and oriental rugs, 24-hour emergency; online prices from /services
(1 room and hallway $89.95 to 10 rooms $349.95, emergency from $350, ducts $15 per vent and per return, duct packages by home size, pet
treatment $100); payment on completion (cards, checks, cash); three named reviews. Areas: Salt Lake and Utah counties (home), Utah, Summit
and Tooele counties (meta).
NAP: Google listing phone +1801-785-7385, no address (service-area). The site shows 801-645-3501. The Google phone is used; flagged.
Also flagged: the home page says ducts are $10 per vent/return, the services (booking) page says $15; the booking price is used.
Left out until confirmed: Google rating (4.7 from 292), "#1 recommended method", "go-to carpet cleaning company in Utah".
Photos: the site's photos are Wix library stock, so none are used. Banners are credited Wikimedia Commons photos of Persian carpets (A.Davey,
CC BY 2.0) and a carpet texture (Kurt Kaiser, CC0)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "utahbluechipcarpetcleaning.com"
U = "https://www.utahbluechipcarpetcleaning.com/"
TRAIL = False
NAME = "Blue Chip Carpet Cleaning"
TODAY = "2026-10-22"
HOME_OG = "bc-rug"
THEME_COLOR = "#13265c"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,700;1,9..144,500&family=Figtree:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "bc-logo"
CTA_PATH = "services/"
CTA_LABEL = "Book Online"
CTA_TITLE = "Call today. <em>We&rsquo;ll be there tomorrow.</em>"
CTA_TEXT = "Book online at our published prices, or call 801-785-7385. Exact appointment times, no prep, no moving furniture, and payment only when the job is done."
SIDE_TITLE = "Exact appointment times. Next-day and same-day most days."
PHONES = [("Call", "801-785-7385", "+18017857385")]
EMAIL = ""
HOURS = "Evenings &amp; weekends available &middot; 24-hour emergency service"
ADDRESS = []
AREAS = ["Salt Lake County", "Utah County", "Summit County", "Tooele County"]
SOCIAL = []
BLURB = "Family-owned organic carpet, rug, upholstery and air duct cleaning, from a company that started out restoring antique Persian and oriental rugs. Spotless."
SVC_LABEL = "Services"
SVC = [("services/#carpet", "Carpet cleaning", None), ("services/#rugs", "Area &amp; oriental rugs", None), ("services/#upholstery", "Upholstery", None), ("services/#ducts", "Air duct cleaning", None),
       ("services/#pet", "Pet odor removal", None), ("services/#commercial", "Commercial carpet &amp; tile", None)]
NAV = [("Prices", "services/"), ("About", "about-us/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18017857385", "logo": U + "assets/img/bc-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "addressRegion": "UT", "addressCountry": "US"}, "paymentAccepted": "Credit card, check, cash, cashier's check", "priceRange": "$$"}
    if full:
        n.update({"description": "Family-owned organic carpet cleaning, area and oriental rug cleaning, upholstery, pet odor removal and air duct cleaning in Salt Lake, Utah, Summit and Tooele counties.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", UT"} for c in AREAS]})
    return [n]
