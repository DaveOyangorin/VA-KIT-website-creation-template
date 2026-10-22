"""armour-crete.com: facts and settings (20 Oct 2026).
The site calls the business "Armour Crete"; the Google profile says "Armored Concrete Systems" (report; flagged). Phones from the
site header: Dylan 435-994-5235 (also the schema telephone on the live site), Zac 435-224-6987. Google lists +1435-938-9271
(flagged). Email evans@armour-crete.com. No street address on the site or Google (service-area business): none shown.
Licensed & insured, certified Deco applicator, free on-site assessment (site text). Google: 5 stars from 3 reviews (report).
Tracking kept: Google Analytics 4 G-MYHF4YMJ3Y (gtag, as on the live site).
Photos: the client has no photos on its site. Atmosphere photos of Snow Canyon / Color Country / Pine Valley are openly licensed
(Openverse: CC BY 2.0 by pkinney62 on Flickr; public domain BLM Utah and US Forest Service) and credited on the site and in the
notes. They are never presented as the client's work; the services are shown with original drawings."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "armour-crete.com"
U = "https://www.armour-crete.com/"
TRAIL = True
NAME = "Armour Crete"
TODAY = "2026-10-20"
HOME_OG = "snow-canyon-slickrock"
THEME_COLOR = "#1b1512"
FONTS = "https://fonts.googleapis.com/css2?family=Gloock&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MYHF4YMJ3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-MYHF4YMJ3Y');
</script>"""
LOGO = "ac-logo"
CTA_PATH = "#assessment"
CTA_LABEL = "Free Assessment"
CTA_TITLE = "We come out, look, and tell you what it needs."
CTA_TEXT = "The on-site assessment is free and there is no obligation. Call Dylan or Zac, or email Evans."
SIDE_TITLE = "Free on-site assessment. No charge for the visit."
PHONES = [("Dylan", "435-994-5235", "+14359945235"), ("Zac", "435-224-6987", "+14352246987")]
EMAIL = "evans@armour-crete.com"
HOURS = ""
ADDRESS = []
AREAS = ["St. George", "Kayenta", "Entrada", "Ivins", "Santa Clara", "Snow Canyon", "SunRiver", "Coral Canyon", "Green Springs", "Bloomington", "Washington", "Hurricane"]
SOCIAL = []
BLURB = "Concrete sealing, decorative finishes and foundation waterproofing for homes and builders across southern Utah. Licensed &amp; insured. Certified Deco applicator."
SVC_LABEL = "Services"
SVC = [("driveway-sealing/", "Driveway sealing", None), ("wet-look-concrete-sealing/", "Wet-look &amp; decorative", None), ("pool-deck-sealing/", "Pool decks &amp; salt", None),
       ("expansion-joint-replacement/", "Expansion joints", None), ("foundation-waterproofing/", "Foundation waterproofing", None), ("asphalt-sealing/", "Asphalt sealing", None)]
NAV = [("Products", "products/"), ("For Contractors", "contractors/"), ("Blog", "blog/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U.rstrip("/"), "telephone": "+1-435-994-5235", "email": EMAIL,
         "logo": U + "assets/img/ac-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "addressLocality": "St. George", "addressRegion": "UT", "addressCountry": "US"}}
    if full:
        n.update({"description": "Armour Crete seals concrete in St. George and Washington County, Utah: driveways, patios, pool decks, wet-look and decorative finishes, expansion joints, asphalt, and foundation waterproofing for new construction. Certified Deco applicator.",
                  "areaServed": [{"@type": "Place", "name": a + ", UT"} for a in AREAS]})
    return [n]
