# 008: Lesson feedback

**Files:** `core/feedback.py` (`feedback_url`), `core/components.py` (`lesson_footer`)
**Status:** Implemented

## Purpose
Let a learner tell us when a lesson is unclear, wrong or missing something,
without any extra service. The button opens a new GitHub issue that already names
the lesson.

## Requirements
- **R1** `feedback_url(lesson)` points to the repository's "new issue" page.
- **R2** The issue title contains the lesson number and title.
- **R3** The issue body names the lesson and its page file, and asks what was
  unclear, wrong or missing.
- **R4** The link is URL-encoded: it has no spaces or line breaks.
- **R5** Decoding the link gives back the exact title and body.
- **R6** Every lesson page shows a feedback button that uses this link.
- **R7** Clicking the button opens GitHub in a new tab. This is checked by hand.

## Notes
- Sending the issue needs a free GitHub account. The page says so.
