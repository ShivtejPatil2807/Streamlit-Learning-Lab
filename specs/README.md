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
| [005-visual-style.md](005-visual-style.md) | `core/theme.py`, `.streamlit/config.toml` | Implemented |
| [006-lesson-navigation.md](006-lesson-navigation.md) | `neighbours`, Previous / Home / Next buttons | Implemented |
| [007-lesson-download.md](007-lesson-download.md) | `core/export.py`, download button | Implemented |
| [008-lesson-feedback.md](008-lesson-feedback.md) | `core/feedback.py`, feedback button | Implemented |
| [009-iris-classifier.md](009-iris-classifier.md) | `pages/20_Project_Iris_Classifier.py` | Implemented |
| [010-sales-dashboard.md](010-sales-dashboard.md) | `pages/21_Project_Sales_Dashboard.py` | Implemented |

## How to write a new spec

1. Copy an existing spec and change the title.
2. Write requirements that a test can answer with yes or no.
3. Add it to the table above.
4. Change the status to *Implemented* once the code and its tests exist.
