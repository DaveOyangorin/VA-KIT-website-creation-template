# Semantic Site Audit & Tools — Video Transcripts

> Machine transcripts of the course videos (Rank Expand Academy, Skool) — Loom captions,
> or YouTube captions for the YouTube-hosted lessons. Timestamps preserved.
> Internal reference only — not for redistribution.
> Caveat: names, tool names and acronyms are occasionally mis-transcribed. Treat exact
> strings with suspicion; the substance is sound.

---

## What Semantic Drift Is & Why It Matters

🎥 https://www.loom.com/share/c57e8681f78348d3ad5d2c6720d758bd · ~4 min · 67 cues

[0:00] Today we're gonna go over something incredibly helpful.
[0:04] We're gonna talk about semantic drift and how to
[0:09] fix it. So, if you have a side with lots of pages this is
[0:13] an old side for example, or you wanna know where to branch out to
[0:17] next, this is a very useful tool.
[0:20] semantic drift is when a page slowly moves away from the original topic of
[0:24] the cluster, either because the content changed,
[0:27] the SERP changed, or the side structure shifted.
[0:30] And so, it's very useful for us to know how Google,
[0:33] uh, interprets our side structure and our core,
[0:36] what it identifies as being our core topics,
[0:39] and how far out certain pages are,
[0:42] or how well they are within the core of our website.
[0:45] So, if we can- All right.
[0:48] Identify pages based on these,
[0:50] uh, criteria, we get a map of sorts to
[0:56] see how focused is our website,
[0:58] actually. This is a tool I found,
[1:02] uh, of LinkedIn, uh,
[1:04] some- somebody I follow on LinkedIn.
[1:07] Uh, a very good international SEO that provides very good- tools,
[1:12] and so we have access to the codebase, we can use it freely.
[1:16] It's called the Semantic Drift Analyzer. You'll need a paid screaming frog license.
[1:22] There are, I think, other ways to go about it.
[1:24] Uh, I'll show you what you'll need. But you'll need an export of your-
[1:28] of your entire site with all the internal linking in it,
[1:31] uh, as well as embeddings.
[1:35] And screaming frog- break. 8 gives a very nice way to- to do that
[1:38] now. Show you how to do it and tell you what it is in
[1:41] a minute. So you'll be able to spot pages that have drifted away from
[1:46] the original topic of the site or the site core has shifted over time.
[1:52] And that, um, um, will give us the input we need to turn it
[1:55] into a focused optimization plan.
[1:59] Why does it matter? Well- Symantec Drift is a big deal.
[2:03] It weakens topical authority, creates weird pages,
[2:06] and my biggest site, my theory is that it got hit by H.U.
[2:11] back in the days because I started branching out into TV shows.
[2:16] It was about sailing, and then I thought, this is a sailing related to
[2:19] v-show, but it was more of a, um,
[2:23] celebrity show. Let's- say. It can drag down into a link equity,
[2:28] uh, it's considered outliers,
[2:30] and we're gonna keep the focus. And so,
[2:33] before we had to guess what the core topic was
[2:37] of our site, and which pages were inside of that,
[2:41] and which weren't. Now we have a way to visualize it,
[2:44] makes it very clear and easy to fix things.
[2:47] So, This tool shows you which pages are drifting based on semantic distance.
[2:53] It combines content vectors. So it vectorizes your actual content,
[2:58] and gives it a score, or a, uh,
[3:01] uh, value, and then you can analyze,
[3:04] or the tool will, analyze the relevance of each page based on those vectors.
[3:10] And gives you a radial map of your, cl- faster health.
[3:14] So when do you need this? When you have a large site with lots
[3:17] of old blood logs, when you are thinking about doing some content pruning,
[3:21] e-commerce product catalogs, any site with migrating content,
[3:25] so if you want a clean house, um, or teams that publish without cluster
[3:29] guardrails. So if you're branching out really quickly,
[3:31] this can give you some guardrails.
[3:35] Let me- show you real quick. I'll pull up a semantic.
[3:39] Uh, no, let's-let's set up the tools from scratch first.
[3:42] Uh, I'll-I'll, uh, I'll add a screenshot of the semantic map below
[3:47] here so you can get a teaser, a preview.
[3:50] But I've uninstalled all the software from my computer so that we can get
[3:55] a clean walkthrough, walk through it, uh,
[3:58] through it together one by one. And, uh,
[4:00] You will do that next. See you in the next module.
[4:02] So,

---

## Quick Start Guide

🎥 https://www.loom.com/share/9e39b8fca24846819ce7d876693bcc0d · ~2 min · 29 cues

[0:00] Let me just go over the basics really quickly,
[0:02] this is a quick start guide, so we're gonna find pages that drift from
[0:05] there topic. Um,
[0:08] we're gonna use a tool, and the tool runs locally on your machine.
[0:12] Uh, we need a screaming frog install with open AI and beddings enabled.
[0:17] Most of you, or some of you, will at least have a screaming frog
[0:20] account. If you don't you can use the trial version uh,
[0:24] up to 500 pages is free to crawl,
[0:26] so if you're a smaller site, this could work.
[0:29] I'm not sure if the open AI and beddings will work.
[0:32] We export all the URLs, uh, to a CSV with address,
[0:36] so URL, open AI embeddings, so a vector,
[0:39] and in links, so all the internal links to this page.
[0:43] Then we export Google search console, uh,
[0:46] CSV with page, clicks, uh, for,
[0:49] let's say last three months, and then we run these commands locally,
[0:53] one by one, in terminal, and that is basically what we need to do.
[0:57] So I'll walk you through each step here,
[1:00] one by one next. Uh,
[1:02] and here's what we need, uh, Mac or PC with Python 3.
[1:07] Get to, uh, to download the code,
[1:10] but you don't need a count. And this is more advanced stuff,
[1:14] so your skill level, you need to be comfortable installing apps,
[1:17] running terminal commands, uh,
[1:20] have basic understanding of internal linking, URLs,
[1:23] clicks, impressions, and content clusters. So if you qualify,
[1:26] if this is, is the, if this is something you are
[1:31] comfortable with doing, or you're comfortable learning,
[1:34] let's dive into the first step together.

