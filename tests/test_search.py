"""Tests for specs/017-lesson-search.md (core/search.py and the search box on the Home page)."""
import re

from conftest import HOME
from streamlit.testing.v1 import AppTest

from core.search import search_lessons


def numbers(query: str, limit: int = 8) -> list[int]:
    return [lesson.number for lesson in search_lessons(query, limit)]


def load_home(query: str = "") -> AppTest:
    at = AppTest.from_file(str(HOME), default_timeout=30)
    at.run()
    if query:
        at.text_input(key="search").set_value(query).run()
    assert not at.exception, at.exception
    return at


def result_numbers(at: AppTest) -> list[int]:
    found = []
    for markdown in at.markdown:
        if 'class="lab-result"' in markdown.value:
            found.append(int(re.search(r"(\d+)\. ", markdown.value).group(1)))
    return found


def test_r1_an_empty_or_blank_query_finds_nothing():
    assert numbers("") == []
    assert numbers("   ") == []
    assert numbers("the of to") == []  # only filler words


def test_r2_a_title_match_comes_first():
    assert numbers("charts")[0] == 5
    assert numbers("session")[0] == 9
    assert numbers("caching")[0] == 11
    assert numbers("chatbot")[0] == 22


def test_r3_function_names_find_their_lesson():
    assert numbers("st.form")[0] == 10
    assert numbers("download button")[0] == 6
    assert numbers("st.dialog")[0] == 15


def test_r4_plurals_and_capitals_do_not_matter():
    assert numbers("CHART") == numbers("charts") == numbers("chart")


def test_r5_at_most_the_limit_is_returned_and_each_lesson_once():
    found = numbers("session state", limit=3)
    assert len(found) <= 3 and len(set(found)) == len(found)
    assert len(numbers("state")) <= 8


def test_r6_a_query_with_no_match_finds_nothing():
    assert numbers("zzzz qqqq") == []


def test_r7_the_home_page_shows_the_results_under_the_search_box():
    at = load_home("chart")
    assert result_numbers(at) == [5]


def test_r8_no_match_says_so():
    at = load_home("zzzz")
    assert result_numbers(at) == []
    assert any(c.value.startswith("No lessons match") for c in at.caption)


def test_r9_without_a_query_the_page_shows_no_results():
    assert result_numbers(load_home()) == []
