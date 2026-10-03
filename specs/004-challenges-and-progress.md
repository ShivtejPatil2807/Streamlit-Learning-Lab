# 004: Challenges and progress

**Files:** `core/challenges.py`, `core/components.py` (`lesson_footer`)
**Status:** Implemented

## Purpose
Let learners check what they just learned and mark the lesson as done. The
Home page shows the result in its progress bar.

## Why multiple choice
The app is public. Letting visitors type and run their own code would let
anyone run code on the server, so the "try it" step is limited to the live demo
plus questions with fixed answers.

## Requirements
- **R1** Every lesson in the registry has at least one challenge.
- **R2** Every challenge has a question, at least two different options, an
  explanation, and an answer that points to one of its options.
- **R3** `lesson_footer` shows one question per challenge, with no option
  selected at first.
- **R4** Choosing the right option shows a success message that includes the
  explanation.
- **R5** Choosing a wrong option shows an error message and does not reveal the
  answer, so the learner can try again.
- **R6** `lesson_footer` shows a "Mark this lesson as done" checkbox. It is
  ticked only if the lesson is in `st.session_state["completed"]`.
- **R7** Ticking the checkbox adds the lesson to `st.session_state["completed"]`.
  Unticking removes it.
- **R8** The Home page reads the same set, so a lesson marked as done on its own
  page counts in Home's "Completed" stat.

## Adding a challenge
Add a `Challenge(...)` to the lesson's list in `core/challenges.py`. The tests
check R1 and R2.
