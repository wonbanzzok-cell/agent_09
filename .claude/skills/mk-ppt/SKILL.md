---
name: mk-ppt
description: Build, edit, and inspect PowerPoint (.pptx) files in this repository with the python-pptx library. Use this skill whenever the user asks for a PPT, slides, a deck, a presentation, 발표자료, or 슬라이드, wants a research note or report turned into a presentation, or wants an existing .pptx changed, filled in from a template, or mined for its text, tables, notes, or images, even when they do not mention python-pptx by name.
---

# mk-ppt

Make and modify PowerPoint files with `python-pptx`. This skill lives in `.claude/skills/` of this repository, so it only loads here, and everything it produces stays inside this repository.

The work is always the same shape: write a Python build script, run it, then open the result again and check it. A script is kept rather than a one-off command because a deck is revised many times, and a script makes the next version a small edit instead of a rebuild.

## Before starting

- Follow the workflow in `CLAUDE.md`: report a todo list, wait for approval, and finish by organizing the structure. Put the slide outline (step 3 below) in that todo list so the user approves the content before anything is built.
- Check the library with `python -c "import pptx; print(pptx.__version__)"`. If the import fails, add `python -m pip install python-pptx` to the todo list instead of installing silently.

## Where files go

| Item | Location |
|---|---|
| Presentation | `presentation/<주제>_발표자료_v<N>.pptx` |
| Build script | `scripts/build-presentation-v<N>.py` |
| Images made for a deck | `presentation/assets/v<N>/` |
| Throwaway files | the session scratchpad, never the repository |

- Create `presentation/` when the first deck is built.
- Do not overwrite an existing deck. Use the next number after the highest existing version, and copy the previous build script to the new version number before changing it.
- A deck built from a research note or report takes the same version number as its source when that number is free.
- Write slide content in Korean unless the user asks otherwise, matching the reports in `report/`.

## Workflow

1. **Pin down the content.** Find the source (a research note, a report, or the user's message), the audience, and the rough slide count. Ask only when the answer changes the deck.
2. **Inspect first when a file already exists.** For an edit or a template, run the inspector before writing any code, because placeholder indexes and layout names differ in every file and guessing them fails:
   ```
   python .claude/skills/mk-ppt/scripts/inspect_pptx.py <file.pptx>
   ```
3. **Outline the slides.** One line per slide: title, the point it makes, and its element (bullets, table, chart, picture). Report this in the todo list.
4. **Write the build script.** It takes the output path as its only argument, like `scripts/build-report.js`. Start from the skeleton in `references/python-pptx-api.md`.
5. **Run it from the repository root.**
   ```
   python scripts/build-presentation-v<N>.py "presentation/<주제>_발표자료_v<N>.pptx"
   ```
6. **Verify.** Run the inspector on the output and compare it with the outline: slide count, titles, no empty placeholders, no shape outside the slide. Fix the script and rebuild rather than patching the file by hand.
7. **Report and organize.** Tell the user what was built and what could not be done, then update the structure and tables in `CLAUDE.md` and its translation.

## Design defaults

Use these unless the user or a template says otherwise.

- **Size:** 16:9, `13.333 x 7.5` inches. The built-in default template is 4:3, so set the size explicitly.
- **Layout:** the blank layout (`slide_layouts[6]` in the default template) with text boxes placed by coordinates gives predictable results. Use placeholders when filling a user's template, so the template's design is kept.
- **Margins:** keep content at least 0.5 inch from every edge.
- **Font:** `맑은 고딕`. Title 32–40 pt, body 18–24 pt, captions no smaller than 12 pt.
- **Density:** one point per slide, about five bullets at most. Move the detail to the speaker notes.
- **Color:** one accent color plus neutrals, defined once as constants at the top of the script.

## Things that go wrong

- **Korean text falls back to another font.** `font.name` sets only the Latin typeface. Set the East Asian typeface too with the `set_font_name` helper in the reference.
- **Text overflows its box.** The library does not measure text, and PowerPoint only applies auto-fit when the file is opened and edited. Size boxes generously and set font sizes explicitly.
- **Placeholders sit off-center in a 16:9 deck.** Changing the slide size does not move the default template's placeholders; they stay where the 4:3 layout put them. Use the blank layout with text boxes, or set each placeholder's position and size.
- **Placeholder not found.** Look placeholders up by `placeholder_format.idx` from the inspector output, not by their position in the list.
- **`PermissionError` on save.** The file is open in PowerPoint. Ask the user to close it; do not save under another name to get around it.
- **Odd sizes.** Lengths are EMU integers. Always wrap numbers in `Inches()`, `Cm()`, or `Pt()`.
- **Chart will not build.** Series values must be numbers (or `None`), and every series needs one value per category.

## What the library cannot do

Say so plainly when the user asks for one of these, and offer the nearest thing that works.

- Animations and slide transitions
- Creating SmartArt, editing equations
- Rendering slides to images or PDF
- Old `.ppt` files and password-protected files
- Comments

Deleting, reordering, or duplicating slides, deleting shapes, changing z-order, and adding or removing table rows have no public API but work through direct XML edits. The reference has tested snippets for each.

## Reference

Read `references/python-pptx-api.md` for code. It is organized by task, so read only the section needed:

1. Script skeleton and helpers
2. Presentation and slides
3. Placeholders
4. Shapes
5. Text
6. Pictures
7. Tables
8. Charts
9. Fill, line, and color
10. Actions and media
11. Reading and extracting
12. XML workarounds
