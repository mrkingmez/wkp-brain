"""Regression tests: frozen real prompts from the logs. Failed set must be flagged, good set must have zero FAIL.
Run: python -m unittest discover -s tests -v. WARNs on the good set are printed on purpose (read them)."""
import os
import re
import subprocess
import sys
import unittest

from _util import *   # noqa

PY = sys.executable
M = manifest()
FAILED = {e["id"]: e for e in M["failed"] if e["set"] == "failed"}
CONFLICT = [e for e in M["failed"] if e["set"] == "known_conflict"]


def run_entry(e, history=None):
    meta = meta_of(e)
    meta["SHOT"] = e["id"]
    return P.run_checks(e["text"], meta, None, history)


class FailedSet(unittest.TestCase):
    def test_fixture_counts(self):
        self.assertEqual(len([e for e in FAILED if e.startswith("G")]), 12)       # garage 1 to 13 without 5
        self.assertEqual(len([e for e in FAILED if e.startswith("J") and not e.startswith("JS")]), 4)
        self.assertEqual(len([e for e in FAILED if e.startswith("JS") and "-" not in e]), 7)
        self.assertEqual([e["id"] for e in CONFLICT], ["G5"])

    def test_each_failed_prompt_is_flagged_as_the_manifest_says(self):
        for eid, e in FAILED.items():
            with self.subTest(fixture=eid):
                f = run_entry(e)
                miss_flag = set(e["must_flag"]) - fired(f)
                miss_fail = set(e["must_fail"]) - failed(f)
                self.assertFalse(miss_flag, "%s not flagged: %s (fired: %s)" % (eid, sorted(miss_flag), sorted(fired(f))))
                self.assertFalse(miss_fail, "%s not FAIL: %s" % (eid, sorted(miss_fail)))
                self.assertEqual(P.verdict(f), "FAIL" if e["must_fail"] else P.verdict(f))

    def test_every_failed_prompt_gets_a_non_pass_verdict(self):
        for eid, e in FAILED.items():
            self.assertNotEqual(P.verdict(run_entry(e)), "PASS", eid)

    def test_garage6_specific_pairs(self):
        f = run_entry(FAILED["G6"])
        self.assertEqual({"PF04", "PF05"} <= failed(f), True)
        self.assertIn("WARN", sevs(f, "PF06"))

    def test_garage12_contact_pair(self):
        f = run_entry(FAILED["G12"])
        self.assertIn("FAIL", sevs(f, "R9"))
        self.assertIn("WARN", sevs(f, "PF03"))

    def test_joust4_spear_is_fail(self):
        self.assertIn("FAIL", sevs(run_entry(FAILED["J4"]), "PF10"))

    def test_logo_with_no_start_frame_fails_pf09(self):
        self.assertIn("FAIL", sevs(run_entry(FAILED["JS2-nostart"]), "PF09"))
        self.assertNotIn("FAIL", sevs(run_entry(FAILED["JS2"]), "PF09"))      # same text, start frame yes: WARN only

    def test_legacy_r_findings_match_prompt_lint_exactly(self):
        lint = P.lint_module()
        for e in M["failed"]:
            kind = "video" if e["kind"] == "video" else "still"
            fails, warns = lint.lint(e["id"], e["text"], kind, e["engine"], e["start_frame"], "off", allow_impact=e["allow_impact"])
            f = run_entry(e)
            self.assertEqual({s.split()[0] for s in fails}, {x.rule for x in f if x.sev == "FAIL" and x.rule.startswith("R")}, e["id"])
            self.assertEqual({s.split()[0] for s in warns} - {s.split()[0] for s in fails},
                             {x.rule for x in f if x.sev == "WARN" and x.rule.startswith("R")} - {s.split()[0] for s in fails}, e["id"])


class KnownConflict(unittest.TestCase):
    def test_garage5_is_a_judgement_call_not_a_pass(self):
        e = CONFLICT[0]
        f = run_entry(e)
        self.assertIn("FAIL", sevs(f, "R1"))          # "no camera movement" trips R1: our best clip fails the rule
        print("\nKNOWN CONFLICT G5 (best clip, 189 words): verdict %s, fired %s, FAIL %s" % (P.verdict(f), sorted(fired(f)), sorted(failed(f))))


