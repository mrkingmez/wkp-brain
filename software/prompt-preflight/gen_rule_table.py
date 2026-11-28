#!/usr/bin/env python
"""Writes RULE-TABLE.md from rules.py, so the docs cannot drift from the code.
Run: python gen_rule_table.py   (the unit tests fail if RULE-TABLE.md is stale)."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rules as R   # noqa: E402


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def build():
    out = ["# RULE TABLE (generated from rules.py by gen_rule_table.py, do not edit by hand)", "",
           "Severity says the worst result a rule can give. Tags: PROVEN = seen on Zac's clips (count in the evidence), "
           "PROPOSED = our rule, not yet tested, UNTESTED = no failure of ours logged, SOURCED = a maker page says it.",
           "R1 to R13 are the ids printed by `prompt_lint.py`. They are NOT the same numbers as STANDARD.md past R4 "
           "(see the standard_ref column). PF ids are new.", "",
           "Evidence quotes are checked against the named files by the unit tests (`test_every_quote_is_in_its_file`).", ""]
    out.append("| Id | Name | Severity | Tag | Applies | STANDARD ref | Fix | Emitted |")
    out.append("|---|---|---|---|---|---|---|---|")
    for r in R.RULES:
        out.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["id"], cell(r["name"]), cell(r["severity"]), cell(r["tag"]), cell(r["applies"]),
            cell(r["standard_ref"] or "-"), cell(r["fix"]), "yes" if r["emitted"] else "no (folded into another rule)"))
    out += ["", "## Evidence per rule", ""]
    for r in R.RULES:
        out.append("### %s  %s" % (r["id"], r["name"]))
        out.append("- Evidence: " + r["evidence"])
        out.append("- Evidence status: " + r["evidence_status"])
        out.append("- Source files: " + "; ".join("`%s`" % s for s in r["sources"]))
        out.append("- Why (plain words): " + r["why"])
        out.append("")
    out += ["## Info printed for every video prompt (not scored)", ""]
    out += ["- " + p for p in R.NINE_POINTS + R.EXTRA_POINTS]
    out += ["- " + R.RETRY_RULE, "", R.LIMIT, ""]
    return "\n".join(out)


if __name__ == "__main__":
    with open(os.path.join(HERE, "RULE-TABLE.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build())
    print("wrote RULE-TABLE.md (%d rules)" % len(R.RULES))
