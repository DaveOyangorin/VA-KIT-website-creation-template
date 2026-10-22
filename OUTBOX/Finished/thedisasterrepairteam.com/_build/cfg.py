"""thedisasterrepairteam.com: facts and settings (20 Oct 2026).
From the client's own site: Disaster Repair Team. Northern Utah 385-287-6344 (tel:+13852876344, "Available 24/7"); Southern Utah
(St. George) 435-619-9594. Office "45 South 2920 West, Lehi, UT 84043" (about page and footer). Stated on the site: Licensed &
Insured (B-100 General Contractor), Certified (IICRC), "Target 60-minute on-site response", free estimates, residential and
commercial, insurance support and documentation, "Over 20 Years of Experience", "4.9 · 120+ Google reviews".
Google profile (report): +1801-515-2257 and 441 W Main St Ste E, Lehi, UT 84043, 4.9 stars from 168 reviews: phone and address
differ from the site (flagged; the site's are used). Tracking kept: Google Analytics 4 G-ZQJHV4JHEF.
Photos: most images on the live site are AI-generated (several file names end in "-ai") and are not used. Only the real job
photos are: a fire-damaged ceiling, mold behind removed baseboard, a water-bulged ceiling, carpet pulled back after water, a
mold corner. The truck image may be a wrap mockup (not used; flagged)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "thedisasterrepairteam.com"
U = "https://thedisasterrepairteam.com/"
TRAIL = True
NAME = "Disaster Repair Team"
TODAY = "2026-10-20"
HOME_OG = "drt-ceiling"
THEME_COLOR = "#0e1116"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo+Black&family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
TRACK_HEAD = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ZQJHV4JHEF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-ZQJHV4JHEF');
</script>"""
LOGO = "drt-logo"
CTA_PATH = "request-help/"
CTA_LABEL = "Request Help"
CTA_TITLE = "Active damage? Call now. It&rsquo;s the fastest way."
CTA_TEXT = "Available 24/7 for Northern Utah and St. George. For contained damage, callbacks and estimates, send a request and the team will follow up as quickly as possible."
SIDE_TITLE = "Available 24/7. Target 60-minute on-site response."
PHONES = [("Northern Utah, 24/7", "385-287-6344", "+13852876344"), ("St. George", "435-619-9594", "+14356199594")]
EMAIL = ""
HOURS = "Available 24/7"
ADDRESS = [("Office", "45 South 2920 West<br>Lehi, UT 84043")]
AREAS = ["Salt Lake County", "Utah County", "Davis County", "Weber County", "Box Elder County", "Summit County", "Tooele County", "Wasatch County", "Juab County", "Washington County", "Iron County"]
SOCIAL = []
BLURB = "Water, fire, smoke and mold restoration, plus foundation, insulation and commercial work, across Northern Utah and St. George. Licensed &amp; insured (B-100). IICRC certified."
SVC_LABEL = "Services"
SVC = [("water-damage-cleanup-restoration/", "Water damage", None), ("fire-damage-cleanup-restoration/", "Fire damage", None), ("smoke-damage-cleanup-restoration/", "Smoke damage", None),
       ("mold-remediation-restoration/", "Mold remediation", None), ("sewage-cleanup/", "Sewage cleanup", None), ("foundation-repair/", "Foundation repair", None),
       ("insulation-services/", "Insulation", None), ("commercial-restoration/", "Commercial restoration", None)]
NAV = [("Areas", "landing-pages/"), ("Blog", "blog/"), ("About", "about-us/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13852876344",
         "logo": U + "assets/img/drt-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "45 South 2920 West", "addressLocality": "Lehi", "addressRegion": "UT", "postalCode": "84043", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}]}
    if full:
        n.update({"description": "Disaster Repair Team provides water, fire, smoke and mold restoration in Lehi and across Northern Utah and St. George, with sewage cleanup, foundation crack and leak repair, insulation and commercial restoration. B-100 licensed and IICRC certified.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": a + ", UT"} for a in AREAS]})
    return [n]
