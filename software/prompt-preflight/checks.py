"""The new PF rule checks, one small function each. Pure text, stdlib only, no network.

Every check takes a Ctx and returns None (rule does not apply to this prompt) or a list of
(severity, detail) tuples (empty list = applies and passed). Severity is "FAIL" or "WARN" (PF24 alone returns "INFO": a note, never scored).
Rule text, evidence and fixes live in rules.py, not here.
"""
import re

VIDEO_ENGINES = ("veo", "kling", "seedance", "runway", "luma", "flux")


class Ctx:
    def __init__(self, text, kind, engine, start, end, audio, master, ref_type, shot, negative, history, end_file=None):
        self.text, self.kind, self.engine = text, kind, engine
        self.start, self.end, self.audio = start, end, audio
        self.master, self.ref_type, self.shot = master, ref_type, shot
        self.negative, self.history = negative, history
        self.end_file = end_file


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", t) if s.strip()]


def _uniq(items, n=6):
    seen = []
    for i in items:
        i = i.strip()
        if i.lower() not in [s.lower() for s in seen]:
            seen.append(i)
    extra = len(seen) - n
    out = ", ".join("'%s'" % s for s in seen[:n])
    return out + (" (+%d more)" % extra if extra > 0 else "")


# ---------------------------------------------------------------- PF01
_SIDE_SKIP = re.compile(r"\b(all right|right (now|away|after|before))\b", re.I)
_SIDE = re.compile(r"\b(leftmost|rightmost|left|right)\b|\bnearest (the )?camera\b|\bfarthest (from )?(the )?camera\b", re.I)


# Camera-relative or screen-relative wording is the safe way to say a side (the rule's own fix), so it is removed
# before the check. Only side words left over after that (bare left/right, or leftmost/rightmost) fire the rule.
_SIDE_CAMREL = re.compile(
    r"\b(camera|screen|frame)[- ](left|right)\b|\b(left|right) of (the )?(frame|screen)\b"
    r"|\bnearest (the )?camera\b|\bfarthest (from )?(the )?camera\b", re.I)


def pf01(c):
    rest = _SIDE_CAMREL.sub(" ", _SIDE_SKIP.sub(" ", c.text))
    hits = [m.group(0) for m in _SIDE.finditer(rest)]
    if not hits:
        return []
    msg = "side words %s" % _uniq(hits)
    if c.kind == "video" and c.start == "yes":
        msg += " (start frame is yes: remove them from the text, the picture decides)"
    return [("WARN", msg)]


# ---------------------------------------------------------------- PF02
_TOOL = re.compile(r"\b(wrench|ratchet|socket|hammer|screwdriver|lance|sword|tool)s?\b", re.I)
_HANDS = re.compile(r"\b(hands?|forearms?)\b", re.I)
_HAND_QUAL = re.compile(
    r"\b(left|right|one|other|both|each)\s+(hand|hands|forearm|forearms|arm|arms)\b"
    r"|\b(hand|hands|forearm|forearms|arm|arms)\b[^.,;]{0,20}\b(nearest|farthest|closest)\b", re.I)


def pf02(c):
    t = re.sub(r"\btool wall\b", " ", c.text, flags=re.I)
    tool, hands = _TOOL.search(t), _HANDS.search(t)
    if tool and hands and not _HAND_QUAL.search(t):
        return [("WARN", "tool '%s' and '%s' but no hand named (left, right, nearest, one hand, other hand)" % (tool.group(0), hands.group(0)))]
    return []


# ---------------------------------------------------------------- PF03
_ROLL = re.compile(r"\b(rolls?|rolled|rolling|slides?|slid|sliding|glides?|skids?)\b(?!-up)", re.I)
_DEST = re.compile(r"\b(boot|toe|foot|shoe|wall|door|wheel)s?\b", re.I)


# A last frame counts as planned when END_FRAME is yes, an END_FRAME_FILE header key is filled in, or the text itself
# says 'last frame', 'end frame' or 'final frame' (also 'Image 2 is the last frame'). 'no end frame' / 'without an end
# frame' does not count as planned.
_END_PLANNED = re.compile(r"(?<!\bno )(?<!\bwithout )(?<!\bwithout an )(?<!\bno an )\b(last|end|final) frame\b", re.I)


