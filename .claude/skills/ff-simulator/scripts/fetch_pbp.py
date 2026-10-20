"""Pull nflverse play-by-play (and schedules) for the coaching-tendency model.

Filenames are discovered live from the nflverse-data release listing, never
hardcoded (same rule as the nfl-data skill). Saves to D:\\WKP\\data\\nfl\\pbp\\.
Usage: python fetch_pbp.py 2023 2024 2025 2026
"""
import json, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com/repos/nflverse/nflverse-data/releases/tags/pbp"
DEST = Path(r"D:\WKP\data\nfl\pbp")


def main(seasons):
    req = urllib.request.Request(API, headers={"User-Agent": "wkp-ff-simulator"})
    with urllib.request.urlopen(req, timeout=60) as r:
        assets = json.load(r)["assets"]
    DEST.mkdir(parents=True, exist_ok=True)
    for s in seasons:
        name = f"play_by_play_{s}.parquet"
        a = next((x for x in assets if x["name"] == name), None)
        if a is None:
            print("NOT FOUND:", name); continue
        out = DEST / name
        rq = urllib.request.Request(a["browser_download_url"], headers={"User-Agent": "wkp-ff-simulator"})
        with urllib.request.urlopen(rq, timeout=300) as resp, open(out, "wb") as f:
            f.write(resp.read())
        Path(str(out) + ".meta.json").write_text(json.dumps({
            "downloaded_at": datetime.now(timezone.utc).isoformat(),
            "source_url": a["browser_download_url"],
            "source_updated_at": a["updated_at"],
            "size_bytes": out.stat().st_size}, indent=2), encoding="utf-8")
        print("Saved", out, out.stat().st_size, "bytes, source updated", a["updated_at"])


if __name__ == "__main__":
    main(sys.argv[1:] or ["2023", "2024", "2025", "2026"])
