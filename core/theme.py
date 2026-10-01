import streamlit as st

_CSS = """
<style>
.hero {
    padding: 2rem 1.5rem;
    border-radius: 16px;
    background: linear-gradient(135deg, #FF4B4B22, #7B61FF22);
    border: 1px solid #ffffff22;
    margin-bottom: 1rem;
}
.hero h1 { margin: 0 0 .4rem 0; }
.hero p  { margin: 0; opacity: .85; font-size: 1.05rem; }
</style>
"""


def apply_theme() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)