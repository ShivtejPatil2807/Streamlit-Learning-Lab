"""Tests for specs/014-data-files.md (the YAML data files and their loaders)."""
from pathlib import Path

import pytest
import yaml

import core.challenges as challenges_module
import core.lessons as lessons_module
import core.paths as paths_module
from core.challenges import CHALLENGES, load_challenges
from core.lessons import CATEGORIES, DATA_DIR, LESSONS, LEVELS, load_lessons
from core.paths import PATHS, load_paths

FILES = ["lessons.yaml", "challenges.yaml", "paths.yaml"]

GOOD_LESSON = {
    "number": 1,
    "title": "Example",
    "icon": "🧪",
    "file": "01_Example.py",
    "category": "Display & Content",
    "level": "Beginner",
    "summary": "An example lesson.",
    "functions": ["st.write"],
}


def write_yaml(tmp_path: Path, name: str, data) -> Path:
    path = tmp_path / name
    path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")
    return path


def lessons_file(tmp_path: Path, entries: list[dict]) -> Path:
    data = {"categories": ["Display & Content"], "levels": ["Beginner"], "lessons": entries}
    return write_yaml(tmp_path, "lessons.yaml", data)


def test_r1_the_course_is_described_by_the_data_files():
    assert LESSONS and CHALLENGES and PATHS
    for module in (lessons_module, challenges_module, paths_module):
        source = Path(module.__file__).read_text(encoding="utf-8")
        assert "Text & Markdown" not in source, f"{module.__name__} still holds lesson text"


def test_r2_the_data_files_are_utf8_yaml_that_loads():
    for name in FILES:
        text = (DATA_DIR / name).read_text(encoding="utf-8")
        assert yaml.safe_load(text), name


def test_r3_a_missing_field_is_rejected_with_a_helpful_message(tmp_path):
    broken = {key: value for key, value in GOOD_LESSON.items() if key != "summary"}
    with pytest.raises(ValueError, match=r"lessons\.yaml: lesson entry 2 is missing summary"):
        load_lessons(lessons_file(tmp_path, [GOOD_LESSON, broken]))

    no_options = {"question": "Why?", "answer": 0, "explanation": "Because."}
    path = write_yaml(tmp_path, "challenges.yaml", {7: [no_options]})
    with pytest.raises(ValueError, match=r"lesson 7, question 1 is missing options"):
        load_challenges(path)

    path = write_yaml(tmp_path, "paths.yaml", {"paths": [{"slug": "x", "title": "X"}]})
    with pytest.raises(ValueError, match=r"path entry 1 is missing icon, summary, lessons"):
        load_paths(path)


def test_r4_an_answer_outside_the_options_is_rejected(tmp_path):
    bad = {"question": "Pick one", "options": ["a", "b"], "answer": 2, "explanation": "No."}
    path = write_yaml(tmp_path, "challenges.yaml", {3: [bad]})
    with pytest.raises(ValueError, match=r"lesson 3, question 1: the answer does not point"):
        load_challenges(path)


def test_r5_adding_a_lesson_needs_no_python_code(tmp_path):
    second = {**GOOD_LESSON, "number": 2, "title": "Another", "file": "02_Another.py"}
    _categories, _levels, lessons = load_lessons(lessons_file(tmp_path, [GOOD_LESSON, second]))
    assert [lesson.title for lesson in lessons] == ["Example", "Another"]
    assert lessons[1].path == "pages/02_Another.py"
    assert lessons[0].functions == ("st.write",)  # a list in the file, a tuple in the code


def test_r6_the_modules_keep_their_public_names():
    assert isinstance(CATEGORIES, list) and isinstance(LEVELS, list)
    assert all(isinstance(lesson.number, int) for lesson in LESSONS)
    assert all(isinstance(number, int) for number in CHALLENGES)
    assert all(isinstance(number, int) for path in PATHS for number in path.lessons)
    # text that YAML could mistake for another type must still arrive as text
    assert all(isinstance(option, str) for items in CHALLENGES.values()
               for item in items for option in item.options)
