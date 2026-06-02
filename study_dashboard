import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & CUTE AESTHETICS 🌸
# ==========================================
st.set_page_config(page_title="Moral Philosophy Rescue! ✨", layout="wide", page_icon="💖")

st.markdown("""
    <style>
    .big-font { font-size:30px !important; color: #FF69B4; font-weight: bold; }
    .cute-box { background-color: #FFF0F5; padding: 15px; border-radius: 10px; border: 2px solid #FFB6C1; margin-bottom: 20px;}
    .vocab-box { background-color: #E6E6FA; padding: 10px; border-radius: 5px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE (PROGRESS TRACKING)
# ==========================================
if 'progress' not in st.session_state:
    st.session_state.progress = 0

# Randomize questions on load/refresh
if 'q_sample' not in st.session_state:
    st.session_state.q_sample = [0, 1]

def refresh_questions():
    st.session_state.q_sample = random.sample([0, 1, 2], 2)

def advance_progress():
    st.session_state.progress += 1
    refresh_questions()
    st.balloons()

# ==========================================
# DATA: CONTENT & QUIZZES
# ==========================================
# Quiz Banks (3 questions per section, we will sample 2 randomly each time)
quizzes = {
    0: [ # IBE
        {"q": "In IBE, what does the 'F' stand for?", "options": ["A seeming fact", "A false assumption", "A future event"], "a": "A seeming fact"},
        {"q": "True/False: If we find a secret tunnel in the prison escape case, it undermines the explanation that Guard Nigel let the prisoner out.", "options": ["True", "False"], "a": "True"},
        {"q": "In Singer's Pond case, his moral principle is used as the 'E' (Explanation) for what?", "options": ["Why justice is greater than decency", "Why we are morally obligated to save the drowning child", "Why prison breaks happen"], "a": "Why we are morally obligated to save the drowning child"}
    ],
    1: [ # Thomson
        {"q": "According to Thomson, moral requirements grounded in 'moral rights' are called requirements of:", "options": ["Decency", "Justice", "Explanation"], "a": "Justice"},
        {"q": "True/False: Thomson argues that justice is ALWAYS weightier and more forceful than decency.", "options": ["True", "False"], "a": "False"},
        {"q": "If I refuse to throw you my life preserver when you are drowning, Thomson says I am acting:", "options": ["Unjustly", "Indecently, but not unjustly", "Both unjustly and indecently"], "a": "Indecently, but not unjustly"}
    ],
    2: [ # Marquis
        {"q": "What is Marquis' primary explanation for why killing is wrong?", "options": ["It deprives the victim of a valuable future like ours", "It violates the victim's personhood", "It violates human DNA rights"], "a": "It deprives the victim of a valuable future like ours"},
        {"q": "True/False: Marquis' argument focuses heavily on proving that a fetus is legally a 'person'.", "options": ["True", "False"], "a": "False"},
        {"q": "The 'Circle of Death' challenge argues that a fetus's future is different from an adult's because:", "options": ["A fetus doesn't have DNA yet", "A fetus relies on the mother's body to even REACH its future", "Adults don't have valuable futures"], "a": "A fetus relies on the mother's body to even REACH its future"}
    ]
}

# ==========================================
# SIDEBAR: PROGRESS & APPENDIX
# ==========================================
with st.sidebar:
    st.title("🌱 Growing Brain!")
    progress_percent = int((st.session_state.progress / 3) * 100)
    st.progress(st.session_state.progress / 3)
    st.write(f"**Course Progress: {progress_percent}%**")
    
    st.markdown("---")
    st.header("📚 Appendix & Vocab")
    
    if st.session_state.progress >= 0:
        st.markdown("<div class='vocab-box'><b>IBE:</b> Inference to the Best Explanation. Consists of a seeming fact (F) and the best candidate explanation (E).</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Singer's Pond Case:</b> Example showing you're obligated to prevent something bad if it doesn't cost you something nearly as important.</div>", unsafe_allow_html=True)
        
    if st.session_state.progress >= 1:
        st.markdown("<div class='vocab-box'><b>Justice (Thomson):</b> Moral requirements based on moral rights.</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Decency (Thomson):</b> Moral requirements based on moral reasons OTHER than rights.</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Water Bottle vs. Drowning Case:</b> Proves decency can sometimes outweigh justice.</div>", unsafe_allow_html=True)

    if st.session_state.progress >= 2:
        st.markdown("<div class='vocab-box'><b>Marquis Principle:</b> The idea that there is a big moral reason against depriving something of its valuable future (VFP).</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Circle of Death Challenge:</b> The counter-argument that a fetus doesn't inherently 'have' a future yet because it requires the mother's body to achieve it.</div>", unsafe_allow_html=True)

    if st.session_state.progress == 3:
        st.success("🎉 YOU ARE READY FOR THIS EXAM!")

# ==========================================
# MAIN CONTENT AREA
# ==========================================
st.markdown('<p class="big-font">✨ Moral Philosophy Exam Rescue ✨</p>', unsafe_allow_html=True)
st.write("Take a deep breath! We are going to master IBE, Thomson, and Marquis. Read the fun summaries, then pass the checkpoint quizzes to unlock the next section. You've got this! 💖")

# ------------------------------------------
# SECTION 1: IBE
# ------------------------------------------
if st.session_state.progress >= 0:
    st.header("🔍 Checkpoint 1: Inference to the Best Explanation (IBE)")
    st.markdown("""
    <div class='cute-box'>
    <b>What is IBE?</b><br>
    Think of yourself as a detective. You see something that seems to be a fact (we call this <b>F</b>). You brainstorm a bunch of reasons why this fact exists (we call these Candidate Explanations, or <b>E</b>). If one explanation (let's say E3) is the absolute <i>best</i> explanation for the fact, then you have a good reason to believe E3 is true!<br><br>
    <b>The Prison Break Example 🚨:</b><br>
    <b>F (Fact):</b> Prisoner Smith was locked in a super-secure steel cell at 7pm, but at 5am, he's gone.<br>
    <b>E (Explanation):</b> The lone night guard, Nigel, let him out.<br>
    If there are no secret tunnels or broken locks, Nigel letting him out is the <i>best explanation</i> for the missing prisoner.<br><br>
    <b>Singer's Pond Example 🦆:</b><br>
    <b>F (Fact):</b> It seems like a fact that you are morally obligated to save a drowning child.<br>
    <b>E (Explanation):</b> Singer's Principle: "If you can prevent something bad from happening without sacrificing anything nearly as important, you have to do it."<br>
    Singer argues his principle is the best explanation for our moral obligation in the pond case!
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.progress == 0:
        st.subheader("📝 Checkpoint 1 Quiz")
        q_idx_1, q_idx_2 = st.session_state.q_sample[0], st.session_state.q_sample[1]
        
        ans1 = st.radio(quizzes[0][q_idx_1]["q"], quizzes[0][q_idx_1]["options"], index=None, key="1_1")
        ans2 = st.radio(quizzes[0][q_idx_2]["q"], quizzes[0][q_idx_2]["options"], index=None, key="1_2")
        
        if st.button("Submit Checkpoint 1 ✨"):
            if ans1 == quizzes[0][q_idx_1]["a"] and ans2 == quizzes[0][q_idx_2]["a"]:
                st.success("Correct! You unlocked the next section!")
                advance_progress()
                st.rerun()
            else:
                st.error("Oops! Not quite. Try again! (The questions might change! 🔄)")
                refresh_questions()
                st.rerun()

# ------------------------------------------
# SECTION 2: THOMSON
# ------------------------------------------
if st.session_state.progress >= 1:
    st.markdown("---")
    st.header("⚖️ Checkpoint 2: Thomson on Rights vs. Decency")
    st.markdown("""
    <div class='cute-box'>
    <b>Justice vs. Decency 🦋</b><br>
    Thomson wants us to understand that "morally impermissible" behavior falls into two categories:<br>
    1. <b>Justice:</b> Based on Moral Rights. (e.g., You stole my water bottle. I have a right to it. You acted unjustly).<br>
    2. <b>Decency:</b> Based on other moral reasons, NOT rights. (e.g., You refuse to throw a life preserver to a drowning person. They don't technically have a "right" to your property, so it's not unjust, but it is deeply <i>indecent</i>).<br><br>
    <b>Which is stronger? 💪</b><br>
    It's tempting to think Justice (rights) is always weightier than Decency. Thomson says <b>NOPE!</b> In the example above, the requirement of decency (saving a drowning life) is intuitively way weightier than the requirement of justice (giving back a stolen water bottle). <br><br>
    <b>What does this mean for Abortion? 🤰</b><br>
    Thomson believes women have moral rights over their bodies. Even if a fetus is removed, it doesn't necessarily mean the mother violated a right (acted unjustly). She might just be refusing to be a "Good Samaritan", which Thomson argues falls under decency, not justice. And women aren't morally required to make huge, massive sacrifices just for decency.
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.progress == 1:
        st.subheader("📝 Checkpoint 2 Quiz")
        q_idx_1, q_idx_2 = st.session_state.q_sample[0], st.session_state.q_sample[1]
        
        ans1 = st.radio(quizzes[1][q_idx_1]["q"], quizzes[1][q_idx_1]["options"], index=None, key="2_1")
        ans2 = st.radio(quizzes[1][q_idx_2]["q"], quizzes[1][q_idx_2]["options"], index=None, key="2_2")
        
        if st.button("Submit Checkpoint 2 ✨"):
            if ans1 == quizzes[1][q_idx_1]["a"] and ans2 == quizzes[1][q_idx_2]["a"]:
                st.success("Nailed it! Last section unlocked! 🎉")
                advance_progress()
                st.rerun()
            else:
                st.error("Uh oh! Give it another shot! (Questions mixed up! 🔄)")
                refresh_questions()
                st.rerun()

# ------------------------------------------
# SECTION 3: MARQUIS
# ------------------------------------------
if st.session_state.progress >= 2:
    st.markdown("---")
    st.header("🕰️ Checkpoint 3: Marquis & The 'Circle of Death'")
    st.markdown("""
    <div class='cute-box'>
    <b>The Marquis Principle 🌟</b><br>
    Marquis bypasses the messy argument about whether a fetus is a "person" or a "human being." Instead, he says killing is wrong because it deprives a victim of a <b>Valuable Future Like Ours</b> (let's call it VFP). Because a fetus has a valuable future identical to a young child's, he argues abortion is prima facie (at first glance) seriously morally wrong.<br><br>
    <b>The Challenge: The "Circle of Death" 🔄☠️</b><br>
    Here is a huge hole poked in Marquis' argument by your professor's handout:<br>
    To deprive someone of a valuable future, they must actually <i>have</i> that future to begin with. You can't deprive me of an Olympic Gold Medal because I don't have one! <br>
    In ordinary killings (like shooting an adult), the adult <i>would have</i> reached their future if the killer just left them alone. 
    But a fetus is different. A fetus <b>needs to use the mother's body</b> to survive and reach its future. <br><br>
    So, it's not like killing an adult who is doing perfectly fine on their own; it's more like pulling someone out of a burning building. Therefore, the mother gets stuck in a "circle of death" logic loop: she needs to know if the fetus has a valuable future to know if abortion is permissible, but the fetus only <i>gets</i> that valuable future if she decides to help it!
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.progress == 2:
        st.subheader("📝 Final Checkpoint Quiz!")
        q_idx_1, q_idx_2 = st.session_state.q_sample[0], st.session_state.q_sample[1]
        
        ans1 = st.radio(quizzes[2][q_idx_1]["q"], quizzes[2][q_idx_1]["options"], index=None, key="3_1")
        ans2 = st.radio(quizzes[2][q_idx_2]["q"], quizzes[2][q_idx_2]["options"], index=None, key="3_2")
        
        if st.button("Submit Final Checkpoint 🏆"):
            if ans1 == quizzes[2][q_idx_1]["a"] and ans2 == quizzes[2][q_idx_2]["a"]:
                st.success("YOU DID IT! YOU ARE READY FOR YOUR EXAM! 🎊")
                advance_progress()
                st.rerun()
            else:
                st.error("So close! Try again! 🔄")
                refresh_questions()
                st.rerun()

# ------------------------------------------
# COMPLETION
# ------------------------------------------
if st.session_state.progress >= 3:
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: #FF69B4;'>🎊 100% COMPLETED! GO ACE THAT EXAM! 🎊</h2>", unsafe_allow_html=True)
    if st.button("Reset Dashboard & Study Again 🔄"):
        st.session_state.progress = 0
        st.rerun()
