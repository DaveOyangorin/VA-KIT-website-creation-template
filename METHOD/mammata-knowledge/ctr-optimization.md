> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

<!-- MAMMATA reference module — extracted verbatim from the agent definition 2026-06-11. The agent def mandates reading this file before the matching task. -->

## CTR OPTIMIZATION — EARNING THE CLICK (NON-NEGOTIABLE)

**The Iron Rule:** Ranking without clicks is worthless. A page with impressions and 0 clicks is a broken page. Fix it before anything else.

### GSC CTR Triage Protocol

When analyzing Google Search Console data, MAMMATA MUST:
1. Flag every query with **10+ impressions and 0 clicks** as a P1 (Priority 1) fix
2. Flag every page with **CTR below 2%** on position 1-5 as a P1 fix
3. Flag every page with **CTR below 1%** on position 6-10 as a P2 fix
4. Rewrite title tags and meta descriptions for ALL flagged pages before touching anything else

**CTR benchmarks by position (2026):**
| Position | Expected CTR | Below this = problem |
|----------|-------------|----------------------|
| 1 | 25-35% | < 15% |
| 2 | 13-18% | < 8% |
| 3 | 8-12% | < 5% |
| 4-5 | 4-8% | < 3% |
| 6-10 | 1-4% | < 1% |

### Title Tag CTR Formulas

**NEVER write a title like this:**
- `Service Name Location | Brand Name` — generic, no hook, no reason to click
- `Brand Name | Service Name` — brand first kills CTR
- `Service in City, ST | Brand` — no urgency, no differentiator

**ALWAYS write titles that include at least 2 of these CTR signals:**
1. **Exact query match** — mirror the words people type
2. **Power modifier** — Same-Day, 24/7, Emergency, Licensed, 5-Star, Trusted, Local, Near Me
3. **Benefit or differentiator** — Upfront Pricing, No Hidden Fees, Fast Response, Free Estimate
4. **Social proof signal** — 5-Star Rated, Hundreds of Reviews, #1 in [City]
5. **Urgency** — Available Now, Call Today, Open Now

**Title formulas that convert:**
```
[Service] Near Me | [Power Modifier] | [Brand] [City]
[Service] [City] | [Social Proof] | [Differentiator]
[Urgency Question]? | [Service] [City] | [Brand]
[Service] [City], [ST] | [Power Modifier] | [Brand]
```

**Real examples (what we changed and why):**
| Before (0 clicks) | After (CTR-optimized) | Why it works |
|---|---|---|
| `Water Heater Repair & Installation Tooele \| Example Plumbing` | `Water Heater Repair Near Me \| Same-Day Service \| Example Plumbing Tooele` | Matches "near me" query + same-day urgency |
| `Plumber in Tooele, UT \| Example Plumbing` | `Plumber Tooele, UT \| 5-Star Rated \| Same-Day Service \| Example Plumbing` | Social proof + urgency = click magnet |
| `Plumber in North Salt Lake, UT \| Example Plumbing` | `Plumber North Salt Lake, UT \| Same-Day Available \| Example Plumbing` | Specific city + urgency modifier |

### Meta Description CTR Psychology

**The meta description is a 160-character ad. Treat it like one.**

**Techniques that drive clicks:**

1. **Open with a question** matching the user's pain: `"Water heater broken?"` → creates instant recognition
2. **Social proof early**: `"5-star rated"`, `"Tooele's most trusted"`, `"100+ 5-star reviews"`
3. **Specific benefits, not features**: `"upfront pricing, no surprises"` beats `"competitive rates"`
4. **Action close**: End with phone number + call to action: `"Call (801) 262-0399 today."`
5. **Licensed/insured signal**: Always include for trades and service businesses — it reduces risk perception

**Meta description formula for local service businesses:**
```
[Pain point or question]? [Brand] offers [key benefit] in [City]. [Social proof] + [differentiator]. Call [phone] [urgency].
```

**Hard rules:**
- Never write a meta description that is just a list of services — that is a navigation menu, not an ad
- Never exceed 160 characters — truncation kills CTR
- Never leave a meta description empty — Google will auto-generate a bad one
- Always include the phone number for local service businesses
- Always include at least one trust signal (licensed, insured, 5-star, years in business)

### Power Words by Business Type

**Local Service (plumbing, HVAC, electrical, roofing):**
- Same-Day, Emergency, 24/7, Licensed & Insured, 5-Star Rated, Upfront Pricing, No Hidden Fees, Trusted, Local, Fast Response, Free Estimate

**Medical / Healthcare:**
- Board-Certified, Accepting New Patients, Same-Day Appointments, Covered by Insurance, Compassionate, Expert, Evidence-Based

**E-Commerce:**
- Free Shipping, In Stock, Ships Today, Best Price, Top Rated, New Arrival, Limited Stock

**Legal / Financial:**
- Free Consultation, No Fee Unless You Win, Board-Certified, Experienced, Trusted, Confidential

### CTR Audit — Required in Every SEO Audit

Add this as Signal 8 in all MAMMATA audit reports:

```
## SIGNAL 8 — CTR OPTIMIZATION [score/20]
Rating: PASS / NEEDS WORK / FAIL

Pages with 10+ impressions & 0 clicks:
- [list every URL]

Pages with CTR below benchmark for their position:
- [list every URL with position and actual vs expected CTR]

Title tag issues:
- Brand-first titles: ✅/❌
- Generic titles with no power modifiers: ✅/❌
- Titles not matching primary query: ✅/❌

Meta description issues:
- Service list descriptions (not ad-style): ✅/❌
- Missing phone number (for local businesses): ✅/❌
- Missing trust signal: ✅/❌
- Over 160 characters: ✅/❌
- Missing descriptions (Google auto-generating): ✅/❌

Rewrites required:
[List each URL with current title/description → recommended title/description]
```
