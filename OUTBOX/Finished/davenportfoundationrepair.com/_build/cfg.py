"""davenportfoundationrepair.com: facts and settings (19 Oct 2026).
Name, address and both phones copied from the client's own site: the header and call buttons use 1-801-569-2302; the location
block uses 1-801-429-9989 (the number on the Google profile, per the report). Address 9427 S 6400 W, West Jordan, UT 84081.
Owner Ron Davenport; "30 years" in business; certified Foundation Supportworks dealer and Basement Systems dealer (about page).
Google profile: 4.8 stars from 1,473 reviews (report), not shown as a number until confirmed.
Tracking kept: Google Tag Manager GTM-KTXCTXQ (head snippet copied as on the live site)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "davenportfoundationrepair.com"
U = "https://www.davenportfoundationrepair.com/"
TRAIL = True
NAME = "Davenport Foundation Repair"
TODAY = "2026-10-19"
HOME_OG = "push-pier-grantsville"
THEME_COLOR = "#16180f"
FONTS = "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Manrope:wght@400;500;600;700;800&family=Spline+Sans+Mono:wght@400;500;600&display=swap"
S = {"phone": "1-801-569-2302", "tel": "+18015692302", "phone2": "1-801-429-9989", "tel2": "+18014299989",
     "street": "9427 S 6400 W", "city": "West Jordan", "st": "UT", "zip": "84081",
     "fb": "https://www.facebook.com/DVPTC/", "ig": "https://www.instagram.com/davenportfoundationrepair/",
     "li": "https://www.linkedin.com/company/davenport-foundation-repair/about/", "yt": "https://www.youtube.com/channel/UCp0VJFE8EyuC-fcwoSXCXow"}
TRACK_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KTXCTXQ');</script>
<!-- End Google Tag Manager -->"""
CITIES = ["West Jordan", "Salt Lake City", "West Valley City", "Provo", "Orem", "Ogden", "Sandy", "South Jordan", "Lehi", "Layton"]


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "url": U, "telephone": S["tel2"],
         "logo": U + "assets/img/davenport-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "sameAs": [S["fb"], S["ig"], S["li"], S["yt"]]}
    if full:
        n.update({"description": "Davenport Foundation Repair is a locally owned foundation repair company in West Jordan, Utah: foundation stabilization, basement waterproofing, crawl space repair, concrete lifting and sealing, and sump pumps.",
                  "employee": {"@type": "Person", "name": "Ron Davenport", "jobTitle": "Owner"},
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in CITIES]})
    return [n]
