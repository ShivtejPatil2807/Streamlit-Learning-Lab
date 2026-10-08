"""Learning paths: short, ordered lists of lessons that lead to a goal."""
from dataclasses import dataclass

from core.lessons import LESSONS


@dataclass(frozen=True)
class LearningPath:
    slug: str
    title: str
    icon: str
    summary: str
    lessons: tuple[int, ...]  # lesson numbers, in the order to study them


PATHS: list[LearningPath] = [
    LearningPath(
        "beginner", "Beginner in 5 lessons", "🌱",
        "The basics: show text, take input, arrange a page, give feedback and remember things.",
        (1, 2, 3, 8, 9),
    ),
    LearningPath(
        "dashboard", "Build a dashboard", "📊",
        "Take input, arrange the page, show data and graphs, then build a sales dashboard.",
        (2, 3, 4, 5, 21),
    ),
    LearningPath(
        "chatbot", "Build a chatbot", "💬",
        "Take input, remember state, build a chat window, stream replies, then build a chatbot.",
        (2, 9, 12, 17, 22),
    ),
    LearningPath(
        "machine-learning", "Machine learning demo", "🔬",
        "Take input, remember state, cache a model, then train an iris classifier.",
        (2, 9, 11, 20),
    ),
]


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
