"""abode.cleaning: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 6 pages (21 Oct 2026), same URLs (no trailing slash). The site sets no canonicals; self-canonicals added.
Abode is a booking platform: Abode Home Maintenance LLC (d/b/a Abode) connects homeowners with vetted small cleaning businesses.
From the site: "Serving Roy to Spanish Fork" (home) and "Ogden to Payson UT and St. George Area" (services page): both shown as written
and flagged; flat-rate packages set at minimum rates for homes up to 3 bed / 2 bath / 2,800 sq ft; teams of 2 with their own
equipment and supplies; partner businesses insured, vetted with the Abode quality process and in business more than 3 years;
no contract; you don't have to be home; no laundry, dishes extra; arrival windows (9 am, 11:30 am, 2:30 pm starts, 1-2 hour window);
pre-cleaning instructions; cancellation fees ($25 inside 24-48 hours/same day; $65 up to 8 hours before); five customer reviews
quoted word for word with names; promo "$100 off your first recurring cleaning with promo code VIP100U" (as on the site, flagged).
The site shows NO phone number. Google listing (report), copied exactly: Abode House Cleaning, 126 12300 S Suite A, Draper, UT 84020,
+1801-845-0297 (note: the site's own legal pages give "126 W 12300 S Suite A Draper": flagged). support@abode-cleaning.com from the
privacy page.
Left out until confirmed: "Over 20,000+ Happy Homes", "6+ years", "thousands of reviews", "400+ cleaning teams", "4.8 rating from
400+ reviews", "nation wide company", "80% of clients aren't home". Google rating (4.7 from 521) not shown. Pricing plans load from the
booking app and aren't in the HTML, so no prices are shown.
Photos: stills from Abode's own brand video (their cleaning teams at work in a real home). The video's stock-style call-center shot and
screen mockups are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "abode.cleaning"
U = "https://abode.cleaning/"
TRAIL = False
NAME = "Abode House Cleaning"
TODAY = "2026-10-21"
HOME_OG = "ab-team-door"
THEME_COLOR = "#8332f8"
FONTS = "https://fonts.googleapis.com/css2?family=Gabarito:wght@500;600;700;800;900&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,400&family=Geist+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "ab-logo"
CTA_PATH = "our-services/"
CTA_LABEL = "Book a Cleaning"
CTA_TITLE = "From click to clean. It&rsquo;s that simple."
CTA_TEXT = "Take your time back. We&rsquo;ll take care of the rest. Flat-rate packages, teams of two with their own supplies, and no contract."
SIDE_TITLE = "Flat rates. No contract. You don&rsquo;t have to be home."
PHONES = [("Call", "(801) 845-0297", "+18018450297")]
EMAIL = "support@abode-cleaning.com"
HOURS = ""
ADDRESS = [("Office", "126 12300 S Suite A<br>Draper, UT 84020")]
AREAS = ["Draper", "Roy to Spanish Fork", "Ogden to Payson", "the St. George area"]
SOCIAL = [("Instagram", "https://www.instagram.com/abodehousecleaning/")]
BLURB = "House cleaning in Draper and along the Wasatch Front, booked online with vetted, insured local cleaning teams. Flat-rate packages and no contract."
SVC_LABEL = "Cleaning"
SVC = [("our-services/", "Services &amp; booking", None), ("cancellation-policy/", "Cancellation policy", None), ("marketplace/", "Marketplace", None)]
NAV = [("How it works", "#how"), ("Get ready", "#ready"), ("FAQ", "#faq")]


def biz(full=True):
    n = {"@type": "LocalBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18018450297", "email": EMAIL,
         "image": U + "assets/img/" + HOME_OG + ".webp", "sameAs": [s[1] for s in SOCIAL],
         "address": {"@type": "PostalAddress", "streetAddress": "126 12300 S Suite A", "addressLocality": "Draper", "addressRegion": "UT", "postalCode": "84020", "addressCountry": "US"}}
    if full:
        n.update({"description": "Abode connects homeowners with vetted, insured local house cleaning teams: flat-rate packages, teams of two with their own equipment and supplies, and no contract.",
                  "areaServed": {"@type": "State", "name": "Utah"}})
    return [n]