---

## 1 - Install & Start Semantic Drift Analyzer

🎥 https://www.loom.com/share/bc49eb6dd9f84c78944b21df7a7dd8c4 · ~2 min · 44 cues

[0:00] So the first thing we need to do is we need to install the
[0:03] software and download the app.
[0:05] I use Terminal because I'm on macOS for this.
[0:09] So you open a new Terminal and you simply download the app by doing
[0:14] git clone. All right,
[0:17] so I didn't uninstall it completely, it seems,
[0:20] fatal destination path already exists is not empty,
[0:23] so I already, downloaded this. But that is all you need to do.
[0:26] Then we need to create and activate a virtual environment.
[0:30] And probably this is gonna throw an error. Oh, it doesn't.
[0:33] If you don't have Python 3 installed already,
[0:36] you need to install that first.
[0:39] And I would ask JetGBT, but it's the command is something like PIP 3
[0:42] or something. Not quite sure,
[0:45] uh, 100%, but installing Python 3,
[0:48] It's very straightforward. There's lots of resources you can,
[0:50] you can use to, to figure that out.
[0:54] Then next we need, uh, to activate our,
[0:59] uh, I think, virtual environment.
[1:03] So let's see. Done. And then we need to install dependencies.
[1:09] Alright, so requirement already satisfied.
[1:12] I'm to try one. Alright, so I have a bunch of things already,
[1:15] uh, already installed. I can install new
[1:20] Python. So this is the command I'm,
[1:22] I meant pip install. That is going to install Python for you.
[1:26] Now we're going to run the app. If you have worked with replet at
[1:29] all, you will recognize streamlet. And so this is to,
[1:33] this is a way to, uh, run streaml- game.
[1:36] They're on your own computer. And this is the semantic drift analyzer.
[1:39] So it's now installed. Very exciting. Uh,
[1:42] and we can now use it to upload our exports and run it,
[1:46] uh, to find,
[1:49] to find, uh, the semantic relevance of each page.
[1:53] So if you accidentally close the terminal,
[1:57] you get stuck in a little bit of a, uh,
[2:00] uh, between- between a rock and a hard place, uh, to sort of have-
[2:03] have a wall and a strip is what we say in Dutch. It's a
[2:05] maritime, uh, expression where you fall between the,
[2:09] uh, the, uh,
[2:12] harbor coast and the ship. Pretty,
[2:15] uh, gnarly. So this is what you should do if you close the terminal
[2:19] and accident. You need to re-activate the environment.
[2:24] Alright. . So next up we're gonna export the Screaming Frog CSV.
[2:28] SV.

---

## 2 - Export Screaming Frog CSV

🎥 https://www.loom.com/share/8ff8f073e62046d089ee99ee618ad819 · ~3 min · 58 cues

[0:00] We have our tool up and running and now we need to get our
[0:03] cz files. So we open screaming frog and we need to include
[0:08] an embedding column. You need to set that up so you need an opening
[0:10] AI key and,
[0:13] uh, configure this correctly. So I'll show you.
[0:16] We go in screaming frog, we open up screaming frog and then we go
[0:19] to. Let's see if I can make this work.
[0:24] Umm, I'm gonna make it a little bit smaller.
[0:28] There we go. So we need to go to configuration API access,
[0:33] AI open AI. So that's the one.
[0:35] AI open AI. There it is. Alright.
[0:39] Please don't steal my API key. Then we need to add it.
[0:44] So we just input it here. You go to the open AI platform.
[0:48] You go to your dashboard, you generate an API key,
[0:51] and then you punch it in here. Then we need to go to,
[0:56] uh, let's see, prompt configuration,
[0:59] or the font. No, no, we're not in here.
[1:02] We need to go to configuration, uh,
[1:05] content embeddings. And this is a new feature of,
[1:08] uh, screen and frog. And I've been wanting to test this out.
[1:11] out. And it's quite, quite awesome.
[1:14] For internal linking and things like that, it's very cool. Alright.
[1:17] So what we need to do is enable it.
[1:20] Uh, we need to configure at least one
[1:25] embedding prompt, which we don't have right here.
[1:28] And then what else we need to do, uh, yeah, a prompt that embeds
[1:31] the page content. Alright, so let's set that up.
[1:34] I think, uh, we do the- that here.
[1:37] If I remember correctly. So we do, yeah,
[1:43] so I have created a template. So open, uh,
[1:46] uh, add a new one, and then we do open AI embeddings.
[1:50] Number one is the name I called it.
[1:53] We do embeddings. We do text embedding three small,
[1:57] which is, uh,
[1:59] this one. HTML,
[2:03] page, text. That is what we need.
[2:06] Uh, not configure to store HTML.
[2:10] Enable store HTML via config spider extraction.
[2:13] We'll do that next. So we go to config spider extraction.
[2:18] And we say store HTML,
[2:21] store rendered HTML. There we go. So we now,
[2:24] So, we should be good now. Uh, this is all we need to do.
[2:28] It should now be, There we go.
[2:31] It should now be, Set up.
[2:34] Now we go to content, uh, embeddings.
[2:38] Enable, There it is. Embedding prompt. Excellent.
[2:42] You'll see enable semantic similarity. So this is a parball park.
[2:46] Alright. We crawl the side. I've already done, that.
[2:49] Umm, simply punch the ural in,
[2:51] say start, and it should show you an embeddings column.
[2:57] Don't know if it, you know, semantic search. Uh,
[3:00] and it will include an embeddings column here.
[3:04] Which is what we need, and then we do export.
[3:08] Uh, well, we should go to internal export.
[3:12] for and it will say internal all dot csv.
[3:15] So pull up that csv and we can load it up in our tool.
[3:19] And then we need to do, uh, obviously Google search console.
[3:23] Next.

