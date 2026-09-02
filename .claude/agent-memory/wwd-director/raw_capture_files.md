---
name: raw-capture-files
description: WWD raw video captures (.m4v) can be bare elementary h264 streams with no container/audio; wait for the real Premiere export instead of fighting them
metadata:
  type: project
---

Raw Footage folders (e.g. `Raw Footage\<Movie>\<name>.m4v` +
`<name>.aac`) are not always finished containers. Confirmed on Good Boy
(2025) 2026-08-31: the `.m4v` was a bare elementary h264 stream (`ffmpeg -i`
reported `Input #0, h264`, no container, no timestamps, no audio track at
all) with audio captured separately as a raw `.aac`. ffmpeg/ffprobe seeking
into the raw `.m4v` with `-ss`/`-t` silently produced empty output rather
than an error — the tell is `duration=N/A` from ffprobe and "Output file is
empty, nothing was encoded" from ffmpeg.

Also hit the same day: ffmpeg/ffprobe returned "Permission Denied" on the
`.m4v` even though a plain .NET `File.Open` succeeded — turned out Premiere/
Media Encoder was actively exporting the finished video into that same
folder at that exact moment (a growing `<name>.mp4` plus a `._00_` temp
file). The `.aac` disappeared mid-session as that export consumed it.

**Why:** Zac's capture rig apparently records video and audio as separate
raw tracks that only get muxed into a real deliverable when Premiere
finishes its export. A director session landing mid-export will see
confusing, transient file states (locked file, vanishing audio, a raw
video-only stream) that look like real blockers but resolve on their own
once the export finishes.

**How to apply:** If a source `.m4v`/`.aac` pair in a Raw Footage folder
won't open cleanly (Permission Denied, `duration=N/A`, or ffmpeg reports it
as a bare `h264` stream with no audio), check the folder for a sibling
`.mp4` and a `._00_`-style temp file before concluding the source is
broken. If one is present, poll the `.mp4`'s file size (e.g. every 15s)
until it stops growing and the temp file disappears, then use that
finished export as the cut source instead. Do this with a PowerShell
script written to a `.ps1` file and run via
`powershell -File <script>.ps1` — see [[bash-quoting]] for why inline
`-Command` strings with `$` variables break through this Bash tool.
Once cutting works, apply a small safety pad (2s was used here) on clip
in/out points if the raw capture's total duration and the final export's
duration don't match exactly — small trims during final edit are normal
and can shift a transcript-derived timecode by a few seconds.
