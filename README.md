<p align="center">
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="100" alt="Streamlit logo"/>
</p>

<h1 align="center">📚 Streamlit Learning Lab</h1>

<p align="center">
  A hands-on, beginner-friendly reference repo for learning <b>Streamlit</b> —<br>
  one function at a time, with real, runnable examples.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/License-Educational-green" alt="License"/>
</p>

---

## 🚀 Try it live

**[Open the live app and learn from here](https://shivtejpatil2807-streamlit-cookbook-home-2l87yc.streamlit.app/)**

No setup needed — just open the link, pick a topic from the sidebar, and see every function's code and output side by side in your browser.

---

## 📑 Table of contents

- [What is Streamlit?](#what-is-streamlit)
- [Installation and quickstart](#installation-and-quickstart)
- [How this repo works](#how-this-repo-works)
- [Topics covered](#topics-covered)
- [Project structure](#project-structure)
- [Running locally](#running-locally)
- [Core Streamlit concepts](#core-streamlit-concepts)
- [Who this is for](#who-this-is-for)
- [Further reading](#further-reading)
- [License](#license)

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

## Installation and quickstart

**1. Install Streamlit**

```bash
pip install streamlit
```

**2. Create your first app**

Create a file named `streamlit_app.py` in your project directory with the following code:

```python
import streamlit as st

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

**3. Run it**

```bash
streamlit run streamlit_app.py
```

Your browser opens the app automatically. 🎉

---

## How this repo works

This repo covers Streamlit **topic by topic**. Every page follows the same three-part pattern for each function, so you always know what you're looking at:

1. **Title:** the name of the function
2. **Code:** the exact code that produces the result
3. **Output:** the live result, rendered right below the code

Click any topic below to jump straight to its file and start learning.

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

## Project structure

```text
Streamlit-Cookbook/
├── Home.py                  # Landing page + topic index
├── requirements.txt         # Python dependencies
├── README.md                # You are here
├── .gitignore
├── assets/                  # Images/media used by example pages
└── pages/                   # Each file = one sidebar page (auto-detected)
    ├── 01_Text_and_Markdown.py
    ├── 02_Input_Widgets.py
    ├── 03_Layouts.py
    ├── 04_Data_Display.py
    ├── 05_Charts.py
    ├── 06_File_Handling.py
    ├── 07_UI_and_Styling.py
    ├── 08_Status_and_Messages.py
    ├── 09_Session_State.py
    ├── 10_Forms.py
    ├── 11_Caching.py
    ├── 12_Chat_Elements.py
    ├── 13_Navigation.py
    └── 14_Authentication.py
```

Streamlit automatically turns every file inside `pages/` into a sidebar entry. The numbered prefixes only control the order. You don't need to register pages anywhere: drop a new `.py` file into `pages/` and it shows up.

---

## Running locally

```bash
# 1. Clone the repo
git clone https://github.com/ShivtejPatil2807/Streamlit-Cookbook.git
cd Streamlit-Cookbook

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run Home.py
```

Your browser opens automatically at `http://localhost:8501`.

---

## Core Streamlit concepts

Good to know before diving in:

- **Script reruns, not page reloads:** every interaction reruns your whole `.py` file from top to bottom. Streamlit is fast enough that this feels instant.
- **Widgets return values:** `x = st.slider(...)` gives you the current value directly. No callbacks are needed for simple cases.
- **State doesn't persist by default:** normal Python variables reset on every rerun. Use `st.session_state` to remember values between reruns (topic 9).
- **Layout is just more function calls:** `st.columns()`, `st.tabs()`, and `st.sidebar` arrange widgets without any CSS.
- **Caching avoids repeated work:** wrap slow functions (data loading, model inference) with `@st.cache_data` or `@st.cache_resource` so they only run once (topic 11).

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
