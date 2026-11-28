"""Unit tests for prompt-preflight. Run: python -m unittest discover -s tests -v  (or tests\\run_tests.bat)"""
import contextlib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import unittest

from _util import *   # noqa

PY = sys.executable
LONG = " ".join(["word"] * 200)


def run(text, **meta):
    m = {"KIND": "video", "ENGINE": "veo", "START_FRAME": "no", "AUDIO": "off"}
    m.update({k.upper(): v for k, v in meta.items()})
    return P.run_checks(text, m, meta.get("negative"), meta.get("history"))


def cli(argv, stdin=None):
    out, old = io.StringIO(), sys.stdin
    if stdin is not None:
        sys.stdin = io.StringIO(stdin)
    try:
        with contextlib.redirect_stdout(out):
            code = P.main(argv)
    finally:
        sys.stdin = old
    return code, out.getvalue()


# (rule, meta, triggering text, expected severity, non-triggering text)
CASES = [
    ("R1", {}, "A man walks. No hat. Static camera.", "FAIL", "A man walks. Static camera."),
    ("R2", {}, "A man walks. STOP now. Static camera.", "FAIL", "A man walks. Static camera."),
    ("R3", {}, LONG + " Static camera.", "FAIL", "A man walks. Static camera."),
    ("R4", {}, "A man walks as if tired. Static camera.", "FAIL", "A man walks. Static camera."),
    ("R5", {}, "A man walks — slowly. Static camera.", "FAIL", "A man walks. Static camera."),
    ("R6", {}, "A man walks walks. Static camera.", "FAIL", "A man walks. Static camera."),
    ("R7", {}, "A man walks.", "FAIL", "A man walks. Static camera."),
    ("R8", {}, "Locked camera. A man walks.", "WARN", "Dolly in. A man walks."),
    ("R9", {}, "Static camera. A ball bumps the wall.", "FAIL", "Static camera. A ball rests against the wall."),
    ("R10", {"audio": "on"}, "Static camera. A man walks.", "FAIL", "Static camera. A man walks. SFX: footsteps."),
    ("R11", {"start_frame": "yes"}, "Static camera. The car points to the right edge.", "WARN", "Static camera. The car idles."),
    ("R12", {}, "[00:00-00:02] Static camera. [00:03-00:05] He walks.", "FAIL", "[00:00-00:02] Static camera. [00:02-00:05] He walks."),
    ("R13", {}, "Static camera. " + " ".join("He steps %d." % i for i in range(10)), "WARN", "Static camera. He steps."),
    ("PF01", {}, "The car nose points toward the right edge of the frame.", "WARN", "The car sits in the middle of the frame."),
    ("PF02", {"kind": "still"}, "A man holds a steel wrench in his hands.", "WARN",
     "A man holds a steel wrench in his right hand, the other hand rests on the car."),
    ("PF03", {}, "A white ball rolls across the floor and stops against his boot.", "WARN", "A white ball sits on the floor."),
    ("PF04", {}, "He hands the wrench to a second man.", "FAIL", "He holds the wrench still."),
    ("PF05", {}, "He holds it out as if offering it to someone.", "FAIL", "He holds it still."),
    ("PF06", {}, "His face is out of frame.", "WARN", "A close-up of two forearms."),
    ("PF09", {}, "The logo appears on the shield.", "FAIL", "The shield is smooth oak."),
    ("PF10", {}, "He levels a long wooden lance.", "WARN", "He levels a long pole painted in red and white stripes."),
    ("PF11", {}, "Locked camera. He rolls out from under the car and sits up.", "FAIL", "Locked camera. He lies still."),
    ("PF12", {}, "Locked camera at floor level. A hand reaches in and picks up the ball.", "WARN",
     "Locked camera at floor level. A hand lowers from the top of the frame."),
    ("PF13", {}, "The open garage door lets in bright daylight.", "WARN", "The garage door is fully raised and daylight pours in."),
    ("PF14", {}, "At 4 seconds the lance hits.", "FAIL", "From 0 to 2 seconds he gallops."),
    ("PF15", {}, "A horse gallops. No music.", "WARN", "A horse gallops."),
    ("PF16", {}, "He walks. . then stops.", "WARN", "He walks. Then he stops."),
    ("PF20", {"kind": "edit"}, "Change the sky to dusk.", "FAIL", "Change the sky to dusk. Keep the face as in the source."),
    ("PF21", {"kind": "edit"}, "Change the sky to dusk. Remove the car. Keep the face as in the source.", "FAIL",
     "Change the sky to dusk. Keep the face as in the source."),
    ("PF22", {"kind": "edit"}, "Change the sky to dusk. Do not change the face.", "FAIL", "Change the sky to dusk. Keep the face as in the source."),
    ("PF23", {"kind": "still"}, "A man, 4k, 8k, hdr, masterpiece.", "WARN", "A man, 35mm film grain, shallow depth of field."),
    ("PF24", {"kind": "edit"}, "Change the sky to dusk. Keep the face.", "INFO", "Change the sky to dusk. Keep the face as in the source."),
    ("PF25", {"kind": "still", "engine": "firefly"}, "A man stands. " * 60, "WARN", "A man stands."),
    ("PF28", {"engine": "kling", "start_frame": "yes"}, "A man walks. Static camera.", "WARN",
     "Use @Image1 as the first frame. Single shot. A man walks. Static camera."),
]


