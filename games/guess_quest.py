import html
import random

import streamlit as st

st.set_page_config(
    page_title="Guess Quest",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ATTEMPTS = 3  

POINTS = {"stage_1": 100, "pattern": 200, "verify": 200, "final": 300}
BONUS_PER_SPARE_ATTEMPT = 50 

PATTERN_RANGE = (1, 9)

DEFAULT_HERO = {
    "emoji": "🎯",
    "title": "GUESS QUEST",
    "text": "Complete all five stages to claim the crown.",
}
STAGE_HEROES = {
    2: {"emoji": "", "title": "INSTRUCTIONS READ BEFORE YOU ENTER", "text": ""},
    3: {"emoji": "🧠", "title": "Pattern Challenge", "text": ""},
    4: {
        "emoji": "👁️",
        "title": "Now the real challenge begins",
        "text": "Before entering the final stage, solve this verification challenge.",
    },
}

CSS = """
<style>
.stApp{background:radial-gradient(circle at 20% 10%,#18264d 0,#080d1c 38%,#040611 100%);color:#fff}
[data-testid="stHeader"]{background:transparent}
.block-container{max-width:1100px;padding-top:2rem}
.hero{padding:55px 35px;text-align:center;border:1px solid #2d3c66;border-radius:28px;background:linear-gradient(135deg,rgba(24,38,77,.75),rgba(9,13,31,.88));box-shadow:0 20px 70px rgba(0,0,0,.35)}
.hero h1{font-size:4.2rem;margin:0;background:linear-gradient(90deg,#7dd3fc,#c4b5fd,#f0abfc);-webkit-background-clip:text;color:transparent;font-weight:900}
.hero p{font-size:1.2rem;color:#b7c1dc}
.badge{display:inline-block;padding:7px 14px;border-radius:999px;background:#18264d;color:#8ddcff;font-weight:700}
.card{padding:22px;border:1px solid #29375f;border-radius:20px;background:rgba(14,20,42,.75);margin-bottom:16px}
.big{font-size:2.2rem;font-weight:800}
.progress{height:12px;background:#1b2644;border-radius:20px;overflow:hidden}
.fill{height:100%;background:linear-gradient(90deg,#60a5fa,#c084fc);border-radius:20px}
.hint{padding:14px 18px;border-left:4px solid #60a5fa;background:#101a34;border-radius:10px;color:#cbd5f1}
</style>
"""


def new_run_state():
    """Fresh values for one playthrough (everything except page and username)."""
    return {
        "stage": 1,
        "secret_number": random.randint(1, 50),
        "attempts": 0,
        "game_over": False,
        "challenge_a": random.randint(2, 10),
        "challenge_b": random.randint(2, 10),
        "pattern_a": random.randint(*PATTERN_RANGE),
        "pattern_b": random.randint(*PATTERN_RANGE),
        "score": 0,
    }


def init_state():
    defaults = {"page": "landing", "username": "", **new_run_state()}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_run():
    for key, value in new_run_state().items():
        st.session_state[key] = value


def restart_game():
    reset_run()
    st.session_state.username = ""
    st.session_state.page = "landing"


def award(points):
    st.session_state.score += points


def flash(message, kind="success"):
    """Queue a message to show after the next rerun.

    A message shown right before st.rerun() is wiped by the rerun, so we store
    it in session state and display it at the top of the next screen instead.
    `kind` is the name of the st function to use: "success", "error", ...
    """
    st.session_state.flash = (kind, message)


def show_flash():
    item = st.session_state.pop("flash", None)
    if item:
        kind, message = item
        getattr(st, kind)(message)


def show_balloons_once():
    """Balloons are requested with a flag so they survive the st.rerun()."""
    if st.session_state.pop("celebrate", False):
        st.balloons()


def start_stage_one():
    st.session_state.stage = 1
    st.session_state.secret_number = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False


def new_pattern_numbers():
    """Pick the two starting numbers for the pattern, never the same pair as last time."""
    previous = (st.session_state.get("pattern_a"), st.session_state.get("pattern_b"))
    while True:
        pair = (random.randint(*PATTERN_RANGE), random.randint(*PATTERN_RANGE))
        if pair != previous:
            return pair


def start_pattern_stage():
    st.session_state.stage = 3
    st.session_state.pattern_a, st.session_state.pattern_b = new_pattern_numbers()


def start_stage_four():
    st.session_state.stage = 4
    st.session_state.challenge_a = random.randint(2, 10)
    st.session_state.challenge_b = random.randint(2, 10)


def start_final_stage():
    st.session_state.stage = 5
    st.session_state.secret_number = random.randint(1, 30)
    st.session_state.attempts = 0
    st.session_state.game_over = False


def show_stage_one():
    name = st.session_state.username
    st.success(f"Welcome, **{name}**!")
    st.write("I have selected a number between 1 to 50.")

    if st.session_state.game_over:
        attempts = st.session_state.attempts
        word = "attempt" if attempts == 1 else "attempts"
        st.success(
            f"🎉 Congratulations **{name}**! "
            f"You guessed the number in **{attempts} {word}**."
        )
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Play Again"):
                start_stage_one()
                st.rerun()
        with col2:
            if st.button("Next Stage"):
                award(POINTS["stage_1"])
                st.session_state.stage = 2
                st.rerun()
        return

    guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        secret = st.session_state.secret_number

        if guess < secret:
            st.warning("📉 Too low! Try a higher number.")
        elif guess > secret:
            st.warning("📈 Too high! Try a lower number.")
        else:
            st.session_state.game_over = True
            st.session_state.celebrate = True
            st.rerun()


def show_stage_two():
    st.success("🎉 Congratulations! You're moving to the next level, your next opponent is You.")
    st.write("**1. You have successfully completed the first stage.**")
    st.write("**2. The challenges are getting harder.**")
    st.write("**3. One wrong decision could end your run.**")
    st.write("**4. Your next opponent is not the computer... it is YOU.**")
    st.write("**5. Stay focused. Stay calm. Trust your decisions.**")
    st.write(f"**Good luck {st.session_state.username}.**")

    with st.form("stage_two_form"):
        agree = st.checkbox("I understand the rules and choose to continue.")
        continue_button = st.form_submit_button("I AGREE - ENTER IF YOU DARE")

    if continue_button:
        if agree:
            start_pattern_stage()
            st.rerun()
        else:
            st.error("You must accept the rules before continuing.")


def show_pattern_stage():
    a = st.session_state.pattern_a
    b = st.session_state.pattern_b

    st.write(f"1. {a} + {b} = {a**2 + b**2}")
    st.write(f"2. {a + 1} + {b + 1} = {(a + 1)**2 + (b + 1)**2}")
    st.write(f"3. {a + 2} + {b + 2} = {(a + 2)**2 + (b + 2)**2}")

    next_a = a + 3
    next_b = b + 3
    st.write(f"4. {next_a} + {next_b} = ?")

    with st.form("pattern_form"):
        answer = st.number_input("Enter a missing answer:", min_value=0, step=1)
        submit = st.form_submit_button("Verify Pattern")

    if submit:
        if answer == next_a**2 + next_b**2:
            award(POINTS["pattern"])
            flash("✅ Pattern verified!")
            start_stage_four()
            st.rerun()
        else:
            st.session_state.pattern_a, st.session_state.pattern_b = new_pattern_numbers()
            flash("❌ Incorrect pattern. Here is a new one - look carefully!", "error")
            st.rerun()


def show_stage_four():
    a = st.session_state.challenge_a
    b = st.session_state.challenge_b

    st.info(f"If $a = {a}$ and $b = {b}$, What is the value of **(a+b)²**?")

    with st.form("verification_form"):
        answer = st.number_input("Enter your answer:", min_value=0, step=1)
        submit = st.form_submit_button("Verify")

    if submit:
        if answer == (a + b) ** 2:
            award(POINTS["verify"])
            flash("✅ Verification successful!")
            start_final_stage()
            st.rerun()
        else:
            st.error("❌ Incorrect answer. Try again.")


def show_final_stage():
    st.subheader("💀 FINAL STAGE")

    if st.session_state.game_over:
        st.error("GAME OVER!")
        st.write(f"The number was **{st.session_state.secret_number}**.")
        st.write(f"Attempts used: **{st.session_state.attempts}/{ATTEMPTS}**")
        st.divider()
        st.subheader(f"{st.session_state.username}! BETTER LUCK NEXT TIME")
        st.error("SYSTEM FAILURE")

        if st.button("Restart Game"):
            restart_game()
            st.rerun()
        return

    st.warning(f"⚠️ You have ONLY {ATTEMPTS} chances!")
    st.write("I have selected a number between 1 to 30")

    guess = st.number_input("Enter your final guess:", min_value=1, max_value=30, step=1)

    if st.button("☠️ GUESS"):
        st.session_state.attempts += 1
        secret = st.session_state.secret_number
        remaining = ATTEMPTS - st.session_state.attempts

        if guess == secret:
            award(POINTS["final"] + BONUS_PER_SPARE_ATTEMPT * remaining)
            st.session_state.celebrate = True
            st.session_state.page = "victory"
            st.rerun()
        elif remaining <= 0:
            st.session_state.game_over = True
            st.rerun()
        elif guess < secret:
            st.warning(f"📉 Too low! You have **{remaining} chances** left.")
        else:
            st.warning(f"📈 Too high! You have **{remaining} chances** left.")


def show_stage_hero(stage):
    """Draw the big banner at the top of the game page for the given stage."""
    hero = STAGE_HEROES.get(stage, DEFAULT_HERO)
    emoji = f'<div style="font-size:3rem">{hero["emoji"]}</div>' if hero["emoji"] else ""
    text = f'<p>{hero["text"]}</p>' if hero["text"] else ""
    size = "3rem" if stage in (1, 5) else "2.4rem"
    st.markdown(
        f'<div class="hero">{emoji}<h1 style="font-size:{size}">{hero["title"]}</h1>{text}</div>',
        unsafe_allow_html=True,
    )


def show_landing():
    st.markdown(
        '<div class="hero"><span class="badge">🎮 PYTHON • STREAMLIT • 5 STAGES</span>'
        "<h1>GUESS QUEST</h1>"
        "<p>Crack the number. Clear every stage. Claim the crown.</p></div>",
        unsafe_allow_html=True,
    )
    st.write("")

    cards = [
        ("🎯", "Smart Challenges", "Numbers get harder every level."),
        ("⚡", "Limited Attempts", "Think fast and use the clues."),
        ("🏆", "Final Victory", "Complete all stages to win."),
    ]
    for column, (icon, title, text) in zip(st.columns(3), cards):
        column.markdown(
            f'<div class="card"><div class="big">{icon}</div><b>{title}</b><br>'
            f'<span style="color:#aab5d3">{text}</span></div>',
            unsafe_allow_html=True,
        )

    if st.button("🚀 ENTER THE QUEST", width="stretch", type="primary"):
        st.session_state.page = "login"
        st.rerun()


def show_login():
    st.markdown(
        '<div class="hero"><span class="badge">PLAYER ACCESS</span>'
        '<h1 style="font-size:3rem">Ready, Challenger?</h1>'
        "<p>Enter your player name to begin your journey.</p></div>",
        unsafe_allow_html=True,
    )

    with st.form("login"):
        name = st.text_input("Player name", placeholder="Enter your username", max_chars=20)
        submitted = st.form_submit_button("🎮 START GAME", width="stretch", type="primary")

    if submitted:
        if name.strip():
            reset_run()
            st.session_state.username = name.strip()
            st.session_state.page = "game"
            st.rerun()
        else:
            st.error("Please enter a player name.")

    if st.button("← Back"):
        st.session_state.page = "landing"
        st.rerun()


def show_game():
    show_stage_hero(st.session_state.stage)
    show_flash()
    show_balloons_once()

    stages = {
        1: show_stage_one,
        2: show_stage_two,
        3: show_pattern_stage,
        4: show_stage_four,
        5: show_final_stage,
    }
    stages[st.session_state.stage]()


def show_victory():
    show_balloons_once()

    name = html.escape(st.session_state.username)

    st.markdown(
        '<div class="hero"><div style="font-size:5rem">🏆</div><h1>VICTORY!</h1>'
        "<p>You conquered every stage of Guess Quest.</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="card" style="text-align:center"><div class="big">{name}</div>'
        '<p style="color:#aab5d3">FINAL SCORE</p>'
        f'<div style="font-size:4rem;font-weight:900">{st.session_state.score} XP</div>'
        "<p>🌱 Stage 1 → 🧠 Stage 2 → 🔢 Stage 3 → 👁️ Stage 4 → 💀 Stage 5</p></div>",
        unsafe_allow_html=True,
    )

    if st.button("🎮 PLAY AGAIN", width="stretch", type="primary"):
        reset_run()
        st.session_state.page = "game"
        st.rerun()
    if st.button("🏠 HOME", width="stretch"):
        restart_game()
        st.rerun()


def main():
    init_state()
    st.markdown(CSS, unsafe_allow_html=True)

    pages = {
        "landing": show_landing,
        "login": show_login,
        "game": show_game,
        "victory": show_victory,
    }
    page = pages.get(st.session_state.page)
    if page is None:  
        st.session_state.page = "landing"
        st.rerun()
    page()


if __name__ == "__main__":
    main()
