# PPT rules v1

Apply these rules whenever you build or edit a presentation (.pptx).

## Priority

- Apply these rules first, before the defaults of the `mk-ppt` skill.
- When sources disagree, follow them in this order:
  1. The user's request
  2. These rules
  3. The design-related `.md` file the user provides
  4. The design defaults of the `mk-ppt` skill
- Use the skill's defaults only for what the sources above leave open.

## Slide count

- Build 8 slides by default.
- Use a different number only when the user asks for one.

## Design reference

- Before building, read the design-related `.md` file the user provides and follow it.
- If the user has not provided one, ask for it before starting.

## Layout and readability

- Keep all text inside the slide boundaries. No text may run off the slide.
- Do not let text and shapes overlap in a way that makes them hard to read.
- After building, inspect the deck and fix any overflow or overlap before reporting.
