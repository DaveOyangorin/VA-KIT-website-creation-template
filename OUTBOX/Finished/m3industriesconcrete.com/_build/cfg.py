"""m3industriesconcrete.com: facts and settings (20 Oct 2026).
From the client's own site: M3 Industries (concrete contractor), St. George, UT. Phone (435) 701-0081 (tel 4357010081);
m3industriesconcrete@gmail.com; address "2570 South 3430 East, St. George, UT, USA" (Wix service pages). Licensed & insured in
Utah (FAQ). Areas: St. George, Washington, Santa Clara, Ivins, Hurricane and surrounding Southern Utah (FAQ). Experience: "over
20 years" (foundations pages) vs "25+ yrs exp" (home meta): flagged; "over 20 years" used. Coatings: NexaNano SiO2 sealer.
Report: no Google profile found. The live home page shows "5.0 ... Based on Google Reviews": not shown (no profile to check).
The live contact page and several page footers still show the Wix template placeholder ("500 Terry Francine St., San
Francisco", 123-456-7890, info@mysite.com): never used; flagged. Tracking kept: Google Analytics 4 G-RM58WGPQMM.
Photos: many images on the live site look AI-generated (red-rock scenes with workers, logo-stamped cleaning photos, patio
renders): not used. Only the client's phone-camera job photos are."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "m3industriesconcrete.com"
U = "https://www.m3industriesconcrete.com/"
TRAIL = False
NAME = "M3 Industries"
TODAY = "2026-10-20"
HOME_OG = "m3-pour-crew"
THEME_COLOR = "#1f2326"
FONTS = "https://fonts.googleapis.com/css2?family=Anton&family=Work+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RM58WGPQMM"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-RM58WGPQMM');
</script>"""
LOGO = "m3-logo"
CTA_PATH = "inquiry-services-page/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Get a free estimate in St. George."
CTA_TEXT = "Call (435) 701-0081 or send the form for a free, no-obligation quote. Spring and summer fill quickly, so contact us a few weeks ahead when you can."
SIDE_TITLE = "Free, no-obligation quotes across Southern Utah."
PHONES = [("Call", "(435) 701-0081", "+14357010081")]
EMAIL = "m3industriesconcrete@gmail.com"
HOURS = ""
ADDRESS = [("Office", "2570 South 3430 East<br>St. George, UT")]
AREAS = ["St. George", "Washington", "Santa Clara", "Ivins", "Hurricane"]
SOCIAL = []
BLURB = "Concrete driveways, patios, stamped concrete, retaining walls, pads and slabs, foundations, coatings and sealing across St. George and Southern Utah. Licensed &amp; insured."
SVC_LABEL = "Services"
SVC = [("concrete-driveway-patio/", "Driveways &amp; patios", None), ("concrete-coatings-st-george/", "Coatings &amp; sealing", None), ("stamped-decorative-concrete/", "Stamped &amp; decorative", None),
       ("retaining-walls/", "Retaining walls", None), ("concrete-pads-slabs/", "Pads &amp; slabs", None), ("concrete-foundations/", "Foundations", None),
       ("concrete-sidewalks-walkways/", "Sidewalks &amp; walkways", None), ("concrete-cleaning-st-george/", "Concrete cleaning", None)]
NAV = [("All services", "concrete-services-st-george/"), ("FAQs", "faqs/"), ("Blog", "blog/"), ("Contact", "contact-5/")]


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "GeneralContractor"], "@id": U + "#business", "name": NAME, "url": U.rstrip("/"), "telephone": "+14357010081", "email": EMAIL,
         "logo": U + "assets/img/m3-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "2570 South 3430 East", "addressLocality": "St. George", "addressRegion": "UT", "addressCountry": "US"}}
    if full:
        n.update({"description": "M3 Industries is a concrete contractor in St. George, Utah: driveways, patios, stamped and decorative concrete, retaining walls, pads and slabs, foundations, sidewalks, concrete coatings, sealing and cleaning.",
                  "areaServed": [{"@type": "City", "name": a + ", UT"} for a in AREAS]})
    return [n]
