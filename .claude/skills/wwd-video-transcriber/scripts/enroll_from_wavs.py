#!/usr/bin/env python3
"""
enroll_from_wavs.py  (added 2026-11-11)

Builds or refreshes one person's voiceprint from one or more clean one-person
audio files (for example a StreamYard solo webcam mp4). Replaces enroll_voices.py
for this machine: that script needs --hf-token and reads audio through
torchcodec, which is broken here. This one reads WAV directly and takes the
token from the HF_TOKEN environment variable.

Usage (python from LOCAL-PATHS.md):
    python enroll_from_wavs.py --name zac --src "C:\\path\\solo1.mp4" "C:\\path\\solo2.mp4"
    --name is matt, zac or gabby. Any audio/video ffmpeg can read works.

What it does per source file: converts to 16 kHz mono (scratch), cuts 3 s
windows that are speech all the way through, embeds each with
pyannote/embedding, drops windows that do not sound like the file's own
speaker (cosine to the file centroid below 0.5, usually bleed or noise), keeps
up to --cap windows per file (default 30 = 90 s), then saves the L2-normalised
mean of everything as <voiceprints-dir>/<name>.npy (512 floats, the format
transcribe.py loads).

Biometric data: output stays in D:\\WKP\\voiceprints (gitignored). Nothing is
uploaded. Use a different --voiceprints-dir to test without touching the live set.
"""
import argparse, os, subprocess, sys, tempfile, wave

import numpy as np

SR = 16000
WIN = 3.0


def to_wav(src, dst, ss, t):
    cmd = ["ffmpeg", "-v", "error", "-y"]
    if ss:
        cmd += ["-ss", str(ss)]
    if t:
        cmd += ["-t", str(t)]
    cmd += ["-i", src, "-vn", "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", dst]
    subprocess.run(cmd, check=True)


def load(path):
    with wave.open(path, "rb") as wf:
        raw = wf.readframes(wf.getnframes())
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


def active_windows(x, rms_min=0.012, frac=0.85):
    n, f = int(WIN * SR), SR // 10
    out = []
    for s in range(0, len(x) - n + 1, n):
        fr = x[s:s + n][: (n // f) * f].reshape(-1, f)
        if (np.sqrt((fr ** 2).mean(1)) > rms_min).mean() >= frac:
            out.append(x[s:s + n])
    return out


def unit(v):
    return v / (np.linalg.norm(v, axis=-1, keepdims=True) + 1e-8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, choices=["matt", "zac", "gabby"])
    ap.add_argument("--src", required=True, nargs="+")
    ap.add_argument("--start", type=float, default=300, help="skip this many seconds at the start of each source (default 300)")
    ap.add_argument("--length", type=float, default=1500, help="seconds to read from each source (default 1500)")
    ap.add_argument("--cap", type=int, default=30, help="max 3 s windows per source file")
    ap.add_argument("--voiceprints-dir", default=os.path.normpath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "voiceprints")))
    a = ap.parse_args()

    token = os.environ.get("HF_TOKEN")
    if not token:
        sys.exit("HF_TOKEN environment variable is not set.")
    import torch
    from pyannote.audio import Inference, Model
    inf = Inference(Model.from_pretrained("pyannote/embedding", token=token), window="whole",
                    device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    allw, report = [], []
    with tempfile.TemporaryDirectory(dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "scratch")
                                     if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "scratch")) else None) as td:
        for i, src in enumerate(a.src):
            wav = os.path.join(td, f"s{i}.wav")
            to_wav(src, wav, a.start, a.length)
            ws = active_windows(load(wav))
            embs = np.stack([np.asarray(inf({"waveform": torch.from_numpy(w.reshape(1, -1).copy()), "sample_rate": SR})).flatten() for w in ws])
            e = unit(embs)
            keep = np.where(e @ unit(e.mean(0)) > 0.5)[0]
            if len(keep) > a.cap:
                keep = keep[np.linspace(0, len(keep) - 1, a.cap).astype(int)]
            allw.append(e[keep])
            report.append((src, len(ws), len(keep)))
    E = np.concatenate(allw)
    vp = unit(E.mean(0)).astype(np.float32)
    os.makedirs(a.voiceprints_dir, exist_ok=True)
    out = os.path.join(a.voiceprints_dir, f"{a.name}.npy")
    np.save(out, vp)
    for src, n_all, n_keep in report:
        print(f"  {os.path.basename(src)}: {n_all} usable windows, kept {n_keep}")
    print(f"Saved {a.name} voiceprint from {len(E)} windows ({len(E) * WIN:.0f} s): {out}")


if __name__ == "__main__":
    main()
