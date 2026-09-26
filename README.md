<p align="left">
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="100"/>
</p>

# Welcome to Streamlit

A faster way to build and share data apps.

## 📚 Streamlit Learning Lab

A hands-on, beginner-friendly reference repo for learning **Streamlit** —
one function at a time, with real, runnable examples.

### Try it live

**[Open the live app and learn from here](https://shivtejpatil2807-streamlit-cookbook-home-2l87yc.streamlit.app/)**

No setup needed — just open the link, pick a topic from the sidebar, and
see every function's code and output side by side in your browser.

---

## What is Streamlit?

[Streamlit](https://streamlit.io/) is an open-source Python library that lets
you build interactive web apps — dashboards, data tools, ML demos, forms —
using **only Python**. No HTML, CSS, or JavaScript required.

You write a normal `.py` script using Streamlit's functions (`st.title()`,
`st.button()`, `st.dataframe()`, etc.), and Streamlit turns it into a live
web page. Every time the user interacts with something (clicks a button,
moves a slider, types text), Streamlit **reruns your script from top to
bottom** and updates the page automatically.

**Why people like it:**
- ⚡ Extremely fast to build with — a working app in a few lines of code
- 🐍 Pure Python — no separate frontend code to write or maintain 
- 🔄 Auto-reload while developing — save the file, see the change instantly 
- 📊 Built for data — plays naturally with pandas, NumPy, matplotlib, and ML models 
- 🌐 Easy to deploy — including free hosting on [Streamlit Community Cloud](https://streamlit.io/cloud)

**Install it:**
```bash
pip install streamlit
```

**Run any app:**
```bash
streamlit run Home.py
```

---

## How this repo works

This repo covers Streamlit **topic by topic**. Every page follows the exact
same three-part pattern for each function, so you always know what you're
looking at:

1. **Title** — the name of the function
2. **Code** — the exact code that produces the result
3. **Output** — the live result, rendered right below the code

Click any topic below to jump straight to its file and start learning.

---

## Topics covered (in order)

| # | Topic | Link | What you'll learn |
|---|-------|------|--------------------|
| 1 | Text & Markdown | [pages/01_Text_and_Markdown.py](pages/01_Text_and_Markdown.py) | `title`, `header`, `subheader`, `write`, `markdown`, `caption`, `code`, `divider`, `table`, `expander` |
| 2 | Input Widgets | [pages/02_Input_Widgets.py](pages/02_Input_Widgets.py) | `button`, `checkbox`, `radio`, `selectbox`, `multiselect`, `slider`, `text_input`, `text_area`, `number_input`, `date_input` |
| 3 | Layouts | [pages/03_Layouts.py](pages/03_Layouts.py) | `columns`, `tabs`, `container`, `sidebar`, `empty` |
| 4 | Data Display | [pages/04_Data_Display.py](pages/04_Data_Display.py) | `dataframe`, `table`, `metric`, `json` |
| 5 | Charts | [pages/05_Charts.py](pages/05_Charts.py) | `line_chart`, `bar_chart`, `area_chart`, `scatter_chart`, `map` |
| 6 | File Handling | [pages/06_File_Handling.py](pages/06_File_Handling.py) | `file_uploader`, `download_button`, `image`, `audio`, `video` |
| 7 | UI & Styling | [pages/07_UI_and_Styling.py](pages/07_UI_and_Styling.py) | `set_page_config`, `color_picker`, custom CSS with `st.markdown` |
| 8 | Status & Messages | [pages/08_Status_and_Messages.py](pages/08_Status_and_Messages.py) | `success`, `error`, `warning`, `info`, `progress`, `spinner`, `toast`, `balloons` |
| 9 | Session State | [pages/09_Session_State.py](pages/09_Session_State.py) | reading and writing `st.session_state` across reruns |
| 10 | Forms | [pages/10_Forms.py](pages/10_Forms.py) | `form`, `form_submit_button` |
| 11 | Caching | [pages/11_Caching.py](pages/11_Caching.py) | `cache_data`, `cache_resource` |
| 12 | Chat Elements | [pages/12_Chat_Elements.py](pages/12_Chat_Elements.py) | `chat_message`, `chat_input` |
| 13 | Navigation | [pages/13_Navigation.py](pages/13_Navigation.py) | `page_link`, `switch_page`, how multipage apps work |
| 14 | Authentication | [pages/14_Authentication.py](pages/14_Authentication.py) | DIY `session_state` login pattern, `st.login()` overview |

> Tip: read them in order the first time through — later pages
> sometimes reuse ideas (like `session_state`) introduced earlier.

---

## Project structure

```
streamlit-cookbook/
├── game.py
├── Home.py                        # Landing page + topic index
├── requirements.txt                # Python dependencies
├── README.md                       # You are here
├── .gitignore
├── assets/                         # Images/media used by example pages
└── pages/                          # Each file = one sidebar page (auto-detected by Streamlit)
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

Streamlit automatically turns every file inside `pages/` into a sidebar
entry — the numbered prefixes just control the order they appear in. You
don't need to register pages anywhere; just drop a new `.py` file into
`pages/` and it shows up.

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

Your browser will open automatically at `http://localhost:8501`.

---

## Core Streamlit concepts (good to know before diving in)

- **Script reruns, not page reloads** — every interaction reruns your whole
  `.py` file top to bottom. Streamlit is fast enough that this feels instant.
- **Widgets return values** — `x = st.slider(...)` gives you the current
  value directly; no callbacks needed for simple cases.
- **State doesn't persist by default** — normal Python variables reset on
  every rerun. Use `st.session_state` to remember values between reruns
  (covered in topic 9).
- **Layout is just more function calls** — `st.columns()`, `st.tabs()`, and
  `st.sidebar` let you arrange widgets without any CSS.
- **Caching avoids repeated work** — wrap slow functions (data loading,
  model inference) with `@st.cache_data` or `@st.cache_resource` so they
  only run once (covered in topic 11).

---

## Who this is for

Beginners learning Streamlit from scratch, or anyone who wants a quick,
copy-paste reference for a specific function without digging through the
full [official docs](https://docs.streamlit.io/).

## Further reading

- [Streamlit official docs](https://docs.streamlit.io/)
- [Streamlit API reference](https://docs.streamlit.io/develop/api-reference)
- [Streamlit Community Cloud (free deployment)](https://streamlit.io/cloud)
- [Streamlit forum](https://discuss.streamlit.io/)

## Featured Project: Guess Quest

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-green)

</p>

## Introduction
Guess Quest is an interactive multi-stage number guessing web application built with Python and Streamlit, enhanced with HTML and CSS to create a modern, visually engaging user interface.

The game takes players through five challenging stages, starting with a number guessing challenge and progressing through an instructions stage, a mathematical pattern puzzle, a verification challenge, and a high-stakes final guessing round with limited attempts.

The project combines Python game logic, Streamlit components, HTML-based layouts, and custom CSS styling to create an interactive and user-friendly gaming experience. It also demonstrates concepts such as random number generation, conditional logic, functions, forms, session state, user input handling, and stage-based progression.

## Features

* **User Login:** Users can enter their username before starting the game.
* **Random Number Generation:** The application generates a random number for the user to guess.
* **Number Guessing:** Users can enter their guesses and try to find the correct number.
* **Guess Hints:** The application provides feedback to help users determine whether their guess is too high or too low.
* **Pattern Challenge:** Players must identify a hidden mathematical pattern and calculate the missing answer.
* **Randomized Challenges:** Pattern challenges use randomly generated numbers.
* **Winning Message:** A success message is displayed when the user guesses the correct number.
* **Play Again:** Users can restart the game and play again.
* **Interactive UI:** The application provides a simple and interactive Streamlit interface.
* **Session State:** Streamlit session state is used to maintain the user's game information during the session.

## How It Works

1. The user enters their username.
2. The game starts after submitting the username.
3. A random number is generated for the number guessing stage.
4. The user enters a guess and receives feedback depending on the result.
5. The player progresses through the different game stages.
6. The player encounters a same instructions before continuing.
7. The Pattern Challenge displays a sequence of mathematical equations.
8. The player must identify the hidden pattern and calculate the missing answer.
9. After successfully completing all stages, the success screen is displayed.
10. If the player fails, the game-over screen is displayed.
11. The player can start another game.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShivtejPatil2807/Streamlit-Learning-Lab.git
```

### 2. Navigate to the Project Directory

```bash
cd Guess Quest
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. install Streamlit 

```bash
pip install streamlit
```

### 5. Run the Application

```bash
streamlit run game.py
```

### 6. Open the Application

After running the command, Streamlit will provide a local URL in the terminal. Open that URL in your web browser to start playing the game.

## Live Demo

**Play the game online:** [Simple Guess Game](https://guess-quest.streamlit.app/)

## Future Improvements

* **Add difficulty levels.**
* **Add a score system.**
* **Add a leaderboard.**
* **Add a timer for each stage.**
* **Store player scores.**
* **Add more game stages.**

## License

This project is available for educational and learning purposes.

---
If you like this project, consider giving the repository a star!
