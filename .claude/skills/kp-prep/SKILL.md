---
name: kp-prep
description: Builds the eight-image photo set for a Kingdom Planners
  listing. Screenshots, not mockups - there is no physical product.
  Trigger on 'kp prep', 'photo set', 'kp images'.
---

# Kingdom Planners Prep

## The eight images
1. Title card - navy, gold accent, product name. Adobe Express, done, swap headline per product.
2. Main tab screenshot, real data visible, not placeholder text.
3. Calculator close-up, visibly working - show an actual result, not an empty cell.
4. Second tab screenshot.
5. Third tab screenshot.
6. Contents graphic - every tab named. THIS IS THE ONE THAT CONVERTS. Never write "and more." Enumerate every tab.
7. "Works in Excel and Google Sheets" - done, permanent, never changes.
8. Veteran credential card - done, permanent, never changes.

## Watermarking previews (optional, not automatic)

scripts\watermark.py tiles a rotated, translucent shop name across a
preview image. Whether to watermark KP screenshots is still Zac's
open call - the tab and calculator shots are his own product, not
art, so the theft risk is different from WKD's printables. Run it
only when asked. Do not apply it by default to every image.

Usage:
python scripts\watermark.py --input "path\to\screenshot.png" --text "Kingdom Planners" --out "path\to\preview.jpg"

## Rules
Images 2-5 are real screenshots of the actual working file, not
staged. If the spreadsheet isn't finished, this skill cannot run yet.
Image 6 needs the real tab names from kp-generator's output - never
guess a tab name to fill this in early.

## Escalation
Spreadsheet not finished, or tab names not confirmed - say which
images are blocked and why, don't produce placeholders.