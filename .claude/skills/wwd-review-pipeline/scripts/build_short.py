# -*- coding: utf-8 -*-
"""WWD shorts builder. Local Windows ffmpeg, stdlib only.

Subcommands
  analyze  --src FINAL.mp4 --out silence.json
      Mono 16k analysis audio + silencedetect (-32dB, 0.28s). Run once per review.
  snap     --silence silence.json --start T --end T
      Prints the snapped in/out points (seconds) for an approximate window.
  render   --spec clip.json
      Builds one finished clip: blurred-fill frame, burned-in captions, timed hook
      text, film tag, cover PNG, one-frame cover prepend, loudness-normalised audio,
      then runs QC (ffprobe, head silence, three frames written for eyeballing).

Spec keys for render: src, outdir, slug, film, start, end, hook, text, silence,
cover_at (optional, seconds into the clip), n (optional clip number).
Never hardcode paths: the caller reads them from LOCAL-PATHS.md.
"""
import argparse, json, os, re, shutil, subprocess, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(SKILL, "assets", "fonts")
SIL_DB, SIL_D = "-32dB", "0.28"

def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit("FAILED: " + " ".join(cmd[:6]) + "\n" + r.stderr[-1500:])
    return r.stderr + r.stdout

def probe_duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", path])
    return float(out.strip().splitlines()[0])

def silences(mp3):
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp3, "-af", f"silencedetect=noise={SIL_DB}:d={SIL_D}",
                          "-f", "null", "-"], capture_output=True, text=True, errors="replace").stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    return list(zip(starts, ends[:len(starts)]))

def cmd_analyze(a):
    tmp = os.path.splitext(a.out)[0] + "_analysis.mp3"
    run(["ffmpeg", "-y", "-i", a.src, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "48k", tmp])
    gaps = silences(tmp)
    json.dump({"src": a.src, "duration": probe_duration(a.src), "gaps": gaps}, open(a.out, "w"))
    print(f"{len(gaps)} silence gaps mapped -> {a.out}")

def cmd_snap(a):
    gaps = json.load(open(a.silence))["gaps"]
    s = min((g for g in gaps if abs(g[1] - a.start) < 3), key=lambda g: abs(g[1] - a.start), default=None)
    e = min((g for g in gaps if abs(g[0] - a.end) < 3), key=lambda g: abs(g[0] - a.end), default=None)
    print("in :", round(s[1] - 0.06, 2) if s else "NO GAP within 3s, widen the window")
    print("out:", round(e[0] + 0.35, 2) if e else "NO GAP within 3s, widen the window")

