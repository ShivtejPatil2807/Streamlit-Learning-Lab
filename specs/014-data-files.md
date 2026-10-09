# 014: Lessons from data files

**Files:** `data/lessons.yaml`, `data/challenges.yaml`, `data/paths.yaml`,
`core/lessons.py`, `core/challenges.py`, `core/paths.py`
**Status:** Implemented

## Purpose
Describe the course in plain data files, so adding a lesson, a question or a
learning path means editing text, not Python. The lesson demos stay in Python
(`pages/`), because the code a learner reads is the code that runs.

## Requirements
- **R1** The lessons, their challenges and the learning paths live in
  `data/*.yaml`. No lesson text is left in the Python modules.
- **R2** The three files are UTF-8 YAML and load without errors.
- **R3** A lesson, challenge or path entry with a missing field is rejected with
  a message that names the file, the entry and the field.
- **R4** A challenge whose answer does not point to one of its options is
  rejected with a message that names the lesson and the question.
- **R5** Adding a lesson needs no Python code: a new entry in the lessons file
  appears in the loaded registry.
- **R6** The modules keep their public names (`LESSONS`, `CATEGORIES`, `LEVELS`,
  `CHALLENGES`, `PATHS`), so the Home page, the lesson pages and the other
  modules did not need to change.

## Notes
- Every other rule about the data (unique numbers, existing page files, known
  categories and levels, a challenge for every lesson, valid paths) is checked
  by the tests in specs 001, 004 and 012. They run on the loaded data.
- Requires `pyyaml` in `requirements.txt`.
- Strings that YAML could read as another type (for example `False` or `3`) must
  be in quotes. The tests would notice, because the option would stop being text.
