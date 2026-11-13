# EP120 shorts copy, copywriting desk brief (script-room, GENERATE, public copy, pass 1)

Source brief (hard rules, 23 clips, ranges): D:\WKP\scratch\ep120-shorts-brief.md  READ IT FIRST, all rules apply.
Transcript (only source of truth): L:\Winter Wolfs Den review show\Frost-Cast\EP 120\James Gunn is James GONE _ FrostCast Episode 120_transcript.txt
Show Prep facts (official/reported/rumor labels): D:\WKP\WWD\reports\FrostCast-EP120-Show-Prep.md
Format to match exactly: D:\WKP\WWD\opusclip\EP119-approved-copy.json
  - {"clips":[{id,title,description,youtube{title,description},instagram{description},facebook{description},spoiler}]}
  - top-level description == youtube.description, top-level title == youtube.title
  - YouTube 5 hashtags (no channel-branded tags, no #FrostCast, never #WinterWolfsDen), Instagram 5, Facebook 2, at the end after a blank line (\n\n)
  - spoiler=true clips open with "SPOILER WARNING: ..." (YouTube/top), "Spoiler warning: ..." (IG/FB), see EP119 clip 1Lts0AC0DH

Outputs:
  1. D:\WKP\scratch\ep120-copy-draft.json  (valid JSON, 23 clips, brief order, brief ids)
  2. D:\WKP\Post-Production\writing-room\ep120-shorts\claims-table.md : one row per clip, each factual claim in the copy, the transcript timestamp that supports it (must be INSIDE that clip's range), or Show Prep OBSERVED section. No claim without a row.

Writing rules: no em dashes, nothing generic, no AI-tell phrases, YouTube title is the hook (under 100 chars), different copy on all three platforms, lead with question/fight/surprise, never hand over the answer. Handles KingZ and Oracle only. No viewer names, no poll numbers, no numeric scores. Rumor labeled rumor, news labeled as reported. Do not state the clips' verdicts as fact, attribute opinions to KingZ or Oracle. Respectful, no hype on the Veterans Day clips. No service-as-credibility hook, never call the channel veteran-owned. Do not quote lines of existing films or shows (clearance hard fail).

Pre-read traps (showrunner checked the transcript, obey these):
- Clip 20 (41:38-42:15): range only holds Oracle saw Jimmy and enjoyed it, KingZ says it was a fantastic movie, KJ Apa plays the lead, and a Vision Quest aside (no spoilers). The "voice" praise is at 43:22 and the review scores at 43:54, OUTSIDE the range. Do NOT claim the voice or any score. Keep copy to what is in range and say so in the claims table.
- Clip 23 (24:50-25:50): last seconds (25:30-25:50) include a line about a host's real military service and the first words of clip 13's material. Do not use them in clip 23. Palpatine/Rise of Skywalker content is spoiler, flag accordingly.
- Clip 22: Driver said it on the Rich Eisen show per KingZ (Show Prep: his own words, The Direct). Mr. Sinister casting is "reported". Do not claim Disney's reason, the Hunt for Ben Solo title, or any Iger/Bergman detail (not said in range).
- Clip 11: do not quote the Family Guy line. Do not use the chat comment about The Rock.
- Clip 12: range never names the show in so many words. Band of Brothers is inferred from context (56:03 and 57:03 name it, brief title names it). Do not quote the scene's dialogue, describe the bit in your own words. Note the inference in the claims table.
- Clip 8: do not mention the concert drop-in (4:11-4:32), the speaker is not named there. Gorilla Grodd title is garbled in the transcript ("Gorilla Grog"), use the Show Prep spelling (The People v. Gorilla Grodd).
- Clip 7: the new boss name is garbled in the transcript, use "a Marvel producer" or Show Prep "Latcham" only if needed. Do not name Paige or any chat viewer.
- Clip 21: write it about families and the question of space, third person. Do not attribute private feelings to Chris Kyle.
- Clip 19: do not state who dies, keep spoiler false, hook is the question and the answer being in the title.
- Clip 4: height numbers are what was said (comic Wolverine 5'3", White 5'7", four inches). Rumor label stays.
- Clips 3 and 4: Jeremy Allen White Wolverine is rumor, one newsletter source, say so. No Marvel comment exists.
- Clip 9: speculation only, DC Studios on the selling block is "just rumor and speculation" per KingZ at 10:01.
- Clip 15: opinion only, attribute to KingZ, do not say the AV Club or AI complaints, do not claim anything about the film's accuracy.

Do not call marketing-director or no-ai-slop, script-room does the room checks after you and the caller runs those next. Return: draft path, claims-table path, any clip where you changed the angle or refused something, and a one-line list of things you were unsure of.
