r"""find_asset.py - keyword lookup over the P: drive index and the media map.

Usage:
  python find_asset.py baseball bounce
  python find_asset.py "garage door" --max 20
  python find_asset.py ratchet --ext wav,mp3
  python find_asset.py lut --map-only

Rules: every keyword must match (case-insensitive, any order, in the full path).
Read-only. Never moves, copies or deletes anything.
Sources: D:\WKP\data\assets\p-drive-index.csv (file level, P: drive) and
D:\WKP\data\assets\media-map.md (folder level, every drive).
"""
import argparse, csv, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
IDX = os.path.join(ROOT, "data", "assets", "p-drive-index.csv")
MAP = os.path.join(ROOT, "data", "assets", "media-map.md")


def kw_match(text, kws):
    t = text.lower()
    return all(k in t for k in kws)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+")
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument("--ext", default="", help="comma list, e.g. wav,mp3")
    ap.add_argument("--map-only", action="store_true")
    ap.add_argument("--index-only", action="store_true")
    a = ap.parse_args()
    # split quoted phrases into words so "garage door" == garage door
    kws = [w.lower() for k in a.keywords for w in k.split()]
    exts = {"." + e.strip().lower().lstrip(".") for e in a.ext.split(",") if e.strip()}

    if not a.index_only and os.path.exists(MAP):
        print("== Media map (folder level) ==")
        n = 0
        with open(MAP, encoding="utf-8") as f:
            for ln, line in enumerate(f, 1):
                if line.lstrip().startswith("|") and kw_match(line, kws):
                    print(f"  media-map.md:{ln}: {line.strip()[:220]}")
                    n += 1
        if not n:
            print("  (no map rows matched)")
    if not a.map_only:
        print("== P: drive index (file level) ==")
        if not os.path.exists(IDX):
            print("  index not available:", IDX)
            return 1
        hits = []
        with open(IDX, encoding="utf-8-sig", newline="") as f:
            r = csv.reader(f)
            next(r, None)
            for row in r:
                if len(row) < 3:
                    continue
                if exts and row[1].lower() not in exts:
                    continue
                if kw_match(row[0], kws):
                    hits.append(row)
        print(f"  {len(hits)} match(es), showing {min(len(hits), a.max)}")
        for row in hits[: a.max]:
            try:
                kb = int(row[2]) / 1024
                size = f"{kb:,.0f} KB"
            except ValueError:
                size = "?"
            exists = "ok" if os.path.exists(row[0]) else "NOT ON DISK NOW"
            print(f"  {row[0]}  [{row[1]}, {size}, {exists}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
