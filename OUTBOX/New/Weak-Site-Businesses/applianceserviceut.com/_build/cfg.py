"""applianceserviceut.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of the 4 pages (no trailing slash): /, /about-us, /services, /contact. Same URLs on the www host, same canonicals.
From the site: ASI Appliance Service, Inc.; (801) 487-8591; asi@asiapplianceservice.com; family owned and locally owned; "more than 25 years of
continued professional service" and "nearly 40 years of experience in the industry"; technicians drug-free and background approved; fully
licensed, registered and insured; 30-day guarantee on all service calls; same or next-day service; residential repair and maintenance for
dishwashers, dryers, electric appliances, freezers, garbage disposals, gas appliances, microwaves, refrigerators, ranges, trash compactors and
washing machines; brands: Danby, Frigidaire, GE, Gibson, Hotpoint, Kenmore, KitchenAid, Magic Chef, Maytag, Speed Queen, Tappan, Westinghouse,
Whirlpool, White; areas: Salt Lake City, Ogden, Provo and Tooele metros; hours Mon-Fri 8:00 AM-5:00 PM, Sat-Sun closed; closed on New Year's,
Memorial Day, July 4th, July 24th, Labor Day, Thanksgiving and Christmas; payment: Visa, Mastercard, Discover, Amex, cash, check, debit.
NAP: Google listing has 2755 S 300 W, Salt Lake City, UT 84115 with the same phone (used, copied exactly). The site's contact page says
359 W Ironwood Dr, Salt Lake City UT 84115. Flagged for the client.
Left out until confirmed: Google rating (4.2 from 234), "The Manufacturers Trust Us" (no manufacturer program named), "the best price possible".
Photos: the site's two photos are stock, so none are used. Banners are credited Wikimedia Commons photos of Salt Lake City."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "applianceserviceut.com"
U = "https://www.applianceserviceut.com/"
TRAIL = False
NAME = "ASI Appliance Services"
TODAY = "2026-10-22"
HOME_OG = "asi-slc"
THEME_COLOR = "#0f4f7f"
FONTS = "https://fonts.googleapis.com/css2?family=Rubik:wght@500;600;700;800&family=Source+Sans+3:wght@400;500;600;700&family=Courier+Prime:wght@400;700&display=swap"
TRACK_HEAD = ""
LOGO = "asi-logo"
CTA_PATH = "contact/"
CTA_LABEL = "Schedule Service"
CTA_TITLE = "Same or next-day service. <em>Guaranteed 30 days.</em>"
CTA_TEXT = "Call (801) 487-8591, Monday to Friday, 8 to 5. Family-owned, licensed and insured, with drug-free, background-approved technicians across the Wasatch Front."
SIDE_TITLE = "Same or next-day service, with a 30-day guarantee on every call."
PHONES = [("Call", "(801) 487-8591", "+18014878591")]
EMAIL = "asi@asiapplianceservice.com"
HOURS = "Mon&ndash;Fri 8 am&ndash;5 pm &middot; Sat&ndash;Sun closed"
ADDRESS = [("Shop", "2755 S 300 W<br>Salt Lake City, UT 84115")]
AREAS = ["Salt Lake City", "Ogden", "Provo", "Tooele"]
SOCIAL = []
BLURB = "Family-owned appliance repair in Salt Lake City for more than 25 years, with nearly 40 years in the industry. Same or next-day service, 30-day guarantee."
SVC_LABEL = "Services"
SVC = [("services/#appliances", "Appliances we repair", None), ("services/#brands", "Brands we service", None), ("about-us/", "About ASI", None), ("contact/", "Hours &amp; contact", None)]
NAV = [("About", "about-us/"), ("Contact", "contact/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "legalName": "ASI Appliance Service, Inc.", "url": U, "telephone": "+18014878591", "email": EMAIL,
         "logo": U + "assets/img/asi-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp", "paymentAccepted": "Visa, Mastercard, Discover, American Express, cash, check, debit",
         "address": {"@type": "PostalAddress", "streetAddress": "2755 S 300 W", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84115", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Family-owned residential appliance repair in Salt Lake City, Ogden, Provo and Tooele: refrigerators, washers, dryers, dishwashers, ranges, microwaves, freezers and more, with a 30-day guarantee.",
                  "areaServed": [{"@type": "City", "name": c + ", UT"} for c in AREAS]})
    return [n]
