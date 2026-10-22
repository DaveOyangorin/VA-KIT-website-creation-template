# 🎙️ The Wisdom's In The Calls

> Source: AI SEO: Rank Expand Academy (Skool) — `classroom/55a9c23d`  
> 10 lessons · 0 videos (~0 min) · 47 KB of written material  
> Internal reference for MAMMATA. Not for redistribution.

---

## Start Here

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/74751ace2f81412f915825048a66f74ea11398c4dd5d4c0faa2e25c7767239ed-md.png)

## **What this is**

Every week we get on a live call and share what's actually working right now: the tools, the scripts, the fixes, the hard-won lessons. The problem with live calls is they're hard to search. A great tactic gets shared in week 30, and by week 40 nobody can remember which recording it was in.

This section solves that. We pull the best insights from the calls, write them up so they're usable on their own, and credit the member who shared them. It's the searchable, permanent version of everything that gets figured out on the calls.

## **Why it matters**

The calls are where the edge is. It's the stuff being worked out this week, before it's written up anywhere else. But an insight you can't find again is an insight you've lost. This library makes sure the best of what gets shared stays findable, so you can come back to it when you actually need it.

## **How to use this section**

Each lesson tackles one problem operators actually hit, with a running list of fixes underneath. As more solutions surface on the calls, we add them, so these lessons get more useful over time. Browse by the problem you're stuck on, not front to back.

Every lesson links back to the full call it came from, and out to a community post where you can ask questions, add your own take, or pick up where the conversation left off.

## **Where to start**

Scroll down and pick the lesson that matches whatever you're wrestling with right now. There's no order, just the problem you want solved.

## Why Your AI Keeps Falling Apart Mid-Build

*Last updated: 23 July 2026*

---

## Context Overload

Your AI starts strong, then quality drops. You load one model with the whole job - research, content, schema, code - and it starts hallucinating, forgetting earlier instructions, or producing sloppier work the longer it runs. 

This isn't a bad model. It's **context overload**: the more you cram into one AI's working memory, the worse it performs.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/effbc95836b647819cf67f3a7b3912e2e8d8fd54214748b493b4a782694dc2c8-md.png)

Below is a running collection of fixes our members have shared on the calls. Each one attacks the same root problem from a different angle. Start with whichever matches where you're stuck.

---

## Solution #1 - Use an AI Hiring System (Paperclip)

