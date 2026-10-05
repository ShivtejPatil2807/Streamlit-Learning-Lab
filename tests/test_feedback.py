"""Tests for specs/008-lesson-feedback.md (core/feedback.py and the footer button)."""
from textwrap import dedent
from urllib.parse import parse_qs, urlparse

from streamlit.testing.v1 import AppTest

from core.export import REPO_URL
from core.feedback import feedback_url
from core.lessons import LESSONS


def fields(lesson) -> dict[str, str]:
    query = urlparse(feedback_url(lesson)).query
    return {key: values[0] for key, values in parse_qs(query).items()}


def test_r1_link_points_to_the_new_issue_page():
    for lesson in LESSONS:
        assert feedback_url(lesson).startswith(f"{REPO_URL}/issues/new?")


def test_r2_title_has_the_lesson_number_and_title():
    for lesson in LESSONS:
        title = fields(lesson)["title"]
        assert str(lesson.number) in title
        assert lesson.title in title


def test_r3_body_names_the_lesson_and_asks_what_was_wrong():
    for lesson in LESSONS:
        body = fields(lesson)["body"]
        assert f"{lesson.number}. {lesson.title}" in body
        assert lesson.path in body
        assert "unclear, wrong or missing" in body


def test_r4_link_has_no_spaces_or_line_breaks():
    for lesson in LESSONS:
        url = feedback_url(lesson)
        assert " " not in url
        assert "\n" not in url


def test_r5_decoding_gives_back_the_original_text():
    lesson = next(item for item in LESSONS if "&" in item.title)  # "&" must survive encoding
    assert fields(lesson)["title"] == f"Feedback on lesson {lesson.number}: {lesson.title}"


def test_r6_every_lesson_page_has_a_feedback_button(tmp_path):
    for lesson in LESSONS:
        page = tmp_path / f"feedback_{lesson.number}.py"
        page.write_text(
            dedent(
                f"""
                from core.components import lesson_footer, lesson_page

                lesson_page({lesson.number})
                lesson_footer({lesson.number})
                """
            ),
            encoding="utf-8",
        )
        at = AppTest.from_file(str(page), default_timeout=30)
        at.run()
        assert not at.exception, at.exception
        assert len(at.get("link_button")) == 1, lesson.file
