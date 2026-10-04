import time

import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(15, "Show extra content on top of the page, only when the learner asks for it.")


@demo(
    "st.dialog()",
    "A decorator that turns a function into a pop-up window. Call the function to open it.",
)
def _():
    @st.dialog("Say hello")
    def hello_dialog():
        name = st.text_input("Your name")
        if st.button("Submit"):
            st.session_state.hello_name = name
            st.rerun()

    if st.button("Open dialog"):
        hello_dialog()

    if "hello_name" in st.session_state:
        st.write(f"Hello, {st.session_state.hello_name}!")


@demo(
    "st.popover()",
    "A button that opens a small floating panel. Good for settings and filters.",
)
def _():
    with st.popover("Open settings"):
        st.write("Settings panel")
        enabled = st.checkbox("Enable notifications")

    st.write("Notifications:", "on" if enabled else "off")


@demo(
    "st.status()",
    "A container that shows the progress of a longer task, and can collapse when it finishes.",
)
def _():
    if st.button("Run task"):
        with st.status("Working...", expanded=True) as status:
            st.write("Loading data...")
            time.sleep(1)
            st.write("Crunching numbers...")
            time.sleep(1)
            status.update(label="Done!", state="complete", expanded=False)


lesson_footer(15)
