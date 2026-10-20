"""Tests for specs/015-home-page-redesign.md (the layout of Home.py)."""
import html
import re
from datetime import datetime, timezone

import tomllib
from conftest import HOME, ROOT
from streamlit.testing.v1 import AppTest
from test_accessibility import contrast, hex_rgb

from core.export import REPO_URL
from core.lessons import LESSONS
from core.theme import _CSS

HEADINGS = [
    "Choose your level",
    "Your progress",
    "How to use the Lab",
    "Learning paths",
    "Latest lessons",
    "Elsewhere",
]


def load_home(completed=None) -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    if completed is not None:
        at.session_state["completed"] = completed
    at.run()
    assert not at.exception, at.exception
    return at


def blocks(at: AppTest, marker: str) -> list[str]:
    return [m.value for m in at.markdown if f'class="{marker}"' in m.value]


def css_background(selector: str) -> tuple[int, int, int]:
    pattern = re.escape(selector) + r"\s*\{[^}]*?\bbackground:\s*(#[0-9A-Fa-f]{6})"
    return hex_rgb(re.search(pattern, _CSS).group(1))


def test_r1_the_page_is_laid_out_in_order():
    at = load_home()
    order = [m.value for m in at.markdown]

    def position(marker: str) -> int:
        return next(i for i, value in enumerate(order) if f'class="{marker}"' in value)

    assert (
        position("lab-hero")
        < position("lab-stage")
        < position("lab-how")
        < position("lab-path")
        < position("lab-news")
        < position("lab-community")
        < position("lab-link-row")
        < position("lab-footer")
    )


def test_r2_the_title_is_a_plain_heading_with_the_course_steps():
    hero = blocks(load_home(), "lab-hero")[0]
    assert hero.count("<h1>") == 1 and "Streamlit Learning Lab" in hero
    assert "gradient" not in hero  # a plain title, not a coloured box


def test_r3_the_button_says_start_for_a_new_visitor_and_continue_after_that():
    assert load_home().button(key="start").label == "▶ Start learning"
    assert load_home(completed={1}).button(key="start").label == "▶ Continue"


def test_r4_when_everything_is_done_there_is_no_start_button_but_a_success_message():
    at = load_home(completed={lesson.number for lesson in LESSONS})
    assert "start" not in [button.key for button in at.button]
    assert len(at.success) == 1


def test_r5_section_titles_are_headings_in_order():
    assert [h.value for h in load_home().header] == HEADINGS


def test_r6_how_to_use_has_three_rows():
    section = blocks(load_home(), "lab-how")[0]
    assert section.count('class="lab-how"') == 3
    for lead in ("Start", "Practice", "Build"):
        assert f">{lead}</strong>" in section


def test_r7_latest_lessons_are_the_six_newest_newest_first():
    cards = blocks(load_home(), "lab-news")
    newest = sorted(LESSONS, key=lambda lesson: -lesson.number)[:6]
    assert len(cards) == 6
    for card, lesson in zip(cards, newest):
        assert f"<h3>{html.escape(lesson.title)}</h3>" in card
        assert f'class="lab-code">{html.escape(lesson.functions[0])}<' in card


def test_r8_the_community_card_links_to_the_issues_and_the_source():
    card = blocks(load_home(), "lab-community")[0]
    assert f'href="{REPO_URL}/issues"' in card and f'href="{REPO_URL}"' in card
    assert "Help improve the Lab" in card


def test_r9_elsewhere_lists_four_places():
    rows = " ".join(blocks(load_home(), "lab-link-row"))
    assert rows.count('class="lab-link-row"') == 4
    for url in (REPO_URL, "https://docs.streamlit.io", "https://discuss.streamlit.io", "https://streamlit.io/cloud"):
        assert f'href="{url}"' in rows


def test_r10_the_footer_links_to_the_source_the_issues_and_the_docs():
    footer = blocks(load_home(), "lab-footer")[0]
    assert f'href="{REPO_URL}"' in footer
    assert f'href="{REPO_URL}/issues"' in footer
    assert 'href="https://docs.streamlit.io"' in footer
    assert f"© {datetime.now(timezone.utc).date().year}" in footer
    assert "not affiliated" in footer


def test_r11_white_text_is_readable_on_every_coloured_tile_and_button():
    white = (255, 255, 255)
    for name in ("beginner", "intermediate", "advanced"):
        assert contrast(white, css_background(f'.lab-stage[data-level="{name}"]')) >= 4.5, name
    for name in ("orange", "purple", "cyan"):
        assert contrast(white, css_background(f".lab-how-{name}")) >= 4.5, name
    assert contrast(white, css_background(".lab-button")) >= 4.5
    assert contrast(white, css_background(".lab-button.dark")) >= 4.5
    config = tomllib.loads((ROOT / ".streamlit" / "config.toml").read_text(encoding="utf-8"))
    assert contrast(white, hex_rgb(config["theme"]["primaryColor"])) >= 4.5


def test_r11_text_is_readable_on_the_light_community_card():
    card = css_background(".lab-community")
    heading = re.search(r"\.lab-community h3\s*\{[^}]*?\bcolor:\s*(#[0-9A-Fa-f]{6})", _CSS).group(1)
    body = re.search(r"\.lab-community p\s*\{[^}]*?\bcolor:\s*(#[0-9A-Fa-f]{6})", _CSS).group(1)
    assert contrast(hex_rgb(heading), card) >= 4.5
    assert contrast(hex_rgb(body), card) >= 4.5


def test_r12_the_stylesheet_styles_every_new_block():
    for selector in (
        ".lab-brand", ".lab-result", ".lab-stage", ".lab-how", ".lab-news", ".lab-code",
        ".lab-community", ".lab-button", ".lab-link-row", ".lab-link-icon", ".lab-footer", ".lab-footer-copy",
    ):
        assert selector in _CSS, selector
