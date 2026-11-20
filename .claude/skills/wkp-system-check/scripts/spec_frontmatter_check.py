"""spec_frontmatter_check.py - check every agent spec in D:\\WKP\\.claude\\agents\\*.md.

Checks: frontmatter block present, parses as simple YAML key: value, has name and
description (tools optional: none means all tools), name equals the filename stem. Read-only.
Exit 0 when clean, 1 otherwise. Built 2026-11-19 (readiness pass).
"""
import sys
from pathlib import Path

AGENTS = Path(r"D:\WKP\.claude\agents")


def parse(text):
    if not text.startswith("---"):
        return None, "no frontmatter"
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return None, "frontmatter not closed"
    fm = {}
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(parts[0][3:])
        if not isinstance(data, dict):
            return None, "frontmatter is not a mapping"
        return data, None
    except ImportError:
        for line in parts[0][3:].splitlines():
            if ":" in line and not line.startswith((" ", "-")):
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        return fm, None
    except Exception as e:  # yaml error
        return None, f"yaml error: {e}"


def main():
    bad = 0
    specs = sorted(AGENTS.glob("*.md"))
    for f in specs:
        data, err = parse(f.read_text(encoding="utf-8", errors="replace"))
        probs = []
        if err:
            probs.append(err)
        else:
            for k in ("name", "description"):
                if not data.get(k):
                    probs.append(f"missing {k}")
            if "tools" not in data:
                # Claude Code: no tools line = the agent inherits every tool. By design for
                # the "All tools" agents (marketing, social, copywriting, graphic-design,
                # market-research, video-ugc, fantasy-football-director). Listed, not failed.
                print(f"INFO {f.name}: no tools line, inherits all tools (by design)")
            if data.get("name") and data["name"] != f.stem:
                probs.append(f"name '{data['name']}' != filename '{f.stem}'")
        if probs:
            bad += 1
            print(f"FAIL {f.name}: {'; '.join(probs)}")
    print(f"specs: {len(specs)}  fail: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
