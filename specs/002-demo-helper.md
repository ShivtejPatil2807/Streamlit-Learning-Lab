# 002: Demo helper

**File:** `core/components.py`  **Status:** Implemented

## Purpose
Show the code and its live output from a single source, so what is displayed
can never differ from what runs.

## Public functions
- `lesson_page(number, intro=None)` page setup
- `demo(title, description, *, run=True, caption=None)` decorator
- `section(title, description=None)` numbered section without code
- `show_setup(func)` shows a helper's code in an expander

## Requirements
- **R1** `lesson_page` is the first Streamlit call on a page. It sets the tab
  title and icon from the registry.
- **R2** `lesson_page` shows the page title (icon + title) and the intro text.
  Without `intro` it uses the lesson summary.
- **R3** Section numbers start at 1 on every run and increase by one for each
  `demo` or `section`.
- **R4** `demo` shows the decorated function's body (not the decorator or the
  `def` line, dedented) as Python code.
- **R5** `demo` runs the function after showing the code, unless `run=False`.
- **R6** With `run=False` the function is never called.
- **R7** `caption`, when given, appears after the output.
- **R8** `show_setup` returns the function unchanged so it can still be called.

## Limits
- The decorated function must be defined in a `.py` file (its source has to be
  readable).
- Demo bodies must not depend on variables defined inside other demos.
