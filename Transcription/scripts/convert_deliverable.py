"""Convert the proofread master transcript into the file types the buyer asked for.

  python convert_deliverable.py JOB                      formats from job.json
  python convert_deliverable.py JOB --formats docx,srt   pick formats
  python convert_deliverable.py JOB --clean              no timestamps, same-speaker lines merged
  python convert_deliverable.py JOB --title "Sermon, Nov 9"  --speaker-labels

Reads  <job>\\02-working\\*_master.txt   (lines: [HH:MM:SS] Speaker 1: text)
Writes <job>\\03-final-documents\\<JOBID>_transcript.<ext>   (captions: ..._captions.srt / .vtt)
If 02-working has <name>_segments.json (from run_pipeline.py) the SRT and VTT use its
millisecond start and end times. Otherwise each cue ends where the next line starts.
Formats: docx (python-docx), txt, md, pdf (Edge headless, from HTML), srt, vtt, csv.
No network, nothing installed.
"""
import argparse
import csv
import glob
import html
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjlib as T

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
LINE = re.compile(r"^\[(\d+):(\d{2}):(\d{2})(?:\.(\d{1,3}))?\]\s*(?:([^:\[\]]{1,40}?):\s+)?(.*)$")


def parse_master(path):
    """-> list of dicts: start (sec float), speaker (str or ''), text."""
    segs = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            m = LINE.match(line)
            if m:
                h, mi, s, ms, spk, text = m.groups()
                start = int(h) * 3600 + int(mi) * 60 + int(s) + (int(ms.ljust(3, "0")) / 1000 if ms else 0)
                segs.append({"start": start, "speaker": (spk or "").strip(), "text": text.strip()})
            elif segs:
                segs[-1]["text"] += " " + line.strip()
            else:
                segs.append({"start": 0.0, "speaker": "", "text": line.strip()})
    return segs


def attach_ends(segs, seg_json, audio_end=None):
    """Give each seg an 'end'. Prefer exact times from segments.json."""
    exact = []
    if seg_json and os.path.isfile(seg_json):
        with open(seg_json, encoding="utf-8") as f:
            exact = json.load(f)
    for i, s in enumerate(segs):
        nxt = segs[i + 1]["start"] if i + 1 < len(segs) else None
        match = None
        for e in exact:
            if abs(e["start"] - s["start"]) < 1.0:
                match = e
                break
        if match:
            s["start"], s["end"] = match["start"], match["end"]
        else:
            s["end"] = nxt if nxt is not None else s["start"] + max(2.0, len(s["text"]) / 15.0)
        if s["end"] <= s["start"]:
            s["end"] = s["start"] + 2.0
        if nxt is not None and s["end"] > nxt and not match:
            s["end"] = nxt
    return segs


def ts(sec, sep=","):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def hms(sec):
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def split_text(text, width=42, max_lines=2):
    """Break text into cue chunks of at most max_lines lines of width chars."""
    words = text.split()
    chunks, lines, cur = [], [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
            if len(lines) == max_lines:
                chunks.append(lines)
                lines = []
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    if lines:
        chunks.append(lines)
    return chunks


def make_cues(segs, speaker_labels=False, max_dur=7.0):
    cues = []
    for s in segs:
        chunks = split_text(s["text"])
        if not chunks:
            continue
        total = sum(len(" ".join(c)) for c in chunks) or 1
        t = s["start"]
        dur = s["end"] - s["start"]
        for i, c in enumerate(chunks):
            share = dur * len(" ".join(c)) / total
            lines = list(c)
            if speaker_labels and s["speaker"] and i == 0:
                lines[0] = f"{s['speaker']}: {lines[0]}"
            cues.append((t, t + share, lines))
            t += share
    # long cues: nothing to do beyond the split; cap obviously wrong spans
    return [(a, min(b, a + max(max_dur, 0.1) * 2), l) for a, b, l in cues]


def to_srt(cues):
    return "\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n" + "\n".join(l) + "\n"
                     for i, (a, b, l) in enumerate(cues, 1))


def to_vtt(cues):
    return "WEBVTT\n\n" + "\n".join(f"{ts(a, '.')} --> {ts(b, '.')}\n" + "\n".join(l) + "\n"
                                    for a, b, l in cues)


def blocks(segs, clean):
    """Paragraph blocks: (start, speaker, text). clean merges same-speaker runs."""
    if not clean:
        return [(s["start"], s["speaker"], s["text"]) for s in segs]
    out = []
    for s in segs:
        if out and out[-1][1] == s["speaker"]:
            out[-1] = (out[-1][0], out[-1][1], out[-1][2] + " " + s["text"])
        else:
            out.append((s["start"], s["speaker"], s["text"]))
    return out


def text_lines(bl, clean, with_md=False):
    out = []
    for start, spk, text in bl:
        tag = "" if clean else f"[{hms(start)}] "
        if with_md:
            lab = f"**{spk}:** " if spk else ""
            out.append(f"{tag}{lab}{text}\n")
        else:
            lab = f"{spk}: " if spk else ""
            out.append(f"{tag}{lab}{text}")
    return out


