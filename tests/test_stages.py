"""Tests for specs/016-level-stages.md (the level cards and their lessons on the Home page)."""

import re

from conftest import HOME
from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS, LEVELS


def load_home(completed=None) -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    assert not at.exception, at.exception
    return at


def open_stage(at: AppTest, level: str) -> AppTest:
    at.button(key=f"stage_{level.lower()}").click().run()
    assert not at.exception, at.exception
    return at


def blocks(at: AppTest, marker: str) -> list[str]:
    return [m.value for m in at.markdown if f'class="{marker}"' in m.value]


def card_numbers(at: AppTest) -> list[int]:
    """Lesson numbers of the lesson cards on the page, in the order shown."""
    return [
        int(re.search(r'lab-card-num">(\d+)<', b).group(1))
        for b in blocks(at, "lab-card-title")
    ]


def lessons_in(level: str) -> list:
    return [lesson for lesson in LESSONS if lesson.level == level]


def test_r1_there_is_no_all_lessons_list_search_or_filter():
    at = load_home()
    assert card_numbers(at) == []
    assert len(at.checkbox) == 0
    assert (
        len(at.text_input) == 0 and len(at.selectbox) == 0 and len(at.multiselect) == 0
    )
    assert "All lessons" not in [h.value for h in at.header]


def test_r2_there_is_one_card_per_level_in_order_with_its_counts():
    cards = blocks(load_home(), "lab-stage")
    assert len(cards) == len(LEVELS)
    for card, level in zip(cards, LEVELS):
        assert f'lab-card-name">{level}<' in card
        assert f"{len(lessons_in(level))} lessons" in card
        assert f"0 / {len(lessons_in(level))} done" in card


def test_r3_every_level_has_an_open_button_and_none_is_open_at_first():
    at = load_home()
    keys = [button.key for button in at.button]
    for level in LEVELS:
        assert f"stage_{level.lower()}" in keys
    assert "stage_close" not in keys
    assert not any("Showing below" in card for card in blocks(at, "lab-stage"))


def test_r4_opening_a_level_shows_exactly_its_lessons_in_course_order():
    for level in LEVELS:
        at = open_stage(load_home(), level)
        assert card_numbers(at) == [lesson.number for lesson in lessons_in(level)]
        assert [h.value for h in at.header][-1] == f"{level} lessons"
        assert [c.label for c in at.checkbox] == [
            lesson.done_label for lesson in lessons_in(level)
        ]


def test_r5_opening_another_level_replaces_the_first():
    at = open_stage(load_home(), "Beginner")
    open_stage(at, "Advanced")
    assert card_numbers(at) == [lesson.number for lesson in lessons_in("Advanced")]
    assert [h.value for h in at.header].count("Beginner lessons") == 0


def test_r6_the_open_level_says_so_and_the_others_do_not():
    at = open_stage(load_home(), "Intermediate")
    flags = ["Showing below" in card for card in blocks(at, "lab-stage")]
    assert flags == [level == "Intermediate" for level in LEVELS]


def test_r7_hiding_the_lessons_closes_the_level():
    at = open_stage(load_home(), "Beginner")
    at.button(key="stage_close").click().run()
    assert not at.exception, at.exception
    assert card_numbers(at) == []
    assert not any("Showing below" in card for card in blocks(at, "lab-stage"))


def test_r8_marking_a_lesson_done_updates_its_level_card():
    at = open_stage(load_home(), "Beginner")
    at.checkbox[0].check().run()
    assert not at.exception, at.exception
    beginner = blocks(at, "lab-stage")[0]
    assert f"1 / {len(lessons_in('Beginner'))} done" in beginner
    other = blocks(at, "lab-stage")[1]
    assert f"0 / {len(lessons_in('Intermediate'))} done" in other


def test_r9_every_lesson_belongs_to_exactly_one_level():
    assert all(lessons_in(level) for level in LEVELS), "a level with no lessons"
    assert sum(len(lessons_in(level)) for level in LEVELS) == len(LESSONS)


def test_r10_every_level_card_has_a_description():
    for card in blocks(load_home(), "lab-stage"):
        text = re.search(r'<p class="lab-summary">(.*?)</p>', card).group(1)
        assert len(text) >= 20
