"""Smoke test: every lesson page runs from top to bottom without an error."""
from streamlit.testing.v1 import AppTest

from conftest import ROOT
from core.lessons import LESSONS


def test_every_lesson_page_runs_without_errors():
    failures = []
    for lesson in LESSONS:
        at = AppTest.from_file(str(ROOT / lesson.path), default_timeout=30)
        at.run()
        if at.exception:
            failures.append(f"{lesson.file}: {at.exception[0].value}")
    assert not failures, "\n".join(failures)