class RuleCases(unittest.TestCase):
    def test_each_rule_triggers_and_stays_quiet(self):
        for rule, meta, bad, sev, good in CASES:
            with self.subTest(rule=rule):
                self.assertIn(sev, sevs(run(bad, **meta), rule), "trigger case did not fire " + rule)
                self.assertFalse(sevs(run(good, **meta), rule) & {"FAIL", "WARN", "INFO"}, "clean case fired " + rule)

    def test_pf01_start_frame_message(self):
        f = [x for x in run("The car points right.", start_frame="yes") if x.rule == "PF01"][0]
        self.assertIn("remove them from the text", f.detail)

    def test_pf01_camera_relative_words_do_not_fire(self):
        for ok in ("The ball enters from camera left.", "A rider at screen right.", "The shield sits frame left.",
                   "The ball rolls from the left of the frame.", "The hand nearest the camera holds it.",
                   "The far wall, farthest from the camera, is bare.", "He stands at frame right of the car."):
            self.assertEqual(sevs(run(ok), "PF01"), {"PASS"}, ok)

    def test_pf01_bare_side_words_still_fire(self):
        for bad in ("The shield sits on the left.", "The car points to the right edge of the frame.", "His right hand holds it."):
            self.assertEqual(sevs(run(bad), "PF01"), {"WARN"}, bad)
        # camera-relative phrase present, but a bare side word as well: still fires
        self.assertEqual(sevs(run("The ball enters from camera left. The car points right."), "PF01"), {"WARN"})

    def test_pf01_video_start_frame_scene_geometry_always_fires(self):
        f = [x for x in run("The ball enters from camera left. The car nose points to the left.", start_frame="yes") if x.rule == "PF01"][0]
        self.assertEqual(f.sev, "WARN")
        self.assertIn("remove them from the text", f.detail)
        self.assertEqual(sevs(run("The ball enters from camera left.", start_frame="yes"), "PF01"), {"PASS"})

    def test_pf03_only_warns_when_no_last_frame_is_claimed(self):
        t = "Static camera. A white ball rolls across the floor and stops against his boot."
        f = [x for x in run(t) if x.rule == "PF03"][0]
        self.assertEqual(f.sev, "WARN")
        self.assertIn("no end frame claimed; if you plan one, write END_FRAME: yes", f.detail)
        self.assertEqual(sevs(run(t, end_frame="yes"), "PF03"), {"PASS"})
        self.assertEqual(sevs(run(t, end_frame_file="GD-still-end.png"), "PF03"), {"PASS"})
        for planned in (" Use a last frame.", " The end frame shows it at rest.", " Image 2 is the last frame.", " The final frame is the boot."):
            self.assertEqual(sevs(run(t + planned), "PF03"), {"PASS"}, planned)
        self.assertEqual(sevs(run(t + " There is no end frame."), "PF03"), {"WARN"})

    def test_pf03_end_frame_file_header_key_is_parsed(self):
        blk = ("```prompt\nID: X\nKIND: video\nENGINE: veo\nEND_FRAME_FILE: end.png\n---\n"
               "Static camera. A ball rolls and stops against his boot.\n```\n")
        (meta, prompt, neg), = P.parse_blocks(blk)
        self.assertEqual(meta["END_FRAME_FILE"], "end.png")
        self.assertEqual(sevs(P.run_checks(prompt, meta, neg), "PF03"), {"PASS"})

    def test_pf05_still_is_warn(self):
        self.assertEqual(sevs(run("as if offering it to someone", kind="still"), "PF05"), {"WARN"})

    def test_pf09_variants(self):
        self.assertEqual(sevs(run("The logo glows.", start_frame="yes"), "PF09"), {"WARN"})
        self.assertEqual(sevs(run("The logo glows.", kind="still"), "PF09"), {"WARN"})

    def test_pf10_spear_fails_and_other_anchor_words(self):
        self.assertEqual(sevs(run("a spear flies"), "PF10"), {"FAIL"})
        self.assertIn("WARN", sevs(run("a coronal tip"), "PF10"))
        self.assertIn("WARN", sevs(run("a three-pronged tip"), "PF10"))

    def test_pf14_variants(self):
        self.assertFalse(sevs(run("At 4 seconds the lance hits.", engine="seedance"), "PF14") & {"FAIL"})
        self.assertIn("FAIL", sevs(run("The rider is accelerating."), "PF14"))
        self.assertIn("WARN", sevs(run("A slow-motion beat."), "PF14"))
        self.assertIn("WARN", sevs(run("The tip settles dead center and then strikes."), "PF14"))

    def test_pf15_not_applied_with_audio_on(self):
        self.assertEqual(sevs(run("Music plays.", audio="on"), "PF15"), set())

    def test_pf20_pf21_variants(self):
        self.assertIn("FAIL", sevs(run("Keep the face as in the source.", kind="edit"), "PF20"))
        self.assertIn("WARN", sevs(run("Change the sky. Keep the face.", kind="edit"), "PF20"))
        self.assertIn("WARN", sevs(run("Change the sky and then remove the car. Keep the face as in the source.", kind="edit"), "PF21"))

    def test_pf23_camera_body(self):
        for t in ("shot on a Canon", "ISO 800", "f/2.8 lens", "shutter 1/250"):
            self.assertIn("WARN", sevs(run("A man, " + t + ".", kind="still"), "PF23"), t)

    def test_pf24_reference_roles(self):
        self.assertIn("INFO", sevs(run("Use image one.", kind="edit"), "PF24"))
        self.assertFalse(sevs(run("Image one is the person.", kind="edit", master="m.png"), "PF24") & {"WARN", "INFO"})

    def test_pf24_is_info_only_and_never_scored(self):
        f = run("Change the sky to dusk. Keep the face as in the source. Image one.", kind="edit")
        self.assertEqual(sevs(f, "PF24"), {"INFO"})
        self.assertNotIn("WARN", {x.sev for x in f})
        self.assertEqual(P.verdict(f), "PASS")
        self.assertIn("[INFO] PF24", P.render({"ID": "t"}, "x", f, "edit", "other"))
        # an ALLOW on an INFO note changes nothing and is not an error
        self.assertEqual(sevs(run("Change the sky to dusk. Keep the face.", kind="edit", allow="PF24"), "PF24"), {"INFO"})

    def test_pf26_negative(self):
        t = "A man on a pickup truck at dusk, film grain."
        f = run(t, kind="still", engine="firefly", negative="text, second wrench")
        self.assertEqual(sevs(f, "PF26"), {"WARN"})
        f = run(t, kind="still", engine="firefly", negative="film grain, text")
        self.assertIn("FAIL", sevs(f, "PF26"))
        f = run("A man holds a second wrench.", kind="still", engine="firefly", negative="second wrench")
        self.assertIn("FAIL", sevs(f, "PF26"))
        f = run("A man holds a wrench.", kind="still", engine="firefly", negative="second wrench")
        self.assertNotIn("FAIL", sevs(f, "PF26"))

    def test_pf29(self):
        self.assertIn("WARN", sevs(run("A hand.", kind="still", reference_type="composition"), "PF29"))
        self.assertEqual(sevs(run("A hand.", kind="still", reference_type="style"), "PF29"), set())

    def test_pf27_context_added_to_r1_on_video_only(self):
        v = [f for f in run("No hat. Static camera.") if f.rule == "R1"][0]
        s = [f for f in run("No hat.", kind="still") if f.rule == "R1"][0]
        self.assertIn("5 of 5 clips", v.detail)
        self.assertNotIn("5 of 5 clips", s.detail)

    def test_pf17_not_double_counted(self):
        f = run("NOTHING IN HIS HAND!!! Static camera.")
        self.assertEqual([x.rule for x in f if x.rule == "PF17"], [])

    def test_allow_override_prints_overridden(self):
        f = run("He hands the wrench to a man. Static camera.", allow="PF04")
        self.assertEqual(sevs(f, "PF04"), {"OVERRIDDEN"})
        code, out = cli(["--text", "He hands the wrench to a man. Static camera.", "--kind", "video", "--engine", "other",
                         "--allow", "PF04", "--quiet"])
        self.assertIn("[OVERRIDDEN] PF04", out)

    def test_overridden_does_not_count_as_fail(self):
        f = run("A man walks. Static camera. He hands the wrench to a man.", allow="PF04")
        self.assertNotIn("PF04", failed(f))


