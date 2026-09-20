import random
import streamlit as st

st.set_page_config(page_title="Guess Quest", page_icon="🎯", layout="wide", initial_sidebar_state="collapsed")

LEVELS = [
    {"name":"Rookie Range", "emoji":"🌱", "low":1, "high":10, "attempts":5, "points":100},
    {"name":"Cipher Cave", "emoji":"🔐", "low":1, "high":25, "attempts":6, "points":200},
    {"name":"Shadow Vault", "emoji":"🌑", "low":1, "high":50, "attempts":7, "points":350},
    {"name":"Final Core", "emoji":"👑", "low":1, "high":100, "attempts":8, "points":500},
]

for k, v in {
    "page": "landing",
    "username": "",
    "stage": 1,
    "secret_number": random.randint(1, 50),
    "attempts": 0,
    "game_over": False,
    "final_won": False,
    "challenge_a": random.randint(2, 10),
    "challenge_b": random.randint(2, 10),
    "pattern_a": random.randint(1, 5),
    "pattern_b": random.randint(2, 6),
    "pattern_completed": False,
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

ATTEMPTS = 3

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


def start_stage_one():
    st.session_state.stage = 1
    st.session_state.secret_number = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.final_won = False


def start_final_stage():
    st.session_state.stage = 5
    st.session_state.secret_number = random.randint(1, 30)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.final_won = False


def start_pattern_stage():
    st.session_state.stage = 3
    st.session_state.pattern_a = random.randint(1, 5)
    st.session_state.pattern_b = random.randint(2, 6)
    st.session_state.pattern_completed = False


def start_stage_four():
    st.session_state.stage = 4
    st.session_state.challenge_a = random.randint(2, 10)
    st.session_state.challenge_b = random.randint(2, 10)


def restart_game():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.stage = 1
    st.session_state.secret_number = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.final_won = False
    st.session_state.challenge_a = random.randint(2, 10)
    st.session_state.challenge_b = random.randint(2, 10)
    st.session_state.pattern_a = random.randint(1, 5)
    st.session_state.pattern_b = random.randint(2, 6)
    st.session_state.pattern_completed = False
    st.session_state.page = "landing"


def show_stage_one():
    st.success(f"Welcome, **{st.session_state.username}**!")
    st.write("I have selected a number between 1 to 50.")

    guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.warning("📉 Too low! Try a higher number.")
        elif guess > st.session_state.secret_number:
            st.warning("📈 Too high! Try a lower number.")
        else:
            st.session_state.game_over = True
            st.success(
                f"🎉 Congratulations **{st.session_state.username}**! "
                f"You guessed the number in **{st.session_state.attempts} attempts**."
            )
            st.balloons()

    if st.session_state.game_over:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Play Again"):
                start_stage_one()
                st.rerun()
        with col2:
            if st.button("Next Stage"):
                st.session_state.stage = 2
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
        agree_checkbox = st.checkbox("I understand the rules and choose to continue.")
        continue_button = st.form_submit_button("I AGREE - ENTER IF YOU DARE")
        if continue_button:
            if agree_checkbox:
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

    with st.form("Pattern form"):
        answer = st.number_input("Enter a missing answer:", min_value=0, step=1)
        submit = st.form_submit_button("Verify Pattern")
        if submit:
            correct_answer = next_a**2 + next_b**2
            if answer == correct_answer:
                st.session_state.pattern_completed = True
                st.success("✅ Verification successful!")
                start_stage_four()
                st.rerun()
            else:
                st.error("❌ Incorrect pattern. Look carefully and try again.")


def show_stage_four():
    a = st.session_state.challenge_a
    b = st.session_state.challenge_b
    correct_answer = (a + b) ** 2

    st.info(f"If $a = {a}$ and $b = {b}$, What is the value of **(a+b)²**?")

    with st.form("verification_form"):
        answer = st.number_input("Enter your answer:", min_value=0, step=1)
        submit = st.form_submit_button("Verify")
        if submit:
            if answer == correct_answer:
                st.success("✅ Verification successful!")
                start_final_stage()
                st.rerun()
            else:
                st.error("❌ Incorrect answer. Try again.")


def show_final_stage():
    st.subheader("💀 FINAL STAGE")
    st.warning(f"⚠️ You have ONLY {ATTEMPTS} chances!")
    st.write("I have selected a number between 1 to 30")

    if not st.session_state.game_over:
        guess = st.number_input("Enter your final guess:", min_value=1, max_value=30, step=1)

        if st.button("☠️ GUESS"):
            st.session_state.attempts += 1

            if guess == st.session_state.secret_number:
                st.session_state.final_won = True
                st.session_state.game_over = True
                st.success(f"🎉🏆 CONGRATULATIONS **{st.session_state.username}**!")
                st.success("YOU COMPLETED THE GAME!")
                st.balloons()

            elif st.session_state.attempts >= ATTEMPTS:
                st.session_state.game_over = True
                st.error("💀 YOU FAILED THE FINAL STAGE.")
                st.write(f"The number was **{st.session_state.secret_number}**.")

            elif guess < st.session_state.secret_number:
                remaining = ATTEMPTS - st.session_state.attempts
                st.warning(f"📉 Too low! You have **{remaining} chances** left.")

            else:
                remaining = ATTEMPTS - st.session_state.attempts
                st.warning(f"📈 Too high! You have **{remaining} chances** left.")

    else:
        if st.session_state.final_won:
            st.success(f"🎉🏆 Congratulations **{st.session_state.username}**!")
            st.success("***You successfully completed all Stages.***")
        else:
            st.error("GAME OVER!")
            st.write(f"Attempts used: **{st.session_state.attempts}/{ATTEMPTS}**")
            st.divider()
            st.subheader(f"{st.session_state.username}! BETTER LUCK NEXT TIME")
            st.error("SYSTEM FAILURE")

            if st.button("Restart Game"):
                restart_game()
                st.rerun()


def css():
    st.markdown('''<style>
    .stApp{background:radial-gradient(circle at 20% 10%,#18264d 0,#080d1c 38%,#040611 100%);color:#fff}
    [data-testid="stHeader"]{background:transparent}.block-container{max-width:1100px;padding-top:2rem}
    .hero{padding:55px 35px;text-align:center;border:1px solid #2d3c66;border-radius:28px;background:linear-gradient(135deg,rgba(24,38,77,.75),rgba(9,13,31,.88));box-shadow:0 20px 70px rgba(0,0,0,.35)}
    .hero h1{font-size:4.2rem;margin:0;background:linear-gradient(90deg,#7dd3fc,#c4b5fd,#f0abfc);-webkit-background-clip:text;color:transparent;font-weight:900}
    .hero p{font-size:1.2rem;color:#b7c1dc}.badge{display:inline-block;padding:7px 14px;border-radius:999px;background:#18264d;color:#8ddcff;font-weight:700}
    .card{padding:22px;border:1px solid #29375f;border-radius:20px;background:rgba(14,20,42,.75);margin-bottom:16px}.big{font-size:2.2rem;font-weight:800}
    .progress{height:12px;background:#1b2644;border-radius:20px;overflow:hidden}.fill{height:100%;background:linear-gradient(90deg,#60a5fa,#c084fc);border-radius:20px}
    .hint{padding:14px 18px;border-left:4px solid #60a5fa;background:#101a34;border-radius:10px;color:#cbd5f1}
    </style>''',unsafe_allow_html=True)
css()


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


if st.session_state.page=="landing":
    st.markdown('<div class="hero"><span class="badge">🎮 PYTHON • STREAMLIT • 5 STAGES</span><h1>GUESS QUEST</h1><p>Crack the number. Clear every stage. Claim the crown.</p></div>',unsafe_allow_html=True)
    st.write("")
    c1,c2,c3=st.columns(3)
    c1.markdown('<div class="card"><div class="big">🎯</div><b>Smart Challenges</b><br><span style="color:#aab5d3">Numbers get harder every level.</span></div>',unsafe_allow_html=True)
    c2.markdown('<div class="card"><div class="big">⚡</div><b>Limited Attempts</b><br><span style="color:#aab5d3">Think fast and use the clues.</span></div>',unsafe_allow_html=True)
    c3.markdown('<div class="card"><div class="big">🏆</div><b>Final Victory</b><br><span style="color:#aab5d3">Complete all stages to win.</span></div>',unsafe_allow_html=True)
    if st.button("🚀 ENTER THE QUEST",use_container_width=True,type="primary"):
        st.session_state.page="login"; st.rerun()

elif st.session_state.page=="login":
    st.markdown('<div class="hero"><span class="badge">PLAYER ACCESS</span><h1 style="font-size:3rem">Ready, Challenger?</h1><p>Enter your player name to begin your journey.</p></div>',unsafe_allow_html=True)
    with st.form("login"):
        name=st.text_input("Player name",placeholder="Enter your username")
        submitted=st.form_submit_button("🎮 START GAME",use_container_width=True,type="primary")
        if submitted:
            if name.strip():
                st.session_state.username=name.strip(); start_stage_one(); st.session_state.page="game"; st.rerun()
            else: st.error("Please enter a player name.")
    if st.button("← Back"): st.session_state.page="landing"; st.rerun()

elif st.session_state.page=="game":

    show_stage_hero(st.session_state.stage)

    if st.session_state.stage == 1:
        show_stage_one()
    elif st.session_state.stage == 2:
        show_stage_two()
    elif st.session_state.stage == 3:
        show_pattern_stage()
    elif st.session_state.stage == 4:
        show_stage_four()
    elif st.session_state.stage == 5:
        show_final_stage()

else:
    st.markdown('<div class="hero"><div style="font-size:5rem">🏆</div><h1>VICTORY!</h1><p>You conquered every stage of Guess Quest.</p></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="card" style="text-align:center"><div class="big">{st.session_state.username}</div><p style="color:#aab5d3">FINAL SCORE</p><div style="font-size:4rem;font-weight:900">{st.session_state.score} XP</div><p>🌱 Stage 1 → 🧠 Stage 2 → 🔢 Stage 3 → 👁️ Stage 4 → 💀 Stage 5</p></div>',unsafe_allow_html=True)
    if st.button("🎮 PLAY AGAIN",use_container_width=True,type="primary"):
        start_stage_one(); st.session_state.page="game"; st.rerun()
    if st.button("🏠 HOME",use_container_width=True): st.session_state.page="landing"; st.rerun()
