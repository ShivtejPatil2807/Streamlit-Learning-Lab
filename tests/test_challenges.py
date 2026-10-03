"""Tests for specs/004-challenges-and-progress.md (data part of core/challenges.py).

Pure Python: no Streamlit needed.
"""
from core.challenges import CHALLENGES
from core.lessons import LESSONS


def test_r1_every_lesson_has_at_least_one_challenge():
    for lesson in LESSONS:
        assert CHALLENGES.get(lesson.number), f"no challenge for lesson {lesson.number}"


def test_r1_no_challenges_for_unknown_lessons():
    numbers = {lesson.number for lesson in LESSONS}
    assert set(CHALLENGES) <= numbers


def test_r2_every_challenge_is_well_formed():
    for number, items in CHALLENGES.items():
        for item in items:
            where = f"lesson {number}: {item.question}"
            assert item.question.strip(), where
            assert item.explanation.strip(), where
            assert len(item.options) >= 2, where
            assert len(set(item.options)) == len(item.options), where
            assert 0 <= item.answer < len(item.options), where
