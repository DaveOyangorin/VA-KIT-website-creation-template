"""rhinofoundationsystems.com: facts and settings (20 Oct 2026).
SOURCE: the live site blocks this network (connection timed out), so every page is rebuilt from the Internet Archive's captures
of July-September 2025 (30 pages: the page sitemap plus the nav). The report (5 Oct 2026 audit) counts 96 pages, so the site has
grown since; pages added after September 2025 are not in this draft (flagged).
From the site's own pages: phone 801-509-5344 (tel:8015095344; a second number 801-492-3503 appears on a quote banner),
office@rhinofoundationsystems.com. The site shows no street address. The Google profile (report) gives 35 Barratt Ave, American
Fork, UT 84003, phone +1435-660-5182 and 4.7 stars from 290 reviews: not shown until the client confirms (flagged).
Left out until confirmed: "over 40 years", "Trusted since 1985", "thousands of customers/projects", "hundreds of 5-star reviews",
"certified", warranties, "no subcontractors", "Utah's leading", and the named-family case studies on the city pages.
Kept as stated: "licensed and insured"; free estimates; the three testimonials quoted word for word with the names the site shows.
Tracking kept as on the live site: Google Tag Manager GTM-PKK38W6K.
Photos: only the client's own (branded truck, helical piers, push-pier install, basement install, measured slab lips, sidewalk).
Stock files on the live site (Depositphotos, Adobe 240_F_, iStock, product renders, cartoon illustrations) are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "rhinofoundationsystems.com"
U = "https://rhinofoundationsystems.com/"
TRAIL = True
NAME = "Rhino Foundation Systems"
TODAY = "2026-10-20"
HOME_OG = "rhino-truck"
THEME_COLOR = "#0d1620"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap"
TRACK_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PKK38W6K');</script>
<!-- End Google Tag Manager -->"""
LOGO = "rhino-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Cracks, a wet basement or a sinking slab? Get a free estimate."
CTA_TEXT = "Call 801-509-5344 or send the form. We&rsquo;ll look at the problem, explain what&rsquo;s causing it, and give you a free estimate."
SIDE_TITLE = "Free consultations and free estimates."
PHONES = [("Call", "801-509-5344", "+18015095344")]
EMAIL = "office@rhinofoundationsystems.com"
HOURS = ""
ADDRESS = []
AREAS = ["Salt Lake City", "West Valley City", "Sandy", "Draper", "Lehi", "American Fork", "Alpine", "Highland", "Saratoga Springs", "Orem", "Provo", "Ogden", "Logan",
         "Layton", "Bountiful", "Park City", "Heber City", "St. George"]
SOCIAL = []
BLURB = "Foundation repair, basement waterproofing, crawl space encapsulation and concrete lifting across Utah, from the Wasatch Front to St. George. Licensed and insured."
SVC_LABEL = "Services"
SVC = [("foundation-repair/", "Foundation repair", None), ("helical-piers-push-piers/", "Helical &amp; push piers", None), ("basement-waterproofing/", "Basement waterproofing", None),
       ("crawl-space-encapsulation/", "Crawl space encapsulation", None), ("french-drains/", "French drains", None), ("sump-pumps/", "Sump pumps", None),
       ("commercial-foundation-repair/", "Commercial foundation repair", None), ("concrete-lifting/", "Concrete lifting", None), ("concrete-installation/", "Concrete installation", None),
       ("vuba-stone/", "Vuba Stone overlays", None)]
NAV = [("Service area", "service-area/"), ("About", "about-us/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18015095344", "email": EMAIL,
         "logo": U + "assets/img/rhinoink-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "addressRegion": "UT", "addressCountry": "US"}}
    if full:
        n.update({"description": "Rhino Foundation Systems repairs foundations, waterproofs basements, encapsulates crawl spaces and lifts and repairs concrete for homes and businesses across Utah.",
                  "areaServed": [{"@type": "State", "name": "Utah"}] + [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
