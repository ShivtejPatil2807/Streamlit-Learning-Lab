"""Structural checks on the lesson pages.

Pure Python: the pages are parsed, not run, so no Streamlit is needed.
"""
import ast

from conftest import PAGES_DIR

from core.lessons import LESSONS


def _calls(lesson):
    tree = ast.parse((PAGES_DIR / lesson.file).read_text(encoding="utf-8"))
    return [node for node in ast.walk(tree) if isinstance(node, ast.Call)]


def _name(call):
    func = call.func
    return getattr(func, "id", None) or getattr(func, "attr", None)


def test_every_page_calls_lesson_page_once_with_its_own_number():
    for lesson in LESSONS:
        numbers = [
            call.args[0].value
            for call in _calls(lesson)
            if _name(call) == "lesson_page"
            and call.args
            and isinstance(call.args[0], ast.Constant)
        ]
        assert numbers == [lesson.number], (
            f"{lesson.file} should call lesson_page({lesson.number}) exactly once"
        )


def test_pages_do_not_call_set_page_config_themselves():
    # lesson_page() already calls it, and a second call raises an error.
    for lesson in LESSONS:
        offenders = [c for c in _calls(lesson) if _name(c) == "set_page_config"]
        assert not offenders, f"{lesson.file} calls set_page_config directly"
