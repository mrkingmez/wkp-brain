# WKP Voice Capture App — Handoff Document
## Working title: "Spark Capture" (placeholder — needs branding pass)

## 1. Concept
Hands-free, wake-word-triggered idea capture app for Android (Pixel-first).
Problem: user gets strong creative ideas while driving, walking, or in the
shower — moments where touching a phone breaks the flow or isn't safe/possible.
Existing voice memo apps (Otter, Audionotes, Google Recorder) all require
opening the app first. Gap: true zero-touch capture triggered by a custom
spoken wake word/phrase, with automatic transcription.

## 2. Core Differentiator
User-selectable custom wake word/phrase (not a fixed "Hey App" trigger).
This is the hard technical problem — no vendor currently offers true
instant, self-serve, train-it-yourself-in-the-moment custom wake words.
Closest options require pre-training a model (minutes to hours), not
instant recognition of a brand-new phrase on first utterance.

## 3. Technical Approach (MVP)
- Platform: Android native (Pixel 4 test device on hand)
- Wake word engine: OpenWakeWord (free, open-source, self-trained models)
  - Fallback/upgrade path: Picovoice Porcupine (free tier, 3 active users/mo
    cap; commercial scale ~$6,000/yr+) or Outspoken (~$1/model, newer/smaller vendor)
- On-device or cloud transcription layer once wake word fires
- Local storage of captured notes; cloud sync as a paid-tier feature
- Background/foreground service for always-listening detection (low battery
  impact — wake word detection is lightweight vs. full always-on ASR)

## 4. Build Phases
1. Discovery/spec (finalize MVP feature list, wake word engine choice)
2. Core app shell — UI, settings, note storage/organization (vibe-codeable)
3. Wake word engine integration (OpenWakeWord SDK integration — the
   non-vibe-codeable, native/compiled piece)
4. Transcription pipeline integration
5. QA across real-world noise/accent conditions
6. Beta test (small user group) before public launch

## 5. Cost Estimate (rough, start to production)
- Bare-bones freelance-built MVP: ~$5,000–15,000
- Fuller-featured native MVP (design + backend + wake word integration): ~$15,000–40,000
- Wake word licensing: $0 (OpenWakeWord) during MVP phase; budget for
  Picovoice/Outspoken licensing if scaling past free-tier limits
- These are third-party market rates, not a quote — actual cost depends on
  how much is self-built vs. contracted

## 6. Monetization — Freemium Model
Hook tied to the app's actual differentiator (wake word capture), not
generic transcription minutes:
- FREE tier: unlimited basic manual voice memo capture; 1–2 wake word
  slots; capped number of wake-triggered recordings per month
- PAID tier: unlimited custom wake words, longer auto-transcribed sessions,
  cloud sync, project/world tagging (e.g., tag ideas to Shadowfall vs.
  Shattered Empire vs. general), priority processing
- Rationale: industry-standard freemium apps (Otter, etc.) gate on
  minutes/session length; this app should gate on the wake-word capacity
  itself since that's the unique value prop

## 7. Competitive Landscape (as of research)
- Otter.ai, Audionotes, Google Recorder, Speakwise — all require manually
  opening app before recording; none offer true wake-word zero-touch trigger
- No competitor currently offers instant self-serve custom wake words —
  this is a genuine open gap, but also the hardest part to solve; MVP should
  ship with a curated list of pretrained wake phrases first, then pursue
  true self-serve custom training as a v2/scale-up goal

## 8. Next Steps for Claude Code
- Use this doc as the seed spec for the repository
- Recommend starting with app shell + note storage before touching the
  wake word SDK integration
- Flag: wake word SDK integration will require native Android dev work,
  not pure vibe-coding — plan accordingly
