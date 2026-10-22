# Automation Accelerator

> Source: AI SEO: Rank Expand Academy (Skool) — `classroom/52339bb6`  
> 24 lessons · 19 videos (~85 min) · 19 KB of written material  
> Internal reference for MAMMATA. Not for redistribution.

---

## Welcome to The Automation Accelerator

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/711f40503dae4a9a9f24da967e0d650dbea507b3f49745089fc84c03fb3ddf9d-md.png)

Welcome to the Automation Accelerator.

This is where you go from "I don't know how to automate anything" to building AI systems that do real work for you. No coding background needed. You'll learn by building.

## **What's inside**

The course is split into modules, each one a complete skill:

- **Basics of Automation**: Start here. You'll learn what n8n is, import your first working workflow, set up your API keys, and get comfortable with the tools we use every day (DataForSEO, Apify, OpenAI). By the end you'll be running automations, not just watching them.
- **How to Talk to AI (coming soon)**: Get pro-level output from AI by briefing it the way you'd brief a contractor. The skill that makes every other workflow in here work better.
- **The Knowledge Engine**: Build a self-organizing knowledge base that an AI maintains for you. Drop in your research and the AI synthesizes it into something Claude can read and build from while it works.

More modules get added over time. This course grows with the community.

## **How to work through it**

Go in order the first time. The modules build on each other, and the Basics module sets up the tools every other module assumes you have.

Don't just watch. Open n8n in another tab and build alongside the videos. The members who get results are the ones who pause, copy what's on screen, and run it themselves.

Stuck? Post in the community. Someone has hit the same wall, and we answer fast.

## **One thing before you start**

You don't need to be technical. You need to be willing to follow steps and try things. Every person in here who now runs automations started exactly where you are.

Let's build.

**🤖 **[**Start with Basics of Automation.**](https://www.skool.com/rank-expand-academy/classroom/52339bb6?md=b634bf56b9ef406ea0295a1b29d4d532)

## 🆕 Basics of Automation with N8N

### The basics of automation

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/2d822d7936cd4e19a3d23ea79245e4c75557bc7be4c34f7f8ed9aa4bfaf2c561-md.png)

This is where automation stops being a buzzword and becomes something you can actually do.

By the end of this module you'll have built and run real workflows in n8n, the tool we use every day. Not theory. Working automations you set up yourself.

Here's the path:

First, you'll learn what n8n is and why we use it over everything else. Then you'll import your first working workflow, so you see a real automation run before you build one from scratch. From there you'll set up the API keys that connect your tools (OpenAI, DataForSEO), get the core concepts down, and meet the tools we lean on most: DataForSEO and Apify.

By the last lesson, you'll be running automations on your own.

#### **Two things that make this stick:**

1. Build alongside the videos. Open n8n in another tab and do each step as you watch. Reading about automation teaches you nothing. Running one teaches you everything.
2. Don't skip the credentials lessons. Setting up API keys is the boring part, and it's also the part that makes every other workflow in here actually work. Get it done once and you're set.

You don't need any technical background. You need to follow the steps and try things. Let's go.

