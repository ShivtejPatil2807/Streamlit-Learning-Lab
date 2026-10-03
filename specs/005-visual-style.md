# 005: Visual style

**Files:** `core/theme.py`, `.streamlit/config.toml`  **Status:** Implemented

## Purpose
One shared look for Home and every lesson page: colours, the hero, lesson
cards, level labels and function chips.

## Requirements
- **R1** `pill(text, kind)` returns a label with the class `lab-pill lab-<kind>`.
- **R2** HTML in the text passed to `pill` and `chips` is escaped, so lesson text
  can never inject markup.
- **R3** `level_pill(level)` uses the lower-case level as its colour class.
- **R4** Every level in `LEVELS` has a colour class in the stylesheet, so adding
  a level without a colour fails a test.
- **R5** `chips(names)` returns one chip per name, in order.
- **R6** Every lesson page shows its level, category and "Lesson N of M" under
  the page title.

## Notes
- Rules that target Streamlit's own elements (tabs, metrics, bordered
  containers) are cosmetic. If a Streamlit update renames those elements, the
  app keeps working and only the extra styling is lost.
- The theme colours live in `.streamlit/config.toml`. The extra styling lives in
  `core/theme.py`.
