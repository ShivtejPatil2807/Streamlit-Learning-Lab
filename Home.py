import html

import streamlit as st

from core.export import REPO_URL
from core.lessons import LESSONS, LEVELS, total_functions
from core.paths import PATHS, next_in_path, path_lessons, path_progress
from core.theme import apply_theme, chips, level_pill, pill

st.set_page_config(page_title="Streamlit Learning Lab", page_icon="📚", layout="wide")
apply_theme()

# Completed lessons live in a plain set so they survive page navigation.
st.session_state.setdefault("completed", set())
completed: set[int] = st.session_state["completed"]

HERO_HTML = (
    '<div class="lab-hero">'
    '<div class="lab-kicker">📚 INTERACTIVE STREAMLIT COURSE</div>'
    "<h1>Streamlit Learning Lab</h1>"
    "<p>Learn Streamlit by doing: read the code, see it run, then test yourself. "
    "Free and open source.</p>"
    '<div class="lab-steps">'
    '<span class="lab-step">📖 Learn</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">💻 Code</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">▶️ Try</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">🎯 Challenge</span>'
    "</div></div>"
)

TILES = [
    ("📖", "Learn → Code → Try", "Every function has a short explanation, the exact code and a live result on the page."),
    ("🎯", "Challenges", "End each lesson with a quick question, and tick it off to track your progress."),
    ("🚀", "Real projects", "Build an iris classifier, a sales dashboard and a chatbot."),
    ("⬇️", "Take it home", "Download any lesson as a .py file and run it on your own computer."),
]

FOOTER_HTML = (
    '<div class="lab-footer">'
    "<div>Streamlit Learning Lab · free and open source, made for learning.</div>"
    '<div class="lab-footer-links">'
    f'<a href="{REPO_URL}" target="_blank" rel="noopener noreferrer">Source on GitHub</a>'
    f'<a href="{REPO_URL}/issues" target="_blank" rel="noopener noreferrer">Report an issue</a>'
    '<a href="https://docs.streamlit.io" target="_blank" rel="noopener noreferrer">Streamlit docs</a>'
    "</div></div>"
)


STAGE_INFO = {
    "Beginner": ("🌱", "Start here. Learn to show content, take input and arrange a page."),
    "Intermediate": ("🌿", "Data, files, state, forms and your first dashboard."),
    "Advanced": ("🌳", "Caching, navigation, login, testing and the bigger projects."),
}

st.session_state.setdefault("stage", None)  # the level whose lessons are open, or None


def open_stage(level: str) -> None:
    st.session_state["stage"] = level


def close_stage() -> None:
    st.session_state["stage"] = None


def toggle_done(number: int) -> None:
    if st.session_state[f"done_{number}"]:
        completed.add(number)
    else:
        completed.discard(number)


def tile_html(icon: str, title: str, text: str) -> str:
    return (
        '<div class="lab-tile">'
        f'<div class="lab-tile-icon" aria-hidden="true">{icon}</div>'
        f"<h3>{html.escape(title)}</h3>"
        f"<p>{html.escape(text)}</p>"
        "</div>"
    )


def card_top(lesson) -> str:
    """The text part of a lesson card, as one block of HTML."""
    badges = level_pill(lesson.level) + pill(lesson.category, "category")
    if lesson.number in completed:
        badges += pill("✓ Done", "beginner")
    return (
        '<div class="lab-card-title">'
        f'<span class="lab-card-icon" aria-hidden="true">{lesson.icon}</span>'
        '<span class="lab-card-name">'
        f'<span class="lab-card-num">{lesson.number:02d}</span>{html.escape(lesson.title)}'
        "</span></div>"
        f'<div class="lab-meta">{badges}</div>'
        f'<p class="lab-summary">{html.escape(lesson.summary)}</p>'
        f'<div class="lab-chips">{chips(lesson.functions[:4])}</div>'
    )


def stage_top(level: str, lessons: list, done: int, is_open: bool) -> str:
    """The text part of a level card, as one block of HTML."""
    icon, text = STAGE_INFO.get(level, ("📚", ""))
    total = len(lessons)
    badges = pill(f"{total} lessons", "category")
    badges += pill(f"{done} / {total} done", "beginner" if total and done == total else "category")
    if is_open:
        badges += pill("▼ Showing below", level.lower())
    titles = [lesson.title for lesson in lessons[:5]]
    if total > 5:
        titles.append(f"+{total - 5} more")
    return (
        '<div class="lab-stage">'
        '<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem">'
        f'<span class="lab-card-icon" aria-hidden="true">{icon}</span>'
        f'<span class="lab-card-name">{html.escape(level)}</span></div>'
        f'<div class="lab-meta">{badges}</div>'
        f'<p class="lab-summary">{html.escape(text)}</p>'
        f'<div class="lab-chips">{chips(titles)}</div>'
        "</div>"
    )