class History(unittest.TestCase):
    def hist(self, n, text="Static camera. A man walks."):
        return [{"shot": "S1", "attempt": i + 1, "date": "2026-11-24", "text": text} for i in range(n)]

    def test_three_earlier_tries_fail(self):
        self.assertIn("FAIL", sevs(run("Static camera. A man runs.", shot="S1", history=self.hist(3)), "PF07"))

    def test_same_words_warn(self):
        f = run("Static camera. A man walks.", shot="S1", history=self.hist(2))
        self.assertEqual(sevs(f, "PF07"), {"WARN"})

    def test_new_words_one_earlier_is_quiet(self):
        f = run("Static camera. A man runs.", shot="S1", history=self.hist(1))
        self.assertEqual(sevs(f, "PF07"), {"PASS"})

    def test_other_shot_not_counted(self):
        self.assertEqual(sevs(run("x. Static camera.", shot="S2", history=self.hist(3)), "PF07"), {"PASS"})

    def test_stacked_changes_warn(self):
        old = self.hist(1, "Static camera. A man walks. He waves. He sits. It rains.")
        f = run("Dolly in. A woman runs. She nods. She stands. It snows.", shot="S1", history=old)
        self.assertEqual(sevs(f, "PF08"), {"WARN"})
        f = run("Static camera. A man walks. He waves. He sits. It snows.", shot="S1", history=old)
        self.assertEqual(sevs(f, "PF08"), {"PASS"})

    def test_no_history_means_not_applicable(self):
        f = run("Static camera. A man walks.", shot="S1")
        self.assertEqual(sevs(f, "PF07"), set())

    def test_record_appends_and_numbers_tries(self):
        p = os.path.join(SCRATCH, "hist-record.jsonl")
        if os.path.exists(p):
            os.remove(p)
        for _ in range(2):
            cli(["--text", "Static camera. A man walks.", "--kind", "video", "--shot", "S9", "--history", p, "--record"])
        rows = [json.loads(l) for l in open(p, encoding="utf-8")]
        self.assertEqual([r["attempt"] for r in rows], [1, 2])
        self.assertEqual(set(rows[0]), {"shot", "attempt", "date", "text"})
        code, out = cli(["--text", "Static camera. A man walks.", "--kind", "video", "--shot", "S9", "--history", p])
        self.assertIn("same words as the last try", out)

    def test_record_without_history_is_usage_error(self):
        self.assertEqual(cli(["--text", "x", "--record"])[0], 2)


