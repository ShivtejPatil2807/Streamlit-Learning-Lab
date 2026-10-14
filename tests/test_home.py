"""Tests for specs/003-home-page.md (the core of Home.py), using Streamlit's AppTest."""
from conftest import HOME
from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS, total_functions


def load_home(completed=None) -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    assert not at.exception, at.exception
    return at


def html_blocks(at: AppTest, marker: str) -> list[str]:
    """Markdown blocks that contain an element with this CSS class."""
    return [m.value for m in at.markdown if f'class="{marker}"' in m.value]


def test_r1_hero_shows_the_title_and_the_steps():
    hero = html_blocks(load_home(), "lab-hero")[0]
    assert "Streamlit Learning Lab" in hero
    for step in ("Learn", "Code", "Try", "Challenge"):
        assert step in hero
    assert '",' not in hero  # stray Python quotes would show on the page


def test_r2_stats_show_lessons_functions_and_completed():
    values = {m.label: m.value for m in load_home().metric}
    assert values["Lessons"] == str(len(LESSONS))
    assert values["Functions covered"] == str(total_functions())
    assert values["Completed"] == f"0 / {len(LESSONS)}"


def test_r3_completed_lessons_are_remembered_for_the_session():
    at = load_home(completed={1, 2})
    values = {m.label: m.value for m in at.metric}
    assert values["Completed"] == f"2 / {len(LESSONS)}"
    at.run()  # a rerun keeps them
    assert {m.label: m.value for m in at.metric}["Completed"] == f"2 / {len(LESSONS)}"


def test_r4_marking_a_lesson_as_done_updates_the_completed_count():
    at = load_home()
    at.button(key="stage_beginner").click().run()
    at.checkbox[0].check().run()
    assert not at.exception, at.exception
    values = {m.label: m.value for m in at.metric}
    assert values["Completed"] == f"1 / {len(LESSONS)}"


def test_r5_next_up_points_to_the_first_unfinished_lesson():
    at = load_home(completed={1, 2})
    assert any(c.value == "Next up: 3. Layouts" for c in at.caption)
    assert len(at.success) == 0


def test_r6_when_everything_is_done_a_success_message_replaces_next_up():
    at = load_home(completed={lesson.number for lesson in LESSONS})
    assert len(at.success) == 1
    assert not any("Next up" in c.value for c in at.caption)
