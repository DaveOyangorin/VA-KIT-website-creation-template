"""danielswildlife.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 18 sitemap URLs (Squarespace on the www host, no trailing slash; the home page also answers at /home).
From the site: Daniel's Wildlife & Pest; owner-operated ("I am the owner and the technician on every job"); over eight years of hands-on
experience; "thousands of pest and wildlife cases"; fully licensed and insured; open 24/7; call or text (801) 783-9638; serves Northern
Utah and the Salt Lake Valley; integrated pest management approach; 14 service pages (bats, birds incl. solar panel bird exclusion and
netting, gophers, insects incl. bed bugs, cockroaches, wasps, mice, raccoons, rats, skunks, snakes, squirrels, voles, termites, cleanup &
sanitization, dead animal removal).
NAP: Google listing 6870 S Village Green Rd, Cottonwood Heights, UT 84121, +1801-783-9638 (used, copied exactly). The site shows only
"Northern Utah" as a location.
Left out until confirmed: the 5-star / 198-review rating (not on the site).
Photos: their own job photos (raccoons and squirrels in traps, entry holes, droppings, attic and crawlspace cleanup, bird netting, solar
panel work, gopher mounds, vole damage, termites, wasp nest, snake). Not used: daniel.png, back.png and squirrel.png (1536/1024 sizes typical
of generated images), skunk.jpg (looks like stock) and the dog portrait."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "danielswildlife.com"
U = "https://www.danielswildlife.com/"
TRAIL = False
NAME = "Daniel's Wildlife & Pest Control"
TODAY = "2026-10-22"
HOME_OG = "dw-hero"
THEME_COLOR = "#1e4a32"
FONTS = "https://fonts.googleapis.com/css2?family=Bitter:wght@600;700;800&family=Karla:wght@400;500;600;700&family=Courier+Prime:wght@400;700&display=swap"
TRACK_HEAD = ""
LOGO = "dw-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Call or text 24/7"
CTA_TITLE = "Something in the attic? <em>Call the owner.</em>"
CTA_TEXT = "Call or text (801) 783-9638, any hour. You'll deal directly with the person responsible for the job, from inspection to the last sealed gap."
SIDE_TITLE = "Owner-operated. Licensed, insured, open 24/7."
PHONES = [("Call or text", "(801) 783-9638", "+18017839638")]
EMAIL = ""
HOURS = "Open 24/7"
ADDRESS = [("Cottonwood Heights", "6870 S Village Green Rd<br>Cottonwood Heights, UT 84121")]
AREAS = ["Cottonwood Heights", "the Salt Lake Valley", "Northern Utah"]
SOCIAL = []
BLURB = "Owner-operated wildlife removal and pest control in Cottonwood Heights, the Salt Lake Valley and Northern Utah. Licensed, insured, open 24/7."
SVC_LABEL = "Animals &amp; services"
SVC = [("raccoons/", "Raccoons", None), ("squirrels/", "Squirrels", None), ("bats/", "Bats", None), ("birds/", "Birds &amp; solar panels", None), ("skunks/", "Skunks", None),
       ("snakes/", "Snakes", None), ("mice/", "Mice", None), ("rats/", "Rats", None), ("gophers/", "Gophers", None), ("voles/", "Voles", None), ("insects/", "Insects", None),
       ("termites/", "Termites", None), ("cleanup-sanitization/", "Cleanup &amp; sanitization", None), ("dead-animal-removal/", "Dead animal removal", None)]
NAV = [("All services", "services/"), ("About", "about/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18017839638",
         "logo": U + "assets/img/dw-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "6870 S Village Green Rd", "addressLocality": "Cottonwood Heights", "addressRegion": "UT", "postalCode": "84121", "addressCountry": "US"}}
    if full:
        n.update({"description": "Owner-operated, licensed and insured wildlife removal, exclusion and pest control for homes and commercial properties in Cottonwood Heights, the Salt Lake Valley and Northern Utah. Open 24/7.",
                  "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"},
                  "areaServed": [{"@type": "City", "name": "Cottonwood Heights, UT"}, {"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}, {"@type": "Place", "name": "Northern Utah"}]})
    return [n]
