<p align="center">
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="100" alt="Streamlit logo"/>
</p>

<h1 align="center">📚 Streamlit Learning Lab</h1>

<p align="center">
  A hands-on, beginner-friendly reference for learning <b>Streamlit</b> —<br>
  one function at a time, with real, runnable examples.
</p>

<p align="center">
  <a href="https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab">
    <img src="https://img.shields.io/badge/View_Source_Code-181717?style=for-the-badge&logo=github&logoColor=white" alt="View source code" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab/actions/workflows/ci.yml">
    <img src="https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab/actions/workflows/ci.yml/badge.svg" alt="CI Status"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.12%20%7C%203.14-3776AB?logo=python&logoColor=white" alt="Python Versions"/>
  <img src="https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit Version"/>
  <img src="https://img.shields.io/badge/Code%20Style-Ruff-000000?logo=ruff&logoColor=white" alt="Ruff Formatted"/>
  <img src="https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen?logo=pytest&logoColor=white" alt="Tests"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License"/>
</p>

---

## 🚀 Try it live

Experience the full interactive course directly in your browser without local setup:
<div align="center">

[![Try Live App](https://img.shields.io/badge/_Open_Here-Experience_the_Course-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://shivtejpatil2807-streamlit-cookbook-home-2l87yc.streamlit.app/)
[![Streamlit Cloud](https://img.shields.io/badge/Hosted%20on-Streamlit%20Cloud-blue?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/cloud)

</div>

---

> 💡**Tip:** No setup needed. Open the link, pick a lesson, and see every function's explanation, code and live result side by side in your browser.

---

## 📑 Table of contents

- [What you get](#what-you-get)
- [What is Streamlit?](#what-is-streamlit)
- [How each lesson works](#how-each-lesson-works)
- [Topics covered](#topics-covered)
- [Running locally](#running-locally)
- [Project structure](#project-structure)
- [Development](#development)
- [Core Streamlit concepts](#core-streamlit-concepts)
- [Who this is for](#who-this-is-for)
- [Further reading](#further-reading)
- [License](#license)

---

## What you get

- **17 lessons** covering the everyday Streamlit functions, from text to authentication, plus newer features like dialogs, fragments and streaming
- **An interactive Home page** with search, category and level filters, colored level labels, and a progress bar
- **A "Continue" button** that takes you to the next lesson you haven't finished
- **Learn → Code → Try tabs** on every function, so you read it, copy it and run it
- **A challenge at the end of each lesson** to check what you learned
- **Tests and CI**: every change is checked automatically on GitHub
- **Learning paths** such as "Build a chatbot", so you don't have to choose from 22 lessons

---

## What is Streamlit?

[Streamlit](https://streamlit.io/) is an open-source Python library that lets you build interactive web apps — dashboards, data tools, ML demos, forms — using **only Python**. No HTML, CSS, or JavaScript required.

You write a normal `.py` script using Streamlit's functions (`st.title()`, `st.button()`, `st.dataframe()`, etc.), and Streamlit turns it into a live web page. Every time the user interacts with something (clicks a button, moves a slider, types text), Streamlit **reruns your script from top to bottom** and updates the page automatically.

## Installation
Open a terminal and run:

```bash

$ pip install streamlit
$ streamlit hello

```
If this opens our sweet Streamlit Hello app in your browser, you're all set! If not, head over to [our docs](https://docs.streamlit.io/get-started) for specific installs.


**Why people like it:**

- ⚡ **Fast to build:** a working app in a few lines of code
- 🐍 **Pure Python:** no separate frontend code to write or maintain
- 🔄 **Auto-reload:** save the file and see the change instantly
- 📊 **Built for data:** works naturally with pandas, NumPy, matplotlib, and ML models
- 🌐 **Easy to deploy:** including free hosting on [Streamlit Community Cloud](https://streamlit.io/cloud)

---

## How each lesson works

Every function on every page has the same three tabs:

| Tab | What it shows |
|-----|---------------|
| 📖 **Learn** | A short explanation of what the function does |
| 💻 **Code** | The exact code, with a copy button |
| ▶️ **Try** | The live result, running right on the page |

The code you see is the code that runs. Both come from the same function, so they can never drift apart.

At the bottom of each lesson there is a short **🎯 Challenge** (multiple choice) and a **Mark this lesson as done** checkbox. Completed lessons are labelled "Done" on the Home page and count towards the progress bar.

---

## Topics covered

<!-- course:start -->
Every lesson belongs to one of three levels. In total there are **22** pages: 19 lessons and 3 mini-projects.

<details open>
<summary><strong>🌱 Beginner</strong> · 5 lessons</summary>

| Lesson | What you learn | Key functions |
| --- | --- | --- |
| [01 — Text & Markdown](pages/01_Text_and_Markdown.py) | Show titles, text, code and tables on the page. | `st.title`, `st.header`, `st.subheader`, `st.write`, `st.markdown`, `st.caption`, … |
| [02 — Input Widgets](pages/02_Input_Widgets.py) | Collect input with buttons, sliders, text boxes and selectors. | `st.button`, `st.checkbox`, `st.radio`, `st.selectbox`, `st.multiselect`, `st.slider`, … |
| [03 — Layouts](pages/03_Layouts.py) | Arrange content with columns, tabs, containers and placeholders. | `st.columns`, `st.tabs`, `st.container`, `st.sidebar`, `st.empty` |
| [04 — Data Display](pages/04_Data_Display.py) | Present tables, metrics and JSON. | `st.dataframe`, `st.table`, `st.metric`, `st.json` |
| [08 — Status & Messages](pages/08_Status_and_Messages.py) | Give users feedback with alerts, spinners and progress. | `st.success`, `st.error`, `st.warning`, `st.info`, `st.progress`, `st.spinner`, … |
</details>

<details>
<summary><strong>🌿 Intermediate</strong> · 10 lessons</summary>

| Lesson | What you learn | Key functions |
| --- | --- | --- |
| [05 — Charts](pages/05_Charts.py) | Plot data with Streamlit's built-in charts and maps. | `st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.scatter_chart`, `st.map` |
| [06 — File Handling](pages/06_File_Handling.py) | Upload and download files, and show images, audio and video. | `st.file_uploader`, `st.download_button`, `st.image`, `st.audio`, `st.video` |
| [07 — UI & Styling](pages/07_UI_and_Styling.py) | Customize the look with page config, colors and CSS. | `st.set_page_config`, `st.color_picker`, `st.markdown (CSS)`, `st.image` |
| [09 — Session State](pages/09_Session_State.py) | Remember values between reruns. | `st.session_state`, `widget key=` |
| [10 — Forms](pages/10_Forms.py) | Group inputs and submit them together. | `st.form`, `st.form_submit_button` |
| [12 — Chat Elements](pages/12_Chat_Elements.py) | Build chat interfaces. | `st.chat_message`, `st.chat_input` |
| [15 — Dialogs & Pop-ups](pages/15_Dialogs_and_Popups.py) | Show extra content on top of the page, only when the learner asks for it. | `st.dialog`, `st.popover`, `st.status` |
| [16 — Modern Inputs](pages/16_Modern_Inputs.py) | Newer widgets: clickable pills, star ratings and editable tables. | `st.pills`, `st.feedback`, `st.data_editor` |
| [18 — Secrets & Deployment](pages/18_Secrets_and_Deployment.py) | Keep private values out of your code and put your app online. | `st.secrets`, `st.__version__`, `Community Cloud` |
| [21 — Project: Sales Dashboard](pages/21_Project_Sales_Dashboard.py) | Explore sales data with filters, key numbers and graphs, using only pandas. | `pandas`, `st.multiselect`, `st.metric`, `st.columns` |
</details>

<details>
<summary><strong>🌳 Advanced</strong> · 7 lessons</summary>

| Lesson | What you learn | Key functions |
| --- | --- | --- |
| [11 — Caching](pages/11_Caching.py) | Speed up apps by caching data and resources. | `st.cache_data`, `st.cache_resource`, `ttl`, `cache.clear()` |
| [13 — Navigation](pages/13_Navigation.py) | Link and jump between pages. | `st.page_link`, `st.switch_page` |
| [14 — Authentication](pages/14_Authentication.py) | Protect content with a simple login, and see real auth. | `session-state login`, `st.login`, `st.user` |
| [17 — Fragments & Streaming](pages/17_Fragments_and_Streaming.py) | Rerun just part of a page, and show text as it is being produced. | `st.fragment`, `st.write_stream` |
| [19 — Testing Your App](pages/19_Testing_Your_App.py) | Check your app with automatic tests instead of clicking through it. | `assert`, `AppTest`, `pytest`, `GitHub Actions` |
| [20 — Project: Iris Classifier](pages/20_Project_Iris_Classifier.py) | Train a small model and predict an iris flower's species from four sliders. | `scikit-learn`, `st.slider`, `st.metric`, `st.cache_resource` |
| [22 — Project: Chatbot](pages/22_Project_Chatbot.py) | Build a chatbot that remembers the conversation, using simple rules instead of a paid AI model. | `st.chat_message`, `st.chat_input`, `st.session_state`, `st.write_stream` |
</details>

## Running locally

```bash
# 1. Clone the repo
git clone https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab.git
cd Streamlit-Learning-Lab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run Home.py
```

Your browser opens automatically at `http://localhost:8501`.

---

## Project structure

```text
Streamlit-Learning-Lab/
├── Home.py                    # Landing page: hero, search, filters, progress
├── core/                      # Shared code used by every page
│   ├── lessons.py             #   registry of all lessons
│   ├── components.py          #   lesson_page, demo (Learn/Code/Try), lesson_footer
│   ├── challenges.py          #   multiple-choice questions for each lesson
│   └── theme.py               #   shared look: hero, cards, level labels
├── pages/                     # One file per lesson (auto-detected by Streamlit)
│   ├── 01_Text_and_Markdown.py
│   ├── ...
│   └── 22_Project: Chatbot 
├── specs/                     # What each part of the app must do
├── tests/                     # Automated tests that check the specs
├── .github/workflows/ci.yml   # Runs ruff and the tests on every push and PR
├── .streamlit/config.toml     # Theme colors and server settings
├── assets/                    # Images and data used by the lessons
├── docs/                      # Screenshots used in this README
├── pyproject.toml             # ruff and pytest settings
├── requirements.txt           # Dependencies to run the app
└── requirements-dev.txt       # Adds pytest and ruff for development
```

Streamlit turns every file inside `pages/` into a sidebar entry. The numbered prefixes control the order. To add a lesson:

1. Create the page in `pages/`.
2. Add an entry to `core/lessons.py`.
3. Add a challenge to `core/challenges.py`.

The tests tell you if something is missing.

---

## Development

```bash
pip install -r requirements-dev.txt

python -m pytest -v     # run the tests
ruff check .            # check the code style
```

- **Specs** in [`specs/`](specs/) describe what each part must do as short numbered requirements (R1, R2, ...). Each test names the requirement it checks.
- **CI** runs ruff and the tests on Python 3.12 and 3.14 for every pull request and every push to `main`.
- Changes go through a branch and a pull request. Merge once the checks are green.

---

## Core Streamlit concepts

Good to know before diving in:

- **Script reruns, not page reloads:** every interaction reruns your whole `.py` file from top to bottom. Streamlit is fast enough that this feels instant.
- **Widgets return values:** `x = st.slider(...)` gives you the current value directly. No callbacks are needed for simple cases.
- **State doesn't persist by default:** normal Python variables reset on every rerun. Use `st.session_state` to remember values between reruns (lesson 9).
- **Layout is just more function calls:** `st.columns()`, `st.tabs()`, and `st.sidebar` arrange widgets without any CSS.
- **Caching avoids repeated work:** wrap slow functions (data loading, model inference) with `@st.cache_data` or `@st.cache_resource` so they only run once (lesson 11).

## Who this is for

Beginners learning Streamlit from scratch, or anyone who wants a quick, copy-paste reference for a specific function without digging through the full [official docs](https://docs.streamlit.io/).

## Further reading

- [Streamlit official docs](https://docs.streamlit.io/)
- [Streamlit API reference](https://docs.streamlit.io/develop/api-reference)
- [Streamlit Community Cloud (free deployment)](https://streamlit.io/cloud)
- [Streamlit forum](https://discuss.streamlit.io/)

## License

This project is available for educational and learning purposes.

---

⭐ If you like this project, consider giving the repository a star!