def end_frame_planned(c):
    f = (c.end_file or "").strip().lower()
    return c.end == "yes" or (f not in ("", "no", "none", "n/a")) or bool(_END_PLANNED.search(c.text))


def pf03(c):
    if end_frame_planned(c):
        return []
    for s in sentences(c.text):
        r, d = _ROLL.search(s), _DEST.search(s)
        if r and d:
            return [("WARN", "'%s' ... '%s': no end frame claimed; if you plan one, write END_FRAME: yes" % (r.group(0), d.group(0)))]
    return []


# ---------------------------------------------------------------- PF04
_HANDOFF = re.compile(
    r"\bhands (it|him|her|them|over|back|off|the|a|an)\b|\bhands (in|out) (a|an|the|him|her|it)\b"
    r"|\b(handing|handed|handoff|hand-off)\b|\bpass(es|ing)\b|\bswap(s|ped|ping)?\b|\bexchang(e|es|ed|ing)\b"
    r"|\boffer(s|ing)\b|\btakes? (the|a|an) [^.]{0,40}\bfrom\b", re.I)


def pf04(c):
    hits = [m.group(0) for m in _HANDOFF.finditer(c.text)]
    return [("FAIL", "handoff or swap words %s" % _uniq(hits))] if hits else []


# ---------------------------------------------------------------- PF05
_PERSON = re.compile(r"\b(someone|somebody|another person)\b", re.I)
_OFFER = re.compile(r"\b(offer\w*|hand\w*|pass\w*|holds? (it |the \w+ )?out|gives?|takes?)\b", re.I)


def pf05(c):
    out, sev_strong = [], ("FAIL" if c.kind == "video" else "WARN")
    for s in sentences(c.text):
        p = _PERSON.search(s)
        if re.search(r"\bas if offering\b", s, re.I) or (p and _OFFER.search(s)) or \
                (re.search(r"\bbeside (him|her)\b", s, re.I) and re.search(r"\b(offer\w*|hand(s|ing|ed)?)\b", s, re.I)):
            out.append((sev_strong, "implied second person in: '%s'" % s[:90]))
        elif p:
            out.append(("WARN", "implied person word '%s'" % p.group(0)))
    return out


# ---------------------------------------------------------------- PF06
_HIDE = re.compile(r"\bout of (the )?(frame|shot)\b|\boff-?screen\b|\bnot visible\b|\bface (is |are )?(hidden|in shadow)\b|\bhidden face\b|\bface[^.]{0,25}\bout of (the )?(frame|shot)\b", re.I)


def pf06(c):
    hits = [m.group(0) for m in _HIDE.finditer(c.text)]
    return [("WARN", "framing by hiding: %s" % _uniq(hits))] if hits else []


# ---------------------------------------------------------------- PF07, PF08 (history)
def _norm(t):
    return re.sub(r"\s+", " ", t.strip().lower())


def _earlier(c):
    if c.history is None or not c.shot:
        return None
    rows = [h for h in c.history if str(h.get("shot", "")).lower() == str(c.shot).lower()]
    rows.sort(key=lambda h: h.get("attempt", 0))
    return rows


def pf07(c):
    rows = _earlier(c)
    if rows is None:
        return None
    if len(rows) >= 3:
        return [("FAIL", "shot %s already tried %d times: redesign the shot, no fourth try" % (c.shot, len(rows)))]
    if rows and _norm(rows[-1].get("text", "")) == _norm(c.text):
        return [("WARN", "same words as the last try of shot %s (%d earlier): same words give the same result" % (c.shot, len(rows)))]
    return []


def _sent_set(t):
    return set(_norm(s) for s in sentences(t))


def pf08(c):
    rows = _earlier(c)
    if rows is None:
        return None
    if not rows:
        return []
    old, new = _sent_set(rows[-1].get("text", "")), _sent_set(c.text)
    n = max(len(new - old), len(old - new))
    if n > 2:
        return [("WARN", "%d sentences added, removed or changed since the last try: stacked changes" % n)]
    return []


