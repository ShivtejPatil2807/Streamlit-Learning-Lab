import html
from datetime import date

import streamlit as st

from core.export import REPO_URL
from core.lessons import LESSONS, LEVELS, total_functions
from core.paths import PATHS, next_in_path, path_lessons, path_progress
from core.search import search_lessons
from core.theme import apply_theme, chips, level_pill, pill

st.set_page_config(page_title="Streamlit Learning Lab", page_icon="📚", layout="wide")
apply_theme()

# Completed lessons live in a plain set so they survive page navigation.
st.session_state.setdefault("completed", set())
completed: set[int] = st.session_state["completed"]
st.session_state.setdefault("stage", None)  # the level whose lessons are open, or None

BRAND_HTML = '<div class="lab-brand"><span class="lab-brand-logo" aria-hidden="true">📚</span>Learning Lab</div>'

HERO_HTML = (
    '<div class="lab-hero">'
    '<div class="lab-kicker">INTERACTIVE STREAMLIT COURSE</div>'
    "<h1>Streamlit Learning Lab</h1>"
    "<p>A hands-on course for learning Streamlit. Read the code, see it run, then test yourself. "
    "Free and open source.</p>"
    '<div class="lab-steps">'
    '<span class="lab-step">📖 Learn</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">💻 Code</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">▶️ Try</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">🎯 Challenge</span>'
    "</div></div>"
)

STAGE_INFO = {
    "Beginner": ("🌱", "Start here. Learn to show content, take input and arrange a page."),
    "Intermediate": ("🌿", "Data, files, state, forms and your first dashboard."),
    "Advanced": ("🌳", "Caching, navigation, login, testing and the bigger projects."),
}

HOW_ROWS = [
    ("orange", "🌱", "Start", "with the Beginner lessons. Each one teaches a few Streamlit functions, from text to layouts."),
    ("purple", "💻", "Practice", "with Learn, Code and Try. Read the explanation, copy the exact code, then watch it run."),
    ("cyan", "🚀", "Build", "something real. Follow a learning path to an iris classifier, a sales dashboard or a chatbot."),
]

LINKS = [
    ("#24292F", "🐙", "GitHub", "View the source code and the issue tracker.", REPO_URL),
    ("#C0261C", "📘", "Streamlit docs", "The official reference for every Streamlit function.", "https://docs.streamlit.io"),
    ("#1D4ED8", "💬", "Streamlit forum", "Ask questions and share what you build.", "https://discuss.streamlit.io"),
    ("#0E7490", "☁️", "Community Cloud", "Deploy your own Streamlit app for free.", "https://streamlit.io/cloud"),
]

COMMUNITY_HTML = (
    '<div class="lab-community">'
    "<h3>Help improve the Lab</h3>"
    "<p>This course is free and open source. Found a mistake, or have an idea for a new lesson? "
    "Open an issue on GitHub, or star the project to show your support.</p>"
    f'<a class="lab-button" href="{REPO_URL}/issues" target="_blank" rel="noopener noreferrer">Open an issue</a>'
    f'<a class="lab-button dark" href="{REPO_URL}" target="_blank" rel="noopener noreferrer">View on GitHub</a>'
    "</div>"
)

FOOTER_HTML = (
    '<div class="lab-footer">'
    "<div>Streamlit Learning Lab · free and open source, made for learning.</div>"
    '<div class="lab-footer-links">'
    f'<a href="{REPO_URL}" target="_blank" rel="noopener noreferrer">Source on GitHub</a>'
    f'<a href="{REPO_URL}/issues" target="_blank" rel="noopener noreferrer">Report an issue</a>'
    '<a href="https://docs.streamlit.io" target="_blank" rel="noopener noreferrer">Streamlit docs</a>'
    "</div>"
    f'<div class="lab-footer-copy">© {date.today().year} Streamlit Learning Lab. '
    "An independent learning project, not affiliated with Streamlit or Snowflake.</div>"
    "</div>"
)


def open_stage(level: str) -> None:
    st.session_state["stage"] = level


def close_stage() -> None:
    st.session_state["stage"] = None


def toggle_done(number: int) -> None:
    if st.session_state[f"done_{number}"]:
        completed.add(number)
    else:
        completed.discard(number)


def result_html(lesson) -> str:
    """One search result, as a block of HTML."""
    return (
        '<div class="lab-result">'
        f'<strong><span aria-hidden="true">{lesson.icon}</span> {lesson.number}. {html.escape(lesson.title)}</strong>'
        f"<p>{html.escape(lesson.summary)}</p>"
        "</div>"
    )


