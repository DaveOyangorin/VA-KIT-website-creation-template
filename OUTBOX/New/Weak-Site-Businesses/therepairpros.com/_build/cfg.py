"""therepairpros.com: facts and settings (21 Oct 2026). NOT A CLIENT YET. Do not contact this business.
SOURCE: live crawl over plain HTTP (21 Oct 2026). The HTTPS certificate is broken (apex: name mismatch, www: expired) and the site's own
canonicals are http://therepairpros.com/..., so the same URLs and canonicals are kept (flagged: switch to https once the certificate works).
3 pages: home, website-privacy-policy, sms-privacy-and-terms.
From the site's own pages: phone (801) 268-6868, dispatch@therepairpros.com (customerservice@therepairpros.com in the privacy policy),
on-site service in Salt Lake, Utah, Davis and Weber counties with a 61-city list; services (refrigerator, washer, dryer, oven, TV,
dishwasher, air dresser, range hood, microwave) and their symptoms; licensed, insured, background and drug screened technicians;
factory certified and trained; usually fixed on the first visit; factory original parts with a 90-day parts and labor warranty
(on the work done); $125 on-site service call to diagnose, a virtual repairman visit, $150-$400 average cost per job; Samsung
branded engineer, Sharp master service center, "the only authorized service center for Philips TV in Utah", Dacor authorized
service center; out-of-warranty brands list; eight Google-style testimonials quoted word for word with the names shown.
Google listing (report): The Repair Pros, +1801-268-6868, no address (service-area business), 4.8 stars from 942 reviews.
Left out: "hundreds of 5-star reviews", "won several awards for our service excellence"; the Google rating isn't shown or marked up.
No tracking tags found on the live site.
Photos: only their own (branded van, fridge, range, washer and dryer installs, a TV install, an open TV panel). Unsplash stock
(gold stars, electronics bench) and brand logo files are not used."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "therepairpros.com"
U = "http://therepairpros.com/"
TRAIL = True
NAME = "The Repair Pros"
TODAY = "2026-10-21"
HOME_OG = "rp-van"
THEME_COLOR = "#f4f3ef"
FONTS = "https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:ital,wght@0,500;0,700;0,800;0,900;1,800&family=Figtree:wght@400;500;600;700&family=Martian+Mono:wght@400;500&display=swap"
TRACK_HEAD = ""
LOGO = "rp-logo"
CTA_PATH = "#book"
CTA_LABEL = "Book a Repair"
CTA_TITLE = "Something broken? Book the repair."
CTA_TEXT = "Call (801) 268-6868 or request service online. We&rsquo;ll call you back to go over service call rates for your product and area."
SIDE_TITLE = "On-site appliance and TV repair."
PHONES = [("Call", "(801) 268-6868", "+18012686868")]
EMAIL = "dispatch@therepairpros.com"
HOURS = ""
ADDRESS = []
COUNTIES = [("Salt Lake County", ["Salt Lake City", "Murray", "Millcreek", "Cottonwood Heights", "Sandy", "Midvale", "Draper", "West Valley City", "Magna", "Kearns",
                                  "Taylorsville", "West Jordan", "South Jordan", "Herriman", "Riverton"]),
            ("Utah County", ["Lehi", "Eagle Mountain", "Saratoga Springs", "Alpine", "Highland", "Pleasant Grove", "Cedar Hills", "American Fork", "Orem", "Provo",
                             "Vineyard", "Lindon", "Springville", "Mapleton", "Spanish Fork", "Salem", "Payson", "Santaquin", "Elk Ridge", "Woodland Hills"]),
            ("Davis County", ["Bountiful", "West Bountiful", "North Salt Lake", "Woods Cross", "Centerville", "Farmington", "Kaysville", "Layton", "Fruit Heights",
                              "Clearfield", "Syracuse", "Sunset", "South Weber", "Clinton", "West Point"]),
            ("Weber County", ["Ogden", "South Ogden", "Roy", "Riverdale", "West Haven", "Plain City", "Harrisville", "Pleasant View", "North Ogden", "Uintah", "Washington Terrace"])]
AREAS = ["Salt Lake", "Utah", "Davis and Weber counties"]
SOCIAL = [("Facebook", "https://www.facebook.com/profile.php?id=100069383871472")]
BLURB = "On-site appliance, TV and electronics repair across Salt Lake, Utah, Davis and Weber counties. Factory original parts and a 90-day parts and labor warranty on the work done."
SVC_LABEL = "Repairs"
SVC = [("#fix-refrigerator", "Refrigerator repair", None), ("#fix-washer", "Washer repair", None), ("#fix-dryer", "Dryer repair", None), ("#fix-oven", "Oven repair", None),
       ("#fix-tv", "TV repair", None), ("#fix-dishwasher", "Dishwasher repair", None), ("#fix-microwave", "Microwave repair", None), ("#fix-range-hood", "Range hood repair", None)]
NAV = [("Brands", "#brands"), ("Pricing", "#pricing"), ("Service area", "#area")]


def biz(full=True):
    n = {"@type": "HomeAndConstructionBusiness", "@id": U + "#business", "name": NAME, "url": U,
         "telephone": "+18012686868", "email": EMAIL, "logo": U + "assets/img/rp-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "priceRange": "$125 service call", "sameAs": [s[1] for s in SOCIAL]}
    if full:
        n.update({"description": "The Repair Pros repairs refrigerators, washers, dryers, ovens, dishwashers, microwaves, range hoods and flat panel TVs on site across Salt Lake, Utah, Davis and Weber counties.",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", UT"} for c, t in COUNTIES]})
    return [n]