class Settings(unittest.TestCase):
    def tpl(self):
        return open(os.path.join(P.LINT_DIR, "SETTINGS-TEMPLATE.txt"), encoding="utf-8").read()

    def write(self, name, text):
        p = os.path.join(SCRATCH, name)
        open(p, "w", encoding="utf-8").write(text)
        return p

    def test_blank_template_passes(self):
        self.assertEqual({f.sev for f in P.check_settings(self.write("s-ok.txt", self.tpl()))}, {"PASS"})

    def test_missing_field_fails(self):
        t = self.tpl().replace("SEED SHOWN:\n", "")
        f = P.check_settings(self.write("s-miss.txt", t))
        self.assertEqual(f[0].sev, "FAIL")
        self.assertIn("SEED SHOWN", f[0].detail)

    def test_credit_digits_without_engine_readout_warns(self):
        t = re.sub(r"(CREDIT READOUT BEFORE CLICK[^\n]*:)", r"\1 120", self.tpl())
        f = P.check_settings(self.write("s-credit.txt", t))
        self.assertEqual(f[0].sev, "WARN")
        t2 = t.replace("ENGINE AS SHOWN:", "ENGINE AS SHOWN: Veo 3.1 Fast")
        self.assertEqual(P.check_settings(self.write("s-credit2.txt", t2))[0].sev, "PASS")

    def test_real_ian_settings_files(self):
        for d in ("R3b", "H1", "B1", "W1"):
            p = os.path.join(ROOT, "data", "firefly-prompt-log", "ian-" + d, "settings.txt")
            self.assertEqual({f.sev for f in P.check_settings(p)}, {"PASS"}, d)

    def test_cli_settings(self):
        p = self.write("s-cli.txt", self.tpl().replace("SEED SHOWN:\n", ""))
        self.assertEqual(cli(["--settings", p])[0], 1)
        self.assertEqual(cli(["--settings", os.path.join(SCRATCH, "nope.txt")])[0], 2)