def stage_top(level: str, lessons: list, done: int, is_open: bool) -> str:
    """The text part of a level tile, as one block of HTML."""
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
        f'<div class="lab-stage" data-level="{html.escape(level.lower())}">'
        '<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem">'
        f'<span class="lab-card-icon" aria-hidden="true">{icon}</span>'
        f'<span class="lab-card-name">{html.escape(level)}</span></div>'
        f'<div class="lab-meta">{badges}</div>'
        f'<p class="lab-summary">{html.escape(text)}</p>'
        f'<div class="lab-chips">{chips(titles)}</div>'
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


def news_top(lesson) -> str:
    """One 'latest lesson' card, as a block of HTML."""
    codes = " ".join(f'<span class="lab-code">{html.escape(name)}</span>' for name in lesson.functions[:3])
    return (
        '<div class="lab-news">'
        f'<div class="lab-news-icon" aria-hidden="true">{lesson.icon}</div>'
        f"<h3>{html.escape(lesson.title)}</h3>"
        f"<p>{html.escape(lesson.summary)}</p>"
        f"<p>{codes}</p>"
        "</div>"
    )


def how_html() -> str:
    return "".join(
        '<div class="lab-how">'
        f'<div class="lab-how-icon lab-how-{color}" aria-hidden="true">{icon}</div>'
        f'<p><strong class="{color}">{lead}</strong> {text}</p>'
        "</div>"
        for color, icon, lead, text in HOW_ROWS
    )


def link_rows(links) -> str:
    return "".join(
        '<div class="lab-link-row">'
        f'<div class="lab-link-icon" style="background:{color}" aria-hidden="true">{icon}</div>'
        f'<div><a href="{url}" target="_blank" rel="noopener noreferrer">{html.escape(name)}</a>'
        f"<p>{html.escape(text)}</p></div>"
        "</div>"
        for color, icon, name, text, url in links
    )


# ---------- Top bar: brand and search ----------
brand_col, search_col = st.columns([3, 2])
brand_col.markdown(BRAND_HTML, unsafe_allow_html=True)
query = search_col.text_input(
    "Search lessons",
    key="search",
    placeholder="Search lessons, for example chart or session",
    label_visibility="collapsed",
)
if query.strip():
    with st.container(border=True):
        found = search_lessons(query)
        if found:
            for lesson in found:
                st.markdown(result_html(lesson), unsafe_allow_html=True)
                st.page_link(lesson.path, label=f"Jump to {lesson.title}", icon=lesson.icon)
        else:
            st.caption(f"No lessons match “{query.strip()}”. Try a function name or a topic.")

# ---------- Title ----------
st.markdown(HERO_HTML, unsafe_allow_html=True)

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

# ---------- Your progress ----------
st.header("Your progress")
c1, c2, c3 = st.columns(3)
c1.metric("Lessons", len(LESSONS))
c2.metric("Functions covered", total_functions())
c3.metric("Completed", f"{len(completed)} / {len(LESSONS)}")

remaining = [lesson for lesson in LESSONS if lesson.number not in completed]
next_lesson = remaining[0] if remaining else None
with st.container(border=True):
    if next_lesson is not None:
        left, right = st.columns([3, 1])
        left.progress(len(completed) / len(LESSONS))
        left.caption(f"Next up: {next_lesson.number}. {next_lesson.title}")
        if right.button("▶ Continue" if completed else "▶ Start learning", type="primary", key="start"):
            st.switch_page(next_lesson.path)
    else:
        st.progress(1.0)
        st.success("🎉 You finished every lesson. Well done!")

# ---------- How to use the Lab ----------
st.header("How to use the Lab")
st.markdown(how_html(), unsafe_allow_html=True)

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

# ---------- Latest lessons ----------
st.header("Latest lessons")
st.caption("The newest additions to the course.")
latest = sorted(LESSONS, key=lambda lesson: -lesson.number)[:6]
for start in range(0, len(latest), 3):
    for col, lesson in zip(st.columns(3), latest[start : start + 3]):
        with col.container(border=True):
            st.markdown(news_top(lesson), unsafe_allow_html=True)
            st.page_link(lesson.path, label=f"Read {lesson.title}", icon="📖")

# ---------- Community ----------
st.markdown(COMMUNITY_HTML, unsafe_allow_html=True)

# ---------- Elsewhere ----------
st.header("Elsewhere")
first_links, second_links = st.columns(2)
first_links.markdown(link_rows(LINKS[:2]), unsafe_allow_html=True)
second_links.markdown(link_rows(LINKS[2:]), unsafe_allow_html=True)

# ---------- Next ----------
if next_lesson is not None:
    st.page_link(next_lesson.path, label=f"Next: {next_lesson.title} →", icon="➡️")

# ---------- Footer ----------
st.markdown(FOOTER_HTML, unsafe_allow_html=True)
