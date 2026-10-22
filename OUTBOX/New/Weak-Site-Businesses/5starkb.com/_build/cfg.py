"""5starkb.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl of all 16 sitemap pages (21 Oct 2026), same URLs (no trailing slash: /home, /about_us, /kitchens, /bathrooms, /windows,
/walk_in_tubs, /why_choose_our_walk_in_tubs, /bath_gallery, /kitchen_gallery, /designmybath, /testimonials, /contact_us, /contact2,
/now_hiring, /privacy_policy) and canonicals (the home page /home canonicalizes to the root; kept).
From the site: phone 801-999-4548, sales@5starkb.com (contact page; support@ and steve@ also appear), showroom 6951 S. 300 W. Suite A,
Midvale (Google, copied exactly: "6951 S 300 W Ste a, Midvale, UT 84047"); hours Mon-Fri 9:00 am-6:00 pm, Sat 10:00 am-3:00 pm, Sun closed;
free in-home estimate and what happens at the consultation; process Appointment, Design, Planning, Remodeling; services: kitchens,
bathrooms (incl. tub-to-shower conversions), walk-in tubs (acrylic vs gelcoat, dual 2" gravity drains etc. from their own page),
windows, cabinets/refacing and countertops (galleries); family operated and locally owned; mission and core values; now hiring roles.
Left out until confirmed: "10+ Years Experience", "A+ BBB Rating", "5-Star Reviews", "the best choice", "national dealer network with
over 200 locations". The /testimonials page is unedited template text ("Click to edit... Customer Name"), so no testimonials are shown
and the page is noindex until real reviews are supplied. Google rating (4.7 from 527) not shown.
Photos: their own job photos from the bath and kitchen galleries (iPhone shots from 2020, project photos and their before/after
composites, split into pairs for the slider). Manufacturer/stock images (walk-in tub ads, "us-..." renders, supplier granite shots,
window renders, Adobe Stock banner) are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "5starkb.com"
U = "https://5starkb.com/"
TRAIL = False
NAME = "5 Star Kitchen and Bath"
TODAY = "2026-10-21"
HOME_OG = "kb-hero"
THEME_COLOR = "#141416"
FONTS = "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;0,6..96,700;1,6..96,500&family=Karla:wght@400;500;600;700&family=Space+Mono:wght@400&display=swap"
TRACK_HEAD = ""
LOGO = "kb-logo"
CTA_PATH = "contact_us/"
CTA_LABEL = "Free In-Home Estimate"
CTA_TITLE = "Experience the ultimate remodel."
CTA_TEXT = "Call 801-999-4548 or book a free in-home estimate. We&rsquo;ll evaluate your space, review design options and materials, and give you a clear, written estimate."
SIDE_TITLE = "Free in-home estimate. No pressure, no guesswork."
PHONES = [("Call", "801-999-4548", "+18019994548")]
EMAIL = "sales@5starkb.com"
HOURS = "Mon&ndash;Fri 9 am&ndash;6 pm &middot; Sat 10 am&ndash;3 pm &middot; Sun closed"
ADDRESS = [("Showroom", "6951 S 300 W Ste a<br>Midvale, UT 84047")]
AREAS = ["Midvale", "Salt Lake City and surrounding Utah communities"]
SOCIAL = []
BLURB = "Family-operated, locally owned kitchen and bathroom remodeling in Midvale, serving Salt Lake City and surrounding Utah communities."
SVC_LABEL = "Remodeling"
SVC = [("kitchens/", "Kitchens", None), ("bathrooms/", "Bathrooms", None), ("walk_in_tubs/", "Walk-in tubs", None), ("windows/", "Windows", None),
       ("kitchen_gallery/", "Kitchen gallery", None), ("bath_gallery/", "Bath gallery", None)]
NAV = [("Before &amp; after", "#before-after"), ("About", "about_us/"), ("Contact", "contact_us/")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U, "telephone": "+18019994548", "email": EMAIL,
         "logo": U + "assets/img/kb-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "6951 S 300 W Ste a", "addressLocality": "Midvale", "addressRegion": "UT", "postalCode": "84047", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"},
                                       {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "15:00"}]}
    if full:
        n.update({"description": "5 Star Kitchen and Bath remodels kitchens and bathrooms in Midvale and the Salt Lake City area: cabinets, countertops, showers and tub-to-shower conversions, walk-in tubs and windows.",
                  "areaServed": [{"@type": "City", "name": "Midvale, UT"}, {"@type": "City", "name": "Salt Lake City, UT"}]})
    return [n]
