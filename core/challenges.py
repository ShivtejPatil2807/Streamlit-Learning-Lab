"""Short multiple-choice questions shown at the bottom of each lesson."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Challenge:
    question: str
    options: tuple[str, ...]
    answer: int  # index into options
    explanation: str


CHALLENGES: dict[int, list[Challenge]] = {
    1: [
        Challenge(
            "Which function draws a horizontal line between sections?",
            ("st.line()", "st.divider()", "st.hr()", "st.separator()"),
            1,
            "st.divider() draws the horizontal line.",
        ),
    ],
    2: [
        Challenge(
            "What does st.button() return on the rerun right after it is clicked?",
            ("False", "None", "The button label", "True"),
            3,
            "It returns True for that one run, then goes back to False.",
        ),
    ],
    3: [
        Challenge(
            "Which function splits the page into side-by-side sections?",
            ("st.tabs()", "st.columns()", "st.container()", "st.sidebar"),
            1,
            "st.columns() gives you side-by-side sections.",
        ),
    ],
    4: [
        Challenge(
            "Which function shows an interactive table you can sort and scroll?",
            ("st.table()", "st.json()", "st.dataframe()", "st.metric()"),
            2,
            "st.dataframe() is interactive. st.table() is static.",
        ),
    ],
    5: [
        Challenge(
            "Which two columns does st.map() look for in your data?",
            ("x and y", "city and country", "name and value", "lat and lon"),
            3,
            "st.map() plots points from latitude and longitude columns.",
        ),
    ],
    6: [
        Challenge(
            "Which function lets the user save a file that your app generates?",
            ("st.download_button()", "st.file_uploader()", "st.image()", "st.save()"),
            0,
            "st.download_button() offers a file for download. st.file_uploader() is the reverse.",
        ),
    ],
    7: [
        Challenge(
            "Which st.markdown() argument allows raw HTML and CSS?",
            ("html=True", "allow_css=True", "unsafe_allow_html=True", "raw=True"),
            2,
            "unsafe_allow_html=True turns on raw HTML. Only use it with content you trust.",
        ),
    ],
    8: [
        Challenge(
            "Which function shows a small, temporary notification in the corner?",
            ("st.success()", "st.progress()", "st.balloons()", "st.toast()"),
            3,
            "st.toast() shows a short-lived message in the corner of the screen.",
        ),
    ],
    9: [
        Challenge(
            "What happens to ordinary Python variables on every rerun?",
            ("They keep their value", "They are reset", "They are saved to disk",
             "They move into session state"),
            1,
            "The whole script runs again, so plain variables start fresh. "
            "Use st.session_state to remember things.",
        ),
        Challenge(
            "Where is the value of a widget with key='username' stored?",
            ("st.session_state['username']", "st.cache_data", "A file named username",
             "Nowhere, it is lost"),
            0,
            "Every widget with a key stores its value in st.session_state under that key.",
        ),
    ],
    10: [
        Challenge(
            "When does an st.form() rerun the app?",
            ("After every keystroke", "Only when the submit button is pressed",
             "Every second", "Never"),
            1,
            "Widgets inside a form wait until the submit button is pressed.",
        ),
    ],
    11: [
        Challenge(
            "Which decorator suits a shared ML model or database connection?",
            ("st.cache_data", "st.session_state", "st.cache_resource", "st.form"),
            2,
            "st.cache_resource returns the same shared object every time.",
        ),
        Challenge(
            "Which argument makes a cache entry expire after a number of seconds?",
            ("expire", "ttl", "timeout", "max_age"),
            1,
            "ttl, for example @st.cache_data(ttl=60), keeps results for 60 seconds.",
        ),
    ],
    12: [
        Challenge(
            "Which function shows a chat bubble for a role such as 'user'?",
            ("st.chat_message()", "st.chat_input()", "st.write_chat()", "st.bubble()"),
            0,
            "st.chat_message() draws the bubble. st.chat_input() is the box you type in.",
        ),
    ],
    13: [
        Challenge(
            "Which function jumps to another page from code, for example after a button click?",
            ("st.page_link()", "st.switch_page()", "st.goto()", "st.redirect()"),
            1,
            "st.switch_page() moves the user. st.page_link() only shows a clickable link.",
        ),
    ],
    14: [
        Challenge(
            "Why is the session-state login on this page not safe for real passwords?",
            ("Session state is deleted too fast",
             "Forms cannot hold passwords",
             "The username and password are written directly in the code",
             "st.error() leaks the password"),
            2,
            "Anyone who can read the code can read the password. "
            "Real apps use an identity provider, for example with st.login().",
        ),
    ],
}
