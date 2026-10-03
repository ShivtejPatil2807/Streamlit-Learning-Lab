import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section

lesson_page(13, "These functions move users between pages in a multipage app.")


@demo("st.page_link()", "Displays a clickable link to another page in your app.")
def _():
    st.page_link("Home.py", label="Go to Home", icon="🏠")


@demo(
    "st.switch_page()",
    "Jumps the user straight to another page in code (e.g. after a button click).",
)
def _():
    if st.button("Jump to Home"):
        st.switch_page("Home.py")


section(
    "How multipage apps work",
    "Any .py file placed in a folder named pages/, next to your main script, "
    "automatically shows up as its own page in the sidebar, with no extra setup. "
    "Streamlit orders them by filename, so this repo uses numbered prefixes like "
    "01_Text_and_Markdown.py, 02_Input_Widgets.py, and so on.",
)
st.code("your-app/\n├── Home.py\n└── pages/\n    ├── 01_Text_and_Markdown.py\n    └── 02_Input_Widgets.py")


lesson_footer(13)
