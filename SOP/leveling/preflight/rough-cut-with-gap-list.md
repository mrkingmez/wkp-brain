# Pre-flight: Rough cut with gap list (non-WWD, e.g. Ian trailer)

Created 2026-11-22.

1. [ ] Every shot accounted for: HAVE, WEAK or NEED, with source path checked by ffprobe (duration, resolution, fps, audio present). No path guessed.
2. [ ] Total runtime against target. Two numbers when short: the floor (HAVE only) and the cheapest path to target, each with arithmetic a second person re-adds (lesson 2026-11-21).
3. [ ] Render spec by ffprobe: size, fps, frame count (`-count_frames`) equals seconds times fps (for example 1080 at 24 fps for 45 s).
4. [ ] Contain and fit, never crop (S1 scale force_original_aspect_ratio). Fills for non-matching aspect are symmetric or centered on the subject, checked on a frame pull of every still that is not 16:9.
5. [ ] Frames pulled at every cut and at 0.4 s steps over any moving crop. The sheet path is named. Anything not viewed says "not viewed".
6. [ ] Black tail: blackdetect on the last 20 s, tail 1 s or less. If sound exists, ebur128 integrated LUFS and true peak with the lock named (Zac's lock -14 LUFS, EBU R 128 -1 dBTP, S2).
7. [ ] Music and sound: owned or confirmed license stated per file. Unknown license named and routed to music. Nobody heard it: say so.
8. [ ] No credits, no money. Any generation need is named with exact cost or "NOT RETRIEVED", queued for Zac.
9. [ ] AI-generated shots labeled as such. Spoiler fence and any locked project memo re-read (Ian: memory\project-ian-trailer-secret.md).
10. [ ] Previous version kept, new file vN+1, one change at a time.
11. [ ] Head-editor notes requested, creative calls listed with both options and a pick.
12. [ ] Zero em dashes. Ledger row and lesson written.
