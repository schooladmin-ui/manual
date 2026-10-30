---
name: "canva-to-html-guide"
description: "Use when converting a visible Canva slide deck or manual into a concise scrollable HTML guide with matched instructional images and modal previews for the 온라인교무실 매뉴얼 portal."
---

# Canva slide manual to HTML guide

1. Attach the active Canva tab and inspect it with `snapshot()`. Use the viewer's accessible previous/next controls and confirm the page number after every navigation.
2. For each slide, collect visible slide text from the rendered slide container (often `div._mXnjA` with a nonzero bounding box). Also collect nested image URLs and capture the visible slide container as a PNG when exact visual evidence is needed. Never include Canva's surrounding toolbar or editor chrome in the output. If standalone PNG screenshots are saved in the workspace, store them under the `images/` directory.
3. Build a concise, scrollable Korean HTML guide wrapped in `<main class="page">...</main>`:
   - Keep the layout to one page only when the content fits naturally; otherwise allow vertical scrolling instead of omitting or over-compressing information.
   - Use `<header><div class="title-row"><h1><span class="title-highlight">...</span></h1><a class="source-button" href="<canva-url>" target="_blank" rel="noopener">원본 Canva 슬라이드 열기</a></div><p class="lead">...</p></header>` (omit the `.source-button` link if there is no source Canva URL).
   - Convert slide content into a small number of numbered action steps (`.steps` / `.step` with `.step-head` or `.step-top`, and `.num`).
   - Apply a yellow highlighter effect to the main title using a text-sized `.title-highlight` wrapper, not a full-width block background.
   - Move warnings into a prominent `.notice` callout with larger, bold text, and highlight key step cautions with `.important` or `.hint`.
   - Put troubleshooting cases in separate numbered `.panel` blocks inside `.lower`, or group multi-track guides using `.two-col-sections` and `.section`.
   - Remove redundant setup steps when they do not explain the requested task.
   - Match each instructional image to the step it actually illustrates; use slide text and the captured visual to verify the mapping.
4. Embed the selected PNGs as base64 data URLs (`data-image="data:image/png;base64,..."` or `data-images="[...]"`) so the delivered HTML is self-contained. Keep the page responsive and print-friendly.
5. Put a magnifying-glass button (`🔍`, `class="img-toggle"`) at the top-right of every panel/step that has an image. Give it `aria-label` and `title` of `이미지 보기`. Clicking it must open a large modal dialog containing the matched image. Support a close button, backdrop click, and Escape key. Keep the modal image constrained to the viewport while allowing it to be viewed large.
6. Verify the generated HTML by injecting it into an `about:blank` tab, taking a fresh snapshot, confirming the expected number of buttons, clicking at least one button, and confirming that a dialog with the correct image appears.
7. Save the final standalone HTML file into the project's `pages/` directory (`pages/<manual-slug>.html`) and also keep a copy under the session's `artifacts` directory when requested:
   - Register or update the manual entry in `bundle_manuals.py` (`MANUALS` list).
   - Run `python bundle_manuals.py` from the workspace root to rebuild `index.html` so the portal navigation bar and embedded panes include the updated guide.
   - Verify the destination files (`pages/<manual-slug>.html` and `index.html`) after building.
