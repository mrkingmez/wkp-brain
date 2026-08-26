---
name: wwd-frostcast-chapters
description: Turns a diarized, timestamped transcript into a YouTube
  chapter list. Works for FrostCast, reviews, Den Files, Retro Watch,
  exposes, or any WWD video. Trigger on 'get me the chapters',
  'chapter list', 'chapters for this episode', or when a transcript is
  handed over and chapters are requested.
---

# WWD Chapters

Input: a diarized, timestamped transcript.
Output: the chapter list. Nothing above it, nothing below it.

## Format - exact, no deviation

First line is ALWAYS:
00:00:00 - Start

Every line after:
HH:MM:SS - Chapter name

Rules YouTube enforces and will silently ignore the whole list over:
- The list must begin at 00:00:00. No exceptions.
- Minimum three chapters total.
- Each chapter minimum 10 seconds long.
- Ascending order. No gaps. No overlaps.
- Use HH:MM:SS throughout, including under an hour (00:04:12).

## Where chapters come from

The transcript. Only the transcript.

There is no fixed show structure. WWD videos are two people talking
and the conversation goes where it goes. Do NOT assume segments. Do
NOT read a format file for structure. Do NOT impose a template.

Read the transcript and find where the SUBJECT changes. That is a
chapter boundary. A long back and forth about one film is ONE
chapter no matter how many times the speakers swap.

If the conversation wanders back to an earlier subject, that is a
new chapter at that timecode. Do not merge it with the earlier one.
Chapters are chronological, not thematic.

## Chapter names

Name what is actually being discussed during that timecode range.
Use the real subject name - the film, the game, the person, the
event. The subject name is what search picks up.

'Nolan's Odyssey Trailer' beats 'Trailer Talk'.

Verify before writing: read what is actually said between the in and
out points. If the name does not match the talk, it is wrong.

Under 50 characters. No em dashes.

Scores and numbers are fine. If a rating is given in that section
and it belongs in the name, use it.

## Output

Return ONLY the chapter list. No preamble, no notes, no summary.
It gets pasted straight into the description.

## Escalation

No timestamps, or not diarized? Say so and stop.
Never estimate a timecode.