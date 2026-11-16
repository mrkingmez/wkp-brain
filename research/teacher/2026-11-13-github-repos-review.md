# Teacher: four GitHub repos reviewed, 2026-11-13

Method: GitHub web pages and the public GitHub API through WebFetch. No clone, no download, no signup. Numbers below are as the API returned them on 2026-11-13. Stars drift daily. Page summaries came from a small model reading each page, so structure claims are "as summarized", not line-checked. Nothing here was copied from the repos.

Learner: beginner adult, free Claude and free ChatGPT only, no code, no card.

## Bottom line

| Repo | Recommendation | One reason |
|---|---|---|
| walkinglabs/awesome-harness-engineering | SKIP | Written for engineers running coding agents, nothing a beginner can use. |
| microsoft/generative-ai-for-beginners | LINK ONLY (Lessons 4 and 5 read-only), ADAPT not advised | Free to read, but the build lessons need Azure or OpenAI keys and code. |
| steven2358/awesome-generative-ai | LINK ONLY | Big tool directory, handy as Further reading, mixed with paid and risky tools. |
| aishwaryanr/awesome-generative-ai-guide | LINK ONLY (Use AI 101 and Generative AI Genius only) | Has a real beginner path, rest is research and interview prep. |

## 1. walkinglabs/awesome-harness-engineering

- What it is: curated link list on "harness engineering", the setup around AI agents so they run reliably (context, guardrails, evals, runtimes). Observed from README.
- Last commit: 2026-11-09 (API commit date; merge of a CC0 license text fix).
- Stars 4,710, forks 494, size 179 KB (API). Created 2026-03-29, so under eight months old.
- License: Creative Commons Zero v1.0 Universal (CC0-1.0). Public domain dedication. Copying, adapting, commercial use all allowed, no attribution required. Attribution is polite, not owed.
- Structure (as summarized): Courses, Foundations, Context and memory, Guardrails and safe autonomy, Specs and agent files, Evals and observability, Benchmarks, Runtimes and reference implementations.
- Audience: engineers and researchers building or operating agent systems. Assumes Claude Code, Codex, MCP, CLIs, git, CI, APIs.
- Quality and currency: current. Many listed tools are self-described alpha or pre-alpha, some entries are self-promotion, and one hosted leaderboard is noted as down. Vendor security claims are unverified.
- Flags: nearly everything assumes API keys, installs, and code. Not safe-or-unsafe content, just the wrong level and risky to a beginner who might run an agent tool with file access.
- Fit to tracks: none for Start Here, Make Things, or Stay Safe. For Build and Automate, at most a Further reading line for a future advanced doorway, and only after she has finished the course. The Guardrails section is conceptually related to Stay Safe but is written for developers.
- Recommendation: SKIP. One reason: the audience is engineers, and linking it would send her to material she cannot use or safely try.

## 2. microsoft/generative-ai-for-beginners

- What it is: Microsoft's open course, lessons plus code samples. Description says 21 lessons, the table runs 00 to 21 (22 entries as summarized).
- Last commit: 2026-11-02 (merge of a markdown validation fix). API pushed_at shows 2026-11-12, so there is later activity not on the main commit list I fetched. I am reporting the commit I retrieved and the pushed_at separately.
- Stars 123,465, forks 66,376 (API). Size 6,639,791 KB, about 6.6 GB, mostly translations and images. Do not clone it. A translations folder exists (API listing returned 200).
- License: MIT, copyright Microsoft Corporation (LICENSE file retrieved). Allows use, copy, modify, publish, distribute, sublicense, sell. Condition: keep the copyright notice and license text with copies or substantial portions. No warranty. Caveat: I only read the root LICENSE. I did not check whether images, logos or linked media carry separate terms. Microsoft marks and course branding are not licensed to us by an MIT file. Check before reusing any image.
- Lessons (as summarized): 
  - Learn: 00 Course Setup, 01 Intro to Generative AI and LLMs, 02 Exploring and Comparing LLMs, 03 Using Generative AI Responsibly, 04 Prompt Engineering Fundamentals, 05 Creating Advanced Prompts, 12 Designing UX for AI Applications, 13 Securing Your Generative AI Applications, 14 Application Lifecycle, 18 Fine-Tuning LLMs, 19 Building with SLMs, 20 Mistral models, 21 Meta models. The numbering I received was off by one in places, so confirm the exact numbers on the repo before linking.
  - Build: Text generation apps, Chat apps, Search with vector databases, Image generation apps, Low-code AI apps, Function calling, RAG and vector databases, Open source models and Hugging Face, AI Agents.
