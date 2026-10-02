import streamlit as st

from core.components import demo, lesson_page, section

lesson_page(7, "These functions change how your app looks and feels.")

section(
    "st.set_page_config()",
    "Sets the browser tab title, icon, and page layout. "
    "Must be the first Streamlit command in a page.",
)
st.code('st.set_page_config(page_title="My App", page_icon="🎨", layout="wide")')
st.caption("Every page here calls it (through lesson_page), which is why the tab shows 🎨 UI & Styling.")


@demo("st.color_picker()", "Lets the user pick a color.")
def _():
    color = st.color_picker("Pick a color", "#1D9E75")
    st.write("You picked:", color)


@demo(
    "Custom CSS with st.markdown()",
    "You can inject raw HTML/CSS using unsafe_allow_html to restyle elements.",
)
def _():
    st.markdown(
        "<p style='color:#1D9E75; font-weight:bold;'>Styled text</p>",
        unsafe_allow_html=True,
    )


@demo(
    "st.image() as a logo/banner",
    "Images aren't just for content. They're often used as logos or banners.",
)
def _():
    st.image("https://placehold.co/400x80", use_container_width=True)
