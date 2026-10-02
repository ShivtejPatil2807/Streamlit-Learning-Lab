# 001: Lesson registry

**File:** `core/lessons.py`  **Status:** Implemented

## Purpose
One list that describes every lesson. The Home page, the page headers and the
tests all read from it, so a lesson is described in exactly one place.

## Data model
Each `Lesson` is a frozen dataclass with: `number`, `title`, `icon`, `file`,
`category`, `level`, `summary`, `functions`.

## Requirements
- **R1** Lesson numbers are unique and run 1..N with no gaps.
- **R2** Every `file` exists inside `pages/`.
- **R3** Every `file` starts with its two-digit number (lesson 5 -> `05_...`).
- **R4** Every `category` is listed in `CATEGORIES`.
- **R5** Every `level` is listed in `LEVELS`.
- **R6** `title`, `summary` and `functions` are never empty.
- **R7** `Lesson.path` returns `"pages/" + file`.
- **R8** `total_functions()` equals the sum of every lesson's `functions` length.
- **R9** Every page in `pages/` has a registry entry (no orphan pages).

## Adding a lesson
1. Create `pages/NN_Name.py`.
2. Add a `Lesson(...)` entry to `LESSONS`.
3. Run the tests. R1-R9 catch most mistakes.
