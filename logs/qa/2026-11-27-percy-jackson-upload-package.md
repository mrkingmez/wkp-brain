# QA: Percy Jackson S3 E1 and 2 Upload Package, 2026-11-27

Verdict: FAIL on one fix (docx rebuild). Everything else PASS or PASS WITH NOTES. After the docx is rebuilt, the package is PASS WITH NOTES.
Benches: qa-documents, qa-claims, qa-media. Nothing edited. Visual page render NOT AVAILABLE (no LibreOffice or soffice installed). Drive N: not mounted, so "no Drive copy" is not verified.

## Blocker
B1. docx: 24 paragraphs holding a single backtick, one before and one after each of the 12 paste blocks (md code fences leaked). Breaks "docx matches md, print-ready" and risks a backtick landing in the YouTube title, description or tags. Fix: rebuild the docx without fence characters, paste blocks as plain monospace paragraphs. Also copy the rebuilt file to the movie folder (the two copies are byte-identical today, md5 f62644f7...).

## Notes (none block)
N1. docx "IN THIS REVIEW" list became Word bullets, the md has "- " hyphen lines inside the description paste block. Pasting gives bullet glyphs. Rebuild with literal "- " text.
N2. Gate 1: script-room was not launched, copy went copywriting, social-media, graphic-design via marketing-director, slop_check exit 0 on all three files, judgment pass done. Copywriting sits inside the writing room (org change 2026-10-29), so I accept it as the gate. The package states the skip openly. The pinned-correction notes say script-room wrote it, the package header says script-room not launched: make the two statements agree.
N3. Pinned-Correction-DRAFT short version (404 chars) says flatly "The card game is Mythomagic, not Magic: The Gathering". Facts-Refresh section 5 says what the episodes show is NOT RETRIEVED. Package Section 8.4 repeats it unhedged. Hedge or drop before Zac pins. "Atlas is the General, Bane of Olympus is separate" rests on a LIKELY WRONG, medium confidence row.
N4. Pinned-Correction-DRAFT.md line 38 says "slop_check result below", nothing below. I ran it, exit 0.
N5. Chapter check line, 29:18 quote ("what does Annabeth do... you kept us safe") is not verbatim. The transcript reads "what is an about do". Chapter lands about 2.4 s before that line, within 1 to 2 s tolerance of the block start. Fix the quote description.
N6. Facebook V2 slot "weekday evening about 7 PM" is not in the Facebook table in post-times.md. Say it is a judgment slot, not a researched one. Whether the locked shorts cadence in root CLAUDE.md covers review shorts is unclear; the package uses the post-times table. Zac or Jarvis to rule.
N7. The Next Up card in v8 is the generic "NEW REVIEW, COMING TO THE DEN". The package says so. TASKS says Percy Jackson was the next-up after A Knight's Tale, not after this review, so generic is right. Open item: next review NOT KNOWN.
N8. End card boxes are empty placeholders: Zac places the end-screen elements in Studio. Card 3 (EP 122), both playlist IDs: NOT KNOWN, allowed. Inventory pull 25 days old (35 views stale).
N9. Package's own open flags still block upload and are Zac's: music origin of Tide of Heroes (Flag 2), AI box (3), CC BY credit block (4), C01 corner mark (5), nobody has listened to v8.
N10. qa-media did not check the two clips (7.00 and 8.00 s) in the file or run a whole-file logo scan. qa-claims confirmed 210 and 240 frames in the plan, 15.0 s, 0.80 percent. Frame check of platform bugs is only on six frames.
N11. Chapter 00:08:01 times: all 13 within 1 s of my rebuilt map. "Journey" in a chapter title is the hosts' topic, not slop.

## Verified (retrieved)
- v8 ffprobe: H.264 High, 1920x1080, 30 fps, AAC 48 kHz stereo, 1882.467 s, 56,474 frames; v7 is 1.000 s longer.
- v8 loudness measured by qa-media: -14.0 LUFS, true peak -1.3 dBFS (first independent measure, package had not re-measured).
- Next Up 1864.467 to 1870.467 and end card 1870.467 to 1882.467 (12.0 s, fades out, no black tail). No black over 0.5 s, no silence, no picture over 5.8 s in the body.
- Tags 454 by len(), 23 tags; titles 47 and 53; hashtags exactly 5 and same in description; description block 4,759 chars; fair use last; section order correct; 3 cards all before 3:00; card IDs txYiPEe2Axc (35 views) and YWRdI5A_cdw match VIDEO-LIBRARY and inventory; EP 122 matches PROJECT-BOARD; cast pairs match Facts-Refresh; picture counts sum to 35; no em dashes in md, docx, copy files; slop_check exit 0; no verdict stated; no on-air error repeated as fact in public copy.

Lessons file append (memory\agents\qa-director.md) not done: this agent has no edit tool. Lesson for Jarvis to add: docx built from md can leak code-fence backticks, grep the docx paragraphs for a lone backtick on every package.
