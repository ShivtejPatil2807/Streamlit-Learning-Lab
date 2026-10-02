import numpy as np
import pandas as pd
import streamlit as st

from core.components import demo, lesson_page

lesson_page(6, "These functions let users upload files, or let you show and offer files.")


@demo("st.file_uploader()", "Lets the user upload a file from their device.")
def _():
    uploaded = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded:
        st.write("File name:", uploaded.name)


@demo("st.download_button()", "Lets the user download a file that your app generates.")
def _():
    marks = pd.DataFrame({"Name": ["Shivtej", "Tejas"], "Marks": [70, 90]})
    st.download_button(
        "Download as CSV",
        data=marks.to_csv(index=False),
        file_name="marks.csv",
        mime="text/csv",
    )


@demo("st.image()", "Displays an image from a file, URL, or array.")
def _():
    pixels = np.random.rand(120, 240, 3)  # height x width x RGB
    st.image(pixels, caption="Random pixels from a NumPy array")


@demo("st.audio()", "Embeds an audio player for a sound file, URL, or array.")
def _():
    sample_rate = 44100
    t = np.linspace(0, 1, sample_rate)
    tone = 0.3 * np.sin(2 * np.pi * 440 * t)  # one second of the note A
    st.audio(tone, sample_rate=sample_rate)


@demo("st.video()", "Embeds a video player for a video file or URL.")
def _():
    st.video("https://youtu.be/RjiqbTLW9_E?si=MrzlHQytg_ww6Hkf")
