"""Tests for specs/006-lesson-navigation.md."""
from textwrap import dedent

from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS, neighbours


def footer_buttons(tmp_path, number: int) -> list[str]:
    page = tmp_path / "nav_page.py"
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
    at.run()
    assert not at.exception, at.exception
    return [button.label for button in at.button]


def test_r1_first_lesson_has_no_previous_and_last_has_no_next():
    assert neighbours(LESSONS[0].number) == (None, LESSONS[1])
    assert neighbours(LESSONS[-1].number) == (LESSONS[-2], None)


def test_r2_every_other_lesson_has_its_numeric_neighbours():
    for lesson in LESSONS[1:-1]:
        previous, following = neighbours(lesson.number)
        assert previous.number == lesson.number - 1
        assert following.number == lesson.number + 1


def test_r3_r4_r6_first_lesson_shows_home_then_next(tmp_path):
    assert footer_buttons(tmp_path, LESSONS[0].number) == [
        "🏠 Home",
        f"{LESSONS[1].title} →",
    ]


def test_r5_last_lesson_shows_previous_then_home(tmp_path):
    assert footer_buttons(tmp_path, LESSONS[-1].number) == [
        f"← {LESSONS[-2].title}",
        "🏠 Home",
    ]


def test_r6_middle_lesson_shows_previous_home_next_in_order(tmp_path):
    middle = LESSONS[4]
    assert footer_buttons(tmp_path, middle.number) == [
        f"← {LESSONS[3].title}",
        "🏠 Home",
        f"{LESSONS[5].title} →",
    ]
