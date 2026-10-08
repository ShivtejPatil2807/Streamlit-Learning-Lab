# 013: Mobile and accessibility

**Files:** `core/theme.py`, `Home.py`, `.streamlit/config.toml`
**Status:** Implemented

## Purpose
Many learners will open the app on a phone, and some will use a keyboard or a
screen reader. This spec lists what the app does for them. Streamlit already
stacks columns on narrow screens and collapses the sidebar, so the lesson
buttons at the bottom of each page are how a phone user moves around.

## Requirements
- **R1** On screens up to 640px wide, the hero is smaller: less padding and a
  smaller title.
- **R2** The hover lift on lesson cards only applies to devices that can hover,
  so it does not stay stuck after a tap.
- **R3** On touch screens, buttons are at least 44px tall.
- **R4** A wide table in a lesson scrolls sideways inside its box instead of
  widening the page.
- **R5** Keyboard focus stays visible on the tabs. Only the outline caused by a
  mouse click is hidden.
- **R6** For people who ask their system for less motion, cards do not animate.
- **R7** The text colours used for labels, chips and card numbers have a
  contrast of at least 4.5:1 against both theme backgrounds (the WCAG AA
  level for normal text).
- **R8** The decorative emoji on lesson and path cards are hidden from screen
  readers.
- **R9** Every image in the README has alt text.
- **R10** Every lesson card has its own link text ("Open <title>") and its own
  checkbox label ("Mark <title> as done"). Screen readers list links and form
  fields out of context, and 22 links that all say "Open lesson" are
  indistinguishable.

## Not covered (known limits)
- Graphs and plots have no text description. A description could be added under
  each one.
- Colour themes come from `.streamlit/config.toml`. Learners can still switch
  to a light theme in Streamlit's own settings menu, which this spec does not
  test.
