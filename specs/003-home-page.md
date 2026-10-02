# 003: Home page

**File:** `Home.py`  **Status:** Implemented

## Purpose
Landing page: shows what the Lab covers and lets the learner find, open and
track lessons.

## Requirements
- **R1** Shows a title and short description (hero section).
- **R2** Shows three stats: number of lessons, functions covered, and
  completed lessons as `done / total`.
- **R3** Shows a progress bar equal to `completed / total lessons`.
- **R4** Search matches the lesson title, summary or any function name,
  ignoring case and surrounding spaces.
- **R5** The category filter shows all lessons for "All", otherwise only that
  category.
- **R6** The level filter shows only the selected levels.
- **R7** Search, category and level filters combine (a lesson must pass all).
- **R8** Each lesson card shows icon, number, title, category, level, summary,
  its first four functions, and a link that opens the lesson page.
- **R9** If no lesson matches, a warning is shown instead of cards.
- **R10** "Mark as done" updates the completed count and the progress bar.
- **R11** Completed lessons are kept in `st.session_state`, so they survive page
  navigation but reset when the browser tab is refreshed.

## Out of scope (for now)
- Saving progress permanently (file or database).
