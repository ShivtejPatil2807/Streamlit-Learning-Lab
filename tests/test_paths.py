"""Tests for specs/012-learning-paths.md (core/paths.py and the path cards on the Home page)."""

from conftest import HOME
from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS
from core.paths import PATHS, next_in_path, path_lessons, path_progress

NUMBERS = {lesson.number for lesson in LESSONS}


def load_home(completed=None) -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    assert not at.exception, at.exception
    return at


def blocks(at: AppTest, marker: str) -> list[str]:
    """Markdown blocks that contain an element with this CSS class."""
    return [m.value for m in at.markdown if f'class="{marker}"' in m.value]


def test_r1_paths_have_unique_names_and_enough_lessons():
    assert len({path.slug for path in PATHS}) == len(PATHS)
    assert len({path.title for path in PATHS}) == len(PATHS)
    for path in PATHS:
        assert len(path.lessons) >= 3, path.title


def test_r2_path_lessons_exist_and_are_not_repeated():
    for path in PATHS:
        assert set(path.lessons) <= NUMBERS, path.title
        assert len(set(path.lessons)) == len(path.lessons), path.title
        assert [lesson.number for lesson in path_lessons(path)] == list(path.lessons)


def test_r3_a_project_can_only_be_the_last_lesson_of_a_path():
    projects = {lesson.number for lesson in LESSONS if lesson.category == "Projects"}
    for path in PATHS:
        assert not projects & set(path.lessons[:-1]), path.title


def test_r4_progress_counts_only_the_lessons_of_the_path():
    path = PATHS[0]
    assert path_progress(path, set()) == (0, len(path.lessons))
    assert path_progress(path, {path.lessons[0], path.lessons[1]}) == (
        2,
        len(path.lessons),
    )
    outside = next(number for number in NUMBERS if number not in path.lessons)
    assert path_progress(path, {outside}) == (0, len(path.lessons))


def test_r5_next_in_path_is_the_first_lesson_not_completed():
    path = PATHS[0]
    assert next_in_path(path, set()).number == path.lessons[0]
    assert next_in_path(path, {path.lessons[0]}).number == path.lessons[1]
    assert next_in_path(path, {path.lessons[1]}).number == path.lessons[0]
    assert next_in_path(path, set(path.lessons)) is None


def test_r6_home_shows_one_card_per_path_with_its_progress():
    at = load_home()
    cards = blocks(at, "lab-path")
    assert len(cards) == len(PATHS)
    for card, path in zip(cards, PATHS):
        assert path.title in card
        assert f"{len(path.lessons)} lessons" in card
        assert f"0 / {len(path.lessons)} done" in card


def test_r6_progress_on_a_path_card_follows_the_completed_lessons():
    path = PATHS[0]
    at = load_home(completed={path.lessons[0], path.lessons[1]})
    assert f"2 / {len(path.lessons)} done" in blocks(at, "lab-path")[0]


def test_r7_a_completed_path_says_so_and_others_do_not():
    path = PATHS[0]
    at = load_home(completed=set(path.lessons))
    assert sum(c.value == "✓ Path completed" for c in at.caption) == 1
    assert (
        f"{len(path.lessons)} / {len(path.lessons)} done" in blocks(at, "lab-path")[0]
    )
