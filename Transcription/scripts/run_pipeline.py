"""Run the local transcription pipeline on a job's audio. No network, nothing leaves the machine.

  python run_pipeline.py JOB                    one speaker (sermon, captions): fast timed run
  python run_pipeline.py JOB --speakers 2       diarized run through the WWD transcribe.py
  python run_pipeline.py JOB --speakers 2 --also-timed   plus millisecond times for subtitles
  python run_pipeline.py JOB --file name.mp3 --model small

Reads  <job>\\01-raw-audio\\<first audio or video file>
Writes <job>\\02-working\\<stem>.wav, <stem>_draft_raw.txt (never edit), <stem>_master.txt (proofread this),
       <stem>_segments.json (exact times, used for subtitle files)
Speaker labels are generic: Speaker 1, Speaker 2. Client audio is NEVER matched against
D:\\WKP\\voiceprints (that would label a client as Zac, Matt or Gabby): the diarized run is pointed at an
empty folder and the output is checked for host names. Machine time goes on the job clock.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjlib as T
import job_clock

MEDIA = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg", ".opus", ".wma", ".mp4", ".mov", ".mkv",
         ".webm", ".avi", ".m4v"}
TRANSCRIBE = r"D:\WKP\.claude\skills\wwd-video-transcriber\scripts\transcribe.py"
EMPTY_VP = os.path.join(T.JOBS_ROOT, "_no-voiceprints")
HOSTS = re.compile(r"\b(Matt|Winter Wolf|Zac|KingZ|Gabby|Oracle)\b")


def hms(sec):
    sec = int(sec)
    return f"[{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}]"


def user_env_token():
    if os.environ.get("HF_TOKEN"):
        return os.environ["HF_TOKEN"]
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            return winreg.QueryValueEx(k, "HF_TOKEN")[0]
    except Exception:
        return None


def extract_wav(src, wav):
    cmd = ["ffmpeg", "-y", "-i", src, "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", wav]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("ffmpeg failed:\n" + r.stderr[-800:])


def timed_run(wav, model_name, language):
    from faster_whisper import WhisperModel
    try:
        model = WhisperModel(model_name, device="cuda", compute_type="float16")
        segs, info = model.transcribe(wav, language=language, vad_filter=True, beam_size=5)
        segs = list(segs)
        device = "cuda"
    except Exception as e:  # GPU or cuDNN trouble: fall back to CPU, say so
        print(f"GPU run failed ({str(e)[:120]}). Falling back to CPU, slower.")
        model = WhisperModel(model_name, device="cpu", compute_type="int8")
        segs, info = model.transcribe(wav, language=language, vad_filter=True, beam_size=5)
        segs = list(segs)
        device = "cpu"
    out = [{"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()} for s in segs]
    return out, info.language, device


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--speakers", type=int, default=1)
    ap.add_argument("--file")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--language", default="en")
    ap.add_argument("--also-timed", action="store_true")
    a = ap.parse_args()

    folder = T.find_job(a.job)
    raw_dir, work = os.path.join(folder, "01-raw-audio"), os.path.join(folder, "02-working")
    os.makedirs(work, exist_ok=True)
    if a.file:
        src = a.file if os.path.isabs(a.file) else os.path.join(raw_dir, a.file)
    else:
        found = sorted(f for f in os.listdir(raw_dir) if os.path.splitext(f)[1].lower() in MEDIA)
        if not found:
            sys.exit(f"No audio or video file in {raw_dir}. Zac downloads the buyer's file there first.")
        src = os.path.join(raw_dir, found[0])
    if not os.path.isfile(src):
        sys.exit(f"File not found: {src}")
    stem = os.path.splitext(os.path.basename(src))[0]
    wav = os.path.join(work, stem + ".wav")
    t0 = time.time()
    print(f"Job {T.job_id_of(folder)}: extracting audio from {os.path.basename(src)}")
    extract_wav(src, wav)

    draft, master = (os.path.join(work, stem + s) for s in ("_draft_raw.txt", "_master.txt"))
    seg_json = os.path.join(work, stem + "_segments.json")

    if a.speakers <= 1 or a.also_timed:
        print(f"Timed transcription ({a.model}, language {a.language})...")
        segs, lang, device = timed_run(wav, a.model, a.language)
        with open(seg_json, "w", encoding="utf-8") as f:
            json.dump(segs, f, indent=1)
        print(f"  {len(segs)} segments on {device}, language {lang}")
        if a.speakers <= 1:
            with open(draft, "w", encoding="utf-8") as f:
                for s in segs:
                    f.write(f"{hms(s['start'])} Speaker 1: {s['text']}\n")

    if a.speakers >= 2:
        token = user_env_token()
        if not token:
            sys.exit("HF_TOKEN not set. The diarized run needs it (see the wwd-video-transcriber setup guide).")
        os.makedirs(EMPTY_VP, exist_ok=True)
        raw_out = os.path.join(work, stem + "_diarized_raw.txt")
        env = dict(os.environ, HF_TOKEN=token)
        cmd = [sys.executable, TRANSCRIBE, "--audio", wav, "--output", raw_out,
               "--voiceprints-dir", EMPTY_VP, "--num-speakers", str(a.speakers)]
        print("Diarized run (local models), voiceprints disabled for client audio...")
        r = subprocess.run(cmd, env=env, cwd=work)
        if r.returncode != 0 or not os.path.isfile(raw_out):
            sys.exit("transcribe.py failed. See its output above.")
        with open(raw_out, encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r"Guest/Unknown \[(\d+)\]", r"Speaker \1", text)
        labels = [re.sub(r"^\[[^\]]*\]\s*", "", l).split(":")[0] for l in text.splitlines()]
        if any(HOSTS.search(x) for x in labels):
            sys.exit("A WWD host name appeared as a speaker label. Aborting: client audio must stay generic.")
        with open(draft, "w", encoding="utf-8") as f:
            f.write(text)

    if not os.path.isfile(master):  # never overwrite a proofread master
        with open(draft, encoding="utf-8") as src_f, open(master, "w", encoding="utf-8") as dst_f:
            dst_f.write(src_f.read())
        print(f"Master created: {master}")
    else:
        print(f"Master already exists, left untouched: {master}")

    mins = (time.time() - t0) / 60
    job_clock.add_minutes(folder, "machine", mins, "run_pipeline (wall clock)")
    T.tracker_upsert(T.job_id_of(folder), {"Status": "Drafted", "Waiting on": "agent",
                                           "Notes": "Draft ready, proofread next"})
    print(f"Done in {mins:.1f} min. Draft: {draft}")
    print("Next: start the proofreading clock, edit the _master.txt, then convert_deliverable.py")


if __name__ == "__main__":
    main()
