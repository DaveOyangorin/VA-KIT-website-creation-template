"""swiftrestoreutah.com: facts and settings (20 Oct 2026).
Swift Restoration and Remodeling, Ogden. From the client's contact page: Office 2900 Pennsylvania Ave, Unit C, Ogden, UT 84401;
phone +13854128633 (shown on the site as (385) 412-8633; Google: +1385-412-8633); Hours: 24/7 Emergency Services; Contractor
License Numbers: 4853926-5501. About page: locally owned, serving the community since 2009; "over 13 years of experience in
restoration, and over 30 years of experience in construction". The home page CTA also shows (385) 402-8536 (flagged).
Financing through Hearth (their own embed). Owner/author: Darin Jenks. Google: 4.6 stars from 179 reviews (report), not shown
until confirmed. Tracking kept: Google Tag Manager GTM-KKGCS6ND (the client's container). The UA-228094282-1 gtag on the live
site is injected by the Duda site builder and is not carried over."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "swiftrestoreutah.com"
U = "https://www.swiftrestoreutah.com/"
TRAIL = False
NAME = "Swift Restoration and Remodeling"
TODAY = "2026-10-20"
HOME_OG = "basement-drying"
THEME_COLOR = "#0a1220"
FONTS = "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fraunces:ital,opsz,wght@1,9..144,400;1,9..144,600&family=DM+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KKGCS6ND');</script>
<!-- End Google Tag Manager -->"""
LOGO = "swift-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Get a Quote"
CTA_TITLE = "Water in the house? Call now."
CTA_TEXT = "24/7 emergency service from our Ogden office: water, fire, mold and sewage, then the rebuild and remodel, with one crew from first call to final finish."
SIDE_TITLE = "One crew from the first call to the final finish."
PHONES = [("24/7 emergency", "(385) 412-8633", "+13854128633")]
EMAIL = ""
HOURS = "24/7 emergency service"
ADDRESS = [("Office", "2900 Pennsylvania Ave, Unit C<br>Ogden, UT 84401")]
AREAS = ["Ogden", "Layton", "Kaysville", "Farmington", "Bountiful", "North Salt Lake", "Roy", "Harrisville", "Huntsville", "West Haven", "Plain City", "Brigham City"]
SOCIAL = []
BLURB = "Locally owned in Ogden since 2009: water, fire and mold restoration, then the rebuild and the remodel. Contractor license 4853926-5501."
SVC_LABEL = "Services"
SVC = [("services/water-damage-restoration/", "Water damage restoration", None), ("services/flooded-basement-cleanup/", "Flooded basement cleanup", None), ("services/fire-damage-restoration/", "Fire damage restoration", None),
       ("services/ogden-mold-removal/", "Mold removal", None), ("services/ogden-sewage-cleanup/", "Sewage cleanup", None), ("services/leak-detection/", "Leak detection", None),
       ("services/boardup-services/", "Board-up", None), ("services/kitchen-remodeling/", "Kitchen remodeling", None), ("services/bathroom-remodeling/", "Bathroom remodeling", None),
       ("services/reconstruction/", "Reconstruction", None), ("services/commercial-damage-restoration/", "Commercial restoration", None), ("services/insurance-claims-restoration-ogden/", "Insurance claims", None)]
NAV = [("Our Work", "case-studies/"), ("Service Areas", "service-areas/"), ("Tips", "restoration-tips/"), ("About", "about-us/"), ("Contact", "contact/")]
ST = {"street": "2900 Pennsylvania Ave, Unit C", "city": "Ogden", "zip": "84401", "license": "4853926-5501", "tel": "+13854128633", "phone": "(385) 412-8633"}


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "url": U, "telephone": ST["tel"],
         "logo": U + "assets/img/swift-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "foundingDate": "2009",
         "address": {"@type": "PostalAddress", "streetAddress": ST["street"], "addressLocality": "Ogden", "addressRegion": "UT", "postalCode": ST["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}]}
    if full:
        n.update({"description": "Swift Restoration and Remodeling is a locally owned restoration and remodeling company in Ogden, Utah, serving the community since 2009: 24/7 water, fire, mold and sewage restoration, reconstruction, and kitchen and bathroom remodeling.",
                  "founder": {"@type": "Person", "name": "Darin Jenks"}, "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
