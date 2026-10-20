"""Search the lessons by title, function name and summary.

Used by the search box at the top of the Home page. Plain word matching, no
outside service.
"""
import re

from core.lessons import LESSONS

STOPWORDS = {"a", "an", "the", "how", "to", "do", "i", "what", "is", "of", "in", "for", "with", "and", "st"}


def _stem(word: str) -> str:
    return word[:-1] if len(word) > 3 and word.endswith("s") else word


def _words(text: str) -> set[str]:
    found = re.findall(r"[a-z0-9]+", text.lower())
    return {_stem(word) for word in found if word not in STOPWORDS}


def _score(lesson, query_words: set[str], query_text: str) -> int:
    title = _words(lesson.title)
    summary = _words(lesson.summary)
    functions = set().union(*(_words(function) for function in lesson.functions))
    score = (
        4 * len(query_words & title)
        + 3 * len(query_words & functions)
        + len(query_words & summary)
    )
    if query_text and query_text in lesson.title.lower():
        score += 6
    return score


def search_lessons(query: str, limit: int = 8) -> list:
    """The lessons that match the query, best match first (at most `limit`)."""
    query_text = (query or "").strip().lower()
    query_words = _words(query_text)
    if not query_words:
        return []
    scored = []
    for lesson in LESSONS:
        score = _score(lesson, query_words, query_text)
        if score > 0:
            scored.append((-score, lesson.number, lesson))
    scored.sort(key=lambda item: item[:2])
    return [lesson for _, _, lesson in scored[:limit]]
