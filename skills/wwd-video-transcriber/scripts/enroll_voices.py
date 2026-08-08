#!/usr/bin/env python3
"""
enroll_voices.py

One-time voice enrollment for the WWD transcriber. Extracts a speaker
embedding from a clean solo audio clip and saves it as a voiceprint
fingerprint used later to auto-map diarized speakers to Matt/Zac/Gabby
by name instead of generic SPEAKER_00/01/02 labels.

Usage:
    python enroll_voices.py --name matt  --clip /path/to/matt_solo.wav
    python enroll_voices.py --name zac   --clip /path/to/zac_solo.wav
    python enroll_voices.py --name gabby --clip /path/to/gabby_solo.wav

Clip requirements:
    - 20-60 seconds of ONE person talking alone, no crosstalk, no music/SFX
    - Same rough mic/setup as normal recordings if possible (levels drift
      matter less than actual voice timbre, but cleaner is better)

Re-run for a name to overwrite/refresh that person's voiceprint if mapping
starts drifting or a mic setup changes significantly.
"""

import argparse
import os
import sys

import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, choices=["matt", "zac", "gabby"],
                         help="Which host this clip belongs to")
    parser.add_argument("--clip", required=True, help="Path to solo audio clip (wav)")
    parser.add_argument("--hf-token", required=True, help="Hugging Face token")
    parser.add_argument(
        "--voiceprints-dir",
        default=os.path.join(os.path.dirname(__file__), "..", "voiceprints"),
        help="Where to save the voiceprint .npy file",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.clip):
        print(f"Clip not found: {args.clip}")
        sys.exit(1)

    try:
        from pyannote.audio import Inference, Model
    except ImportError:
        print("pyannote.audio not installed. Run scripts/setup_env.sh first.")
        sys.exit(1)

    print(f"Loading speaker embedding model (first run downloads weights)...")
    inference = Inference(Model.from_pretrained("pyannote/embedding", token=args.hf_token), window="whole")

    print(f"Extracting voiceprint from {args.clip}...")
    embedding = inference(args.clip)
    embedding = np.asarray(embedding).flatten()

    os.makedirs(args.voiceprints_dir, exist_ok=True)
    out_path = os.path.join(args.voiceprints_dir, f"{args.name}.npy")
    np.save(out_path, embedding)

    print(f"Saved voiceprint for {args.name}: {out_path}")
    print("Enroll the remaining hosts (if not done yet), then run transcribe.py.")


if __name__ == "__main__":
    main()
