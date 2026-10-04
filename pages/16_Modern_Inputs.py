import pandas as pd
import streamlit as st

from core.components import demo, lesson_footer, lesson_page

lesson_page(16, "Newer input widgets: clickable pills, star ratings and tables you can edit.")


@demo(
    "st.pills()",
    "A row of clickable pill buttons. Pick one, or several with selection_mode=\"multi\".",
)
def _():
    topic = st.pills("Favorite topic", ["Layouts", "Forms", "Caching"])
    st.write("You picked:", topic or "nothing yet")


@demo(
    "st.feedback()",
    "A thumbs or star rating. It returns the choice as a number, or None if nothing is picked.",
)
def _():
    stars = st.feedback("stars")
    if stars is not None:
        st.write(f"You rated this {stars + 1} out of 5 stars.")


@demo(
    "st.data_editor()",
    "A table the user can edit. It returns the edited data as a DataFrame.",
)
def _():
    tasks = pd.DataFrame({"Task": ["Write code", "Run tests"], "Done": [True, False]})
    edited = st.data_editor(tasks)
    st.write("Tasks done:", int(edited["Done"].sum()))


lesson_footer(16)
