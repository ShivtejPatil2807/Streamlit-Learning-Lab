# 016: Level stages

**Files:** `Home.py`
**Status:** Implemented

## Purpose
Instead of one long list of 22 lessons with search and filters, the Home page
offers three stages, Beginner, Intermediate and Advanced. A learner picks a stage
and only then sees its lessons. It is simpler, and it tells a newcomer where to
start.

## Requirements
- **R1** The Home page has no "All lessons" list, no search box and no filters.
  Lessons appear only after a stage is opened.
- **R2** "Choose your level" shows one card per level, in the order Beginner,
  Intermediate, Advanced. Each card shows the number of lessons and how many are
  done ("done / total").
- **R3** Every card has an "Open <level>" button. When the page first loads, no
  stage is open.
- **R4** Opening a level shows exactly that level's lessons, in course order, under
  the heading "<level> lessons". Each lesson card has its number, title, level,
  category, summary and functions, an "Open <title>" link and a "Mark <title> as
  done" checkbox.
- **R5** Only one stage is open at a time. Opening another replaces the first.
- **R6** The open level's card says "Showing below" and its button is the
  highlighted (primary) one. The other cards do not say it.
- **R7** "Hide these lessons" closes the open level.
- **R8** Marking a lesson as done updates the "done / total" on its level card and
  the stats at the top.
- **R9** Every lesson belongs to exactly one level, and every level has lessons.
- **R10** Every level card has a short description.

## Notes
- Which stage is open is kept in `st.session_state`, so it survives reruns but not
  a page refresh.
- The descriptions of the stages live in `STAGE_INFO` in `Home.py`. A new level
  in `data/lessons.yaml` still works without one: its card gets a default icon and
  no description (the tests ask for one, so you would add it).
