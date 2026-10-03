import time

import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(8, "These functions give the user feedback about what's happening.")


@demo("st.success()", "Shows a green success message.")
def _():
    st.success("Task completed successfully!")


@demo("st.error()", "Shows a red error message.")
def _():
    st.error("Something went wrong.")


@demo("st.warning()", "Shows a yellow warning message.")
def _():
    st.warning("This action cannot be undone.")


@demo("st.info()", "Shows a blue informational message.")
def _():
    st.info("Streamlit auto-reruns on every interaction.")


@demo("st.progress()", "Shows a progress bar for a value between 0 and 100.")
def _():
    st.progress(70)


@demo("st.spinner()", "Shows a spinner while a block of code is running.")
def _():
    if st.button("Run spinner demo"):
        with st.spinner("Loading..."):
            time.sleep(1)
        st.write("Done!")


@demo("st.toast()", "Shows a small temporary notification in the corner of the screen.")
def _():
    if st.button("Show toast"):
        st.toast("Saved!")


@demo("st.balloons()", "Celebrates with floating balloons across the screen.")
def _():
    if st.button("Launch balloons"):
        st.balloons()


lesson_footer(8)
