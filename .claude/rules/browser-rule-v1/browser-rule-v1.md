# Browser rules v1

Apply these rules whenever a task could involve opening or controlling a web browser.

## Tool choice

- Use the Playwright MCP (`mcp__playwright__*` tools) for browser work by default.
- Use another browser tool, such as Claude in Chrome, only when the user names it.

## Automatic use

- If the user's message contains one of the keywords below, use the Playwright MCP right away without asking first.
  - "브라우저를 열어서 작업" (open a browser and work)
  - "웹 제어" (web control)
  - "직접 작업" (do it directly)
  - Similar expressions, such as "브라우저로", "브라우저 열어서", "사이트에 들어가서", "웹에서 직접"

## Use with consent

- If the user has not used a keyword but the task could be done with the Playwright MCP (for example, checking a web page, filling in a form, clicking through a site, or taking a screenshot), ask for consent before calling it.
  - Example: "브라우저를 직접 열어서 작업해도 될까요?"
- Do not call any Playwright MCP tool until the user agrees.
- If the user declines, do the task another way or explain what cannot be done without the browser.

## Safety

- Even when a keyword was used, confirm with the user before any action that is hard to undo, such as making a payment, entering login credentials, submitting a form, or posting content.
- Close the browser with `mcp__playwright__browser_close` when the browser work is finished.