---

## 4 - Use the Semantic Drift Analyzer

🎥 https://www.loom.com/share/12a0ae99bbc640f0a066e1fb70f4fa2c · ~4 min · 60 cues

[0:00] So I've run my exports and this is what it should look like.
[0:02] So this is the screaming frock export,
[0:04] and I'll just show it to you so you know what to look for.
[0:24] We need, we need, uh, in-links.
[0:27] Which will be somewhere down here.
[0:33] Unique out-links. Unique in-links.
[0:38] So this is the one. And then we need embeddings.
[0:41] And this is, uh, what it,
[0:44] what it did. So it will send each page to opening eye.
[0:48] And the process takes a while. It can take 10-15 minutes for a big
[0:50] site, uh, easily. And it will add a vector value.
[0:56] Vector embedding. Uh, and now it can compare all of these values.
[1:00] So this is all we need to do. We just want to verify that
[1:02] we have those columns in there. And then we have our Google
[1:07] search console export. This is the usual stuff,
[1:10] right? This is, uh, for- It knows this. This is the last three months,
[1:14] uhm, performance data. I want to make sure I get the pages overview.
[1:18] So we are now ready to load this up,
[1:21] which is very exciting. Uh,
[1:24] let me do that by dragging it internal.
[1:28] Screen and frog. There we go. And,
[1:31] uh, pages. There we go.
[1:35] And it will start. The analysis, and you'll see this is very exciting to
[1:39] me. This is such a great tool. So it's gonna compute all of the
[1:43] semantic relevance. It's gonna map it.
[1:46] Uh, and then it will show you exactly a visualization.
[1:51] There we go. Isn't that beautiful? So,
[1:54] purple, no drift. Uh,
[1:58] yellow, lot of drift. So this site is very,
[2:01] very focused. And if we take a look where this is,
[2:04] this is the about page that makes sense. Uh,
[2:07] this is, uh, tags, archive,
[2:10] capitalism, books. So,
[2:12] like the, the category pages or the collection page and tags.
[2:16] So, this looks good. And then you'll see we have our overall distribution.
[2:21] We have 9.1% is inside the core.
[2:24] 75% is inside the focus. 7% about 7% is ready for expansion.
[2:30] And then 9% is peripheral. These, you'll see are all the actual articles
[2:35] that are highly relevant, but they are in the peripheral,
[2:39] peripheral or expansion, mostly peripheral.
[2:44] Um, and that means that there's a little bit of work to be done.
[2:47] It seems to, to get those to the core,
[2:50] or our core is very sparingly populated at the moment,
[2:54] but we have a lot of expansion opportunities here in the archive pages.
[2:59] Uh, and so this is, uh, I'm not gonna discuss or debate with this
[3:02] tool. This is how it semantically organizes our website.
[3:07] This is how it uh, sees the website.
[3:10] It's very, very exciting. So it's- shows us the high drift pages,
[3:13] and we'll talk about what to do with these pages next.
[3:17] Um, and we can export the analysis as well.
[3:20] And this gives us a lot of information. Uh,
[3:23] yeah, it gives us core focus expansion,
[3:26] peripheral. There we go. So,
[3:30] a radial orbit style visualization.
[3:34] And this, for me, made things very, very clear.
[3:36] Thank you. I was looking for something like this for a long time.
[3:39] Um, this gives a, uh, at a glance overview of the health of
[3:44] our side and how focused it is.
[3:47] So this side is doing pretty well. We're gonna take a look at how
[3:50] to interpret these results next.

---

## 5 - Interpret The Results

🎥 https://www.loom.com/share/2868bb58c801471e827a2947e1b09132 · ~6 min · 116 cues

