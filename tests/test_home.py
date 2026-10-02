"""Tests for specs/003-home-page.md (Home.py), using Streamlit's AppTest."""
from streamlit.testing.v1 import AppTest

from conftest import HOME
from core.lessons import LESSONS, total_functions


def load_home() -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    at.run()
    assert not at.exception, at.exception
    return at


def cards(at: AppTest) -> int:
    """One 'Mark as done' checkbox is drawn per lesson card."""
    return len(at.checkbox)


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
