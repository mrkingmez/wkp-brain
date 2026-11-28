# Lessons: motion-graphics

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\motion-graphics.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Spend no credits: Veo and Firefly credits are at zero, work from what is on disk | evidence: memory\project-ian-trailer-settled.md | NEW
- 2026-11-19 | Nobody can hear audio: say 'not heard' for every sound claim | evidence: agent-runs.md rows 2026-11-17 and 2026-11-18 | NEW

## Lessons
- 2026-11-25 | Never edit a source with CRLF-unsafe heredoc patches: use the Edit tool for TSX changes, and check the file after a python replace (two stray quote marks shipped in a draft render) | evidence: end-15s v1 render | NEW
- 2026-11-25 | When Zac says use a client picture as is, contain-fit it whole and expect the picture itself to carry extra text (Ian banner has QR, handles, email): flag it in the report | evidence: Ian-Trailer-End-15s v2 frame 14.9 s | NEW
- 2026-11-25 | A relayed Zac yes comes via the coordinator: build to it but write it in the notes as relayed, and keep layers as props so they can switch off | evidence: showBadge prop in End15.tsx | NEW
- 2026-11-25 | A vertical tear at screen center cuts through the subject's face: check the real still and set tear-x to split subjects, and say so in the report | evidence: W1a frames 30 to 39 | NEW
- 2026-11-25 | Heredocs with apostrophes in a path broke the Bash tool: write code files with the Write tool | evidence: first rip.py attempt | NEW
- 2026-11-25 | A "rip" means what a person pictures: read the physical action first (vertical center tear, crack zips top to bottom, halves hinge on outer edges and exit sideways), test every frame for slivers, never let halves fall off the bottom | evidence: Zac "really bad" on W1 rip v1, v2-center rebuilt | CONFIRMED
- 2026-11-25 | Batch files that render named versions must auto-pick the next free version, and never reuse a taken vN | evidence: render_real.bat v2 collision | NEW
- 2026-11-25 | For a physical act (paper tear) a 2D slide reads fake: model it as a connected 3D mesh (per-row hinge angle that ramps from 0 at the crack tip, curl along the width, perspective, normal-based shading) and keep a V gap that closes at the bottom until the snap | evidence: rip_paper_v3.py, v3 frames 38 to 50 vs v2 | NEW
- 2026-11-25 | When a state function has several time stages, write each boundary from one named constant: my tear/snap boundaries used tp 0.97 instead of 0.77 and froze the tear 0.2 s until I viewed the frames | evidence: v3 first render f46 to f51 identical | NEW
- 2026-11-25 | Shutter blur needs 20 or more sub-samples over a 0.6 frame shutter; 6 samples over a full frame showed ghost copies | evidence: v3 first render f54 to f57 | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
