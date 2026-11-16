# Teacher topic coverage map, 2026-11-14

Researcher: market-research. Read-only, WebFetch on the four repo pages, $0. Nothing copied, all topic names below are my own wording. Page summaries came from a small model reading each page, so this is "as summarized", not line-checked. TripleTen data is reused from `research\teacher\2026-11-13-course-outline-research.md`, not re-fetched. Repo facts (licenses, stars, audience) are in `2026-11-13-github-repos-review.md` and are not repeated.

## 1. What each source covers (high level)

**walkinglabs/awesome-harness-engineering** (summary read). Link list for engineers who run coding agents. Areas: learning resources, foundations, context and memory, guardrails and safe autonomy (tool limits, permissions, prompt injection, spending limits), instruction files and spec-driven work, human oversight, evals and tracing, benchmarks, sandboxes, coding-agent harnesses, multi-agent orchestration, MCP and browser tool layers, skills and config management.

**microsoft/generative-ai-for-beginners** (summary read). Learn lessons: setup, what generative AI and LLMs are, comparing models, responsible use, prompting basics, advanced prompting, UX for AI apps, securing AI apps, app lifecycle and metrics, fine-tuning, small models, Mistral and Meta model families. Build lessons: text apps, chat apps, search with embeddings, image apps, low-code apps, function calling, RAG, open-source models, agents. All build lessons are code.

**steven2358/awesome-generative-ai** (summary read). Directory by modality: recommended reading and timeline, text tools (chatbots, search, writing, productivity, research aids), coding tools, agents and assistant builders, image, video, audio (speech, music), other (prompt marketplaces, AI detectors), learning resources, more lists.

**aishwaryanr/awesome-generative-ai-guide** (summary read). Three journeys, each at 101, 201, 301. Use AI: chat tools and prompting, then power prompting, projects, connecting tools and agent tools at work, then personal automation and multi-step agent workflows. Build AI: foundations, then RAG, agents, evals, fine-tuning, guardrails, then production and security. Understand AI: research papers. Nine topic areas: LLM foundations, prompting and context, retrieval and RAG, fine-tuning, agents, evaluation, multimodal, production, safety and security. Free courses named: evals for everyone, personal assistant setup, agentic crash course (agents, tools, RAG, MCP, planning, memory, multi-agent), a no-math intro. Note the "Use AI 201 and 301" tier is the closest thing in any source to our "power tools" idea.

**TripleTen AI Automation** (from the 11-13 file, observed from its page). Order: AI tools and prompting, how LLMs work and small AI apps, no-code automation (Google tools, Make), agents and image models, APIs and webhooks, robotic process automation, capstone. **TripleTen AI Software Engineering** is mostly web development (HTML, CSS, JavaScript, MERN) with four of 28 weeks on AI-assisted coding.

## 2. Master topic list (all sources combined, grouped)

| Group | Topics seen across sources |
|---|---|
| A. AI basics | what AI and LLMs are, how they work in plain words, comparing models, tokens and context limits, hallucination, model families, small and local models, timeline and history |
| B. Prompting and context | clear asks, roles, examples, step-by-step reasoning, output formats, long documents, memory and projects, prompt libraries, prompt chaining, system instructions |
| C. Everyday use at work and home | writing, summarizing, research aids, productivity, planning, data and spreadsheets |
| D. Creative and media | image, video, audio, speech, music, design, avatars, photo work |
| E. Agents | what an agent is, tool use, planning, memory, multi-agent, computer use, agent platforms |
| F. MCP, connectors and tools | function calling, connecting apps and data to the assistant, MCP, APIs and webhooks |
| G. Skills, instruction files and specs | reusable instruction files, spec-driven work, project rules |
| H. Workflows and automation | no-code automation, forms to sheets, triggers and reminders, RPA, multi-step workflows |
| I. RAG and data | embeddings, vector search, retrieval apps, grounding on your own documents |
| J. Building apps | text and chat apps, low-code apps, web pages, scripts, APIs, front end and back end, deployment |
| K. Evaluation and trust | evals, checking outputs, quality gates, tracing, benchmarks, observability |
| L. Responsible use and safety | ethics, privacy, security threats, prompt injection, scams and deepfakes, guardrails, spending and permission limits |
| M. Fine-tuning and model work | fine-tuning, open-source models, small models, LLMOps |
| N. Research and careers | papers, interview prep, system design, bootcamp paths, portfolios |
| O. Selling and business | disclosure rules, listings (not in the four repos, comes from our own track and the 11-13 platform research) |

## 3. Coverage against the current course