class Cli(unittest.TestCase):
    def test_exit_codes(self):
        self.assertEqual(cli(["--text", "A man walks. No hat. Static camera.", "--kind", "video", "--engine", "veo"])[0], 1)
        self.assertEqual(cli(["--text", "A man stands in a field at dusk, film grain.", "--kind", "still"])[0], 0)
        self.assertEqual(cli([])[0], 2)
        self.assertEqual(cli(["--bogus"])[0], 2)
        self.assertEqual(cli([os.path.join(SCRATCH, "nope.md")])[0], 2)

    def test_exit_code_in_a_real_process(self):
        r = subprocess.run([PY, os.path.join(PF, "preflight.py"), "--text", "No hat. Static camera.", "--kind", "video"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("VERDICT: FAIL", r.stdout)

    def test_stdin(self):
        code, out = cli(["-", "--kind", "still"], stdin="A man stands in a field at dusk.")
        self.assertEqual(code, 0)
        self.assertIn("VERDICT: PASS", out)

    def test_ian_format_txt(self):
        p = os.path.join(ROOT, "data", "firefly-prompt-log", "ian-W1", "prompt.txt")
        code, out = cli([p])
        self.assertIn("PREFLIGHT ian-W1", out)
        self.assertIn("firefly, still", out)
        self.assertIn("a negative field is set", out)   # negative parsed separately, box warning shown

    def test_block_file(self):
        p = os.path.join(FIX, "good", "playbook-PB-edit-pose.md")
        code, out = cli([p])
        self.assertIn("PREFLIGHT PB-edit-pose", out)

    def test_auto_kind_prints_guess(self):
        code, out = cli(["--text", "Static camera. A man walks.", "--kind", "auto"])
        self.assertIn("kind guessed: video", out)
        code, out = cli(["--text", "Change the sky to dusk. Keep the face as in the source.", "--kind", "auto"])
        self.assertIn("kind guessed: edit", out)
        code, out = cli(["--text", "A man stands in a field at dusk.", "--kind", "auto"])
        self.assertIn("kind guessed: still", out)

    def test_checklist_printed_once_for_video_and_hidden_by_flag(self):
        code, out = cli(["--text", "Static camera. A man walks.", "--kind", "video"])
        self.assertEqual(out.count("NINE-POINT START-FRAME CHECK"), 1)
        self.assertIn("12 The geometry", out)
        self.assertIn("RETRY RULE", out)
        self.assertIn("LIMIT: this tool reads words", out)
        code, out = cli(["--text", "Static camera. A man walks.", "--kind", "video", "--no-checklist"])
        self.assertNotIn("NINE-POINT", out)
        code, out = cli(["--text", "A man.", "--kind", "still"])
        self.assertNotIn("NINE-POINT", out)

    def test_quiet_hides_pass_line(self):
        self.assertIn("[PASS]", cli(["--text", "Static camera. A man walks.", "--kind", "video"])[1])
        self.assertNotIn("[PASS]", cli(["--text", "Static camera. A man walks.", "--kind", "video", "--quiet"])[1])

    def test_json(self):
        code, out = cli(["--text", "No hat. Static camera.", "--kind", "video", "--json"])
        data = json.loads(out)
        self.assertEqual(data[0]["verdict"], "FAIL")
        self.assertTrue(any(f["rule"] == "R1" for f in data[0]["findings"]))

    def test_ascii_only_output(self):
        txt = "A man — walks “quietly” é. No hat. Static camera."
        for argv in (["--text", txt, "--kind", "video"], ["--text", txt, "--kind", "video", "--json"], ["--rules"]):
            code, out = cli(argv)
            out.encode("ascii")

    def test_no_em_dash_in_source_files(self):
        for fn in ("rules.py", "checks.py", "preflight.py", "gen_rule_table.py"):
            s = open(os.path.join(PF, fn), encoding="utf-8").read()
            self.assertNotIn("—", s, fn)

    def test_flags_override_block_meta(self):
        p = os.path.join(FIX, "good", "playbook-PB-edit-pose.md")
        code, out = cli([p, "--kind", "edit", "--engine", "firefly"])
        self.assertIn("firefly, edit", out)


class Tables(unittest.TestCase):
    def test_unique_ids_and_required_fields(self):
        ids = [r["id"] for r in R.RULES]
        self.assertEqual(len(ids), len(set(ids)))
        for r in R.RULES:
            for k in ("id", "name", "severity", "tag", "kinds", "applies", "evidence", "sources", "fix", "why", "quotes"):
                self.assertTrue(r[k], "%s has empty %s" % (r["id"], k))

    def test_every_source_file_exists(self):
        for r in R.RULES:
            for s in r["sources"]:
                self.assertTrue(os.path.exists(os.path.join(R.ROOT, s)), "%s: missing source %s" % (r["id"], s))

    def test_every_quote_is_in_its_file(self):
        norm = lambda s: re.sub(r"\s+", " ", s)
        cache = {}
        for r in R.RULES:
            for f, q in r["quotes"]:
                cache.setdefault(f, norm(open(os.path.join(R.ROOT, f), encoding="utf-8", errors="replace").read()))
                self.assertIn(norm(q), cache[f], "%s: quote not found in %s: %r" % (r["id"], f, q))

    def test_every_check_has_a_rule_row_and_every_emitted_pf_row_has_a_check(self):
        import checks
        for rid in checks.CHECKS:
            self.assertIn(rid, R.RULE_BY_ID)
        for r in R.RULES:
            if r["id"].startswith("PF") and r["emitted"] and r["id"] not in ("PF30", "PF31"):
                self.assertIn(r["id"], checks.CHECKS, r["id"])

    def test_every_finding_id_exists_in_rules(self):
        seen = set()
        for rule, meta, bad, sev, good in CASES:
            for t in (bad, good):
                seen |= {f.rule for f in run(t, **meta)}
        self.assertTrue(seen <= set(R.RULE_BY_ID), seen - set(R.RULE_BY_ID))

    def test_rule_table_md_is_current(self):
        import gen_rule_table
        p = os.path.join(PF, "RULE-TABLE.md")
        self.assertTrue(os.path.exists(p), "run gen_rule_table.py")
        self.assertEqual(open(p, encoding="utf-8").read(), gen_rule_table.build(), "RULE-TABLE.md is stale: run gen_rule_table.py")


class Safety(unittest.TestCase):
    def test_no_network_imports_in_source(self):
        for fn in ("preflight.py", "rules.py", "checks.py", "gen_rule_table.py"):
            s = open(os.path.join(PF, fn), encoding="utf-8").read()
            self.assertIsNone(re.search(r"^\s*(import|from)\s+(socket|urllib|http|requests|ssl|ftplib|smtplib)\b", s, re.M), fn)

    def test_network_modules_not_loaded_at_runtime(self):
        code = ("import sys; sys.path.insert(0, %r); import preflight, rules, checks; "
                "preflight.run_checks('A man walks. Static camera.', {'KIND':'video'});"
                "bad=[m for m in ('socket','urllib','http','requests','ssl') if m in sys.modules]; print(bad)") % PF
        r = subprocess.run([PY, "-c", code], capture_output=True, text=True)
        self.assertEqual(r.stdout.strip(), "[]", r.stdout + r.stderr)

    def test_prompt_lint_unchanged(self):
        want = open(os.path.join(TESTS, "LINT_SHA256.txt")).read().split()[0]
        got = hashlib.sha256(open(os.path.join(P.LINT_DIR, "prompt_lint.py"), "rb").read()).hexdigest()
        self.assertEqual(got, want, "prompt_lint.py CHANGED since the build. If that was on purpose, "
                         "write the new sha256 into tests/LINT_SHA256.txt and re-run the legacy baseline tests.")


class TesterFixes(unittest.TestCase):
    """Fixes from the tester report, 2026-11-24."""
    def tmp(self, name, data=b""):
        p = os.path.join(SCRATCH, name)
        if os.path.isdir(p):
            os.rmdir(p)
        with open(p, "wb") as fh:
            fh.write(data)
        return p

    OK = ["--text", "Static camera. A man walks.", "--kind", "video"]

    # B1
    def test_b1_binary_history_does_not_crash(self):
        p = self.tmp("hist-binary.jsonl", b"\x00\xff\xfe\x80garbage\n" + b'{"shot": "S1", "attempt": 1, "text": "x"}\n' + b"not json\n[1,2]\n")
        code, out = cli(self.OK + ["--shot", "S1", "--history", p])
        self.assertEqual(code, 0)
        self.assertIn("skipped 3 unreadable history lines", out)
        self.assertNotIn("Traceback", out)

    def test_b1_good_history_prints_no_skip_note(self):
        p = self.tmp("hist-good.jsonl", b'{"shot": "S1", "attempt": 1, "text": "x"}\n')
        self.assertNotIn("skipped", cli(self.OK + ["--shot", "S1", "--history", p])[1])

    def test_b1_read_history_counts(self):
        p = self.tmp("hist-count.jsonl", b'{"shot": "A"}\n\n{bad\n')
        rows, skipped = P.read_history(p)
        self.assertEqual((len(rows), skipped), (1, 1))

    # B2
    def test_b2_bad_history_paths_exit_2(self):
        missing = os.path.join(SCRATCH, "no-such-folder", "h.jsonl")
        for extra in (["--record"], []):
            code, out = cli(self.OK + ["--shot", "S1", "--history", missing] + extra)
            self.assertEqual(code, 2, out)
            self.assertIn("folder does not exist", out)
        d = os.path.join(SCRATCH, "a-folder")
        os.makedirs(d, exist_ok=True)
        code, out = cli(self.OK + ["--shot", "S1", "--history", d, "--record"])
        self.assertEqual(code, 2)
        self.assertIn("is a folder", out)

    def test_b2_unwritable_file_exits_2(self):
        p = self.tmp("hist-ro.jsonl", b"")
        import stat
        os.chmod(p, stat.S_IREAD)
        try:
            code, out = cli(self.OK + ["--shot", "S1", "--history", p, "--record"])
        finally:
            os.chmod(p, stat.S_IWRITE | stat.S_IREAD)
        self.assertEqual(code, 2, out)
        self.assertIn("not writable", out)
        self.assertNotIn("Traceback", out)

    # 3
    def test_empty_text_exits_2(self):
        for argv, stdin in ((["--text", ""], None), (["--text", "   \n "], None), (["-"], "  \n")):
            code, out = cli(argv, stdin)
            self.assertEqual(code, 2, argv)
            self.assertIn("no prompt text", out)
            self.assertNotIn("PASS", out)
        p = self.tmp("empty.txt", b"")
        code, out = cli([p])
        self.assertEqual(code, 2)
        self.assertIn("no prompt text", out)

    # 4
    def test_pf31_unknown_kind_and_engine(self):
        f = run("Static camera. A man walks.", kind="vidio", engine="veoo")
        msgs = [x.detail for x in f if x.rule == "PF31"]
        self.assertEqual(len(msgs), 2)
        self.assertTrue(any("KIND" in m and "vidio" in m for m in msgs))
        self.assertTrue(any("ENGINE" in m and "veoo" in m for m in msgs))
        self.assertEqual(P.verdict(f), "WARN")

    def test_pf31_in_a_block_file_is_visible(self):
        p = self.tmp("typo.md", b"```prompt\nID: T1\nKIND: vidio\nENGINE: veoo\n---\nStatic camera. A man walks.\n```\n")
        code, out = cli([p])
        self.assertIn("[WARN] PF31", out)
        self.assertIn("unknown KIND value 'vidio'", out)
        self.assertEqual(code, 0)

    def test_pf31_valid_values_are_quiet(self):
        self.assertEqual(sevs(run("Static camera. A man walks."), "PF31"), set())

    def test_pf31_unknown_allow_id_warns_exit_by_verdict(self):
        code, out = cli(self.OK + ["--allow", "PF99"])
        self.assertIn("unknown rule id in ALLOW", out)
        self.assertEqual(code, 0)
        code, out = cli(["--text", "No hat. Static camera.", "--kind", "video", "--allow", "PF99"])
        self.assertIn("unknown rule id in ALLOW", out)
        self.assertEqual(code, 1)
        f = run("Static camera. A man walks.", allow="PF04")      # a real id is fine
        self.assertEqual(sevs(f, "PF31"), set())

    # 5
    def test_md_without_blocks_prints_note(self):
        p = self.tmp("plain.md", b"Static camera. A man walks.\n")
        code, out = cli([p, "--kind", "video"])
        self.assertIn("no prompt blocks found, treating the whole file as one prompt", out)

    def test_header_without_dashes_is_noted_not_linted(self):
        p = self.tmp("nodash.md", b"```prompt\nID: ND\nKIND: video\nENGINE: veo\nStatic camera. A man walks.\n```\n")
        code, out = cli([p])
        self.assertIn("no line with only ---", out)
        self.assertIn("PREFLIGHT ND  (veo, video, 5 words", out)

    # 6
    def test_record_blocked_on_fail_unless_anyway(self):
        p = os.path.join(SCRATCH, "hist-fail.jsonl")
        if os.path.exists(p):
            os.remove(p)
        bad = ["--text", "No hat. Static camera.", "--kind", "video", "--shot", "F1", "--history", p, "--record"]
        code, out = cli(bad)
        self.assertEqual(code, 1)
        self.assertIn("not recorded: verdict FAIL", out)
        self.assertFalse(os.path.exists(p))
        code, out = cli(bad + ["--record-anyway"])
        self.assertEqual(len(open(p, encoding="utf-8").read().splitlines()), 1)
        good = ["--text", "Static camera. A man walks.", "--kind", "video", "--shot", "F1", "--history", p, "--record"]
        cli(good)
        self.assertEqual(len(open(p, encoding="utf-8").read().splitlines()), 2)

    # 7
    def test_pf09_narrowed(self):
        for ok in ("She writes a letter to her mother.", "The man sends a text message to his wife.",
                   "He folds the letter and puts it away.", "A long text about nothing.",
                   "A dinner plate sits on the table.", "He reads a book by the window.",
                   "A letter on the table.", "The sign reads open.", "Letters on the wall.", "A plate on the car.",
                   "A text on the phone screen."):
            self.assertEqual(sevs(run(ok, kind="still"), "PF09"), {"PASS"}, ok)
        for bad in ("A logo on the shield.", "Gold lettering on the door.", "A blank license plate.", "A number plate.",
                    "The numerals 12.", "A wordmark glows.", "A title card appears.", "The words fade in.",
                    "Text reading Joust.", "text that says hello", "Text saying hello", "Letters spelling WOLF.",
                    "The emblem painted on the shield.", "A shield with a wolf emblem."):
            self.assertEqual(sevs(run(bad, kind="still"), "PF09"), {"WARN"}, bad)

    def test_pf09_joust_emblem_no_start_frame_still_fails(self):
        t = "Static camera. A battered wooden shield stands on a post, the emblem painted on its face, centered and readable."
        self.assertEqual(sevs(run(t, start_frame="no"), "PF09"), {"FAIL"})
        self.assertEqual(sevs(run(t, start_frame="yes"), "PF09"), {"WARN"})


if __name__ == "__main__":
    unittest.main()
