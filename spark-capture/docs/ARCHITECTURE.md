# Architecture Notes

Scaffolding-stage notes only. See `HANDOFF.md` for the full spec these
decisions trace back to.

## Package layout → build phase

| Package                                 | Phase | Status                          |
|------------------------------------------|-------|----------------------------------|
| `ui/`                                     | 2     | Empty — screens not started      |
| `data/` (`Note`, `NoteRepository`)        | 2     | Shape stubbed, no persistence    |
| `wakeword/` (`WakeWordEngine`)            | 3     | Interface only, no OpenWakeWord  |
| `transcription/` (`TranscriptionEngine`)  | 4     | Interface only                   |
| `service/` (`CaptureForegroundService`)   | 3     | Stub, no real service logic      |

## Why interfaces first

`WakeWordEngine` and `TranscriptionEngine` are defined as interfaces before
any real implementation exists. Two reasons:

1. **Swappability.** The wake-word engine choice (OpenWakeWord →
   Porcupine/Outspoken fallback) and the transcription approach
   (on-device vs. cloud) are both still open per the handoff doc
   (Sections 3, 8). An interface boundary means neither decision blocks
   Phase 2 work.
2. **Testability of Phase 2 against fakes.** The app shell (navigation,
   note list, settings) can be built and demoed with a fake
   `WakeWordEngine`/`TranscriptionEngine` before the real, non-vibe-codeable
   native integration exists.

## Open decisions carried over from the handoff doc

- Wake word engine: OpenWakeWord (MVP) vs. Porcupine/Outspoken (scale).
- Transcription: on-device vs. cloud.
- minSdk: currently set to 26 as a placeholder floor below the Pixel 4
  test device's Android 10 (API 29). Revisit once the wake-word SDK's
  actual minimum is known.
- App identity: package name `com.wkp.sparkcapture`, app name
  "Spark Capture," and namespace are all placeholders pending the
  branding pass flagged in Section 1 of the handoff doc.

## Not yet decided / not in scope for this scaffold

- Room schema for `Note` (currently a plain data class, no `@Entity`)
- Navigation structure for the app shell
- Cloud sync design (paid-tier feature, Section 6)
- CI setup
