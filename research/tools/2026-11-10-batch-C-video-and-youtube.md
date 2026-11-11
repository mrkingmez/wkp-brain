# Batch C: video and YouTube tools (notebook list)

Date read: 2026-11-10. Research only. Nothing installed, downloaded, run or called. Sources are web pages read today unless marked.
Earlier review reused: Graphify was "Maybe later" on 2026-10-30. Open Higgsfield / Open Generative AI and Wan2GP were tried and REMOVED 2026-10-31 (local models fell far short of Veo 3.1). That is why local video is rated low below.

## Ranked list, best first

1. yt-dlp: USE WITH LIMITS (stills, audio, own-channel files, transcripts; NOT bulk clip ripping)
2. YouTube Data API: USE WITH LIMITS (Analytics read first, uploads stay manual)
3. OpenMontage: USE WITH LIMITS (one zero-key test for What If only)
4. Remotion: USE WITH LIMITS (already covered, small gaps)
5. Graphify: MAYBE LATER (unchanged from 10-30)
6. "AI-Video" survey: MAYBE LATER (nothing free beats Firefly Veo 3.1 and Kling that Zac already has)
7. "YouTube Video Generator" / "Video Genius": SKIP

---

## 1. yt-dlp

- **Matched:** yt-dlp, github.com/yt-dlp/yt-dlp. Confidence HIGH.
- **What:** command line audio and video downloader, thousands of sites. Source: https://github.com/yt-dlp/yt-dlp (read 2026-11-10).
- **License:** Unlicense for the repo and PyPI package. The prebuilt .exe bundles GPLv3+ code, so the exe is GPLv3+ as a combined work. Same page.
- **Activity:** latest release 2026.10.26 published 2026-10-26 (https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest). About 207k stars, 24,037 commits (repo page). Very active.
- **Cost:** free.
- **Security:** download only from the official GitHub releases or PyPI, verify hash. For YouTube it needs a JavaScript runtime to solve YouTube challenges: Deno 2.3.0 or newer (default), or Node 22 or newer via `--js-runtimes node` (https://github.com/yt-dlp/yt-dlp/wiki/EJS). Zac's PC has Node 26, so that part is covered. Never feed it browser cookies without thinking: cookie options give it your logged-in session.
- **Terms and copyright (important):** YouTube's Terms of Service forbid you to "access, reproduce, download, distribute..." any Content "except as expressly authorized by the Service" or "with prior written permission from YouTube and, if applicable, the respective rights holders". Personal use is limited to viewing or listening, and embedding through the official player is allowed (https://www.youtube.com/t/terms, read 2026-11-10). So downloading a trailer from YouTube breaks YouTube's terms even if the clip is later used under fair use. Fair use is a defense to a copyright claim, not permission from YouTube, and a copyright owner can still file a claim that Zac then has to dispute. The yt-dlp project page has no legal disclaimer. I am not a lawyer, this is the plain reading of the terms.
- **Plug in:** a local command Claude runs through Bash, only after Zac's per-download yes (existing WKP rule: downloads need his OK). Nothing to install into Claude Code itself.
- **Verdict: USE WITH LIMITS.**
  Good uses: (a) pull audio or the video of WWD's OWN uploads for Shorts and transcripts; (b) fetch a creator's own public-domain or Creative Commons material; (c) get captions or metadata for research; (d) pull video from sources whose terms allow it (Archive.org, NASA, Wikimedia Commons, which OpenMontage also lists as free sources). For review clips, WKP's current path (official trailers, short, muted, rights agent check) stays. If Zac OKs a trailer download, yt-dlp is a better tool than screen recording, but each pull is a named download with a rights check and logged, never a bulk ripper, and never a way to grab studio clips beyond trailers. Studio trailer hosting on the studio's own site or press kit pages is a cleaner source than YouTube when it exists.
- **First safe test:** with Zac's yes, install nothing new first. Run `yt-dlp --version` is not possible until installed, so the test is: install by the official release exe into `D:\Tools\yt-dlp\`, then run it with `--skip-download --write-info-json` on one of WWD's own videos to read metadata only. No media downloaded.

## 2. YouTube Data API (plus Analytics API)

- **Matched:** YouTube Data API v3. HIGH.
- **What it can do:** read channel, video, comment and playlist data; upload (`videos.insert`); set thumbnails; manage captions; post and moderate comments.
- **Quota (retrieved):** default 10,000 units per day for all endpoints except two separate buckets of 100 calls per day each for `search.list` and `videos.insert`. Resets midnight Pacific. Costs: videos.list 1, commentThreads.list 1, comments.insert 50, thumbnails.set 50, captions.list 50, captions.insert 400, captions.update 450, captions.delete 50. Each `videos.insert` call counts 1 from its own 100 per day bucket. Sources: https://developers.google.com/youtube/v3/determine_quota_cost and https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits (both read 2026-11-10). More quota needs a compliance audit form.
- **Cost:** free, within quota. A Google Cloud project is needed (no payment shown on the pages read; billing requirement NOT CONFIRMED).
- **OAuth:** reading public data (video stats, public comments) works with an API key. Anything on Zac's own channel (uploads, private analytics, thumbnails, captions) needs OAuth consent as Zac. Upload needs scope `youtube.upload` or broader (https://developers.google.com/youtube/v3/docs/videos/insert).
- **Upload privacy:** the docs page for `videos.insert` says uploads from unverified API projects are not restricted to private. I know of an older rule that forced such uploads private; the current page says the opposite, so treat it as unresolved until tested. NOT VERIFIED beyond that page.
- **Analytics API:** separate API for channel owners' reports (views, trends); there is also a Reporting API for bulk reports. The page read did not state scopes or quota for either. NOT AVAILABLE: Analytics scopes and quota (https://developers.google.com/youtube/analytics, read 2026-11-10).
- **Security:** OAuth tokens and client secret are secrets: environment variables only, never files in the repo. Revoke access at myaccount.google.com if unused.
- **Plug in:** a small local Python script in a skill's `scripts\` folder, or a community MCP server (not reviewed here).
- **Verdict: USE WITH LIMITS.** Biggest win is reading data the 744-sub channel currently gets by hand or through VidIQ credits (which are at 0 until 11-11): per-video views, retention-adjacent metrics through Analytics, comment pulls for the weekly review. This feeds the subscriber loss tests already running. Uploads: technically possible and cheap (1 unit of 100 per day), but the standing rule is nothing posts publicly without Zac, so use it at most to create PRIVATE or scheduled drafts, and only with his yes. Comment replies (50 units each) should stay a human job.
- **First safe test:** with Zac's yes to create a Google Cloud project and an OAuth client, do one read-only call: `videos.list` for WWD's own latest video IDs. Costs 1 unit. No writes.

## 3. OpenMontage (already cloned, audited, never tested)

- **Matched:** calesthio/OpenMontage, AGPL-3.0, created 2026-03-29, last push 2026-11-09, about 79k stars (https://api.github.com/repos/calesthio/OpenMontage and https://github.com/calesthio/OpenMontage, read 2026-11-10). Local clone is at commit 195eab2 (audited, not redone). Your clone is behind the latest push by an unknown number of commits, NOT CHECKED.
- **What:** agent-driven video production inside Claude Code: research, script, assets, edit, render. 12 pipelines per the README, including Documentary Montage, Animated Explainer, Clip Factory, Podcast Repurpose, Screen Demo, Talking Head, Cinematic, Localization and Dub.
- **Zero-key mode (README):** Piper offline narration, Remotion and HyperFrames rendering, FFmpeg, built-in word-level captions, free footage from Archive.org, NASA, Wikimedia Commons (no key), and Pexels, Pixabay, Unsplash (free but need a free developer key). `make demo` renders zero-key demos. Paid cloud tools (Kling, Veo, Runway, ElevenLabs, Suno, FLUX) only turn on if a key is set.
- **AGPL note:** fine for private use. If WKP ever offers the tool itself as a network service to others, the AGPL source rule applies. Rendering videos with it does not make the videos AGPL (my reading, not legal advice).
- **Overlap with Batch C:** it already bundles Remotion, FFmpeg, free stock footage sources, captions, and a Clip Factory pipeline for Shorts. It does NOT need yt-dlp for its zero-key mode. It overlaps most of "AI-Video" and "YouTube Video Generator", so those two are mostly covered if the test passes. Zac's existing `remotion-motion-graphics` skill is a separate hand-built path and may conflict in style rules, so keep one owner per project.
- **Fit for What If:** documentary montage from free archival sources (NASA and Wikimedia are weak for military history, Archive.org has public domain film such as US government WWII footage, quality varies, rights per item must be checked) plus Piper narration plus Remotion. The format laws in `WKP-CHANNEL\CLAUDE.md` stand: scripts come from the writing room and the format skills, evidence tags and "closing with the three weakest claims" must be kept. OpenMontage must not write What If claims by itself.
- **Fit for WWD:** the Clip Factory and captions could help Shorts, but WWD's shorts-factory already exists and is built to Zac's spec. Test only if What If test is good.
- **Verdict: USE WITH LIMITS.**
- **First honest test (zero keys, zero spend):** a 30 to 45 second What If style teaser from a script the writing room already approved, using only `make demo` first (to prove the install works), then one documentary-montage run on a single public-domain Archive.org WWII clip with Piper narration. Pass criteria: renders end to end, captions are correct, every asset has a logged source and license, no paid tool called, no unlicensed clip, output is watchable beside a normal edit. Run it in a scratch folder under `D:\WKP\scratch\`. Do not set any API key. Pull the latest commit only after a fresh diff review (your audit covers 195eab2 only).

## 4. Remotion

- **Matched:** remotion-dev/remotion. HIGH. Last push 2026-11-10, about 72k stars, license shown as NOASSERTION on GitHub (custom license), so it is source-available, not plain open source (https://api.github.com/repos/remotion-dev/remotion, read 2026-11-10).
- **Cost and license:** Remotion's license page says individuals and companies of up to three people are free. Company licenses for others: Creators $25 per month per seat, Automators $0.01 per render with a $100 per month minimum, Enterprise from $500 per month (https://www.remotion.pro/license, read 2026-11-10). WKP is Zac alone, so free. Check again if WKP adds staff or Post-Production sells paid client work with more than three people.
- **Security:** npm packages and a Chromium download at render time. Install with the project's lockfile, no global installs.
- **Plug in:** already there. `D:\WKP\.claude\skills\remotion-motion-graphics\SKILL.md` covers: easing rules, five-layer scenes, Ken Burns, theme object, render command, and a mandatory frame check. It uses `npx remotion render`.
- **What is missing (from the first 80 lines of the skill that I read; I did not read its references):**
  1. License note: no mention of the free-for-three-people limit.
  2. No WWD or What If brand theme file (WWD fonts and colors, What If map-and-timeline look). Without it every video gets the generic default.
  3. No recipes for the two real jobs: a branching timeline or map graphic for What If, and a "Next Up" or sticker kit that is currently built in Python at `P:\WWD Kit\`. Decide whether to keep Python or move to Remotion, not both.
  4. No captions recipe tied to Whisper word times (the `@remotion/captions` package exists, I did not verify its current state).
  5. No handoff rule to Premiere (Zac edits in Premiere, so Remotion output should be ProRes or alpha MP4. Note the log says ProRes froze on Zac's machine, so use MP4).
- **Verdict: USE WITH LIMITS.** Keep the skill. Add a short What If theme and one timeline component when the channel actually starts.
- **First safe test:** none needed now. When What If starts, build one animated map or timeline card from a theme file and check frames per the skill.

## 5. Graphify

- **Matched:** Graphify-Labs/graphify (PyPI `graphifyy`). Earlier review matched the same repo. Confidence MEDIUM to HIGH.
- **Facts:** Apache-2.0 (sidebar also lists MIT), about 145k stars, last push 2026-11-09, 1,637 open issues (https://api.github.com/repos/Graphify-Labs/graphify and https://github.com/Graphify-Labs/graphify, read 2026-11-10). Turns code, docs, PDFs, images and (optional extra) audio and video into a queryable graph. Code is parsed locally with no LLM. Docs, PDFs and images go to the model (Claude or a configured provider). No telemetry stated, queries logged locally to `~/.cache/graphify-queries.log`. Graphify Cloud is a separate paid product, not needed.
- **Security and fit:** same concern as 10-30: the Claude install step adds a hook that fires before Read, Glob and some Bash calls, which would sit inside Zac's custom setup. Use package-only, skip the install step. Optional video extra uses local faster-whisper. For Batch C: it could index a folder of What If research notes or transcripts, but WWD's transcripts already work and What If has no notes yet.
- **Verdict: MAYBE LATER**, unchanged. First safe test, whenever wanted: `--code-only` style run on a copy of one research folder in scratch, no install step, no cloud.

## 6. "AI-Video" (survey, generic)

- **Matched:** no single project. Survey only. Zac already has Firefly with Veo 3.1 and Kling 3.0, Runway Gen-4.5 and Luma, which are paid-by-credit (Matt paid for credits per memory). The 10-31 test of free local models (Open Generative AI, Wan2GP) failed on quality and stability.
- **Open weights, local (GPU needed, Zac has an RTX 5060):**
  - Wan 2.2, Apache-2.0, about 18.5k stars, last push 2026-09-21 (https://api.github.com/repos/Wan-Video/Wan2.2).
  - LTX-Video, Apache-2.0, about 11.4k stars, last push 2026-11-02 (https://api.github.com/repos/Lightricks/LTX-Video).
  - Reality check: the 10-31 test already found local models well below Veo 3.1. VRAM of the RTX 5060 is NOT retrieved here, and it limits clip length and size. Not worth repeating without a specific reason.
- **Free tiers of hosted tools:** one web search returned only vendor listicles that contradict each other (for example one says Microsoft Clipchamp has unlimited 1080p exports without a watermark on its free tier, another lists CapCut or Pika, Pika at 480p, Kapwing 720p with watermark). Results are marketing pages and change often, so I did NOT verify any free tier on an official pricing page. Treat as UNVERIFIED. Source list: https://scrimba.com/articles/free-ai-video-generators-2026/ and https://fast.io/resources/best-free-ai-video-generators-2026/ (search results only, not opened).
- **Verdict: MAYBE LATER.** For What If, which needs mostly maps, archival footage, stills and motion graphics rather than generated video, generated footage is the wrong core anyway (period-accurate visuals and the "no invented" spirit of the format). Spending nothing new: use Firefly credits already paid for, OpenMontage's free sources, and Remotion. Revisit if a specific scene needs a shot no archive has.
- **First safe test:** none. If wanted, open each official pricing page in Chrome (Clipchamp, CapCut) and record the free-tier limits on the date read.

## 7. "YouTube Video Generator" / "Video Genius"

- **Matched:** no project named Video Genius or YouTube Video Generator found. Confidence LOW. Search returned a handful of faceless-video repos (https://github.com/topics/faceless-video-generator, search results, read 2026-11-10):
  - SamurAIGPT/AI-Faceless-Video-Generator, MIT, about 407 stars, Jupyter notebook.
  - codewithdark-git/Faceless-short (AutoShorts AI), Python.
  - ULNIT AI Video Factory, Python stdlib plus Pillow and FFmpeg.
  - VUZA, described as free and open source.
  Star counts, last commits and safety NOT VERIFIED for any except the first star count.
- **Fit:** these make generic topic-to-video output from AI scripts. That is the "generic AI video" look WKP's rules and the writing room are set up to avoid, and it bypasses the writing room, devils-advocate and format laws. Automated "zero human input" pipelines also risk YouTube's reused or mass-produced content policy (policy page NOT checked here).
- **Verdict: SKIP.** OpenMontage already does the legitimate version with human gates. If Zac meant a specific product named Video Genius, send a link or the notebook page and it can be matched.

---

## Open questions for Zac

1. Does he want to OK a read-only YouTube Data API setup (Google Cloud project plus OAuth for WWD)?
2. Does he OK installing yt-dlp for metadata and own-channel uses only, with per-clip yes for any trailer?
3. Is the OpenMontage zero-key test approved to run in scratch, after the writing room supplies a script?
4. What does "Video Genius" refer to?

## Not retrieved (so not claimed)

yt-dlp last commit date; OpenMontage commits since 195eab2; YouTube Analytics scopes and quota; whether a Google Cloud billing account is required; current unverified-project upload privacy behavior; Remotion references files in the local skill; official free-tier limits of any hosted AI video tool; RTX 5060 VRAM; YouTube reused-content policy text.
