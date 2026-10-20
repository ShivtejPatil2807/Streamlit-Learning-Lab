# 015: Home page in the style of a docs site

**Files:** `Home.py`, `core/theme.py`, `.streamlit/config.toml`
**Status:** Implemented

Builds on spec 003 (what the Home page does), spec 012 (learning paths), spec 016
(the level tiles) and spec 017 (search). This spec covers the layout.

## Purpose
A page that feels like the Streamlit documentation home page: a plain page title,
three big coloured tiles, then clear sections. A visitor should know what the site
is, where to start, and where to go next.

## Requirements
- **R1** The page is laid out in this order: top bar with search, title, level tiles,
  progress, "How to use the Lab", learning paths, latest lessons, the community card,
  "Elsewhere", the next lesson, the footer.
- **R2** The title is a single plain level-1 heading, "Streamlit Learning Lab", with a
  short description and the Learn → Code → Try → Challenge steps. It is not inside a
  coloured box.
- **R3** The progress panel's button says "Start learning" for a new visitor and
  "Continue" once a lesson is done. It opens the first lesson that is not completed.
  (Opening the lesson is checked by hand.)
- **R4** When every lesson is done, the panel shows a success message and no button.
- **R5** The section titles are real headings, in this order: Choose your level, Your
  progress, How to use the Lab, Learning paths, Latest lessons, Elsewhere.
- **R6** "How to use the Lab" has three rows: Start, Practice, Build.
- **R7** "Latest lessons" shows the six newest lessons, newest first, each with its
  title, summary and first functions.
- **R8** The community card links to the issue page and to the source on GitHub.
- **R9** "Elsewhere" lists four places: GitHub, the Streamlit docs, the Streamlit forum
  and Streamlit Community Cloud.
- **R10** The footer links to the source, the issues and the docs, shows the year, and
  says the project is not affiliated with Streamlit or Snowflake.
- **R11** All text is readable (contrast of at least 4.5:1): white on every coloured
  tile, icon box and button, and dark text on the light community card.
- **R12** The stylesheet defines the style of every block above.

## Notes
- The tiles use a darker orange than the Streamlit docs do. White text on the docs'
  orange is only 2.3:1, below the 4.5:1 minimum. Ours is 5.0:1.
- Internal links use `st.page_link`, which keeps the learner's progress. A plain HTML
  link would reload the app and reset it.
- When a level is open (spec 016), its lessons get a heading of their own,
  for example "Beginner lessons", right after "Choose your level".
