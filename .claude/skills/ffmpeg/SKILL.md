---
name: ffmpeg
description: Tested ffmpeg and ffprobe recipes for what WKP actually does - cut, concat, contain-fit to 1080p or 1080x1920 with blurred sides (never crop), burned-in captions with drawtext, zoompan stills, audio extract, loudnorm measure, contact sheets and frame grabs, Premiere-safe H.264 re-encode. Use whenever an agent must cut, convert, caption, measure or inspect video or audio from the command line. Includes the Windows gotchas that hang or break runs.
---

# ffmpeg for WKP

ffmpeg: `C:\Users\kingz\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe` (also on PATH; ffprobe is in the same folder). Path comes from `D:\WKP\LOCAL-PATHS.md`, read it, do not hardcode elsewhere. Scratch work goes to `D:\WKP\scratch\`. Never overwrite a source file: write to a new name. Always pass `-y -loglevel error` in scripts and `-hide_banner` when you want to read a report.

Working code that uses these patterns: `D:\WKP\scratch\ian\build_rough.py` (Ian trailer rough cut). Also used inside wwd-video-transcriber, wwd-review-pipeline, remotion-motion-graphics, wkp-system-check, and by qa-media.

## Gotchas (learned the hard way)

1. **An endless source needs a duration.** `-f lavfi color=...`, `testsrc`, `sine`, and `-loop 1` on a still never end. Put `-t <seconds>` on the output (and before `-i` for a looped still, as in `-loop 1 -t 3 -i still.png`). Without it ffmpeg runs until killed. Verified: a bare `color` source hung until a 6 s timeout killed it.
2. **Windows font path in drawtext.** Use forward slashes and escape the colon: `fontfile='C\\:/Windows/Fonts/georgia.ttf'`. In Python source write `C\\\\:/Windows/Fonts/georgia.ttf` or use a raw string. Bold: `georgiab.ttf`. A bare `C:\Windows\...` breaks the filter parser.
3. **Quote the filter, not the shell.** In bash wrap the whole `-vf` in double quotes with single quotes inside. In PowerShell prefer a Python or `.cmd` script for long filter graphs.
4. **Contain, never crop** (locked rule, `memory\topics\visual-media.md`). Scale with `force_original_aspect_ratio=decrease`, pad or overlay. The blurred-sides recipe below is the vertical version.
5. **`-c copy` cuts only on keyframes.** For exact cuts re-encode. Put `-ss` before `-i` for speed, then re-encode, and check the result's duration.
6. **Concat demuxer needs identical codec, size, fps and timebase** across files. Different sizes: re-encode through a filter chain first.
7. Add `-pix_fmt yuv420p` (or `format=yuv420p`) to anything going to Premiere, phones or Facebook, or it may play black or fail.
8. Never read a loudness, duration or resolution off memory: use ffprobe and report only what it returns.

## Inspect

```
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration -show_entries format=duration -of default=nw=1 file.mp4
```

## Recipes (A, B, C, D, E and concat were run on 2026-11-17 against a generated 5 s 1280x720 test clip in `D:\WKP\scratch\ffmpeg-test\`; the others are standard and NOT run in that test)

**A. 16:9 to 1080x1920 with blurred sides (tested, output verified 1080x1920 h264)**
```
ffmpeg -y -loglevel error -i in.mp4 -filter_complex "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5[bg];[b]scale=1080:1920:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p" -c:v libx264 -crf 18 -r 24 -c:a copy out_vert.mp4
```
(The crop is on the blurred background only, never on the picture.)

**B. Contain to 1920x1080 with transparent-look black bars (not run)**
```
ffmpeg -y -loglevel error -i in.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p" -c:v libx264 -crf 18 -c:a copy out_1080.mp4
```

**C. Burned-in caption with timing (tested)**
```
ffmpeg -y -loglevel error -i in.mp4 -vf "drawtext=fontfile='C\\:/Windows/Fonts/georgia.ttf':text='YOUR TEXT':fontcolor=white:fontsize=64:borderw=3:bordercolor=black@0.8:x=(w-text_w)/2:y=h*0.8:enable='between(t,0.5,4)'" -c:v libx264 -crf 18 -c:a copy out_cap.mp4
```
Apostrophes in text: write `\\'` or avoid. Captions shown to viewers come from the writing room, then slop_check.

**D. Loudness measure (tested; read `input_i` LUFS and `input_tp` true peak)**
```
ffmpeg -hide_banner -i in.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -
```
Test clip read -21.81 LUFS and -16.08 dBTP. WWD uses -24.7 LUFS reference noted in TASKS.md; confirm the target with wwd-sound before normalizing.

**E. Zoom-in on a still (tested; duration verified 3.0 s)**
```
ffmpeg -y -loglevel error -loop 1 -t 3 -i still.png -filter_complex "[0:v]scale=3200:-2,zoompan=z='1+0.1*on/72':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1280x720:fps=24,format=yuv420p" -t 3 -c:v libx264 -crf 18 zoom.mp4
```
Zoom step is `end_zoom_gain*on/total_frames` (3 s at 24 fps is 72). Scale the still up first or the zoom looks soft.

**F. Contact sheet, one frame per second, 5 across (tested)**
```
ffmpeg -y -loglevel error -i in.mp4 -vf "fps=1/1,scale=320:-2,tile=5x1" -frames:v 1 sheet.png
```
Change `fps=1/3` and `tile=4x3` for a long clip. Resize screenshots to about 1,000 px wide before an agent views them (limit rule L19).

**G. Concat with `-c copy` (tested, same-spec files)**
```
printf "file 'a.mp4'\nfile 'b.mp4'\n" > list.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -c copy out.mp4
```

**H. Cut without re-encoding (keyframe-accurate only) (not run)**
```
ffmpeg -y -ss 00:01:05 -to 00:01:20 -i in.mp4 -c copy cut.mp4
```
**Exact cut (re-encode) (not run)**
```
ffmpeg -y -ss 65 -t 15 -i in.mp4 -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k cut.mp4
```

**I. Extract audio (not run)**
```
ffmpeg -y -i in.mp4 -vn -c:a libmp3lame -q:a 2 out.mp3
ffmpeg -y -i in.mp4 -vn -ac 1 -ar 16000 out.wav
```
(second line is the transcription-friendly form.)

**J. Frame grab (not run)**
```
ffmpeg -y -ss 12.5 -i in.mp4 -frames:v 1 frame.png
```

**K. Premiere-safe H.264 re-encode (not run)**
```
ffmpeg -y -i in.* -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -movflags +faststart out.mp4
```
Match `-r` to the project frame rate. Variable-frame-rate phone clips: always set `-r`.

**L. Normalize to a target loudness after measuring (not run)**
Run recipe D, then pass the measured values to a second loudnorm pass (`measured_I=`, `measured_TP=`, `measured_LRA=`, `measured_thresh=`), or use single-pass `-af loudnorm=I=-16:TP=-1.5:LRA=11` for a quick job.

## Check your own output

After every run: ffprobe the result (duration, size, audio stream present), grab a frame or contact sheet and look at it, and say in your report which of these you did. Never say "done" on a file you did not probe.
