"""Short multiple-choice questions shown at the bottom of each lesson.

The questions live in data/challenges.yaml. This module loads them and checks
that each one is complete.
"""
from dataclasses import dataclass
from pathlib import Path

import yaml

from core.lessons import DATA_DIR

REQUIRED_FIELDS = ("question", "options", "answer", "explanation")


@dataclass(frozen=True)
class Challenge:
    question: str
    options: tuple[str, ...]
    answer: int  # index into options
    explanation: str


def load_challenges(path: Path) -> dict[int, list[Challenge]]:
    """Read a challenges file and return {lesson number: [challenges]}."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    challenges: dict[int, list[Challenge]] = {}
    for number, entries in data.items():
        for position, entry in enumerate(entries, start=1):
            where = f"{path.name}: lesson {number}, question {position}"
            missing = [field for field in REQUIRED_FIELDS if field not in entry]
            if missing:
                raise ValueError(f"{where} is missing {', '.join(missing)}")
            if not 0 <= entry["answer"] < len(entry["options"]):
                raise ValueError(f"{where}: the answer does not point to one of the options")
            challenges.setdefault(int(number), []).append(
                Challenge(
                    question=entry["question"],
                    options=tuple(entry["options"]),
                    answer=entry["answer"],
                    explanation=entry["explanation"],
                )
            )
    return challenges


CHALLENGES = load_challenges(DATA_DIR / "challenges.yaml")
