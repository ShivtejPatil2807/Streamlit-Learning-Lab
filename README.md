<p align="center">
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="100" alt="Streamlit logo"/>
</p>

<h1 align="center">📚 Streamlit Learning Lab</h1>

<p align="center">
  A hands-on, beginner-friendly reference for learning <b>Streamlit</b> —<br>
  one function at a time, with real, runnable examples.
</p>

<p align="center">
  <a href="https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab/actions/workflows/ci.yml">
    <img src="https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab/actions/workflows/ci.yml/badge.svg" alt="CI status"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python 3.12+"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/License-Educational-green" alt="License"/>
</p>


---

## 🚀 Try it live

**[Open the live app and learn from here](https://shivtejpatil2807-streamlit-cookbook-home-2l87yc.streamlit.app/)**

No setup needed. Open the link, pick a lesson, and see every function's explanation, code and live result side by side in your browser.

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

- **14 lessons** covering the everyday Streamlit functions, from text to authentication
- **An interactive Home page** with search, category and level filters, and a progress bar
- **Learn → Code → Try tabs** on every function, so you read it, copy it and run it
- **A challenge at the end of each lesson** to check what you learned
- **Tests and CI**: every change is checked automatically on GitHub

---

## What is Streamlit?

[Streamlit](https://streamlit.io/) is an open-source Python library that lets you build interactive web apps — dashboards, data tools, ML demos, forms — using **only Python**. No HTML, CSS, or JavaScript required.

You write a normal `.py` script using Streamlit's functions (`st.title()`, `st.button()`, `st.dataframe()`, etc.), and Streamlit turns it into a live web page. Every time the user interacts with something (clicks a button, moves a slider, types text), Streamlit **reruns your script from top to bottom** and updates the page automatically.

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

At the bottom of each lesson there is a short **🎯 Challenge** (multiple choice) and a **Mark this lesson as done** checkbox. Completed lessons count towards the progress bar on the Home page.

---

## Topics covered

| # | Topic | File | What you'll learn |
|---|-------|------|-------------------|
| 1 | Text & Markdown | [01_Text_and_Markdown.py](pages/01_Text_and_Markdown.py) | `title`, `header`, `subheader`, `write`, `markdown`, `caption`, `code`, `divider`, `table`, `expander` |
| 2 | Input Widgets | [02_Input_Widgets.py](pages/02_Input_Widgets.py) | `button`, `checkbox`, `radio`, `selectbox`, `multiselect`, `slider`, `text_input`, `text_area`, `number_input`, `date_input` |
| 3 | Layouts | [03_Layouts.py](pages/03_Layouts.py) | `columns`, `tabs`, `container`, `sidebar`, `empty` |
| 4 | Data Display | [04_Data_Display.py](pages/04_Data_Display.py) | `dataframe`, `table`, `metric`, `json` |
| 5 | Charts | [05_Charts.py](pages/05_Charts.py) | `line_chart`, `bar_chart`, `area_chart`, `scatter_chart`, `map` |
| 6 | File Handling | [06_File_Handling.py](pages/06_File_Handling.py) | `file_uploader`, `download_button`, `image`, `audio`, `video` |
| 7 | UI & Styling | [07_UI_and_Styling.py](pages/07_UI_and_Styling.py) | `set_page_config`, `color_picker`, custom CSS with `st.markdown` |
| 8 | Status & Messages | [08_Status_and_Messages.py](pages/08_Status_and_Messages.py) | `success`, `error`, `warning`, `info`, `progress`, `spinner`, `toast`, `balloons` |
| 9 | Session State | [09_Session_State.py](pages/09_Session_State.py) | Reading and writing `st.session_state` across reruns |
| 10 | Forms | [10_Forms.py](pages/10_Forms.py) | `form`, `form_submit_button` |
| 11 | Caching | [11_Caching.py](pages/11_Caching.py) | `cache_data`, `cache_resource` |
| 12 | Chat Elements | [12_Chat_Elements.py](pages/12_Chat_Elements.py) | `chat_message`, `chat_input` |
| 13 | Navigation | [13_Navigation.py](pages/13_Navigation.py) | `page_link`, `switch_page`, how multipage apps work |
| 14 | Authentication | [14_Authentication.py](pages/14_Authentication.py) | DIY `session_state` login pattern, `st.login()` overview |

> 💡 **Tip:** read them in order the first time through. Later pages sometimes reuse ideas (like `session_state`) introduced earlier.

---

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
├── Home.py                    # Landing page: search, filters, progress
├── core/                      # Shared code used by every page
│   ├── lessons.py             #   registry of all lessons
│   ├── components.py          #   lesson_page, demo (Learn/Code/Try), lesson_footer
│   ├── challenges.py          #   multiple-choice questions for each lesson
│   └── theme.py               #   shared styling
├── pages/                     # One file per lesson (auto-detected by Streamlit)
│   ├── 01_Text_and_Markdown.py
│   ├── ...
│   └── 14_Authentication.py
├── specs/                     # What each part of the app must do
├── tests/                     # Automated tests that check the specs
├── .github/workflows/ci.yml   # Runs ruff and the tests on every push and PR
├── .streamlit/config.toml     # Theme and server settings
├── assets/                    # Images and data used by the lessons
├── docs/                      # Screenshots for this README
├── pyproject.toml             # ruff and pytest settings
├── requirements.txt           # Dependencies to run the app
└── requirements-dev.txt       # Adds pytest and ruff for development
```

Streamlit turns every file inside `pages/` into a sidebar entry. The numbered prefixes control the order. To add a lesson, create the page, add an entry to `core/lessons.py` and a challenge to `core/challenges.py`. The tests tell you if something is missing.

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
