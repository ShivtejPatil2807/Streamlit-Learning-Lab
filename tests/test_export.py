"""Tests for specs/007-lesson-download.md (core/export.py and the download button)."""
import ast
import re
from textwrap import dedent

from conftest import PAGES_DIR
from streamlit.testing.v1 import AppTest

from core.export import build_script
from core.lessons import LESSONS

HELPERS = {"lesson_page", "demo", "section", "show_setup", "lesson_footer"}


def page_demo_count(lesson) -> int:
    """How many demos and sections the page itself defines."""
    tree = ast.parse((PAGES_DIR / lesson.file).read_text(encoding="utf-8"))
    count = 0
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                target = decorator.func if isinstance(decorator, ast.Call) else decorator
                if getattr(target, "id", None) == "demo":
                    count += 1
        elif (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and getattr(node.value.func, "id", None) == "section"
        ):
            count += 1
    return count


def test_r1_every_lesson_script_is_valid_python():
    for lesson in LESSONS:
        compile(build_script(lesson.number), lesson.file, "exec")


def test_r2_scripts_use_no_project_helpers():
    for lesson in LESSONS:
        tree = ast.parse(build_script(lesson.number))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                assert (node.module or "").split(".")[0] != "core", lesson.file
            if isinstance(node, ast.Import):
                assert all(a.name.split(".")[0] != "core" for a in node.names), lesson.file
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                assert node.func.id not in HELPERS, f"{lesson.file} calls {node.func.id}"
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    target = decorator.func if isinstance(decorator, ast.Call) else decorator
                    assert getattr(target, "id", None) not in HELPERS, lesson.file


def test_r3_first_streamlit_call_is_set_page_config():
    for lesson in LESSONS:
        tree = ast.parse(build_script(lesson.number))
        first = next(
            node.value
            for node in tree.body
            if isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Attribute)
            and getattr(node.value.func.value, "id", None) == "st"
        )
        assert first.func.attr == "set_page_config", lesson.file


def test_r4_numbered_headings_count_up_from_one():
    for lesson in LESSONS:
        tree = ast.parse(build_script(lesson.number))
        numbers = []
        for node in tree.body:
            if (
                isinstance(node, ast.Expr)
                and isinstance(node.value, ast.Call)
                and getattr(node.value.func, "attr", None) == "header"
                and node.value.args
                and isinstance(node.value.args[0], ast.Constant)
            ):
                match = re.match(r"^(\d+)\. ", node.value.args[0].value)
                if match:
                    numbers.append(int(match.group(1)))
        assert numbers == list(range(1, page_demo_count(lesson) + 1)), lesson.file


def test_r5_demo_code_and_comments_are_copied_from_the_page():
    caching = build_script(11)
    assert "@st.cache_data" in caching
    assert "# pretend this is slow" in caching
    charts = build_script(5)
    assert "def make_chart_data():" in charts
    assert "@show_setup" not in charts
    assert "chart_data = make_chart_data()" in charts
    assert 'st.title("My Streamlit App")' in build_script(1)


def test_r6_docstring_says_how_to_run_and_what_to_install():
    assert "pip install streamlit\n" in build_script(1)
    assert "pip install streamlit numpy pandas\n" in build_script(5)
    for lesson in LESSONS:
        assert f"streamlit run {lesson.file}" in build_script(lesson.number)


def test_r7_demos_that_cannot_run_alone_are_commented_out():
    navigation = build_script(13)
    assert '# st.page_link("Home.py"' in navigation
    assert "multipage app" in navigation
    auth = build_script(14)
    assert '# if st.button("Log in with provider"):' in auth
    assert "#     st.login()" in auth


def test_r8_every_lesson_page_has_a_download_button(tmp_path):
    for lesson in LESSONS:
        page = tmp_path / f"footer_{lesson.number}.py"
        page.write_text(
            dedent(
                f"""
                from core.components import lesson_footer, lesson_page

                lesson_page({lesson.number})
                lesson_footer({lesson.number})
                """
            ),
            encoding="utf-8",
        )
        at = AppTest.from_file(str(page), default_timeout=30)
        at.run()
        assert not at.exception, at.exception
        assert len(at.get("download_button")) == 1, lesson.file
