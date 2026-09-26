import streamlit as st

st.set_page_config(page_title="File Handling", page_icon="📁")

st.title("📁 File Handling Functions")
st.write("These functions let users upload files, or let you show/offer files.")

st.divider()
st.header("1. st.file_uploader()")
st.write("Lets the user upload a file from their device.")
st.code('st.file_uploader("Upload a CSV file", type="csv")')
uploaded = st.file_uploader("Upload a CSV file", type="csv")
if uploaded:
    st.write("File name:", uploaded.name)

st.divider()
st.header("2. st.download_button()")
st.write("Lets the user download a file you generate.")
st.write("Or fetch the file's content from a URL instead of a local path:")
file_url = "https://github.com/streamlit/streamlit"
url_data = requests.get(file_url).content
 
st.code(
    'file_url = "https://github.com/streamlit/streamlit"\n'
    'url_data = requests.get(file_url).content\n\n'
    'st.download_button("Download from URL", data=url_data, file_name="README.md")'
)
st.download_button("Download from URL", data=url_data, file_name="README.md")

st.divider()
st.header("3. st.image()")
st.write("Displays an image from a file, URL, or array.")
st.code('st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqxQHsJ5GXalp3VMSKLn4LIYdt5mO_8GF9RymX4I-yF_GGESoVS29rYXM&s=10", caption="Sample image")')
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqxQHsJ5GXalp3VMSKLn4LIYdt5mO_8GF9RymX4I-yF_GGESoVS29rYXM&s=10", caption="Sample image")

st.divider()
st.header("4. st.audio()")
st.write("Embeds an audio player for a sound file or URL.")
st.code('st.audio(audio_bytes_or_path)')
st.caption("Provide a local file path, URL, or bytes to try this one — no sample here.")

st.divider()
st.header("5. st.video()")
st.write("Embeds a video player for a video file or URL.")
st.code('st.video("https://youtu.be/RjiqbTLW9_E?si=MrzlHQytg_ww6Hkf")')
st.video('https://youtu.be/RjiqbTLW9_E?si=MrzlHQytg_ww6Hkf')
