# Module 5: Advanced track (optional)

This module opens after you finish Modules 1 to 4. It is a doorway to a free course written by someone else, for people who build AI software. Read this page first so you know what you are walking into.

## The honest version

- The course is called **AI Engineering from Scratch**. It is free and open source under the MIT license. It was not written for this site and nobody here has tested it with a beginner.
- It is **builder-oriented**. Most lessons ask you to write and run code. You do not need that to use AI well, and you can finish this whole course without it.
- It is huge. Its own README says 542 lessons in 20 phases. Nobody is expected to do it all, and you should not try.
- What it can give you is a look at how these tools are built, how they fail, and why they act the way they do. That can make the earlier modules make more sense. It is a curiosity track, not a requirement.
- Do not install or run anything from it on the home computer without asking Zac first. Reading the lessons in a web browser is all you need.

## Where it lives

- On the web: [github.com/rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
- A copy sits on the home computer in `D:\WKP\Teacher\vendor\`. It was downloaded and left alone. Nothing in it has been run.
- Checked 2026-11-12: MIT license, latest commit on the main branch dated 2026-11-12.

## Lessons that suit a non-programmer

Each lesson below opens as a long page of text with code mixed in. The advice is to read the explaining parts and skip the code. I read the openings and section headings of these lessons, not every word, so treat the notes as a starting map.

| Lesson | What the lesson says it is | How to read it |
|---|---|---|
| [Prompt Engineering: Techniques and Patterns](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/01-prompt-engineering/docs/en.md) | Marked a "Build" lesson in Python, about 90 minutes. Its headings include role prompting, instruction clarity, constraints and anti-patterns. | Read "The Problem" and "The Concept". Skip "Build It". It lists an earlier phase of model-building lessons as a prerequisite, which you can ignore for the ideas. |
| [Sycophancy as RLHF Amplification](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/04-sycophancy-rlhf-amplification/docs/en.md) | Marked "Learn", about 60 minutes. The opening is about an AI agreeing with something wrong because agreeing is rewarded. | Read "The Problem". The sections after it have headings like "The two-stage formalism", so they look technical. Skip them if they lose you. This ties straight to Lesson 1: a pleasant answer is not a correct one. |
| [Indirect Prompt Injection](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/15-indirect-prompt-injection/docs/en.md) | Marked "Build", about 75 minutes. The concept section covers instructions hidden in a web page, an email or a document that an AI then reads and follows. | Read "The Problem" and "The Concept". Skip the code. Useful before you let any AI tool read your email or browse for you. |
| [Watermarking: SynthID, Stable Signature, C2PA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/23-watermarking-synthid-stable-signature-c2pa/docs/en.md) | Marked "Build", about 75 minutes. It covers ways of marking AI-made content, and a "Limitations" section. | Read "The Concept" and "Limitations". It fits Module 3 on fakes. Skip the code and the math prerequisites. |
| [Regulatory Frameworks: EU, US, UK, Korea](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/24-regulatory-frameworks-eu-us-uk-korea/docs/en.md) | Marked "Learn", about 75 minutes. A policy lesson on AI laws. | Optional. I read only the opening. Laws change, so check any date in it against an official source before you rely on it. |

## What you can skip

- The setup and tooling phase, the math phase, and the phases on training models. Judging by their folder names these are about installing tools, mathematics and building models. I did not open them.
- Anything whose lesson page starts with "Prerequisites" naming several earlier lessons of code.
- Everything on agents, infrastructure and capstone projects, unless you become curious about building something. I judged that from folder names only.

## A caution about what the lessons say

These are one author's lessons, and many cite research papers and dates from 2026. We have not checked those claims. Apply Lesson 1 to the course itself: when a lesson states a number or a date, look at where it comes from before you repeat it.

## When you finish

There is no quiz here. If a lesson caught your interest, tell Zac. He can help you try the ideas safely, or decide whether a coding lesson is worth setting up.
