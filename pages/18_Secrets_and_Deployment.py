import platform

import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section

lesson_page(18, "Keep private values out of your code, and put your app online for everyone.")


@demo(
    "st.__version__",
    "The Streamlit version your app runs on. Your computer and Community Cloud can run "
    "different versions, so print it when something works in one place but not the other.",
)
def _():
    st.write("Streamlit version:", st.__version__)
    st.write("Python version:", platform.python_version())


@demo(
    "st.secrets",
    "A read-only dictionary of private values such as API keys, loaded from a secrets file. "
    "Never print a secret on the page.",
    caption="No secret found? That is normal here. Add one to .streamlit/secrets.toml "
    "to see the green message.",
)
def _():
    try:
        api_key = st.secrets["demo_api_key"]
        st.success(f"Found demo_api_key ({len(api_key)} characters). Its value stays hidden.")
    except (KeyError, FileNotFoundError):
        st.info("No secret called demo_api_key was found.")


section(
    "The secrets.toml file",
    "On your computer, secrets live in .streamlit/secrets.toml. "
    "Add that file to .gitignore so it never reaches GitHub.",
)
st.code('demo_api_key = "paste-your-key-here"', language="toml")
st.caption("On Community Cloud you paste the same text into the app's Secrets settings.")

section(
    "Deploying to Streamlit Community Cloud",
    "Community Cloud hosts public Streamlit apps for free, straight from a GitHub repository.",
)
st.markdown(
    """
1. Push your app to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app**, then pick the repository, the branch and the main file
   (for this project, `Home.py`).
4. Open **Advanced settings** to choose the Python version and paste your secrets.
5. Click **Deploy**. Every push to that branch updates the live app.
"""
)
st.caption(
    "Every package your app imports must be listed in requirements.txt, "
    "because the cloud starts with nothing installed."
)


lesson_footer(18)
