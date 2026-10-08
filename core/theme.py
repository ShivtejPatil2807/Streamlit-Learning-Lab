"""Shared look and feel: one stylesheet used by Home and every lesson page.

Classes starting with `lab-` belong to our own HTML blocks. The rules that
target Streamlit's own elements (tabs, metrics, bordered containers) are
cosmetic: if a future Streamlit version renames those elements, the app keeps
working and only the extra styling is lost.
"""
import html

import streamlit as st

_CSS = """
<style>
:root {
    --lab-accent: #7C5CFF;
    --lab-accent-2: #FF5C8A;
    --lab-accent-text: #A592FF;
    --lab-border: rgba(255, 255, 255, 0.10);
    --lab-muted: rgba(232, 236, 244, 0.65);
}

/* ---------- hero ---------- */
.lab-hero {
    padding: 2.2rem 2rem 1.8rem 2rem;
    border-radius: 20px;
    border: 1px solid var(--lab-border);
    background:
        radial-gradient(circle at 12% 0%, rgba(124, 92, 255, 0.35), transparent 55%),
        radial-gradient(circle at 100% 100%, rgba(255, 92, 138, 0.25), transparent 50%),
        #141A2B;
    margin-bottom: 1.2rem;
}
.lab-kicker {
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    font-weight: 700;
    color: var(--lab-muted);
    margin-bottom: 0.4rem;
}
.lab-hero h1 {
    margin: 0 0 0.5rem 0;
    padding: 0;
    font-size: 2.6rem;
    line-height: 1.1;
    background: linear-gradient(90deg, #FFFFFF, #C9BFFF);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
.lab-hero p { margin: 0 0 1.1rem 0; font-size: 1.08rem; color: var(--lab-muted); }
.lab-steps { display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; }
.lab-step {
    padding: 0.28rem 0.8rem;
    border-radius: 999px;
    font-size: 0.88rem;
    font-weight: 600;
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid var(--lab-border);
}
.lab-arrow { color: var(--lab-muted); }

/* ---------- lesson cards (our HTML part) ---------- */
.lab-card-title { display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.5rem; }
.lab-card-icon { font-size: 1.7rem; line-height: 1; }
.lab-card-name { font-size: 1.15rem; font-weight: 700; line-height: 1.2; }
.lab-card-num { color: var(--lab-accent-text); margin-right: 0.35rem; }
.lab-meta { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.7rem; }
.lab-pill {
    padding: 0.14rem 0.65rem;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 700;
    border: 1px solid transparent;
}
.lab-beginner     { color: #34D399; background: rgba(52, 211, 153, 0.12); border-color: rgba(52, 211, 153, 0.35); }
.lab-intermediate { color: #FBBF24; background: rgba(251, 191, 36, 0.12);  border-color: rgba(251, 191, 36, 0.35); }
.lab-advanced     { color: #FB7185; background: rgba(251, 113, 133, 0.12); border-color: rgba(251, 113, 133, 0.35); }
.lab-category     { color: var(--lab-muted); background: rgba(255, 255, 255, 0.06); border-color: var(--lab-border); }
.lab-summary { margin: 0 0 0.7rem 0; color: var(--lab-muted); font-size: 0.95rem; min-height: 2.6em; }
.lab-chips { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.4rem; }
.lab-chip {
    font-family: "Source Code Pro", ui-monospace, monospace;
    font-size: 0.72rem;
    padding: 0.1rem 0.45rem;
    border-radius: 6px;
    color: #A5B4FC;
    background: rgba(124, 92, 255, 0.12);
}

/* ---------- Streamlit elements ---------- */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 16px;
    transition: transform 0.15s ease, border-color 0.15s ease;
}
@media (hover: hover) {
    [data-testid="stVerticalBlockBorderWrapper"]:has(.lab-card-title):hover {
        transform: translateY(-3px);
        border-color: var(--lab-accent);
    }
}

[data-testid="stMetric"] {
    background: #141A2B;
    border: 1px solid var(--lab-border);
    border-radius: 14px;
    padding: 0.9rem 1.1rem;
}

button[data-baseweb="tab"] { font-weight: 600; }
button[data-baseweb="tab"]:focus:not(:focus-visible) { outline: none; box-shadow: none; }
button[data-baseweb="tab"]:focus-visible {
    outline: 2px solid var(--lab-accent-text);
    outline-offset: 2px;
}

/* a wide table in the lesson text scrolls sideways instead of widening the page */
[data-testid="stMarkdownContainer"] table {
    display: block;
    max-width: 100%;
    overflow-x: auto;
}

/* bigger tap targets on touch screens */
@media (pointer: coarse) {
    [data-testid="stButton"] button,
    [data-testid="stDownloadButton"] button,
    a[data-testid^="stBaseLinkButton"] {
        min-height: 2.75rem;
    }
}

/* small screens: a smaller hero */
@media (max-width: 640px) {
    .lab-hero { padding: 1.4rem 1.1rem 1.2rem 1.1rem; border-radius: 16px; }
    .lab-hero h1 { font-size: 1.9rem; }
    .lab-hero p { font-size: 1rem; }
    .lab-step { font-size: 0.8rem; padding: 0.22rem 0.6rem; }
}

/* people who ask their system for less motion get none */
@media (prefers-reduced-motion: reduce) {
    [data-testid="stVerticalBlockBorderWrapper"] { transition: none; }
    [data-testid="stVerticalBlockBorderWrapper"]:has(.lab-card-title):hover { transform: none; }
}

h2 {
    border-left: 4px solid var(--lab-accent);
    padding-left: 0.7rem !important;
}
</style>
"""


def apply_theme() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def pill(text: str, kind: str) -> str:
    """One small rounded label, as HTML. `kind` picks the colour class."""
    return f'<span class="lab-pill lab-{kind}">{html.escape(text)}</span>'


def level_pill(level: str) -> str:
    return pill(level, level.lower())


def chips(names) -> str:
    """Function names as small code-style chips, as HTML."""
    return "".join(f'<span class="lab-chip">{html.escape(name)}</span>' for name in names)
