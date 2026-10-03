"""Smoke test: every lesson page runs from top to bottom without an error."""
from conftest import ROOT
from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS

# AppTest runs one page on its own, without the multipage app around it.
# st.page_link() needs that context, so these pages cannot run here.
# They are still compiled below, which catches syntax errors.
NEEDS_MULTIPAGE_CONTEXT = {"13_Navigation.py"}


def test_every_lesson_page_runs_without_errors():
    failures = []
    for lesson in LESSONS:
        path = ROOT / lesson.path
        if lesson.file in NEEDS_MULTIPAGE_CONTEXT:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
            continue
        at = AppTest.from_file(str(path), default_timeout=30)
        at.run()
        if at.exception:
            failures.append(f"{lesson.file}: {at.exception[0].value}")
    assert not failures, "\n".join(failures)