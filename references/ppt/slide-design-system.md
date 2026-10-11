# Slide design system

Design reference for building presentations (.pptx) in this repository. It is derived from a minimal light-gray template image. Colors and fonts are estimated by eye from that image.

## Concept

- Minimal and modern: a light gray canvas, near-black type, and one photo per slide.
- Generous white space. Leave areas empty rather than filling them.
- No gradients, shadows, rounded corners, or decorative icons.

## Canvas

- Size: 16:9 (13.333 in × 7.5 in).
- Margins: 1.0 in left and right, 0.9 in top and bottom.
- Split: text column on the left (x 1.0–6.4 in), image column on the right (x 7.3–12.5 in), with a 0.9 in gutter.

## Colors

| Role | HEX | Use |
|---|---|---|
| Background | `#EEEEEE` | Every slide background |
| Primary text | `#111111` | Titles, quote mark, caption labels |
| Secondary text | `#333333` | Subtitles |
| Muted text | `#777777` | Body text, small captions |
| Line | `#BDBDBD` | Thin divider lines |
| Accent | `#6F8FB5` | Chart highlights and key numbers only |
| Surface | `#FFFFFF` | Cards and table cells, when needed |

- Keep slides almost monochrome. Use the accent on at most one element per slide.

## Fonts

- Typeface: `Pretendard`. Fallback: `맑은 고딕` (Malgun Gothic).
- Align all text left. Do not center or justify.

| Element | Size | Weight | Color |
|---|---|---|---|
| Cover title | 54 pt | Bold | `#111111` |
| Cover subtitle | 28 pt | Light | `#333333` |
| Slide title | 32 pt | Bold | `#111111` |
| Body | 14–16 pt | Regular | `#777777` |
| Caption label | 12 pt | SemiBold | `#111111` |
| Caption, source | 10–11 pt | Regular | `#777777` |

- Line spacing: 1.0 for titles, 1.5 for body text.
- Body text: at most 5 lines per block, and at most 3 blocks per slide.

## Components

- **Quote line:** a bold `“` mark (24 pt, `#111111`), then a thin line (0.75 pt, `#BDBDBD`, about 2.4 in long), then a short label (12 pt). Use it for the presenter name or a section label.
- **Image:** a sharp-cornered rectangle with no border or shadow. Prefer architecture or abstract photos in low-saturation blue and gray tones.
- **Caption block:** below the image, left-aligned to its edge. Bold label on the first line, regular text on the second, and an optional source in small letter-spaced capitals to the right.
- **Divider:** a 0.75 pt `#BDBDBD` line. Use lines instead of boxes to separate content.

## Slide types

| Type | Layout |
|---|---|
| Cover | Left: title, subtitle, quote line, short summary. Right: large image with a caption block below |
| Section | Left: section number and title, large. Right: empty or a narrow image |
| Content | Title at top left, body below it. Image or chart in the right column |
| Data | Title at top left. Chart or table across the full width, with the key number in the accent color |
| Closing | Same split as the cover, with a short closing line and contact details |

## Do and don't

- Do keep the same margins and the same left edge on every slide.
- Do use one message and one image per slide.
- Don't add colors outside the palette or more than one typeface.
- Don't let text run off the slide or overlap images and shapes.