class History(unittest.TestCase):
    def _hist(self, ids, shot="JOUST"):
        return [{"shot": shot, "attempt": i + 1, "date": "2026-11-24", "text": FAILED[x]["text"]} for i, x in enumerate(ids)]

    def test_final_three_joust_texts_are_identical(self):
        self.assertEqual(FAILED["JS5"]["text"], FAILED["JS6"]["text"])
        self.assertEqual(FAILED["JS6"]["text"], FAILED["JS7"]["text"])

    def test_pf07_after_three_identical_tries_fails_with_redesign(self):
        meta = meta_of(FAILED["JS7"])
        meta["SHOT"] = "JOUST"
        f = P.run_checks(FAILED["JS7"]["text"], meta, None, self._hist(["JS5", "JS6", "JS5"]))
        self.assertIn("FAIL", sevs(f, "PF07"))
        self.assertIn("redesign", [x for x in f if x.rule == "PF07"][0].detail)

    def test_pf07_two_identical_tries_warns(self):
        meta = meta_of(FAILED["JS7"])
        meta["SHOT"] = "JOUST"
        f = P.run_checks(FAILED["JS7"]["text"], meta, None, self._hist(["JS5", "JS6"]))
        self.assertEqual(sevs(f, "PF07"), {"WARN"})

    def test_pf08_between_real_joust_retries(self):
        meta = meta_of(FAILED["JS3"])
        meta["SHOT"] = "JOUST"
        f = P.run_checks(FAILED["JS3"]["text"], meta, None, self._hist(["JS2"]))
        n = [x for x in f if x.rule == "PF08"]
        print("\nPF08 JS2 -> JS3:", n[0].sev, n[0].detail)
        self.assertEqual(n[0].sev, "WARN")           # real runs changed many sentences at once (LESSONS F18)

    def test_pf08_identical_final_runs_is_not_stacked(self):
        meta = meta_of(FAILED["JS6"])
        meta["SHOT"] = "JOUST"
        f = P.run_checks(FAILED["JS6"]["text"], meta, None, self._hist(["JS5"]))
        self.assertEqual(sevs(f, "PF08"), {"PASS"})

    def test_history_through_a_temp_file_and_cli(self):
        p = os.path.join(SCRATCH, "joust-history.jsonl")
        if os.path.exists(p):
            os.remove(p)
        txt = FAILED["JS7"]["text"]
        tp = os.path.join(SCRATCH, "js7.txt")
        open(tp, "w", encoding="utf-8").write(txt)
        codes = []
        for _ in range(4):
            r = subprocess.run([PY, os.path.join(PF, "preflight.py"), tp, "--kind", "video", "--engine", "veo", "--start-frame", "yes",
                                "--shot", "JOUST", "--history", p, "--record", "--record-anyway", "--quiet", "--no-checklist"], capture_output=True, text=True)
            codes.append((r.returncode, "PF07" in r.stdout and "[FAIL] PF07" in r.stdout))
        self.assertTrue(codes[3][1], "fourth try should hit the PF07 FAIL: " + repr(codes))
        self.assertFalse(codes[0][1])


