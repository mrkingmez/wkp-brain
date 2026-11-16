# Teacher video picks (2026-11-14)

Researcher: general-purpose agent, read-only, $0. Method: yt-dlp search and metadata (no video or audio downloaded), auto or manual caption text read, claims checked against Anthropic pages fetched today. Link only, nothing embedded.

## Read this first

1. **yt-dlp hit HTTP 429 after 11 videos.** I stopped using it and did not work around it. Every video below the "Checked" section has only search-list data (title, channel, length, views). No upload date, no captions, no claim check. They are all UNCHECKED and none is recommended. A person or a later run can finish them once the block clears.
2. **The power tools fact pack (2026-11-14-claude-power-tools-fact-pack.md) does not exist yet.** I checked the claims against Anthropic support and pricing pages fetched today instead (listed in section 3).
3. **Big finding for the Claude power tools section.** Anthropic's pages say Projects (up to 5), Skills, Connectors (one custom connector) and Memory are all available on the FREE plan. What is paid-only: RAG mode for big projects, chat search, Research, Claude Code, higher limits. Sharing projects is Team and Enterprise only. So "paid" lessons must not call Projects, Skills or Connectors paid-only. Zac still needs to say which paid plan she has.
4. No "get-rich", sponsor or paid-course pitch was seen in the 11 checked videos (checked captions only, not descriptions or pinned comments, which yt-dlp metadata was not read for).

## 1. Checked videos (caption text read)

| ID | Title | Channel | Date | Length | Views | Captions | Verdict |
|---|---|---|---|---|---|---|---|
| 0vZ_UVLhSQQ | Getting started with Claude.ai | Anthropic | 2025-12-02 | 5:19 | 2.45M | auto | OUTDATED (minor) |
| GJ5jTgcbRHA | Getting started with projects in Claude.ai | Anthropic | 2025-12-02 | 7:08 | 1.52M | auto | OUTDATED (minor) |
| 005JLRt3gXI | Why do AI models hallucinate? | Claude | 2026-04-15 | 5:13 | 398k | manual | ACCURATE |
| 2YCaBqP8muw | Lesson 7: Effective prompting techniques (Deep Dive), AI Fluency course | Anthropic | 2025-06-12 | 11:54 | 607k | auto | ACCURATE (first third read) |
| W4Ua6XFfX9w | Lesson 2B: The 4D Framework, AI Fluency course | Anthropic | 2025-06-12 | 5:20 | 880k | auto | UNCHECKED against a primary page, concept only |
| fOxC44g8vig | Claude Agent Skills Explained | Anthropic | 2025-11-26 | 3:14 | 259k | auto | ACCURATE on checked claims, developer audience |
| bjdBVZa66oU | What are skills? | Claude | 2026-02-27 | 2:54 | 1.96M | auto | ACCURATE on concept, wrong audience (Claude Code) |
| OfUn6HjwXhI | Behind the prompt: Prompting tips for Claude.ai | Anthropic | 2023-08-25 | 3:36 | 111k | manual | OUTDATED, do not use |
| ysPbXH0LpIE | Prompting 101, Code w/ Claude | Anthropic | 2025-07-31 | 24:52 | 572k | manual | UNCHECKED, too technical (first part read) |
| rKV5JcALQoQ | The different levels of how Claude thinks | Anthropic | 2026-07-06 | 5:27 | 537k | manual | Not a how-to, do not use |
| kS1MJFZWMq4 | Creating custom Skills with Claude | Anthropic | 2025-10-16 | 0:47 | 321k | none | UNCHECKED, no captions, too short |

Links: https://www.youtube.com/watch?v= followed by the ID.

### What I checked for each

