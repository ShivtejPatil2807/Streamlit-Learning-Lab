import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(12, "These functions are built specifically for chatbot-style interfaces.")


@demo("st.chat_message()", "Displays a chat bubble styled for a given role (user or assistant).")
def _():
    with st.chat_message("user"):
        st.write("Hello!")

    with st.chat_message("assistant"):
        st.write("Hi there, how can I help?")


@demo(
    "st.chat_input()",
    "A text box fixed to the bottom of the page, made for sending chat messages.",
)
def _():
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"You said: {prompt}")


lesson_footer(12)