**One agent per job (multi-agent builds)** *Surfaced by Blair in *[*Community Call #30*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=114f5d7fc24f4cf69937a2eea0fce731)*.*

**The principle:** narrow scope keeps each agent's context tight, which keeps quality high.

Instead of a single "master prompt" doing everything, split the build across specialised agents - each handling one narrow task with only the context it needs.

Blair uses **Paperclip** ([paperclip.ing](http://paperclip.ing)), an AI agent "hiring" system that lets you spin up role-specific agents, control budget, and plug in the models you want. 

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/c357419afca741be80f12c2f18833ee39f1bfa26088f46689e43aff2381d2859-md.png)

A microsite build splits like this:

- **Research agent**: pulls neighborhood/market data (e.g. Perplexity)
- **Content agent**: writes the copy
- **Schema agent**: handles structured data and technical code
- **QA agent**: checks the others

Each agent only gets the skills and memory for its role, then they hand off and cross-check each other. It's effectively a one-person agency where the "team" is a stack of narrow AI agents that don't step on each other.

---

## **Solution #2: Give Claude a filing system, not a pile**

**The WikiLLM memory setup ***Surfaced by Shlomi in *[*Community Call #44*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=bcb6a7bbb1fd4ef5911b489dad6a3c4b)*.*

Before this, Shlomi trained Claude on his materials the way most of us do: PDFs, images, and notes dumped in one folder, half of it overlapping and duplicating itself. The AI drowned in it.

The fix is the WikiLLM memory system: one [CLAUDE.md](http://CLAUDE.md) file with the rules, a wiki folder Claude owns and organizes, and a raw folder where you dump anything new. Then you say one word: "ingest." Claude files everything into the right place and the context stays clean, project after project. Shlomi: "There's no way to work with Claude without it, every project."

Teja runs the same idea per client: a full Markdown copy of each client's website on his machine, so Claude always understands the whole business before it touches anything. The starter prompt lives in the classroom (WikiLLM Memory System).

**The principle:** the AI doesn't fall apart because it's dumb. It falls apart because its memory is a junk drawer. Give it a librarian's system and it stays sharp.

[**Here are the steps for setting up a Wiki LLM**](https://www.skool.com/rank-expand-academy/classroom/52339bb6?md=2b41d555ba15407ca082b46579ea8155).

---

## **Solution #3: Fence off what works, and keep an undo button**

*Surfaced by Jesse and Shawn in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

Jesse runs client sites where Claude writes content, revises pages, and pushes changes on automated schedules. The client's one rule: "don't change anything that's working."

Two safeguards make that possible. First, the wiki memory setup (Solution #2) holds explicit rules about what the AI may and may not touch, so the boundary survives every session. Second, everything lives in version control (a private GitHub repo), so any mistake, yours or the AI's, rolls back in one command.

**The principle:** you don't need the AI to be perfect. You need its guardrails written down where it can't forget them, and a way to undo anything it breaks.

---

*More solutions will be added here as they surface on the calls.*

---

> **Try this**

Take one build you currently run through a single prompt. Break it into 3-4 narrow steps and run each with only the context that step needs. Compare the output.

[**💬 Discuss this in the community**](https://www.skool.com/rank-expand-academy/why-your-ai-gets-dumber-the-longer-you-use-it?p=c7d4de0c)

## Picking Clients That Actually Stick

*Last updated: 23 July 2026*

---

## Not All Clients Are Created Equal

Not all clients are worth having. The wrong ones churn fast, drain your time, second-guess your work, or make you nervous every time your phone rings. Most operators learn this the hard way - they say yes to everyone, then spend their energy on the clients least likely to stay.

Below is a running collection of hard-won filters our members have shared on the calls. Each one helps you pick clients that stick, and spot the ones that won't before you sign them.

---

## **Filter #1 - Avoid the client who knows just enough SEO**

***Surfaced by Blair**** in *[*Community Call #39*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=af901f71e65c4609aa84d8ea34c6cf13)*.*

The clients who come from YouTube, podcasts, or AI content and know *a little* about SEO are often the most painful. They send emails at 2am with walls of ChatGPT output telling you how to do your job, and they never fully trust your expertise.

The client you actually want is the business owner who says: *"You're the expert - you handle it."* They value the outcome, not the tactics, and they let you do the work you're good at.

**The principle:** the best client respects your expertise. Someone who wants to co-pilot every decision will cost you more than they pay.

---

## **Filter #2 - Pre-qualify lead buyers by review count**

***Surfaced by Naomi**** in *[*Community Call #30*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=114f5d7fc24f4cf69937a2eea0fce731)*.*

When Naomi looks for businesses to send leads to, she sorts by Google review count. A company with thousands of reviews will ignore you. A company with around 50 is hungry - they pick up, they listen, and they say yes.

She targets the business sitting *just below* the leader in the map pack: enough proof they want to grow, not so established they don't need you. Her hit rate on those calls is near 100%.

**The principle:** the hungriest partners make the stickiest clients. Pick the ones who actually need what you bring.

---

## **Filter #3: Only rev-share with partners who can swallow the volume**

*Surfaced by Jesse in *[*Community Call #43*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=e315b592808940c1a8106ea311e4fe3d)*.*

Jesse's team has burned through a lot of local contractors on rev-share deals. The filter they landed on: only sign partners who can absorb 100+ leads per month. Smaller operators choke on the volume, ghost when things get busy, and the deal dies.

Second check: service radius. A small contractor will drive 30-40 minutes; a bigger operator will go up to 90 for large jobs. Match your site's geographic coverage to what the partner will actually service, or you're generating leads nobody wants.

**The principle:** rev-share only works when the partner's capacity matches your output. Qualify for appetite before you qualify for anything else.

---

## **Filter #4: Pick niches where your work is actually the lever**

*Surfaced by Shlomi in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

Shlomi spent months on a restaurant local SEO project. More keywords, more content, better strategy: the niche didn't respond. The reason: in restaurants, the review score is the ranking parameter. Content barely moves the needle, so his best work couldn't win.

He quit the niche, and called it right: "It was a nice ride, a nice attempt. It was a lesson. You have to walk the path to learn things."

**The principle:** before you take the client, ask what actually ranks in their niche. If the answer isn't the thing you sell, the client can't stick no matter how good you are.

---

*More filters will be added here as they surface on the calls.*

---

> **Try this**

Look at your current client list. Which ones respect your expertise, sit at a healthy revenue level, and genuinely needed you when you started? Those are your model clients - go find more like them, and be slower to say yes to the ones who don't fit.

**💬 Discuss this in the community**

## What To Charge And How To Structure Deals

*Last updated: 23 July 2026*

---

## **Most Operators Leave Money On The Table**

Underpricing is the quietest way to stay broke. So is a messy deal structure that leaves you chasing payments or arguing over lead quality. The operators who do well aren't always the best at SEO. They're the ones who price with confidence and structure deals so they get paid cleanly and the client has every reason to stay.

Below is a running collection of pricing and deal-structure plays our members have shared on the calls.

---

## **Play #1: The fastest raise is charging the clients you already have**

***Surfaced by Blair**** in *[*Community Call #33*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c45bd362a8af4a1da1c5b1153e95232e)*.*

Blair ran a price adjustment across his entire book, raising every single client. Some balked, a few left and later came back, but his across-the-board average landed near $1,600 a month, with $500 clients on one end and $5,000 clients on the other. Chasing new clients is slow. Lifting your existing rates is the fastest path to more revenue, and most clients don't leave over it.

**The principle:** you almost certainly undercharge your current clients. Raising them is faster and cheaper than finding new ones.

---

## **Play #2: Per-lead, percentage, or flat retainer, and when to use each**

***Surfaced by Jesse ****in *[*Community Call #1*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=066e5914800f468e9f9075350ef6b407)*.*

Three ways to get paid on a rank-and-rent or lead-gen asset:

- **Per lead** is the simplest. You deliver a lead, they pay (for example, $150 for a garage-door lead, depending on the industry). The risk: people stiff you. Members have been burned for as much as $1,000 in unpaid leads.
- **Percentage of the job** can pay more, but you need access to their CRM to verify what closed, which most clients resist.
- **Flat retainer** is the cleanest long-term. Once the lead volume is steady, you move them to a flat monthly fee so you stop counting individual leads.

The pitch for your pricing: you deliver *exclusive* leads, unlike Angie's List, which sells the same $150 lead to five businesses at once.

**The principle:** start per-lead to prove value, move to flat retainer once volume is steady and trust is built.

---

## **Play #3: The 12-microsite deal structure**

***Surfaced by Jesse ****in *[*Community Call #7*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=16f9be0a0ad349e9b3a114de98986646)*.*

A clean, repeatable package for selling microsites to a local business: 12 sites for $1,500 a month on a 12-month engagement (10 paid, 2 thrown in as a bonus, so effectively $150 per site per month). At the end of the term, if they want to keep a site and own the IP outright, it's $3,500 per site to buy out.

It gives the client a clear monthly number, a bonus that feels generous, and a defined path to ownership, while you keep recurring revenue for a year.

**The principle:** package the offer with a simple monthly number, a small bonus, and a buyout path. It closes easier than pricing sites one at a time.

---

## **Play #4: Take the cheap "prove-out" deal on purpose**

*Surfaced in *[*Community Call #7*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=16f9be0a0ad349e9b3a114de98986646)*.*

When a client wants flexibility or a lower price, sometimes you take it on purpose, to get paid while you prove your model on a real client. The members framed it as a test case: you get a year of runway to show results, and a client who started by negotiating you down usually ends up keeping more sites and handing you the bigger project (their main-site SEO) once you've delivered.

**The principle:** a discounted deal that proves your system on a live client can be worth more than a full-price one-off. Play the long game when the upside is real.

---

## **Play #5: Stack offers so the client can't afford to leave**

*Surfaced in *[*Community Call #5*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=d1b4b17621b043968de399dbd731bfc2)*.*

Microsites are a sticky offer on their own, but the real retention comes from stacking. Get a client on microsites, then add their main-site SEO, then their web hosting. With two or three lines of business tied together, leaving becomes painful enough that they simply don't. Each added service deepens the relationship and raises the cost of switching.

**The principle:** one service is easy to cancel. Three intertwined services are not. Stack them and retention takes care of itself.

---

### **Play #6: The dedicated-hosting and SaaS markup**

*Surfaced by Bryan in *[*Community Call #25*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=d26da71f7cd249458c2ca4a820d22efa)*.*

Bryan builds client sites and adds recurring layers on top of the build fee. A live site on a dedicated VM (around $20/month in real cost on Replit) gets sold as "dedicated hosting, not a shared server." On top of that sits a CRM/automation layer (white-labeled GHL handling SMS, email automations, scheduling) billed monthly. One build went out at $1,500 up front plus roughly $197/month for the automation stack.

**The principle:** the build fee is one-time. The hosting and automation layers are recurring. Bundle real ongoing value (a CRM they actually use) so the monthly fee is justified, not arbitrary.

---

## **Play #7: Charge upfront. Always.**

*Surfaced by Jesse and the group in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

Coaching a member converting her first Upwork client to a $1,500/month direct deal, the room's advice was blunt and unanimous: "I don't work until I get paid." Never bill after the work is done.

The mechanics that came with it:

- **Stripe subscription** for the monthly. Simple, and it removes the chase.
- **Price in US dollars** for cross-border work. The currency swing is not your problem; Wise handles conversion.
- **Anchor and hold.** She asked $2,500, the client pushed back, she settled at $1,500 for a 90-day term. She already came down once, so that's where it stays.

**The principle:** getting paid is a system, not a hope. Upfront, on subscription, in dollars, and one concession maximum.

---

## **Play #8: The prepaid prove-out (learn on their dime)**

*Surfaced by Jesse in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

A new member, a commercial real estate broker, had a partner asking for leads. The catch: commercial deals take six months to two years to close, so a pure commission deal could mean a year with no income.

Jesse's structure: don't negotiate a rev share. Have the partner prepay about $1,000 for three microsites. He gets every lead from them for year one. You keep ownership of the sites. "You build them, you learn them on his dime. And then you can build 10 more." Shawn's hybrid version: get the first sites out for cash flow, then lease the sites and layer a rev share later to offset the long close cycle.

This is the sharper cousin of Play #4: the cheap deal is fine when it funds your learning and you keep the asset.

One caution from Call #45: revenue sharing tied to closed loans is largely prohibited in the US (mortgage, and likely real estate and insurance commissions too). Treat regulated niches as flat-fee territory unless you've checked the rules.

**The principle:** when the payoff is slow, get paid to build, keep what you build, and add upside later.

---

## **Play #9: The three-hour client ($500 an hour by design)**

*Surfaced by Jesse in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

Don't ask "how many hours will this client take?" Decide the answer, then build the system that makes it true. Jesse's number: a maximum of three hours a month per client.

The system: give Claude automated access to Google Search Console, FTP access to the site, and a private GitHub repo where it accumulates knowledge (the wiki memory setup). It writes new content, revises pages, and runs on automated schedules. Add Mailgun and Claude emails the client every update it makes, so the perceived value climbs while you sleep.

Three hours a month on a $1,500 client is $500 an hour, and it frees you to take the next client. Jesse: "You'll be making $10K a month before you know it."

**The principle:** your hourly rate is a design decision. Cap the hours first, then automate until the cap holds.

---

## **Play #10: Sell low or sell high. Never the middle.**

*Surfaced by Shawn (via Hormozi) in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*, proven by Teja in Calls #43-44.*

Two offers work: the $20,000-a-clip premium deal, and the cheap-at-volume deal. The middle limps, because mid-priced clients expect premium service without premium money.

Teja is the volume proof: his "Netflix for websites" runs around 40 clients at $100/month per site, fully automated, no upfront cost. The retention logic, in Jesse's words from Call #43: "You have to get to the point where it's so painless for the business owners to just pay you monthly that the retention is so high. They never think of it." And the reframe that sells it (Call #44): you're not selling a website, you're selling infrastructure: the site, the CRM, the profile, the posts, the leads.

**The principle:** pick an end of the barbell. Commodity pricing at volume, or premium pricing with premium positioning. The middle is where deals go to be renegotiated.

---

## **Play #11: A contract where every clause has a scar behind it**

*Surfaced by Blair in *[*Community Call #42*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=28aa58858d8348b892d12e1773c6d6d1)*.*

Blair's contract has grown to 2.5 pages over 15 years, and every clause came from a real incident. The ones earning their keep:

- No refund policy.
- No matter when the client cancels, one additional payment is due (they initial this line specifically).
- Arbitration clause.
- Not responsible for ADA compliance or privacy policy accuracy (client consults their own attorney; also initialed).

The payoff: "I had my first chargeback ever in 15 years and I won it... You never win against American Express." He won because the terms were explicit and initialed. AI can draft the language, but don't invent clauses speculatively; add them as real situations teach you.

**The principle:** a contract is a record of everything that ever went wrong, priced in advance. Make the scary clauses initialed, not buried.

---

*More plays will be added here as they surface on the calls.*

---

> **Try this**

Look at your lowest-priced client. When did you last raise them? If it's been over a year, draft the email. Then look at your best client and ask what second or third service you could stack on top of what they already buy.

**💬 Discuss this in the community**

## Beating Overwhelm and Shipping Consistently

*Last updated: 23 July 2026*

---

## **The Real Bottleneck Is Starting**

Most operators don't fail for lack of knowledge. They fail because they wake up with ten ideas, feel the weight of all of them at once, and freeze. The work isn't hard. Starting is. Consistency beats intensity in this game, and the members who win are the ones who show up and ship five days a week, not the ones with the best plan.

Below is a running collection of ways our members beat the freeze and keep shipping, shared on the calls.

---

## **Approach #1: The 20-minute timer**

***Surfaced by Naomi**** in *[*Community Call #17*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=37544182cb1d4659be28a59770d7d314)*.*

When a task feels too big to start, Naomi sets a timer for 20 minutes and just goes. Cleaning, building, whatever she's been avoiding, she commits to 20 minutes and busts it out. The point isn't to finish. It's to start, because starting is the part that traps most of us, especially anyone prone to distraction or jumping between tasks.

**The principle:** you're not committing to finish, only to 20 minutes. That small commitment is enough to break the freeze.

---

## **Approach #2: Let AI pick your priority**

*Surfaced in *[*Community Call #17*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=37544182cb1d4659be28a59770d7d314)*.*

One member keeps a running thread in Claude or ChatGPT and dumps every idea into it through the week. Then on Sunday or Monday they ask it one question: "Based on everything I told you this week, what should my priority be?" Instead of staring at ten competing ideas, they get one clear next thing to work on.

**The principle:** offload the deciding. When everything feels urgent, let the AI sort the noise so you can just execute the top item.

---

## **Approach #3: Eat the elephant one bite at a time**

*Surfaced in *[*Community Call #17*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=37544182cb1d4659be28a59770d7d314)*.*

When a project feels overwhelming, the answer raised on the call was the oldest one there is: you eat an elephant one bite at a time. Don't try to see the whole thing done. Pick the single next action and do only that. The plan reveals itself as you move.

**The principle:** you don't need the whole path mapped. You need the next step. Take it, then find the one after.

---

## **Approach #4: Too many open doors? Walk through the one with a buyer behind it**

*Surfaced by Jesse in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

A new member arrived with 20 years of domains: home services EMDs, commercial real estate, short sales, four metro markets. Every door open, none walked through. Sound familiar?

What broke the freeze wasn't a prioritization framework. It was one concrete buyer: a broker in his co-working space who'd been paying $500/month for leads until his supplier died. Jesse's advice was to build for that one deal (three prepaid microsites) and ignore the rest. Learn the build on one live deal, then repeat it per broker, per market.

**The principle:** options don't need ranking, they need a customer. Pick the door with real demand behind it and let the other doors wait.

---

## **Approach #5: Quit the thing that isn't responding**

*Surfaced by Shlomi in *[*Community Call #46*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4a44deed9af404987fb2f92941daac2)*.*

Half of overwhelm is dead projects still on the list. Shlomi put months into a restaurant SEO project before accepting the niche doesn't respond to content (reviews are the ranking lever there). He closed it without drama: "It was a nice ride, a nice attempt. It was a lesson."

**The principle:** shipping consistently includes shipping endings. A project that can't win is weight, not work.

---

## **Approach #6: Stop polishing, start buying data**

*Surfaced by Jesse in *[*Community Call #43*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=e315b592808940c1a8106ea311e4fe3d)*.*

A member was building four microsites a day, all the exact same way. Jesse's push: stop repeating one recipe and start testing variables. Group A gets backlinks, group B gets nothing, group C gets a different link type. "What you're doing now is buying data." In six months you know what actually works instead of having one big untested bet.

**The principle:** volume without variation is superstition. Ship variants and let the results decide, instead of agonizing over the perfect approach upfront.

---

## **Approach #7: Keep one source of truth, then ask it what today's move is**

*Surfaced by Kate in *[*Community Call #44*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=bcb6a7bbb1fd4ef5911b489dad6a3c4b)*.*

Kate logs everything twice: Claude commits every site change to GitHub, and writes it to one big Google Sheet, her "2026 content dashboard." Every project and step is recorded, so any AI agent can pick up the thread cold. Then each morning she asks Claude one question, per site: "What should I be doing today?" and it answers from the log.

This is Approach #2 grown up: instead of a loose idea dump, the AI prioritizes from a complete record of what's actually done and pending.

**The principle:** the freeze comes from holding the whole map in your head. Put the map in one place the AI can read, and let it hand you the next step.

---

*More approaches will be added here as they surface on the calls.*

---

> **Try this**

Pick the one task you've been avoiding longest. Set a timer for 20 minutes and start it now. Don't aim to finish, just to begin. Notice how much further you get than you expected.

**💬 Discuss this in the community**

## Getting Clients When Cold Outreach Feels Dead

*Last updated: 4 June 2026*

---

## **Everyone Is Tired Of The Same Pitch**

Cold email, voicemail drops, automated funnels, "AI-powered" everything. Prospects have seen all of it, and they've learned to tune it out. The harder you lean on the same automated tactics everyone else uses, the more invisible you become. The fix isn't a better automation. It's standing out in the ways automation can't.

Below is a running collection of approaches our members have shared on the calls for landing clients when the usual outreach has gone stale.

---

## **Approach #1: Be the human, not the bot**

*Surfaced by Blair in Community Call #34.*

People are so used to AI ads and automated outreach that a real human on the phone is now the surprise. Blair opens cold calls with exactly that: "I'm a real person in South Carolina, not AI." It stops people, because it's the opposite of what they're braced for.

It sounds almost too simple, but in a market drowning in automation, being unmistakably human is the differentiator.

**The principle:** when everyone automates, the human touch becomes the edge. Lead with it.

---

## **Approach #2: Give them a reason to pick up**

*Surfaced by Blair in Community Call #39.*

A cold call with no reason behind it gets hung up on. So Blair built a reason. He wrote a Claude prompt that runs an instant "AI visibility" check on a prospect's site, grading the seven things AI looks for. He's not a coder, just a prompt.

Then the call has a hook: "I'm on your About page right now, and here's what I'm seeing." It's specific, it's about them, and it opens a real conversation instead of a pitch.

**The principle:** the call works when you arrive with something useful about their business, not a generic offer.

---

## **Approach #3: Facebook and Meta ads as the cheap lead engine**

*Surfaced in Community Call #39.*

A catchy video ad can reach the right prospects for around $49. One member's lead-gen stack, in order: rank your own city sites, then cold and warm email, then Facebook and Instagram ads through Meta. The ads keep the pipeline full when the other channels go quiet.

**The principle:** don't rely on one source. Stack a few so a slow week on one doesn't dry up your leads.

---

*More approaches will be added here as they surface on the calls.*

---

> **Try this**

Pick your next cold call and change one thing: open with something specific and human about their business, not your offer. See how far the conversation gets before they try to hang up.

**💬 Discuss this in the community**

## AI Stacks Members Are Actually Using

*Last updated: 16 June 2026*

---

## Too Many Tools, No Map

There are a thousand AI tools and a new one every week. Everyone online is shouting about a different one, and it's impossible to tell what actually moves the needle in a business like yours versus what's just noise. The result is the forest-for-the-trees problem: so many options that you freeze instead of building.

This lesson is the map. Below are the real stacks members are running right now, grouped by the job they do. Don't read it front to back. Jump to the job you're trying to solve and see what's actually working, and on which exact tools.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/c89e778526dc4082be5721063296e2a783b7843abc884565a5dbd8d6fd47c446-md.png)

---

## Content & Pages

### **Stack #1 - Shawn's programmatic page recipe**

*Surfaced by Shawn in *[*Community Call #6*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=e6f5ffc976494c35aea7adf551574382)*.*

**The principle:** break a page into parts, give each part its own specialized generator, and you can produce hundreds of optimized pages instead of one at a time.

Shawn built a separate custom GPT for every individual paragraph and section of a page, each with very specific instructions, then assembled them into semantically optimized pages. One rough build produced 300 pages in a month or two and pulled 50,000 to 70,000 pageviews a month at peak. Run it manually, or off a location CSV to do it programmatically.

**Tools**: a library of custom GPTs (one per page section), a location CSV.

---

### **Stack #2 - The dual-AI content and image build**

*Surfaced in *[*Community Call #25*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=d26da71f7cd249458c2ca4a820d22efa)*.*

**The principle:** the words are only part of the asset. Two models cross-checking, plus genuinely custom images, produce pages that read like a team made them.

This member writes long-form "monster pages" (4,000 to 5,000 words, no fluff) by running two AIs back and forth against each other to find and fill content gaps, then generates custom graphics through nano banana. Every few paragraphs the page pivots to a call or quiz-funnel CTA.

**Tools**: ChatGPT and Claude (run against each other), nano banana (Google Gemini's image model, [gemini.google.com](http://gemini.google.com)).

---

### **Stack #3 - The Claude writing tool built for VAs**

*Surfaced in *[*Community Call #28*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=52131403bb674ab2beb5f506ffd2dea0)*.*

**The principle:** don't just delegate the task, delegate a tool. Build the judgment into Claude once, then hand the VA something that already knows the standard.

Instead of training a VA on every nuance of his content process, this member built a writing tool in Claude that encodes exactly what he wants, then handed it over. The VA runs the articles, listicles, and image sourcing through it. He trained the system once instead of training a person repeatedly.

**Tools**: a custom writing tool built in Claude.

---

## Building Sites At Scale

### **Stack #4 - The Claude Code WordPress factory**

*Surfaced in *[*Community Call #26*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=8f60758ad8af4faa8402c55d2f60cfa5)*.*

**The principle:** structured prompts beat credit-based vibe coders. Once you outgrow the training wheels, Claude Code plus Skills is dramatically cheaper at scale.

A member who admits he can't code vibe-coded his own WordPress theme and plugin through Claude Code. It builds pages and pushes them straight to WordPress, with separate agents per job (one builds pages, one adds schema, one does internal linking by reading the surrounding content and dropping contextual links). He chains Anthropic Skills together and runs the whole thing on a $200/month Claude Max plan instead of burning thousands in credits on platforms like Lovable or Replit.

**Tools**: Claude Code on the Claude Max plan ([claude.com/claude-code](http://claude.com/claude-code)), Anthropic Skills, WordPress.

---

## Lead Capture

### **Stack #5 - The voice-AI that books leads at 3am**

*Surfaced in *[*Community Call #8.*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=f6f0cf7a9a5e4fdcb95db5757f904654)

**The principle:** an AI front desk doesn't sleep. For a service business losing after-hours calls, that alone is an easy thing to sell.

A member running voice AI for a client watched it catch a real lead and book an appointment at two or three in the morning, hours no human receptionist works. The bigger insight raised on the call: most of the value isn't the voice AI itself, it's what you do with the data it captures (why people call, why they hang up). The voice agent is the front door; the brain sits behind it.

**Tools**: a voice-AI agent feeding into GoHighLevel ([gohighlevel.com](http://gohighlevel.com)).

---

## Client Ops & Onboarding

## **Stack #6 - Seth's SMS-first contractor brain**

*Surfaced by Seth in *[*Community Call #27*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=15ee82614ca046409cc5403f1cf1b790)*.*

**The principle:** AI's best use is often an interface layer over tools that already exist. Don't replace the CRM. Remove the part of it the user hates.

Seth hates living in his CRM between job sites, so he's wiring an AI agent through Twilio that connects to GoHighLevel and his financial data. He texts it the project details, and on a schedule it runs a P&L and job-costing analysis so he knows what he actually made on each job. He's already pitched it to three contractors who'd pay $4,500 to $6,000 to build, plus a hosting fee.

**Tools**: Twilio ([twilio.com](http://twilio.com)), GoHighLevel ([gohighlevel.com](http://gohighlevel.com)), an AI agent layer.

---

## **Stack #7 - Leadsie for one-click client access**

*Surfaced in *[*Community Call #27*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=15ee82614ca046409cc5403f1cf1b790)*.*

**The principle:** the fastest part of onboarding to fix is access. One tool removes the slowest step in week one.

Members who hear about this one tend to sign up the same day. One email to the client, they answer a few questions, and in a single click you get access to their Google Business Profile, Google Analytics, Search Console, and Facebook/Meta ad accounts, all in one dashboard. It replaces the "send me an invite to your GBP" chain that kills the first week of every engagement.

**Tools**: Leadsie ([leadsie.com](http://leadsie.com)).

---

## Scaling

### **Stack #8 - Kate's custom DataForSEO MCP**

*Surfaced by Kate in *[*Community Call #36*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=c4b8d2e4ba824c9b9e5d54b19679aa98)*.*

**The principle:** MCP is the unlock most people are sleeping on. Any API you already pay for can be wired into Claude in an afternoon.

Kate built her own MCP connector to DataForSEO inside Claude Code, then used it to run hours of niche brainstorming directly in Claude, pulling real data to validate and ditch niche ideas. No tool-switching, just Claude reasoning over live SERP data.

**Tools**: DataForSEO ([dataforseo.com](http://dataforseo.com)), a self-built MCP connector in Claude Code.

---

### **Stack #9 - Brandon's GHL-at-scale consolidation**

*Surfaced by Brandon in *[*Community Call #25*](https://www.skool.com/rank-expand-academy/classroom/9bbd4400?md=d26da71f7cd249458c2ca4a820d22efa)*.*

**The principle:** at small scale, multiple specialized tools win. At real scale, consolidating onto one platform wins.

At Brandon's volume, GoHighLevel runs everything: CRM, voice agent, phone system, and tracking-number infrastructure in one platform. He builds number pools, drops them on microsites, tracks which site produces which call, and tightens his intake so only high-quality leads reach the client.

**Tools**: GoHighLevel ([gohighlevel.com](http://gohighlevel.com)).

---

*More stacks will be added here as they surface on the calls.*

---

## **The pattern**

Nobody here is buying their stack off the shelf. They're stitching cheap APIs together, building custom MCPs, vibe-coding their own tools, delegating tools instead of tasks, and replacing whole SaaS subscriptions with a single Claude Max plan. The map isn't "use these nine tools." It's "pick the job in front of you, then reach for the simplest thing that does it."

> **Try this**

Pick the one job costing you the most time right now (writing, building, lead capture, onboarding, or admin). Find the stack above that matches it and copy just that one. Don't rebuild your whole toolkit. Solve one job.

**💬 Discuss this in the community**

## Getting Cited by AI

*Last updated: 23July 2026*

---

## **Getting Mentioned Is the New Ranking**

When someone asks ChatGPT or Gemini who to hire, the AI repeats back what it already sees cited. So the work moves to wherever the AI reads. Two full calls went deep on this. Below are the moves members are running right now.

---

## **Move #1: Find the invisible URLs AI already trusts**

*Surfaced in Community Call #44, built out and shared by Jesse in Community Call #45.*

Take your top queries from Google Search Console (say 30 per client) and turn each into a question. Use DataForSEO to check which third-party pages ChatGPT and Gemini cite for each one. Aggregate everything (250-500 URLs) and sort by citation frequency. The URLs cited 10+ times are the invisible layer: pages the AI leans on constantly that show up on zero backlink tools. "Ahrefs can't see them."

Then outreach those URLs and get listed, sometimes for as little as $50. That's your backlink target list, sourced from AI behavior instead of domain authority. Jesse turned the whole build into a Fable prompt: the "Invisible URLs = AI Visibility Outreach Targets" lesson in the classroom. Cost note: pulling AI results via DataForSEO costs money, so run the discovery once or monthly, not daily.

**The principle:** stop guessing which links matter. Ask the AI where it reads, then go get listed there.

---

## **Move #2: Get mentioned where the AI reads: YouTube, Facebook groups, Reddit**

*Surfaced by Jesse and Justin in Community Call #44.*

A study shared on the call found YouTube mentions are the single biggest factor in AI mentions, and YouTube is the #2 cited source behind Reddit. Justin is acting on it: affiliate YouTube accounts for his water-treatment company, cranking out videos.

Local Facebook groups are the contractor version: profiles active in the local town groups recommending a business absolutely get cited inside Gemini and ChatGPT. And the cheap on-page move: list every social profile on your pages with sameAs schema so the entity connects.

**The principle:** AI answers are a mirror of public conversation. Put your client's name where the conversation happens.

---

## **Move #3: Third-party beats self-praise (the persona listicle)**

*Surfaced by Blair in Community Call #45.*

AI detects a self-bought press release as paid press and discounts it. Blair's workaround: publish a listicle on an unrelated site under a completely separate author persona ("best roofers in Charlotte NC"), front-loading "best [service] in [city]" in the title and first line. It reads as third-party verification, and it triggers citations a direct press release never does.

**The principle:** the AI weighs who's talking, not just what's said. Independent-looking praise outranks your own.

---

## **Move #4: Expired-domain sponsorships (local links for $20)**

*Surfaced by Blair in Community Call #45.*

Buy the expired domains of past local 5Ks, charity walks, and events ($20-50 each plus ~$5/month hosting), relaunch the site, and list your clients as sponsors. The link is genuinely local, dirt cheap, and one relaunched event site serves 4-5 clients. Same spirit as the Call #43 sponsorship play (search `[city] "sponsorships"` and give back for a legit local link), sourced from dead event domains instead.

**The principle:** local trust signals don't have to be expensive. They have to be real-looking and genuinely local.

---

**Move #5: The profiles page that indexes your citations**

*Surfaced in Community Call #44 (a Bradley Benner idea, updated by Claude).*

The old two-tier play was Web 2.0 properties backlinking to your citations. The refresh: create a /profiles page on your own site, link out to all your citations and social profiles from it, and index that page. It's a trusted page on your own domain, so it gets crawled and cited, and the citations it links to get indexed, becoming indexed backlinks pointing back at you.

**The principle:** your own domain is the most reliable indexing tool you have. Use one page of it to power up everything pointing at you.

---

*More moves will be added here as they surface on the calls.*

---

## Scaling Past Doing Everything Yourself

*Last updated: 22 July 2026*

---

## **The Solo Ceiling Is Real**

Solo, you cap out around 15-20 clients. Every member who has pushed past that did the same uncomfortable thing: they stopped being the person who does the work and became the person who runs the system that does the work.

---

## **Shift #1: Loom everything now, hire before you're ready**

*Surfaced by Blair in Community Call #45.*

Blair's push: record a Loom video of every task you do, starting today, so the work is teachable the moment you hire. Filipino VAs are excellent when trained (junior-to-senior level at roughly 1/10th the cost of Western juniors), but build the arrangement to survive churn: they come and go, so the training library is the asset, not the person.

The goal state, in Blair's words: "Become the person who talks to the client and manages the work, not the person who does the work." One caveat he insists on: AI taken as gospel will embarrass you in front of a client. Keep a human review in the loop.

**The principle:** you can't delegate what only exists in your head. Record it once, and every future hire starts trained.

---

## **Shift #2: Put boundaries on the service, not just the price**

*Surfaced by Teja in Community Call #43.*

Teja's $100/month website clients don't get on-demand changes. The policy: "We do a quarterly review of the website. We're not changing it until then. That's why it's a hundred dollars a month." His VA handles change requests only; everything else is automated. The boundary is what makes the cheap price profitable, and clients accept it because it's stated up front.

**The principle:** scale dies from unlimited scope faster than from low prices. Define what the money buys, out loud.

---

## **Shift #3: Train the system, then let anyone (or anything) run it**

*Surfaced by Kate and Shlomi in Community Call #44.*

Kate logs every project step to GitHub and a master Google Sheet so "any agent can pick up the source of truth." Shlomi does the same with ClickUp plus a running memory file, updated after every dev cycle. The point isn't the tool: it's that the process lives outside any one person's head, so a VA, a new hire, or a Claude agent can pick up mid-stream without a handover meeting.

This is the same move as the Claude writing tool for VAs in the AI Stacks lesson: encode the standard once, then people and agents plug into it.

**The principle:** systems scale, heroics don't. If the work only happens when you remember how, you're the bottleneck by design.

---

*More shifts will be added here as they surface on the calls.*

---

## Keeping the Clients You Have

*Last updated: 23 July 2026*

---

## **Retention Is Where The Money Compounds**

Winning a client costs weeks. Keeping one costs a phone call. The members with the slowest churn aren't the ones who never break anything: they're the ones whose clients would feel the loss personally.

---

## **Habit #1: The relationship forgives what perfection can't prevent**

*Surfaced by Blair, Shlomi, and Shawn in Community Call #45.*

Long thread, one conclusion: clients forgive broken things and missed deadlines when the relationship is strong. Blair: "We are way harder on ourselves than our clients are." Do the reports, make the calls, show you care, and the client stays even when the work slips. Shlomi's version: "If you truly care about a client and that comes through, that is what matters." Shawn's concrete example: he spent an hour on Zoom setting up a 70-something client's Office 365 email. That client has been golden ever since, on email love alone.

**The principle:** clients don't churn over mistakes. They churn over feeling like a line item. Make them feel like neither.

---

## **Habit #2: Make the invisible work visible**

*Surfaced by Jesse in Community Call #46 and Teja in Community Call #44.*

Automated work has a retention problem: the client can't see it happening. Two fixes. Jesse wires Mailgun into his automated client systems so Claude emails the client every update it makes; the perceived value climbs with every message. Teja auto-generates 50 days of rotating social posts per client (plus auto-posting their 5-star reviews), and the client believes Teja is posting by hand every day.

**The principle:** value the client can't see is value they won't pay for next month. Ship the proof along with the work.

---

## **Habit #3: Intertwine, don't just retain**

*See "What To Charge And How To Structure Deals" in this course.*

The structural side of retention lives in the pricing lesson: stack two or three services (site, hosting, tools, retainer) so leaving becomes genuinely painful, and Teja's version where the site, CRM, profile, and posts arrive as one infrastructure nobody wants to untangle.

---

*More habits will be added here as they surface on the calls.*

---
