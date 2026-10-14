# 003: Home page

**File:** `Home.py`  **Status:** Implemented

The layout is described in spec 015, the learning paths in spec 012 and the level
cards in spec 016. This spec covers the basics.

## Purpose
Landing page: shows what the Lab is, tracks the learner's progress and points to
the next lesson.

## Requirements
- **R1** Shows a hero section with the title, a short description and the
  Learn → Code → Try → Challenge steps.
- **R2** Shows three stats: number of lessons, functions covered, and completed
  lessons as `done / total`.
- **R3** Completed lessons are kept in `st.session_state`, so they survive page
  navigation but reset when the browser tab is refreshed.
- **R4** Marking a lesson as done updates the completed count.
- **R5** While some lessons are not completed, a "Next up" line names the first
  lesson that is not completed.
- **R6** When every lesson is completed, a success message replaces the "Next up"
  line.

## History
- The search box, the category, level and path filters and the "All lessons"
  list were removed. Lessons are now reached through the level cards (spec 016)
  and the learning paths (spec 012).

## Out of scope (for now)
- Saving progress permanently (file or database).
