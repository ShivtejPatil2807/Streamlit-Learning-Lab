"""Reusable building blocks for lesson pages.

Every lesson page follows the same pattern:

    lesson_page(5)

    @demo("st.line_chart()", "Draws a line chart from a table of numbers.")
    def _():
        st.line_chart(chart_data)

The body of the decorated function is BOTH shown as code AND executed, so the
code on screen can never drift out of sync with the live output.
"""
import inspect
import textwrap

import streamlit as st

from core.lessons import LESSONS
from core.theme import apply_theme

_COUNTER_KEY = "_demo_count"


def lesson_page(number: int, intro: str | None = None) -> None:
    """Page setup: tab title/icon, theme, page title and intro text.

    Title and icon come from core/lessons.py, so they are defined in one place.
    Must be the first Streamlit call on the page.
    """
    lesson = next(item for item in LESSONS if item.number == number)
    st.set_page_config(page_title=lesson.title, page_icon=lesson.icon)
    apply_theme()
    st.session_state[_COUNTER_KEY] = 0  # restart numbering on every run
    st.title(f"{lesson.icon} {lesson.title}")
    st.write(intro or lesson.summary)


def _next_number() -> int:
    n = st.session_state.get(_COUNTER_KEY, 0) + 1
    st.session_state[_COUNTER_KEY] = n
    return n


def section(title: str, description: str | None = None) -> None:
    """A numbered section with no code demo (plain explanation)."""
    st.divider()
    st.header(f"{_next_number()}. {title}")
    if description:
        st.write(description)


def _body(func) -> str:
    """Source of a function's body, without the decorator, def line or indent."""
    lines = inspect.getsource(func).splitlines()
    start = next(i for i, line in enumerate(lines) if line.lstrip().startswith("def "))
    return textwrap.dedent("\n".join(lines[start + 1:])).strip("\n")


def demo(title: str, description: str, *, run: bool = True, caption: str | None = None):
    """Decorator: Title -> Code -> Output for one Streamlit function.

    run=False shows the code without executing it (for things that need setup,
    like st.login()).  caption adds small grey text under the output.
    """

    def decorator(func):
        section(title, description)
        st.code(_body(func), language="python")
        if run:
            func()
        if caption:
            st.caption(caption)
        return func

    return decorator


def show_setup(func):
    """Show a helper's code in an expander ('sample data used on this page')."""
    with st.expander("Sample data used on this page"):
        st.code(_body(func), language="python")
    return func
