#!/bin/bash
# setup_env.sh
# One-time environment setup for the WWD video transcriber.
# Run this once on Zac's machine (or the Cowork/Claude Code environment
# that has access to it) before any transcription job.

set -euo pipefail

echo "Checking for ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
  echo "ffmpeg not found. Install it first (e.g. 'brew install ffmpeg' on macOS,"
  echo "'apt install ffmpeg' on Linux) then re-run this script."
  exit 1
fi
echo "ffmpeg OK."

echo "Installing Python dependencies (whisperx, pyannote, torch)..."
pip install --break-system-packages -U \
  whisperx \
  pyannote.audio \
  torch \
  torchaudio \
  numpy

mkdir -p "$(dirname "$0")/../voiceprints"

echo ""
echo "Setup complete. Next steps:"
echo "1. Get a Hugging Face token and accept the pyannote model license"
echo "   (see references/setup-guide.md)"
echo "2. Enroll Matt, Zac, and Gabby's voices with scripts/enroll_voices.py"
echo "   before running your first real transcription job."
