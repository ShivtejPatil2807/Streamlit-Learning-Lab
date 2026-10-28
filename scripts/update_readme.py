"""Keeps the course tables in README.md in step with the data files.

Run this after you change data/lessons.yaml or data/paths.yaml:

    python -m scripts.update_readme

It rewrites the part of README.md between the two course markers. The test suite
fails if that part is out of date, so the README can never say "17 lessons"
when there are 22.
"""
from pathlib import Path

from core.lessons import LESSONS, LEVELS
from core.paths import PATHS, path_lessons

README = Path(__file__).resolve().parents[1] / "README.md"
START = "<!-- course:start -->"
END = "<!-- course:end -->"
LEVEL_ICONS = {"Beginner": "🌱", "Intermediate": "🌿", "Advanced": "🌳"}
MAX_FUNCTIONS = 6


def _cell(text: str) -> str:
    return text.replace("|", "\\|")


def _functions(lesson) -> str:
    shown = [f"`{name}`" for name in lesson.functions[:MAX_FUNCTIONS]]
    if len(lesson.functions) > MAX_FUNCTIONS:
        shown.append("…")
    return ", ".join(shown)


def build_course_section() -> str:
    """The generated part of the README, as Markdown."""
    projects = [lesson for lesson in LESSONS if lesson.category == "Projects"]
    lessons = len(LESSONS) - len(projects)
    parts = [
        (f"Every lesson belongs to one of three levels. In total there are **{len(LESSONS)}** "
        f"pages: {lessons} lessons and {len(projects)} mini-projects."),
        "",
    ]
    for index, level in enumerate(LEVELS):
        in_level = [lesson for lesson in LESSONS if lesson.level == level]
        icon = LEVEL_ICONS.get(level, "📚")
        parts += [
            f"<details{' open' if index == 0 else ''}>",
            f"<summary><strong>{icon} {level}</strong> · {len(in_level)} lessons</summary>",
            "",
            "| Lesson | What you learn | Key functions |",
            "| --- | --- | --- |",
        ]
        for lesson in in_level:
            link = f"[{lesson.number:02d} — {_cell(lesson.title)}]({lesson.path})"
            parts.append(f"| {link} | {_cell(lesson.summary)} | {_functions(lesson)} |")
        parts += ["</details>", ""]

    parts += [
        "### Learning paths",
        "",
        "Short routes through the lessons, in the order to study them:",
        "",
        "| Path | Lessons in order |",
        "| --- | --- |",
    ]
    for path in PATHS:
        route = " → ".join(_cell(lesson.title) for lesson in path_lessons(path))
        parts.append(f"| {path.icon} **{_cell(path.title)}** | {route} |")
    return "\n".join(parts)


def split_readme(text: str) -> tuple[str, str, str]:
    """(before the marker, the generated part, after the end marker)."""
    start = text.index(START) + len(START)
    end = text.index(END)
    return text[:start], text[start:end], text[end:]


def update_readme(path: Path = README) -> bool:
    """Rewrite the generated part. Returns True if the file changed."""
    text = path.read_text(encoding="utf-8")
    before, old, after = split_readme(text)
    new = "\n" + build_course_section() + "\n"
    if old == new:
        return False
    path.write_text(before + new + after, encoding="utf-8")
    return True


if __name__ == "__main__":
    print("README updated" if update_readme() else "README already up to date")
