"""Tests for specs/013-mobile-and-accessibility.md."""
import re

import tomllib
from conftest import HOME, ROOT
from streamlit.testing.v1 import AppTest

from core.lessons import LESSONS
from core.theme import _CSS


def hex_rgb(color: str) -> tuple[int, int, int]:
    return tuple(int(color[i : i + 2], 16) for i in (1, 3, 5))


def luminance(rgb) -> float:
    def channel(value: int) -> float:
        value /= 255
        return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4

    red, green, blue = (channel(v) for v in rgb)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast(first, second) -> float:
    lighter, darker = sorted((luminance(first), luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def backgrounds() -> list[tuple[int, int, int]]:
    config = tomllib.loads((ROOT / ".streamlit" / "config.toml").read_text(encoding="utf-8"))
    theme = config["theme"]
    return [hex_rgb(theme["backgroundColor"]), hex_rgb(theme["secondaryBackgroundColor"])]


def css_color(selector: str) -> tuple[int, int, int]:
    """The first '#rrggbb' text colour in the rule for this selector."""
    pattern = re.escape(selector) + r"\s*\{[^}]*?\bcolor:\s*(#[0-9A-Fa-f]{6})"
    return hex_rgb(re.search(pattern, _CSS).group(1))


def test_r1_small_screens_get_a_smaller_hero():
    match = re.search(r"@media \(max-width: 640px\)\s*\{(.*?)\n\}", _CSS, re.DOTALL)
    assert match, "no rule for small screens"
    assert ".lab-hero h1" in match.group(1)
    assert ".lab-hero {" in match.group(1)


def test_r2_hover_lift_only_applies_to_devices_that_can_hover():
    match = re.search(r"@media \(hover: hover\)\s*\{(.*?)\n\}", _CSS, re.DOTALL)
    assert match, "the hover rule is not inside a hover media query"
    assert "translateY" in match.group(1)
    outside = _CSS.replace(match.group(0), "")
    assert "translateY(-3px)" not in outside.split("prefers-reduced-motion")[0]


def test_r3_touch_screens_get_taller_buttons():
    match = re.search(r"@media \(pointer: coarse\)\s*\{(.*?)\n\}", _CSS, re.DOTALL)
    assert match, "no rule for touch screens"
    assert "min-height: 2.75rem" in match.group(1)  # 2.75rem is 44px


def test_r4_wide_tables_scroll_inside_their_box():
    assert re.search(r"table\s*\{[^}]*overflow-x:\s*auto", _CSS)


def test_r5_keyboard_focus_is_visible_on_tabs():
    assert 'button[data-baseweb="tab"]:focus-visible' in _CSS
    assert "outline: 2px solid" in _CSS


def test_r6_reduced_motion_turns_the_animation_off():
    match = re.search(r"@media \(prefers-reduced-motion: reduce\)\s*\{(.*?)\n\}", _CSS, re.DOTALL)
    assert match, "no reduced-motion rule"
    assert "transition: none" in match.group(1)
    assert "transform: none" in match.group(1)


def test_r7_label_colours_are_readable_on_both_backgrounds():
    colours = {
        "card number": hex_rgb(re.search(r"--lab-accent-text:\s*(#[0-9A-Fa-f]{6})", _CSS).group(1)),
        "Beginner label": css_color(".lab-beginner"),
        "Intermediate label": css_color(".lab-intermediate"),
        "Advanced label": css_color(".lab-advanced"),
        "function chip": css_color(".lab-chip"),
    }
    # the muted grey is semi-transparent, so mix it with each background first
    muted = re.search(r"--lab-muted:\s*rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", _CSS)
    red, green, blue, alpha = (float(v) for v in muted.groups())
    for background in backgrounds():
        mixed = tuple(round(alpha * c + (1 - alpha) * b) for c, b in zip((red, green, blue), background))
        colours[f"muted text on {background}"] = mixed
        for name, colour in colours.items():
            if name.startswith("muted text on") and name != f"muted text on {background}":
                continue
            assert contrast(colour, background) >= 4.5, f"{name} on {background}"


def test_r8_card_icons_are_hidden_from_screen_readers():
    at = AppTest.from_file(str(HOME), default_timeout=30)
    at.run()
    assert not at.exception, at.exception
    cards = [m.value for m in at.markdown if 'class="lab-card-title"' in m.value]
    paths = [m.value for m in at.markdown if 'class="lab-path"' in m.value]
    assert len(cards) == len(LESSONS)
    assert all('class="lab-card-icon" aria-hidden="true"' in block for block in cards + paths)


def test_r9_every_readme_image_has_alt_text():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    images = re.findall(r"<img\b[^>]*>", readme)
    assert images, "the README has no images to check"
    for image in images:
        match = re.search(r'\balt="([^"]+)"', image)
        assert match and match.group(1).strip(), image


def test_r10_every_lesson_has_its_own_link_text_and_checkbox_label():
    assert len({lesson.open_label for lesson in LESSONS}) == len(LESSONS)
    assert len({lesson.done_label for lesson in LESSONS}) == len(LESSONS)

    at = AppTest.from_file(str(HOME), default_timeout=30)
    at.run()
    assert not at.exception, at.exception
    labels = [checkbox.label for checkbox in at.checkbox]
    assert labels == [lesson.done_label for lesson in LESSONS]
