import streamlit as st

from core.components import demo, lesson_footer, lesson_page, section

lesson_page(
    20,
    "Train a small machine-learning model, then use sliders to predict the species of an iris flower.",
)

section(
    "The idea",
    "The iris dataset holds 150 flowers from three species. Each flower has four measurements: "
    "sepal length, sepal width, petal length and petal width, in centimetres. A classifier learns "
    "how the measurements point to the species, then names the species of a flower it has never "
    "seen. Each step below runs on its own, so you can copy any of them.",
)


@demo(
    "Look at the data",
    "scikit-learn ships with the iris data. load_iris(as_frame=True) gives it as a pandas table.",
)
def _():
    from sklearn.datasets import load_iris

    iris = load_iris(as_frame=True)
    st.dataframe(iris.frame.head(8))
    st.write(f"Species 0, 1 and 2 are: {', '.join(iris.target_names)}.")


@demo(
    "Train and test a model",
    "Keep 30% of the flowers hidden while the model learns, then score it on them. "
    "That shows how well it does on flowers it has never seen.",
)
def _():
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split

    iris = load_iris(as_frame=True)
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=0
    )
    model = LogisticRegression(max_iter=200).fit(x_train, y_train)

    st.metric("Accuracy on unseen flowers", f"{model.score(x_test, y_test):.0%}")


@demo(
    "The classifier app",
    "Train once with st.cache_resource, then predict from four sliders. "
    "predict_proba gives the model's chance for each species.",
    caption="Setosa has the smallest petals and virginica the largest. Move the sliders to see it.",
)
def _():
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression

    @st.cache_resource
    def train():
        iris = load_iris()
        model = LogisticRegression(max_iter=200).fit(iris.data, iris.target)
        return model, list(iris.target_names)

    model, names = train()

    left, right = st.columns(2)
    sepal_length = left.slider("Sepal length (cm)", 4.0, 8.0, 5.0, 0.1)
    sepal_width = left.slider("Sepal width (cm)", 2.0, 4.5, 3.4, 0.1)
    petal_length = right.slider("Petal length (cm)", 1.0, 7.0, 1.5, 0.1)
    petal_width = right.slider("Petal width (cm)", 0.1, 2.5, 0.2, 0.1)

    flower = [[sepal_length, sepal_width, petal_length, petal_width]]
    chances = model.predict_proba(flower)[0]
    best = chances.argmax()

    st.metric(
        "Predicted species",
        names[best].capitalize(),
        f"{chances[best]:.0%} sure",
        delta_color="off",
    )
    st.bar_chart(pd.DataFrame({"chance": chances}, index=names))


lesson_footer(20)
