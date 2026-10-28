"""Tests for specs/018-readme.md (README.md and scripts/update_readme.py)."""
import re

import yaml
from conftest import ROOT

from core.lessons import LESSONS
from scripts.update_readme import END, START, build_course_section, split_readme

README = (ROOT / "README.md").read_text(encoding="utf-8")


def manual_part() -> str:
    """The parts of the README that people write by hand (not the generated tables)."""
    before, _, after = split_readme(README)
    return before + after


def test_r1_the_readme_has_one_pair_of_course_markers_in_order():
    assert README.count(START) == 1 and README.count(END) == 1
    assert README.index(START) < README.index(END)


def test_r2_the_course_tables_are_up_to_date():
    generated = split_readme(README)[1].strip()
    assert generated == build_course_section().strip(), (
        "The course tables in README.md are out of date. Run: python -m scripts.update_readme"
    )


def test_r3_every_lesson_is_linked_from_the_readme():
    for lesson in LESSONS:
        assert f"]({lesson.path})" in README, lesson.file


def test_r4_every_relative_link_points_to_a_file_that_exists():
    for target in re.findall(r"\]\(([^)\s]+)\)", README):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = target.split("#")[0]
        assert (ROOT / path).exists(), f"broken link in README: {target}"


def test_r5_the_project_tree_only_lists_things_that_exist():
    tree = re.search(r"```text\n(.*?)\n```", README, re.DOTALL).group(1)
    names = re.findall(r"^[├└]── (\S+)", tree, re.MULTILINE)
    assert len(names) >= 10
    for name in names:
        assert (ROOT / name.rstrip("/")).exists(), f"the tree lists {name}, which does not exist"


def test_r6_the_license_is_the_same_everywhere():
    assert "License-MIT" in README and "MIT License" in README
    assert (ROOT / "LICENSE").read_text(encoding="utf-8").startswith("MIT License")
    assert "educational and learning purposes" not in README


def test_r7_adding_a_lesson_points_to_the_data_files():
    start = README.index("## Adding a lesson")
    section = README[start : README.index("## Development")]
    for name in ("data/lessons.yaml", "data/challenges.yaml", "data/paths.yaml"):
        assert name in section, name
    assert "core/lessons.py" not in section


def test_r8_the_handwritten_text_does_not_describe_removed_features():
    text = manual_part()
    for phrase in ("17 lessons", "category and level filters", "Home page filters"):
        assert phrase not in text, phrase


def test_r9_the_python_badge_matches_the_versions_ci_tests():
    workflow = yaml.safe_load((ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8"))
    versions = workflow["jobs"]["test"]["strategy"]["matrix"]["python-version"]
    assert "Python-" + "%20%7C%20".join(versions) in README
