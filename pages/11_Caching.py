import time
import streamlit as st

st.set_page_config(page_title="Caching", page_icon="⚡")

st.title("⚡ Caching")
st.write(
    "Streamlit reruns your whole script on every interaction. Caching stops it "
    "from redoing slow work (like loading a big file) when nothing changed."
)

st.divider()
st.header("1. st.cache_data()")
st.write(
    "Caches the return value of a function that returns data (numbers, dataframes, etc). "
    "The cache is keyed by the function's arguments: the same number is instant the "
    "second time, but a new number is slow again."
)
st.code(
    '''@st.cache_data
def slow_calculation(n):
    time.sleep(2)
    return n * n

n = st.number_input("Number to square", value=5, step=1)

if st.button("Run slow calculation"):
    start = time.time()
    result = slow_calculation(n)
    st.write("Result:", result)
    st.write(f"Took {time.time() - start:.2f} seconds")''',
    language="python",
)

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

st.caption("Click twice with the same number (fast the second time), then try a different number.")

st.divider()
st.header("2. st.cache_resource()")
st.write(
    "Caches objects that shouldn't be recreated each time, like a database connection "
    "or an ML model. Unlike cache_data, you get back the very same object every time "
    "(not a copy), shared by everyone using the app."
)
st.code(
    '''@st.cache_resource
def load_model():
    time.sleep(2)  # pretend this is slow, like loading a big ML model
    return {"name": "pretend_model", "loaded_at": time.time()}

if st.button("Load model"):
    model = load_model()
    st.write("Model:", model["name"])
    st.write("Loaded at:", time.strftime("%H:%M:%S", time.localtime(model["loaded_at"])))''',
    language="python",
)


@st.cache_resource
def load_model():
    time.sleep(2)  
    return {"name": "pretend_model", "loaded_at": time.time()}


if st.button("Load model"):
    model = load_model()
    st.write("Model:", model["name"])
    st.write("Loaded at:", time.strftime("%H:%M:%S", time.localtime(model["loaded_at"])))

st.caption("Click again: the 'Loaded at' time doesn't change, because the same model object is reused.")

st.divider()
st.header("3. cache_data vs cache_resource")
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

st.divider()
st.header("4. Clearing the caches")
st.write("Use this while developing, or when the underlying data has changed.")
st.code(
    '''if st.button("Clear all caches"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("Caches cleared - the next run will be slow again.")''',
    language="python",
)
if st.button("Clear all caches"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("Caches cleared - the next run will be slow again.")
