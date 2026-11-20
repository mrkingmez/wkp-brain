# WWD Music Reference

Working knowledge for the `music` bench. Update every job. Each entry: finding, source, date, how sure. Created 2026-10-26.

## House rules (from WWD/CLAUDE.md, Zac)
- Music is intro and outro only. No beds under the talk (locked 2026-10-17).
- Match the movie's tone. No comedy cues over heavy scenes.
- Owned library first: catalog `D:\WKP\data\assets\music-catalog.md` (built 2026-11-19, 5,450 audio files). Channel theme: `L:\Winter Wolfs Den review show\Audio\Main Channel Theme.mp3` (117.2 s).

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
- WWD review intro sting is 6 seconds or less (Zac 2026-11-19, the 12 s A Knight's Tale intro was way too long). Hook lands inside that. Outro resolves clean, no hard cut at the host's last word.

## Owned library notes (from file names, not heard)
- `bcc-031814-slow-and-somber-haunted-piano-notes-157.mp3`: haunted piano. Copied to `P:\WWD Kit\Clayface\Sounds\` 2026-10-26 as the Clayface pick.
- `bcc-031814-eerie-ghosts-175.mp3`, `jdi-0414-eb-min-sad-cinematic-piano.mp3`, `bbc-051117-Horror-Film-Opening.mp3`, `short-horror-sting-build-up_MyTehEEu.mp3`: candidates.
- Adobe pack: `P:\Sounds\Music\adobe\Ambient\Chamber_Strings_60BPM\`, `...\Choir_Emin_160BPM\`.

## Learning log
- 2026-10-26: reference created from three web searches. Next: horror scoring research, the YouTube Audio Library filters, and a first audit with ffprobe and ebur128 of every track in the owned library.

## ElevenLabs Music (official docs, fetched 2026-11-19)
- Model ids: music_v2_5 (newest), music_v2; music_v1 deprecated, removed 2027-01-31, and is still the API default, so set the model on purpose. Source: elevenlabs.io/docs/overview/capabilities/music and /docs/api-reference/music/compose. Official.
- Compose settings: prompt OR composition_plan; music_length_ms 3,000 to 600,000 (overview page says 3 s to 5 min, conflict); force_instrumental (prompt only); seed (not with a prompt); store_for_inpainting; output mp3 or WAV. Official.
- Prompting: state genre, mood, instruments, tempo as a number, key ("in A minor"), "instrumental only", narrate the arrangement in time order ("start with", "then", "bring in"), give a length. Source: /docs/overview/capabilities/music/best-practices. Official. Untested by us.
- Terms (eleven-music-model-specific-terms, dated 09 October 2026): no artist, song, album, label names or distinctive lyrics in prompts; Free plan no downloads and attribution required; Starter and up no attribution; commercial use online and offline allowed except film, TV, radio, studio games; no indemnity, user clears output. Official. Older Nov 2025 version reported stricter (search summary only, not opened).
- Connector tools (creative_get_model_guide, get_model_schema) were not exposed to the music subagent on 2026-11-19.

## Learning log (cont.)
- 2026-11-19: A Knight's Tale stomp and clap job. Original song tempo about 81 BPM (162 double time), key reported D major, D minor or E minor depending on tool. Our difference plan: 108 BPM, four-beat pattern with a late second stomp, G Dorian, horns and war drums. Prompts in reports\music-stomp-clap-prompt-2026-11-19.md. Owned rock-the-crowd.mp3 measured -7.4 LUFS, +1.1 dBTP: generated and library tracks run hot, always measure.
