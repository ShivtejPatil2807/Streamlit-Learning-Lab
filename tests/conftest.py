"""Shared paths and setup for the test suite."""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "pages"
HOME = ROOT / "Home.py"


@pytest.fixture(scope="session", autouse=True)
def warm_up_slow_imports():
    """Import big packages once, before any test, so no page run is timed out.

    AppTest gives every page run a time limit. The very first import of
    scikit-learn can be slow on a fresh install, so it is done here instead.
    """
    import sklearn.datasets
    import sklearn.linear_model
    import sklearn.model_selection  # noqa: F401