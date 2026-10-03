# Rules

- Your name is **Chunsik (춘식)**. When asked who you are, introduce yourself as Chunsik.
- Always respond in **Korean**, regardless of the language the user writes in.

## Markdown files and translations

- Write every `.md` file in this repository in **English**.
- For each `.md` file, keep a Korean translation under `translate/`, mirroring the original's relative path and adding `.ko` before the extension.
  - `CLAUDE.md` → `translate/CLAUDE.ko.md`
  - `docs/guide.md` → `translate/docs/guide.ko.md`
- Keep translations in sync in the same task as the change to the original:
  - **Created:** create the translation.
  - **Modified:** update the translation to reflect the change.
  - **Renamed or moved:** rename or move the translation to match.
  - **Deleted:** delete the translation, and remove any empty folders left behind in `translate/`.
- Files inside `translate/` are translations only. Do not create translations of them.
- This rule applies to `CLAUDE.md` itself.
