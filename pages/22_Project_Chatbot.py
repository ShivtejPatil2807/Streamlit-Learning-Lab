import time

import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section, show_setup

lesson_page(
    22,
    "Build a chatbot that remembers the conversation. It answers with simple rules, "
    "so it needs no paid AI model.",
)


@show_setup
def make_answers():
    return [
        (("hello", "hey"), "Hi! Ask me how to do something in Streamlit, for example how to draw a chart."),
        (("chart", "plot", "graph"), "Use st.line_chart(), st.bar_chart() or st.area_chart() with a table of numbers. See lesson 5."),
        (("button", "click"), "st.button() returns True on the run right after it is clicked. See lesson 2."),
        (("remember", "state", "session"), "st.session_state keeps values between reruns. See lesson 9."),
        (("cache", "slow", "fast"), "Wrap slow functions with @st.cache_data or @st.cache_resource. See lesson 11."),
        (("column", "layout", "side"), "st.columns() puts things side by side. st.tabs() and st.sidebar organise a page. See lesson 3."),
        (("upload", "download", "file"), "st.file_uploader() takes a file in and st.download_button() gives one out. See lesson 6."),
        (("form", "submit"), "st.form() groups widgets so the app reruns only when you submit. See lesson 10."),
        (("login", "password", "auth"), "Keep a logged_in flag in session state, or use st.login(). See lesson 14."),
        (("secret", "key"), "Keep keys in st.secrets, never in your code. See lesson 18."),
        (("deploy", "online", "share"), "Push to GitHub and deploy on Streamlit Community Cloud. See lesson 18."),
        (("test",), "Use pytest and Streamlit's AppTest to check your app automatically. See lesson 19."),
        (("chat", "bot"), "That is what you are using right now! See lessons 12 and 17, and this project."),
    ]


answers = make_answers()

section(
    "The idea",
    "A chatbot is a loop: the user sends a message, the bot replies, and the page remembers "
    "the conversation. This bot has no AI model. It splits your question into words and looks "
    "for a keyword it knows. That keeps the project free and safe to run for everyone, and the "
    "last part shows how to swap in a real language model.",
)


@demo(
    "What the bot knows",
    "The bot's knowledge is a list of keywords, each with an answer.",
)
def _():
    for keywords, answer in answers:
        st.write(f"**{', '.join(keywords)}** → {answer}")


@demo(
    "Find the answer",
    "Split the question into words, then return the first answer that has a matching keyword. "
    "rstrip(\"s\") turns \"charts\" into \"chart\", so plurals work too.",
)
def _():
    question = st.text_input("Ask me about Streamlit", value="How do I make a chart?")
    words = {word.strip("?.,!").rstrip("s") for word in question.lower().split()}

    for keywords, answer in answers:
        if words & set(keywords):
            st.write(answer)
            break
    else:
        st.write("I do not know that one yet.")


@demo(
    "Remember the conversation",
    "st.chat_input() takes the message, st.chat_message() draws the bubbles, and "
    "st.session_state remembers every message. st.write_stream() makes the reply appear word by word.",
)
def _():
    def reply(question):
        words = {word.strip("?.,!").rstrip("s") for word in question.lower().split()}
        for keywords, answer in answers:
            if words & set(keywords):
                return answer
        return "I do not know that one yet."

    def typing(text):
        for word in text.split():
            yield word + " "
            time.sleep(0.03)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! Ask me how to do something in Streamlit."}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if question := st.chat_input("Ask about Streamlit"):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        answer = reply(question)
        with st.chat_message("assistant"):
            st.write_stream(typing(answer))
        st.session_state.messages.append({"role": "assistant", "content": answer})


section(
    "Using a real language model",
    "To get free-form answers, replace reply() with a call to a language model API. "
    "The code below shows the shape of it. It is not run here, because a public app must never "
    "contain your key: every visitor would spend your credit.",
)
st.code(
    """import anthropic

client = anthropic.Anthropic(api_key=st.secrets["API_KEY"])  # the key lives in secrets.toml

response = client.messages.create(
    model="MODEL_NAME",  # pick a model from the provider's documentation
    max_tokens=500,
    messages=[{"role": "user", "content": question}],
)
answer = response.content[0].text""",
    language="python",
)
st.caption(
    "Keep the key in st.secrets (lesson 18). For a public app, let each visitor paste their "
    "own key instead of using yours."
)


lesson_footer(22)