[0:00] So now that we have this data, we need to actually interpret the results.
[0:04] So what does this show you? It shows you the center,
[0:06] the semantic core. Each dot is a page.
[0:09] It's distance shows you how far it has drifted from the core topic.
[0:13] Angle, uh, subtopic or a theme,
[0:16] it's most similar to. So this is so focused.
[0:18] It's just the simple, uh,
[0:21] purple, but you can see multiple colors.
[0:24] Here, it shows the different clusters you have.
[0:27] And then size, color, reflects, performance,
[0:30] uh, clicks from search console.
[0:33] So these are doing the best.
[0:36] They are all very relevant. They are somewhat more in the peripheral
[0:41] or expansion category. It,
[0:43] it says. So it gives you which pages belong,
[0:47] which pages has- have drifted, uh,
[0:49] hidden opportunities, and how healthy the clusters are.
[0:52] This website is basically one big cluster,
[0:55] but if you have other big websites with lots of content clusters,
[0:58] you'll see, uh, different colors. So quick interpretation checklist.
[1:03] If it's far out in a low clicks, fix a prune it.
[1:06] If it's far out with high clicks, new cluster opportunity.
[1:09] So this would be something like that.
[1:12] If it's close in low clicks, improve, improve the quality to curate and links.
[1:16] So these pages should be,
[1:18] uh, optimized. If they are grouped at the same angle,
[1:22] but different distances, uh,
[1:24] there's an uneven content quality.
[1:28] So, let's take
[1:33] a look at the key concepts. So the distance- Listen.
[1:36] Which from center, how far is it off topic?
[1:39] And the angle on neighborhood, which semantics up theme the page belongs to.
[1:42] So these are related. These are a little bit further
[1:48] out, it says. Uh,
[1:50] the point, the size, the color, performance signals.
[1:53] So that is clicks from Search Console. Big pride dot is a strong performer.
[1:57] So that would be these. And then we see strong- strong. Performance here as
[2:01] well. So the patterns we want to look for,
[2:04] and how we can then address those patterns is far from center,
[2:08] low clicks. It has drifted off topic,
[2:11] and they dragged down top of authority. So semantic,
[2:14] not as relevant. Semantically. So what we want to do is we want to
[2:18] rewrite those pages to realign with the cluster intent.
[2:22] Move it to another cluster, or redirect, or proof.
[2:24] True. Umm, if it's irrelevant or redundant. And then,
[2:27] if it's far from center, by high clicks, these are break out topics.
[2:31] Don't fix it. Expand them. New cluster trying to form.
[2:34] That would be these. So especially this one,
[2:36] if I can cluster these together with, let's say,
[2:39] a pillar page. Uh, that would be good.
[2:41] These as well. Here's a big one. Bhagavagita,
[2:44] periods. Alright, interesting.
[2:46] Uh, we can say more about- what the Bhagavagita says on periods.
[2:51] This is about women's menstruation cycles.
[2:53] Uh, or we can do other books on menstruation.
[2:57] And then do a pillar article tying all of those together.
[3:00] That would be a very good idea. Close the center,
[3:04] low clicks. It's on topic, but underperforming.
[3:06] Highest leverage, easy wins. These ones.
[3:09] So let's say we have, uh,
[3:11] these are pet- I'll you in a pagination and archive pages.
[3:14] Mostly it's gonna. So theme,
[3:17] art, uh,
[3:19] theme, artificial intelligence. Yeah, these are tags.
[3:22] In my case. So philosophers,
[3:25] Socrates. Yeah,
[3:28] mostly, uh, pagination in this case.
[3:31] So we can do on page quick wins.
[3:34] Optimizations. Improving page.
[3:36] Which titles, et cetera. Uh,
[3:38] if we have a group of pages at the same angle but different distances,
[3:42] that is a subtopic with uneven quality.
[3:45] So that would be this. So these should be moved
[3:49] closer in by improving the relevance.
[3:52] We can do, uhm,
[3:54] best examples. So close the center with these and clicks.
[3:57] And use these as templates for the weaker articles.
[4:00] So mimic. Those more. And then rewrite,
[4:02] consolidate, or merge. And then we have a couple of expert mode advanced
[4:07] insights. So the angle is semantic direction.
[4:11] Pages of the same angle, share topic DNA. Uh,
[4:14] if it has multiple angles far apart,
[4:16] the cluster is too broad. In this case,
[4:18] I would say it's not too broad.
[4:21] Although peripheral here. Uh,
[4:24] these are probably a little bit too far out,
[4:27] so those could be tightened up. Distance is semantic purity,
[4:31] so pages that are far from the core are not bad,
[4:33] but they are just less aligned, so we should semantically optimize those.
[4:37] You can rewrite those, redirect those,
[4:39] or expand them into a new cluster. Uh,
[4:42] and that, that, based off of distance, you can make up your mind.
[4:45] If they're very far out, like, this one,
[4:48] we could- rewrite those, or do a new cluster,
[4:51] and then this will be pulled in right here.
[4:54] Sorry about that. High drift,
[4:56] uh, high internal links is a drift of page with many in links,
[5:01] and so the internal linking is lightly pointing at the wrong content.
[5:05] We should, uhm, evaluate the internal linking there and redirect
[5:10] to a better, semantically more relevant page.
[5:12] age. . Uh, density is topic consistency,
[5:16] so if the cluster is near the center, it's a healthy silo.
[5:19] If it's sparse, noisy, we have messy information architecture.
[5:23] This information architecture is pretty good, I think.
[5:26] And then sudden drift, if you, uh, do screenshots over time,
[5:29] or, um, exports over time, you can analyze,
[5:32] uh, sudden drift, and that is a reason to investigate.
[5:36] To rewrite, uh, or there's a search-intense shift.
[5:42] If a cluster visually breaks in two, it's usually,
[5:45] it's usually a sign you have two themes mixed together.
[5:49] And then you can do, like, a split,
[5:51] and do two cluster build-out for that.
[5:54] So that is the advanced mode. Uh, it gives very good insights,
[5:57] I think. It's a very powerful tool. Up next we're gonna talk about,
[6:00] how to translate that to actions.
[6:03] directions.

