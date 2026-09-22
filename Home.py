import streamlit as st

st.set_page_config(page_title="Streamlit Learning Lab", page_icon="📚", layout="wide")

st.title("📚 Streamlit Learning Lab")
st.write(
    "A hands-on reference for learning Streamlit. Every page in the sidebar "
    "covers one topic. Inside each page, every function follows the same "
    "three-part pattern:"
)

st.markdown(
    """
    1. **Title** — the name of the function
    2. **Code** — the exact code that produces the result
    3. **Output** — the live result, rendered right below the code
    """
)

st.info("👈 Pick a topic from the sidebar to get started.")

st.divider()
st.subheader("Topics covered")

topics = [
    "✍️ Text & Markdown", "🔘 Input Widgets", "📐 Layouts", "📊 Data Display",
    "📈 Charts", "📁 File Handling", "🎨 UI & Styling", "💬 Status & Messages",
    "🧠 Session State", "📝 Forms", "⚡ Caching", "💬 Chat Elements",
    "🔄 Navigation", "🔐 Authentication",]

cols = st.columns(3)
for i, topic in enumerate(topics):
    cols[i % 3].write(f"- {topic}")
