"""equitypmusa.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 21 sitemap pages (21 Oct 2026), same URLs (no trailing slash) and canonicals.
From the site: phone 801-545-4302 (matches Google), info@equitypmusa.com (also epmagent@ and office@ on the FAQ), office 1218 E. 7800 S.
#150, Sandy, UT 84094 (Google, copied exactly: "1218 E 7800 S Suite 150, Sandy, UT 84094"), Monday-Friday 9:00 AM-5:00 PM MST;
"now servicing areas in Utah, Florida, New Mexico, Oregon, Idaho, California, and Hawaii"; property management division of Equity Real
Estate; programs: Tenant Placement (one-time leasing fee; marketing & showing, application processing, lease signing) and Full Service
(one-time set-up fee + monthly management fee; adds rent collection, maintenance coordination, evictions, tenant communication, lease
enforcement); the owner FAQ (fees 50-100% of one month's rent for placement, 8-10% monthly for full service, set-up fee varies; deposit
typically one month's rent; typical $350 pet deposit and $50 pet fee; payout within 5 business days; inspections twice a year; vacancy
2-3 weeks when priced in the average range; etc.); tenant criteria ($65 application fee, 3x income, 2 years rental history...); agent
pages (Join Equity PM benefits, referral program with a non-compete promise); one owner testimonial (SFH Properties, Landlord).
Left out until confirmed: "1.2% eviction rate", "75% of renters have pets", "one of the most established real estate brokerages",
"over 10 years" (inside the testimonial it stays, word for word). Google rating (4.4 from 464) not shown. The site already had
business schema; it is rebuilt here with the Google NAP.
Template leftovers: 13 /properties/... pages are the Wix real-estate template's sample listings (fake addresses, "Brenda Rogers",
"Built Year 2034", San Francisco). They keep their URLs as noindex pages pointing to available rentals (flag: remove on the live site).
/groups (empty Wix groups feed) and /current-agents ("not in use") are noindex too.
Images: all photos on the site are Wix stock or AI-generated interiors, so none are used; the design is typographic around their logo."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "equitypmusa.com"
U = "https://www.equitypmusa.com/"
TRAIL = False
NAME = "Equity Real Estate Property Management"
TODAY = "2026-10-21"
HOME_OG = "eq-logo"
THEME_COLOR = "#0b2b4f"
FONTS = "https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "eq-logo"
CTA_PATH = "copy-of-landlords/"
CTA_LABEL = "Request a Rental Analysis"
CTA_TITLE = "Your property, our priority."
CTA_TEXT = "Call 801-545-4302 or request a rental analysis. Tenant placement or full-service management: you decide how involved you want to be."
SIDE_TITLE = "Tenant placement or full-service management."
PHONES = [("Call", "801-545-4302", "+18015454302")]
EMAIL = "info@equitypmusa.com"
HOURS = "Monday &ndash; Friday, 9:00 AM &ndash; 5:00 PM MST"
ADDRESS = [("Office", "1218 E 7800 S Suite 150<br>Sandy, UT 84094")]
AREAS = ["Utah", "Florida", "New Mexico", "Oregon", "Idaho", "California", "Hawaii"]
SOCIAL = []
BLURB = "The property management division of Equity Real Estate, based in Sandy, Utah: tenant placement and full-service management for rental owners."
SVC_LABEL = "Owners &amp; tenants"
SVC = [("copy-of-landlords/", "Owner information", None), ("copy-of-tenants/", "Application criteria", None), ("copy-of-contact-us/", "FAQs", None),
       ("join-equity-pm/", "Join Equity PM (agents)", None), ("submit-a-referral/", "Submit a referral", None)]
NAV = [("Owners", "copy-of-landlords/"), ("Tenants", "copy-of-tenants/"), ("FAQs", "copy-of-contact-us/"), ("Contact", "contact-us/")]


def biz(full=True):
    n = {"@type": "RealEstateAgent", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18015454302", "email": EMAIL,
         "logo": U + "assets/img/eq-logo.png", "image": U + "assets/img/eq-logo.png",
         "address": {"@type": "PostalAddress", "streetAddress": "1218 E 7800 S Suite 150", "addressLocality": "Sandy", "addressRegion": "UT", "postalCode": "84094", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Equity Real Estate's property management division in Sandy, Utah: tenant placement and full-service rental property management.",
                  "areaServed": [{"@type": "State", "name": a} for a in AREAS], "parentOrganization": {"@type": "Organization", "name": "Equity Real Estate"}})
    return [n]