- Needs paid keys, cloud, or code (observed in the setup page):
  - A GitHub account and forking the repo (account is free, but it is an extra signup).
  - Coding lessons call Azure OpenAI or Microsoft Foundry models, which need an Azure subscription and API key, or an OPENAI_API_KEY. The page does not state pricing or whether a card is required, so treat it as likely yes and unverified.
  - GitHub Models and the GITHUB_TOKEN route retire at the end of July 2026 per the page, so that old free path is gone.
  - Python and pip installs for local runs. Optional Miniconda, VS Code, Docker.
  - Foundry Local runs models on your own machine with no cloud subscription, but it is a heavy install and needs capable hardware. Hardware needs not verified.
- Free-tools-only: the Learn lessons are readable with no account. The Build lessons are not usable with free Claude and free ChatGPT, since they are code against model APIs. The page itself names no free path for the coding lessons.
- Audience: people who can read basic Python or TypeScript. Not a no-code course despite the title.
- Quality and currency: high production quality, actively maintained, but the setup page has an internal mismatch (Foundry variables in one step, OPENAI_API_KEY in another) that the page does not reconcile.
- Fit to tracks:
  - Start Here and Make Things: the prompt engineering Learn lessons and the responsible use lesson can be Further reading after our own lessons. Our Track 1 lessons already cover this ground.
  - Build and Automate: Build lessons are an advanced doorway only if she later wants code and decides to open a key herself. Not part of a free-only path.
  - Stay Safe: the responsible use lesson as a read-only link. The securing-applications lesson is for developers.
- Recommendation: LINK ONLY, and link the specific Learn lessons, not the repo root, so she does not land in setup steps that ask for keys. ADAPT is legal but not worth it. If we ever adapt a passage, the required attribution is the copyright notice and the MIT license text with it. One reason: the readable parts duplicate what we are writing, and the hands-on parts need keys.

## 3. steven2358/awesome-generative-ai

- What it is: a curated directory of generative AI models, apps, dev tools and learning resources, organized by modality.
- Last commit: 2026-10-30 (retrieved, message about a homepage link).
- Stars 12,830, forks 2,763, size 476 KB (API). Created 2022-10-20. About 1.3k open pull requests per the page, so submissions queue up and quality control is mostly the maintainer's.
- License: Creative Commons Zero v1.0 Universal. Copying, adapting, commercial use all allowed, no attribution required. Fine to quote entries, but a tool list goes stale, so copying it is not wise.
- Structure (as summarized): Foundations, Text (chatbots, search, writing assistants, productivity, research tools), Coding, Agents, Image/Video/Audio (including avatars, text-to-speech, music), Other, Learning resources, More lists.
- Audience: developers and technically inclined creators, with some sections friendly to general users.
- Quality and currency: current, mentions 2026 items. It is a catalog, not a vetting service. Large share is commercial or freemium.
- Flags: many entries need a paid plan, an account, or a card after a trial. Voice cloning, talking avatar and realistic video tools are listed, which is a deepfake and scam-risk area relevant to Stay Safe. Autonomous agent and computer-control tools carry risk without guardrails. The page does not mention NSFW (the summary reading was inference only). Character chat platforms may allow adult content, not stated.
- Fit to tracks: Make Things (a Further reading link for finding image, music or video tools), Stay Safe (a "why you should vet a tool before you sign up" example, referencing the voice cloning category without linking tools).
- Recommendation: LINK ONLY, with a note: "a long list, not a recommendation list, check pricing and privacy before signing up for anything." One reason: useful discovery tool, but it mixes free, paid and risky entries without telling a beginner which is which.

