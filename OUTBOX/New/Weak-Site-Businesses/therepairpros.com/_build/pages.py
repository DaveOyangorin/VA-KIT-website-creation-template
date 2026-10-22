"""Pages for the therepairpros.com redesign: "The service manual".

A repair company lives on diagnosis, so the site reads like a service manual and a work order: numbered sections, figure captions
under their own job photos, spec readouts for the real prices, and the signature "Diagnose" tool, where you pick the product and
symptom (both from their own copy) and a work order prints with the $125 service call, the $150-$400 average job and the 90-day
warranty, then pre-fills the booking form.
References (screenshotted 21 Oct 2026): iFixit (repair culture, honest how-to tone), Teenage Engineering (technical type, spec
readouts, one signal colour), Fairphone (repairability, plain-spoken product pages). Miele captured behind a cookie wall only.
Brand: the black italic "The Repair Pros" plug wordmark and the white van; signal yellow added as the accent (multimeter yellow).
Same 3 URLs and canonicals (http, as on the live site), plus one new post."""
import html, re
from engine import img, canon
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_rp
import p_blog

cta = K.cta


def header():
    return K.header()


def footer():
    f = K.footer()
    return re.sub(r'<span class="flogo"><img[^>]*></span>', '<span class="flogo">' + img("rp-logo-white", "The Repair Pros logo") + '</span>', f)


def policy(key, heads):
    """their policy text, split on its own numbered headings; bullet characters become list items."""
    import json, os
    t = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))[key]["text"]
    t = re.sub(r'^class="layout main">\s*', "", t)
    for junk in ("Privacy Policy Privacy Policy ", "SMS Privacy policy and Terms & Conditions "):
        if t.startswith(junk): t = t[len(junk):]
    parts, out = [], []
    pos = 0
    for h in heads:
        i = t.find(h, pos)
        if i < 0: continue
        parts.append((t[pos:i], None)); parts.append(("", h)); pos = i + len(h)
    parts.append((t[pos:], None))
    for txt, h in parts:
        if h: out.append(f"<h2>{html.escape(h)}</h2>"); continue
        txt = txt.strip()
        if not txt: continue
        bits = [b.strip() for b in txt.split("•")]
        if bits[0]: out.append(f"<p>{html.escape(bits[0])}</p>")
        if len(bits) > 1: out.append("<ul>" + "".join(f"<li>{html.escape(b)}</li>" for b in bits[1:] if b) + "</ul>")
    return "\n".join(out)


PRIV_H = ["1. Information We Collect", "2. How We Use Your Information", "3. SMS Communications and TCR Compliance", "4. Disclosure of Your Information",
          "5. Data Security", "6. Your Choices and Rights", "7. Changes to This Privacy Policy", "8. Contact Us", "9. Consent"]
SMS_H = ["SMS Privacy Policy", "Information We Collect:", "How We Use Your Information:", "Your Choices:", "Data Security:", "Contact Us:", "SMS Terms and conditions",
         "Terms and Conditions", "1. Message Frequency", "2. Charges, Carriers", "3. Opt-In and Opt-Out.", "4. Privacy", "5. ", "6. ", "7. "]


def make_pages():
    out = [home_rp.home()]
    out.append(K.page("website-privacy-policy/", "Privacy Policy", "Privacy Policy", "Effective date: 10/1/2024", "Legal", "Website Privacy Policy | The Repair Pros, Salt Lake City",
                      "The Repair Pros website privacy policy: what we collect, how we use it, SMS communications and TCR compliance, data security and your choices and rights.",
                      policy("website_privacy_policy", PRIV_H).replace("<p>Effective Date: 10/1/2024 ", "<p>"), canonical=U + "website-privacy-policy/"))
    out.append(K.page("sms-privacy-and-terms/", "SMS Terms", "SMS Privacy Policy and Terms &amp; Conditions", "", "Legal", "SMS Privacy Policy and Terms | The Repair Pros, Utah",
                      "The Repair Pros SMS privacy policy and terms and conditions: what we collect when you opt in, message frequency, rates, opting out with STOP and help.",
                      policy("sms_privacy_and_terms", SMS_H), canonical=U + "sms-privacy-and-terms/"))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Start a work order", "#diagnose"), ("Pricing", "#pricing"), ("Book a repair", "#book"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (801) 268-6868.",)) for x in out]
