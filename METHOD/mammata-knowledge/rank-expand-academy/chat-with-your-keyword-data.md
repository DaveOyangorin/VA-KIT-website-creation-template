# ⚡ Chat With Your Keyword Data

> Source: AI SEO: Rank Expand Academy (Skool) — `classroom/5d44ffd9`  
> 8 lessons · 3 videos (~19 min) · 12 KB of written material  
> Internal reference for MAMMATA. Not for redistribution.

---

## Why Build Your Own AI SEO Assistant?

🎥 [Loom](https://www.loom.com/share/2426b16f13b248a5b1d6a4e4a137bb6d?sid=e7bd124f-138d-4657-a757-e37ef5fc49cb) · 5:12

I used to find keyword research a grind.

Exporting endless CSVs, scrolling through columns, setting up filters in Google Sheets—it eats up hours.

And after all that, you still end up staring at a wall of numbers thinking: *“Okay… but what does this actually mean for me or my client?”*

That’s where your personal AI SEO Assistant comes in. Instead of slogging through spreadsheets, **you just… ask.**

- “What are some low-competition keywords around *roofing in florida* that could bring in leads?”
- “Which opportunities are my competitors ranking for that I’m missing?”
- “Summarize the SERP features for my top 20 keywords.”

It gives you straight answers pulled straight from live keyword data. No exporting, no fiddling with filters—just insights on demand.

- It saves you time (no more CSV gymnastics).
- It speaks your language (plain English questions).
- It makes SEO research fun again.

By the end of this training, you’ll have your own assistant sitting inside ChatGPT—ready to pull fresh keyword and SERP data whenever you need it.

## Chat With Your Keyword Data

🎥 video · 5:12

A couple of months ago, DataForSEO released their custom action you can hook up straight to ChatGPT.

Instead of pulling exports from everywhere and compiling it into spreadsheets, you can literally **have a conversation with your keyword data.**

Actual keyword data, actual live SERPs, not the stuff ChatGPT makes up and some people call 'good enough'.

Now, you can go back-and-forth like you would with a teammate:

- You: “Which keywords in my cluster have low CPC but decent traffic?”
- Assistant: “Here are 5 solid ones under $1 CPC with over 1,000 searches each.”
- You: “Nice. Which of these show a featured snippet I could target?”
- Assistant: “Three of them—want me to outline what those snippets look like?”

It uses the DataForSEO API to pull actual keyword data and uses ChatGPT's logic model to analyze and reason.

That’s the game-changer. Instead of wasting time digging, you’re **exploring.** Instead of crunching, you’re **strategizing.**

And that’s exactly what you’ll set up in the next module—your own assistant that doesn’t just give you raw data, but helps you think with it.

## Setting Up Your SEO Researcher

### What You'll Need

This is a professional-grade tool, and it comes at a cost.

You will have to pay for DataForSEO's API usage, and you'll need a paid ChatGPT subscription.

DataForSEO runs on credits.

If you're serious about SEO, I promise it will be worth the cost 10x.

The cost are marginal compared to the time saved and the cost saved on keyword research tools.

DataForSEO is one of the most affordable options for pulling SEO data.

A heavy day of work at our agency usually runs us between $1-$2 of API usage.

$1-$2 buys you thousands of pulled keywords, back and forth on competitors, scraping the SERPs, and compiling content briefings for dozens of pages.

Our average spend over the last four months was $8 / mo.

It was the best $30 I spend over my entire career as an SEO.

### Set Up Your Personal AI SEO Research Assistant

🎥 [Loom](https://www.loom.com/share/298b28e17d394e64a00f9fbf8416a1af?sid=47dc3bcc-f7dc-49cf-afde-c918480b42e8) · 8:10

In this module, we're going to set everything up. You don’t need to be a developer to pull this off. If you can copy-paste and follow steps, you’re good. Here’s the roadmap:

## **Get your tools ready**

- First, you’ll need a [DataForSEO account](https://dataforseo.com/?aff=197083). That’s where our keyword and SERP data is coming from.
- **Some members have pointed out that you need to deposit $50 initially in credits.**
- Second, you’ll need ChatGPT (CustomGPTs) so we can connect the dots.
- Think of DataForSEO as your data engine, and ChatGPT as your assistant’s brain.

## **Grab your API credentials**

- Once you’re inside DataForSEO, they’ll give you an API username and password.
- Save those—you’ll plug them into ChatGPT in just a minute.

## Grab the OpenAI Actions from DataForSEO

DataForSEO has created a toolkit with OpenAI actions you can plugin to your CustomGPT. You can find all of them here: [https://github.com/dataforseo/open-ai-actions/](https://github.com/dataforseo/open-ai-actions/)

The one you'll want is called the [Researcher Toolkit](https://github.com/dataforseo/open-ai-actions/blob/fa11cee5a26cf49f648653e0414a966d353496f5/dataforseo_researcher_toolkit.json). It combines all the endpoints and knows which one to call when.

## **Create your CustomGPT**

1. In ChatGPT, go to *Explore GPTs → Create*.
2. Give it a name (I've called ours “SEO Research Assistant”).
3. Jump to the **Actions** tab. This is where we tell ChatGPT how to fetch your keyword data.
4. **Connect the API (this is where the magic happens)**

- Add a new Action.
- Plugin the Researcher Toolkit JSON code you've downloaded.
- Plug in your API credentials under *Authentication*.

#### Click Create New Action

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/8386574cc15c4c4bb54d5457428c967e4d22987236c44781a1145cb325c176e4-md.png)

#### Click Authentication to open the popup

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/3027c39aee024949a33adb112490bb62c50d51efe3ad4d3b9cce63bced791a43-md.png)

#### Enter your API Key

Select *API Key* and *Auth Type: Basic*. Then use your [**Base64-encoded login details**](https://www.skool.com/rank-expand-academy/classroom/5d44ffd9?md=59dc11aac0114a2c997da6ac4fb56167) for DataForSEO as your API Key.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/afedbc6efc57453398873f276b19e3247fbe548daede471c9c1972b71b619d09-md.png)

## **Test it out**

Now type in something like:

> “Perform a full SEO audit of my domain https://mydomain.com/. Run a competitive analysis and find keyword gaps. Based on that, recommend my three highest-impact SEO actions. Use DataForSEO.”

> **Please note**: lately we need to add 'Use DataForSEO' to the prompt in order for it to pull from the API so make sure to include it when you prompt the Assistant.

If everything’s hooked up right, ChatGPT will call the DataForSEO API and bring you back fresh keyword data… in plain English.

That’s it. You now have a personal AI SEO Research Assistant.

### Finding your DataForSEO API key

🎥 [Loom](https://loom.com/share/af0c7c71c1d6495a9025dd79021210ac) · 0:19

## Step 1: Navigate to API Access

- Go to the API access section of the platform.
- Select the option to send the API key by email.

## Step 2: Check Your Email

- Open your email inbox.
- Look for an email containing your API key.

 

## Step 3: Copy the base64 API Key

- The email will contain a clear base64 value of the API key.
- Copy the base64 encoded string provided in the email.

## Step 5: Use the API Key in Chat-GPT

- Paste the copied API key into Chat-GPT, select Basic Authorizatoin.

## Bonus Material

### Project Parser

The purpose of the "Project Parser" custom GPT is to give you exact prompts to then use with the SEO Research custom GPT you created earlier in this module.

**Copy and paste everything below this bolded sentence into your CustomGPT's Instructions (you need to create a new custom GPT similar to how you did previously in this module):**

You have access to these different prompts - take what I input and tell me specific prompts I can use with the data (give unique prompts with the URL mentioned):

Here’s a 1:1 mapping of operationId → the natural-language prompt you’d send (fill in the bracketed variables):

serp_organic_live_advanced

“Get live organic SERP results for keyword <keyword> in <search_engine> with language code <language_code>, location <location_name>, depth <depth>, max crawl pages <max_crawl_pages>, device <device>, and PAA click depth <people_also_ask_click_depth>.”

keywords_data_google_ads_search_volume

“Fetch Google Ads search-volume data for keywords [<keyword1>, <keyword2>, …] in location <location_name> and language <language_code>.”

keywords_data_dataforseo_trends_explore

“Explore Trends data for keywords [<kw1>, <kw2>, …] of type <web|news|ecommerce> from <date_from> to <date_to> in <location_name>.”

on_page_content_parsing

“Parse the page at <url>, with JavaScript enabled=<true|false>, custom JS=<custom_js>, UA=<custom_user_agent>, accept-language=<accept_language>.”

on_page_instant_pages

“Run an instant on-page SEO audit for <url> with JS enabled=<true|false>, custom JS=<custom_js>, custom UA=<custom_user_agent>, accept-language=<accept_language>.”

dataforseo_labs_google_ranked_keywords

“Get up to <limit> ranked keywords for target <domain_or_url> in <location_name>, language <language_code>, offset <offset>, filters <filters>, order_by <order_by>, include subdomains=<true|false>, include clickstream=<true|false>.”

dataforseo_labs_google_competitors_domain

“Compare competitor domains for target <domain> in <location_name>, language <language_code>, ignore synonyms=<true|false>, limit <limit>, offset <offset>, filters <filters>, order_by <order_by>, exclude top domains=<true|false>, include clickstream=<true|false>.”

dataforseo_labs_google_domain_rank_overview

“Get domain rank overview for <domain> in <location_name>, language <language_code>, ignore synonyms=<true|false>.”

dataforseo_labs_google_keyword_ideas

“Generate up to <limit> keyword ideas based on seed keywords [<kw1>,…] for <location_name>, language <language_code>, offset <offset>, filters <filters>, order_by <order_by>, include clickstream=<true|false>.”

dataforseo_labs_bulk_keyword_difficulty

“Fetch Keyword Difficulty for keywords [<kw1>,<kw2>,…] in <location_name> and language <language_code>.”

dataforseo_labs_google_subdomains

“List up to <limit> subdomains of <domain> in <location_name>, language <language_code>, ignore synonyms=<true|false>, offset <offset>, filters <filters>, order_by <order_by>, item_types <item_types>, include clickstream=<true|false>.”

dataforseo_labs_google_keyword_overview

“Get keyword overview for keywords [<kw1>,…] in <location_name>, language <language_code>, include clickstream=<true|false>.”

dataforseo_labs_google_keywords_for_site

“Fetch up to <limit> relevant keywords for target <domain> in <location_name>, language <language_code>, offset <offset>, filters <filters>, order_by <order_by>, include_subdomains=<true|false>, include clickstream=<true|false>.”

dataforseo_labs_google_domain_intersection

“Find up to <limit> intersecting keywords between domain1 <target1> and domain2 <target2> in <location_name>, language <language_code>, ignore synonyms=<true|false>, offset <offset>, filters <filters>, order_by <order_by>, intersections=<true|false>, include clickstream=<true|false>.”

dataforseo_labs_google_historical_rank_overview

“Get historical rank overview for <domain> in <location_name>, language <language_code>, ignore synonyms=<true|false>, include clickstream=<true|false>.”

dataforseo_labs_google_page_intersection

“Compare page intersection for pages {1:<url1>, 2:<url2>}, excluding [<exc1>,…], mode=<union|intersect>, in <location_name>, language <language_code>, ignore synonyms=<true|false>, limit <limit>, offset <offset>, filters <filters>, order_by <order_by>, include clickstream=<true|false>.”

dataforseo_labs_bulk_traffic_estimation

“Estimate traffic for targets [<t1>,…] (domains/subdomains/URLs) in <location_name>, language <language_code>, ignore synonyms=<true|false>.”

dataforseo_labs_google_historical_serp

“Get historical SERP for keyword <keyword> in <location_name>, language <language_code>.”

backlinks_backlinks

“List up to <limit> backlinks for target <target_url_or_domain>, mode <as_is|one_per_domain|one_per_anchor>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_anchors

“Fetch up to <limit> anchor texts for target <target>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_domain_intersection

“Get link-gap domains between targets 1:<dom1>, 2:<dom2>, limit <limit>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_domain_pages_summary

“Summarize backlink data by page for target <target>, limit <limit>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_domain_pages

“List up to <limit> pages with backlink data for <target>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_page_intersection

“Page-level link-gap between targets 1:<t1>, 2:<t2>, limit <limit>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_referring_domains

“Get up to <limit> referring domains for <target>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_referring_networks

“Fetch referring networks for <target>, type <ip|subnet>, limit <limit>, offset <offset>, filters <filters>, order_by <order_by>.”

backlinks_summary

“Get high-level backlink summary for <target>, include_subdomains=<true|false>, exclude_internal_backlinks=<true|false>.”

backlinks_timeseries_summary

“Fetch time-series backlink summary for <target> from <date_from> to <date_to>, grouped by <day|week|month|year>.”

backlinks_bulk_pages_summary

“Bulk summarize backlink data for targets [<t1>,…] (max 1,000), include_subdomains=<true|false>.”

backlinks_available_filters

“List all available filters for DataForSEO Backlinks API.”
