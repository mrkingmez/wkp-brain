# Tool-gap audit: agent spec tool lists vs what each job needs

Created 2026-11-26 by chief-of-staff (Zac 2026-11-26, after wwd-pictures ran with no claude-in-chrome tool, `logs\agent-runs.md` 2026-11-26 row). Method: read the `tools:` line of every spec in `D:\WKP\.claude\agents\` (63 files) and compared to the job text in the spec, the skill it calls, and the lessons files. Authority: chief-of-staff does not edit agent specs, so every fix below is QUEUED (`logs\DECISIONS.md` TOOLS-2026-11-26-01). Nothing here was changed in a spec.

Spec reading rule used: a spec with NO `tools:` line inherits the session's tools (seven specs: copywriting, fantasy-football-director, graphic-design, market-research, marketing-director, social-media, video-ugc). Whether a subagent actually receives MCP tools such as claude-in-chrome depends on the launching session: NOT VERIFIED by me (I have no browser tool in this run either). Tool names for the browser come from `.claude\skills\wwd-review-photo-pull\SKILL.md` lines 37 to 39 (`mcp__claude-in-chrome__*`: navigate, javascript_tool, find, read_page, browser_batch); exact frontmatter spelling is NOT VERIFIED.

## Confirmed gaps (evidence on disk)
| # | Agent | Gap | Evidence | Proposed fix | Risk |
|---|---|---|---|---|---|
| 1 | wwd-pictures | No browser tool. Its own skill says it needs `mcp__claude-in-chrome__*` for IMDb per-actor and per-character galleries, TMDb and TV Insider. Spec tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch | SKILL.md L37 to L39; wwd-pictures lesson 2026-11-26 and `logs\agent-runs.md` 2026-11-26 (IMDb and TV Insider never tried, `list_connected_browsers` never run); Initial-Pull-Report blocked items list IMDb, TMDb API, Fandom, TV Insider | Add the claude-in-chrome tools to the `tools:` line, or drop the line so it inherits. Add a Step 0 to the spec: state at once whether the browser is callable, run `list_connected_browsers`, report NOT RUN for what could not happen | Low. Read-only browsing. Facebook is not in scope for this agent |
| 2 | script-room, room-writer, dialogue-doctor, clearance, originality, devils-advocate | No Bash. Root CLAUDE.md slop gate says any agent that writes or reviews public copy runs `slop_check.py` from Bash. script-room writes every word for every department | `tools:` lines read 2026-11-26; script-room drill criterion 6 needed the grader to re-run slop_check | Add Bash to script-room and room-writer (they write copy). Leave devils-advocate and dialogue-doctor Bash-less if Jarvis prefers, and keep the rule that the director or Jarvis runs slop_check for them | Low |
| 3 | clearance, originality | WebSearch only, no WebFetch. Clearance and originality checks need the page text (the script-room result says clearance was not checked against a film transcript for L12, L24, L82) | script-room drill result 2026-11-22, criterion 4 | Add WebFetch to both | Low |
| 4 | wwd-clip-scout | Spec L20 says it downloads nothing itself, but its 2026-11-23 lesson uses yt-dlp for the official caption file, and clip stock is converted from files Zac downloads | wwd-clip-scout.md L20; lessons file 2026-11-23 | Rule clarification, not a tool change: allow caption-only `yt-dlp --skip-download` and keep video downloads with Zac. Needs Jarvis | Low |
| 5 | 33 specs with no WebFetch (list below) | Leveling Step 1 (Craft Brief) requires retrieving primary pages. These agents cannot do it alone | `tools:` lines | Do not add WebFetch to all. Run Step 1 through a general-purpose agent running the spec (the launch files already allow it), and add WebFetch only where the agent's real jobs need it (assistant-editor and qa-media for loudness and Premiere pages are the likeliest) | Low |

No-WebFetch list: animation-director, assistant-editor, blender-builder-characters, blender-builder-props, chief-of-staff, clearance, devils-advocate, dialogue-doctor, etsy-director, fiction-director, kdp-director, last30days-researcher, media-manager, military-scifi-director, motion-graphics, originality, paws-director, qa-auditor, qa-director, qa-documents, qa-media, room-writer, script-room, shattered-empire-director, software-director, software-engineer, software-tester, studio-director, ue-asset-integrator, ue-scene-builder, vfx-compositor, wkp-channel-director, wwd-director.

## Checked and consistent (no gap found)
- wwd-director: no browser by design (spec L72 to L76: Messenger send to Matt goes under Flags and the main session sends it). Dependency to keep: Jarvis must hold the Chrome step. Not a gap.
- wwd-vfx: no browser and no credit-spending tool by design (spec L127).
- qa-media: Read, Write, Glob, Grep, Bash, no Edit, correct for a report-only bench. Needs ffprobe and ffmpeg through Bash.
- media-manager, wwd-run-sheet, wwd-sound, wwd-rights: tools match jobs (Bash for ffmpeg, python and the lint; WebFetch for licence pages where they have it). media-manager has no web, and needs none.
- The seven specs with no tools line: inherit, nothing to fix.

## Not verified
- Whether claude-in-chrome is delivered to a spawned subagent at all (it was absent in the wwd-pictures run per its own report, the cause is not known: spec list or session). Test: launch wwd-pictures once after the spec change and have it call `list_connected_browsers`, cost $0.
- ElevenLabs and Higgsfield MCP tools: not in any spec by design (credits).
