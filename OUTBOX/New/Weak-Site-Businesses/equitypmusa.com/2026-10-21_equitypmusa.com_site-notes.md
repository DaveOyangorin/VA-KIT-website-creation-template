# equitypmusa.com: redesign notes (21 Oct 2026)

**Not a client yet. Do not contact this business.** Draft only; nothing is live.

- `site/`: same 21 URLs (no trailing slash) and canonicals, plus a new post. `preview/`: the review copy.
- **Concept, "The owner's ledger":** navy and ruled paper, Source Serif with tabular figures, and their logo. No photos are used: every photo on the site was Wix stock or an AI-generated interior.
  - **Signature, Rent math:** pick Owner or Renter and set a monthly rent. The figures recalculate from Equity's own published rules:
    - placement fee: 50–100% of one month's rent
    - management: 8–10% a month, plus a variable set-up fee
    - deposit: about one month's rent
    - owner payout: within 5 business days
    - renter income: 3× rent, or 12 months of rent in savings
    - $65 application fee
    - pets: typically $350 deposit plus $50 a month
- **Programs:** the comparison chart, which existed only as an image, is now a real table.
- **References** (21 Oct 2026): Stripe, Mercury and Compass.
- **Facts used (from the site):**
  - Phone 801-545-4302 and info@equitypmusa.com.
  - Office "1218 E 7800 S Suite 150, Sandy, UT 84094" (Google, copied exactly).
  - Hours Mon–Fri 9–5 MST.
  - States served: UT, FL, NM, OR, ID, CA, HI.
  - Their 27 owner FAQs, the tenant criteria, the agent benefits and referral guarantee, and one owner testimonial (word for word).
- **Template leftovers:** the 13 /properties/ pages are Wix sample listings (fake addresses, "Brenda Rogers", built year 2034, San Francisco). /groups is empty and /current-agents says "not in use". All are noindex with links to the real pages. **Remove them on the live site.**
- **Left out:** "1.2% eviction rate", "75% of renters have pets", "one of the most established real estate brokerages", and the Google rating (4.4 from 464).
- **QA note:** the home canonical has no trailing slash (kept as on the live site). This trips a QA false positive, which was accepted.
- **Blog:** `blog/how-to-spot-a-rental-scam`, 1,047 words, FTC "Rental Listing Scams". A Utah security-deposit post was dropped because the legislature's site couldn't be reached to verify the statute.
- **QA:** 23 files, 0 real issues. Mobile header fix applied; menu checked.
