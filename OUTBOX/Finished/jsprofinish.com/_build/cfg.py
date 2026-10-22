"""jsprofinish.com: facts and settings (20 Oct 2026).
From the client's own site: JS ProFinish, basement finishing contractor; 1740 S 300 W #8, Clearfield, UT 84015; (385) 626-3514
(+13856263514); jsprofinish@gmail.com; Mon-Fri 8am-5pm, closed weekends; UT Lic. #11152584-5501 (S220 carpentry and flooring,
S270 drywall, paint, and plaster); owner Pablo J. Padilla; since 2019; licensed & insured; Davis and Weber Counties.
The site states "Rated 4.8 out of 5 from 18 Google reviews, as of September 2026" and quotes three named Google reviews.
The report's Google profile is a different business ("Vista Concrete Construction", Ogden, +1385-644-6281, 5 stars from 45):
flagged for Angelo, not used anywhere on the site.
Tracking kept: the Google Ads tag AW-17847227430 (gtag), as on the live site."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "jsprofinish.com"
U = "https://jsprofinish.com/"
TRAIL = False
NAME = "JS ProFinish"
TODAY = "2026-10-20"
HOME_OG = "basement1"
THEME_COLOR = "#1d1a17"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Newsreader:ital,opsz,wght@1,6..72,400;1,6..72,500&family=JetBrains+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17847227430"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-17847227430');
</script>"""
LOGO = "jsp-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Tell us about your basement."
CTA_TEXT = "We come out, measure, and put a written estimate in your hands, free, with the price fixed before work starts. We call back within one business day."
SIDE_TITLE = "Free written estimate. Price fixed before we start."
PHONES = [("Call", "(385) 626-3514", "+13856263514")]
EMAIL = "jsprofinish@gmail.com"
HOURS = "Mon&ndash;Fri 8am&ndash;5pm &middot; Closed weekends"
ADDRESS = [("Shop", "1740 S 300 W #8<br>Clearfield, UT 84015")]
AREAS = ["Clearfield", "Layton", "Kaysville", "Syracuse", "Farmington", "Bountiful", "Ogden", "Roy", "North Ogden", "South Ogden", "Pleasant View", "Harrisville"]
SOCIAL = []
BLURB = "Basement finishing in Davis and Weber County since 2019. Our own crew for framing, drywall, carpentry, paint and flooring. Licensed &amp; insured, UT Lic. #11152584-5501."
SVC_LABEL = "Services"
SVC = [("services/basement-remodeling/", "Basement remodeling", None), ("services/framing/", "Framing", None), ("services/drywall/", "Drywall", None),
       ("services/carpentry/", "Carpentry &amp; trim", None), ("services/painting/", "Painting", None), ("services/flooring/", "Flooring", None),
       ("services/bathroom-remodeling/", "Bathroom remodeling", None), ("basement-finishing-cost/", "Basement finishing cost", None)]
NAV = [("Projects", "projects/"), ("Gallery", "gallery/"), ("Areas", "davis-county/"), ("About", "about-us/")]
ST = {"street": "1740 S 300 W #8", "city": "Clearfield", "zip": "84015", "license": "11152584-5501", "tel": "+13856263514", "phone": "(385) 626-3514"}


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "url": U.rstrip("/"), "telephone": ST["tel"], "email": EMAIL,
         "logo": U + "assets/img/jsp-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "foundingDate": "2019",
         "address": {"@type": "PostalAddress", "streetAddress": ST["street"], "addressLocality": "Clearfield", "addressRegion": "UT", "postalCode": ST["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "JS ProFinish is a licensed and insured basement finishing contractor based in Clearfield, Utah, serving Davis and Weber County since 2019: basement finishing and remodeling, framing, drywall, carpentry and trim, painting, flooring and bathroom remodeling.",
                  "founder": {"@type": "Person", "name": "Pablo J. Padilla"}, "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