Current course as Zac stated it. I looked at the site folder on disk (`Teacher\site\docs`): it has start-here, make-things, build-automate (index and advanced), and stay-safe with checking, privacy, scams and when-not-to-use pages. I did not open the lesson bodies, so "written" and "planned" below are Zac's statement, not my reading.

Legend: COVERED, PLANNED, MISSING (worth adding), OUT (deliberately out of scope for a beginner).

| Group | Status | Where it lives now | Note |
|---|---|---|---|
| A. AI basics | COVERED | Start Here: what AI is, meet Claude | Missing small pieces: context limit, tokens, "why it makes things up" as its own idea. Small gap. |
| A. comparing models, small and local models | OUT for now | none | Fine as a Further reading link only. |
| B. Prompting | COVERED | Start Here: first prompt, role and context, examples, show its work, long tasks, prompt library, chains and checking | Strongest part of the course. Matches every source's order. |
| B. Projects, memory, custom instructions | MISSING | none | Real beginner need, and the heart of the paid-user gap. |
| C. Everyday use (writing, summarizing, planning) | COVERED | Make Things: Write With AI (5 written) | Research aids and "ask about my own files" are thin. |
| C. Spreadsheets, data | COVERED | Build and Automate: spreadsheets, formulas, forms | |
| D. Images, video, printables, selling | PLANNED | Make Things (4 lessons planned) | Audio, speech and music are in the 11-13 outline (2.7) but not in your current plan list. Photo restore also. |
| E. Agents | MISSING | none | Every source has it. Needs a plain-words lesson, not a build. |
| F. MCP, connectors, tools | MISSING | none | Beginner-friendly only as "connect Claude to your Google or files", not as code. Paid-gated (see section 5). |
| G. Skills, instruction files | MISSING | none | Beginner version is "reusable instructions". Paid-gated (verify). |
| H. Workflows and automation | PARTIAL | Rules and reminders planned, forms covered | No lesson on multi-step workflows or a no-code automation tool. TripleTen's automation program leans hard here. |
| I. RAG and data | MISSING, mostly OUT | none | Beginner version is "chat with your documents" (Projects, uploads). Embeddings and vector search are OUT. |
| J. Building: web page, scripts, small tool, debugging, safe code, capstone | COVERED or PLANNED | Build and Automate | Good match to TripleTen's order. APIs and webhooks are OUT for a first pass. |
| K. Evaluation and trust | PARTIAL | Stay Safe: checking answers. Chains and checking in Start Here. | Missing: comparing two answers, a personal checklist for important work, "when to trust it". Formal evals and benchmarks are OUT. |
| L. Privacy, scams, when not to use | COVERED or PLANNED | Stay Safe (3 written, scams planned) | Missing: prompt injection in plain words (when pasted content tries to give instructions), and permission limits when giving an AI access to files or accounts. These matter more once she uses connectors or agents. |
| M. Fine-tuning, open-source, LLMOps | OUT | none | Engineer topics. |
| N. Research papers, interview prep, system design | OUT | none | |
| N. Career paths (bootcamps) | OPTIONAL | link-only bridge after Build capstone | Already proposed in 11-13 outline. |
| O. Selling AI-made work rules | PLANNED | Make Things | Still needs primary Etsy verification, per the 11-13 file. |

Deliberately out of scope for a beginner (all are real topics, each needs code, an API key or an engineering role): fine-tuning, embeddings and vector databases, building RAG pipelines, function calling in code, API and webhook work, sandboxes, benchmarks, observability and tracing, harness design, paper reading, interview and system-design prep, model-family deep dives.

## 4. Top gaps

1. Nothing on Claude's own power features (Projects, Skills, connectors, agents). Every source's "practitioner" tier covers it, and she pays for Claude.
2. Agents and workflows have no home. One plain-words lesson and one hands-on workflow are missing.
3. Evaluating and trusting outputs stops at "check the facts". Missing a repeatable checking habit and a way to compare answers.
4. Safety is not yet updated for tools that act: prompt injection and permission limits.
5. Small prompting and basics holes: context limit, memory across chats, "ask about my own documents".
6. Make Things plan lacks audio and music (in the 11-13 outline, not on the list you gave me).

## 5. Recommended additions, ranked

Paid-only marks are from my general knowledge of Anthropic's plans. **I did not retrieve Anthropic's current plan pages in this run, so every "paid" mark below is UNVERIFIED.** The 11-13 fact pack (`research\teacher\2026-11-13-fact-pack.md`) fetched claude.com pricing, so check it there before writing anything. Features and menu names change often.

