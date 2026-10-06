# 009: Iris classifier project

**Files:** `pages/20_Project_Iris_Classifier.py`, `core/lessons.py`, `core/export.py`
**Status:** Implemented

## Purpose
The first mini project: a small machine-learning app that brings the lessons
together. A learner trains a model on the iris flowers, then moves four sliders
to see which species the model predicts.

## Requirements
- **R1** The project is listed in the registry in the category "Projects".
- **R2** The page has four numbered parts: the idea, then three steps (look at
  the data, train and test a model, the classifier app). Each step has the
  Learn, Code and Try tabs.
- **R3** The data step names the three species: setosa, versicolor, virginica.
- **R4** The training step shows the accuracy on flowers the model has not seen,
  and it is at least 90%.
- **R5** With the sliders at their starting values (a typical setosa), the app
  predicts Setosa.
- **R6** Typical versicolor measurements predict Versicolor, and typical
  virginica measurements predict Virginica.
- **R7** The prediction shows how sure the model is, as a percentage.
- **R8** Every step is self-contained: its code includes its own imports. The
  downloaded script runs on its own, and its `pip install` line lists
  `scikit-learn` (not `sklearn`).

## Notes
- The model trains in a few milliseconds, so there is no saved model file.
  The classifier app trains once with `st.cache_resource`.
- Requires `scikit-learn` in `requirements.txt`.