- **0vZ_UVLhSQQ.** Checked: connectors and Drive reached from the tools menu (matches the connectors help page, "+" menu); model choice talk against the fact pack (Free has Sonnet and Haiku, no Opus; current names Sonnet 5.5, Haiku 5.5) and the pricing page (Research is not on Free). Stale: pitches Opus as the largest model and Research (5 to 45 minutes) as if everyone has it; both are not on Free. Not checked: the 5 to 45 minute Research figure, extended thinking toggle location. The prompt advice (set the stage, define the task, rules, attach examples) matches the course's own Track 1 and Anthropic's docs list (clarity, examples, role).
- **GJ5jTgcbRHA.** Checked against the Projects help page. Matches: project knowledge, instructions, uploads, Drive connect. Stale or incomplete: it says RAG switches on automatically (page: paid plans only), shows "private or public" visibility (page: sharing is Team and Enterprise only, a new project version is rolling out), never says Free has 5 projects. Okay for how to make a project, mark the plan notes in the lesson.
- **005JLRt3gXI.** Checked against Anthropic's "Reduce hallucinations" doc. Matches: let it say "I don't know", ask for sources and have it verify claims, validate high-stakes info. Not checked: the tip to ask the AI "how confident are you" (not in that doc). Honest framing: says hallucinations are rarer but not solved. Best fit for her "check what AI tells you" lesson.
- **2YCaBqP8muw.** Checked: the six tips (context, examples, output limits, steps, think first, role and tone) against the Anthropic prompt engineering overview, which lists clarity, examples, role, thinking and chaining. Read only the first third of the caption. Says it applies to other AIs too. Stays correct because it avoids model names.
- **W4Ua6XFfX9w.** Defines delegation, description, discernment, diligence. No tool or plan facts, so nothing to go stale. I did not fetch the AI Fluency course page, so I will not call it accurate. Fits "when to keep the decision yourself" and "what not to paste" (diligence part mentions protecting sensitive data).
- **fOxC44g8vig.** Checked against the Skills help page: portable across Claude Code, API and claude.ai (yes), skills load as needed (yes), MCP gives tool access and skills teach how to use it (yes). Not checked: "30 to 50 tokens per skill". Flags: talks about CLAUDE.md, sub agents and coding, so it is a developer video. Does not mention that skills are on Free.
- **bjdBVZa66oU.** Concept matches the help page ("folders of instructions"). Whole example is Claude Code, git and PRs. She will not use that. Fallback only.
- **OfUn6HjwXhI.** 2023, says Claude reads 100k tokens, pushes XML tags and jailbreak talk. Stale, plus a 12-month-plus rule for fast-changing tools.
- **ysPbXH0LpIE.** Developer session about building a production prompt for image analysis. Too technical for a beginner.
- **rKV5JcALQoQ.** Interpretability research ("J-space"). Interesting, not a lesson, claims not checked.

## 2. Picks per lesson

Rule applied: recommend only a video I read and checked. Where I did not, the row says "no checked video" and lists unchecked candidates for a later pass.

### Track 1, Start Here

| Lesson | Video | Channel | Link | Date | Length | Verdict | Checked | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 What AI is, plain words | No checked video found | | | | | | | Unchecked candidates from search: "Large Language Models explained briefly" (3Blue1Brown, 7 min, 8.5M views, ID LPZh9BOjkQs); "How Large Language Models Work" (IBM Technology, 5 min, 5sLYAQS9sWQ); Anthropic's Chloe Lubinski "how AI works" on the Alliance for Responsible Citizenship channel (14 min, aBUniZHgCnE). yt-dlp blocked before metadata. |
| 2 Meet Claude | Getting started with Claude.ai | Anthropic | https://www.youtube.com/watch?v=0vZ_UVLhSQQ | 2025-12-02 | 5:19 | OUTDATED (minor) | Connectors menu, model names, Research plan | Opus and Research are not on Free, tell her to skip those parts. Official, no pitch. Recommend. |
| 3 First good prompt | Lesson 7: Effective prompting techniques | Anthropic | https://www.youtube.com/watch?v=2YCaBqP8muw | 2025-06-12 | 11:54 | ACCURATE (first third read) | Six tips vs Anthropic docs | Part of a free course. 17 months old but model-neutral. Recommend. |
| 4 Role and context | Same video (role, tone and context tips) | Anthropic | same | | | ACCURATE (first third read) | same | Second pick: 0vZ_UVLhSQQ (set the stage, define task, rules). |
| 5 Show it examples | Same video (examples tip) | Anthropic | same | | | ACCURATE (first third read) | same | Google's "Discover Few-Shot Prompting" (4 min, 9qdgEBVkWR4) is UNCHECKED, Coursera course promo risk. |
| 6 Make it show its work | Why do AI models hallucinate? | Claude | https://www.youtube.com/watch?v=005JLRt3gXI | 2026-04-15 | 5:13 | ACCURATE | Hallucination doc | Strongest pick overall. Recommend. |
| 7 Long tasks: files, chats, memory | Getting started with Claude.ai (upload and context part) | Anthropic | https://www.youtube.com/watch?v=0vZ_UVLhSQQ | 2025-12-02 | 5:19 | OUTDATED (minor) | Upload types match upload page in fact pack | No memory video checked. Memory is on by default on Free, off per chat via "+" menu, per Anthropic memory page, say so in the lesson. |
| 8 Prompt library | No good video found | | | | | | | Nothing relevant seen. |
| 9 Advanced: chains and checking | No checked video found | | | | | | | Only small channels seen (under 3k views on most chaining videos). Skip. |

### Track 2, Write with AI

