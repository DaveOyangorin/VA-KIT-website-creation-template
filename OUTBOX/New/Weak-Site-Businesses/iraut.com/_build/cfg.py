"""iraut.com: facts and settings (22 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl (22 Oct 2026) of all 48 sitemap URLs (Wix, no trailing slash). Same URLs on the www host, same canonicals.
From the site: Investment Realty Advisors, LLC; one-stop brokerage and property management; (801) 528-4557 with extensions (2 storage,
3 residential leasing, 4 maintenance, 5 tenant relations, 6 maintenance emergencies); info@iraut.com; mailing address 869 East 4500 South,
PMB 224, SLC, UT 84107; brokerage in the Salt Lake metro since 2008; $380M in assets under management (pm page; the performance page says
$400M+, $120M+ in sales and $40M+ in leases over 24 months); 1,600+ units on the Wasatch Front; 100+ combined years of experience; fee "as low
as 3%"; asset classes: retail, office, multifamily, industrial, self storage, residential; $103M transacted in 2021; team and license numbers
(about page); self-storage communities list; Resident Benefits Package $45/month; tenant portal and FAQ; IRA Lux remodel/flip; REO;
seller finance; Elliot Abel bio; Joseph Mills's blog post.
NAP: Google listing 411 W 7200 S, Midvale, UT 84047, +1801-528-4557 (used, copied exactly). The site shows only the PMB mailing address.
Placeholder pages (Wix "This is a Paragraph", team items "Brian Chung, VP Product", duplicate "About" copies, "General", thank-you pages) are
kept at their URLs, noindex. Left out: Google rating (3.2 from 227; report says flag to Angelo before pitching).
Photos: their own property photos (commercial buildings they list or manage, remodels from the IRA Lux page, development renderings, an
example owner report). Stock landscapes and template headshots are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "iraut.com"
U = "https://www.iraut.com/"
TRAIL = False
NAME = "Investment Realty Advisors"
TODAY = "2026-10-22"
HOME_OG = "ira-hero"
THEME_COLOR = "#173f55"
FONTS = "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;1,6..72,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "ira-logo"
CTA_PATH = "contactus/"
CTA_LABEL = "Talk to IRA"
CTA_TITLE = "One firm for the whole <em>life of the asset.</em>"
CTA_TEXT = "Buy, lease, manage, improve, exchange or sell. Call (801) 528-4557 or email info@iraut.com and the right IRA team will get back to you."
SIDE_TITLE = "Brokerage and property management under one roof."
PHONES = [("Main", "(801) 528-4557", "+18015284557")]
EMAIL = "info@iraut.com"
HOURS = ""
ADDRESS = [("Office", "411 W 7200 S<br>Midvale, UT 84047")]
AREAS = ["Midvale", "the Salt Lake metro", "the Wasatch Front"]
SOCIAL = []
BLURB = "Investment Realty Advisors: commercial and residential brokerage, property management, 1031 exchange support and self storage across Utah's Wasatch Front since 2008."
SVC_LABEL = "Services"
SVC = [("pm/", "Property management", None), ("commercial-real-estate/", "Commercial real estate", None), ("residential/", "Residential investing", None), ("lux/", "IRA Lux remodel &amp; flip", None),
       ("bank-owned-services/", "REO &amp; bank owned", None), ("sellerfinance/", "Seller finance", None), ("selfstorage/", "Self storage", None), ("use-cases/", "Performance", None)]
NAV = [("Tenants", "portal/"), ("Owners", "ownerportal/"), ("About", "about/"), ("Contact", "contactus/")]


def biz(full=True):
    n = {"@type": "RealEstateAgent", "@id": U + "#business", "name": "Investment Realty Advisors, LLC", "url": U, "telephone": "+18015284557", "email": EMAIL,
         "logo": U + "assets/img/ira-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "411 W 7200 S", "addressLocality": "Midvale", "addressRegion": "UT", "postalCode": "84047", "addressCountry": "US"}}
    if full:
        n.update({"description": "Utah real estate brokerage and property management firm: commercial and residential brokerage, property management, 1031 exchange support, REO disposition and self storage on the Wasatch Front.",
                  "areaServed": {"@type": "State", "name": "Utah"}})
    return [n]