def write_docx(path, bl, clean, title):
    from docx import Document
    from docx.shared import Pt
    d = Document()
    st = d.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(11)
    d.add_heading(title, level=1)
    for start, spk, text in bl:
        p = d.add_paragraph()
        if not clean:
            r = p.add_run(f"[{hms(start)}] ")
            r.font.size = Pt(9)
        if spk:
            p.add_run(f"{spk}: ").bold = True
        p.add_run(text)
        p.paragraph_format.space_after = Pt(6)
    d.save(path)


def write_pdf(path, bl, clean, title):
    if not os.path.isfile(EDGE):
        raise RuntimeError("Edge not found, cannot make PDF")
    body = []
    for start, spk, text in bl:
        tag = "" if clean else f'<span class="t">[{hms(start)}]</span> '
        lab = f"<b>{html.escape(spk)}:</b> " if spk else ""
        body.append(f"<p>{tag}{lab}{html.escape(text)}</p>")
    doc = (f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(title)}</title>"
           "<style>@page{margin:20mm}body{font-family:Calibri,Arial,sans-serif;font-size:11pt;line-height:1.4}"
           "h1{font-size:18pt}.t{color:#666;font-size:9pt}p{margin:0 0 8pt 0}</style></head><body>"
           f"<h1>{html.escape(title)}</h1>" + "\n".join(body) + "</body></html>")
    tmpdir = tempfile.mkdtemp(prefix="tjpdf_", dir=os.path.dirname(path))
    hp = os.path.join(tmpdir, "t.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(doc)
    prof = os.path.join(tmpdir, "prof")
    cmd = [EDGE, "--headless", "--disable-gpu", f"--user-data-dir={prof}", "--no-pdf-header-footer",
           f"--print-to-pdf={path}", "file:///" + hp.replace("\\", "/")]
    try:
        subprocess.run(cmd, check=False, timeout=90, capture_output=True)
    finally:
        import shutil
        shutil.rmtree(tmpdir, ignore_errors=True)
    if not os.path.isfile(path) or os.path.getsize(path) < 500:
        raise RuntimeError("Edge did not produce a PDF")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--formats")
    ap.add_argument("--master")
    ap.add_argument("--clean", action="store_true")
    ap.add_argument("--title")
    ap.add_argument("--name", help="file name stem, default = job ID")
    ap.add_argument("--speaker-labels", action="store_true", help="put speaker names in subtitle cues")
    a = ap.parse_args()

    folder = T.find_job(a.job)
    jid = T.job_id_of(folder)
    meta = T.read_job_json(folder)
    fmts = [x.strip().lower().lstrip(".") for x in (a.formats or ",".join(meta.get("file_types", []))).split(",") if x.strip()]
    if not fmts:
        sys.exit("No formats given and none in job.json. Use --formats docx,txt")
    work = os.path.join(folder, "02-working")
    out_dir = os.path.join(folder, "03-final-documents")
    os.makedirs(out_dir, exist_ok=True)
    master = a.master or next(iter(sorted(glob.glob(os.path.join(work, "*_master.txt")))), None)
    if not master or not os.path.isfile(master):
        sys.exit(f"No *_master.txt found in {work}. Run the pipeline and proofread first.")
    seg_json = next(iter(sorted(glob.glob(os.path.join(work, "*_segments.json")))), None)
    segs = attach_ends(parse_master(master), seg_json)
    if not segs:
        sys.exit("Master transcript is empty.")
    stem = a.name or jid
    title = a.title or "Transcript"
    bl = blocks(segs, a.clean)
    cues = make_cues(segs, a.speaker_labels)
    made, failed = [], []
    for fmt in fmts:
        try:
            if fmt in ("srt", "vtt"):
                p = os.path.join(out_dir, f"{stem}_captions.{fmt}")
                with open(p, "w", encoding="utf-8") as f:
                    f.write(to_srt(cues) if fmt == "srt" else to_vtt(cues))
            else:
                p = os.path.join(out_dir, f"{stem}_transcript.{fmt}")
                if fmt == "txt":
                    with open(p, "w", encoding="utf-8") as f:
                        f.write("\n\n".join(text_lines(bl, a.clean)) + "\n")
                elif fmt == "md":
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(f"# {title}\n\n" + "\n".join(text_lines(bl, a.clean, True)))
                elif fmt == "docx":
                    write_docx(p, bl, a.clean, title)
                elif fmt == "pdf":
                    write_pdf(p, bl, a.clean, title)
                elif fmt == "csv":
                    with open(p, "w", encoding="utf-8-sig", newline="") as f:
                        w = csv.writer(f)
                        w.writerow(["start", "end", "speaker", "text"])
                        for s in segs:
                            w.writerow([ts(s["start"], "."), ts(s["end"], "."), s["speaker"], s["text"]])
                else:
                    raise ValueError(f"unsupported format {fmt}")
            made.append(p)
        except Exception as e:  # report and keep going with the other formats
            failed.append((fmt, str(e)))
    for p in made:
        print(f"  wrote {os.path.basename(p)}  ({os.path.getsize(p)} bytes)")
    for fmt, why in failed:
        print(f"  FAILED {fmt}: {why}")
    T.append_to_notes(folder, f"- {T.today()}  converted: {', '.join(os.path.basename(p) for p in made)}",
                      T.ISSUE_MARK)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