def ass_time(t):
    t = max(t, 0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"

def speech_spans(gaps, start, end):
    spans, cur = [], start
    for gs, ge in gaps:
        if ge <= start or gs >= end:
            continue
        if gs - cur > 0.12:
            spans.append((cur, min(gs, end)))
        cur = max(cur, ge)
    if end - cur > 0.12:
        spans.append((cur, end))
    return spans

def caption_events(text, spans, start):
    words = text.split()
    total_chars = sum(len(w) for w in words) or 1
    total_time = sum(b - a for a, b in spans) or 1
    timed, wi, used = [], 0, 0.0
    for a, b in spans:
        budget = (b - a) / total_time * total_chars
        taken, chunk = 0.0, []
        while wi < len(words) and (taken < budget or not chunk) and (taken + len(words[wi]) / 2 <= budget or not chunk):
            chunk.append(words[wi]); taken += len(words[wi]); wi += 1
        if not chunk:
            continue
        t = a
        for w in chunk:
            dur = (b - a) * len(w) / max(sum(len(x) for x in chunk), 1)
            timed.append((w, t, t + dur, (a, b))); t += dur
    while wi < len(words):  # leftovers go on the last span
        a, b = spans[-1]; timed.append((words[wi], b - 0.3, b, (a, b))); wi += 1
    lines, cur = [], []
    for w in timed:
        if cur and (len(cur) >= 4 or sum(len(x[0]) for x in cur) + len(w[0]) > 22 or cur[0][3] != w[3]):
            lines.append(cur); cur = []
        cur.append(w)
    if cur:
        lines.append(cur)
    out = []
    for i, ln in enumerate(lines):
        t0, t1 = ln[0][1] - start, ln[-1][2] - start
        if i + 1 < len(lines) and 0 < lines[i + 1][0][1] - ln[-1][2] < 0.25:
            t1 = lines[i + 1][0][1] - start
        out.append((t0, t1, " ".join(w[0] for w in ln).upper()))
    return out

FILLERS = {"um", "uh", "ah", "er", "hmm", "uhh", "umm"}
STUTTER_OK = {"the", "a", "i", "your", "my", "we", "to", "it's", "that's", "in", "of", "and", "like", "so", "but"}

def bare(t):
    return re.sub(r"[^\w']", "", t).lower()

def caption_from_words(words, start, end, fixes=None, head_pad=0.05, drop_tail=0, drop_phrases=None,
                       prepend_text=None):
    """Word-level captions from word_times.py output.
    fixes: {"wrong": "right"} for single-word garbles. drop_phrases: ["words to remove"] for
    audio that is unclear (publish none of it). head_pad: seconds before start to still accept
    words (Whisper times run early). drop_tail: ASR words past the real out-point to discard."""
    fixes = {k.lower(): v for k, v in (fixes or {}).items()}
    ws = [w for w in words if w["s"] >= start - head_pad and w["s"] < end]
    if drop_tail:
        ws = ws[:-drop_tail]
    for ph in (drop_phrases or []):
        seq = [bare(x) for x in ph.split()]
        i = 0
        while i <= len(ws) - len(seq):
            if [bare(w["w"]) for w in ws[i:i + len(seq)]] == seq:
                del ws[i:i + len(seq)]
            else:
                i += 1
    toks = []
    if prepend_text:  # a spoken word the ASR missed, confirmed by listening to the isolated slice
        toks.append((prepend_text, start + 0.05, start + 0.3))
    for w in ws:
        txt = w["w"].strip()
        if bare(txt) in FILLERS:
            continue
        txt = fixes.get(bare(txt), txt)
        if txt.startswith("-") and toks:  # Whisper splits hyphenated words (step -up)
            prev = toks.pop()
            toks.append((prev[0] + txt, prev[1], max(w["e"], prev[2])))
            continue
        txt = re.sub(r"[,.;:!?]+$", "", txt)
        if not txt:
            continue
        if toks and bare(toks[-1][0]) == bare(txt) and bare(txt) in STUTTER_OK:
            continue
        toks.append((txt, max(w["s"], start), min(w["e"], end)))
    lines, cur = [], []
    for t in toks:
        if cur and (len(cur) >= 4 or sum(len(x[0]) for x in cur) + len(t[0]) > 22 or t[1] - cur[-1][2] > 0.6):
            lines.append(cur); cur = []
        cur.append(t)
    if cur:
        lines.append(cur)
    out = []
    for i, ln in enumerate(lines):
        t0, t1 = ln[0][1] - start, ln[-1][2] - start
        if i + 1 < len(lines) and 0 < lines[i + 1][0][1] - ln[-1][2] < 0.3:
            t1 = lines[i + 1][0][1] - start
        out.append((t0, max(t1, t0 + 0.3), " ".join(x[0] for x in ln).upper()))
    return out

def wrap_hook(h, max_width=24):
    """Balanced wrap: fewest lines that fit, broken near equal length (no orphan words)."""
    words = h.upper().split()
    total = len(" ".join(words))
    n = max(1, -(-total // max_width))
    target = total / n
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > target + 2 and len(lines) < n - 1:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    return r"\N".join(lines + [cur])

def write_ass(path, spec, caps, cover=False):
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n"
            "[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,"
            "Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
            "Style: Cap,Poppins,74,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,6,0,2,60,60,400,1\n"
            "Style: Hook,Poppins,86,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,8,0,8,50,50,170,1\n"
            "Style: Tag,Poppins SemiBold,38,&H0000C8FF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,4,0,1,4,0,8,60,60,590,1\n"
            "\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")
    ev = []
    hook_end = 99 if cover else 3.6
    fade = "" if cover else "{\\fad(120,200)}"
    ev.append(f"Dialogue: 1,{ass_time(0)},{ass_time(hook_end)},Hook,,0,0,0,,{fade}{wrap_hook(spec['hook'])}")
    ev.append(f"Dialogue: 0,{ass_time(0)},{ass_time(99)},Tag,,0,0,0,,{spec['film'].upper()}  |  REVIEW")
    if not cover:
        for t0, t1, txt in caps:
            ev.append(f"Dialogue: 0,{ass_time(t0)},{ass_time(t1)},Cap,,0,0,0,,{txt}")
    open(path, "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")

BLUR = ("[0:v]split=2[bg][fg];[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        "boxblur=24:6,eq=brightness=-0.06[bgb];[fg]scale=1080:608[fgs];[bgb][fgs]overlay=(W-w)/2:656,setsar=1[base];"
        "[base]subtitles={ass}:fontsdir=fonts[v]")

def cmd_render(a):
    spec = json.load(open(a.spec, encoding="utf-8-sig"))
    n, slug = spec.get("n", 1), spec["slug"]
    out_name = f"clip{n}_{slug}"
    work = os.path.join(os.environ.get("WKP_SCRATCH", r"D:\WKP\scratch"), "shorts_" + out_name)
    os.makedirs(work, exist_ok=True)
    shutil.copytree(FONTS, os.path.join(work, "fonts"), dirs_exist_ok=True)
    src = spec["src"]; s, e = float(spec["start"]), float(spec["end"])
    gaps = json.load(open(spec["silence"], encoding="utf-8-sig"))["gaps"]
    if spec.get("words"):
        words = json.load(open(spec["words"], encoding="utf-8-sig"))
        caps = caption_from_words(words, s, e, spec.get("fixes"), spec.get("head_pad", 0.05),
                                  spec.get("drop_tail", 0), spec.get("drop_phrases"),
                                  spec.get("prepend_text"))
    else:
        caps = caption_events(spec["text"], speech_spans(gaps, s, e), s)
    print("CAPTIONS:", " / ".join(c[2] for c in caps))
    write_ass(os.path.join(work, "clip.ass"), spec, caps)
    write_ass(os.path.join(work, "cover.ass"), spec, [], cover=True)
    # stage 1 body
    run(["ffmpeg", "-y", "-ss", str(s), "-to", str(e), "-i", src, "-filter_complex", BLUR.format(ass="clip.ass"),
         "-map", "[v]", "-map", "0:a", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
         "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "body.mp4"], cwd=work)
    # cover png: strongest frame from inside the clip, same layout, big hook
    at = s + float(spec.get("cover_at", 6.0))
    run(["ffmpeg", "-y", "-ss", str(at), "-i", src, "-frames:v", "1", "-filter_complex",
         BLUR.format(ass="cover.ass"), "-map", "[v]", "-q:v", "2", "cover.png"], cwd=work)
    # stage 2 one-frame cover clip, params identical to the body
    run(["ffmpeg", "-y", "-loop", "1", "-framerate", "30", "-i", "cover.png", "-f", "lavfi", "-i",
         "anullsrc=channel_layout=stereo:sample_rate=48000", "-frames:v", "1", "-t", "0.0334",
         "-vf", "scale=1080:1920,setsar=1,format=yuv420p", "-c:v", "libx264", "-crf", "19", "-preset", "veryfast",
         "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "cov.mp4"], cwd=work)
    # stage 3 concat
    open(os.path.join(work, "cc.txt"), "w").write("file 'cov.mp4'\nfile 'body.mp4'\n")
    os.makedirs(spec["outdir"], exist_ok=True)
    final = os.path.join(spec["outdir"], out_name + ".mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "cc.txt", "-c", "copy", final], cwd=work)
    shutil.copy(os.path.join(work, "cover.png"), os.path.join(spec["outdir"], out_name + "_cover.png"))
    qc(final, work)

def qc(final, work):
    dur = probe_duration(final)
    info = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                "-of", "csv=p=0", final]).strip()
    has_audio = bool(run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=codec_name",
                          "-of", "csv=p=0", final]).strip())
    head = subprocess.run(["ffmpeg", "-hide_banner", "-i", final, "-t", "1.2", "-af",
                           "silencedetect=noise=-38dB:d=0.05", "-f", "null", "-"],
                          capture_output=True, text=True, errors="replace").stderr
    m = re.search(r"silence_end: ([\d.]+)", head)
    head_sil = float(m.group(1)) if m else 0.0
    for i, t in enumerate([1.0, dur / 2, max(dur - 2, 0)]):
        run(["ffmpeg", "-y", "-ss", str(t), "-i", final, "-frames:v", "1", "-q:v", "3", f"qc_{i + 1}.png"], cwd=work)
    ok_len = 20 <= dur <= 75
    print(json.dumps({"file": final, "size": info, "duration": round(dur, 2), "audio": has_audio,
                      "head_silence_s": round(head_sil, 2), "length_ok_20_75": ok_len,
                      "eyeball_frames": [os.path.join(work, f"qc_{i}.png") for i in (1, 2, 3)]}, indent=2))
    if info != "1080,1920" or not has_audio:
        sys.exit("QC FAIL: wrong size or no audio")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="c", required=True)
    x = sub.add_parser("analyze"); x.add_argument("--src", required=True); x.add_argument("--out", required=True)
    x = sub.add_parser("snap"); x.add_argument("--silence", required=True)
    x.add_argument("--start", type=float, required=True); x.add_argument("--end", type=float, required=True)
    x = sub.add_parser("render"); x.add_argument("--spec", required=True)
    a = p.parse_args()
    {"analyze": cmd_analyze, "snap": cmd_snap, "render": cmd_render}[a.c](a)
