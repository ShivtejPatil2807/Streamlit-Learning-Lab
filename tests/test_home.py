"""Tests for specs/003-home-page.md (Home.py), using Streamlit's AppTest."""
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


def cards(at: AppTest) -> int:
    """One 'Mark as done' checkbox is drawn per lesson card."""
    return len(at.checkbox)

def html_blocks(at: AppTest, marker: str) -> list[str]:
    """Markdown blocks that contain an element with this CSS class."""
    return [m.value for m in at.markdown if f'class="{marker}"' in m.value]

def test_r1_hero_shows_title_and_the_steps():
    at = load_home()
    hero = html_blocks(at, "lab-hero")[0]
    assert "Streamlit Learning Lab" in hero
    for step in ("Learn", "Code", "Try", "Challenge"):
        assert step in hero


def test_r2_stats_show_lessons_functions_and_completed():
    at = load_home()
    values = {m.label: m.value for m in at.metric}
    assert values["Lessons"] == str(len(LESSONS))
    assert values["Functions covered"] == str(total_functions())
    assert values["Completed"] == f"0 / {len(LESSONS)}"


def test_all_lessons_are_shown_by_default():
    assert cards(load_home()) == len(LESSONS)


def test_r4_search_matches_ignoring_case_and_spaces():
    at = load_home()
    at.text_input[0].set_value("  CHART ").run()
    assert cards(at) == 1  # only the Charts lesson mentions "chart"


def test_r4_search_also_matches_function_names():
    at = load_home()
    at.text_input[0].set_value("st.form_submit_button").run()
    assert cards(at) == 1  # only the Forms lesson


def test_r5_category_filter():
    at = load_home()
    at.selectbox[0].select("Data & Charts").run()
    expected = sum(1 for item in LESSONS if item.category == "Data & Charts")
    assert cards(at) == expected > 0


def test_r6_level_filter():
    at = load_home()
    at.multiselect[0].set_value(["Advanced"]).run()
    expected = sum(1 for item in LESSONS if item.level == "Advanced")
    assert cards(at) == expected > 0


def test_r7_filters_combine():
    at = load_home()
    at.selectbox[0].select("Data & Charts").run()
    at.multiselect[0].set_value(["Beginner"]).run()
    expected = sum(
        1 for item in LESSONS
        if item.category == "Data & Charts" and item.level == "Beginner"
    )
    assert cards(at) == expected > 0


def test_r8_completed_lesson_card_shows_a_done_label():
    at = load_home(completed={1})
    cards_html = html_blocks(at, "lab-card-title")
    assert len(cards_html) == len(LESSONS)
    assert sum("✓ Done" in block for block in cards_html) == 1
    assert "✓ Done" in cards_html[0]

def test_r9_no_match_shows_a_warning():
    at = load_home()
    at.text_input[0].set_value("zzzz-no-such-lesson").run()
    assert cards(at) == 0
    assert len(at.warning) == 1


def test_r10_mark_as_done_updates_the_completed_count():
    at = load_home()
    at.checkbox[0].check().run()
    values = {m.label: m.value for m in at.metric}
    assert values["Completed"] == f"1 / {len(LESSONS)}"


def test_r12_next_up_points_to_the_first_unfinished_lesson():
    at = load_home(completed={1, 2})
    assert any(c.value == "Next up: 3. Layouts" for c in at.caption)
    assert len(at.success) == 0


def test_r13_all_done_shows_a_success_message():
    at = load_home(completed={lesson.number for lesson in LESSONS})
    assert len(at.success) == 1
    assert not any("Next up" in c.value for c in at.caption)