[**🤖 Start with: N8N: What it is.**](https://www.skool.com/rank-expand-academy/classroom/52339bb6?md=4236ca59d94a408a90a66f962b2aff17)

### N8N: What it is

🎥 [Loom](https://www.loom.com/share/8da899b85e894c24a342a81535ec4487) · 2:33

### Import a Workflow

🎥 [Loom](https://www.loom.com/share/ba92569c0e104d53903582432f83adb8) · 1:59

### Setting up credentials in N8N

🎥 [Loom](https://www.loom.com/share/c6283ef1895c4cf8b4bfcc31cd155f98) · 3:16

### Core Concepts

🎥 [Loom](https://www.loom.com/share/1712f1e550d04447884a4fbcfd72ff7f) · 13:43

**Workflow**
A workflow is the whole automation — the full sequence of steps that runs from start to finish. In n8n it's the canvas. In Make it's a "scenario." Same idea: a recipe the computer follows.

**Trigger**
The trigger is the first node — it's what *starts* the workflow. Nothing runs until the trigger fires. Common types:

- **Schedule trigger** — runs on a timer (every hour, every morning at 8am)
- **Webhook trigger** — runs when another app sends it data
- **App event trigger** — runs when something happens in a connected app (new row in a sheet, new email, new form submit)
- **Manual trigger** — you click "run" yourself (mostly for testing)

**Node**
A node is a single step in the workflow. One node = one action or one decision. Nodes connect in order, and data flows from one to the next. Think of each node as a worker that takes what it's handed, does one job, and passes the result along.

**Connection (the line between nodes)**
The wire linking one node to the next. It defines the order things run *and* carries the data forward.

**Data / payload**
What flows down the wire. Usually structured as fields (key–value pairs) — like `name: Brian`, `email: brian@x.com`. Each node can read the data from earlier nodes and add to it.

**Credential**
The saved login that lets a node access an account (your OpenAI key, your DataForSEO login, your Google account). You set it up once, then reuse it across nodes. This is why the credential lessons matter — most "it won't run" problems are credential problems.

**Execution / run**
One complete pass through the workflow. Logs of past runs are where you debug — you can see exactly what data each node received and where it broke.

**Field / mapping**
Mapping is telling a node *which* piece of incoming data to use where. "Put the email field from the trigger into the 'to' field of the send-email node." Most of the hands-on work in automation is mapping.

**API**
How two apps talk to each other without a human. An API key is the password that proves you're allowed to make the request. (Ties directly into the OpenAI / DataForSEO key lessons.)

**Loop / iteration**
Running the same steps over a list — e.g. 50 keywords, processed one at a time.

**Conditional / branch (if/then)**
A node that splits the path based on a rule. "If the lead score is above 80, send to Slack; otherwise add to a nurture

### Setup your first workflow

You're ready to pick one of our plug-and-play N8N workflows and start automating your business.

Head over to the AI Workflows & Tools module and pick the one you think has the biggest impact on your business.

Then go set it up!

### DataForSEO

🎥 [Loom](https://www.loom.com/share/7948ce65354e410fa662ca2c91ac2184) · 3:17

### OpenAI API Key

🎥 [Loom](https://www.loom.com/share/aca1adc3db744363bdcf606324ed6648) · 2:32

### DataForSEO API key

🎥 [Loom](https://www.loom.com/share/af0c7c71c1d6495a9025dd79021210ac) · 0:19

### Apify

🎥 [Loom](https://www.loom.com/share/8e1746298eee46b1a1ab16aff5aa7934) · 3:58

## 🆕 Set up a Knowledge Wiki LLM

### The Knowledge Engine

🎥 [Loom](https://www.loom.com/share/8261df42dfd84df5b9118d9088886d7b) · 2:50

You open Claude, and before it can help, you re-explain everything. Your method. The client. What you decided last week. It starts cold every time.

And when you do hand it context, it's a mess. Old notes next to current ones. Decisions you already reversed. The model can't tell what's still true, so it builds on the wrong thing and sounds confident doing it.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/47d77c42eeaa4e99abb105c69857e689bb74e250b57b462daf47b7caf6208a06-md.png)

That's the drift. Same question, different answer, depending on what it happened to read that session.

The Knowledge Engine fixes the root cause.

Instead of feeding raw files into a cold model every time, you build a knowledge base that an AI maintains for you. You drop in a source, the AI reads it, and it updates a clean set of interlinked pages. The thinking happens once, when the source lands, not every time you ask.

So when you query it later, the AI isn't reasoning from a pile. It's reading from a settled, cited, cross-linked source of truth that you curated. It stays on course because the course is written down.

Not a folder of files you dig through. Not another note app you abandon in a week.

A living knowledge base that gets smarter every time you add to it.

That's what you're going to build in this module. The next lesson shows you where operators put it to work, then we get into how it's built.

📚 **Next: what you'll actually use this for.**

### What you're going to build

🎥 [Loom](https://www.loom.com/share/75f9c6bc5419485186f751ce950e52bc) · 1:31

By the end of this module you'll have a knowledge base that gets smarter every time you add to it.

Not a folder of files you dig through. Not another note app you abandon in a week.

A living wiki that an AI builds and maintains for you. You drop in a source, the AI reads it, and it updates a clean set of interlinked pages. Ask it a question later and it answers from the organized version, not the raw mess.

The difference matters for what we do here.

Think about how much research piles up around a single client. Competitor pages. Keyword data. Call notes. Your own playbooks. Right now that knowledge sits in scattered files, and every time you need it you go hunting.

A wiki turns all of that into something Claude Code can read and build from while it works. Client research, competitor data, your SEO process, all synthesized and cross-linked, ready to feed any workflow.

That's the payoff. Let's build it.

**🧠 Watch the video, then move to the next lesson.**

### Use cases

🎥 [Loom](https://www.loom.com/share/a877dcec150a4af7ad30b9e8e9ffef57) · 3:10

Here's what we can use this setup for:

> 🏗️ **Microsite build-outs**
Feed your method, your research, your keyword data into one wiki. Now Claude Code reads from a clean knowledge base while it builds, instead of you re-explaining the playbook every time.

[➡️ Download our Microsite Blueprint for Claude here](https://www.skool.com/rank-expand-academy/classroom/a0ea58c0?md=ccf644bbd5354214b75998db87b3e6bc)

> 🌐 **Website builds in general**
Brand guidelines, page templates, copy frameworks, site structure. All synthesized and cross-linked, ready to feed any build.

> 📁 **Per-client knowledge bases**
Every call note, audit, competitor page, and keyword pull for one client in one place. Onboard a teammate or write a strategy doc without digging through six folders. The wiki gets smarter every week the relationship runs.

> 💼 **Proposals and pitches**
A wiki of past proposals, case studies, and your offers. Ask it to draft a tailored pitch, with every claim cited back to a real result.

> 🧠 **Your own second brain**
Everything you read, watch, and save in one wiki that actually connects it. The article you clipped three months ago links itself to the call you had yesterday. You stop forgetting what you already learned.

The thread through all of it is the same.

Your knowledge stops sitting in scattered files you hunt through.

It becomes something an AI can read, connect, and build from.

That's the payoff. Now let's look at how the pattern works.

🧠 **Next: the LLM Wiki pattern.**

### The LLM Wiki pattern

🎥 [Loom](https://www.loom.com/share/d250c5696f8c4838ba86b9c36f75285a) · 3:43

The LLM wiki is an idea from AI researcher [Andrej Karpathy](https://karpathy.ai/). It's a pattern for building a personal, persistent knowledge base using AI.

Here's the shift.

Most AI knowledge setups use something called RAG. You point an AI at your raw files, and every time you ask a question it searches through everything and re-reads it from scratch. The thinking happens at the moment you ask.

An LLM wiki flips that.

The AI does the hard thinking the moment new information arrives, not when you ask. When you add a source, the AI reads it, pulls out the key concepts, and writes them into an organized set of markdown pages right then. It builds and maintains an interlinked web of notes for you.

So the work compounds. Each new piece of knowledge gets connected to what's already there instead of sitting in a pile.

When you finally ask a question, the answer is fast and integrated, because the synthesis already happened.

That's the whole idea. The next lessons show you how it's put together and how to build one.

**🧠 Next: the three layers that make it work.**

### The three-layer architecture

🎥 [Loom](https://www.loom.com/share/1c6def4cba2e481cb4f38b30b8134f10) · 2:54

An LLM wiki is built on three layers. Keeping them separate is what keeps your data safe while the AI does its work.

## **Layer 1: Raw Sources**

This is your source of truth. A folder of unedited, original documents. PDFs, meeting notes, web articles, data files, images.

One rule: the AI reads these but never changes them. You decide what goes in. The AI treats it as raw material and nothing else.

## **Layer 2: The Wiki**

This is the active knowledge base, and the AI owns it entirely. It's a set of interconnected markdown files holding the AI's synthesized output: concept pages, entity pages, summaries, comparisons.

In this layer, you read and the AI writes.

Two special files keep it navigable:

- [**index.md**](http://index.md) is a catalog that lists every page with a link and a one-line summary. The AI uses it to find the right pages fast when you ask something.
- [**log.md**](http://log.md) is a running, chronological record of everything the AI did: what it ingested, when it ran a health-check, what it answered. It gives you a transparent timeline.

## **Layer 3: The Schema**

This is the rulebook. A single config file, usually named [CLAUDE.md](http://claude.md), that tells the AI how to behave. It's what turns a generic chatbot into a disciplined wiki maintainer.

You and the AI shape this file over time to fit your domain. We'll write yours in Lesson 5.

That's the structure. Next we set it up.

**🧠 Next: build your vault.**

### Set up your vault

🎥 [Loom](https://www.loom.com/share/11072ea208e84144bcc9de3b17a1fe61) · 4:01

Two pieces of software, then three folders. That's all the setup.

## **1. Install the software**

You need two things:

- **Obsidian**: a free note-taking app that works on plain markdown files. This is your viewer. It's how you'll browse the wiki and see the connections form.
- **An AI coding agent**: Claude Code, OpenAI Codex, or Cursor. This is the programmer that does the actual writing and organizing.

Karpathy frames it well: Obsidian is the IDE, the LLM is the programmer, and the wiki is the codebase.

## **2. Create your vault**

Open Obsidian and create a new vault. A vault is just a dedicated folder on your computer. Name it something like "LLM wiki."

Inside it, create three folders that match the architecture from the last lesson:

- **raw**: where you drop your original source documents. The AI reads from here and never alters these files.
- **wiki**: where the AI generates and maintains all the wiki pages.
- **templates**: optional. Add it only if you want to hand-make notes with a consistent format. The AI handles page creation for you either way.

That's the skeleton. Next we give the AI its rules.

**🧠 Next: write the schema.**

### Write your schema (CLAUDE.md)

🎥 [Loom](https://www.loom.com/share/f5a0afd9dfa54c76b1347eca2b4b35ba) · 9:52

This is the most important lesson in the module. The schema is what makes the wiki work.

Create a rules document in the root of your vault. If you're using Claude Code, name it [CLAUDE.md](http://claude.md). If you're using Codex, name it [AGENTS.md](http://AGENTS.md).

This file tells the AI how to operate. It should cover four things:

1. **Purpose**
Define exactly what this knowledge base is about. Be specific. "Client SEO research and competitor analysis for microsite builds" is a purpose. "My notes" is not. The clearer the purpose, the better the AI's decisions about what matters.
2. **Folder structure**
Tell the AI where to find raw sources and where to save new wiki pages. Point it at your raw and wiki folders by name.
3. **Ingest workflow**
Step-by-step instructions for what the AI does when a new document lands. Read the document, extract the key concepts, create or update the relevant pages, add cross-references, update [index.md](http://index.md), and log the change in [log.md](http://log.md).
4. **Formatting and behavior rules**
This is where you enforce consistency. Require a short summary at the top of every page. Require citations for every claim so you can always trace a fact back to its source. Tell the AI to check the existing wiki before answering any question, so it builds on what's there instead of starting over.

You'll keep refining this file as you go. That's normal. You and the AI co-evolve it to fit how you work.

> **Top tip: **you can use Claude to create this file and walk you through the entire Wiki setup by dropping in [Karpathy's Wiki LLM doc](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

**Here's the prompt I use:**
*We're setting up an LLM wiki for [main topic] with the explicit aim of [main goal]. I need you to help me set that up following the pattern Karpathy set out we are setting up the *[*claude.MD*](http://claude.MD)* currently I already have the folder set up called [folder name]. Walk me through the set up process and ask me questions to set up the *[*claude.MD*](http://claude.MD)* file correctly.*

[*https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f*](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

**🧠 Next: feed it your first source.**

### Ingest your first source

🎥 [Loom](https://www.loom.com/share/f824ecd13e494dab8b2a442532fe9296) · 5:26

Now you put a document in and watch the wiki build itself.

## **Drop in your first document**

Put a source into your raw folder. A competitor page, a research doc, a set of call notes, anything real you'll actually use.

## **Prompt the agent**

Open your AI coding agent in your terminal, navigate to your vault's folder, and tell it:

"I just added a new source to the raw folder. Please read it and update the wiki."

The AI reads the source and generates structured concept pages, summaries, and cross-references in your wiki folder. Open Obsidian's graph view and you'll see the connections forming in real time.

From here it's a loop. Every time you add a source, run the same prompt. The AI links the new information into your existing knowledge base, and the whole thing keeps compounding.

**🧠 Next: use the Web Clipper.**

### Using the Web Clipper to ingest

🎥 [Loom](https://www.loom.com/share/32bd49a44d5049e9b3af1d0f31de928c) · 3:31

> **Optional but recommended:** install the [Web Clipper](https://obsidian.md/clipper)

The Obsidian Web Clipper is a browser extension that saves web articles straight into your raw folder as clean markdown. If a lot of your sources live online, this saves real time. You can also set Obsidian to download images locally into a folder like raw/assets, so the AI references local images instead of web links that break

**🧠 Next: ask it questions.**

### Query your wiki

🎥 [Loom](https://www.loom.com/share/fe844e8eb5af4524be1c6eacbd141954) · 4:44

A wiki you can't pull from is just storage. This is where it pays off.

When you ask a question, the AI doesn't dig back through your raw files. It searches the pre-organized wiki, pulls from the synthesized pages, connects the dots across them, and gives you an integrated answer.

Because the thinking already happened on ingest, the answer is fast. And because your schema requires citations, every claim points back to its source, so you can trust what it tells you.

There's one more move that makes this powerful over time.

When a query produces something valuable, a comparison, an insight, a conclusion you'll want again, save it back into the wiki as a new page. Now that answer is part of your permanent knowledge base, not lost in a chat history.

The wiki grows from your sources and from your own thinking. That's the compounding loop.

**🧠 Next: keep it healthy.**

### Lint to keep it healthy

🎥 [Loom](https://www.loom.com/share/eb695af2e17b40e0b3f9d076e87c9e82) · 11:39

As any knowledge base grows, small problems creep in. Linting is how you catch them.

The name comes from code. A linter scans software for bugs. Here, you periodically ask the AI to run a health-check across your entire wiki.

During a lint pass, the AI looks for:

- **Contradictions**: conflicting claims across different pages.
- **Stale claims**: old information that a newer source has replaced.
- **Orphan pages and broken links**: pages nothing links to, or links that point to pages that don't exist.
- **Missing concepts and cross-references**: topics mentioned often enough to deserve their own page, or places where two pages should connect but don't.
- **Data gaps**: missing pieces the AI flags as something a quick web search could resolve.

Once it surfaces these, the AI can offer to fix citation problems, suggest questions worth investigating, and recommend new sources to pull in.

Run a lint every so often and your wiki stays accurate, connected, and trustworthy as it scales.

That's the full system. Sources in, synthesis on arrival, fast cited answers out, and a maintenance pass that keeps it clean. You now have a knowledge base that works for you instead of one you have to manage.

**🧠 That's the module. Go build yours.**