# ---------------------------------------------------------------- PF09
# Narrowed 2026-11-24 (tester): bare "text" and "letter(s)" matched ordinary sentences ("a letter on the desk").
# Narrowed again 2026-11-24 (second pass): only real logo or on-screen-text requests. Bare "plate" (dinner plate), "reads"
# (he reads a book), "letter(s)" and "text" in ordinary use do not fire. An emblem fires only when it is painted or on
# something (a shield), which is how the joust prompts asked for a logo.
_EMBLEM = (r"emblems?\b[^.]{0,40}\b(painted|on)\b|\b(painted|on|with)\b[^.]{0,30}\bemblems?"
           r"|emblems?\b[^.]{0,40}\bshield|\bshield\b[^.]{0,40}\bemblems?")
_TEXTY = re.compile(r"\b(logos?|wordmarks?|lettering|licen[cs]e plates?|number plates?|numerals?|title cards?"
                    r"|the words|text\s+(reading|saying|that says)|letters\s+(reading|spelling)|" + _EMBLEM + r")\b", re.I)


def pf09(c):
    hits = [m.group(0) for m in _TEXTY.finditer(c.text)]
    if not hits:
        return []
    sev = "FAIL" if (c.kind == "video" and c.start != "yes") else "WARN"
    return [(sev, "text or logo words %s%s" % (_uniq(hits),
            " with no start frame (the model will redraw it)" if sev == "FAIL" else "; composite it, never a model (R14)"))]


# ---------------------------------------------------------------- PF10
_LANCE = re.compile(r"\blances?\b", re.I)
_ANCHOR = re.compile(r"\b(striped|blunt|rounded|painted|spiral|thick|forearm|wooden pole|round cap)\b", re.I)


def pf10(c):
    out = []
    if re.search(r"\bspears?\b", c.text, re.I):
        out.append(("FAIL", "the word 'spear' names the unwanted thing and gets it drawn"))
    # the shape words must sit in a sentence that names the lance (an emblem "painted" elsewhere does not count)
    lance_sents = [s for s in sentences(c.text) if _LANCE.search(s)]
    if lance_sents and not any(_ANCHOR.search(s) for s in lance_sents):
        out.append(("WARN", "'lance' with no visible shape (striped, blunt, rounded, painted, thick, forearm...)"))
    for w in ("coronal", "three-pronged", "three pronged"):
        if re.search(r"\b%s\b" % w, c.text, re.I):
            out.append(("WARN", "weak anchor word '%s': describe the visible shape" % w))
    return out


# ---------------------------------------------------------------- PF11
_STILLCAM = re.compile(r"\b(locked|static|locked-off)\b", re.I)
_TRAVEL = re.compile(r"\brolls?\b[^.]{0,15}\bout\b|\bsits? up\b|\bstands? up\b|\bcrouch(es|ing)? (in|into)\b|\bcrouch(es|ing)\b", re.I)


def pf11(c):
    s, t = _STILLCAM.search(c.text), _TRAVEL.search(c.text)
    if s and t:
        return [("FAIL", "'%s' camera with big body travel '%s'" % (s.group(0), t.group(0)))]
    return []


# ---------------------------------------------------------------- PF12
_LOWCAM = re.compile(r"\b(floor|ground)[- ]level\b", re.I)
_REACH = re.compile(r"\breach(es|ing)?\b[^.]{0,25}\bin\b|\bpicks? up\b|\bcloses? around\b", re.I)


def pf12(c):
    if _LOWCAM.search(c.text) and _REACH.search(c.text):
        return [("WARN", "floor-level camera plus '%s'" % _REACH.search(c.text).group(0))]
    return []


# ---------------------------------------------------------------- PF13
_PORTAL = re.compile(r"\b(door|gate|lid)\b", re.I)
_LIGHTW = re.compile(r"\b(light|lit|daylight|glow\w*|sun\w*|bright)\b", re.I)
_STATE = re.compile(r"\b(raised|already open|fully open|rests? overhead|rolled up)\b", re.I)


def pf13(c):
    if _STATE.search(c.text):
        return []
    for s in sentences(c.text):
        p, l = _PORTAL.search(s), _LIGHTW.search(s)
        if p and l:
            return [("WARN", "'%s' is a light source with no state phrase (raised, already open, fully open)" % p.group(0))]
    return []


