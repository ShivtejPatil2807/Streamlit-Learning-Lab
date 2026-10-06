import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section

lesson_page(19, "Check your app with automatic tests instead of clicking through it every time.")


@demo(
    "assert",
    "A test is code that checks a result and fails loudly when it is wrong. "
    "assert raises an AssertionError when the check is false.",
    caption="Change the number to 6 and watch the test fail.",
)
def _():
    def add(a, b):
        return a + b

    expected = st.number_input("Expected result of add(2, 3)", value=5, step=1)

    try:
        assert add(2, 3) == expected
        st.success("Test passed")
    except AssertionError:
        st.error(f"Test failed: add(2, 3) is {add(2, 3)}, not {expected}")


@demo(
    "AppTest.from_function()",
    "Streamlit's AppTest runs an app in memory, so you can click buttons and read "
    "the result without opening a browser.",
    run=False,
)
def _():
    from streamlit.testing.v1 import AppTest

    def counter_app():
        import streamlit as st

        if "count" not in st.session_state:
            st.session_state.count = 0
        if st.button("Add"):
            st.session_state.count += 1
        st.write(f"Count: {st.session_state.count}")

    at = AppTest.from_function(counter_app).run()
    assert at.markdown[0].value == "Count: 0"

    at.button[0].click().run()
    assert at.markdown[0].value == "Count: 1"


@demo(
    "AppTest.from_file()",
    "Test a whole page of your app. Set a widget's value, run again, and check what is left. "
    "This is how this project tests its Home page.",
    run=False,
)
def _():
    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file("Home.py").run()
    at.text_input[0].set_value("chart").run()
    assert len(at.checkbox) == 1  # only one lesson card is left


section(
    "Running the tests",
    "pytest finds every function that starts with test_ and reports which ones fail.",
)
st.code("pip install pytest\npython -m pytest -v", language="bash")

section(
    "Running them on every push",
    "GitHub Actions can run your tests each time you push, and show a red cross when "
    "something breaks. Save this as .github/workflows/ci.yml:",
)
st.code(
    """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.12"
      - run: pip install -r requirements-dev.txt
      - run: python -m pytest
""",
    language="yaml",
)


lesson_footer(19)
