"""
nfl-data skill helper — discovers and downloads nflverse-data GitHub
release assets. No API key, no auth. See ../SKILL.md for the rules this
script exists to enforce (discover before download, honesty on data age,
current-season-only by default).

Usage:
    python nfl_data.py discover [--season YYYY]
    python nfl_data.py get <tag> <asset-substring> [--season YYYY]
    python nfl_data.py age <cached-file-path>
    python nfl_data.py list <tag>

Examples:
    python nfl_data.py discover --season 2026
    python nfl_data.py get stats_team stats_team_reg --season 2026
    python nfl_data.py get schedules games.parquet
    python nfl_data.py age D:\\WKP\\data\\nfl\\schedules\\games.parquet
"""
import argparse
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RELEASES_API = "https://api.github.com/repos/nflverse/nflverse-data/releases?per_page=100"
CACHE_DIR = Path(r"D:\WKP\data\nfl")
MANIFEST_PATH = CACHE_DIR / "nfl-data-manifest.json"

# The six releases this skill was built to serve (NFL-DATA-LAYER-BUILD.md
# Section 1). "player_stats" is the deprecated predecessor to
# "stats_player" — confirmed deprecated 2025-08-01 via its release body,
# never use it.
TRACKED_TAGS = [
    "pbp",
    "stats_team",
    "stats_player",
    "schedules",
    "players",
    "pfr_advstats",
]

# schedules and players ship as one rolling multi-season file, not a
# per-season asset — confirmed by discovery, not assumed.
ROLLING_TAGS = {"schedules", "players"}


def _get_json(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                "User-Agent": "wkp-nfl-data-skill"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def discover(season: str | None = None) -> dict:
    """Hit the GitHub releases API and build the manifest fresh. Never
    trust filenames typed into a doc — this is the only source of truth
    for what nflverse actually published."""
    releases = _get_json(RELEASES_API)
    by_tag = {r["tag_name"]: r for r in releases}

    manifest = {
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "season_filter": season,
        "releases": {},
    }

    for tag in TRACKED_TAGS:
        r = by_tag.get(tag)
        if r is None:
            manifest["releases"][tag] = {"found": False}
            continue

        assets = r["assets"]
        if tag in ROLLING_TAGS:
            picked = assets  # no season split — whole file, every time
        elif season:
            picked = [a for a in assets if season in a["name"]]
        else:
            picked = assets

        manifest["releases"][tag] = {
            "found": True,
            "published_at": r["published_at"],
            "asset_count_total": len(assets),
            "assets": [
                {
                    "name": a["name"],
                    "size": a["size"],
                    "updated_at": a["updated_at"],
                    "download_url": a["browser_download_url"],
                }
                for a in picked
            ],
        }

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def _load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return discover()
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def list_assets(tag: str):
    manifest = _load_manifest()
    entry = manifest["releases"].get(tag)
    if not entry or not entry.get("found"):
        print(f"'{tag}' not found in manifest. Re-run discover().")
        return
    for a in entry["assets"]:
        print(f"{a['name']}  {a['size']} bytes  updated {a['updated_at']}")


def get(tag: str, name_substring: str, season: str | None = None, force_rediscover: bool = False):
    """Download one asset by matching a substring against the discovered
    filenames — never a hardcoded filename. Re-discovers once on a 404,
    per Section 3's re-run rule, then gives up loudly rather than
    guessing at a substitute filename."""
    manifest = _load_manifest() if not force_rediscover else discover(season)
    entry = manifest["releases"].get(tag)
    if not entry or not entry.get("found"):
        raise SystemExit(f"Release '{tag}' not found on nflverse-data. Not substituting anything.")

    matches = [a for a in entry["assets"] if name_substring in a["name"]]
    if not matches:
        if not force_rediscover:
            print(f"No cached match for '{name_substring}' in {tag} — re-discovering once.")
            return get(tag, name_substring, season, force_rediscover=True)
        raise SystemExit(
            f"No asset matching '{name_substring}' in release '{tag}' after re-discovery. "
            f"Available: {[a['name'] for a in entry['assets']]}"
        )

    asset = matches[0]
    dest_dir = CACHE_DIR / tag
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / asset["name"]

    req = urllib.request.Request(asset["download_url"], headers={"User-Agent": "wkp-nfl-data-skill"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp, open(dest_path, "wb") as f:
            f.write(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 404 and not force_rediscover:
            print(f"404 on {asset['download_url']} — re-discovering once before giving up.")
            return get(tag, name_substring, season, force_rediscover=True)
        raise

    meta_path = dest_path.with_suffix(dest_path.suffix + ".meta.json")
    meta_path.write_text(json.dumps({
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
        "source_url": asset["download_url"],
        "source_updated_at": asset["updated_at"],
        "size_bytes": dest_path.stat().st_size,
    }, indent=2), encoding="utf-8")

    print(f"Saved {dest_path} ({dest_path.stat().st_size} bytes)")
    return dest_path


def age_days(path: str) -> float:
    """Honesty-rule helper. A consumer must state data age; this is how
    it checks it. Reads the .meta.json sidecar if present, else falls
    back to file mtime."""
    p = Path(path)
    meta_path = p.with_suffix(p.suffix + ".meta.json")
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        stamp = datetime.fromisoformat(meta["downloaded_at"])
    elif p.exists():
        stamp = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
    else:
        raise SystemExit(f"{path} does not exist — nothing to check.")
    age = datetime.now(timezone.utc) - stamp
    return age.total_seconds() / 86400


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("discover")
    d.add_argument("--season", default=None)

    g = sub.add_parser("get")
    g.add_argument("tag")
    g.add_argument("name_substring")
    g.add_argument("--season", default=None)

    a = sub.add_parser("age")
    a.add_argument("path")

    l = sub.add_parser("list")
    l.add_argument("tag")

    args = parser.parse_args()

    if args.cmd == "discover":
        manifest = discover(args.season)
        print(json.dumps({k: {"found": v.get("found"), "assets": len(v.get("assets", []))}
                           for k, v in manifest["releases"].items()}, indent=2))
    elif args.cmd == "get":
        get(args.tag, args.name_substring, args.season)
    elif args.cmd == "age":
        days = age_days(args.path)
        flag = " — STALE, more than 10 days old" if days > 10 else ""
        print(f"{days:.1f} days old{flag}")
    elif args.cmd == "list":
        list_assets(args.tag)


if __name__ == "__main__":
    main()
