#!/usr/bin/env python3
"""
transcribe.py

Main WWD transcription pipeline:
  1. Transcribe audio with Whisper (word-level timestamps)
  2. Diarize with pyannote (clusters into SPEAKER_00, SPEAKER_01, ...)
  3. Merge transcript words with diarization to get speaker-labeled segments
  4. Compare each diarized cluster's voice embedding against enrolled
     voiceprints (voiceprints/matt.npy, zac.npy, gabby.npy) and relabel
     clusters to real names when confidence clears the threshold
  5. Write out a clean, elapsed-timestamped transcript in WWD's standard
     format, ready to feed into wwd-frostcast-chapters, wwd-video-upload-package,
     and wwd-shorts-clip-factory

Usage:
    python transcribe.py --audio /path/to/audio.wav \
        --output /mnt/user-data/outputs/transcripts/episode_transcript.txt

Requires voiceprints already enrolled via enroll_voices.py.
Requires the HF_TOKEN environment variable to be set (Hugging Face token
with the pyannote gated model licenses accepted).
"""

import argparse
import os
import sys

import numpy as np

MATCH_THRESHOLD = 0.70  # cosine similarity floor before we trust a name match

NAME_MAP = {
    "matt": "Matt/Winter Wolf",
    "zac": "Zac/KingZ",
    "gabby": "Gabby/Oracle",
}


def cosine_sim(a, b):
    a, b = np.asarray(a).flatten(), np.asarray(b).flatten()
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))


def load_voiceprints(voiceprints_dir):
    prints = {}
    for name in ("matt", "zac", "gabby"):
        path = os.path.join(voiceprints_dir, f"{name}.npy")
        if os.path.isfile(path):
            prints[name] = np.load(path)
    return prints


def fmt_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"[{h:02d}:{m:02d}:{s:02d}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True, help="Path to extracted WAV audio")
    parser.add_argument("--output", required=True, help="Path to write the final transcript")
    parser.add_argument(
        "--voiceprints-dir",
        default=os.path.join(os.path.dirname(__file__), "..", "voiceprints"),
    )
    parser.add_argument("--model", default="large-v3", help="Whisper model size")
    args = parser.parse_args()

    hf_token = os.environ.get("HF_TOKEN")
    if not hf_token:
        print("HF_TOKEN environment variable is not set.")
        print("Set it to a Hugging Face token with the pyannote gated model")
        print("licenses accepted (see references/setup-guide.md), then re-run.")
        sys.exit(1)

    if not os.path.isfile(args.audio):
        print(f"Audio file not found: {args.audio}")
        sys.exit(1)

    voiceprints = load_voiceprints(args.voiceprints_dir)
    missing = [n for n in ("matt", "zac", "gabby") if n not in voiceprints]
    if missing:
        print(f"Missing voiceprints for: {', '.join(missing)}.")
        print("Run enroll_voices.py for each before transcribing, or continue")
        print("knowingly - unmapped hosts will show up as Guest/Unknown.")

    try:
        import whisperx
        from whisperx.diarize import DiarizationPipeline
        from pyannote.audio import Inference, Pipeline
    except ImportError:
        print("Missing dependencies. Run scripts/setup_env.sh first.")
        sys.exit(1)

    device = "cuda" if _has_cuda() else "cpu"
    compute_type = "float16" if device == "cuda" else "int8"

    print("Loading Whisper model and transcribing (this is the slow step)...")
    model = whisperx.load_model(args.model, device, compute_type=compute_type)
    audio = whisperx.load_audio(args.audio)
    result = model.transcribe(audio, batch_size=16)

    print("Aligning word-level timestamps...")
    align_model, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], align_model, metadata, audio, device)

    print("Running diarization (clustering speakers)...")
    diarize_pipeline = DiarizationPipeline(token=hf_token, device=device)
    diarize_segments = diarize_pipeline(args.audio)
    result = whisperx.assign_word_speakers(diarize_segments, result)

    print("Mapping diarized clusters to enrolled voices...")
    from pyannote.audio import Model
    embed_model = Inference(Model.from_pretrained("pyannote/embedding", token=hf_token), window="whole")
    cluster_labels = {}  # SPEAKER_00 -> "matt" / "zac" / "gabby" / None

    diarized_speakers = sorted(set(
        seg.get("speaker") for seg in result["segments"] if seg.get("speaker")
    ))

    for cluster in diarized_speakers:
        # Pull a representative chunk of this cluster's audio to embed.
        # Concatenate the first few segments belonging to this speaker.
        cluster_segments = [s for s in result["segments"] if s.get("speaker") == cluster][:5]
        if not cluster_segments:
            cluster_labels[cluster] = None
            continue

        clip_path = _extract_cluster_audio(args.audio, cluster_segments, cluster)
        try:
            cluster_embedding = embed_model(_load_wav_dict(clip_path))
        finally:
            if os.path.exists(clip_path):
                os.remove(clip_path)

        best_name, best_score = None, 0.0
        for name, vp in voiceprints.items():
            score = cosine_sim(cluster_embedding, vp)
            if score > best_score:
                best_name, best_score = name, score

        if best_name and best_score >= MATCH_THRESHOLD:
            cluster_labels[cluster] = best_name
            print(f"  {cluster} -> {NAME_MAP[best_name]} (confidence {best_score:.2f})")
        else:
            cluster_labels[cluster] = None
            print(f"  {cluster} -> UNMAPPED (best guess {best_name}, confidence {best_score:.2f} - below threshold)")

    print("Writing formatted transcript...")
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    guest_counter = {}
    with open(args.output, "w") as f:
        for seg in result["segments"]:
            speaker = seg.get("speaker")
            mapped = cluster_labels.get(speaker)
            if mapped:
                label = NAME_MAP[mapped]
            else:
                guest_counter.setdefault(speaker, len(guest_counter) + 1)
                label = f"Guest/Unknown [{guest_counter[speaker]}]"
            ts = fmt_timestamp(seg["start"])
            text = seg["text"].strip()
            f.write(f"{ts} {label}: {text}\n")

    print(f"Transcript written to: {args.output}")
    unmapped = [c for c, v in cluster_labels.items() if v is None]
    if unmapped:
        print(f"NOTE: {len(unmapped)} speaker cluster(s) did not confidently match a")
        print("core host - check the Guest/Unknown lines before treating this as final.")


