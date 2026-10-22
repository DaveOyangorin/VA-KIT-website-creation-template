"""stgeorgehomeservices.com: facts and settings (20 Oct 2026).
From the client's own site: St. George Home Services, owner Ryan Nunez (holds the Utah license the company works under; the
number is given on request, as the site says). (435) 850-0053 (+14358500053; the Google profile matches: +1435-850-0053).
info@stgeorgehomeservices.com. "St. George, UT 84770. We come to you." (no street address on the site or Google: none shown).
Hours: 7 a.m. to 5 p.m. weekdays; emergency calls answered any hour, every day. Plain Terms: the quote is the number; diagnostic
fee $150 standard hours, $50 more evenings/weekends/holidays, credited if hired; one-year guarantee. Towns: St. George,
Washington, Hurricane, Santa Clara, Ivins, La Verkin, Toquerville, Cedar City (not Mesquite).
Google: 5 stars from 1 review (report): not shown. Tracking kept: Google Analytics 4 G-TVT7CYGXX6.
Photos: the client's own job photos only. The site's "brand" hero images (dusk street scenes, a duct render) and the
"illustration-*" lighting renders look generated and are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "stgeorgehomeservices.com"
U = "https://stgeorgehomeservices.com/"
TRAIL = False
NAME = "St. George Home Services"
TODAY = "2026-10-20"
HOME_OG = "work-bathroom-remodel-wide"
THEME_COLOR = "#171614"
FONTS = "https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,500;0,7..72,600;1,7..72,400;1,7..72,500&family=Archivo:wght@400;500;600;700&family=Spline+Sans+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-TVT7CYGXX6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-TVT7CYGXX6');
</script>"""
LOGO = "sghs-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Ask for a visit"
CTA_TITLE = "Call when you&rsquo;re ready. There&rsquo;s no charge to explain the options."
CTA_TEXT = "A person answers, 7 a.m. to 5 p.m. on weekdays, and emergency calls any hour, every day. The quote is the number. There is no second number."
SIDE_TITLE = "The quote is the number. There is no second number."
PHONES = [("Call", "(435) 850-0053", "+14358500053")]
EMAIL = "info@stgeorgehomeservices.com"
HOURS = "7 a.m. to 5 p.m. weekdays &middot; emergency calls any hour, every day"
ADDRESS = []
AREAS = ["St. George", "Washington", "Hurricane", "Santa Clara", "Ivins", "La Verkin", "Toquerville", "Cedar City"]
SOCIAL = []
BLURB = "Plumbing, heating and air, accessible living, water-wise landscape, concrete coatings and painting in St. George and Washington County. One quote that doesn&rsquo;t change."
SVC_LABEL = "What we do"
SVC = [("plumbing/", "Plumbing", None), ("hvac-st-george-ut/", "Heating and air", None), ("accessible-living/", "Accessible living", None), ("water-wise-landscape/", "Water-wise landscape", None),
       ("epoxy-flooring-st-george-ut/", "Concrete coatings", None), ("painting-st-george-ut/", "Painting", None), ("handyman-st-george-ut/", "Handyman", None), ("permanent-lighting-st-george-ut/", "Permanent lighting", None)]
NAV = [("Plain Terms", "plain-terms/"), ("Guides", "guides/"), ("Towns", "areas/"), ("About", "about/")]


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "Plumber"], "@id": U + "#business", "name": NAME, "url": U.rstrip("/"), "telephone": "+14358500053", "email": EMAIL,
         "logo": U + "assets/img/sghs-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "addressLocality": "St. George", "addressRegion": "UT", "postalCode": "84770", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "St. George Home Services: plumbing, heating and air, accessible living, water-wise landscape, concrete coatings, painting and permanent lighting in St. George and Washington County, Utah. Owner Ryan Nunez.",
                  "founder": {"@type": "Person", "name": "Ryan Nunez"}, "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