class GoodSet(unittest.TestCase):
    """Zero FAIL allowed. WARNs are listed so a human can judge them."""

    def load(self, entry):
        path = os.path.join(FIX, entry["file"])
        text = open(path, encoding="utf-8").read()
        return P.load_input(path) if entry["format"] != "x" else None

    def all_results(self):
        out = []
        for g in M["good"]:
            for meta, prompt, neg in self.load(g):
                m = dict(meta)
                if m.get("ID") == "PB-edit-pose":
                    m["KIND"] = "edit"                       # the playbook block header says still; it is an edit prompt
                if m.get("ID") == "ian-R3b":
                    m["REFERENCE_TYPE"] = "composition"      # from ian-R3b/settings.txt: PANEL MODE reference (Composition)
                out.append((g["file"], m.get("ID"), P.run_checks(prompt, m, neg)))
        return out

    def test_counts(self):
        res = self.all_results()
        per = {}
        for f, i, _ in res:
            per[f] = per.get(f, 0) + 1
        self.assertEqual(per["good/rebuilt-prompts.md"], 20)
        self.assertEqual(per["good/pj-intro-prompts.md"], 3)
        self.assertEqual(sum(v for k, v in per.items() if "ian-" in k), 4)
        self.assertEqual(per["good/playbook-PB-edit-pose.md"], 1)

    def test_no_fail_in_the_good_set(self):
        bad = []
        lines = []
        for fn, pid, f in self.all_results():
            if failed(f):
                bad.append((pid, sorted(failed(f))))
            w = sorted((x.rule for x in f if x.sev == "WARN"))
            lines.append("%-26s %-5s WARN: %s" % (pid, P.verdict(f), " ".join(w) or "-"))
        print("\nGOOD SET (%d prompts):\n  " % len(lines) + "\n  ".join(lines))
        self.assertEqual(bad, [], "good prompts with a FAIL: %r" % bad)

    def test_ian_negative_boxes_parsed_and_warned(self):
        for d in ("R3b", "H1", "B1", "W1"):
            (meta, prompt, neg), = P.load_input(os.path.join(FIX, "good", "ian-%s-prompt.txt" % d))
            self.assertTrue(neg and "text" in neg, d)
            self.assertNotIn("NEGATIVE", prompt)
            self.assertIn("WARN", sevs(P.run_checks(prompt, meta, neg), "PF26"))

    def test_r3b_composition_reference_warns_pf29(self):
        (meta, prompt, neg), = P.load_input(os.path.join(FIX, "good", "ian-R3b-prompt.txt"))
        meta["REFERENCE_TYPE"] = "composition"
        self.assertIn("WARN", sevs(P.run_checks(prompt, meta, neg), "PF29"))

    def test_playbook_edit_example_is_clean_as_an_edit(self):
        (meta, prompt, neg), = P.load_input(os.path.join(FIX, "good", "playbook-PB-edit-pose.md"))
        meta["KIND"] = "edit"
        f = P.run_checks(prompt, meta, neg)
        self.assertEqual(failed(f), set())
        for r in ("PF20", "PF21", "PF22"):
            self.assertEqual(sevs(f, r), {"PASS"}, r)


class LegacyBaseline(unittest.TestCase):
    """prompt_lint.py output must equal the output saved before the preflight build."""

    def lint(self, *args):
        r = subprocess.run([PY, os.path.join(P.LINT_DIR, "prompt_lint.py")] + list(args), capture_output=True, text=True,
                           encoding="utf-8", cwd=P.LINT_DIR)
        return r.returncode, r.stdout.replace("\r\n", "\n")

    def base(self, name):
        return open(os.path.join(TESTS, "baseline", name), encoding="utf-8").read().replace("\r\n", "\n")

    def test_rebuilt_file_20_pass_exit_0(self):
        code, out = self.lint("--file", os.path.join(P.LINT_DIR, "REBUILT-PROMPTS-2026-11-22.md"))
        self.assertEqual(code, 0)
        self.assertEqual(out, self.base("legacy_rebuilt.txt"))
        self.assertEqual(len(re.findall(r"^\[PASS\]", out, re.M)), 20)
        self.assertNotIn("[FAIL]", out)

    def test_audit_old_baseline(self):
        code, out = self.lint("--audit-old")
        self.assertEqual(out, self.base("legacy_audit_old.txt"))
        self.assertEqual(len(re.findall(r"^\[FAIL\]", out, re.M)), 24)
        for pid in ("STILL-R3b", "STILL-H1", "STILL-B1"):
            self.assertRegex(out, r"\[WARN\] %s " % pid)
        self.assertRegex(out, r"\[PASS\] STILL-W1 ")


if __name__ == "__main__":
    unittest.main()