# ---------------------------------------------------------------- PF14
_POINT = re.compile(r"\bat (the )?\d+(\.\d+)?[- ]seconds?( mark)?\b", re.I)


def pf14(c):
    out = []
    for m in _POINT.finditer(c.text):
        if c.engine != "seedance":
            out.append(("FAIL", "point time '%s' (only Seedance documents it)" % m.group(0)))
    if re.search(r"accelerat", c.text, re.I):
        out.append(("FAIL", "'accelerat...' asks for two goals and gets a slow stop"))
    for w in (r"slow[- ]motion", r"\bcreeping\b"):
        m = re.search(w, c.text, re.I)
        if m:
            out.append(("WARN", "'%s' gets the slowness it asks for" % m.group(0)))
    m = re.search(r"\bsettles?\b[^.]*\band then\b", c.text, re.I)
    if m:
        out.append(("WARN", "'settles ... and then' describes a pause before the action"))
    return out


# ---------------------------------------------------------------- PF15
def pf15(c):
    if c.audio == "on":
        return None
    hits = [m.group(0) for m in re.finditer(r"\b(music|dialogue|soundtrack|score)\b", c.text, re.I)]
    return [("WARN", "audio words %s with audio off" % _uniq(hits))] if hits else []


# ---------------------------------------------------------------- PF16
def pf16(c):
    t, out = c.text, []
    t_clean = re.sub(r"\b(e\.g|i\.e|vs|etc|approx|no|fig)\.", "", t, flags=re.I)
    if re.search(r"[.!?]\s+[a-z]", t_clean):
        out.append(("WARN", "a sentence starts in lowercase after a full stop"))
    if re.search(r"\.\s+\.", t):
        out.append(("WARN", "'. .' double full stop"))
    if t.count('"') % 2 or t.count("(") != t.count(")") or t.count("[") != t.count("]"):
        out.append(("WARN", "unbalanced quote or bracket"))
    n = len(re.findall(r"[A-Za-z0-9'\-]+", t))
    if n > 40 and not re.search(r"[.!?]", t):
        out.append(("WARN", "over 40 words with no sentence-ending punctuation"))
    if out:
        out[0] = (out[0][0], out[0][1] + " (this check cannot find typos, no dictionary)")
    return out


# ---------------------------------------------------------------- PF20 to PF22 (edit prompts)
_CV = r"(change|replace|swap|fix|make|edit|relight|remove|add|straighten|match|soften|sharpen)"
_CHANGE_START = re.compile(r"^\s*" + _CV + r"\b", re.I)
_KEEP_START = re.compile(r"^\s*keep\b", re.I)
_KEEP_ANY = re.compile(r"\bkeep\b[^.]*\bas in the source\b", re.I)
_JOINED = re.compile(r"\b" + _CV + r"\b[^.]*\b(and|then|also)\s+" + _CV + r"\b", re.I)


def pf20(c):
    ss = sentences(c.text)
    changes = [s for s in ss if _CHANGE_START.match(s)]
    keeps = [s for s in ss if _KEEP_START.match(s) or _KEEP_ANY.search(s)]
    out = []
    if not changes:
        out.append(("FAIL", "no change line (start a sentence with Change, Replace, Swap, Fix, Make, Relight, Remove, Add...)"))
    if not keeps:
        out.append(("FAIL", "no keep line (a sentence starting 'Keep ... as in the source')"))
    elif not any(re.search(r"\bas in the source\b", s, re.I) for s in keeps):
        out.append(("WARN", "keep line without 'as in the source'"))
    return out


def pf21(c):
    ss = sentences(c.text)
    changes = [s for s in ss if _CHANGE_START.match(s)]
    out = []
    if len(changes) > 1:
        out.append(("FAIL", "%d sentences start with a change verb: one change per pass" % len(changes)))
    for s in changes:
        if _JOINED.search(s):
            m = re.search(r"\b(and|then|also)\s+" + _CV + r"\b", s, re.I)
            out.append(("WARN", "two change verbs joined by '%s'" % m.group(0)))
            break
    return out


