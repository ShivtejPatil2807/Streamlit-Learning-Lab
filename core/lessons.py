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
           "Show titles, text, code and tables on the page.",
           ("st.title", "st.header", "st.subheader", "st.write", "st.markdown",
            "st.caption", "st.code", "st.divider", "st.table", "st.expander")),
    Lesson(2, "Input Widgets", "🔘", "02_Input_Widgets.py", "Input & Layout", "Beginner",
           "Collect input with buttons, sliders, text boxes and selectors.",
           ("st.button", "st.checkbox", "st.radio", "st.selectbox", "st.multiselect",
            "st.slider", "st.text_input", "st.text_area", "st.number_input", "st.date_input")),
    Lesson(3, "Layouts", "📐", "03_Layouts.py", "Input & Layout", "Beginner",
           "Arrange content with columns, tabs, containers and placeholders.",
           ("st.columns", "st.tabs", "st.container", "st.sidebar", "st.empty")),
    Lesson(4, "Data Display", "📊", "04_Data_Display.py", "Data & Charts", "Beginner",
           "Present tables, metrics and JSON.",
           ("st.dataframe", "st.table", "st.metric", "st.json")),
    Lesson(5, "Charts", "📈", "05_Charts.py", "Data & Charts", "Intermediate",
           "Plot data with Streamlit's built-in charts and maps.",
           ("st.line_chart", "st.bar_chart", "st.area_chart", "st.scatter_chart", "st.map")),
    Lesson(6, "File Handling", "📁", "06_File_Handling.py", "Data & Charts", "Intermediate",
           "Upload and download files, and show images, audio and video.",
           ("st.file_uploader", "st.download_button", "st.image", "st.audio", "st.video")),
    Lesson(7, "UI & Styling", "🎨", "07_UI_and_Styling.py", "Display & Content", "Intermediate",
           "Customize the look with page config, colors and CSS.",
           ("st.set_page_config", "st.color_picker", "st.markdown (CSS)", "st.image")),
    Lesson(8, "Status & Messages", "💬", "08_Status_and_Messages.py", "Display & Content", "Beginner",
           "Give users feedback with alerts, spinners and progress.",
           ("st.success", "st.error", "st.warning", "st.info",
            "st.progress", "st.spinner", "st.toast", "st.balloons")),
    Lesson(9, "Session State", "🧠", "09_Session_State.py", "State & Performance", "Intermediate",
           "Remember values between reruns.",
           ("st.session_state", "widget key=")),
    Lesson(10, "Forms", "📝", "10_Forms.py", "Input & Layout", "Intermediate",
           "Group inputs and submit them together.",
           ("st.form", "st.form_submit_button")),
    Lesson(11, "Caching", "⚡", "11_Caching.py", "State & Performance", "Advanced",
           "Speed up apps by caching data and resources.",
           ("st.cache_data", "st.cache_resource", "ttl", "cache.clear()")),
    Lesson(12, "Chat Elements", "🗨️", "12_Chat_Elements.py", "App Features", "Intermediate",
           "Build chat interfaces.",
           ("st.chat_message", "st.chat_input")),
    Lesson(13, "Navigation", "🔄", "13_Navigation.py", "App Features", "Advanced",
           "Link and jump between pages.",
           ("st.page_link", "st.switch_page")),
    Lesson(14, "Authentication", "🔐", "14_Authentication.py", "App Features", "Advanced",
           "Protect content with a simple login, and see real auth.",
           ("session-state login", "st.login", "st.user")),
    Lesson(15, "Dialogs & Pop-ups", "🪟", "15_Dialogs_and_Popups.py", "Display & Content", "Intermediate",
           "Show extra content on top of the page, only when the learner asks for it.",
           ("st.dialog", "st.popover", "st.status")),
    Lesson(16, "Modern Inputs", "🎛️", "16_Modern_Inputs.py", "Input & Layout", "Intermediate",
           "Newer widgets: clickable pills, star ratings and editable tables.",
           ("st.pills", "st.feedback", "st.data_editor")),
    Lesson(17, "Fragments & Streaming", "🌊", "17_Fragments_and_Streaming.py", "State & Performance", "Advanced",
           "Rerun just part of a page, and show text as it is being produced.",
           ("st.fragment", "st.write_stream")),
    Lesson(18, "Secrets & Deployment", "🚀", "18_Secrets_and_Deployment.py", "App Features", "Intermediate",
           "Keep private values out of your code and put your app online.",
           ("st.secrets", "st.__version__", "Community Cloud")),
    Lesson(19, "Testing Your App", "🧪", "19_Testing_Your_App.py", "App Features", "Advanced",
           "Check your app with automatic tests instead of clicking through it.",
           ("assert", "AppTest", "pytest", "GitHub Actions")),
]


def total_functions() -> int:
    return sum(len(lesson.functions) for lesson in LESSONS)


def neighbours(number: int) -> "tuple[Lesson | None, Lesson | None]":
    """The lessons before and after this one (None at either end)."""
    index = next(i for i, lesson in enumerate(LESSONS) if lesson.number == number)
    previous = LESSONS[index - 1] if index > 0 else None
    following = LESSONS[index + 1] if index < len(LESSONS) - 1 else None
    return previous, following
