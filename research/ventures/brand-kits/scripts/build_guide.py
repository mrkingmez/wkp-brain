"""Builds the Side Business Brand Kits guide (.docx) and the Firefly prompts .md. Local only."""
import os
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

KIT = r"D:\WKP\research\ventures\brand-kits"
OUTDIR = r"D:\WKP Reports\Side Business Brand Kits"
DOCX = os.path.join(OUTDIR, "2026-11-10 - Side Business Brand Kits.docx")
os.makedirs(OUTDIR, exist_ok=True)

STYLE = "Style line (paste first in every prompt): "
NEG = "Avoid: people, faces, hands, text, letters, numbers, logos, watermarks, frames with writing, clutter."

PROMPTS = {
    "Photo restoration (Same Face)": [
        ("P1  Fiverr gig hero background (no faces on purpose)",
         "Overhead photograph of a worn dark walnut table in soft window light from the left. A loose scatter of old black and white and sepia prints with white scalloped borders, all turned face down or tilted so nothing on them reads, a few black paper photo corners, a soft white cotton glove, a small soft brush. Shallow depth of field, muted warm palette of cream, brown and one rust accent. Leave the left third of the frame calm and mostly empty for headline text.",
         "Image, Firefly Image model (Adobe's own, commercially safe line; exact model name on Zac's account NOT VERIFIED, read it off the panel). Content type Photo. Aspect 16:9 (Fiverr wants 1280x769, about 5:3, crop the extra off the top and bottom). Variations 4. Record the seed of the keeper in Advanced > Seed. Visual intensity default."),
        ("P2  Facebook cover background strip",
         "Wide flat lay along one horizontal band: a row of aged black and white print corners and torn paper edges on a cream linen surface, warm light, very low contrast, all prints face down, large calm cream area on the left half for text. Soft focus, matte, no strong shadows.",
         "Image, same model. Aspect 16:9, then crop to the central band for 851x315 (the 2x file is 1702x630). Variations 4. Keep it light, text sits on top."),
        ("P3  Optional hero for a Facebook post, lifestyle",
         "A shoebox of old paper prints on a kitchen table beside a mug of coffee, afternoon light through a window, shallow depth of field, prints face down, no people. Warm, quiet, a little nostalgic, not staged-looking.",
         "Image, same model. Aspect 1:1 for feed, 4 variations. Do not ask for faces. Real before/after images come from Zac's own photos, never generated."),
    ],
    "Transcription (Listen Twice)": [
        ("T1  Fiverr gig hero background",
         "Close photograph of a tidy desk in cool soft light. Over-ear headphones resting on a closed matte navy notebook, a blurred monitor behind glowing with abstract teal waveform shapes that read as light only, no readable text anywhere. Shallow depth of field, deep navy and teal palette with a clean white highlight. Leave the left third calm and empty for headline text.",
         "Image, Firefly Image model (name NOT VERIFIED on Zac's account). Content type Photo. Aspect 16:9, crop to 5:3 for 1280x769. Variations 4. Record the seed of the keeper."),
        ("T2  Facebook cover background strip",
         "Abstract flowing ribbons of teal and white light shaped like audio waveforms on a deep navy field, wide and horizontal, soft glow, very low detail on the left half so text can sit there, smooth gradient, no text, no symbols.",
         "Image, same model. Content type Art. Aspect 16:9, crop to the centre band for 851x315 (1702x630 at 2x). Variations 4."),
        ("T3  Optional post hero",
         "A podcast microphone on a desk next to a printed transcript page whose lines are blurred beyond reading, cool morning light, shallow depth of field, navy and teal palette, no people.",
         "Image, same model. Aspect 1:1, 4 variations. Any text on the page must stay unreadable, add real words afterward in Express or code."),
    ],
}

PLATFORM_NOTES = [
    "Add all lettering afterward (Adobe Express or the code in scripts\\brand_kit.py). Image models invent letters.",
    "Nothing here was generated. Zac clicks generate, reports back model name, seed and which variation held, and the reference file gets updated.",
    "Photo restore: Firefly is for backgrounds only. Customer faces are never run through a generative fill (locked in the launch prep face rule).",
    "Fiverr says gig images must be your own. Whether a Firefly-made background counts, and whether Fiverr requires AI disclosure on a gig image: NOT AVAILABLE, check the gig upload page before use.",
]

