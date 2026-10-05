"""Links that let a learner report a problem or suggest an improvement.

The link opens a new GitHub issue with the lesson's name already filled in,
so no extra service or database is needed.
"""
from urllib.parse import quote, urlencode

from core.export import REPO_URL


def feedback_url(lesson) -> str:
    """A pre-filled 'new issue' link for this lesson."""
    title = f"Feedback on lesson {lesson.number}: {lesson.title}"
    body = "\n".join(
        [
            f"**Lesson:** {lesson.number}. {lesson.title}",
            f"**Page:** `{lesson.path}`",
            "",
            "**What was unclear, wrong or missing?**",
            "",
        ]
    )
    query = urlencode({"title": title, "body": body}, quote_via=quote)
    return f"{REPO_URL}/issues/new?{query}"
