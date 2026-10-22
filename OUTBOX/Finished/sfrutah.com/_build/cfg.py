"""sfrutah.com: facts and settings (19 Oct 2026).
The live site is broken today (the home page shows a template "404 Page Not Found" and the blog URLs 404), so all content comes from
the Wayback Machine captures of Mar-Jul 2026 (home: 11 Jul 2026). Business: Superior Foundation Repair Utah, founded 2019 by owner
Matt Baker. Offices as written on the home page (the contact page swaps the labels and adds a Midvale address; flagged):
  Salt Lake City: 774 East 2100 South, Suite 448, Salt Lake City, UT 84106 - 801-970-1473 (Google profile: 774 E 2100 S Ste 448)
  St. George: 1792 N Serenity Dr, St. George, UT 84770 - 435-668-0734
Email office@sfrutah.com. Hours Mon-Fri 9:00 AM - 5:00 PM (contact page). Google: 5 stars from 17 reviews (report), not shown as a
number until confirmed. No tracking code found in the captures."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "sfrutah.com"
U = "https://www.sfrutah.com/"
TRAIL = False
NAME = "Superior Foundation Repair Utah"
SHORT = "Superior Foundation Repair"
TODAY = "2026-10-19"
HOME_OG = "orem-excavation"
THEME_COLOR = "#0c0f3a"
FONTS = "https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,600;0,700;0,800;1,700&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap"
S = {"phone": "801-970-1473", "tel": "+18019701473", "phone2": "435-668-0734", "tel2": "+14356680734", "email": "office@sfrutah.com",
     "street": "774 East 2100 South, Suite 448", "city": "Salt Lake City", "st": "UT", "zip": "84106",
     "street2": "1792 N Serenity Dr", "city2": "St. George", "zip2": "84770", "hours": "Mon&ndash;Fri 9:00 AM &ndash; 5:00 PM",
     "fb": "https://www.facebook.com/SuperiorFoundationRepairSFR/", "ig": "https://www.instagram.com/superior_foundation_repair/",
     "yt": "https://www.youtube.com/@superior-foundationrepair", "bbb": "https://www.bbb.org/us/ut/st-george/profile/foundation-repair/superior-foundation-repair-1166-90027863",
     "kutv": "https://youtu.be/zR61FIV7Myc"}
TRACK_HEAD = ""
CITIES = ["Salt Lake City", "St. George", "Cedar City", "Kanab", "Duck Creek Village", "Provo", "Ogden", "Park City", "Price", "Herriman"]


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "url": U, "telephone": S["tel"], "email": S["email"],
         "foundingDate": "2019", "logo": U + "assets/img/sfr-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"}],
         "sameAs": [S["fb"], S["ig"], S["yt"], S["bbb"]],
         "department": [{"@type": "HomeAndConstructionBusiness", "name": NAME + " (St. George)", "telephone": S["tel2"],
                         "address": {"@type": "PostalAddress", "streetAddress": S["street2"], "addressLocality": S["city2"], "addressRegion": "UT", "postalCode": S["zip2"], "addressCountry": "US"}}]}
    if full:
        n.update({"description": "Superior Foundation Repair Utah is a locally owned foundation repair company with offices in Salt Lake City and St. George: helical piers, house and mobile home leveling, crack repair, waterproofing, crawl space encapsulation, and post and beam repair.",
                  "founder": {"@type": "Person", "name": "Matt Baker"}, "areaServed": [{"@type": "City", "name": c + ", UT"} for c in CITIES]})
    return [n]
