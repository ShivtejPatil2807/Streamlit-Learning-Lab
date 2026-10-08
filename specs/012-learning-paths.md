# 012: Learning paths

**Files:** `core/paths.py`, `Home.py`
**Status:** Implemented

## Purpose
With 22 lessons, a new visitor does not know where to start. A learning path is
a short, ordered list of lessons that leads to a goal, such as "Build a chatbot".
The Home page shows the paths, tracks progress along each one, and can show only
a path's lessons.

## Requirements
- **R1** Every path has a unique slug, a unique title, and at least three lessons.
- **R2** Every lesson number in a path exists in the registry, and no lesson
  appears twice in the same path.
- **R3** A lesson in the category "Projects" can only be the last lesson of a
  path, because a project is where the path leads.
- **R4** `path_progress(path, completed)` returns how many of the path's lessons
  are done and how many it has. Lessons outside the path do not count.
- **R5** `next_in_path(path, completed)` returns the first lesson of the path, in
  the path's order, that is not completed, or None when all are done.
- **R6** The Home page shows one card per path with its title, its number of
  lessons and "done / total".
- **R7** A completed path shows "Path completed" instead of a link. Other paths
  show a link to their next lesson, labelled "Start" or "Continue". This link is
  checked by hand.
- **R8** The "Learning path" filter starts on "All lessons". Choosing a path shows
  only that path's lessons, in the path's order.
- **R9** The path filter combines with the search, category and level filters.

## Notes
- Path cards use their own CSS class (`lab-path`), so they are never counted as
  lesson cards.
- A path is data, not code: add one by adding a `LearningPath(...)` to `PATHS`.