SPECS = [
    ("Fiverr gig image", "1280 x 769 px, 72 DPI, landscape, about 5:3. Minimum 712 x 430, maximum 4000 x 2416. Up to 3 images. Images must be your own.",
     "NOT directly OBSERVED. Fiverr's help pages returned HTTP 403 to my fetch (help.fiverr.com article 15863342952977 and 360010560358). The numbers come from a web search result that summarized Fiverr's own help center, so treat them as search summary of an official page. Confirm on the gig upload screen. File type and size limit: NOT AVAILABLE.",
     "https://help.fiverr.com/hc/en-us/articles/15863342952977-Creating-Gig-images-and-tagging-your-Gig-gallery"),
    ("Facebook Page cover photo", "Recommended 851 x 315 px, sRGB JPG under 100 KB loads fastest. Minimum 400 x 150 px.",
     "OBSERVED on Meta's own help page (facebook.com/help/125379114252045), fetched 2026-11-10. Mobile shows a taller crop of about 640 x 360 per third-party guides (SECONDARY, not on Meta's page), so the text sits in the centre band. 100 KB is a loading tip, the 851x315 JPG here is larger, run it through a compressor or use the 1x JPG if the upload feels slow.",
     "https://www.facebook.com/help/125379114252045"),
    ("Facebook Page profile picture", "Recommended 320 x 320 px.",
     "OBSERVED on the same Meta help page. Minimum: NOT AVAILABLE (page does not state one). Facebook shows it as a circle (SECONDARY), a circle preview is included. 640 x 640 is also saved for sharper display.",
     "https://www.facebook.com/help/125379114252045"),
]

NAMES = {
    "photo": [
        ("1", "Same Face Photo Restoration", "CLEAR", "Says the promise out loud: the face stays the face. Matches the no-redraw rule. Caution: reads as a guarantee, so the 'no guarantee on results' language must sit near it.", "LEAD"),
        ("2", "Grovetown Photo Repair", "CAUTION", "Local and plain. Hard to protect (city name plus service word) and could read as a City of Grovetown service.", ""),
        ("3", "Second Look Photo Restoration", "CAUTION", "Warm, plain, about the human check. A SECOND LOOK mark is registered (reg 5122831), coverage unchecked.", "Backup"),
        ("4", "Keeper Photo Restoration", "CAUTION", "Short, friendly. A KEEPER mark is registered (reg 3473690), coverage unchecked. Faint archive feel.", ""),
        ("5", "Shoebox Photo Restore", "CAUTION (riskiest)", "Best picture in the head (the shoebox of old photos) but SHOEBOX filings crowd the photo field.", "Avoid"),
    ],
    "transcribe": [
        ("1", "Listen Twice Transcription", "CLEAR", "Describes the method, machine draft then a human listen. Honest about AI help, which the market note says to disclose.", "LEAD"),
        ("2", "Clear Page Transcripts", "CAUTION", "Plain and trustworthy. The Clear prefix is crowded in transcription (Clear Choice Transcription, Crystal Clear Transcripts, ClearScribe AI).", "Backup"),
        ("3", "Grovetown Transcription Desk", "CAUTION", "Local. Hard to protect, and Desk can sound like an official office.", ""),
        ("4", "Plain Text Transcription", "CAUTION", "Plain Text is the name of the .txt file nearly every service offers, so it is close to unprotectable.", ""),
        ("5", "Proofed Word Transcripts", "CONFLICT", "PROOFED is a live registered mark for editing and proofreading (reg 6783849) and a company sells transcript proofreading under it.", "Drop"),
    ],
}


def write_prompts_md():
    p = os.path.join(KIT, "firefly-prompts.md")
    L = ["# Firefly prompts, side business brand kits (2026-11-10)", "",
         "Nothing generated. Zac clicks generate. No em dashes, no lettering in the image.", ""]
    L += [f"- {n}" for n in PLATFORM_NOTES]
    L += ["", f"{STYLE}Photographic, natural light, matte, muted palette, no text. {NEG}", ""]
    for biz, items in PROMPTS.items():
        L += [f"## {biz}", ""]
        for t, pr, st in items:
            L += [f"### {t}", "", f"Prompt: {pr}", "", f"Settings: {st}", ""]
    open(p, "w", encoding="utf-8").write("\n".join(L))
    return p


def H(doc, text, lvl):
    doc.add_heading(text, level=lvl)


