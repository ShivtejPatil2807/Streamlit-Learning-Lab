import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(1, "This page shows the basic functions Streamlit gives you to display text.")


@demo("st.title()", "Shows the biggest heading, usually used once at the top of the app.")
def _():
    st.title("My Streamlit App")


@demo("st.header()", "Shows a large section heading.")
def _():
    st.header("Student Information")


@demo("st.subheader()", "Shows a heading smaller than st.header(), good for sub-sections.")
def _():
    st.subheader("Personal Details")


@demo("st.write()", "The all-purpose function. Can display text, numbers, lists, and more.")
def _():
    st.write("Hello, Streamlit!")


@demo("st.markdown()", "Displays text with Markdown formatting, like **bold** or *italic*.")
def _():
    st.markdown("**Hello, Streamlit!**")


@demo("st.caption()", "Shows small, gray text, good for notes or extra info.")
def _():
    st.caption("This is additional information.")


@demo("st.code()", "Displays a block of code with syntax highlighting.")
def _():
    st.code('print("Hello, World!")')


@demo("st.divider()", "Draws a horizontal line to separate sections (used all over this page!).")
def _():
    st.divider()


@demo("st.table()", "Displays data in a simple table.")
def _():
    data = {"Name": ["Shivtej", "Tejas"], "Marks": [70, 90]}
    st.table(data)


@demo("st.expander()", "Creates a section that can be opened or closed by the user.")
def _():
    with st.expander("View Explanation"):
        st.write("This content can be expanded.")


lesson_footer(1)
