import streamlit as st

from core.lessons import CATEGORIES, LEVELS, LESSONS, total_functions
from core.theme import apply_theme

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


# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
        <h1>📚 Streamlit Learning Lab</h1>
        <p>A hands-on reference for learning Streamlit. Pick a topic, read the code,
        and see the live result right below it.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Stats ----------
c1, c2, c3 = st.columns(3)
c1.metric("Lessons", len(LESSONS))
c2.metric("Functions covered", total_functions())
c3.metric("Completed", f"{len(completed)} / {len(LESSONS)}")
st.progress(len(completed) / len(LESSONS))

st.divider()

# ---------- Filters ----------
f1, f2, f3 = st.columns([2, 1, 1])
query = f1.text_input("🔎 Search lessons or functions", placeholder="e.g. chart, session, st.form")
category = f2.selectbox("Category", ["All"] + CATEGORIES)
levels = f3.multiselect("Level", LEVELS, default=LEVELS)


def matches(lesson) -> bool:
    q = query.strip().lower()
    haystack = " ".join([lesson.title, lesson.summary, *lesson.functions]).lower()
    return (
        (not q or q in haystack)
        and (category == "All" or lesson.category == category)
        and lesson.level in levels
    )


results = [lesson for lesson in LESSONS if matches(lesson)]

# ---------- Lesson grid ----------
st.subheader(f"Lessons ({len(results)})")

if not results:
    st.warning("No lessons match your filters. Try clearing the search.")

cols = st.columns(3)
for i, lesson in enumerate(results):
    with cols[i % 3].container(border=True):
        st.markdown(f"### {lesson.icon} {lesson.number:02d}. {lesson.title}")
        st.caption(f"{lesson.category} · {lesson.level}")
        st.write(lesson.summary)
        st.caption(" · ".join(f"`{fn}`" for fn in lesson.functions[:4]))
        st.page_link(lesson.path, label="Open lesson", icon="➡️")
        st.checkbox(
            "Mark as done",
            value=lesson.number in completed,
            key=f"done_{lesson.number}",
            on_change=toggle_done,
            args=(lesson.number,),
        )

# ---------- How it works ----------
with st.expander("How does each lesson work?"):
    st.markdown(
        """
        1. **Title**: the name of the function
        2. **Code**: the exact code that produces the result
        3. **Output**: the live result, rendered right below the code
        """
    )