def pf22(c):
    hits = [m.group(0) for m in re.finditer(r"\b(do not change|don't change|without changing|never change)\b", c.text, re.I)]
    return [("FAIL", "'%s': write 'keep X as in the source'" % hits[0])] if hits else []


# ---------------------------------------------------------------- PF23
_QUALITY = re.compile(r"\b(4k|8k|uhd|hdr|10-bit|premium|masterpiece|award-winning|best quality|highly detailed|ultra detailed|ultra realistic|professional)\b", re.I)
_BODY = re.compile(r"\b(canon|sony|nikon|arri|alexa|red epic|leica|hasselblad|gopro)\b|\biso\s*\d{2,5}\b|\bf/\d(\.\d)?\b|\b1/\d{2,4}\b", re.I)


def pf23(c):
    out = []
    q = set(m.group(0).lower() for m in _QUALITY.finditer(c.text))
    if len(q) >= 3:
        out.append(("WARN", "quality stack %s" % _uniq(sorted(q))))
    b = [m.group(0) for m in _BODY.finditer(c.text)]
    if b:
        out.append(("WARN", "camera body or exposure spec %s" % _uniq(b)))
    return out


# ---------------------------------------------------------------- PF24
_REFWORD = re.compile(r"\b(image (one|two|three|\d)|@image\d|reference image)\b", re.I)
_ROLEW = re.compile(r"\b(person|room|style|composition|first frame|last frame|character|product|place|master)\b", re.I)


def pf24(c):
    out = []
    if (c.kind == "edit" or (c.kind == "video" and c.start == "yes")) and not c.master \
            and not re.search(r"\bas in the (source|first frame)\b", c.text, re.I):
        out.append(("INFO", "no master named (MASTER: header or --master) and no 'as in the source' or 'as in the first frame'"))
    for s in sentences(c.text):
        if _REFWORD.search(s) and not _ROLEW.search(s):
            out.append(("INFO", "reference words with no role in: '%s'" % s[:80]))
            break
    return out


# ---------------------------------------------------------------- PF25
def pf25(c):
    if not (c.kind == "still" and c.engine == "firefly"):
        return None
    n = len(c.text.strip())
    if n > 750:
        return [("WARN", "%d characters, over 750; the panel limit is not verified" % n)]
    return []


# ---------------------------------------------------------------- PF26
def _neg_terms(neg):
    return [x.strip() for x in re.split(r"[,\n]", neg or "") if x.strip()]


def pf26(c):
    if not c.negative:
        return None
    out = []
    if c.kind == "still" and c.engine == "firefly":
        out.append(("WARN", "a negative field is set: the box is not verified, the run must not depend on it"))
    for term in _neg_terms(c.negative):
        pat = r"\b" + r"\s+".join(re.escape(w) for w in term.split()) + r"\b"
        if re.search(pat, c.text, re.I):
            out.append(("FAIL", "negative term '%s' also appears in the main prompt" % term))
    return out


# ---------------------------------------------------------------- PF28
def pf28(c):
    if c.engine != "kling" or c.kind != "video":
        return None
    out = []
    if c.start == "yes" and not re.search(r"use @image1 as the first frame", c.text, re.I):
        out.append(("WARN", "start frame yes but no 'Use @Image1 as the first frame'"))
    if not re.search(r"single shot", c.text, re.I):
        out.append(("WARN", "no 'single shot' (Kling 4.0 defaults to multi-shot)"))
    return out


# ---------------------------------------------------------------- PF29
def pf29(c):
    if c.kind == "still" and (c.ref_type or "").lower() == "composition":
        return [("WARN", "reference type composition carries everything in the reference, wrong content included")]
    return None


CHECKS = {
    "PF01": pf01, "PF02": pf02, "PF03": pf03, "PF04": pf04, "PF05": pf05, "PF06": pf06, "PF07": pf07,
    "PF08": pf08, "PF09": pf09, "PF10": pf10, "PF11": pf11, "PF12": pf12, "PF13": pf13, "PF14": pf14,
    "PF15": pf15, "PF16": pf16, "PF20": pf20, "PF21": pf21, "PF22": pf22, "PF23": pf23, "PF24": pf24,
    "PF25": pf25, "PF26": pf26, "PF28": pf28, "PF29": pf29,
}
