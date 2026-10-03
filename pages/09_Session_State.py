import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(
    9,
    "Normally, Streamlit forgets everything and reruns your script top to bottom "
    "on every interaction. st.session_state is a dictionary that survives "
    "between reruns, so your app can remember things.",
)


@demo(
    "Creating and reading session state",
    "Store a value the first time, then reuse it on every rerun.",
)
def _():
    if "count" not in st.session_state:
        st.session_state.count = 0

    st.write("Count is:", st.session_state.count)


@demo(
    "Updating session state",
    "A button click can update the stored value, and it stays updated after the rerun.",
)
def _():
    if st.button("Increment"):
        st.session_state.count += 1
    st.write("Current count:", st.session_state.count)


@demo(
    "Widget keys as session state",
    "Every widget with a key= automatically stores its value in st.session_state.",
)
def _():
    st.text_input("Your name", key="username")
    st.write("Stored value:", st.session_state.get("username", ""))


lesson_footer(9)
