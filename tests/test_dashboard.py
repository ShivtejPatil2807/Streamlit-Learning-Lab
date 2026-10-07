"""Tests for specs/010-sales-dashboard.md (the sales dashboard project page)."""
from conftest import PAGES_DIR
from streamlit.testing.v1 import AppTest

from core.export import build_script
from core.lessons import LESSONS

FILE = "21_Project_Sales_Dashboard.py"
PAGE = PAGES_DIR / FILE


def run_page(change=None) -> AppTest:
    at = AppTest.from_file(str(PAGE), default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    if change:
        change(at)
        at.run()
        assert not at.exception, at.exception
    return at


def metrics(at: AppTest) -> dict[str, str]:
    return {metric.label: metric.value for metric in at.metric}


def money(text: str) -> int:
    return int(text.replace("$", "").replace(",", ""))


def test_r1_project_is_listed_in_the_projects_category():
    lesson = next(item for item in LESSONS if item.file == FILE)
    assert lesson.category == "Projects"


def test_r2_page_has_the_idea_and_four_steps_with_three_tabs_each():
    at = run_page()
    assert [h.value for h in at.header] == [
        "1. The idea",
        "2. Look at the data",
        "3. Summarise with groupby",
        "4. Filter with widgets",
        "5. The dashboard",
    ]
    assert [tab.label for tab in at.tabs] == ["📖 Learn", "💻 Code", "▶️ Try"] * 4


def test_r3_data_has_288_rows_and_5_columns():
    at = run_page()
    assert any(m.value == "288 rows and 5 columns" for m in at.markdown)


def test_r4_filter_step_starts_with_north_and_south_and_narrows_down():
    at = run_page()
    assert any(m.value == "144 of 288 rows" for m in at.markdown)

    def choose_east_laptops(app):
        app.multiselect[0].set_value(["East"])
        app.selectbox[0].select("Laptop")

    at = run_page(choose_east_laptops)
    assert any(m.value == "24 of 288 rows" for m in at.markdown)


def test_r5_dashboard_shows_revenue_orders_and_average_order():
    shown = metrics(run_page())
    assert list(shown) == ["Revenue", "Orders", "Average order"]
    expected_average = money(shown["Revenue"]) / money(shown["Orders"])
    assert abs(money(shown["Average order"]) - expected_average) <= 1


def test_r6_narrowing_the_filters_lowers_the_revenue():
    everything = money(metrics(run_page())["Revenue"])
    north = money(metrics(run_page(lambda app: app.multiselect[1].set_value(["North"])))["Revenue"])
    assert 0 < north < everything


def test_r7_nothing_selected_shows_a_warning_instead_of_numbers():
    at = run_page(lambda app: app.multiselect[1].set_value([]))
    assert len(at.metric) == 0
    assert any("Pick at least one region" in warning.value for warning in at.warning)


def test_r8_data_is_the_same_every_time():
    assert metrics(run_page()) == metrics(run_page())


def test_r9_download_keeps_the_data_function_and_lists_numpy_and_pandas():
    script = build_script(21)
    compile(script, FILE, "exec")
    assert "pip install streamlit numpy pandas\n" in script
    assert "def make_sales():" in script
    assert "@show_setup" not in script
