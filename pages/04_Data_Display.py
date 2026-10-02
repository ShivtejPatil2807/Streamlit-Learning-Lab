import pandas as pd
import streamlit as st

from core.components import demo, lesson_page, show_setup

lesson_page(4, "These functions show data: tables, numbers, and raw structures.")


@show_setup
def make_df():
    return pd.DataFrame({
        "Name": ["Shivtej", "Tejas", "Amit"],
        "Score": [70, 85, 78],
    })


df = make_df()


@demo("st.dataframe()", "Displays an interactive table, sortable and scrollable.")
def _():
    st.dataframe(df)


@demo("st.table()", "Displays a static (non-interactive) table.")
def _():
    st.table(df)


@demo("st.metric()", "Shows a single number, with an optional change indicator.")
def _():
    st.metric("Average Score", "84.3", "+2.1")


@demo("st.json()", "Displays a dictionary or JSON-like data in a readable, collapsible format.")
def _():
    st.json({"name": "Shivtej", "skills": ["Python", "Streamlit"]})
