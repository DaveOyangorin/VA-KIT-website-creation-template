> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# Introducing a New Spam Policy for "Back Button Hijacking"

- **Source:** https://developers.google.com/search/blog/2026/04/back-button-hijacking
- **Type:** Search Central blog / Spam policy (expansion of "malicious practices")
- **Published / Last updated:** April 13, 2026. Posted by Chris Nelson on behalf of the Google Search Quality team.
- **Scraped by FRAVATA:** 2026-06-01

## What it says
- Google is expanding its spam policies to make "back button hijacking" an explicit violation of the **malicious practices** spam policy, which can lead to spam actions.
- **Definition (verbatim intent):** Back button hijacking "occurs when a site interferes with a user's browser navigation and prevents them from using their back button to immediately get back to the page they came from." Instead of returning to the previous page, users "might be sent to pages they never visited before, be presented with unsolicited recommendations or ads, or are otherwise just prevented from normally browsing the web."
- Rationale: it breaks the fundamental expectation of the back button, causes user frustration, and makes people less willing to visit unfamiliar sites. Google notes inserting deceptive/manipulative pages into a user's browser history has "always been against" Search Essentials; this designation makes it explicit because the behavior is rising.
- The cited malicious-practices definition: "Malicious practices create a mismatch between user expectations and the actual outcome, leading to a negative and deceptive user experience, or compromised user security or privacy."
- **Enforcement deadline: June 15, 2026.** The policy was published two months in advance (April 13) to give site owners time to fix issues.
- Consequences: pages engaging in back button hijacking "may be subject to manual spam actions or automated demotions," impacting Search performance.
- **Important caveat from Google:** some instances "may originate from the site's included libraries or advertising platform." Owners are told to review technical implementation and remove/disable any code, imports, or configurations responsible.
- Recovery path: after fixing a manual action, submit a reconsideration request in Search Console.

## What MAMMATA must do
- Before June 15, 2026, audit each client site for any script, library, or ad/affiliate platform that manipulates browser history or blocks the back button (history.pushState loops, forced redirects on `popstate`, interstitials triggered by back navigation).
- Manually test the back button on each site: load a page from a referrer, click back, confirm the user returns to the prior page without redirect, injected page, ad, or "are you sure you want to leave" trap.
- Specifically inspect third-party ad tags and affiliate scripts (highest risk on the auto repair client auto and any monetized pages) — Google explicitly warns these are common sources.
- If hijacking behavior is found, remove or disable the offending code; do not assume "it's the vendor's fault" exempts the site.
- Document remediation per site so a reconsideration request can be filed if a manual action lands.

## Audit checks (scorable yes/no)
- [ ] Clicking the browser back button returns the user to the actual previous page (no redirect/injection).
- [ ] No JavaScript manipulates `history`/`popstate` to trap users or insert unvisited pages.
- [ ] No interstitial, ad, or recommendation page is forced on back navigation.
- [ ] Third-party ad tags and affiliate scripts have been reviewed and confirmed free of back-button interference.
- [ ] Remediation completed and verified before the June 15, 2026 enforcement date.
