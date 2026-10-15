# -*- coding: utf-8 -*-
"""Word-level timing for a finished review edit (local faster-whisper, GPU).

Usage: python word_times.py --audio analysis.mp3 --out words.json
Pass the mono 16k analysis mp3 that `build_short.py analyze` already wrote
(<silence.json stem>_analysis.mp3). Output: [{"w": "word", "s": start, "e": end}, ...]

Used for caption timing and for exact in/out points. The Premiere transcript stays the
source of truth for wording and speaker labels. Whisper words are timing only, so garbles
in either source still get flagged, never published.
"""
import argparse, json

p = argparse.ArgumentParser()
p.add_argument("--audio", required=True)
p.add_argument("--out", required=True)
p.add_argument("--model", default="large-v3")
a = p.parse_args()

from faster_whisper import WhisperModel
try:
    model = WhisperModel(a.model, device="cuda", compute_type="float16")
except Exception:
    model = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, _ = model.transcribe(a.audio, language="en", word_timestamps=True, vad_filter=False,
                           condition_on_previous_text=False)
words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)}
         for s in segs for w in (s.words or [])]
json.dump(words, open(a.out, "w", encoding="utf-8"))
print(len(words), "words ->", a.out)
