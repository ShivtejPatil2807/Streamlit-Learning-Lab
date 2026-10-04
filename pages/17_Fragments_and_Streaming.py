import time

import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(17, "Rerun just part of a page, and show text as it is being produced.")


@demo(
    "st.fragment()",
    "A decorator that lets one part of the page rerun on its own, "
    "without rerunning the whole script.",
    caption="Click the button: the count changes but the time does not.",
)
def _():
    @st.fragment
    def counter():
        if "fragment_clicks" not in st.session_state:
            st.session_state.fragment_clicks = 0
        if st.button("Click inside the fragment"):
            st.session_state.fragment_clicks += 1
        st.write("Clicks:", st.session_state.fragment_clicks)

    counter()
    st.write("Whole page last ran at:", time.strftime("%H:%M:%S"))


@demo(
    "st.write_stream()",
    "Writes text piece by piece, like a chatbot typing. It accepts a generator.",
)
def _():
    def word_stream():
        for word in ["Streamlit", "can", "stream", "text", "one", "word", "at", "a", "time."]:
            yield word + " "
            time.sleep(0.15)

    if st.button("Stream text"):
        st.write_stream(word_stream())


lesson_footer(17)
