"""Tests for specs/004-challenges-and-progress.md (lesson_footer and Home)."""
from textwrap import dedent

from conftest import HOME
from streamlit.testing.v1 import AppTest

from core.challenges import CHALLENGES
from core.lessons import LESSONS


def run_footer(tmp_path, number: int, completed=None) -> AppTest:
    page = tmp_path / "footer_page.py"
    page.write_text(
        dedent(
            f"""
            from core.components import lesson_footer, lesson_page

            lesson_page({number})
            lesson_footer({number})
            """
        ),
        encoding="utf-8",
    )
    at = AppTest.from_file(str(page), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    assert not at.exception, at.exception
    return at


def test_r3_one_question_per_challenge_with_nothing_selected(tmp_path):
    at = run_footer(tmp_path, 9)  # lesson 9 has two challenges
    assert len(at.radio) == len(CHALLENGES[9]) == 2
    assert all(radio.value is None for radio in at.radio)


def test_r4_right_answer_shows_success_with_the_explanation(tmp_path):
    at = run_footer(tmp_path, 1)
    item = CHALLENGES[1][0]
    at.radio[0].set_value(item.options[item.answer]).run()
    assert len(at.success) == 1
    assert item.explanation in at.success[0].value


def test_r5_wrong_answer_shows_error_and_hides_the_answer(tmp_path):
    at = run_footer(tmp_path, 1)
    item = CHALLENGES[1][0]
    wrong = next(o for i, o in enumerate(item.options) if i != item.answer)
    at.radio[0].set_value(wrong).run()
    assert len(at.error) == 1
    assert len(at.success) == 0
    assert item.explanation not in at.error[0].value


def test_r6_checkbox_is_unticked_when_lesson_is_not_completed(tmp_path):
    at = run_footer(tmp_path, 3)
    assert at.checkbox[0].label == "Mark this lesson as done"
    assert at.checkbox[0].value is False


def test_r6_checkbox_is_ticked_when_lesson_is_completed(tmp_path):
    at = run_footer(tmp_path, 3, completed={3})
    assert at.checkbox[0].value is True


def test_r7_ticking_and_unticking_updates_the_completed_set(tmp_path):
    at = run_footer(tmp_path, 3)
    at.checkbox[0].check().run()
    assert at.session_state["completed"] == {3}
    at.checkbox[0].uncheck().run()
    assert at.session_state["completed"] == set()


def test_r8_home_counts_lessons_completed_on_their_own_pages():
    at = AppTest.from_file(str(HOME), default_timeout=30)
    at.session_state["completed"] = {1, 2}
    at.run()
    assert not at.exception, at.exception
    values = {m.label: m.value for m in at.metric}
    assert values["Completed"] == f"2 / {len(LESSONS)}"
