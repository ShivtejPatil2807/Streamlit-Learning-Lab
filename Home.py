import html

import streamlit as st

from core.lessons import CATEGORIES, LESSONS, LEVELS, total_functions
from core.paths import PATHS, next_in_path, path_lessons, path_progress
from core.theme import apply_theme, chips, level_pill, pill

st.set_page_config(page_title="Streamlit Learning Lab", page_icon="📚", layout="wide")
apply_theme()

# Completed lessons live in a plain set so they survive page navigation.
st.session_state.setdefault("completed", set())
completed: set[int] = st.session_state["completed"]


def toggle_done(number: int) -> None:
    if st.session_state[f"done_{number}"]:
        completed.add(number)
    else:
        completed.discard(number)


def card_top(lesson) -> str:
    """The text part of a lesson card, as one block of HTML."""
    badges = level_pill(lesson.level) + pill(lesson.category, "category")
    if lesson.number in completed:
        badges += pill("✓ Done", "beginner")
    return "".join(
        [
            '<div class="lab-card-title">',
            f'<span class="lab-card-icon" aria-hidden="true">{lesson.icon}</span>',
            '<span class="lab-card-name">',
            f'<span class="lab-card-num">{lesson.number:02d}</span>{html.escape(lesson.title)}',
            "</span></div>",
            f'<div class="lab-meta">{badges}</div>',
            f'<p class="lab-summary">{html.escape(lesson.summary)}</p>',
            f'<div class="lab-chips">{chips(lesson.functions[:4])}</div>',
        ]
    )


def path_top(path, done: int, total: int) -> str:
    """The text part of a learning-path card, as one block of HTML."""
    titles = [lesson.title for lesson in path_lessons(path)]
    progress_label = pill(f"{done} / {total} done", "beginner" if done == total else "category")
    return "".join(
        [
            '<div class="lab-path">',
            '<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem">',
            f'<span class="lab-card-icon" aria-hidden="true">{path.icon}</span>',
            f'<span class="lab-card-name">{html.escape(path.title)}</span></div>',
            f'<div class="lab-meta">{pill(f"{total} lessons", "category")}{progress_label}</div>',
            f'<p class="lab-summary">{html.escape(path.summary)}</p>',
            f'<div class="lab-chips">{chips(titles)}</div>',
            "</div>",
        ]
    )


# ---------- Hero ----------
HERO_HTML = (
    '<div class="lab-hero">'
    '<div class="lab-kicker">📚 INTERACTIVE STREAMLIT COURSE</div>'
    "<h1>Streamlit Learning Lab</h1>"
    "<p>Learn one function at a time: read it, copy the code, see it run.</p>"
    '<div class="lab-steps">'
    '<span class="lab-step">📖 Learn</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">💻 Code</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">▶️ Try</span><span class="lab-arrow">→</span>'
    '<span class="lab-step">🎯 Challenge</span>'
    "</div></div>"
)
st.markdown(HERO_HTML, unsafe_allow_html=True)


# ---------- Stats ----------
c1, c2, c3 = st.columns(3)
c1.metric("Lessons", len(LESSONS))
c2.metric("Functions covered", total_functions())
c3.metric("Completed", f"{len(completed)} / {len(LESSONS)}")
st.progress(len(completed) / len(LESSONS))

# ---------- Next up ----------
remaining = [lesson for lesson in LESSONS if lesson.number not in completed]
if remaining:
    next_lesson = remaining[0]
    st.caption(f"Next up: {next_lesson.number}. {next_lesson.title}")
    st.page_link(next_lesson.path, label=f"Continue with {next_lesson.title}", icon="▶️")
else:
    st.success("🎉 You finished every lesson. Well done!")

# ---------- Learning paths ----------
st.subheader("Learning paths")
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

st.divider()

# ---------- Filters ----------
f1, f2, f3, f4 = st.columns([2, 1, 1, 1])
query = f1.text_input("🔎 Search lessons or functions", placeholder="e.g. chart, session, st.form")
category = f2.selectbox("Category", ["All"] + CATEGORIES)
levels = f3.multiselect("Level", LEVELS, default=LEVELS)
path_name = f4.selectbox("Learning path", ["All lessons"] + [path.title for path in PATHS])

chosen_path = next((path for path in PATHS if path.title == path_name), None)


def matches(lesson) -> bool:
    q = query.strip().lower()
    haystack = " ".join([lesson.title, lesson.summary, *lesson.functions]).lower()
    return (
        (not q or q in haystack)
        and (category == "All" or lesson.category == category)
        and lesson.level in levels
        and (chosen_path is None or lesson.number in chosen_path.lessons)
    )


results = [lesson for lesson in LESSONS if matches(lesson)]
if chosen_path is not None:
    results.sort(key=lambda lesson: chosen_path.lessons.index(lesson.number))

# ---------- Lesson grid ----------
st.subheader(f"Lessons ({len(results)})")

if not results:
    st.warning("No lessons match your filters. Try clearing the search.")

for start in range(0, len(results), 3):
    for col, lesson in zip(st.columns(3), results[start : start + 3]):
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

# ---------- How it works ----------
with st.expander("How does each lesson work?"):
    st.markdown(
        """
        Every function has three tabs:

        1. **📖 Learn**: what the function does
        2. **💻 Code**: the exact code that produces the result
        3. **▶️ Try**: the live result, running on the page

        At the end of each lesson, answer the **🎯 Challenge** and tick
        **Mark this lesson as done** to fill the progress bar.
        """
    )
