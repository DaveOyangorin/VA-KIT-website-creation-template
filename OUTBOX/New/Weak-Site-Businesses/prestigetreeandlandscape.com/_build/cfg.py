"""prestigetreeandlandscape.com: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (23 Oct 2026) of the 35 sitemap URLs (plain PHP site; http, .php file URLs; no canonicals). The home page renders only the
menu (blank in Chrome); every inner page has content. Same URLs. testimonials.php returned a server error and is not rebuilt.
From the site: Prestige Tree And Landscape; family-owned; "My father started this business in 1978"; founder credentials page (Certified
Arborist / Certified Tree Worker, 32 years in tree care, youngest certified arborist in Utah at age 21 (1997), personally planted over
12,500 trees, Sterling J. Morton Society Medal / J. Sterling Morton Award, Arbor Day Award for Tree Stewardship, Honorary Life Member of the
National Arbor Day Foundation, Utah Community Forest Council member for 20 years, city arborist for the Daybreak community, Kauai winter
arborist 2009 to present, Kalihiwai Ridge project 2016-2017); tree and landscape service pages; Draper and Holladay area pages; hours
Mon-Fri 9AM-6PM, Sat-Sun by appointment; 801.859.9786; service@prestigetreeandlandscape.com; three short testimonials.
NAP: Google listing 4780 S Commerce Dr, Murray, UT 84107, +1801-859-9786 (used, copied exactly). The site gives only "Murray, Utah 84107-3752".
Conflicts flagged: certified in 1996 (certified-arborist page) vs 1997 (credentials page); the About page says "residents of Sandy" while the
business is in Murray and the service pages say Draper and Holladay. Left out until confirmed: "Businessman of the Year 2003 - Wall Street
Journal", "Lightning Protection installed for Disney Productions", "One of the World's most dangerous tree jobs", and the 4.4 / 350 rating.
Photos: the arborist's own photos (crane removals, rigging, climbing, Kauai trees) are used; the big slider photos and service tiles are stock
and not used. Banner: credited Wikimedia Commons photo of Big Cottonwood Canyon in fall."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "prestigetreeandlandscape.com"
U = "https://prestigetreeandlandscape.com/"
TRAIL = False
NAME = "Prestige Tree And Landscape"
TODAY = "2026-10-23"
HOME_OG = "pt-hero"
THEME_COLOR = "#1f2b21"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Outfit:wght@400;500;600;700&family=Spline+Sans+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "pt-logo"
CTA_PATH = "contact-us.php/"
CTA_LABEL = "Free consultation"
CTA_TITLE = "Talk to a certified arborist, <em>not a salesman.</em>"
CTA_TEXT = "Call 801.859.9786, Monday to Friday 9 to 6 (weekends by appointment), or email service@prestigetreeandlandscape.com for a free consultation."
SIDE_TITLE = "Family-owned since 1978. Certified arborist."
PHONES = [("Call", "801.859.9786", "+18018599786")]
EMAIL = "service@prestigetreeandlandscape.com"
HOURS = "Mon&ndash;Fri 9AM&ndash;6PM &middot; Sat&ndash;Sun by appointment"
ADDRESS = [("Murray", "4780 S Commerce Dr<br>Murray, UT 84107")]
AREAS = ["Murray", "Holladay", "Draper", "Sandy", "the Salt Lake Valley"]
SOCIAL = []
BLURB = "Family-owned tree care and landscaping since 1978, led by a certified arborist: tree pruning, removal, cabling, plant health, landscaping and hardscaping."
SVC_LABEL = "Tree services"
SVC = [("tree-pruning.php/", "Tree pruning &amp; trimming", None), ("stump-and-tree-removal.php/", "Stump &amp; tree removal", None), ("emergency-tree-removal.php/", "Emergency tree removal", None),
       ("tree-cabling-and-bracing.php/", "Cabling &amp; bracing", None), ("tree-health.php/", "Tree health", None), ("tree-planting.php/", "Tree planting", None),
       ("lightning-protection.php/", "Lightning protection", None), ("land-clearing.php/", "Land clearing", None)]
NAV = [("Landscaping", "landscaping.php/"), ("Credentials", "credentials-awards.php/"), ("About", "about-us.php/"), ("Contact", "contact-us.php/")]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18018599786", "email": EMAIL,
         "logo": U + "assets/img/pt-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "4780 S Commerce Dr", "addressLocality": "Murray", "addressRegion": "UT", "postalCode": "84107", "addressCountry": "US"}}
    if full:
        n.update({"description": "Family-owned tree service and landscaping in Murray, Utah since 1978, led by a certified arborist: pruning, removal, cabling and bracing, tree health, planting, landscaping and hardscaping.",
                  "foundingDate": "1978",
                  "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"},
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in ("Murray", "Holladay", "Draper", "Sandy", "Cottonwood Heights", "Midvale")]})
    return [n]
