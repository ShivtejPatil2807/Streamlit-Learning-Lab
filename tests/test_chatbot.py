"""Tests for specs/011-chatbot.md (the chatbot project page)."""
from conftest import PAGES_DIR
from streamlit.testing.v1 import AppTest

from core.export import build_script
from core.lessons import LESSONS

FILE = "22_Project_Chatbot.py"
PAGE = PAGES_DIR / FILE
GREETING = "Hi! Ask me how to do something in Streamlit."
UNKNOWN = "I do not know that one yet."


def run_page() -> AppTest:
    at = AppTest.from_file(str(PAGE), default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    return at


def ask(at: AppTest, question: str) -> AppTest:
    at.chat_input[0].set_value(question).run()
    assert not at.exception, at.exception
    return at


def bubbles(at: AppTest) -> list[tuple[str, str]]:
    """(role, text) for every chat message on the page."""
    return [(message.name, message.markdown[0].value) for message in at.chat_message]


def test_r1_project_is_listed_in_the_projects_category():
    lesson = next(item for item in LESSONS if item.file == FILE)
    assert lesson.category == "Projects"


def test_r2_page_has_the_idea_three_steps_and_the_real_model_part():
    at = run_page()
    assert [h.value for h in at.header] == [
        "1. The idea",
        "2. What the bot knows",
        "3. Find the answer",
        "4. Remember the conversation",
        "5. Using a real language model",
    ]
    assert [tab.label for tab in at.tabs] == ["📖 Learn", "💻 Code", "▶️ Try"] * 3


def test_r3_the_bot_lists_what_it_knows():
    rules = [m.value for m in run_page().markdown if "→" in m.value]
    assert len(rules) >= 10
    assert any("chart" in rule and "st.line_chart()" in rule for rule in rules)


def test_r4_find_the_answer_step():
    at = run_page()
    assert any("st.line_chart()" in m.value for m in at.markdown)  # the starting question

    at.text_input[0].set_value("how do i cache a slow function?").run()
    assert any("@st.cache_data" in m.value for m in at.markdown)

    at.text_input[0].set_value("What is the weather today?").run()
    assert any(m.value == UNKNOWN for m in at.markdown)


def test_r5_chat_starts_with_one_greeting():
    assert bubbles(run_page()) == [("assistant", GREETING)]


def test_r6_asking_a_question_adds_the_question_and_the_answer():
    at = ask(run_page(), "How do I remember values between reruns?")
    chat = bubbles(at)
    assert [role for role, _ in chat] == ["assistant", "user", "assistant"]
    assert chat[1][1] == "How do I remember values between reruns?"
    assert "st.session_state" in chat[2][1]


def test_r7_conversation_is_remembered_after_a_rerun():
    at = ask(run_page(), "How do I remember values between reruns?")
    before = bubbles(at)
    at.run()
    assert not at.exception, at.exception
    assert bubbles(at) == before


def test_r8_unknown_question_gets_the_do_not_know_answer():
    chat = bubbles(ask(run_page(), "What is the weather?"))
    assert chat[-1] == ("assistant", UNKNOWN)


def test_r9_download_keeps_the_knowledge_and_adds_no_package():
    script = build_script(22)
    compile(script, FILE, "exec")
    assert "pip install streamlit\n" in script
    assert "def make_answers():" in script
    assert "@show_setup" not in script
    assert "anthropic.Anthropic" in script  # shown as text only
