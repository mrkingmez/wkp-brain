# System Reset Report, 19 November 2026

Short version: the agents were not broken one at a time. The system around them was. Rules lived in four places that disagreed, almost no agent read memory, and the WWD chain started too late. All of that is fixed. Nothing was spent, posted or pushed.

## 1. Your questions, answered

| Question | Answer |
|---|---|
| Does the music agent have a research partner? | **It did not. Now it does.** New bench `music-researcher` checks tool terms, licenses, free libraries and reference tempos for it. |
| Does he know the music we have? | **Only partly before, yes now.** He had a raw file list and missed the channel theme on L:. Your A Knight's Tale run sheet said "intro/outro music not found." There is now a music catalog of 5,450 owned audio files, with lengths. He reads it first on every job. |
| Can he create his own music? | **No, and nothing here can.** He writes prompts for Suno and ElevenLabs. He can also cut stings and outros from music you own, for free. A new generation costs credits, so it needs your yes, and he always hands you a free fallback cut. |
| Do the editor and assistant editor help WWD? | **They did not. Now they do.** The old spec told them WWD was off limits. Now every review gets a prep job from them. You still make the cut. |
| Can the editor practice on WWD stuff? | **Yes, and it already has.** A Knight's Tale has a prep stringout ready to drop on V2 (details in section 3). |
| Why was A Knight's Tale slow? | **The agents were not the slow part.** Their prep took about 48 minutes. Three things slowed you down. The chain only started after your edited transcript came in. The clip rule changed in the middle of the job, so the clips were cut twice. And you had to place all 49 stops by hand. |
| Is there memory for everyone? | **There was not, and now there is.** Before today, only 1 of 62 agents was told to read memory. Now every agent has its own lessons file. It reads that before each job and writes a new lesson after. |

## 2. What was there (the problems)