def para(doc, text, bold=False, italic=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    return p


def bullets(doc, items):
    for i in items:
        doc.add_paragraph(i, style="List Bullet")


def table(doc, header, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Light Grid Accent 1"
    for i, h in enumerate(header):
        t.rows[0].cells[i].text = h
        for r in t.rows[0].cells[i].paragraphs[0].runs:
            r.bold = True
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = v
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    return t


def img(doc, path, width):
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(width))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER


def kit_section(doc, key, folder, title, lead, dirn, extra):
    H(doc, title, 1)
    base = os.path.join(KIT, folder)
    H(doc, "Name options (clearance flag attached)", 2)
    table(doc, ["#", "Name", "Flag", "Why, and the catch", "Call"], NAMES[key], [0.3, 1.8, 0.9, 3.3, 0.6])
    para(doc, "Clearance flag is a risk flag, not a legal opinion. Full evidence: research\\ventures\\brand-kits\\clearance-name-flags.md. "
              "NOT AVAILABLE: USPTO's own search (no page-fetch route, third-party copies of USPTO data used) and the Georgia Secretary of State "
              "search (could not run live). Domains and social handles were not checked. No name implies a government, archive or veteran-group "
              "affiliation; the two Grovetown names could suggest a city link, and Keeper carries a faint records feel.", italic=True)
    para(doc, f"Logo built on the lead name: {lead}. The script rebuilds everything for any name: python scripts\\brand_kit.py --kit {'photo' if key == 'photo' else 'transcribe'} --name \"New Name\"", bold=True)
    H(doc, "Logo direction", 2)
    para(doc, dirn)
    H(doc, "Palette and type", 2)
    para(doc, extra)
    img(doc, os.path.join(base, "logo-horizontal-light-padded.png"), 5.6)
    img(doc, os.path.join(base, "logo-horizontal-dark-padded.png"), 5.6)
    H(doc, "Assets built (all in " + base + ")", 2)
    bullets(doc, [
        "logo-horizontal / logo-stacked / logo-mark, light and dark, transparent PNG and on-colour PNG",
        "fiverr-gig-cover-1280x769, light and dark",
        "facebook-cover-851x315 (PNG and JPG) and 2x 1702x630, light and dark",
        "facebook-profile-320 and 640, light and dark, plus a circle preview",
        "_contact-sheet.png shows everything on one page",
    ])
    H(doc, "Fiverr gig cover (1280 x 769)", 2)
    img(doc, os.path.join(base, "fiverr-gig-cover-1280x769-light.png"), 5.0)
    img(doc, os.path.join(base, "fiverr-gig-cover-1280x769-dark.png"), 5.0)
    para(doc, "The headline and bullet lines on the gig cover are my working draft, not cleared copy. Public copy still owes the writing room, "
              "marketing-director and no-ai-slop gates before Zac uploads. The artwork on the right is a code-drawn illustration, not a result claim.")
    H(doc, "Facebook cover (851 x 315) and profile", 2)
    img(doc, os.path.join(base, "facebook-cover-851x315-light.png"), 5.6)
    img(doc, os.path.join(base, "facebook-cover-851x315-dark.png"), 5.6)
    img(doc, os.path.join(base, "facebook-profile-circle-preview-light.png"), 1.6)


def main():
    write_prompts_md()
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(11)
    doc.add_heading("Side Business Brand Kits", 0)
    para(doc, "Photo restoration and transcription, under Warrior King Productions. Built 2026-11-10 by graphic-design. Nothing posted, uploaded, or created as an account. No credits spent, no Firefly generated.", italic=True)

    H(doc, "The short version", 1)
    bullets(doc, [
        "Photo restoration lead name: Same Face (clearance CLEAR). Backup: Second Look (CAUTION, a registered SECOND LOOK mark needs a look). Avoid Shoebox.",
        "Transcription lead name: Listen Twice (clearance CLEAR). Backup: Clear Page. Drop Proofed Word (CONFLICT with a live PROOFED registration).",
        "Both kits have a finished logo in code (light and dark), a Fiverr gig cover, a Facebook cover and profile image. Photo restore also has a before and after template and a compose script.",
        "Two searches could not be done: the USPTO's own search and the Georgia Secretary of State search. Zac runs the Georgia one himself for the finalist before buying anything.",
        "Fiverr's help pages blocked my fetch (HTTP 403), so the 1280 x 769 spec is a search summary of Fiverr's page, not read directly. Meta's sizes were read on Meta's own page.",
        "Public copy on the images (headlines, taglines) is a working draft and still owes the writing room, marketing-director and no-ai-slop gates.",
        "Needs Zac's yes: the name pick for each business, and the Firefly generations. Everything else here is local files.",
    ])

    H(doc, "Size specs (looked up 2026-11-10)", 1)
    table(doc, ["Asset", "Spec", "Label and note", "Source"], [list(s) for s in SPECS], [1.2, 1.8, 2.8, 1.1])

    kit_section(doc, "photo", "photo-restore", "A. Photo restoration", "Same Face",
                "A small print with two photo corners, split along the diagonal. One half is faded, the other half is clear, with a plain head-and-shoulders shape crossing the split. "
                "It says before and after without showing anyone's face and without claiming a result. The photo corners in the accent colour are the old album mount, which is the one object everyone recognises from a shoebox of prints. "
                "Not a copy of any restoration brand: no camera, no phoenix, no sparkle, no flag, no eagle, nothing military or official.",
                "Light: paper cream, near-black ink, rust accent. Dark: charcoal, cream ink, soft orange accent. Poppins Bold and SemiBold (SIL Open Font License, free for commercial use), bundled in the repo.")
    H(doc, "Before and after template", 2)
    para(doc, "Two views in light and dark: 1920 x 1080 landscape and 1080 x 1080 square. The files marked SAMPLE use code-drawn stand-in art and say so in the corner. Never post a SAMPLE file.")
    img(doc, os.path.join(KIT, "photo-restore", "before-after-template-landscape-1920x1080-light-SAMPLE.png"), 5.6)
    img(doc, os.path.join(KIT, "photo-restore", "before-after-template-square-1080x1080-dark-SAMPLE.png"), 3.2)
    para(doc, "To make a real one: python scripts\\make_before_after.py --before B.jpg --after A.jpg --out out.png --mode light --shape landscape. "
              "Photos are fit inside each panel and never cropped. Add --preview for a diagonal PREVIEW watermark, which is the preview version the offer calls for before payment. "
              "Rules from the launch prep still apply: only Zac's own family photos or public-domain items with the rights line saved, nothing of a living person without their OK, "
              "and AI-assisted never gets described as hand restoration. The tagline on the template says 'AI-assisted. Every face checked by hand. Original returned untouched.' and is draft copy awaiting the gates.")

    kit_section(doc, "transcribe", "transcription", "B. Transcription", "Listen Twice",
                "A rounded tile. On the left, five bars of an audio waveform. On the right, four lines of text. The sound turns into words, left to right. "
                "The teal bars carry the accent, the white lines are the finished text. No microphone, no headphones, no speech bubble, no robot, which is where the crowded transcription field lives.",
                "Light: cool white, deep navy ink, teal accent. Dark: midnight navy, white ink, bright teal. Poppins Bold and SemiBold (SIL OFL). "
                "Kept apart from the photo kit (warm and brown versus cool and blue) so the two businesses never look like one.")

    H(doc, "Firefly prompts (Zac generates, nothing was run)", 1)
    for n in PLATFORM_NOTES:
        doc.add_paragraph(n, style="List Bullet")
    para(doc, STYLE + "Photographic, natural light, matte, muted palette, no text. " + NEG, bold=True)
    for biz, items in PROMPTS.items():
        H(doc, biz, 2)
        for t, pr, stg in items:
            para(doc, t, bold=True)
            para(doc, "Prompt: " + pr)
            para(doc, "Settings: " + stg, italic=True)
    para(doc, "Why code did the logos and layouts: crisp shapes, exact sizes, and every name can be re-rendered. Firefly is only asked for photographic backgrounds code cannot fake. "
              "Not used: Higgsfield, ElevenLabs image, Adobe Express (no credits, no accounts). Image model names on Zac's Firefly are not in memory (only the video menu is), so the model line says read it off the panel.")

    H(doc, "What I need from Zac", 1)
    bullets(doc, [
        "Pick a name for each business. Before buying a domain or filing, search the finalist on ecorp.sos.ga.gov (Contains), and check SECOND LOOK reg 5122831 and KEEPER reg 3473690 in TSDR if either is in play.",
        "Say yes or no to the Firefly generations (credits are shared, Matt paid for them). Report back model name, seed and which variation held.",
        "Confirm whether the Warrior King Productions name appears on either page (not on any asset now).",
        "Run copy through the gates before any asset with words goes public.",
        "Fiverr: confirm the gig image limits on the upload screen and whether AI-made backgrounds need a disclosure there.",
        "Commercial-use check for the Firefly backgrounds stays with Zac (Adobe's terms), same open item as the photo restore launch prep.",
    ])
    H(doc, "Files", 1)
    bullets(doc, [
        r"D:\WKP\research\ventures\brand-kits\photo-restore\  and  \transcription\  (all images)",
        r"D:\WKP\research\ventures\brand-kits\scripts\brand_kit.py, make_before_after.py, build_guide.py",
        r"D:\WKP\research\ventures\brand-kits\firefly-prompts.md",
        r"D:\WKP\research\ventures\brand-kits\clearance-name-flags.md",
    ])
    doc.save(DOCX)
    print("saved", DOCX)


main()
