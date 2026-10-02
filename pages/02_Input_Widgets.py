import streamlit as st

from core.components import demo, lesson_page

lesson_page(2, "Widgets let the user send information back into your app.")


@demo("st.button()", "A clickable button. Returns True only on the run right after it's clicked.")
def _():
    if st.button("Click me"):
        st.success("Button was clicked!")


@demo("st.checkbox()", "A box the user can tick on or off.")
def _():
    agree = st.checkbox("I agree")
    st.write("Checked:", agree)


@demo("st.radio()", "Lets the user pick exactly one option from a list.")
def _():
    choice = st.radio("Pick one", ["Python", "Java", "C++"])
    st.write("You picked:", choice)


@demo("st.selectbox()", "A dropdown menu: pick one option and save space.")
def _():
    city = st.selectbox("Choose a city", ["Kolhapur", "Pune", "Mumbai"])
    st.write("City selected:", city)


@demo("st.multiselect()", "Like selectbox, but the user can pick several options.")
def _():
    langs = st.multiselect("Pick languages", ["Python", "JS", "Go", "Rust"])
    st.write("Selected:", langs)


@demo("st.slider()", "Lets the user drag to pick a number in a range.")
def _():
    num = st.slider("Pick a number", 0, 100, 50)
    st.write("Value:", num)


@demo("st.text_input()", "A single-line box for typing short text.")
def _():
    name = st.text_input("Enter your name")
    st.write("Hello,", name if name else "stranger")


@demo("st.text_area()", "A multi-line box for typing longer text.")
def _():
    msg = st.text_area("Write a message")
    st.write("You wrote:", msg)


@demo("st.number_input()", "A box for entering a number, with up/down arrows.")
def _():
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    st.write("Age:", age)


@demo("st.date_input()", "Lets the user pick a date from a calendar.")
def _():
    date = st.date_input("Pick a date")
    st.write("Date chosen:", date)
