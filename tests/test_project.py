"""Tests for specs/009-iris-classifier.md (the iris classifier project page)."""
from conftest import PAGES_DIR
from streamlit.testing.v1 import AppTest

from core.export import build_script
from core.lessons import LESSONS

FILE = "20_Project_Iris_Classifier.py"
PAGE = PAGES_DIR / FILE

SETOSA = None  # the sliders' starting values
VERSICOLOR = [5.9, 2.8, 4.3, 1.3]  # sepal length, sepal width, petal length, petal width
VIRGINICA = [6.6, 3.0, 5.6, 2.0]


def run_page(slider_values=None) -> AppTest:
    at = AppTest.from_file(str(PAGE), default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    if slider_values:
        for slider, value in zip(at.slider, slider_values):
            slider.set_value(value)
        at.run()
        assert not at.exception, at.exception
    return at


def metrics(at: AppTest) -> dict:
    return {metric.label: metric for metric in at.metric}


def test_r1_project_is_listed_in_the_projects_category():
    lesson = next(item for item in LESSONS if item.file == FILE)
    assert lesson.category == "Projects"


def test_r2_page_has_the_idea_and_three_steps_with_three_tabs_each():
    at = run_page()
    assert [h.value for h in at.header] == [
        "1. The idea",
        "2. Look at the data",
        "3. Train and test a model",
        "4. The classifier app",
    ]
    assert [tab.label for tab in at.tabs] == ["📖 Learn", "💻 Code", "▶️ Try"] * 3


def test_r3_data_step_names_the_three_species():
    at = run_page()
    expected = "Species 0, 1 and 2 are: setosa, versicolor, virginica."
    assert any(m.value == expected for m in at.markdown)


def test_r4_accuracy_on_unseen_flowers_is_at_least_90_percent():
    value = metrics(run_page())["Accuracy on unseen flowers"].value
    assert int(value.rstrip("%")) >= 90


def test_r5_starting_sliders_predict_setosa():
    assert metrics(run_page())["Predicted species"].value == "Setosa"


def test_r6_typical_versicolor_and_virginica_are_recognised():
    assert metrics(run_page(VERSICOLOR))["Predicted species"].value == "Versicolor"
    assert metrics(run_page(VIRGINICA))["Predicted species"].value == "Virginica"


def test_r7_prediction_shows_how_sure_the_model_is():
    delta = metrics(run_page())["Predicted species"].delta
    assert delta.endswith("% sure")


def test_r8_download_is_self_contained_and_lists_scikit_learn():
    script = build_script(20)
    compile(script, FILE, "exec")
    assert "pip install streamlit pandas scikit-learn\n" in script
    assert "sklearn" not in script.split('"""')[1]  # the pip line says scikit-learn
    assert "from sklearn.datasets import load_iris" in script
    assert "from sklearn.linear_model import LogisticRegression" in script
    assert "from sklearn.model_selection import train_test_split" in script
