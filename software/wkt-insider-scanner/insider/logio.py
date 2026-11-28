"""Append-only JSONL writers. Every line carries config hash, tool version, run id. No secrets are ever passed in."""
import json
import os


def append_jsonl(path, records):
    if os.path.basename(path).lower() in ("decisions.jsonl", "paper-trades.csv", "state.json"):
        raise RuntimeError("refused: the insider scanner never writes the stock watcher output file names (ruling 8)")
    if not records:
        return 0
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lead = ""
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "rb") as f:
            f.seek(-1, os.SEEK_END)
            if f.read(1) != b"\n":
                lead = "\n"   # torn last line from a crash: start a fresh line
    with open(path, "a", encoding="utf-8") as f:
        f.write(lead + "".join(json.dumps(r, sort_keys=True, default=str) + "\n" for r in records))
        f.flush()
        os.fsync(f.fileno())
    return len(records)


def read_jsonl(path):
    out = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    out.append(json.loads(line))
                except ValueError:
                    continue
    return out
