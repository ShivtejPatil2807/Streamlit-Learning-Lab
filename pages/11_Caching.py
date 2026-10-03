import time

import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section

lesson_page(
    11,
    "Streamlit reruns your whole script on every interaction. Caching stops it "
    "from redoing slow work (like loading a big file) when nothing changed.",
)


@demo(
    "st.cache_data()",
    "Caches the return value of a function that returns data (numbers, dataframes, etc). "
    "The cache is keyed by the function's arguments: the same number is instant the "
    "second time, but a new number is slow again.",
    caption="Click twice with the same number (fast the second time), then try a different number.",
)
def _():
    @st.cache_data
    def slow_calculation(n):
        time.sleep(2)
        return n * n

    n = st.number_input("Number to square", value=5, step=1)

    if st.button("Run slow calculation"):
        start = time.time()
        result = slow_calculation(n)
        st.write("Result:", result)
        st.write(f"Took {time.time() - start:.2f} seconds")


@demo(
    "st.cache_resource()",
    "Caches objects that shouldn't be recreated each time, like a database connection "
    "or an ML model. Unlike cache_data, you get back the very same object every time "
    "(not a copy), shared by everyone using the app.",
    caption="Click again: the 'Loaded at' time doesn't change, because the same model object is reused.",
)
def _():
    @st.cache_resource
    def load_model():
        time.sleep(2)  # pretend this is slow, like loading a big ML model
        return {"name": "pretend_model", "loaded_at": time.time()}

    if st.button("Load model"):
        model = load_model()
        st.write("Model:", model["name"])
        st.write("Loaded at:", time.strftime("%H:%M:%S", time.localtime(model["loaded_at"])))


section("cache_data vs cache_resource")
st.markdown(
    """
| | `st.cache_data` | `st.cache_resource` |
|---|---|---|
| Use it for | Data: numbers, text, dataframes, query results | Shared objects: ML models, database connections |
| What you get back | A fresh copy each time (safe to modify) | The same object each time (shared) |
"""
)
st.write(
    "Both accept a `ttl` so entries expire on their own, for example "
    "`@st.cache_data(ttl=60)` keeps results for 60 seconds."
)


@demo(
    "Clearing the caches",
    "Use this while developing, or when the underlying data has changed.",
)
def _():
    if st.button("Clear all caches"):
        st.cache_data.clear()
        st.cache_resource.clear()
        st.success("Caches cleared - the next run will be slow again.")


lesson_footer(11)
