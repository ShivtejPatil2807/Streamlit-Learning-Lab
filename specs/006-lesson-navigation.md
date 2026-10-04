# 006: Lesson navigation

**Files:** `core/lessons.py` (`neighbours`), `core/components.py` (`lesson_footer`)
**Status:** Implemented

## Purpose
Let learners move through the course without going back to the Home page:
a Previous button, a Home button and a Next button at the end of every lesson.

## Requirements
- **R1** `neighbours(number)` returns `(None, next)` for the first lesson and
  `(previous, None)` for the last lesson.
- **R2** For every other lesson, `neighbours` returns the lessons numbered one
  lower and one higher.
- **R3** Every lesson ends with a "Home" button.
- **R4** Every lesson except the first has a Previous button, labelled
  `← <previous title>`.
- **R5** Every lesson except the last has a Next button, labelled
  `<next title> →`.
- **R6** Buttons appear in this order: Previous, Home, Next.
- **R7** Clicking a button opens that page. This is checked by hand, because
  Streamlit's test tool cannot follow page switches.
