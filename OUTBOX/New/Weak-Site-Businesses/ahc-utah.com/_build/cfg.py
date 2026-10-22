"""ahc-utah.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: the live site blocks our network (403 / timeouts), so the pages were recovered from the Internet Archive (latest copies, Feb 2024 to
Jun 2026): /, /About-Affordable, /About-Us, /Careers, /Carrier-Air-Conditioners, /Carrier-Equipment, /Carrier-Furnaces,
/Carrier-Indoor-Air-Quality, /Contact, /Financing, /Lennox, /Lennox-Air-Conditioners, /Lennox-Furnaces, /Lennox-Indoor-Air-Quality,
/Products, /Promotions, /services. Same URLs (no trailing slash, same capitalization) on the www host. /contact-us is a 404 on the live site.
From the site: Affordable Heating & Cooling, Inc.; 155 Baird Ave, Salt Lake City, UT 84115; 801.261.0924; office Mon-Fri 8am-5pm (Contact,
matches Google); family owned and operated, third generation, "servicing the Salt Lake Valley for more than two decades", "over 50 years of
experience" (About-Affordable; the older About-Us page says "more than a decade", so the newer page is used); sales, installs and service on
all makes and models; 24-HR emergency service; full services list; Carrier and Lennox model lists; financing O.A.C. through Service Finance
Company; careers (service, maintenance and install technicians; RMGA, EPA, NATE).
Left out until confirmed: Google rating (4.9 from 565), the Feb 2024 promotion payment amounts (stale), manufacturer product photos.
Photos: none of their own (the old slider is stock). Homepage banner uses credited open-license photos of Salt Lake City parks a few
minutes from their office: Liberty Park in summer (Pollardjosephd, CC BY-SA 4.0), Sugar House Park in snow (claralieu, CC BY 2.0), and the
valley inversion (Derrellwilliams, CC BY-SA 4.0), all via Wikimedia Commons, credited on the page."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "ahc-utah.com"
U = "https://www.ahc-utah.com/"
TRAIL = False
NAME = "Affordable Heating & Cooling"
TODAY = "2026-10-22"
HOME_OG = "ahc-winter"
THEME_COLOR = "#14232c"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Public+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "ahc-logo"
CTA_PATH = "Contact/"
CTA_LABEL = "Free Estimate"
CTA_TITLE = "Warm in January. <em>Cool in July.</em>"
CTA_TEXT = "Call 801.261.0924 or request a free estimate. We sell, install and service all makes and models, with 24-hour emergency service."
SIDE_TITLE = "Free estimates on new furnaces and air conditioners."
PHONES = [("Call", "801.261.0924", "+18012610924")]
EMAIL = ""
HOURS = "Office: Mon&ndash;Fri 8 am&ndash;5 pm &middot; 24-hour emergency service"
ADDRESS = [("Office", "155 Baird Ave<br>Salt Lake City, UT 84115")]
AREAS = ["Salt Lake City", "the Salt Lake Valley"]
SOCIAL = []
BLURB = "Family owned and operated in our third generation. Sales, installation and service on all makes and models of heating and air conditioning in the Salt Lake Valley."
SVC_LABEL = "Services"
SVC = [("services/#heating", "Furnaces &amp; heating", None), ("services/#cooling", "Air conditioning", None), ("services/#air", "Indoor air quality", None),
       ("services/#commercial", "Commercial HVAC", None), ("Products/", "Carrier &amp; Lennox", None), ("Financing/", "Financing", None)]
NAV = [("Products", "Products/"), ("Financing", "Financing/"), ("About", "About-Affordable/"), ("Careers", "Careers/"), ("Contact", "Contact/")]


def biz(full=True):
    n = {"@type": "HVACBusiness", "@id": U + "#business", "name": "Affordable Heating & Cooling, Inc.", "alternateName": NAME, "url": U, "telephone": "+18012610924",
         "logo": U + "assets/img/ahc-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "155 Baird Ave", "addressLocality": "Salt Lake City", "addressRegion": "UT", "postalCode": "84115", "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "Family-owned HVAC company in Salt Lake City: furnace and air conditioning sales, installation, repair and maintenance for homes and businesses, all makes and models, with 24-hour emergency service.",
                  "areaServed": {"@type": "City", "name": "Salt Lake City, UT"}, "brand": [{"@type": "Brand", "name": "Carrier"}, {"@type": "Brand", "name": "Lennox"}]})
    return [n]
