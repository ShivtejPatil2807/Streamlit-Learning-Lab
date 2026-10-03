import numpy as np
import pandas as pd
import streamlit as st

from core.components import demo, lesson_footer, lesson_page, show_setup

lesson_page(5, "Streamlit has built-in chart functions that need no extra setup.")


@show_setup
def make_chart_data():
    return pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])


chart_data = make_chart_data()


@demo("st.line_chart()", "Draws a line chart from a table of numbers.")
def _():
    st.line_chart(chart_data)


@demo("st.bar_chart()", "Draws a bar chart from a table of numbers.")
def _():
    st.bar_chart(chart_data)


@demo("st.area_chart()", "Draws a filled area chart from a table of numbers.")
def _():
    st.area_chart(chart_data)


@demo("st.scatter_chart()", "Draws a scatter plot from a table of numbers.")
def _():
    st.scatter_chart(chart_data)


@demo("st.map()", "Plots points on a map, given latitude and longitude columns.")
def _():
    map_data = pd.DataFrame({
        "lat": [16.7050, 18.5204],
        "lon": [74.2433, 73.8567],
    })
    st.map(map_data)


lesson_footer(5)
