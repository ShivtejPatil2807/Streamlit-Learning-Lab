"""Tests for specs/002-demo-helper.md (core/components.py).

Each test writes a tiny page to a temp folder and runs it with Streamlit's
AppTest, because the helper needs a real source file to read the code from.
"""
from textwrap import dedent

from streamlit.testing.v1 import AppTest


def run_page(tmp_path, body: str) -> AppTest:
    page = tmp_path / "demo_page.py"
    page.write_text(
        "import streamlit as st\n"
        "from core.components import demo, lesson_page, section, show_setup\n"
        + dedent(body),
        encoding="utf-8",
    )
    at = AppTest.from_file(str(page), default_timeout=30)
    at.run()
    assert not at.exception, at.exception
    return at


def test_r2_lesson_page_shows_title_and_intro(tmp_path):
    at = run_page(tmp_path, 'lesson_page(1, "My custom intro")\n')
    assert "Text & Markdown" in at.title[0].value
    assert any("My custom intro" in m.value for m in at.markdown)


def test_r2_lesson_page_falls_back_to_the_summary(tmp_path):
    from core.lessons import LESSONS

    at = run_page(tmp_path, "lesson_page(1)\n")
    assert any(LESSONS[0].summary in m.value for m in at.markdown)


def test_r3_numbering_starts_at_one_on_every_run(tmp_path):
    at = run_page(
        tmp_path,
        '''
        lesson_page(1)

        @demo("st.first()", "one")
        def _():
            st.write("A")

        @demo("st.second()", "two")
        def _():
            st.write("B")
        ''',
    )
    assert [h.value for h in at.header] == ["1. st.first()", "2. st.second()"]
    at.run()  # a rerun must not continue counting
    assert [h.value for h in at.header] == ["1. st.first()", "2. st.second()"]


def test_r3_section_shares_the_numbering(tmp_path):
    at = run_page(
        tmp_path,
        '''
        lesson_page(1)
        section("Plain section")

        @demo("st.demo()", "text")
        def _():
            st.write("A")
        ''',
    )
    assert [h.value for h in at.header] == ["1. Plain section", "2. st.demo()"]


def test_r4_and_r5_demo_shows_the_body_and_runs_it(tmp_path):
    at = run_page(
        tmp_path,
        '''
        lesson_page(1)

        @demo("st.write()", "text")
        def _():
            st.write("LIVE OUTPUT")
        ''',
    )
    assert at.code[0].value == 'st.write("LIVE OUTPUT")'
    assert any(m.value == "LIVE OUTPUT" for m in at.markdown)


def test_r6_run_false_shows_the_code_but_never_runs_it(tmp_path):
    at = run_page(
        tmp_path,
        '''
        lesson_page(1)

        @demo("st.write()", "text", run=False)
        def _():
            st.write("SHOULD NOT RUN")
        ''',
    )
    assert at.code[0].value == 'st.write("SHOULD NOT RUN")'
    assert not any(m.value == "SHOULD NOT RUN" for m in at.markdown)


def test_r7_caption_appears_after_the_output(tmp_path):
    at = run_page(
        tmp_path,
        '''
        lesson_page(1)

        @demo("st.write()", "text", caption="My caption")
        def _():
            st.write("A")
        ''',
    )
    assert at.caption[0].value == "My caption"


def test_r8_show_setup_returns_the_function_unchanged(tmp_path):
    at = run_page(
        tmp_path,
        '''
        lesson_page(1)

        @show_setup
        def make_value():
            return 42

        st.write(f"value is {make_value()}")
        ''',
    )
    assert at.expander[0].label == "Sample data used on this page"
    assert any(m.value == "value is 42" for m in at.markdown)