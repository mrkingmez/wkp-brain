"""Shared helpers for the preflight tests."""
import json, os, sys

TESTS = os.path.dirname(os.path.abspath(__file__))
PF = os.path.dirname(TESTS)
sys.path.insert(0, PF)
import preflight as P   # noqa: E402
import rules as R       # noqa: E402

ROOT = R.ROOT
FIX = os.path.join(TESTS, "fixtures")
SCRATCH = os.path.join(ROOT, "scratch", "preflight-tests")
os.makedirs(SCRATCH, exist_ok=True)


def manifest():
    return json.load(open(os.path.join(FIX, "MANIFEST.json"), encoding="utf-8"))


def meta_of(e):
    return {"ID": e["id"], "KIND": e["kind"], "ENGINE": e["engine"], "START_FRAME": e["start_frame"],
            "END_FRAME": e["end_frame"], "AUDIO": "off", "ALLOW_IMPACT": "yes" if e["allow_impact"] else "no"}


def sevs(findings, rule):
    return {f.sev for f in findings if f.rule == rule}


def fired(findings):
    return {f.rule for f in findings if f.sev in ("FAIL", "WARN")}


def failed(findings):
    return {f.rule for f in findings if f.sev == "FAIL"}
