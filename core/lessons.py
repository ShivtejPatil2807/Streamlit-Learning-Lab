"""Single source of truth for every lesson in the Learning Lab."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Lesson:
    number: int
    title: str
    icon: str
    file: str
    category: str
    level: str
    summary: str
    functions: tuple[str, ...]

    @property
    def path(self) -> str:
        return f"pages/{self.file}"


CATEGORIES = [
    "Display & Content",
    "Input & Layout",
    "Data & Charts",
    "State & Performance",
    "App Features",
]
LEVELS = ["Beginner", "Intermediate", "Advanced"]

LESSONS: list[Lesson] = [
    Lesson(1, "Text & Markdown", "✍️", "01_Text_and_Markdown.py", "Display & Content", "Beginner",
           "Show titles, text, code and math on the page.",
           ("st.title", "st.header", "st.write", "st.markdown", "st.code", "st.latex")),
    Lesson(2, "Input Widgets", "🔘", "02_Input_Widgets.py", "Input & Layout", "Beginner",
           "Collect input with buttons, sliders, text boxes and selectors.",
           ("st.button", "st.slider", "st.text_input", "st.selectbox", "st.checkbox", "st.radio")),
    Lesson(3, "Layouts", "📐", "03_Layouts.py", "Input & Layout", "Beginner",
           "Arrange content with columns, tabs, expanders and containers.",
           ("st.columns", "st.tabs", "st.expander", "st.container", "st.sidebar")),
    Lesson(4, "Data Display", "📊", "04_Data_Display.py", "Data & Charts", "Beginner",
           "Present tables, metrics and JSON.",
           ("st.dataframe", "st.table", "st.metric", "st.json", "st.data_editor")),
    Lesson(5, "Charts", "📈", "05_Charts.py", "Data & Charts", "Intermediate",
           "Plot data with built-in and third-party charts.",
           ("st.line_chart", "st.bar_chart", "st.area_chart", "st.map", "st.pyplot", "st.plotly_chart")),
    Lesson(6, "File Handling", "📁", "06_File_Handling.py", "Data & Charts", "Intermediate",
           "Upload, read and download files.",
           ("st.file_uploader", "st.download_button", "st.camera_input")),
    Lesson(7, "UI & Styling", "🎨", "07_UI_and_Styling.py", "Display & Content", "Intermediate",
           "Customize the look with themes, CSS and HTML.",
           ("st.set_page_config", "st.markdown(unsafe_allow_html)", "st.divider", "st.image")),
    Lesson(8, "Status & Messages", "💬", "08_Status_and_Messages.py", "Display & Content", "Beginner",
           "Give users feedback with alerts, spinners and progress.",
           ("st.success", "st.info", "st.warning", "st.error", "st.spinner", "st.progress", "st.toast")),
    Lesson(9, "Session State", "🧠", "09_Session_State.py", "State & Performance", "Intermediate",
           "Remember values between reruns.",
           ("st.session_state", "callbacks", "key=")),
    Lesson(10, "Forms", "📝", "10_Forms.py", "Input & Layout", "Intermediate",
           "Group inputs and submit them together.",
           ("st.form", "st.form_submit_button")),
    Lesson(11, "Caching", "⚡", "11_Caching.py", "State & Performance", "Advanced",
           "Speed up apps by caching data and resources.",
           ("st.cache_data", "st.cache_resource")),
    Lesson(12, "Chat Elements", "💬", "12_Chat_Elements.py", "App Features", "Intermediate",
           "Build chat interfaces.",
           ("st.chat_message", "st.chat_input", "st.write_stream")),
    Lesson(13, "Navigation", "🔄", "13_Navigation.py", "App Features", "Advanced",
           "Control pages and links.",
           ("st.page_link", "st.switch_page", "st.navigation", "st.Page")),
    Lesson(14, "Authentication", "🔐", "14_Authentication.py", "App Features", "Advanced",
           "Handle logins and protect content.",
           ("st.login", "st.user", "st.logout", "st.secrets")),
]


def total_functions() -> int:
    return sum(len(lesson.functions) for lesson in LESSONS)