| Rank | Addition | Where it sits | Lessons | Paid? | Why |
|---|---|---|---|---|---|
| 1 | **Claude power tools section, part 1: Projects and memory.** Make a project, add files and standing instructions, ask questions about your own documents, keep the household or a hobby in one project. | New Track 1B or Track 4 "Claude Power Tools", after Start Here lesson 9 | 2 | Unverified, believed to need a paid plan for full use. VERIFY | Biggest beginner payoff, also covers "chat with your documents" without RAG jargon. |
| 2 | **Evaluating and trusting outputs.** A checking habit for important work, comparing two answers, asking Claude to argue against itself, a "trust ladder" (low, medium, high stakes), keeping a log of misses. | Extend Start Here lesson 9 or a new section in Stay Safe, plus a short Power Tools tie-in | 2 | Free | Fills the evals gap in beginner terms. Most-requested theme across sources (K group). |
| 3 | **Safety for tools that act.** Prompt injection in plain words, what to allow and not allow when giving Claude access to files or accounts, undoing and reviewing what it did. | Stay Safe | 1 to 2 | Free to read, applies when she uses connectors | Needed before any connector or agent lesson goes live. Put it first in order, not last. |
| 4 | **Skills (reusable instructions).** What a skill is, when to turn a prompt you reuse into one, write one, test it, share it. | Power Tools | 1 to 2 | Unverified, believed paid-only. VERIFY | Natural next step after the prompt library lesson (Start Here 8). |
| 5 | **Connectors and MCP in plain words.** What "connecting Claude to your calendar, files or notes" means, what data leaves your account, set one up, turn it off. | Power Tools, after the safety lesson | 2 | Unverified, believed paid and plan-dependent. VERIFY. Needs Zac's or her own account decision, and a privacy check per connector | Covers F group at her level. Do not teach code or building a connector. |
| 6 | **Agents and workflows.** What an agent is versus a chat, a multi-step task with a human check at each step, when not to let it run alone. A no-code automation example from the Build track. | Power Tools (1 lesson plain words), and Build and Automate (1 lesson multi-step workflow) | 2 | Mixed. Agent-style features paid, VERIFY. A no-code automation tool may also have free limits, VERIFY | Matches the AI Automation order (tools, then automation, then agents). |
| 7 | **Make Things extras.** Voice and music safely, photo restore (both in the 11-13 outline). | Make Things | 2 | Free | Already designed, just not on your list. |
| 8 | **Basics micro-lesson: context, tokens and why Claude forgets.** | Start Here, between lessons 2 and 3 or as a sidebar | 1 | Free | Closes the A and B gaps cheaply. |
| 9 | **Further reading page.** Link only, with warnings: Microsoft Learn lessons 4 and 5 and responsible use, the no-math intro course and Use AI 101 from the aishwaryanr list (after a human checks signup), steven2358 as a "vet before you sign up" directory. | Site-wide resource page | 0 (one page) | Free to read | Consistent with the 11-13 repo review. Skip harness engineering. |

Counting: about 12 to 15 new lessons if all are built (items 1 to 8), of which 5 to 7 are the Power Tools section proper (items 1, 4, 5, 6 plus a safety lesson that sits in Stay Safe). Suggested order of build: 3, 1, 2, 4, 5, 6, then 7 and 8.

Suggested Power Tools section shape (5 lessons): P1 Projects and memory, P2 Skills, P3 Connectors and MCP in plain words, P4 Agents and workflows, P5 Evaluating and trusting outputs. The safety lesson (item 3) is a prerequisite that lives in Stay Safe.

Section ordering note (my inference): Power Tools should unlock after Start Here and Stay Safe checking, so she meets prompting and verification before anything that can act on her files.

## 6. What I did not verify

- Lesson bodies on the site. I listed file names only. "Written" and "planned" come from Zac's brief.
- Every paid-only claim in section 5. No Anthropic plan page was fetched this run.
- Whether features named (Projects, Skills, connectors) are available on her specific plan or on the free tier today.
- Contents behind any link in the four repos (Use AI 101, the no-math course, the agent crash course, the personal assistant course).
- The four repo summaries are from a small model reading each page. Section lists are likely accurate, descriptions are paraphrase of its summary.
- TripleTen was reused from the 11-13 file, not re-fetched.

## 7. Sources

WebFetch of github.com pages on 2026-11-14: walkinglabs/awesome-harness-engineering, microsoft/generative-ai-for-beginners, steven2358/awesome-generative-ai, aishwaryanr/awesome-generative-ai-guide. Local files read: `research\teacher\2026-11-13-github-repos-review.md`, `research\teacher\2026-11-13-course-outline-research.md`, directory listing of `Teacher\site\docs`.
