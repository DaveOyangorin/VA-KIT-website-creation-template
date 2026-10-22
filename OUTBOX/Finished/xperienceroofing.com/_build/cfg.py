"""xperienceroofing.com: facts and settings (18 Oct 2026).
NAP and hours copied from the client's contact page ("8034 S State St Suite B, Midvale, UT 84047"; the Google profile writes
"Ste B"). Phone (385) 402-6364 matches the Google profile (+1385-402-6364). The client's GA4 tag is kept on the live build."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "xperienceroofing.com"
U = "https://xperienceroofing.com/"
TRAIL = False
NAME = "Xperience Roofing"
TODAY = "2026-10-18"
HOME_OG = "og-card"
THEME_COLOR = "#1d2023"
FONTS = "https://fonts.googleapis.com/css2?family=Gloock&family=Sora:wght@300;400;500;600;700&family=Martian+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-J6XPDS3KLB"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-J6XPDS3KLB');</script>"""
S = {"phone": "(385) 402-6364", "tel": "+13854026364", "email": "service@xperienceroofing.com",
     "street": "8034 S State St Suite B", "city": "Midvale", "st": "UT", "zip": "84047",
     "hours": [("Mon &ndash; Sat", "9:00am &ndash; 8:30pm"), ("Sunday", "Closed")], "since": "2019"}
CITIES = [("Midvale", "locations/midvale-ut/"), ("Sandy", "locations/sandy-ut/"), ("Draper", "locations/draper-ut/"), ("Murray", "locations/murray-ut/"),
          ("South Jordan", "locations/south-jordan-ut/"), ("West Jordan", "locations/west-jordan-ut/"), ("Riverton", "locations/riverton-ut/"),
          ("Holladay", "locations/holladay-ut/"), ("Cottonwood Heights", "locations/cottonwood-heights-ut/"), ("Salt Lake City", "locations/salt-lake-city-ut/")]


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/xperience-roofing-logo.png", "image": U + "assets/img/og-card.webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "09:00", "closes": "20:30"}]}
    if full:
        n.update({"description": "Xperience Roofing is a family-run roofing contractor in Midvale, Utah, serving the Salt Lake Valley since 2019: roof replacement, repair, inspections, commercial roofing, metal roofing and solar detach and reset.",
                  "foundingDate": "2019", "areaServed": [{"@type": "City", "name": c} for c, _ in CITIES]})
    return [n]
