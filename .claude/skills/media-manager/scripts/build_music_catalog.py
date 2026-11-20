"""Build the owned-music catalog for the music department.

Read-only on every source drive. Writes only:
  D:\\WKP\\data\\assets\\music-catalog.csv   (one row per audio file)
  D:\\WKP\\data\\assets\\music-catalog.md    (summary the music agent reads first)

Durations come from ffprobe for top-level tracks and WWD folders (fast).
Loop and stem packs inside subfolders are listed with size only unless --all-durations.

Usage:
  python build_music_catalog.py [--all-durations]
"""
import csv, os, subprocess, sys, datetime, collections, re

ROOTS = [
    # (label, path, recurse)
    ("P music library", r"P:\Sounds\Music", True),
    ("WWD audio (L)", r"L:\Winter Wolfs Den review show\Audio", False),
    ("WWD music folder (L, misspelled)", r"L:\Winter Wolfs Den review show\Muisc", True),
    ("WWD kit sounds", r"P:\WWD Kit", True),
    ("Ian trailer music", r"P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Music", True),
]
AUDIO = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg", ".aif", ".aiff"}
OUT_CSV = r"D:\WKP\data\assets\music-catalog.csv"
OUT_MD = r"D:\WKP\data\assets\music-catalog.md"
FFPROBE = "ffprobe"


def source_guess(name, path=""):
    n = name.lower()
    if (os.sep + "adobe" + os.sep) in path.lower():
        return "Adobe loop pack (terms not verified on disk)"
    if n.startswith("audioblocks-"):
        return "Audioblocks / Storyblocks (plan proof not on disk)"
    if re.search(r"_[A-Za-z0-9\-]{8}\.(mp3|wav)$", name):
        return "Storyblocks-style ID suffix (plan proof not on disk)"
    if n.startswith(("bbc-", "bcc-")):
        return "Storyblocks-style catalog name (plan proof not on disk)"
    if "ytdown" in n or "youtube" in n:
        return "YouTube rip, NOT cleared, never use publicly"
    return "unknown"


def duration(path):
    try:
        r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                            "-of", "default=nw=1:nk=1", path],
                           capture_output=True, text=True, timeout=20)
        return f"{float(r.stdout.strip()):.1f}"
    except Exception:
        return ""


def main():
    all_dur = "--all-durations" in sys.argv
    rows = []
    for label, root, recurse in ROOTS:
        if not os.path.isdir(root):
            rows.append({"group": label, "path": root, "folder": "", "name": "", "ext": "",
                         "size_mb": "", "modified": "", "seconds": "", "source_guess": "FOLDER NOT AVAILABLE"})
            continue
        walker = os.walk(root) if recurse else [(root, [], os.listdir(root))]
        for d, _, files in walker:
            if "__MACOSX" in d.split(os.sep):
                continue  # macOS zip junk, not audio
            for f in files:
                if f.startswith("._"):
                    continue
                ext = os.path.splitext(f)[1].lower()
                if ext not in AUDIO:
                    continue
                p = os.path.join(d, f)
                st = os.stat(p)
                top = (d == root)
                want = all_dur or top or label != "P music library"
                rows.append({
                    "group": label, "path": p,
                    "folder": os.path.relpath(d, root),
                    "name": f, "ext": ext,
                    "size_mb": f"{st.st_size/1e6:.2f}",
                    "modified": datetime.date.fromtimestamp(st.st_mtime).isoformat(),
                    "seconds": duration(p) if want else "",
                    "source_guess": source_guess(f, p),
                })
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    today = datetime.date.today().isoformat()
    by_group = collections.Counter(r["group"] for r in rows if r["name"])
    by_folder = collections.Counter((r["group"], "\\".join(r["folder"].split(os.sep)[:2])) for r in rows if r["name"])
    src = collections.Counter(r["source_guess"] for r in rows if r["name"])
    full = [r for r in rows if r["group"] == "P music library" and r["folder"] == "." and r["name"]]
    lines = [
        "# Owned music catalog",
        "",
        f"Built {today} by `build_music_catalog.py` (read-only listing, ffprobe durations). "
        "Kept by media-manager, read first by `music` on every job. Full rows: `music-catalog.csv`.",
        "",
        "Nobody here can hear audio. Mood and genre come from file names only, labeled that way. Zac auditions.",
        "",
        "## Counts by source folder",
        "",
        "| Group | Audio files |",
        "|---|---|",
    ]
    for g, n in by_group.most_common():
        lines.append(f"| {g} | {n} |")
    lines += ["", "## Folders (loop and stem packs live in subfolders)", "", "| Group | Folder | Files |", "|---|---|---|"]
    for (g, f), n in sorted(by_folder.items()):
        lines.append(f"| {g} | {f} | {n} |")
    lines += ["", "## License picture (from file names, not proof)", "", "| Source guess | Files |", "|---|---|"]
    for s, n in src.most_common():
        lines.append(f"| {s} | {n} |")
    lines += ["", "## WWD audio on disk (L: Audio folder plus P:\\WWD Kit show folders; kit files are mostly SFX)", ""]
    for r in rows:
        if r["group"].startswith("WWD") and r["name"]:
            lines.append(f"- `{r['path']}` ({r['seconds'] or '?'} s, {r['modified']})")
    lines += ["", f"## Full-length tracks at the top of P:\\Sounds\\Music ({len(full)})", "",
              "| File | Seconds | Source guess |", "|---|---|---|"]
    for r in sorted(full, key=lambda x: x["name"].lower()):
        lines.append(f"| {r['name']} | {r['seconds']} | {r['source_guess']} |")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"rows {len(rows)} -> {OUT_CSV}; summary -> {OUT_MD}")


if __name__ == "__main__":
    main()