## 4. aishwaryanr/awesome-generative-ai-guide

- What it is: learning hub with courses, paper roundups, interview prep, notebooks and video guides, maintained by one author and LevelUp Labs.
- Last commit: 2026-11-02 (retrieved, message about a Harness Engineering transcript).
- Stars 30,265, forks 6,070, size 188,394 KB (about 188 MB, API, mostly assets). Do not clone.
- License: MIT, file is LICENSE.md (the root LICENSE path returned 404, the API license endpoint returned LICENSE.md), copyright Aishwarya Naresh Reganti, 2024. Allows use, copy, modify, publish, distribute, sell. Condition: keep the copyright and permission notice with copies. Caveat: the license covers the repo's own content. Linked courses, Maven cohorts and sponsored tools are separate and have their own terms.
- Structure (as summarized): three journeys (Use AI, Build AI, Understand AI) each with 101, 201, 301 levels; nine topic areas; five free LevelUp Labs courses; tools list; interview prep (four role tracks and ten system-design case studies); monthly paper lists (latest June 2026); glossary.
- Free courses named: AI Evals for Everyone, OpenClaw Mastery for Everyone (10-day personal assistant setup, likely heavy and install-based, not read), Agentic AI Crash Course, Generative AI Genius (no-math beginner intro), Applied LLMs Mastery 2024 (archived). The page lists no prerequisites and does not state provider or account terms, so whether each course needs an account or card is not verified.
- Audience: mixed. Use AI 101 and Generative AI Genius look beginner. Build AI 201 and 301, papers, interview prep, system design are for engineers and researchers.
- Quality and currency: active and broad, but promotional links to paid cohorts and sponsored tools sit alongside free material. The page itself says the maintainers do not endorse sponsored tools.
- Flags: OpenClaw Mastery (personal assistant that you set up) could involve installs and keys, and I did not read it. Treat as not for her until someone checks it. I did not open the Use AI 101 page, so its actual content and fit are unverified.
- Fit to tracks: Start Here (Further reading: Generative AI Genius, after a human opens it and confirms it is no-signup and no-card), Build and Automate (Agentic AI Crash Course only as an advanced doorway, unverified requirements), Stay Safe (a safety and security topic area exists, not read).
- Recommendation: LINK ONLY, and only to the Use AI 101 page and the Generative AI Genius course, after a quick human check of both for signup and card requirements. One reason: it has the one clear beginner path of the four, and the rest is not her level.

## What I did not verify

- Whether any linked course, tool or page needs a signup, a card or a paid plan. I read repo pages only, not the courses behind them.
- The exact lesson numbers in the Microsoft course (the summary was off by one in places), and whether any image or media in that repo has separate terms.
- Contents of Use AI 101, Generative AI Genius, OpenClaw Mastery, or any Microsoft lesson body.
- Individual entries in either awesome list for dead links or scam tools. Spot checks only of structure.
- Stars and sizes are API numbers from 2026-11-13 and move.
- License text for the two CC0 repos was taken from the API license name, not from reading their LICENSE files.

## Sources

GitHub API: api.github.com/repos/walkinglabs/awesome-harness-engineering, microsoft/generative-ai-for-beginners, steven2358/awesome-generative-ai, aishwaryanr/awesome-generative-ai-guide, plus each repo's commits endpoint (per_page=1), the aishwaryanr license endpoint, and the Microsoft contents/translations listing. GitHub pages: each repo root and microsoft 00-course-setup README. Raw LICENSE for microsoft. All retrieved 2026-11-13.
