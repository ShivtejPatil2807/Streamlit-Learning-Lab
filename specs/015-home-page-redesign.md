# 015: Professional Home page

**Files:** `Home.py`, `core/theme.py`, `.streamlit/config.toml`
**Status:** Implemented

Builds on spec 003 (what the Home page does) and spec 012 (learning paths). This
spec covers the layout: what a new visitor sees first and what they can do next.

## Purpose
A visitor should understand in a few seconds what the site is, see their
progress, and know the one thing to click next. Everything else (what is
included, the paths, the full lesson list) follows in order of importance.

## Requirements
- **R1** The page is laid out in this order: hero, three stats, a "next step"
  panel, "What you get", "Learning paths", "All lessons", footer.
- **R2** The next-step panel shows the progress bar, the "Next up" line and one
  primary button. The button says "Start learning" for a new visitor and
  "Continue" once a lesson is done. It opens the first lesson that is not
  completed. (Opening the lesson is checked by hand.)
- **R3** When every lesson is done, the panel shows a success message and no
  button.
- **R4** The section titles are real headings, in this order: What you get,
  Learning paths, All lessons.
- **R5** "What you get" has four tiles: Learn → Code → Try, Challenges, Real
  projects and Take it home.
- **R6** The lesson list says "Showing N of M lessons" and changes with the
  filters.
- **R7** The page ends with a footer that links to the source on GitHub, to the
  issue page, and to the Streamlit docs.
- **R8** White text on the primary button has a contrast of at least 4.5:1
  against the primary colour in `.streamlit/config.toml`.
- **R9** The stylesheet defines the styles for the tiles and the footer.

## Notes
- Section titles use `st.header` so that the page has a proper heading outline
  (the hero title is the only level-1 heading).
- Spec 003 still applies. Its R12 and R13 (the "Next up" line and the success
  message) are now shown inside the next-step panel.
