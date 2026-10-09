"""The lesson registry.

The lessons themselves are described in data/lessons.yaml, so adding a lesson
does not need any Python code. This module loads that file, checks that each
entry is complete, and offers a few helpers.
"""
from dataclasses import dataclass
from pathlib import Path

import yaml

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

REQUIRED_FIELDS = ("number", "title", "icon", "file", "category", "level", "summary", "functions")


@dataclass(frozen=True)
class Lesson:
    number: int
    title: str
    icon: str
    file: str
    category: str
    level: str
    summary: str
    functions: tuple[str, ...]

    @property
    def path(self) -> str:
        return f"pages/{self.file}"

    @property
    def open_label(self) -> str:
        """Text of the link that opens this lesson. Unique, so screen readers can tell links apart."""
        return f"Open {self.title}"

    @property
    def done_label(self) -> str:
        """Text of the 'mark as done' checkbox on the Home page. Unique for the same reason."""
        return f"Mark {self.title} as done"


def load_lessons(path: Path) -> tuple[list[str], list[str], list[Lesson]]:
    """Read a lessons file and return (categories, levels, lessons)."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    lessons = []
    for position, entry in enumerate(data["lessons"], start=1):
        missing = [field for field in REQUIRED_FIELDS if field not in entry]
        if missing:
            raise ValueError(
                f"{path.name}: lesson entry {position} is missing {', '.join(missing)}"
            )
        lessons.append(
            Lesson(
                number=int(entry["number"]),
                title=entry["title"],
                icon=entry["icon"],
                file=entry["file"],
                category=entry["category"],
                level=entry["level"],
                summary=entry["summary"],
                functions=tuple(entry["functions"]),
            )
        )
    return list(data["categories"]), list(data["levels"]), lessons


CATEGORIES, LEVELS, LESSONS = load_lessons(DATA_DIR / "lessons.yaml")


def total_functions() -> int:
    return sum(len(lesson.functions) for lesson in LESSONS)


def neighbours(number: int) -> "tuple[Lesson | None, Lesson | None]":
    """The lessons before and after this one (None at either end)."""
    index = next(i for i, lesson in enumerate(LESSONS) if lesson.number == number)
    previous = LESSONS[index - 1] if index > 0 else None
    following = LESSONS[index + 1] if index < len(LESSONS) - 1 else None
    return previous, following
