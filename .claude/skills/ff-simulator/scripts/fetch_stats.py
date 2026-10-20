"""Refresh player-week stats for the simulator (filenames discovered live).
Saves to the nfl-data cache folders so other skills see the same files.
Usage: python fetch_stats.py 2024 2025 2026
"""
import json, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(r"D:\WKP\data\nfl")
UA = {"User-Agent": "wkp-ff-simulator"}


def listing(tag):
    req = urllib.request.Request(f"https://api.github.com/repos/nflverse/nflverse-data/releases/tags/{tag}", headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["assets"]


def pull(tag, assets, name):
    a = next((x for x in assets if x["name"] == name), None)
    if a is None:
        print("NOT FOUND:", tag, name); return
    dest = BASE / tag
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / name
    with urllib.request.urlopen(urllib.request.Request(a["browser_download_url"], headers=UA), timeout=300) as resp, open(out, "wb") as f:
        f.write(resp.read())
    Path(str(out) + ".meta.json").write_text(json.dumps({
        "downloaded_at": datetime.now(timezone.utc).isoformat(), "source_url": a["browser_download_url"],
        "source_updated_at": a["updated_at"], "size_bytes": out.stat().st_size}, indent=2), encoding="utf-8")
    print("Saved", out, out.stat().st_size, "bytes, source updated", a["updated_at"])


def main(seasons):
    sp = listing("stats_player")
    for s in seasons:
        pull("stats_player", sp, f"stats_player_week_{s}.parquet")


if __name__ == "__main__":
    main(sys.argv[1:] or ["2024", "2025", "2026"])
