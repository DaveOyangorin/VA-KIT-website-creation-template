"""ezelectric.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 6 sitemap pages (21 Oct 2026), same URLs (trailing slash) and canonicals.
From the site's own pages: phone (385) 284-0394 (header, contact page, service pages; tel 13852840394); a second number (385) 220-7815
appears in the home footer and the accessibility statement and is the one on Google (report). Shown: 284-0394 as the main number,
220-7815 flagged for the client to choose. info@ezelectric.com; hours Monday-Friday 8 AM-6 PM, closed Saturdays and Sundays; areas:
Utah County and Salt Lake County; licensed electricians; free quotes; free in-person consultation (on-site inspection with a safety check
and load analysis) and a zero-cost evaluation; fast responses and upfront pricing; residential, commercial and outdoor & specialty
services as listed on each page. Three Google reviews quoted word for word; the third's "CEO, Acme Industries" label is a template
placeholder and is dropped (name kept).
Left out until confirmed: "over 15 years", "top-rated", "Quality Work, Guaranteed", "certified electricians" (licensed is kept).
Google listing (report): EZ Electric, +1385-220-7815, no address (service-area business), 4.9 stars from 641 reviews (not shown).
No tracking tags found on the live site.
Photos: only their own (landscape lighting at dusk with the Wasatch behind, a technician in an EZ shirt running conduit in American Fork,
panel work at a brick home). Stock multimeter/hard-hat/pool/breaker photos (incl. two Unsplash files) are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "ezelectric.com"
U = "https://ezelectric.com/"
TRAIL = True
NAME = "EZ Electric"
TODAY = "2026-10-21"
HOME_OG = "ez-landscape-lighting"
THEME_COLOR = "#0b1220"
FONTS = "https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Albert+Sans:ital,wght@0,400;0,500;0,600;0,700;1,500&family=DM+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "ez-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Request an Estimate"
CTA_TITLE = "Need an electrician? Let&rsquo;s get you powered up."
CTA_TEXT = "Call (385) 284-0394 or request an estimate. Free quotes and a free in-person consultation, Monday to Friday, 8 AM to 6 PM."
SIDE_TITLE = "Free quote. Free in-person consultation."
PHONES = [("Call", "(385) 284-0394", "+13852840394")]
EMAIL = "info@ezelectric.com"
HOURS = "Monday &ndash; Friday: 8 AM &ndash; 6 PM &middot; Closed Saturdays &amp; Sundays"
ADDRESS = []
AREAS = ["Salt Lake County", "Utah County"]
SOCIAL = [("Facebook", "https://www.facebook.com/ezelectricutah/"), ("Instagram", "https://www.instagram.com/ezelectricutah/"),
          ("LinkedIn", "https://www.linkedin.com/company/ez-electric-utah")]
BLURB = "Residential and commercial electricians serving Salt Lake County and Utah County. Repairs, installations, upgrades and remodels, with free quotes and upfront pricing."
SVC_LABEL = "Services"
SVC = [("residential-services/", "Residential", None), ("commercial-services/", "Commercial", None), ("outdoor-specialty-electrical-services/", "Outdoor &amp; Specialty", None)]
NAV = [("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "Electrician", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+13852840394", "email": EMAIL,
         "logo": U + "assets/img/ez-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "sameAs": [s[1] for s in SOCIAL],
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"}]}
    if full:
        n.update({"description": "EZ Electric provides residential, commercial and outdoor electrical services across Salt Lake County and Utah County: repairs, installations, panel upgrades, EV chargers, lighting, generators and remodels.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}, {"@type": "AdministrativeArea", "name": "Utah County, UT"}]})
    return [n]
