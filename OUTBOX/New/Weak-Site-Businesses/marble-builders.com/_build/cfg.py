"""marble-builders.com: facts and settings (23 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: the live site shows a hosting "Account Suspended" page (21 Oct) / a Cloudflare challenge (23 Oct), so content comes from the Internet
Archive's most recent real captures of each page (March-September 2025; later captures are Cloudflare challenge pages). WordPress, trailing
slashes. Same URLs. Some mid-2025 posts were only captured behind the challenge and can't be recovered; project photos were not archived.
From the site: Marble Builders; remodeling services in Boise, Denver, Kansas City, Salt Lake City and Dallas (Las Vegas on the contact and
locations pages); "With over 20 years of experience serving our communities"; Utah team "located in Riverton, Utah", serving "anywhere from
Payson to Ogden"; services: custom homes, property repairs, commercial development, remodels (kitchens, bathrooms, basements, mother-in-law
apartments); insurance and restoration rebuild partner (blog posts); three-step process; quality guarantee; business hours M-F 9am-5pm;
info@marble-builders.com; city phone numbers (contact page); two Utah project posts (Bountiful main-level remodel, Farmington bathroom);
reviews quoted on the about, locations and Salt Lake City pages (names as shown).
NAP: Google listing Marble Builders, 12166 S Redwood Rd, Riverton, UT 84065, +1801-828-5540 (used, copied exactly; matches the contact page's
Salt Lake City number). The site also shows 385-644-6304 (home header) and 888-973-3212 (home meta): flagged.
Left out: the service pages' FAQ blocks (copied "Marble Homes ... custom home builders" text on every page), WordPress demo pages
(salient-architect-*, sample-page, example project), the 4.6 / 198 rating.
Photos: none of their own survived in the archive except the logos. Banner: credited Wikimedia Commons photo of Lone Peak's granite."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "marble-builders.com"
U = "https://marble-builders.com/"
TRAIL = True
NAME = "Marble Builders"
TODAY = "2026-10-23"
HOME_OG = "mb-hero"
THEME_COLOR = "#1a1a1c"
FONTS = "https://fonts.googleapis.com/css2?family=Gloock&family=Inter+Tight:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap"
TRACK_HEAD = ""
LOGO = "mb-logo"
CTA_PATH = "getquote/"
CTA_LABEL = "Get a quote"
CTA_TITLE = "From the first call <em>to the final finish.</em>"
CTA_TEXT = "Call 801-828-5540 or email info@marble-builders.com. A representative will reach out within 24 hours, Monday to Friday 9am-5pm."
SIDE_TITLE = "Remodels, repairs and insurance rebuilds."
PHONES = [("Call", "801-828-5540", "+18018285540")]
EMAIL = "info@marble-builders.com"
HOURS = "M&ndash;F 9am&ndash;5pm"
ADDRESS = [("Riverton", "12166 S Redwood Rd<br>Riverton, UT 84065")]
AREAS = ["Riverton", "the Wasatch Front from Payson to Ogden"]
SOCIAL = [("Facebook", "https://www.facebook.com/people/Marble-Builders/61560827575573/"), ("Instagram", "https://www.instagram.com/marble.builders/"), ("LinkedIn", "https://www.linkedin.com/company/marble-builders/"), ("Pinterest", "https://www.pinterest.com/marblebuilders/")]
BLURB = "Marble Builders: remodels, property repairs, insurance rebuilds, custom homes and commercial development, from Riverton across the Wasatch Front and in five other metros."
SVC_LABEL = "Services"
SVC = [("remodels-service-page/", "Remodels", None), ("property-repairs-service-page/", "Property repairs &amp; rebuilds", None), ("custom-homes-service-page/", "Custom homes", None),
       ("commercial-development-service-page/", "Commercial development", None), ("services/", "All services", None)]
NAV = [("Insurance rebuilds", "#rebuild"), ("Locations", "locations/"), ("Blog", "blog/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "GeneralContractor", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18018285540", "email": EMAIL,
         "logo": U + "assets/img/mb-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "12166 S Redwood Rd", "addressLocality": "Riverton", "addressRegion": "UT", "postalCode": "84065", "addressCountry": "US"}}
    if full:
        n.update({"description": "Riverton, Utah general contractor: kitchen, bathroom and basement remodels, property repairs and insurance rebuilds after water or fire damage, custom homes and commercial development.",
                  "sameAs": [u for l, u in SOCIAL],
                  "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"},
                  "areaServed": [{"@type": "City", "name": c} for c in ("Riverton, UT", "Salt Lake City, UT", "Boise, ID", "Denver, CO", "Dallas, TX", "Kansas City, MO", "Las Vegas, NV")]})
    return [n]
