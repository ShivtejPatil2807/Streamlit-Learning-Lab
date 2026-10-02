"""Tests for specs/001-lesson-registry.md (core/lessons.py).

Pure Python: no Streamlit needed.
"""
from conftest import PAGES_DIR
from core.lessons import CATEGORIES, LEVELS, LESSONS, total_functions


def test_r1_numbers_are_unique_and_contiguous():
    numbers = [lesson.number for lesson in LESSONS]
    assert numbers == list(range(1, len(LESSONS) + 1))


def test_r2_every_file_exists_in_pages():
    for lesson in LESSONS:
        assert (PAGES_DIR / lesson.file).is_file(), f"missing: {lesson.path}"


def test_r3_file_starts_with_its_number():
    for lesson in LESSONS:
        assert lesson.file.startswith(f"{lesson.number:02d}_"), lesson.file


def test_r4_category_is_known():
    for lesson in LESSONS:
        assert lesson.category in CATEGORIES, lesson.title


def test_r5_level_is_known():
    for lesson in LESSONS:
        assert lesson.level in LEVELS, lesson.title


def test_r6_required_text_is_not_empty():
    for lesson in LESSONS:
        assert lesson.title.strip(), lesson.number
        assert lesson.summary.strip(), lesson.title
        assert len(lesson.functions) > 0, lesson.title


def test_r7_path_is_pages_plus_file():
    for lesson in LESSONS:
        assert lesson.path == f"pages/{lesson.file}"


def test_r8_total_functions_matches_the_lessons():
    assert total_functions() == sum(len(lesson.functions) for lesson in LESSONS)


def test_r9_every_page_has_a_registry_entry():
    on_disk = {path.name for path in PAGES_DIR.glob("*.py")}
    registered = {lesson.file for lesson in LESSONS}
    assert on_disk == registered
