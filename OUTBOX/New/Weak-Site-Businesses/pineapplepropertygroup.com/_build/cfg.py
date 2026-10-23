"""pineapplepropertygroup.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: the live site refuses connections from our network (403, then timeouts, browser too), so content comes from the Internet Archive's
most recent captures (home 10 Jul 2026, Property-Management 18 Jun 2026, Investments and Investment-Valuation-Tool 12 Jul 2026,
Brokerage-Services / Team 9 May 2026, The-Team 14 Apr 2026, Owner-Tenant-Portal and contact-us 11 Sep 2025). Same 10 URLs (www, no trailing
slash, mixed case); no canonical tags on the live site.
From the site: Pineapple Property Group, LLC; "Integrity. Professionalism. Real Estate." (logo); management fees start at 5% (5% of gross receipts;
"Other Management companies will charge 10% or more"; performance-based: if NOI rises 10%, an additional small commission after 12 months);
90 days with no management fee, cancel any time; company averages they report (99.2% unit occupancy, 18 hrs repair attendance, 10% cash on
cash, 32% average NOI); investment, tenant and maintenance service lists; five managed properties with years managed and returns they report;
brokerage (investment property and residential sales, 1031 exchange analysis); service-area list (40 cities); team of 11; five tenant reviews;
call or text 801-207-9699; 433 S 400 E, ste 200, Salt Lake City; hours Mon-Fri 9am-5pm.
NAP: Google listing 433 S 400 E #200, Salt Lake City, UT 84111, +1801-207-9699 (used, copied exactly).
Ignored: a footer block with "707 West 700 South, Suite 201, Woods Cross" and 801.294.6400 that sits in an HTML comment (web designer's
template leftover). The valuation tool's "What Pineapple Says" box is lorem ipsum.
Left out until confirmed: the 4.2 / 720 Google rating.
Photos: their seven team headshots and logo. The slider photos are stock and not used; banners are credited Wikimedia Commons photos of
Salt Lake City apartment buildings."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "pineapplepropertygroup.com"
U = "https://www.pineapplepropertygroup.com/"
TRAIL = False
NAME = "Pineapple Property Group"
TODAY = "2026-10-22"
HOME_OG = "pp-hero"
THEME_COLOR = "#12342c"
FONTS = "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap"
TRACK_HEAD = ""
LOGO = "pp-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Request info"
CTA_TITLE = "90 days, <em>no management fee.</em>"
CTA_TEXT = "Try Pineapple's property management risk free and cancel any time. After 90 days the rate is just 5%. Call or text 801-207-9699."
SIDE_TITLE = "Management fees start at just 5%."
PHONES = [("Call or text", "801-207-9699", "+18012079699")]
EMAIL = ""
HOURS = "Mon&ndash;Fri 9am&ndash;5pm"
ADDRESS = [("Office", "433 S 400 E #200<br>Salt Lake City, UT 84111")]
AREAS = ["Salt Lake City", "Salt Lake, Utah, Davis &amp; Weber counties", "Park City &amp; Heber"]
SOCIAL = []
BLURB = "Pineapple Property Group, LLC: property management, investment property brokerage and residential sales in Salt Lake City and beyond. Integrity. Professionalism. Real Estate."
SVC_LABEL = "Services"
SVC = [("Property-Management/", "Property management", None), ("Brokerage-Services/", "Brokerage services", None), ("Investments/", "Current investments", None),
       ("Investment-Valuation-Tool/", "Investment valuation tool", None), ("Owner-Tenant-Portal/", "Owner &amp; tenant portal", None)]
NAV = [("Valuation tool", "Investment-Valuation-Tool/"), ("The team", "The-Team/"), ("Contact", "contact-us/")]
CITIES = ["Salt Lake City", "Millcreek", "North Salt Lake", "South Salt Lake", "Holladay", "Cottonwood Heights", "Murray", "Midvale", "Sandy", "Draper", "Bluffdale", "Herriman",
          "South Jordan", "West Jordan", "Riverton", "Taylorsville", "Kearns", "West Valley City", "Magna", "Lehi", "Highland", "Alpine", "Pleasant Grove", "Lindon", "Saratoga Springs",
          "Orem", "Provo", "Spanish Fork", "Bountiful", "Woods Cross", "Centerville", "Farmington", "Layton", "Roy", "Syracuse", "Clearfield", "Ogden", "Park City", "Heber", "Midway"]


def biz(full=True):
    n = {"@type": "RealEstateAgent", "@id": U + "#business", "name": "Pineapple Property Group", "legalName": "Pineapple Property Group, LLC", "url": U, "telephone": "+18012079699",
         "logo": U + "assets/img/pp-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "slogan": "Integrity. Professionalism. Real Estate.",
         "address": {"@type": "PostalAddress", "streetAddress": "433 S 400 E #200", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84111", "addressCountry": "US"}}
    if full:
        n.update({"description": "Salt Lake City property management for multi-unit apartment buildings, condos, townhomes and single-family rentals, plus investment property brokerage and residential sales.",
                  "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"},
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in CITIES]})
    return [n]
