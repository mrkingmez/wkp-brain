# -*- coding: utf-8 -*-
"""Edge check for a finished short: transcribe the first and last 3.5 seconds.

Usage: python check_clip.py --clip clipN_slug.mp4 [--out-dir DIR]
Prints the words actually audible at the head and tail so the cut can be verified against
the transcript (first words must not be So/Yeah/I think/Alright/Well, last word must not be
a clipped fragment of the next sentence). Head includes the one-frame cover, so spoken words
start a few hundredths of a second in.
"""
import argparse, os, subprocess, tempfile

p = argparse.ArgumentParser()
p.add_argument("--clip", required=True)
a = p.parse_args()

from faster_whisper import WhisperModel
try:
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
except Exception:
    model = WhisperModel("large-v3", device="cpu", compute_type="int8")

tmp = os.environ.get("WKP_SCRATCH", r"D:\WKP\scratch")
for label, args in (("HEAD", ["-t", "3.5"]), ("TAIL", ["-sseof", "-3.5"])):
    wav = os.path.join(tmp, f"_edge_{label}.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"] + args +
                   ["-i", a.clip, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    segs, _ = model.transcribe(wav, language="en", word_timestamps=True, vad_filter=False)
    words = [f"{w.word.strip()}[{w.start:.2f}]" for s in segs for w in (s.words or [])]
    print(label + ":", " ".join(words) if words else "(no speech detected)")
