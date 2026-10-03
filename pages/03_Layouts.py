import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(3, "Layout functions control where things appear on the page.")


@demo("st.columns()", "Splits the page into side-by-side sections.")
def _():
    col1, col2 = st.columns(2)
    col1.write("Left column")
    col2.write("Right column")


@demo("st.tabs()", "Creates clickable tabs to organize content.")
def _():
    tab1, tab2 = st.tabs(["Tab A", "Tab B"])
    with tab1:
        st.write("Content for Tab A")
    with tab2:
        st.write("Content for Tab B")


@demo("st.container()", "Groups elements together so you can add to them later in the code.")
def _():
    box = st.container(border=True)
    box.write("I'm inside a container")


@demo("st.sidebar", "Puts a widget or text in the sidebar instead of the main page.")
def _():
    st.sidebar.write("👋 This came from the Layouts page")


@demo("st.empty()", "Reserves a spot on the page that you can update or replace later.")
def _():
    placeholder = st.empty()
    placeholder.write("Original text")
    placeholder.write("Replaced text")


lesson_footer(3)