def _has_cuda():
    try:
        import torch
        return torch.cuda.is_available()
    except Exception:
        return False


def _load_wav_dict(wav_path):
    """Reads a PCM WAV file directly and returns pyannote's expected
    {'waveform', 'sample_rate'} dict, bypassing torchcodec entirely (it's
    broken in this environment - see setup-guide.md troubleshooting)."""
    import wave
    import torch

    with wave.open(wav_path, "rb") as wf:
        sample_rate = wf.getframerate()
        n_channels = wf.getnchannels()
        raw = wf.readframes(wf.getnframes())

    samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if n_channels > 1:
        samples = samples.reshape(-1, n_channels).T
    else:
        samples = samples.reshape(1, -1)

    return {"waveform": torch.from_numpy(samples), "sample_rate": sample_rate}


def _extract_cluster_audio(source_wav, segments, cluster_name):
    """Concatenates a few segments of one speaker cluster into a temp wav
    for embedding. Uses ffmpeg under the hood for simplicity."""
    import subprocess
    import tempfile

    parts = []
    for i, seg in enumerate(segments):
        part_path = tempfile.mktemp(suffix=f"_{cluster_name}_{i}.wav")
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", source_wav,
                "-ss", str(seg["start"]), "-to", str(seg["end"]),
                part_path,
            ],
            check=True, capture_output=True,
        )
        parts.append(part_path)

    concat_list = tempfile.mktemp(suffix=".txt")
    with open(concat_list, "w") as f:
        for p in parts:
            f.write(f"file '{p}'\n")

    out_path = tempfile.mktemp(suffix=f"_{cluster_name}_merged.wav")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-c", "copy", out_path],
        check=True, capture_output=True,
    )

    for p in parts:
        os.remove(p)
    os.remove(concat_list)

    return out_path


if __name__ == "__main__":
    main()
