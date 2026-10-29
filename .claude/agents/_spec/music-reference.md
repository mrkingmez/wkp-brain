# WWD Music Reference

Working knowledge for the `music` bench. Update every job. Each entry: finding, source, date, how sure. Created 2026-10-26.

## House rules (from WWD/CLAUDE.md, Zac)
- Music is intro and outro only. No beds under the talk (locked 2026-10-17).
- Match the movie's tone. No comedy cues over heavy scenes.
- Owned library first: `P:\Sounds\Music\` (index: `D:\WKP\data\assets\p-drive-index.csv`).

## Suno: where things go (community guides, 2026-10-26, not official docs)
- **Style box:** genre, mood, instruments, vocal type, tempo as comma-separated descriptors.
  What the whole track should sound like goes here.
- **Lyrics box:** words and section tags. For an instrumental, use tags only (examples: [Intro], [Build], [Outro]) and no words, or stray "ghost" vocals can appear. Use Instrumental mode for true instrumentals.
- **Exclude Styles box:** keep to 1 to 3 closely related exclusions. Pair each with a positive replacement in the Style box, or the removed role sits empty. Exclusions are guidance, not a guarantee. Check that the positive prompt is not asking for what you exclude.
- **Order matters:** the first few words of the Style box carry more weight. Put the main genre or mood first.
- **BPM:** write it as a number. Skip vague praise words ("professional", "amazing").
- **Length of prompt:** sources conflict. 4 to 8 descriptors or under about 100 words is the common range. Test, do not trust one number.
- **Sliders:** Style Influence and Audio Influence control how tightly it follows. Use them in place of piling on adjectives.
- **Endings:** tags like [Outro], [Fade Out], [End] help it stop instead of running on.
- **Attempts:** expect several generations per good result (community data suggests around 5 or 6).
- **Artist names:** sources conflict on whether Suno allows or restricts them. Our rule: never prompt for a living artist or a named song, whatever Suno allows.
- **Versions change fast.** Sources named v5.5 and a v6 family. Check the interface in front of Zac before trusting a menu name.
Sources: learnprompting.org/blog/guide-suno, roo.beehiiv.com Suno guides, jackrighteous.com guides on where to put a prompt and negative prompting, suno.com/hub/how-to-make-a-song (the only official page found). Confidence: medium, mostly third-party.

## Suno rights (third-party summaries of Suno's terms, verify against suno.com before relying)
- Paid plan (Pro, Premier): commercial-use rights on output made while subscribed. Free (Basic): non-commercial. A later subscription does not reach back to older free-tier songs by default.
- Commercial rights are not copyright. Suno makes no warranty that copyright vests in output, and no indemnity.
- Content ID can still flag AI music. Keep proof: plan status, download records, creation dates.
- YouTube Partner Program rules apply separately (reused or repetitive content).
- Litigation is ongoing between labels and Suno (one label settled with a license deal, 2025-11-25). Watch it.
- **Zac's plan has lapsed (2026-10-26).** No Suno track is commercially clear until he renews.
Sources: terms.law/ai-output-rights/suno, suno.com/hub/copyright-free-music, dynamoi.com, jackrighteous.com monetization guide. Confidence: medium.

## Horror and dark-ambient scoring (starting notes, to be researched further)
- Not yet researched beyond generic Suno guides. First job: search dark ambient, horror score technique, and tension building, then fill this section with tested descriptors per mood (haunted, dread, body horror, carnival, sci-fi cold).
- Instrument and texture words to test: sustained cello, bowed piano, detuned music box, choir pads, granular swell, sub drone, glass harmonica, tape warble. Mark each "untested" until Zac auditions a result.

## Intro and outro craft (to research and fill)
- Intro hook inside 5 seconds. Outro resolves clean, no hard cut at the host's last word.

## Owned library notes (from file names, not heard)
- `bcc-031814-slow-and-somber-haunted-piano-notes-157.mp3`: haunted piano. Copied to `P:\WWD Kit\Clayface\Sounds\` 2026-10-26 as the Clayface pick.
- `bcc-031814-eerie-ghosts-175.mp3`, `jdi-0414-eb-min-sad-cinematic-piano.mp3`, `bbc-051117-Horror-Film-Opening.mp3`, `short-horror-sting-build-up_MyTehEEu.mp3`: candidates.
- Adobe pack: `P:\Sounds\Music\adobe\Ambient\Chamber_Strings_60BPM\`, `...\Choir_Emin_160BPM\`.

## Learning log
- 2026-10-26: reference created from three web searches. Next: horror scoring research, the YouTube Audio Library filters, and a first audit with ffprobe and ebur128 of every track in the owned library.
