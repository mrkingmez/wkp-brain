# GLOSSARY

How WKP defines terms. Owner: chief-of-staff. Built 2026-11-21 from `SOP\`, root and WWD `CLAUDE.md`, `WWD\STANDARDS.md`, `memory\feedback-*.md`, and agent specs. If an SOP disagrees with this page, the SOP wins and this page gets fixed. A term marked (inferred) is my reading of how it is used, not a quoted definition: confirm with the owner before relying on it.

## Org and process
| Term | Meaning |
|---|---|
| Jarvis / Ares | The main session (CEO role). Plans, routes, reviews. Does not produce deliverables. Zac now says Ares |
| Director | Boss of one venture or department. Takes the task list, orders benches, approves. Directors ask each other directly |
| Bench | Worker agents behind a director. Called only through the boss |
| Shared department | Marketing, graphic design, music, fact research, market research, tracking, animation, studio, QA. Open to every director |
| Writing room | `script-room`. Writes every word for every department except Zac's books |
| Gate | A required check. Review gates (root CLAUDE.md): social copy through writing room and marketing and no-ai-slop; scripts get two writing-room passes; promo teases, never gives the verdict |
| QA PASS / PASS WITH NOTES / FAIL | qa-director result. FAIL is a send-back (one per side, then Jarvis) |
| Handoff note | The block at the top of every task sent between agents (`AGENT-NETWORK.md`) |
| DECISION QUEUED | An agent cannot ask Zac. It appends to `logs\DECISIONS.md` and returns this plus the ID |
| Ledger | `logs\agent-runs.md`, one row per agent job |
| Lessons file | `memory\agents\<agent>.md`. Read before a job, one lesson appended after |
| Honesty rule | Never report a number, status or date you did not read. Say "not available" and name the source |
| NOT VERIFIED / NOT KNOWN | Words for facts we could not check or IDs we do not have. Never fill with a guess |
| Locked | Zac decided on purpose. Only Zac changes it. Indexed in `LOCKS.md` |
| Scratch | `D:\WKP\scratch\`, gitignored, never system Temp |
| Deliverable | A human-read document: .docx in `D:\WKP Reports\<Type>\`, working .md in the repo |
| Drive mirror | Copying packages and Shorts to `N:\My Drive\...` ONLY when Zac asks |

## WWD and video
| Term | Meaning |
|---|---|
| Review | A WWD movie or series review video. Pipeline in `SOP\SOP-WWD-Review-Workflow.md` (A Knight's Tale is the model) |
| FrostCast | The weekly Wednesday 9 PM podcast and stream. Weekly chain in root CLAUDE.md |
| Den Files | Series on the true story behind a movie. Separate from the Wednesday slot |
| Raw recording | The uncut StreamYard record. Never transcribed or built from until Zac cuts the banter |
| Final / edited cut | Zac's exported edit. The upload package is built from its transcript |
| Transcript | Diarized speaker-labeled .txt saved next to the video. `--num-speakers` 2 or 3 |
| Chapters | Timecode topic list. Live only inside the full-video description |
| Run sheet (Edit Run Sheet) | One timeline-order doc for Zac's edit. Each stop: timecode, PNG number or SOUND ONLY or STICKER or CAM, the spoken line, picture, transition, sound path, steps. Never called "Image Placement" |
| Stop | One entry in a run sheet (one moment in the video) |
| USE folder | `<movie folder>\USE\`. Numbered 1920x1080 PNG pictures, contain-fit, never cropped, for the edit |
| Picture / cutaway | A still shown over the hosts. Max 7 s on screen, never reused in one video. WWD is not faceless |
| Solo cam / CAM callout | A cut to one host's own camera, a few per video, only when a host has the floor |
| Clip | Trailer or film footage, 6 to 8 s (12 s max), under a host line about that scene, muted |
| Transition | A designed Adobe Modern transition with a paired owned sound on about half of the placements |
| Sting | A short sound or music hit. Review intro sting is 6 s or less |
| Intro / outro | Only places music is allowed. No music bed under conversation |
| Sticker | Finished drop-in clip with sound in `P:\WWD Kit\Stickers\` (Wolfie Award Nominee, Recommend Watch, Save Yourself the Time, Dumpster Fire). Used only where a host says it |
| Poster open | The built opening that shows the poster at the start of a review |
| Card (YouTube card) | An in-video link. Exactly 3 per upload package, card 3 always FrostCast, all before 3:00, only to videos that exist in the library |
| Card (kit card) | A built graphic: End Card, Next Up card, title card in `P:\WWD Kit\Cards\` |
| Next Up card | Kit card naming the next review (series reviews allowed, with a sub line like SEASON 1 REVIEW) |
| End screen / end card | The closing tiles and card |
| Hook | The opening line or first seconds of a video or Short. Opus rule: must hook in the first three words |
| Hook text | On-screen text for that hook, required per Short |
| Upload package | ONE doc: Title (two options), Description, Tags (under 500 chars), exactly 5 Hashtags, Thumbnail, Cards, End Screen, Post Sequence (full video, Facebook, Instagram, Shorts 1 to 5), Flags, Fair Use (always last) |
| Package | Short for upload package. In editing, "prep" is different (below) |
| Shorts / Reels | Vertical clips. Review: 5 max, all finished, burned-in captions. FrostCast via Opus Clip on the cadence in `LOCKS.md` |
| Approved copy | `EPnnn-approved-copy.json`, the gated captions per clip for YouTube, Instagram, Facebook |
| Opus project | The Opus Clip project ID a week's FrostCast Shorts were scheduled from (e.g. P31119047Y39) |
| Prep stringout | A rough assembly of the review from the run sheet, pictures and clips, for Zac to polish. Made by assistant-editor with head-editor notes |
| Sound pull | Copies of every sound the run sheet names, in `P:\WWD Kit\<Movie>\Sounds\`, one folder per stop, plus a pull sheet docx. assistant-editor's duty |
| WWD Kit | `P:\WWD Kit\`. Zac's owned finished kit pieces (cards, stickers, stings, openers, color LUTs, per-movie folders) |
| P: drive | Everything Zac owns: sounds, music, stock footage, tools. Index at `data\assets\p-drive-index.csv`. Not owned: Suno, Firefly output, web search results |
| L: drive | Raw media and source video only. Not deliverables |
| N: drive | Google Drive for desktop |
| Loudness target | -14 LUFS integrated, -1 dBTP true peak for YouTube (STANDARDS and qa-media) |
| Fair use disclaimer | Last section of every upload package |
| Rights note | wwd-rights document per title: license status of every asset, risk flags (HIGH, MEDIUM) |
| Cold open | FrostCast cold open (not shipped) is different from the Den Files cold open template |
| Wolfie Awards | The show's recurring awards bit and sticker |
| Teaser, not verdict | Promo copy leads with the hook and never gives the answer |

## Other ventures
| Term | Meaning |
|---|---|
| Studio job | A non-WWD video production, ONE point man agent per project, delivered as a .docx production package |
| Draft 3.3 | Current Ian trailer plan (Zac's new order, wrench hand-off morph) |
| Silent assembly | A cut with no audio, for picture approval |
| Third draft edit cards | Per-chapter docx edit cards for Shattered Empire Book 1, Zac rules every pitch |
| Story Room pass | story-room report on the third draft |
| IRFL | Fantasy football league. Picks and lineup doc layout is locked (Week 10 format) |
| DFS | Daily fantasy (DraftKings). Agents build lineups, never enter or spend |
| Main effort | The single venture Zac names as focus. Currently none |
| ACTIVE / ACTIVE-UNSCHEDULED / DORMANT | Venture status categories in root CLAUDE.md. Only Zac moves a venture between them |
| Project board | `REFERENCE\PROJECT-BOARD.md` |
