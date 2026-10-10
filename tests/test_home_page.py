"""Tests for specs/015-home-page-redesign.md (the layout of Home.py)."""
import tomllib

from conftest import HOME, ROOT
from streamlit.testing.v1 import AppTest
from test_accessibility import contrast, hex_rgb

from core.export import REPO_URL
from core.lessons import LESSONS
from core.theme import _CSS

TILE_TITLES = ["Learn → Code → Try", "Challenges", "Real projects", "Take it home"]


def load_home(completed=None) -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    assert not at.exception, at.exception
    return at


def blocks(at: AppTest, marker: str) -> list[str]:
    return [m.value for m in at.markdown if f'class="{marker}"' in m.value]


def test_r1_the_page_is_laid_out_in_order():
    at = load_home()
    order = [m.value for m in at.markdown]

    def position(marker: str) -> int:
        return next(i for i, value in enumerate(order) if f'class="{marker}"' in value)

    assert (
        position("lab-hero")
        < position("lab-tile")
        < position("lab-path")
        < position("lab-card-title")
        < position("lab-footer")
    )
    assert len(at.metric) == 3  # the stats sit between the hero and the tiles


def test_r2_the_button_says_start_for_a_new_visitor_and_continue_after_that():
    assert [b.label for b in load_home().button] == ["▶ Start learning"]
    assert [b.label for b in load_home(completed={1}).button] == ["▶ Continue"]


def test_r2_the_panel_shows_the_progress_and_the_next_lesson():
    at = load_home(completed={1, 2})
    assert any(c.value == "Next up: 3. Layouts" for c in at.caption)


def test_r3_when_everything_is_done_there_is_no_button_but_a_success_message():
    at = load_home(completed={lesson.number for lesson in LESSONS})
    assert len(at.button) == 0
    assert len(at.success) == 1


def test_r4_section_titles_are_headings_in_order():
    assert [h.value for h in load_home().header] == ["What you get", "Learning paths", "All lessons"]


def test_r5_what_you_get_has_four_tiles():
    tiles = blocks(load_home(), "lab-tile")
    assert len(tiles) == len(TILE_TITLES)
    for tile, title in zip(tiles, TILE_TITLES):
        assert title in tile


def test_r6_the_lesson_list_says_how_many_lessons_are_shown():
    at = load_home()
    assert any(c.value == f"Showing {len(LESSONS)} of {len(LESSONS)} lessons" for c in at.caption)

    at.text_input[0].set_value("chart").run()
    assert not at.exception, at.exception
    assert any(c.value == f"Showing 1 of {len(LESSONS)} lessons" for c in at.caption)


def test_r7_the_footer_links_to_the_source_the_issues_and_the_docs():
    footer = blocks(load_home(), "lab-footer")[0]
    assert f'href="{REPO_URL}"' in footer
    assert f'href="{REPO_URL}/issues"' in footer
    assert 'href="https://docs.streamlit.io"' in footer


def test_r8_white_text_is_readable_on_the_primary_button():
    config = tomllib.loads((ROOT / ".streamlit" / "config.toml").read_text(encoding="utf-8"))
    primary = hex_rgb(config["theme"]["primaryColor"])
    assert contrast((255, 255, 255), primary) >= 4.5


def test_r9_the_stylesheet_styles_the_tiles_and_the_footer():
    for selector in (".lab-tile", ".lab-tile-icon", ".lab-footer", ".lab-footer-links"):
        assert selector in _CSS, selector
