"""Tests for the Streamlit-docs style Home page layout and structure."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

HOME = Path(__file__).parent.parent / "Home.py"


def load_home(completed=None) -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    return at


def test_r1_the_page_is_laid_out_in_order():
    at = load_home()
    order = [m.value for m in at.markdown]

    def position(marker: str) -> int:
        return next(i for i, value in enumerate(order) if f'class="{marker}"' in value)

    assert (
        position("lab-brand")
        < position("lab-hero")
        < position("lab-stage")
        < position("lab-path")
        < position("lab-footer")
    )


def test_r4_section_titles_are_headings_in_order():
    headings = [h.value for h in load_home().header]
    assert "Choose your level" in headings
    assert "Your progress" in headings
    assert "Learning paths" in headings
    assert "Elsewhere" in headings