| Problem | Evidence |
|---|---|
| Agents started every job cold | Only 1 of 62 specs mentioned `memory\MEMORY.md`. The learning loop pointed at `memory\topics\lessons\`, which never existed. |
| Old rules outlived your corrections | `WWD\STANDARDS.md` still said 4 s clips and a 30 s cap after you changed it. The 6 s intro rule lived only in a memory file. |
| Files saved to different places | 15 path and format conflicts were found. Examples: run sheets named "Image Placement" vs "Edit Run Sheet". Root CLAUDE.md still said deliverables go to L:. Upload packages had two .md copies. Shorts captions had two homes. |
| WWD prep waited on the edit | The chain began only once your edited transcript existed. Vision Quest EP 8 sat about 46 hours between transcript and run sheet. |
| Editing department idle on WWD | The specs told head-editor and assistant-editor that WWD "is not yours." |
| Stale status lines | 14 specs said "loads next session" even though they were already live. |
| Specs point to missing files | Seven paths in five specs do not exist, for example `SciFi-Novel\` (the real folder is `SCI-FI Novel`) and `Shattered-Empire\world-bible.md`. Each is logged as a lesson for its owner. |
| Logging uneven | WWD benches and music wrote only to the WWD log. The root rule says every agent also gets a row in the ledger. |

## 3. What changed

**New files**
- `D:\WKP\SOP\`: six SOPs.
  - Master workflow
  - Output locations and formats, one table plus 15 conflict rulings
  - Agent memory and learning
  - WWD review workflow
  - Editing department
  - Music department
- `D:\WKP\memory\agents\`: one lessons file for each of the 63 agents. Each is seeded from your corrections and locked rules.
- `.claude\agents\music-researcher.md`: the new music research bench.
- `data\assets\music-catalog.md` and `.csv`, plus the script that rebuilds them, `.claude\skills\media-manager\scripts\build_music_catalog.py`. The script is read-only on P: and L:.
- A Knight's Tale prep:
  - Stringout: `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\prep\A-Knights-Tale-PREP-Stringout-v1.mp4` (36:37, 30 fps, silent, 31 pictures and 5 clips at their run-sheet times).
  - Plan: `WWD\reports\A-Knights-Tale-Prep-Assembly-Plan.md`, with head-editor notes.
  - Sound plan copied to `WWD\reports\A-Knights-Tale-Sound-Plan.md`.

**Edited**
- Every agent spec (62) now has a "Memory and learning" section, and 14 status lines were set to LIVE.
- `music.md` now has:
  - the research partner
  - the catalog as the first thing he reads
  - a plain "can and cannot make" section
  - the 6 s intro cap
  - "owned, license unproven" wording for files with no license proof
  - ledger logging
- `assistant-editor.md`, `head-editor.md`, `media-manager.md` and `studio-director.md` now carry the WWD prep job rule.
- `wwd-director.md`:
  - A reset section: start early, order music and kit at intake, pull clip stock the day after recording, order the prep job.
  - The dead older chain was removed.
  - The no-raw-transcript lock stays in place.
- `WWD\STANDARDS.md`: clip rule is now 6 to 8 s, 12 s max.
- `WWD\CLAUDE.md`: shorts count fixed, SOP pointer added.
- Root `CLAUDE.md`: deliverables line fixed, SOPs section added.
- `wwd-review-photo-pull\SKILL.md`: the "Image Placement" doc and the "lean on Cross Dissolve" line are gone.
- `wwd-audio-cut\SKILL.md`: the cut doc now gets a .docx too.
- `AGENT-NETWORK.md`: lessons path, spec-edit rule, music bench, and the new additions.
- `memory\MEMORY.md`: one pointer line.
- `memory\topics\wwd-skill-formats.md`: the captions line.
- `_spec\music-reference.md`.
- `TASKS.md` (A Knight's Tale row plus four new rows), `logs\agent-runs.md`, `logs\jarvis-delegation.md`.

**How learning works now**
1. Before every job, an agent reads its lessons file.
2. After every job, it writes one lesson.
3. When you correct something, it is written down as a lesson the same turn.
4. If an agent makes the same mistake twice, its director fixes that agent's spec the same day. This does not come to you.

## 4. Sign-off: is everyone happy?

| Agent | Verdict | Objections | Resolved? |
|---|---|---|---|
| qa-director | PASS WITH NOTES | 2 folders listed as "in use" do not exist yet; "revise in place" clashed with dated versions of recurring reports; seeded lessons marked CONFIRMED come from locked rules, not from new statements by you | First two fixed: folders marked "planned", and revise-in-place is scoped to working docs. The third is noted here. |
| wwd-director | AGREE WITH CHANGES | Calendar entries must be a flag plus a check that they exist; the skill must not hand-write copy; the audio-cut .docx should not need backfill; the FrostCast Messenger step was missing; the old chain was still in its spec | All 5 fixed |
| studio-director | AGREE WITH CHANGES | Its own spec still said WWD was off limits; prep needed a time budget; logging needed to be stated | All 3 fixed. Studio jobs win when they collide with WWD prep. |
| music | AGREE WITH CHANGES | The catalog has no loudness; the Adobe and Storyblocks licenses are unproven; 352 junk Mac files were counted; the researcher needed web fetch | All 4 fixed. Junk removed, count is now 5,450. |
| wkp-channel-director | AGREE WITH CHANGES | No row for its log; it approves documentary plans first; creative calls should go through it first; rows needed for research, scripts and art prompts | All 4 fixed |
| marketing-director | AGREE WITH CHANGES | The SOP had the writing order backwards (marketing writes the brief, then the writing room writes); the Opus copy row had no gates | All fixed, and a lesson was added to its file |

The sign-offs happened before the fixes. I did not run them again after fixing.

## 5. What still needs you

1. **Push to GitHub.** Everything is committed on this machine but not pushed.
2. **ElevenLabs intro and outro for A Knight's Tale** (decision WWD-2026-11-19-02, already in the queue). It is optional, because a free fallback cut from music you own already exists.

That's all. Your edit of A Knight's Tale is the next step in that pipeline. Posting stays with you, as always.

## 6. What I could not verify

- Nobody played or listened to the stringout. Only 3 of its 36 stops were checked by eye.
- The catalog only knows names, lengths and folders. It does not know mood, loudness or tempo.
- New agent specs (music-researcher) load at the next session start. Until then, run them through a general-purpose agent.
- I have not seen a live agent read its lessons file at the start of a job. That needs a new session.
- QA read only 3 of the 63 lessons files.
- The `_src\` cleanup in the A Knight's Tale folder (23.9 MB) is still pending, because the delete was blocked by a permission check. I did not move or delete any of your media.
- The end card and Next Up card for A Knight's Tale are not built yet. They are on the team's list for wwd-vfx.
