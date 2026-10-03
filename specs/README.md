# Specs

A spec says what a part of the app **must do**, in short numbered requirements.
Tests (see `tests/`) check those requirements, and each test names the
requirement it covers (for example `R3`).

| Spec | Covers | Status |
|------|--------|--------|
| [001-lesson-registry.md](001-lesson-registry.md) | `core/lessons.py` | Implemented |
| [002-demo-helper.md](002-demo-helper.md) | `core/components.py` | Implemented |
| [003-home-page.md](003-home-page.md) | `Home.py` | Implemented |
| [004-challenges-and-progress.md](004-challenges-and-progress.md) | `core/challenges.py`, `lesson_footer` | Implemented |

## How to write a new spec

1. Copy an existing spec and change the title.
2. Write requirements that a test can answer with yes or no.
3. Add it to the table above.
4. Change the status to *Implemented* once the code and its tests exist.
