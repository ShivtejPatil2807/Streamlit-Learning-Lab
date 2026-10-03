# 003: Home page

**File:** `Home.py`  **Status:** Implemented

## Purpose
Landing page: shows what the Lab covers and lets the learner find, open and
track lessons.

## Requirements
- **R1** Shows a hero section with the title, a short description and the
  Learn -> Code -> Try -> Challenge steps.
- **R2** Shows three stats: number of lessons, functions covered, and
  completed lessons as `done / total`.
- **R3** Shows a progress bar equal to `completed / total lessons`.
- **R4** Search matches the lesson title, summary or any function name,
  ignoring case and surrounding spaces.
- **R5** The category filter shows all lessons for "All", otherwise only that
  category.
- **R6** The level filter shows only the selected levels.
- **R7** Search, category and level filters combine (a lesson must pass all).
- **R8** Each lesson card shows icon, number, title, level, category, summary,
  its first four functions, and a link that opens the lesson page. A completed
  lesson also shows a "Done" label.
- **R9** If no lesson matches, a warning is shown instead of cards.
- **R10** "Mark as done" updates the completed count and the progress bar.
- **R11** Completed lessons are kept in `st.session_state`, so they survive page
  navigation but reset when the browser tab is refreshed.
- **R12** While some lessons are not completed, a "Next up" line and a
  "Continue" link point to the first lesson that is not completed.
- **R13** When every lesson is completed, a success message replaces the
  "Continue" link.

## Out of scope (for now)
- Saving progress permanently (file or database).
