"""Turn a lesson page into a script that runs on its own.

The lesson pages use helpers from core/ (lesson_page, demo, section, ...).
A learner who downloads a page could not run it without the whole project, so
this module rewrites a page as plain Streamlit code. The code of every demo is
copied from the page itself, so the download always matches what the lesson
shows.
"""
import ast
import json
import sys
import textwrap
from pathlib import Path

from core.lessons import LESSONS

PAGES_DIR = Path(__file__).resolve().parents[1] / "pages"
REPO_URL = "https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab"

# Some packages are imported under a different name than the one pip installs.
PIP_NAMES = {"sklearn": "scikit-learn", "PIL": "pillow", "cv2": "opencv-python"}


def _lit(text: str) -> str:
    """A Python string literal for `text`."""
    return json.dumps(text, ensure_ascii=False)


def _decorator_name(decorator) -> str | None:
    if isinstance(decorator, ast.Call):
        decorator = decorator.func
    return decorator.id if isinstance(decorator, ast.Name) else None


def _call_name(node: ast.Call) -> str | None:
    return node.func.id if isinstance(node.func, ast.Name) else None


def _start_line(node) -> int:
    """First line of a statement, including its decorators."""
    lines = [node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])]
    return min(lines)


def _comment_out(code: str) -> str:
    return "\n".join(f"# {line}" if line.strip() else "#" for line in code.splitlines())


def _heading(number: int, title: str, description: str | None) -> list[str]:
    out = ["st.divider()", f"st.header({_lit(f'{number}. {title}')})"]
    if description:
        out.append(f"st.write({_lit(description)})")
    return out


def _packages(tree: ast.Module) -> list[str]:
    """Third-party packages the page imports (anywhere), so we can tell the learner what to install."""
    found = {"streamlit"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            names = [node.module.split(".")[0]]
        else:
            continue
        found.update(
            PIP_NAMES.get(name, name)
            for name in names
            if name != "core" and name not in sys.stdlib_module_names
        )
    return ["streamlit"] + sorted(found - {"streamlit"})


def build_script(number: int, pages_dir: Path = PAGES_DIR) -> str:
    """The lesson with this number, as a script that runs with plain `streamlit run`."""
    lesson = next(item for item in LESSONS if item.number == number)
    source = (pages_dir / lesson.file).read_text(encoding="utf-8")
    lines = source.splitlines()
    tree = ast.parse(source)

    def segment(node) -> str:
        return "\n".join(lines[node.lineno - 1 : node.end_lineno])

    imports: list[str] = []
    blocks: list[str] = []
    counter = 0

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module = getattr(node, "module", None) or ""
            if module.split(".")[0] != "core":
                imports.append(segment(node))
            continue

        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            name = _call_name(call)
            if name == "lesson_page":
                intro = lesson.summary
                if len(call.args) > 1:
                    intro = ast.literal_eval(call.args[1])
                config = (
                    f"st.set_page_config(page_title={_lit(lesson.title)}, "
                    f"page_icon={_lit(lesson.icon)})"
                )
                title_line = f"st.title({_lit(f'{lesson.icon} {lesson.title}')})"
                blocks.append("\n".join([config, title_line, f"st.write({_lit(intro)})"]))
                continue
            if name == "lesson_footer":
                continue
            if name == "section":
                counter += 1
                title = ast.literal_eval(call.args[0])
                description = ast.literal_eval(call.args[1]) if len(call.args) > 1 else None
                blocks.append(f"# {counter}. {title}\n" + "\n".join(_heading(counter, title, description)))
                continue

        if isinstance(node, ast.FunctionDef):
            names = [_decorator_name(d) for d in node.decorator_list]

            if "demo" in names:
                counter += 1
                decorator = node.decorator_list[names.index("demo")]
                title = ast.literal_eval(decorator.args[0])
                description = ast.literal_eval(decorator.args[1])
                options = {kw.arg: ast.literal_eval(kw.value) for kw in decorator.keywords}

                first = _start_line(node.body[0])
                body = textwrap.dedent("\n".join(lines[first - 1 : node.end_lineno]))

                parts = [f"# {counter}. {title}", *_heading(counter, title, description), ""]
                if not options.get("run", True):
                    parts.append("# This demo is not run here: it needs extra setup.")
                    body = _comment_out(body)
                elif "Home.py" in body:
                    parts.append(
                        "# This demo needs a multipage app (a pages/ folder), "
                        "so it is commented out here."
                    )
                    body = _comment_out(body)
                parts.append(body)
                if options.get("caption"):
                    parts.append(f"st.caption({_lit(options['caption'])})")
                blocks.append("\n".join(parts))
                continue

            if "show_setup" in names:
                blocks.append("# Sample data used on this page\n" + segment(node))
                continue

        blocks.append(segment(node))

    packages = " ".join(_packages(tree))
    docstring = (
        f'"""{lesson.icon} {lesson.title}: a lesson from the Streamlit Learning Lab.\n\n'
        f"Run it on your own computer:\n\n"
        f"    pip install {packages}\n"
        f"    streamlit run {lesson.file}\n\n"
        f"All lessons: {REPO_URL}\n"
        f'"""'
    )
    return "\n\n".join([docstring, "\n".join(imports), *blocks]) + "\n"
