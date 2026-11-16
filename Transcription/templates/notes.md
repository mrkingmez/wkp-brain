# {{JOB_ID}}  |  Gig {{GIG}}: {{GIG_NAME}}  |  Buyer: {{HANDLE}}

PRIVATE CLIENT JOB. This folder never goes in git, never to a cloud tool or API without the buyer's consent.
Speaker labels for client audio are generic (Speaker 1, Speaker 2). Never run client audio against D:\WKP\voiceprints.

## Order details
- Job ID: {{JOB_ID}}
- Created: {{CREATED}}
- Gig: {{GIG}} ({{GIG_NAME}})
- Fiverr order #: {{ORDER}}
- Buyer handle: {{HANDLE}}
- Audio minutes: {{AUDIO_MIN}}
- Price quoted: {{PRICE}}
- Requested file types: {{FILE_TYPES}}
- Due date: {{DUE}}
- Speakers: (fill at intake)
- Audio quality 1-5: (fill at intake)
- Special requests (names, glossary, verbatim or clean, timestamps): (fill at intake)
- Buyer consented to cloud tools? NO (default). Local pipeline only.

## Checklist  (tick as you go; [ZAC] = only Zac can do it, [AGENT] = agents do it)
Who is the job waiting on right now? Keep the tracker column "Waiting on" in step with this list.

### Intake
- [ ] [AGENT] Check length, audio quality, speaker count (ffprobe plus a listen). Fill the order details above.
- [ ] [AGENT] Draft the buyer questions (file types, names to spell, deadline, verbatim or clean). Draft only.
- [ ] [ZAC] Send the questions to the buyer on Fiverr (every buyer message is Zac's).
- [ ] [ZAC] Give or approve the price quote.
- [ ] [ZAC] Accept the order on Fiverr.

### Work
- [ ] [ZAC] Download the buyer's audio or video from the Fiverr order into 01-raw-audio.
- [ ] [AGENT] Run the local pipeline (run_pipeline.py). Machine time logs itself.
- [ ] [AGENT] Proofread the draft in 02-working with the clock running (job_clock.py start JOB proofreading).
- [ ] [ZAC] Spot-check read of the master (about 10 minutes). Required for the first 3 jobs of each gig, optional after.
- [ ] [AGENT] Convert to every requested file type (convert_deliverable.py). Files land in 03-final-documents.
- [ ] [AGENT] Check 03-final-documents: every requested type present, names right, files open, no client names mixed up.

### Delivery
- [ ] [AGENT] Draft the delivery message (draft only).
- [ ] [ZAC] Upload the files from 03-final-documents on Fiverr and send the delivery.
- [ ] [AGENT] Record delivered date, minutes worked, price in the tracker (close_job.py).
- [ ] [ZAC] Enter price and the Fiverr fee in the tracker (the fee is not verified by any script).
- [ ] [AGENT] Draft the review request (draft only).
- [ ] [ZAC] Send the review request. Anything public is Zac's.
- [ ] [ZAC] Reply to the buyer if they ask for a revision (agent drafts, Zac sends). Log each revision in close_job.py --revisions.

## Timer log
Minutes by category are also in the tracker. Categories: machine, proofreading, conversion, admin.
<!-- TIMER-LOG-END -->

## Issues and notes
<!-- ISSUES-END -->
