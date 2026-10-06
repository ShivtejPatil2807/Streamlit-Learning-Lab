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

    15: [
        Challenge(
            "Which function turns a function into a pop-up window on top of the page?",
            ("st.popup()", "st.modal_window()", "st.dialog()", "st.overlay()"),
            2,
            "@st.dialog turns a function into a pop-up. Call the function to open it.",
        ),
        Challenge(
            "Which function shows the progress of a longer task with a label and a state?",
            ("st.status()", "st.progress_text()", "st.popover()", "st.toast()"),
            0,
            "st.status() shows a task as it runs, and can be updated to \"complete\" when done.",
        ),
    ],
    16: [
        Challenge(
            "What does st.data_editor() return?",
            ("True when the table is edited", "The edited data, as a DataFrame",
             "Only the rows that changed", "Nothing"),
            1,
            "It returns the table with the user's edits, in the same type you passed in.",
        ),
        Challenge(
            "What does st.feedback(\"stars\") return when the user clicks the third star?",
            ("3", "2", "\"3 stars\"", "True"),
            1,
            "It counts from zero: one star is 0 and five stars is 4. Add 1 to show the rating.",
        ),
    ],
    17: [
        Challenge(
            "What does st.fragment let you do?",
            ("Cache a function forever", "Split a page into several files",
             "Rerun just one part of the page", "Delete session state"),
            2,
            "A fragment reruns on its own, so the rest of the script does not run again.",
        ),
        Challenge(
            "What can you give st.write_stream()?",
            ("A generator that yields pieces of text", "A single finished string only",
             "A DataFrame only", "A file path"),
            0,
            "It writes whatever a generator yields piece by piece, like a chatbot typing.",
        ),
    ],

    18: [
        Challenge(
            "Where should a real API key live?",
            ("Directly in your Python code", "In .streamlit/secrets.toml, kept out of Git",
             "In the README so it is easy to find", "In a code comment"),
            1,
            "st.secrets reads it from secrets.toml, which belongs in .gitignore. "
            "On Community Cloud you paste its contents into the app's Secrets settings.",
        ),
        Challenge(
            "Which file tells Community Cloud which Python packages to install?",
            ("README.md", ".gitignore", "requirements.txt", "Home.py"),
            2,
            "The cloud starts with nothing installed, so list every package in requirements.txt.",
        ),
    ],
    19: [
        Challenge(
            "What does a failing assert do?",
            ("Prints a warning and carries on", "Raises an AssertionError",
             "Restarts the app", "Nothing"),
            1,
            "A failed assert raises an AssertionError, which is how test tools notice a failure.",
        ),
        Challenge(
            "What is AppTest for?",
            ("Checking what an app shows without opening a browser", "Making the app load faster",
             "Deploying the app", "Styling the app"),
            0,
            "AppTest runs your app in memory so a test can click, type and read the result.",
        ),
    ],
}
