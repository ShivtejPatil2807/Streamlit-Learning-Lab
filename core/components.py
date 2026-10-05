"""Reusable building blocks for lesson pages.

Every lesson page follows the same pattern:

    lesson_page(5)

    @demo("st.line_chart()", "Draws a line chart from a table of numbers.")
    def _():
        st.line_chart(chart_data)

    lesson_footer(5)

Each demo has three tabs: Learn (the explanation), Code (the code) and
Try (the live result). The body of the decorated function is BOTH shown as
code AND executed, so the code on screen can never drift out of sync with the
live output. lesson_footer adds the challenge questions and a "done" checkbox.
"""
import inspect
import textwrap

import streamlit as st

from core.challenges import CHALLENGES
from core.export import build_script
from core.feedback import feedback_url
from core.lessons import LESSONS, neighbours
from core.theme import apply_theme, level_pill, pill

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
    st.markdown(
        '<div class="lab-meta">'
        + level_pill(lesson.level)
        + pill(lesson.category, "category")
        + pill(f"Lesson {number} of {len(LESSONS)}", "category")
        + "</div>",
        unsafe_allow_html=True,
    )
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
    """Decorator: Learn -> Code -> Try for one Streamlit function.

    run=False shows the code without executing it (for things that need setup,
    like st.login()).  caption adds small grey text under the output.
    """

    def decorator(func):
        section(title)
        learn_tab, code_tab, try_tab = st.tabs(["📖 Learn", "💻 Code", "▶️ Try"])
        with learn_tab:
            st.write(description)
        with code_tab:
            st.code(_body(func), language="python")
        with try_tab:
            if run:
                func()
            else:
                st.info("This demo is not run here. Copy the code to try it in your own app.")
            if caption:
                st.caption(caption)
        return func

    return decorator


def show_setup(func):
    """Show a helper's code in an expander ('sample data used on this page')."""
    with st.expander("Sample data used on this page"):
        st.code(_body(func), language="python")
    return func


def lesson_footer(number: int) -> None:
    """End of a lesson: challenge questions and a 'mark as done' checkbox.

    Completed lessons are stored in st.session_state["completed"], the same set
    the Home page reads, so progress shows up there.
    """
    st.divider()

    challenges = CHALLENGES.get(number, [])
    if challenges:
        st.subheader("🎯 Challenge")
        for index, item in enumerate(challenges):
            choice = st.radio(
                item.question,
                item.options,
                index=None,
                key=f"challenge_{number}_{index}",
            )
            if choice is not None:
                if item.options.index(choice) == item.answer:
                    st.success(f"Correct! {item.explanation}")
                else:
                    st.error("Not quite. Try again.")

    completed = st.session_state.setdefault("completed", set())
    key = f"page_done_{number}"

    def _toggle() -> None:
        if st.session_state[key]:
            completed.add(number)
        else:
            completed.discard(number)

    st.checkbox(
        "Mark this lesson as done",
        value=number in completed,
        key=key,
        on_change=_toggle,
    )

    _download_row(number)
    _feedback_row(number)
    _lesson_nav(number)


@st.cache_data
def _standalone_script(number: int) -> str:
    return build_script(number)


def _download_row(number: int) -> None:
    """A button that downloads this lesson as a script that runs on its own."""
    lesson = next(item for item in LESSONS if item.number == number)
    st.download_button(
        "⬇️ Download this lesson as a .py file",
        data=_standalone_script(number),
        file_name=lesson.file,
        mime="text/x-python",
        key=f"download_{number}",
    )
    st.caption(f"Run it on your own computer with: streamlit run {lesson.file}")


def _feedback_row(number: int) -> None:
    """A link that opens a pre-filled GitHub issue about this lesson."""
    lesson = next(item for item in LESSONS if item.number == number)
    st.link_button("💬 Was this helpful? Share feedback", feedback_url(lesson))
    st.caption("Opens a pre-filled GitHub issue. You need a free GitHub account to send it.")


def _lesson_nav(number: int) -> None:
    """Previous / Home / Next buttons at the very end of a lesson."""
    st.divider()
    previous, following = neighbours(number)
    left, middle, right = st.columns(3)
    if previous is not None and left.button(f"← {previous.title}", key=f"nav_prev_{number}"):
        st.switch_page(previous.path)
    if middle.button("🏠 Home", key=f"nav_home_{number}"):
        st.switch_page("Home.py")
    if following is not None and right.button(f"{following.title} →", key=f"nav_next_{number}"):
        st.switch_page(following.path)
