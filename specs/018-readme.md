# 018: README

**Files:** `README.md`, `LICENSE`, `scripts/update_readme.py`
**Status:** Implemented

## Purpose
The README is the first thing a visitor reads. It must be accurate: no old lesson
counts, no features that were removed, no links to files that do not exist. The
tables that list the course are generated from the data files, so they cannot
drift.

## Requirements
- **R1** The README has one pair of markers (`<!-- course:start -->` and
  `<!-- course:end -->`) around the generated course tables.
- **R2** The text between the markers equals what `scripts/update_readme.py` would
  write. The failure message says how to fix it: `python -m scripts.update_readme`.
- **R3** Every lesson in `data/lessons.yaml` is linked from the README.
- **R4** Every relative link in the README points to a file that exists.
- **R5** The project tree lists only files and folders that exist.
- **R6** The license is MIT everywhere: the badge, the License section and the
  `LICENSE` file. The old "educational use" sentence is gone.
- **R7** "Adding a lesson" points to the three data files and not to Python code.
- **R8** The text written by hand does not describe removed features (the old
  lesson count, the old Home page filters).
- **R9** The Python badge lists the same versions that CI tests.

## Notes
- The hand-written parts (badges, tips, the project tree) are checked by the tests
  above, but still need a person to keep them true.
- The Streamlit badge says 1.40+ because that is the first version with `st.pills`
  (lesson 16). CI tests only the latest Streamlit, so older versions are not
  tested.