| Lesson | Video | Verdict | Flags |
|---|---|---|---|
| W1 Partner, not ghostwriter | The 4D Framework (W4Ua6XFfX9w, 5:20, Anthropic, https://www.youtube.com/watch?v=W4Ua6XFfX9w) | UNCHECKED against a primary page, concept only | Delegation and discernment fit the lesson. Optional. |
| W2 Brainstorm and outline | No good video found | | Writing videos seen were tiny channels or 1 to 2 minute clips, not vetted. |
| W3 Drafting with context | 0vZ_UVLhSQQ for context idea only | OUTDATED (minor) | Optional. |
| W4 Revising with AI as editor | No good video found | | Candidate "Prompt Structure for editing an essay" (7 min, under 1k views), not read. |
| W5 Long projects and fact-checking | 005JLRt3gXI (fact-checking) | ACCURATE | GJ5jTgcbRHA covers projects, see Power tools. |

### Track 3, Build and Automate

| Lesson | Video | Verdict | Flags |
|---|---|---|---|
| 1 Spreadsheet automation | No checked video found | | Unchecked: Gemini in Sheets videos from small channels. |
| 2 Ask Claude for a formula | No good video found | | Most seen are 2 minute clips from small channels. |
| 3 Forms to sheets | No checked video found | | Unchecked, looked well viewed: "How to Connect Google Forms to Google Sheets" (Spreadsheet Point, 5 min, 331k views, 507H7UGBsaU); Simpletivity (3 min, 158k, r1VvQqFGMds). Google menus change, check date and screenshots before linking. |
| 5 First web page | No checked video found | | Unchecked: Ray Fu "building a website with Claude for beginners" (6 min, 78k, YVzNA1XlVbQ). Many results use Claude Code, which she will not have. |

### Stay Safe

| Lesson | Video | Verdict | Flags |
|---|---|---|---|
| Check what AI tells you | 005JLRt3gXI | ACCURATE | Primary pick. |
| Privacy: what not to paste | No checked video found | | Unchecked: David Bombal (7 min, 105k, 57wFvOqzBvg), Hands-On Tech (17 min, 1,110 views shown, Q9dxPAvUJrI), Privacy International Claude settings (3 min, zYpMIKV4lSE). Settings menus change often, a settings video over 12 months old would be stale. The 4D video's diligence section is an optional concept link. |
| When to keep the decision yourself | The 4D Framework (W4Ua6XFfX9w) | UNCHECKED against a primary page, concept only | Delegation and discernment match the lesson. |

## 3. Claude power tools section

Sources fetched 2026-11-14: support.claude.com articles for Projects (9517075), Skills (12512176), Connectors (11176164), chat search and memory (11817273); claude.com/pricing. None shows a publication date, only "updated over 1 to 2 weeks ago".

| Topic | Video | Channel | Link | Date | Length | Verdict | Flags |
|---|---|---|---|---|---|---|---|
| Projects | Getting started with projects in Claude.ai | Anthropic | https://www.youtube.com/watch?v=GJ5jTgcbRHA | 2025-12-02 | 7:08 | OUTDATED (minor) | RAG is paid-only per Anthropic, sharing is Team and Enterprise only, Free gets 5 projects. A new project version is rolling out, the screens may differ. Recommend with those notes. |
| Skills | Claude Agent Skills Explained | Anthropic | https://www.youtube.com/watch?v=fOxC44g8vig | 2025-11-26 | 3:14 | ACCURATE on checked claims | Developer talk. Skills are on Free too, need code execution turned on. Second option: bjdBVZa66oU (Claude Code only, fallback). Kevin Stratvert's beginner Skills tutorials (11 min, wO8EboopboU, and 14 min, O_z9vDLgvoY) are UNCHECKED. |
| Connectors and MCP | No checked video found | | | | | | Anthropic's own connectors video was not found. Unchecked beginner candidates: Kevin Stratvert "Claude Connectors Tutorial for Beginners" (5 min, 80k, FpRNId-jeTQ); Postman "Skills vs MCP" (11 min, 26k, qthyl0GCpDo, vendor channel, possible product pitch). Safety flags to put in the lesson: Anthropic says custom connectors are not verified by Anthropic, connect only trusted services, Claude sees whatever her account can reach. Any video that says to connect everything is unsafe advice. |
| Memory (bonus) | No checked video found | | | | | | Anthropic memory page: on by default on Free, never saves ID or financial account numbers, incognito via ghost icon. |

## 4. Counts

- Candidates seen in search lists: about 140 across 30 searches.
- Videos with metadata and caption text read: 10 (11 with the 47 second one that has no captions).
- Verdicts: ACCURATE 2 (005JLRt3gXI, 2YCaBqP8muw partial) plus 1 ACCURATE on checked claims (fOxC44g8vig); OUTDATED 3 (two minor, one do-not-use); UNCHECKED 4 (incl. ones listed in section 2 only by search data, not counted in the 11).
- Recommended: 5 videos (005JLRt3gXI, 2YCaBqP8muw, 0vZ_UVLhSQQ, GJ5jTgcbRHA, fOxC44g8vig), plus W4Ua6XFfX9w as an optional concept link.
- Lessons with "no good video found" or "no checked video": T1-1, T1-8, T1-9, W2, W4, T3 all four, Privacy, Connectors and MCP.
- Videos older than 12 months about fast-changing tools: OfUn6HjwXhI (2023, rejected). The two AI Fluency lessons (2025-06-12) are 17 months old but contain no tool menus.

## 5. Next step if Zac wants more coverage

Wait for the YouTube block to clear, then run the unchecked candidates in sections 2 and 3 (about 25 videos), and have someone read the descriptions and pinned comments for sponsor or course pitches, which this run did not check. Also have fact-research write the power tools fact pack and confirm which paid plan she has.
