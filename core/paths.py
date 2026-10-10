"""Learning paths: short, ordered lists of lessons that lead to a goal.

The paths live in data/paths.yaml. This module loads them and offers helpers.
"""
from dataclasses import dataclass
from pathlib import Path

import yaml

from core.lessons import DATA_DIR, LESSONS

REQUIRED_FIELDS = ("slug", "title", "icon", "summary", "lessons")


@dataclass(frozen=True)
class LearningPath:
    slug: str
    title: str
    icon: str
    summary: str
    lessons: tuple[int, ...]  # lesson numbers, in the order to study them


def load_paths(path: Path) -> list[LearningPath]:
    """Read a paths file and return the learning paths."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    paths = []
    for position, entry in enumerate(data["paths"], start=1):
        missing = [field for field in REQUIRED_FIELDS if field not in entry]
        if missing:
            raise ValueError(f"{path.name}: path entry {position} is missing {', '.join(missing)}")
        paths.append(
            LearningPath(
                slug=entry["slug"],
                title=entry["title"],
                icon=entry["icon"],
                summary=entry["summary"],
                lessons=tuple(int(number) for number in entry["lessons"]),
            )
        )
    return paths


PATHS: list[LearningPath] = load_paths(DATA_DIR / "paths.yaml")


def path_lessons(path: LearningPath) -> list:
    """The path's lessons, in the order to study them."""
    by_number = {lesson.number: lesson for lesson in LESSONS}
    return [by_number[number] for number in path.lessons]


def path_progress(path: LearningPath, completed: set[int]) -> tuple[int, int]:
    """(lessons done, lessons in the path). Lessons outside the path do not count."""
    done = sum(1 for number in path.lessons if number in completed)
    return done, len(path.lessons)


def next_in_path(path: LearningPath, completed: set[int]):
    """The first lesson of the path that is not completed yet, or None."""
    for lesson in path_lessons(path):
        if lesson.number not in completed:
            return lesson
    return None
