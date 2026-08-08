#!/bin/bash
# extract_audio.sh
# Pulls a mono 16kHz WAV from a source video - the format the transcription
# and diarization models expect.
#
# Usage:
#   ./extract_audio.sh <source_video> <output.wav>

set -euo pipefail

SRC="$1"
OUT="$2"

if [ ! -f "$SRC" ]; then
  echo "Source video not found at: $SRC"
  exit 1
fi

mkdir -p "$(dirname "$OUT")"

ffmpeg -y -i "$SRC" \
  -ac 1 -ar 16000 -vn \
  "$OUT"

echo "Extracted audio: $OUT"
