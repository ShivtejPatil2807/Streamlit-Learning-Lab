import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(
    10,
    "A form groups several widgets together so the app only reruns once, "
    "when the Submit button is pressed, not after every single input.",
)


@demo(
    "st.form() and st.form_submit_button()",
    "Wrap widgets in a form, then use a submit button to process them all at once.",
)
def _():
    with st.form("my_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Hi {name}, you are {age} years old.")


lesson_footer(10)