---

## 7 - Determine What Actions To Take

🎥 https://www.loom.com/share/3d9ae026734647949d6a40ecff3add89 · ~8 min · 138 cues

[0:00] Right. How do we determine what actions to take?
[0:04] Because analysis is nice and well, but we need to take action on the
[0:07] actual analysis to, uh, to move the needle.
[0:12] So, in this module,
[0:15] we're gonna talk about how to decide exactly which actions to,
[0:19] to, to take based on the semantic behavior and performance or based off the
[0:24] address analysis. And, uh,
[0:26] I've come up with five action types.
[0:29] So, we're simply gonna determine for each page and each cluster what is the
[0:33] action type. This gives us broad categories to work off of from.
[0:37] And this will keep things very clear and organized for us when we are
[0:41] gonna take action. So, in the next step,
[0:45] we're gonna turn those into a backlog for,
[0:48] uhh, uhh, for those of you that do client work or run an agency,
[0:50] you'll, you'll know what that is, the dreaded backlog.
[0:54] Umm, it's good, so you'll have a,
[0:57] a list of items to choose from when you sit down and do your
[1:01] work. The five actions are gonna be realigned,
[1:05] expand, optimize, consolidate, or prove.
[1:09] So, there's a simple,
[1:12] binary decision chart here.
[1:16] Realign is when we have drifted pages that are also valuable.
[1:21] You can identify those. When they are far from
[1:26] center, low to medium clicks,
[1:28] but they are still relevant to your business. So, let's say we have these
[1:31] here, especially the, on the outer edge here.
[1:35] Uh, uhh, uhh, uhh, we see these are relevant.
[1:40] They are performing well. Uh,
[1:42] but they are also very far out. So, we want to realign those.
[1:46] Actions we can take. We can rewrite the content to match the cluster intent.
[1:51] In this specific case, that doesn't seem to be a very serious cluster
[1:55] going on. It's just a single page. So,
[1:58] perhaps we should, uhh, .
[1:59] . Add missing subtopics. Improve readability clarity,
[2:03] tighten internal linking from the cluster hub.
[2:05] Or, in this specific case, umm,
[2:09] we have, this perhaps is an expansion action.
[2:13] This is a breakout topic. And that is probably the
[2:18] case. So, it's far from center.
[2:20] We have high clicks. Comparatively high clicks.
[2:24] Thanks. Obvious new sub theme or intent.
[2:26] So, uhh, this is a page about the Bible,
[2:30] what the Bible says on fish skills. I know it's very,
[2:35] uhh, very weighty topic.
[2:39] But, uhh, apparently 300 people a month click that.
[2:43] So, actions we can take, we can create a new hub or a silo
[2:47] for that. Emerging topic, build supported content around it and strengthen the eternal
[2:52] links to that. So,
[2:55] this could be an interesting breakout topic for us.
[2:57] Then the third action category is to optimize.
[3:01] So, if we have an on topic page that is underperforming.
[3:06] Uh, how do you identify those? They are close to center.
[3:09] They have low clicks, but then it's good content, but it's weak performance.
[3:11] performance. So, let's say, uhm,
[3:16] yeah. Again, these are mostly pagination.
[3:20] So, we could, uh, boot those from the export if we want to
[3:24] get, uh, somewhat more focused and
[3:29] clear picture. So, let's say we take this
[3:35] one books wealth of n- Nations. So,
[3:38] these are all books, right? Yeah, interesting. So,
[3:41] the Bible on relationships. This is a little cluster self-satisfaction,
[3:46] watching bad things, wasting time.
[3:51] And then, just trying to figure out where we're
[3:56] at here. Bible on 70- about of the day.
[4:00] The the day I'm we have to years. Timing.
[4:05] Hmm. Car,
[4:08] am I right? Interesting. So, I'm just trying to figure out where we at.
[4:11] Uh, if I have a good example to optimize here.
[4:13] Close the center, low clicks, good content, but weak performance.
[4:17] So, let's take, for example, umm,
[4:21] this one. Books of the Republic. This is very- There.
[4:24] Very light in color. It is pretty close to center.
[4:28] These are even better, probably. But,
[4:31] uh, yeah, again,
[4:34] those are archive pages. So, let's
[4:38] go with this one. Books of the Republic. We have two in-links.
[4:41] We have no clicks. Topical distance is pretty low.
[4:46] Content is good on the book, I assume. So,
[4:49] what we can do is we can improve, we could do basic on-page optimization.
[4:53] To prove the title meta description, we can add schema,
[4:56] FAQ, how-to product. In this case,
[4:59] we could do author, and, uh, is it book,
[5:02] or work, or not quite sure. Add internal links.
[5:05] We saw we only have two. So, that is a good idea.
[5:09] Uh, and add better visuals and EAT. So,
[5:11] it's just your basic- optimization, but instead of doing this for all the pages
[5:16] that you think are underperforming, we now have a five-step framework,
[5:20] or five-path framework, to,
[5:23] uh, make sure we're not over-optimizing anything that shouldn't be there in the first
[5:26] place. So, number four is to consolidate for clusters with uneven content
[5:32] quality. So,
[5:34] pages share- share the same angle. They are far from center side.
[5:36] They are close. They are redundant or overlapping.
[5:40] Uh, and then the actions are merged weaker pages into stronger ones,
[5:44] removed duplicate content, and used the strongest version as the template.
[5:48] That would be, uh, for example, the one that is performing the
[5:52] best. Or the one that is closest to the core.
[5:56] Either one could work. book. I
[6:01] wish we had a website that was more diverse for demo purposes here.
[6:06] But, for example, this, this page here is doing very well.
[6:10] And then, back off at Gita.
[6:19] Yeah, so, this line here.
[6:28] I'm just seeing where the other Bhagavad Gita's are.
[6:31] I'm not really seeing them, though. So,
[6:34] that is very interesting. So, here are a couple of them.
[6:39] I'm still trying to figure out how to read this exactly,
[6:42] to be, uh, to be honest. So, then,
[6:45] number five is to prune and redirect for pages that no longer,
[6:49] or fit your cluster or site strategy. So, when we have far from center,
[6:53] low clicks in links, no strategic value.
[6:56] Uh, the actions we can take,
[6:58] we redirect to Stormless Relevant Page,
[7:00] 301, or, uh, 410,
[7:02] if irrelevant, no value. But, I would opt for 301,
[7:07] almost all of the time. Uh, you could even do it through your home
[7:11] page and, uh, retain some of the,
[7:13] low clicks. And we clean up the orphaned URLs on the site.
[7:16] That is always a good idea. So, any pages without any in-links whatsoever,
[7:19] that is a good idea to clean up. Or to add in-links,
[7:24] if they are, uh, relevant.
[7:27] So, basically, if we zoom out,
[7:30] we have Realign Expand Optimize Consolidate Prune.
[7:33] If we see duplicate content or overlap,
[7:37] Or it's not as relevant, we can consolidate.
[7:39] If it's not relevant, there's a lot of drift.
[7:42] We prune it. If it is relevant, but it's underperforming,
[7:45] we optimize. If it is relevant,
[7:49] but it's a breakout, we expand. If it's drifting,
[7:53] uh, but it is part of a cluster, we realign.
[7:56] That is the basic decision-making framework here.
[8:01] Pick tip, keep it simple. Identify the page type.
[8:03] Choose one action and add it to the backlog. So we just say,
[8:07] alright, this is an interesting page. We should focus on that.
[8:10] Um, we want to, for example, expand the action we should take.
[8:15] And then we add that to the backlog. And we have,
[8:18] uh, drawn up a couple of templates,
[8:22] templated tasks for, for each of these in the next.
[8:25] Module. So I'll see you there. Okay.

