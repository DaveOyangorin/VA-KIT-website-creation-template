"""anyandallservices.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 6 sitemap URLs (Wix on www, no trailing slash).
From the site: "Any & All Electric is now Any & All Services!"; "Need a electrician, not a salesman? At Any & All Services we connect Utah
homeowners with trusted local electricians. With over 14 years of local electrical experience, we know how to help you find the right
professional for your project. We handle the shopping around, saving you time and helping you move forward with confidence."; estimate
request form (first/last name, new or returning customer, phone, email, address, project description); office@anyandallservices.com.
Meta: "Serving Utah and Salt Lake Counties for over 13 years. Request an estimate for Electrical and HVAC" (13 vs 14 years: flagged).
NAP: Google listing "Any & All Services", +1801-717-9125, no address (service-area business; no address on the site, per the report).
IMPORTANT: the live copy describes a service that connects homeowners with electricians, not an electrician doing the work. The draft says
exactly that and flags it; the "electrician salt lake city" target from the report needs Angelo's call.
Left out until confirmed: the 4.8 / 165 rating. The four legal pages are unedited Wix templates: kept at their URLs, noindex, with a notice.
Photos: the site has none of its own work (brick textures, a lamp illustration). Banner is a credited Wikimedia Commons photo of Salt Lake
City at night."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "anyandallservices.com"
U = "https://www.anyandallservices.com/"
TRAIL = False
NAME = "Any & All Services"
TODAY = "2026-10-22"
HOME_OG = "aa-night"
THEME_COLOR = "#0e0e10"
FONTS = "https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Inter:wght@400;500;600;700&family=Share+Tech+Mono&display=swap"
TRACK_HEAD = ""
LOGO = "aa-logo"
CTA_PATH = "#estimate"
CTA_LABEL = "Request an estimate"
CTA_TITLE = "An electrician, <em>not a salesman.</em>"
CTA_TEXT = "Call 801-717-9125 or email office@anyandallservices.com. Tell us about the project and we'll help you find the right local professional."
SIDE_TITLE = "We handle the shopping around."
PHONES = [("Call", "801-717-9125", "+18017179125")]
EMAIL = "office@anyandallservices.com"
HOURS = ""
ADDRESS = []
AREAS = ["Salt Lake County", "Utah County"]
SOCIAL = []
BLURB = "Any & All Electric is now Any & All Services: connecting Utah homeowners with trusted local electricians, with over 14 years of local electrical experience."
SVC_LABEL = "Projects"
SVC = [("#panel", "Electrical projects", None), ("#panel", "Heating &amp; cooling (HVAC)", None), ("#estimate", "Request an estimate", None)]
NAV = [("How it works", "#how"), ("Your project", "#panel"), ("Blog", "signs-you-need-an-electrician/")]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18017179125", "email": EMAIL,
         "logo": U + "assets/img/aa-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp"}
    if full:
        n.update({"description": "Any & All Services (formerly Any & All Electric) connects Utah homeowners with trusted local electricians for electrical and HVAC projects in Salt Lake and Utah Counties.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}, {"@type": "AdministrativeArea", "name": "Utah County, UT"}]})
    return [n]
