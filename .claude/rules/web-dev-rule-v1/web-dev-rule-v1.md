# Web development rules v1

Apply these rules whenever you write code for a web page or deploy one. The `developer` agent must read this file before writing any code.

## Priority

- When sources disagree, follow them in this order:
  1. The user's request
  2. These rules
  3. The web design reference analysis in `references/web/<topic>/`
  4. General best practice

## File structure

- Build every page with plain **HTML, CSS, and JavaScript**. No framework and no build step; the page must work by opening `index.html` from a static server.
- Use this structure inside the version folder `output/web/<topic>/v<N>/`:

```
v<N>/
├── index.html       # Entry point
├── css/
│   └── style.css    # All styles
├── js/
│   └── main.js      # All scripts
├── images/          # Images used by the page
├── libs/            # Downloaded third-party libraries (only if needed)
│   └── <library>-<version>/
├── screenshots/     # Check screenshots (desktop.png, mobile.png); not part of the page
└── .nojekyll        # Lets GitHub Pages serve every file as is
```

- Add more HTML, CSS, or JS files only when the page clearly needs them, and keep them in the folders above.
- Use **relative paths** for every link, image, style, and script (`css/style.css`, not `/css/style.css`), so the page works under the GitHub Pages sub path `/<task_name>/`.
- Use lowercase file names with hyphens.

## Coding rules

- **HTML:** semantic tags (`header`, `nav`, `main`, `section`, `footer`), one `h1`, a logical heading order, `lang="ko"` for Korean content, `<meta name="viewport">`, a page `<title>` and `<meta name="description">`.
- **CSS:** define colors, fonts, and spacing as CSS variables in `:root`, taken from the reference analysis's recommended direction. Mobile first, with media queries for wider screens. Use Flexbox and Grid for layout. No inline styles.
- **JavaScript:** load scripts at the end of `body` or with `defer`. Use `const` and `let`, no global variables beyond what a library needs. The page content must still be readable if JavaScript fails.
- **Accessibility:** `alt` text for every meaningful image, enough color contrast, visible focus styles, and keyboard-reachable controls.
- **Animation:** respect `prefers-reduced-motion` by turning off or reducing motion for users who ask for it. Keep animations short and do not block reading.
- **Content:** use the real content from the material. Do not leave placeholder text. Do not copy text, logos, or brand assets from the references.
- **Fonts:** web fonts may be loaded from Google Fonts. Always set a fallback font stack.

## Libraries

- Use plain CSS and JavaScript first. Add a library only when an animation or effect needs it (for example, GSAP, AOS, Swiper, Lottie).
- When a library is needed, install it yourself without asking:
  1. Choose an exact, stable version (no `latest`).
  2. **Download** the distribution files (for example, the minified `.js` and `.css`) from the official release, npm registry, cdnjs, or jsDelivr.
  3. Save them in `libs/<library>-<version>/` together with the library's license file.
  4. Link them from `index.html` with relative paths. Do not load libraries from a CDN at run time.
- Do not use `npm install` in the output folder, and never commit `node_modules/`.
- Report every library you installed to the user: name, version, download URL, purpose, and license.

## Deployment (GitHub Pages)

- Deploy every finished page right away, **without asking the user first**.
- **Repository name:** the task name (`task_name`), which is the `<topic>` slug of the work (for example, `csat-2027-checklist`). One repository per task.
- **Owner:** the logged-in GitHub CLI account (`gh api user -q .login`). Do not hard-code it.
- **Visibility:** public, so that GitHub Pages works on a free account.
- **Description marker:** every repository created by this workflow has a description that ends with `[agent_09 web]`.

### Steps

1. Check the repository with `gh repo view <owner>/<task_name>`.
   - **Does not exist:** create it with `gh repo create <task_name> --public --description "<page title> [agent_09 web]"`.
   - **Exists and its description ends with `[agent_09 web]`:** it is an earlier version of the same task. Update it with the new version.
   - **Exists without the marker:** it is unrelated. Do not touch it. Stop and report the name conflict to the user.
2. Copy the version folder (without `screenshots/`) into a new temporary folder **outside this repository**, so that no nested Git repository is created inside it. For an existing repository, clone it into the temporary folder first and replace its files (everything except `.git/`) with the new version.
3. In the temporary folder, commit with the message `Deploy <task_name> v<N>`, tag the commit `v<N>`, and push the `main` branch and the tag.
4. Turn on GitHub Pages from the `main` branch root if it is not on yet:
   `gh api -X POST repos/<owner>/<task_name>/pages -f "source[branch]=main" -f "source[path]=/"`
5. Wait for the build (`gh api repos/<owner>/<task_name>/pages/builds/latest`) until its status is `built`, then open `https://<owner>.github.io/<task_name>/` in the browser and check that the page loads with its styles, scripts, and images.
6. Delete the temporary folder.
7. Give the user the deployed link and the repository link as Markdown links.

### Deployment safety

- Never commit secrets, tokens, `.env` files, or personal information.
- Never delete a repository, and never force-push to a repository without the `[agent_09 web]` marker.
- If a deployment step fails after two tries, stop and report the error with the command output.

## Check before reporting

- Check the page locally at 1440px and 390px wide: no broken layout, no text off the screen, no overlapping elements, no missing images, and no console errors.
- Check the deployed page the same way.
- Report: the output folder, the page plan, the libraries installed (or "none"), the deployed link, and the repository link.