---

## 8 - Turn Action Items Into Backlog

🎥 https://www.loom.com/share/bc258af936004328bd4f9298962c6c87 · ~16 min · 260 cues

[0:00] Let's turn our action items into a backlog.
[0:04] So, we want to turn our insights into a prioritized as your backlog
[0:09] and then we can execute. I would start with exporting this analysis.
[0:14] So they will give you a CSV and I have imported that into my
[0:17] Google Drive here. And I had to work through all the metrics
[0:22] in here. So this is based. Basically the, uh, screening frog,
[0:26] uh, Google Search Console,
[0:29] plus this analysis all in one. So there's a lot of data in here.
[0:33] So let's clean it up a little bit really quickly.
[0:39] Because most of this we will not need.
[0:43] Uh, we just want the analysis specifically.
[0:47] Perfectly. Over this part. So.
[0:53] Maybe all of this height. And then we have
[0:57] some Google Search Console performance data,
[0:59] which is relevant and helpful to us.
[1:04] Then. This is gonna be.
[1:08] All of the data points, but I'm gonna.
[1:12] Hide those for now. Uh,
[1:16] let's see. I wanna have the zone here.
[1:19] I wanna have SDI. And I was reading the documentation here.
[1:24] Let's take a quick look what we need else.
[1:28] So we have. Mmm.
[1:33] Clicks. Umm.
[1:38] SDI, we need distance from center. We need that.
[1:41] That is the embedding site-centroid cosine distance.
[1:45] I don't know what that means, but. Driftopacity
[1:49] is support. I thought
[1:54] I magically end. Now we don't. So I would say.
[2:01] Ah, we have clicks normalized this that then.
[2:07] The, uhm, alright,
[2:10] let's not use that size scaled. So the size is interesting to us because
[2:15] it shows us the, uh, the performance of the page.
[2:20] So I would hide all of this.
[2:22] and next week's episode. As much as possible,
[2:25] just to not confuse ourselves. Maybe even this stuff.
[2:29] Maybe just clicks. Click's as the eyes,
[2:32] uh, scale in link, clicks log.
[2:36] Uh, focus on, good, opacity.
[2:40] Alright, so now what we can do, now it gets interesting.
[2:42] interesting. We
[2:47] export the problem pages. We say sort by distance,
[2:49] low clicks, etc. So when we have the interpretations here and the actions we
[2:54] can take, we have to now filter those out.
[2:57] So let's say we want to realign, or let's say we want to expand.
[3:01] Let's find our breakout topic. We're far from center,
[3:03] so we sort by the distance,
[3:06] high clicks that are obvious new themes or intents,
[3:10] so they need to be relevant to us. So we need high clicks,
[3:14] so let's say, zeta a,
[3:16] these are high clicks, and what I always do is I make this a
[3:19] filter by clicking here, and this means I can add and remove stuff
[3:24] easily. So we have high clicks, and then,
[3:27] uh, we need the distance,
[3:30] which is SDI if I remember correctly.
[3:33] Alright, so SDI is cooler, so it's, um,
[3:35] semantic and structure. in direction. . So, uh,
[3:39] higher SDI is then more semantically relevant.
[3:43] So if we say, ah,
[3:47] this is gonna require us to, uh,
[3:50] organize, like, arrange this, um,
[3:53] in a meaningful way. Alright,
[3:57] we'll do that later. So then we need, uh,
[3:59] let's see. High clicks,
[4:03] far from center, and performing well.
[4:07] So that is size, and,
[4:09] uh, this is opacity,
[4:13] in things, et cetera. So let's start with filtering out far from
[4:18] center. So not core, not focus, just peripheral,
[4:22] and expansion, as well.
[4:24] So specifically expansion is peaking my interest,
[4:26] and that is 169 pages in total,
[4:31] but these are high and low clicks,
[4:33] so we can now simply do, um,
[4:40] greater than, let's say 100 clicks,
[4:44] anything above 100 is worthwhile for us at this point.
[4:50] Alright, so these are the pages that are, in
[4:56] the expansion zone, have high clicks, and
[5:01] the expansion zone is a distance from center. We could add peripheral,
[5:04] perhaps, or peripheral.
[5:08] Then we have 53 pages, we can,
[5:10] we can look at, um,
[5:12] uhh, but I would start with expansion just to stay focused.
[5:17] So these would be the pages to work on, to re-align,
[5:22] uh, or expand. So these are breakout topics,
[5:25] the F-high clicks, and then we can manually double check,
[5:28] are these all relevant to our core focus for this website?
[5:33] They all are, because they are all the same color. We could.
[5:38] Uh, do something with this as well. So we could do.
[5:42] These are all pretty close. This is the color.
[5:45] Value. All pretty close. Percentage.
[5:50] Reads easier. So I would say,
[5:52] and these have a, uh, decent amount of,
[5:55] some links at least. So these are all worthwhile.
[5:59] They have clicks already. All right. They are, uh,
[6:02] far out there. So we could say, build out clusters with,
[6:05] uh, if we now filter this own name,
[6:09] we have a bunch on the Bible. That,
[6:12] that would be an interesting and easy cluster.
[6:15] We could try and find, uh, themes here.
[6:18] Content themes to focus on and, and build some,
[6:21] like, two or three hubs here. Then we have philosophers sort of Socrates,
[6:25] alright, so that, that requires a good cluster. I'm not wondering,
[6:29] did I ever build out this page? No.
[6:33] So there you go. So for other philosophers, I think Nietzsche's one,
[6:37] we did build out a hub here.
[6:40] There you go. And so Socrates is missing that.
[6:44] Uh, where we tie it all together. And then we can refer to all
[6:48] the, the ar- articles that are in here as well.
[6:51] So there you go. That is a quick win. Build out that hub,
[6:53] link all of these. Uh, and that will bring it the semantic relevance title,
[6:59] uh, closer together, tighten it up a bit.
[7:03] Alright, so, let's try and optimize,
[7:06] uh, close the center, low clicks, good content,
[7:08] but weak performance. How would we filter that out?
[7:12] We would say- they close the center, so core focus, and then low clicks,
[7:17] we should say, uh, less than 20.
[7:23] There you go. So that is a lot of pages.
[7:26] 2000, to be exact. So then we need,
[7:29] uh, perhaps relevance as well.
[7:32] Um, if we've got to do this manually, that is not gonna work for
[7:37] us. So all of these are very small
[7:42] numbers, uh, a to z,
[7:46] these. And so these are all,
[7:48] this color is different. Those are the old ones out.
[7:52] And these are all the pagination pages and things like that.
[7:55] So that makes sense. So let's say we filter out
[8:00] text does not contain what do we need to filter out.
[8:04] Like a colon, it seems for all those filters.
[8:08] Oh, we don't. We're left with nothing.
[8:10] Alright, interesting. I think the zone is too small.
[8:14] Let's add expansion here. It's still too small.
[8:18] Oh, of course, the colon will filter out all the URLs.
[8:21] Sorry about that. Let's see. So how are we gonna do this?
[8:26] Now we're gonna filter those out. Perhaps it's just gonna be manual.
[8:31] Theme. Yeah, alright, so we'll have to do it like this.
[8:35] So, if you've never worked with sheets like this,
[8:39] this is gonna be interesting. So, theme,
[8:43] filter by velice, theme, colon.
[8:46] Alright, I'm gonna delete those for now. And we- We want to do it
[8:50] like this and do backspace, because we don't want to delete within those rows,
[8:55] but in between those rows. So we have page, we need to delete all
[8:57] of those.
[9:03] I'm making this up as I go, so this is how I would do
[9:06] it with the knowledge I have today.
[9:09] Anything with archive in it. Umm,
[9:14] there are many ways this is going to get cut, obviously, so.
[9:18] Uh, text contains? Yes.
[9:22] That is a lot. 200. Delete.
[9:27] Alright, reset that. Are
[9:32] we really just left with this one?
[9:35] That is not a lot. Less than a hundred.
[9:39] Uh, less than a hundred and fifty clicks.
[9:45] Oh, sorry. It's still just
[9:50] this one. Alright, so this is the single page that we should build out.
[9:54] And, uh, I agree this is a very low content page and it is
[9:58] one of the biggest clusters, so that makes sense.
[10:00] That is, Perfect analysis. So we can,
[10:04] uhm, do all the own page here.
[10:08] Well, the, the own page optimizations are not there,
[10:10] so we should build that out, but that is, that makes,
[10:13] that is correct, the correct action here. Alright.
[10:17] I'm gonna, Oh,
[10:20] we can,
[10:22] Pro when I redirect, but that is, again,
[10:24] filtering far from- Umm center, low clicks, and then low in-links,
[10:27] which will be, uh, this one.
[10:32] So let's reset this filter real quick to give
[10:37] us a little bit, uh,
[10:41] we need peripheral, maybe expansion,
[10:46] I would say peripheral, uh,
[10:49] low in-link. So, let's just sort that for now.
[10:54] We want to do A to Z lower.
[11:03] Alright, and then low clicks. I think it's at low clicks,
[11:07] right? Yeah. And then no strategic value,
[11:11] which is on this side, it's very focused. open your eyes.
[11:13] So, uh, less than,
[11:17] 100. Okay.
[11:22] 181. Let's do less than a 50.
[11:27] Just make our data set a little bit smaller. 155.
[11:30] Let's do it's, 20. 110 still.
[11:36] So, you see, What I'm doing is I'm just trying to narrow the data
[11:39] set until I get the, the, the,
[11:42] like the no brainers, the easiest to decide on.
[11:46] And then we see we have a bunch of pages here that are of
[11:49] low relevance at this point,
[11:52] and also low clicks,
[11:55] low inlinks. So, and then we can either do one of two things.
[11:58] We can do prune or redirect if it's irrelevant.
[12:01] These are, irrelevant, so we should expand or realign
[12:06] with those. Alright, so this,
[12:08] this video is running a little bit long. I hope this makes sense.
[12:11] It is pretty rough at this point.
[12:13] I'm just working with the raw data here. It is not as pretty as
[12:17] some processes in this, uh,
[12:20] community. But this is how I would go about it.
[12:25] Raw data is good. But if you learn to work with Google sheets like
[12:28] this using the filter function, it's very, very powerful stuff.
[12:31] So, I, I invite you to try your hand at it.
[12:35] And there's so much we can take from this data.
[12:38] Um, just by sorting,
[12:40] filtering, removing irrelevant stuff.
[12:43] And I, I am very easy to delete 500 rows.
[12:48] Because I can always re-in- port. So, for the next analysis,
[12:51] when I have done, for example, the pages I wanna,
[12:55] uh, build out, like the lowest hanging fruit.
[12:59] Clusters for optimize, for example. Uh,
[13:02] the first one we did, uh, we found,
[13:04] for example, Socrates, the Bible, a couple of good ones.
[13:08] Then I'll just go and add that to the backlog,
[13:11] and then redo the entire analysis for the next,
[13:13] the next. We'll be back next. Action, right here.
[13:16] And once we've done the low hanging fruit, I would go and simply do
[13:21] the analysis over again, but delete all the pages we already went
[13:25] through, and then go to the next 20%.
[13:28] Always trying to hit the highest impact pages first.
[13:38] Alright, I'm gonna go over this real quick,
[13:40] so we do, we take the page URL,
[13:43] we assign any of these, uhh,
[13:46] task types, and then we can write the action item,
[13:50] we've included examples here. So rewrite to better match this intent,
[13:54] move this to that cluster, add five internal links when we're gonna optimize,
[13:59] combine with this URL when we're gonna merge or consolidate.
[14:02] Or create a hub for Breakout Topic 4.
[14:05] Umm, what was the one? Umm,
[14:10] I forgot the article there, every write to better match,
[14:13] umm,
[14:16] add five internal links, so the Bible would be a good one.
[14:20] Alright, estimate effort, small, medium,
[14:22] large. So for this, uhh,
[14:25] to work we need to do, The lowest effort, highest impact first,
[14:29] or that is how we go about it always. And so,
[14:32] small effort, good, umm,
[14:35] and then score impact, clicks impressions,
[14:37] imports of cluster and business goods. So, the hub page for the Bible,
[14:41] it's medium effort, perhaps, umm,
[14:45] and it's high impact. So that is a good score,
[14:48] and then we can prioritize based on the, It's called the ICE framework,
[14:52] impact, umm, confidence effort.
[14:57] So if we're very confident, this is a very relevant hub for us,
[15:01] and it's decent effort,
[15:04] it's not high effort, uhh,
[15:06] and the impact is big, then that it has a high ICE score,
[15:10] and we should prioritize that action. And then we have,
[15:14] One task on the backlog, you can do this in Google Sheets,
[15:17] we use ClickUp as well, uh, where you just have this page,
[15:21] needs this work, and it's high impact,
[15:23] medium effort, high confidence, so it's one of the first things I'm gonna do.
[15:28] And once you have a backlog of,
[15:30] let's say, 10, 20 items, uhh,
[15:34] we can do steady work and execute very consistently,
[15:38] And you'll never wonder what to do next again.
[15:41] That is the way to, to, uh, chew through a big project like this,
[15:45] or that is how I've always done it,
[15:48] at least. Hope that's helpful, hope you,
[15:51] uh, are gonna do a semantic drift analysis for your main site.
[15:56] And, uh, yeah, let us know what observations you make.
[16:00] Is there anything that, uh, that, that is very,
[16:03] very useful, or very particularly interesting that comes out of
[16:08] this analysis. Let us know, and,
[16:10] uh, good luck. See you on the other end.

---
