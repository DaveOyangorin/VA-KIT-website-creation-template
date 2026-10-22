"""lockthesmithut.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 10 sitemap URLs (21 Oct 2026), same URLs (trailing slash) and canonicals. Only the home page carries real
content; /about/ is the WordPress sample page, /2026/06/16/hello-world/ is the sample post (with a coaching theme's "Who's the Coach?"
filler), /new-site/ (-2, -3) and the four /lock-the-smith-ut-llc-logo/ attachment pages are leftovers. They keep their URLs but become
noindex pages pointing to the real content (flagged: remove or redirect on the live site).
From the home page: phone 801-462-4094 (matches Google), service@lockthesmith.com (note: a different domain from the website),
storefront 2852 S Redwood Rd B14, West Valley City, UT (Google adds ZIP 84119: "2852 S Redwood Rd B14, West Valley City, UT 84119",
copied exactly); storefront hours Mon-Fri 9:00 AM-4:00 PM; mobile service Mon-Sun 8:00 AM-8:00 PM; mobile emergency service; areas
served by county (Salt Lake, Davis, Utah, Weber, Summit; 44 towns as listed); the service list (from their services image, 23 items);
complimentary service call and savings for new customers (offer as stated on the site: flagged to confirm).
Left out: "Expert Experience Guaranteed!", "years of expertise", "fastest response times". Google rating (4.9 from 521) not shown.
No tracking tags beyond WordPress/Jetpack found; none added.
Images: none of the site's photos are used: two are stock, the hero is copied from another locksmith's site ("TML_Emergency-Locksmith_
Hero"), and the services image is a Canva list. The site is drawn instead: their key logo and a drawn pin-tumbler lock."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "lockthesmithut.com"
U = "https://lockthesmithut.com/"
TRAIL = True
NAME = "Lockthesmith"
TODAY = "2026-10-21"
HOME_OG = "lk-logo"
THEME_COLOR = "#121417"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,500..800&family=Inter+Tight:wght@400;500;600;700&family=Red+Hat+Mono:wght@400;500;600&display=swap"
TRACK_HEAD = ""
LOGO = "lk-logo"
CTA_PATH = "#call"
CTA_LABEL = "Call 801-462-4094"
CTA_TITLE = "Locked out? Lost a key? Call now."
CTA_TEXT = "Mobile locksmith service seven days a week, 8 AM to 8 PM, across Salt Lake, Davis, Utah, Weber and Summit counties. Storefront in West Valley City, Monday to Friday, 9 AM to 4 PM."
SIDE_TITLE = "Mobile service daily, 8 AM&ndash;8 PM."
PHONES = [("Emergency call", "801-462-4094", "+18014624094")]
EMAIL = "service@lockthesmith.com"
HOURS = "Storefront: Mon&ndash;Fri 9 AM&ndash;4 PM &middot; Mobile: Mon&ndash;Sun 8 AM&ndash;8 PM"
ADDRESS = [("Storefront", "2852 S Redwood Rd B14<br>West Valley City, UT 84119")]
COUNTIES = [("Salt Lake County", ["Bluffdale", "Cottonwood Heights", "Draper", "Herriman", "Holladay", "Kearns", "Midvale", "Millcreek", "Murray", "Riverton", "Salt Lake City", "Sandy",
                                  "South Jordan", "Taylorsville", "West Jordan", "West Valley City"]),
            ("Davis County", ["Bountiful", "Centerville", "Clearfield", "Farmington", "Kaysville", "Layton", "Syracuse", "West Bountiful", "Woods Cross"]),
            ("Utah County", ["American Fork", "Eagle Mountain", "Lehi", "Orem", "Pleasant Grove", "Provo", "Saratoga Springs", "Spanish Fork", "Vineyard"]),
            ("Weber County", ["North Ogden", "Ogden", "Riverdale", "Roy", "South Ogden", "Washington Terrace"]),
            ("Summit County", ["Coalville", "Kamas", "Park City"])]
AREAS = ["West Valley City", "Salt Lake City", "Salt Lake, Davis, Utah, Weber and Summit counties"]
SOCIAL = []
BLURB = "Mobile and storefront locksmith in West Valley City: lockouts, key replacement and programming, high-security and smart locks, safes, and emergency service."
SVC_LABEL = "Services"
SERVICES = [("Lockouts", ["Car Lockout Service", "Residential Lockout Service", "Commercial Lockout Service", "Emergency Locksmith"]),
            ("Keys", ["Key Duplication and Replacement", "Lost Key Replacement", "Key Replacement Service", "Car Key Duplication", "Key Programming", "Smart Key Programming"]),
            ("Car keys by make", ["Chevy Car Key Replacement", "Dodge Car Key Replacement", "Honda Car Key Replacement", "Lexus Car Key Replacement", "Nissan Car Key Replacement", "Toyota Car Key Replacement"]),
            ("Locks &amp; safes", ["High-Security Lock Setup", "Lock Upgrade", "Smart Lock Installation", "Safe Installation and Repair"]),
            ("Who we help", ["Residential Locksmith", "Commercial Locksmith", "Automotive Locksmith"])]
SVC = [("#lock", "Lockouts", None), ("#lock", "Car keys", None), ("#lock", "Key programming", None), ("#lock", "Locks &amp; safes", None)]
NAV = [("Services", "#services"), ("Hours", "#hours"), ("Areas", "#areas"), ("About", "about/")]


def biz(full=True):
    n = {"@type": "Locksmith", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18014624094", "email": EMAIL,
         "logo": U + "assets/img/lk-logo.png", "image": U + "assets/img/lk-logo.png",
         "address": {"@type": "PostalAddress", "streetAddress": "2852 S Redwood Rd B14", "addressLocality": "West Valley City", "addressRegion": "UT", "postalCode": "84119", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "16:00", "description": "Storefront"}]}
    if full:
        n.update({"description": "Lockthesmith is a mobile and storefront locksmith in West Valley City, Utah: lockouts, key duplication and replacement, key programming, high-security and smart locks, safes and emergency service.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", UT"} for c, t in COUNTIES],
                  "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Locksmith services", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s}} for g, ss in SERVICES[:4] for s in ss]}})
    return [n]
