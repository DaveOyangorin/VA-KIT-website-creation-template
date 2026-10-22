"""acs-hoa.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
REVIEWER NOTE (report): 3.2 stars from 406 reviews. A new site won't fix the rating: flag to Angelo before pitching. The domain says
"hoa": HOA management is likely the main business, so it leads here.
SOURCE: live crawl (21 Oct 2026): home, management-services.html, online-services.html, professional-services.html, about.html,
testimonials.html, service-areas.html, request-a-quote.html, same URLs (static .html files) with self-canonicals (the site had none).
/index.html is the same file as the home page; the two crawled 404 URLs (favicon.html, cdn-cgi email protection) are not pages.
From the site: toll-free 1-877-844-4227, info@acs-hoa.com and sales@acs-hoa.com (Cloudflare-encoded on the site), corporate office
2940 W Maple Loop Dr #102, Lehi, UT 84043 (matches Google), "Serving all of Utah, Washington, Idaho and Arizona", offices in Clearfield,
Lehi, Eagle Mountain, St. George and two in Park City (as listed, 2015-era site: confirm), the mission statement, the managerial,
online and professional service lists, Community Action Items, broadcasts, monthly board reporting, reserve analysis, separate bank
accounts per community, four HOA testimonials (word for word).
Google listing (report): +1801-641-1844 (local number, shown as the Lehi office line) and the same address; 3.2 stars (not shown).
Left out until confirmed: "patented" software, "premier HOA management services", "years of experience" claims, the in-house attorney
researching issues "for free".
Images: every photo on the site is stock (models, device mockups, generic houses), so none are used; the design is typographic."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "acs-hoa.com"
U = "https://acs-hoa.com/"
TRAIL = True
NAME = "Advanced Community Services"
TODAY = "2026-10-21"
HOME_OG = "acs-logo"
THEME_COLOR = "#362f4c"
FONTS = "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "acs-logo"
CTA_PATH = "request-a-quote.html"
CTA_LABEL = "Request a Bid"
CTA_TITLE = "Increase the value of your community."
CTA_TEXT = "Call 1-877-844-4227 or request a bid. A Community Manager, transparent monthly reporting, and an online portal for your board and homeowners."
SIDE_TITLE = "HOA management with a Community Manager and online portal."
PHONES = [("Toll-free", "1-877-844-4227", "+18778444227"), ("Lehi office", "801-641-1844", "+18016411844")]
EMAIL = "info@acs-hoa.com"
HOURS = ""
ADDRESS = [("Corporate", "2940 W Maple Loop Dr #102<br>Lehi, UT 84043")]
AREAS = ["Utah", "Washington", "Idaho", "Arizona"]
OFFICES = ["Clearfield", "Lehi", "Eagle Mountain", "St. George", "Park City (2)"]
SOCIAL = []
BLURB = "HOA and community association management from Lehi, Utah: Community Managers, transparent financials, online portals and professional services for boards."
SVC_LABEL = "Services"
SVC = [("management-services.html", "Management services", None), ("online-services.html", "Online services", None), ("professional-services.html", "Professional services", None)]
NAV = [("About", "about.html"), ("Testimonials", "testimonials.html"), ("Service areas", "service-areas.html")]


def biz(full=True):
    n = {"@type": "ProfessionalService", "@id": U + "#business", "name": NAME, "alternateName": "ACS HOA", "url": U, "telephone": "+18778444227", "email": EMAIL,
         "logo": U + "assets/img/acs-logo.png", "image": U + "assets/img/acs-logo.png",
         "address": {"@type": "PostalAddress", "streetAddress": "2940 W Maple Loop Dr #102", "addressLocality": "Lehi", "addressRegion": "UT", "postalCode": "84043", "addressCountry": "US"}}
    if full:
        n.update({"description": "Advanced Community Services (ACS) manages homeowners associations and condominium communities: Community Managers, dues collection, financial reporting, online portals, reserve analysis and board support.",
                  "areaServed": [{"@type": "State", "name": a} for a in AREAS]})
    return [n]
