"""actionyardcare.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 4 sitemap URLs (Squarespace on www, no trailing slash; the home page also answers at /home).
From the site: Action Lawn & Yardcare (logo: "Action Lawn & Yard Care"); "experienced landscape professionals serving the Salt Lake Valley";
"a group of licensed & insured professionals with decades of experience"; services list in three groups (Landscaping: sod, mulch/rocks,
flagstone, planting, edging, new landscaping and renovation; Maintenance: weekly lawn mowing with string trimming and edging, yard clean
ups, tree/bush trimming, leaf clean up, snow removal, aeration, fertilizing, lawn treatment programs, flower bed treatment programs,
landscape pest treatments, weed management; Sprinklers: start up and shut down, new system installation, system check ups, repair);
801-244-4035; info@actionyardcare.com; Facebook and Instagram.
NAP: Google listing "Action Lawn and Yard", 6501 S Cottonwood St, Murray, UT 84107, +1801-244-4035 (used, copied exactly). The site gives
no address and calls itself "Action Lawn & Yardcare".
Left out until confirmed: "one of the highest rated landscaping companies in Utah" and the 4.7 / 187 Google rating.
Photos: their three crew photos (sprinkler line trench, planting, leaf cleanup). The 300 px lawn background is too small to use."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "actionyardcare.com"
U = "https://www.actionyardcare.com/"
TRAIL = False
NAME = "Action Lawn & Yardcare"
TODAY = "2026-10-22"
HOME_OG = "ay-trench"
THEME_COLOR = "#111411"
FONTS = "https://fonts.googleapis.com/css2?family=Graduate&family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap"
TRACK_HEAD = ""
LOGO = "ay-logo"
CTA_PATH = "contact-us/"
CTA_LABEL = "Get a quote"
CTA_TITLE = "Put Action <em>on your yard.</em>"
CTA_TEXT = "Call 801-244-4035 or email info@actionyardcare.com. Landscaping, maintenance and sprinklers across the Salt Lake Valley."
SIDE_TITLE = "Licensed &amp; insured. Decades of experience."
PHONES = [("Call", "801-244-4035", "+18012444035")]
EMAIL = "info@actionyardcare.com"
HOURS = ""
ADDRESS = [("Murray", "6501 S Cottonwood St<br>Murray, UT 84107")]
AREAS = ["Murray", "the Salt Lake Valley"]
SOCIAL = [("Facebook", "https://www.facebook.com/actionyardcare"), ("Instagram", "https://www.instagram.com/actionyardcare/")]
BLURB = "Licensed and insured landscape professionals with decades of experience: landscaping, lawn and yard maintenance, and sprinklers in Murray and the Salt Lake Valley."
SVC_LABEL = "Services"
SVC = [("services/", "Landscaping", None), ("services/", "Lawn &amp; yard maintenance", None), ("services/", "Sprinklers", None)]
NAV = [("Services", "services/"), ("About", "about/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": "Action Lawn and Yard", "alternateName": "Action Lawn & Yardcare", "url": U, "telephone": "+18012444035", "email": EMAIL,
         "logo": U + "assets/img/ay-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "6501 S Cottonwood St", "addressLocality": "Murray", "addressRegion": "UT", "postalCode": "84107", "addressCountry": "US"}}
    if full:
        n.update({"description": "Licensed and insured landscaping, lawn and yard maintenance, snow removal and sprinkler service in Murray and the Salt Lake Valley.",
                  "sameAs": [u for l, u in SOCIAL], "areaServed": [{"@type": "City", "name": "Murray, UT"}, {"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}]})
    return [n]
