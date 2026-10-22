"""poly-lift.com: facts and settings (20 Oct 2026).
From the client's own site: Poly-Lift (Poly-Lift Concrete Lifting and Piering), Logan, UT. Cache location (435) 999-9309,
PolyLiftUtah@gmail.com; Weber location (801) 530-5617, PolyLiftWeber@gmail.com. Address: the footer and Google say
"715 W 1725 N, Logan, UT 84341"; the contact page says "715 N 1725 W" (flagged; the footer/Google form is used). Hours Mo-Fr
7:00 AM - 5:00 PM. Deep Foamjection (HMI foam) concrete lifting, concrete sealing, foundation repair (push piers and helical
piles, partnered with Magnum Piering), Core Foam Masonry Foam Insulation(R). Projects named on the site: Weber State University,
Utah State University, the Utah stadium, residential, a lifted garage. Clay Ogden is quoted on the reviews page.
Google: 4.6 stars from 14 reviews (report): not shown until confirmed. Tracking kept: Google Tag Manager GTM-PM5FXG3.
Left out until confirmed: superlatives ("the best on the market", "no one does it better", "state-of-the-art"), the "Trusted
and Certified" badge strip. Stock photos (Ukraine, city landmarks, an insurance policy) are not used; job photos and the
manufacturer's pier diagrams are."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "poly-lift.com"
U = "https://www.poly-lift.com/"
TRAIL = True
NAME = "Poly-Lift"
TODAY = "2026-10-20"
HOME_OG = "pl-poly-lift-crewman-injecting-deepfoam-into-concrete-walkway"
THEME_COLOR = "#14211c"
FONTS = "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800;900&family=Manrope:wght@400;500;600;700&family=Red+Hat+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PM5FXG3');</script>
<!-- End Google Tag Manager -->"""
LOGO = "pl-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Concrete sinking? Foundation settling? Get a free estimate."
CTA_TEXT = "Call the Cache location or the Weber location, Monday to Friday, 7 a.m. to 5 p.m. Most concrete lifting jobs are done in less than a day and ready to use immediately."
SIDE_TITLE = "Most lifting jobs: less than a day, ready to use immediately."
PHONES = [("Cache location", "(435) 999-9309", "+14359999309"), ("Weber location", "(801) 530-5617", "+18015305617")]
EMAIL = "polyliftutah@gmail.com"
HOURS = "Mon&ndash;Fri 7:00 AM&ndash;5:00 PM"
ADDRESS = [("Office", "715 W 1725 N<br>Logan, UT 84341")]
AREAS = ["Logan", "Cache County", "Smithfield", "Davis County", "Layton", "Syracuse", "St. George"]
SOCIAL = []
BLURB = "Concrete lifting with Deep Foamjection polyurethane foam, foundation repair with push piers and helical piles, concrete sealing and Core Foam Masonry Foam Insulation&reg;. Logan and across Utah."
SVC_LABEL = "Services"
SVC = [("concrete-leveling-and-lifting/", "Concrete leveling &amp; lifting", None), ("foundation-repair/", "Foundation repair", None), ("foundation-repair/push-piering/", "Push piers", None),
       ("foundation-repair/helical-piles/", "Helical piles", None), ("concrete-sealing/", "Concrete sealing", None), ("injection-foam-insulation/", "Core Foam Masonry Foam Insulation&reg;", None)]
NAV = [("Projects", "completed-projects/"), ("Areas", "service-areas/"), ("FAQs", "faqs/"), ("Blog", "blog/")]


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "url": U, "telephone": "+14359999309", "email": EMAIL,
         "logo": U + "assets/img/pl-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "715 W 1725 N", "addressLocality": "Logan", "addressRegion": "UT", "postalCode": "84341", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Poly-Lift is a concrete lifting and foundation repair contractor in Logan, Utah: Deep Foamjection polyurethane foam concrete lifting, push piers and helical piles, concrete sealing and Core Foam Masonry Foam Insulation.",
                  "areaServed": [{"@type": "Place", "name": a + ", UT"} for a in AREAS]})
    return [n]
