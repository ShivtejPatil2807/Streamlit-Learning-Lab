# 007: Download a lesson as a .py file

**Files:** `core/export.py` (`build_script`), `core/components.py` (`lesson_footer`)
**Status:** Implemented

## Purpose
Let a learner take a lesson home and run it on their own computer with
`streamlit run`. The lesson pages need the rest of the project (`core/`), so the
download is a rewritten, self-contained version of the page.

## Requirements
- **R1** `build_script(number)` returns valid Python for every lesson.
- **R2** The script uses no project helpers: no import from `core`, and no calls
  to `lesson_page`, `demo`, `section`, `show_setup` or `lesson_footer`.
- **R3** The first Streamlit call is `st.set_page_config`.
- **R4** Every demo and section keeps its number and title as a numbered
  `st.header`, counting 1, 2, 3, ... in order.
- **R5** The code of every demo is copied from the page, including its comments.
  Helper functions for sample data are kept, without their decorator.
- **R6** The script starts with a docstring that says how to run it, with the
  `pip install` line listing the packages the lesson imports.
- **R7** Demos that cannot run on their own (they need a secrets file or a
  multipage app) are kept as commented-out code with a note saying why.
- **R8** Every lesson page shows a download button for its script.

## Notes
- The script is built from the page file each time (and cached), so the download
  can never go out of date with the lesson.
