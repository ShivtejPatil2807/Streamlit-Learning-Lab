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

/* ---------- hero: a plain page title, like a docs site ---------- */
.lab-hero {
    padding: 0.6rem 0 0.4rem 0;
    margin-bottom: 0.6rem;
}
.lab-kicker {
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    font-weight: 700;
    color: var(--lab-muted);
    margin-bottom: 0.4rem;
}
.lab-hero h1 {
    margin: 0 0 0.8rem 0;
    padding: 0;
    font-size: 3.2rem;
    line-height: 1.1;
    color: #FFFFFF;
}
.lab-hero p {
    margin: 0 0 1.1rem 0;
    font-size: 1.15rem;
    line-height: 1.55;
    color: var(--lab-muted);
    max-width: 60rem;
}
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

/* ---------- top bar (Home) ---------- */
.lab-brand {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-size: 1.3rem;
    font-weight: 600;
}
.lab-brand-logo { font-size: 1.9rem; line-height: 1; }

/* ---------- search results (Home) ---------- */
.lab-result { padding: 0.5rem 0 0.3rem 0; }
.lab-result strong { font-size: 1.02rem; }
.lab-result p { margin: 0.15rem 0 0 0; color: var(--lab-muted); font-size: 0.92rem; }

/* ---------- big level tiles (Home) ---------- */
.lab-stage {
    border-radius: 14px;
    padding: 1.4rem 1.4rem 1rem 1.4rem;
    color: #FFFFFF;
}
.lab-stage[data-level="beginner"]     { background: #B45309; }
.lab-stage[data-level="intermediate"] { background: #6D4AFF; }
.lab-stage[data-level="advanced"]     { background: #0E7490; }
.lab-stage:not([data-level="beginner"]):not([data-level="intermediate"]):not([data-level="advanced"]) {
    background: #334155;
}
.lab-stage .lab-card-name { color: #FFFFFF; font-size: 1.4rem; }
.lab-stage .lab-summary { color: rgba(255, 255, 255, 0.95); font-size: 1rem; }
.lab-stage .lab-pill {
    background: rgba(0, 0, 0, 0.28);
    color: #FFFFFF;
    border-color: rgba(255, 255, 255, 0.25);
}
.lab-stage .lab-chip { background: rgba(0, 0, 0, 0.25); color: #FFFFFF; }

/* ---------- "how to use" rows (Home) ---------- */
.lab-how {
    display: flex;
    align-items: center;
    gap: 1.1rem;
    padding: 1rem 0;
    border-bottom: 1px solid var(--lab-border);
}
.lab-how-icon {
    flex: 0 0 3.2rem;
    height: 3.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    font-size: 1.5rem;
}
.lab-how-orange { background: #B45309; }
.lab-how-purple { background: #6D4AFF; }
.lab-how-cyan   { background: #0E7490; }
.lab-how p { margin: 0; font-size: 1.05rem; line-height: 1.5; }
.lab-how strong.orange { color: #FBBF24; }
.lab-how strong.purple { color: #A592FF; }
.lab-how strong.cyan   { color: #67E8F9; }

/* ---------- "latest lessons" cards (Home) ---------- */
.lab-news { padding: 0.4rem 0.2rem 0.2rem 0.2rem; }
.lab-news-icon { font-size: 1.6rem; line-height: 1; }
.lab-news h3 { margin: 0.7rem 0 0.35rem 0; padding: 0; font-size: 1.25rem; line-height: 1.25; }
.lab-news p { margin: 0 0 0.5rem 0; color: var(--lab-muted); font-size: 0.95rem; line-height: 1.55; }
.lab-code {
    font-family: "Source Code Pro", ui-monospace, monospace;
    font-size: 0.85em;
    color: #34D399;
    background: rgba(52, 211, 153, 0.12);
    padding: 0.05rem 0.35rem;
    border-radius: 5px;
}

/* ---------- community card (Home) ---------- */
.lab-community {
    background: #F0F2F6;
    color: #1B1F2A;
    border-radius: 14px;
    padding: 2rem 2.2rem;
}
.lab-community h3 { margin: 0 0 0.7rem 0; padding: 0; font-size: 2rem; color: #1B1F2A; }
.lab-community p {
    margin: 0 0 1.2rem 0;
    font-size: 1.08rem;
    line-height: 1.6;
    color: #3A3F4B;
    max-width: 46rem;
}
.lab-button {
    display: inline-block;
    margin: 0 0.6rem 0.4rem 0;
    padding: 0.7rem 1.3rem;
    border-radius: 8px;
    background: #C0261C;
    color: #FFFFFF !important;
    font-weight: 600;
    text-decoration: none !important;
}
.lab-button:hover, .lab-button:focus-visible { background: #8F1D15; }
.lab-button.dark { background: #24292F; }
.lab-button.dark:hover, .lab-button.dark:focus-visible { background: #000000; }

/* ---------- "elsewhere" links (Home) ---------- */
.lab-link-row {
    display: flex;
    align-items: center;
    gap: 1.1rem;
    padding: 0.55rem 0;
}
.lab-link-icon {
    flex: 0 0 3.4rem;
    height: 3.4rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    font-size: 1.5rem;
}
.lab-link-row a { color: #FFFFFF; font-weight: 700; font-size: 1.15rem; text-decoration: none; }
.lab-link-row a:hover, .lab-link-row a:focus-visible { text-decoration: underline; }
.lab-link-row p { margin: 0.1rem 0 0 0; color: var(--lab-muted); font-size: 0.95rem; }

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

/* ---------- feature tiles (Home) ---------- */
.lab-tile { padding: 0.2rem 0.2rem 0.6rem 0.2rem; }
.lab-tile-icon { font-size: 1.7rem; line-height: 1; margin-bottom: 0.6rem; }
.lab-tile h3 { margin: 0 0 0.35rem 0; padding: 0; font-size: 1.05rem; line-height: 1.3; }
.lab-tile p { margin: 0; color: var(--lab-muted); font-size: 0.93rem; line-height: 1.5; }

/* ---------- footer (Home) ---------- */
.lab-footer {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 0.6rem 1.6rem;
    margin-top: 3rem;
    padding: 1.4rem 0 0.4rem 0;
    border-top: 1px solid var(--lab-border);
    color: var(--lab-muted);
    font-size: 0.9rem;
}
.lab-footer-links { display: flex; flex-wrap: wrap; gap: 0.4rem 1.3rem; }
.lab-footer-copy { width: 100%; margin-top: 0.4rem; font-size: 0.85rem; }
.lab-footer a { color: var(--lab-accent-text); text-decoration: none; }
.lab-footer a:hover, .lab-footer a:focus-visible { text-decoration: underline; }

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
    .lab-hero h1 { font-size: 2.1rem; }
    .lab-hero p { font-size: 1rem; }
    .lab-step { font-size: 0.8rem; padding: 0.22rem 0.6rem; }
    .lab-community { padding: 1.4rem 1.2rem; }
    .lab-community h3 { font-size: 1.5rem; }
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
    return "".join(
        f'<span class="lab-chip">{html.escape(name)}</span>' for name in names
    )
