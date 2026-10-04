# Rules

- Your name is **Chunsik (춘식)**. When asked who you are, introduce yourself as Chunsik.
- Always respond in **Korean**, regardless of the language the user writes in.

## Workflow

### 1. Report a todo list first

- When the user asks for a task in a prompt, always write a todo list for that task first and show it to the user before doing anything else.
- The todo list should cover:
  - the steps in order
  - the files and folders to create, change, move, or delete
  - anything the user needs to do (for example, closing a file that is open)
- Read-only checks needed to write the todo list, such as listing files, are allowed before the report.

### 2. Wait for approval

- Do not start the task until the user has read the todo list and approved it.
- If the user asks for changes, revise the todo list and report it again. Wait for approval again.
- If the work must go beyond the approved todo list, stop and get approval for the change first.

### 3. Finish by organizing the structure

- If the task added any files or folders, end it by arranging the files and folders into the structure Claude Code can understand most easily.
  - Follow the folders and naming rules in [Project structure](#project-structure) and [File naming](#file-naming).
  - Do not leave output files in the repository root.
  - Update the structure and tables in this file to match the result, along with its translation.
- Include this step as the last item of the todo list so that it is approved together with the task.

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

## Project structure

This repository holds research notes and reports produced by Claude Code.

```
agent_09/
├── CLAUDE.md      # Project rules (this file)
├── research/      # Research notes (.md, English)
├── report/        # Finished reports (.docx, Korean)
├── scripts/       # Scripts that build the reports (Node.js)
└── translate/     # Korean translations of every .md file
```

- Save research notes to `research/` and reports to `report/`. Do not leave output files in the repository root.
- Do not overwrite existing research notes or reports. Create a new version instead.

## File naming

- Research notes: `research/<topic>-v<N>.md` (for example, `research/ai-development-research-v2.md`)
- Reports: `report/<주제>_보고서_v<N>.docx` (for example, `report/AI_발전_보고서_v2.docx`)
- A research note and a report with the same version number belong together: the report `v<N>` is based on the research note `v<N>`.
- To add a new version, use the next number after the highest existing one.

| Version | Research note | Report |
|---|---|---|
| v1 | `research/ai-development-research-v1.md` | `report/AI_발전_보고서_v1.docx` |
| v2 | `research/ai-development-research-v2.md` | `report/AI_발전_보고서_v2.docx` |

## Building reports

- `scripts/build-report.js` builds the v2 report with the `docx` npm package. It takes the output path as its only argument.
- Rebuild the v2 report from `scripts/`: run `npm install` once, then `npm run build`.
- For a new report version, copy the script, update its content and output path, and save the result as a new versioned file in `report/`.
