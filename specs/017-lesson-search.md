# 017: Lesson search

**Files:** `core/search.py`, `Home.py`
**Status:** Implemented

## Purpose
A search box in the top bar of the Home page, like the one on a docs site. It finds a
lesson by its title, a function name or a word in its summary.

## Requirements
- **R1** An empty or blank query, or one made only of filler words ("the", "of", "to"),
  finds nothing.
- **R2** A word in a lesson's title ranks that lesson first.
- **R3** A function name ("st.form", "download button") finds the lesson that teaches
  it.
- **R4** Capital letters and plurals do not matter.
- **R5** At most the requested number of lessons is returned, each lesson once.
- **R6** A query that matches nothing finds nothing.
- **R7** On the Home page, typing a query shows one result per lesson found, under the
  search box, each with a link to the lesson. (Opening the link is checked by hand.)
- **R8** If nothing matches, the page says so.
- **R9** Without a query the page shows no results.

## Notes
- Search is plain word matching with no outside service. A title word counts most, a
  function name next, a summary word least.
