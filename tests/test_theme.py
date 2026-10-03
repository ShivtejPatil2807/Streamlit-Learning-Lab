"""Tests for specs/005-visual-style.md (core/theme.py and the lesson meta line)."""
from textwrap import dedent

from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS, LEVELS
from core.theme import _CSS, chips, level_pill, pill


def test_r1_pill_has_the_pill_and_kind_classes():
    assert 'class="lab-pill lab-category"' in pill("Hello", "category")


def test_r2_pill_and_chips_escape_html():
    assert "<script>" not in pill("<script>", "category")
    assert "&lt;script&gt;" in pill("<script>", "category")
    assert "<b>" not in chips(["<b>"])


def test_r3_level_pill_uses_the_lowercase_level():
    assert "lab-advanced" in level_pill("Advanced")
    assert "Advanced" in level_pill("Advanced")


def test_r4_every_level_has_a_colour_class():
    for level in LEVELS:
        assert f".lab-{level.lower()}" in _CSS, f"no CSS for level {level}"


def test_r5_chips_returns_one_chip_per_name_in_order():
    result = chips(["st.a", "st.b", "st.c"])
    assert result.count('class="lab-chip"') == 3
    assert result.index("st.a") < result.index("st.b") < result.index("st.c")


def test_r6_lesson_page_shows_level_category_and_position(tmp_path):
    page = tmp_path / "meta_page.py"
    page.write_text(
        dedent(
            """
            from core.components import lesson_page

            lesson_page(5)
            """
        ),
        encoding="utf-8",
    )
    at = AppTest.from_file(str(page), default_timeout=30)
    at.run()
    assert not at.exception, at.exception
    lesson = next(item for item in LESSONS if item.number == 5)
    meta = next(m.value for m in at.markdown if 'class="lab-meta"' in m.value)
    assert lesson.level in meta
    assert lesson.category.replace("&", "&amp;") in meta
    assert f"Lesson 5 of {len(LESSONS)}" in meta