def path_top(path, done: int, total: int) -> str:
    """The text part of a learning-path card, as one block of HTML."""
    titles = [lesson.title for lesson in path_lessons(path)]
    progress_label = pill(f"{done} / {total} done", "beginner" if done == total else "category")
    return (
        '<div class="lab-path">'
        '<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem">'
        f'<span class="lab-card-icon" aria-hidden="true">{path.icon}</span>'
        f'<span class="lab-card-name">{html.escape(path.title)}</span></div>'
        f'<div class="lab-meta">{pill(f"{total} lessons", "category")}{progress_label}</div>'
        f'<p class="lab-summary">{html.escape(path.summary)}</p>'
        f'<div class="lab-chips">{chips(titles)}</div>'
        "</div>"
    )


# ---------- Hero ----------
st.markdown(HERO_HTML, unsafe_allow_html=True)

# ---------- Stats ----------
c1, c2, c3 = st.columns(3)
c1.metric("Lessons", len(LESSONS))
c2.metric("Functions covered", total_functions())
c3.metric("Completed", f"{len(completed)} / {len(LESSONS)}")

# ---------- Where to go next ----------
remaining = [lesson for lesson in LESSONS if lesson.number not in completed]
with st.container(border=True):
    if remaining:
        next_lesson = remaining[0]
        left, right = st.columns([3, 1])
        left.progress(len(completed) / len(LESSONS))
        left.caption(f"Next up: {next_lesson.number}. {next_lesson.title}")
        if right.button("▶ Continue" if completed else "▶ Start learning", type="primary", key="start"):
            st.switch_page(next_lesson.path)
    else:
        st.progress(1.0)
        st.success("🎉 You finished every lesson. Well done!")

# ---------- What you get ----------
st.header("What you get")
for col, (icon, title, text) in zip(st.columns(len(TILES)), TILES):
    col.markdown(tile_html(icon, title, text), unsafe_allow_html=True)

# ---------- Learning paths ----------
st.header("Learning paths")
st.caption("Short routes through the lessons. Pick the goal you care about.")
for col, path in zip(st.columns(len(PATHS)), PATHS):
    done, total = path_progress(path, completed)
    upcoming = next_in_path(path, completed)
    with col.container(border=True):
        st.markdown(path_top(path, done, total), unsafe_allow_html=True)
        st.progress(done / total)
        if upcoming is None:
            st.caption("✓ Path completed")
        else:
            verb = "Start" if done == 0 else "Continue"
            st.page_link(upcoming.path, label=f"{verb}: {upcoming.title}", icon="▶️")

# ---------- Choose your level ----------
st.header("Choose your level")
st.caption("Open a level to see its lessons.")
selected = st.session_state["stage"]
for col, level in zip(st.columns(len(LEVELS)), LEVELS):
    in_level = [lesson for lesson in LESSONS if lesson.level == level]
    done = sum(1 for lesson in in_level if lesson.number in completed)
    with col.container(border=True):
        st.markdown(stage_top(level, in_level, done, selected == level), unsafe_allow_html=True)
        st.progress(done / len(in_level) if in_level else 0.0)
        st.button(
            f"Open {level}",
            key=f"stage_{level.lower()}",
            type="primary" if selected == level else "secondary",
            on_click=open_stage,
            args=(level,),
        )

if selected in LEVELS:
    in_stage = [lesson for lesson in LESSONS if lesson.level == selected]
    st.header(f"{selected} lessons")
    st.caption(f"{len(in_stage)} lessons. Tick each one off as you finish it.")
    st.button("Hide these lessons", key="stage_close", on_click=close_stage)
    for start in range(0, len(in_stage), 3):
        for col, lesson in zip(st.columns(3), in_stage[start : start + 3]):
            with col.container(border=True):
                st.markdown(card_top(lesson), unsafe_allow_html=True)
                st.page_link(lesson.path, label=lesson.open_label, icon="➡️")
                st.checkbox(
                    lesson.done_label,
                    value=lesson.number in completed,
                    key=f"done_{lesson.number}",
                    on_change=toggle_done,
                    args=(lesson.number,),
                )

# ---------- Footer ----------
st.markdown(FOOTER_HTML, unsafe_allow_html=True)
