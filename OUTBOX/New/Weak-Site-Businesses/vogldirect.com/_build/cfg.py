"""vogldirect.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 24 pages in the menu and sitemap. Same URLs (trailing slash) and canonicals.
From the site: (385) 352-3285, call or text; locally owned and operated; veteran owned ("our owners are proud veterans of the U.S. armed
forces"); located in Eagle Mountain; serving Utah County, Salt Lake County and Tooele; regular hours 8:00 am - 5:00 pm Monday - Sunday,
24-hour emergency service (fees applicable); free second opinion and free on-site estimates; American Standard and Mitsubishi installs with a
Lifetime Workmanship Guarantee and system sizing; services: heating, cooling, mini splits, gas lines (TracPipe), duct work, air quality and
filters, commercial maintenance, refrigerant reclaim, solar via partner Red Stone Clean Energy; Comfort Club plans (Basic $8.99/mo,
Preferred $15.99/mo, Preferred Plus $34.99/mo, add-ons $9/$4/$6/$4); current deals ($25 off any service, call for rebates, 65% off a year
supply of filters); filters: year supply of 1" pleated $39.95, free Aprilaire 4" filter box with new furnaces; financing available; five
named reviews on the home and about pages. Google listing has no address (service-area business), so no street address is shown.
Left out until confirmed: Google rating (4.9 from 334), "Guaranteed Best Value in Town", "best in the business", "one of Utah's most qualified".
Lorem-ipsum page /energy-efficiency/, empty /our-reviews/ and /recent-projects/, and the WordPress "Hello world!" post: kept at their URLs,
noindex. Photos: all site photos are Shutterstock, so none are used; banners are credited Wikimedia Commons photos of Utah County."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "vogldirect.com"
U = "https://vogldirect.com/"
TRAIL = True
NAME = "Vogl Direct"
TODAY = "2026-10-22"
HOME_OG = "vg-timp"
THEME_COLOR = "#0f2740"
FONTS = "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap"
TRACK_HEAD = ""
LOGO = "vg-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Straight answers. <em>Day or night.</em>"
CTA_TEXT = "Call or text (385) 352-3285 for a free on-site estimate or a free second opinion. 24-hour emergency service across Utah County, Salt Lake County and Tooele."
SIDE_TITLE = "Free on-site estimates and free second opinions."
PHONES = [("Call or text", "(385) 352-3285", "+13853523285")]
EMAIL = ""
HOURS = "Mon&ndash;Sun 8 am&ndash;5 pm &middot; 24-hour emergency service (fees apply)"
ADDRESS = []
AREAS = ["Utah County", "Salt Lake County", "Tooele"]
SOCIAL = []
BLURB = "Veteran owned, locally owned and operated heating and air from Eagle Mountain. Up-front, transparent, honest work with no added fluff."
SVC_LABEL = "Services"
SVC = [("heating/", "Heating &amp; furnaces", None), ("cooling/", "Cooling &amp; mini splits", None), ("installations/", "Installations", None), ("duct-work-2/", "Duct work", None),
       ("air-quality/", "Air quality &amp; filters", None), ("commercial/", "Commercial maintenance", None), ("reclaim/", "Refrigerant reclaim", None), ("solar/", "Solar", None)]
NAV = [("Comfort Club", "comfort-club/"), ("Deals", "current-deals/"), ("Financing", "financing/"), ("About", "about/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "HVACBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13853523285", "logo": U + "assets/img/vg-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "addressLocality": "Eagle Mountain", "addressRegion": "UT", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Veteran-owned heating and air conditioning company in Eagle Mountain serving Utah County, Salt Lake County and Tooele: furnace and AC repair and installation, mini splits, duct work, commercial maintenance and refrigerant reclaim.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": "Utah County, UT"}, {"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}, {"@type": "AdministrativeArea", "name": "Tooele County, UT"}],
                  "brand": [{"@type": "Brand", "name": "American Standard"}, {"@type": "Brand", "name": "Mitsubishi"}]})
    return [n]
