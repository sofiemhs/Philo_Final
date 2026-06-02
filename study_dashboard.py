import streamlit as st
import random

# ==========================================
# PAGE CONFIGURATION & CUTE AESTHETICS 🌸
# ==========================================
st.set_page_config(page_title="Moral Philosophy Rescue! ✨", layout="wide", page_icon="💖")

# We are forcing a bright, cute theme and ensuring ALL text has high contrast 
# so nothing gets lost if Streamlit defaults to a dark/grey background.
st.markdown("""
    <style>
    /* Force the main background to a warm, cheerful cream/pink color so there is no sad grey */
    .stApp {
        background-color: #FFF9FA;
    }
    
    /* Force all default text to a highly readable dark grey/black */
    html, body, p, div, span, label, li {
        color: #2E2E2E !important;
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #8B008B !important; 
        font-weight: 800 !important;
    }

    .big-font { 
        font-size:36px !important; 
        color: #FF1493 !important; 
        font-weight: 900; 
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(255,105,180,0.3);
    }
    
    .cute-box { 
        background-color: #FFF0F5; 
        color: #330019 !important; /* Very dark pink/black for high contrast */
        padding: 25px; 
        border-radius: 15px; 
        border: 3px solid #FFB6C1; 
        margin-bottom: 25px;
        box-shadow: 3px 3px 15px rgba(255, 182, 193, 0.4);
        line-height: 1.6;
        font-size: 17px;
    }
    
    .vocab-box { 
        background-color: #F8F8FF; /* Ghost white */
        color: #190033 !important; /* Very dark purple for high contrast */
        padding: 15px; 
        border-radius: 10px; 
        border: 2px solid #D8BFD8; /* Thistle border */
        margin-bottom: 15px; 
        box-shadow: 2px 2px 8px rgba(216, 191, 216, 0.4);
    }

    /* Style the quiz radio buttons so they stand out */
    .stRadio > div[role="radiogroup"] {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        border: 2px dashed #FF69B4;
    }
    
    /* Override sidebar background to make it cute too */
    [data-testid="stSidebar"] {
        background-color: #FFE4E1 !important; /* Misty Rose */
    }
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
        st.markdown("<div class='vocab-box'><b>IBE (Inference to the Best Explanation):</b> A method of philosophical reasoning. It consists of starting with a seeming fact (F) and evaluating candidate explanations (E) to find the most plausible one.</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Singer's Pond Case:</b> A thought experiment demonstrating that if you can prevent a severe bad (a child drowning) at a minimal cost to yourself (ruining your shoes), you are morally obligated to do so. This acts as the 'Best Explanation' for our moral intuitions.</div>", unsafe_allow_html=True)
        
    if st.session_state.progress >= 1:
        st.markdown("<div class='vocab-box'><b>Justice (Thomson):</b> Strict moral requirements grounded exclusively in moral rights (e.g., right to property, right to life). Violating these means acting <i>unjustly</i>.</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Decency (Thomson):</b> Moral requirements based on reasons OTHER than rights, such as kindness, charity, or being a Good Samaritan. Violating these means acting <i>indecently</i>, but not necessarily unjustly.</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Water Bottle vs. Drowning:</b> A comparative case proving that decency (saving a life you have no strict 'obligation' to save) can carry much heavier moral weight than justice (returning a stolen water bottle).</div>", unsafe_allow_html=True)

    if st.session_state.progress >= 2:
        st.markdown("<div class='vocab-box'><b>Marquis Principle (FLO/VFP):</b> The argument that killing is wrong because it deprives a being of a 'Valuable Future Like Ours'—all the experiences, projects, and enjoyments they would have otherwise had.</div>", unsafe_allow_html=True)
        st.markdown("<div class='vocab-box'><b>Circle of Death Challenge:</b> The counter-argument against Marquis stating a fetus doesn't inherently 'possess' a future in the same way an adult does, because it explicitly requires the continuous, massive bodily assistance of the mother to reach it.</div>", unsafe_allow_html=True)

    if st.session_state.progress == 3:
        st.success("🎉 YOU ARE READY FOR THIS EXAM!")

# ==========================================
# MAIN CONTENT AREA
# ==========================================
st.markdown('<p class="big-font">✨ Moral Philosophy Exam Rescue ✨</p>', unsafe_allow_html=True)
st.write("Take a deep breath! We are going to master IBE, Thomson, and Marquis. Read the comprehensive summaries below, then pass the checkpoint quizzes to unlock the next section. You've got this! 💖")

# ------------------------------------------
# SECTION 1: IBE
# ------------------------------------------
if st.session_state.progress >= 0:
    st.header("🔍 Checkpoint 1: Inference to the Best Explanation (IBE)")
    st.markdown("""
    <div class='cute-box'>
    <b>What exactly is IBE?</b><br>
    Inference to the Best Explanation is a foundational method of reasoning used in philosophy (and science!). Think of yourself as a detective arriving at a scene. You start with something that seems to be true—we call this a <b>Seeming Fact (F)</b>. Then, you brainstorm a bunch of reasons why this fact exists—we call these <b>Candidate Explanations (E)</b>. You evaluate all the candidates. If one explanation (let's say E3) is vastly more plausible, simple, and has more explanatory power than the rest, then you have excellent rational justification to believe E3 is the truth.<br><br>
    
    <b>The Prison Break Example 🚨:</b><br>
    <ul>
        <li><b>F (Fact):</b> Prisoner Smith was locked in a super-secure steel cell at 7pm, but at 5am, his cell is empty.</li>
        <li><b>Candidate E1:</b> Aliens beamed him through the ceiling. (Highly unlikely, lacks simplicity).</li>
        <li><b>Candidate E2:</b> He turned into a ghost and walked through the bars. (Impossible according to physics).</li>
        <li><b>Candidate E3 (The Best Explanation):</b> The lone night guard, Nigel, unlocked the door and let him out.</li>
    </ul>
    Unless we find new evidence (like a secret tunnel dug from the outside, which would make a new E4 the best explanation), Nigel letting him out is the <i>best explanation</i> for the missing prisoner.<br><br>
    
    <b>Applying IBE to Morality: Singer's Pond Example 🦆:</b><br>
    Philosopher Peter Singer uses IBE to prove his moral principles.<br>
    <ul>
        <li><b>F (Fact):</b> You are walking past a shallow pond and see a child drowning. It seems like an absolute moral fact that you are obligated to wade in and save them, even if it ruins your expensive shoes and makes you late for work.</li>
        <li><b>E (Explanation):</b> Singer proposes his principle: "If it is in our power to prevent something very bad from happening, without thereby sacrificing anything of comparable moral importance, we ought, morally, to do it."</li>
    </ul>
    Singer argues that this principle is the <i>absolute best explanation</i> for why we all instinctively know we must save the drowning child. The bad thing (death) is massive, and the sacrifice (muddy shoes) is not morally comparable.
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
    <b>The Great Divide: Justice vs. Decency 🦋</b><br>
    Judith Jarvis Thomson wants to clear up a major confusion in moral philosophy. When we say an action is "morally impermissible" or "wrong," we are usually conflating two very different categories. She splits them up:<br>
    <ol>
        <li><b>Requirements of Justice:</b> These are strict duties grounded entirely in <b>Moral Rights</b> (e.g., the right to life, bodily autonomy, property rights). If you violate someone's moral right, you have acted <i>unjustly</i>.</li>
        <li><b>Requirements of Decency:</b> These are moral requirements grounded in moral reasons <b>OTHER than rights</b>. These involve things like kindness, charity, or being a 'Minimally Decent Samaritan'. If you fail to do these things, you are acting <i>indecently</i>, but not unjustly.</li>
    </ol>
    
    <b>Which one is stronger? The Water Bottle vs. Drowning Case 💪</b><br>
    It is extremely tempting to assume that Justice (because it deals with strict rights) is always weightier, more forceful, and more important than Decency. Thomson forcefully argues <b>NOPE!</b> 
    <ul>
        <li><b>Scenario A (Justice):</b> I steal your water bottle. You have a property right to it. I have violated your right and acted unjustly. But in the grand scheme of things, it's a minor offense.</li>
        <li><b>Scenario B (Decency):</b> You are drowning in the ocean. I am safely on a boat with 50 life preservers. I refuse to toss you one simply because I don't feel like getting up. You do <i>not</i> have a strict moral right to my property (the life preserver). Therefore, I haven't acted unjustly. However, my action is monstrously, deeply <i>indecent</i>.</li>
    </ul>
    This proves that a requirement of decency (saving a life at zero cost) can vastly outweigh a requirement of justice (a stolen water bottle).<br><br>
    
    <b>What does this mean for Abortion? 🤰</b><br>
    Thomson uses this framework to argue about bodily autonomy. She concedes (for the sake of argument) that a fetus is a person. However, no person has a strict moral <i>right</i> to use another person's body to survive. Therefore, withdrawing life support (abortion) does not violate the fetus's rights, meaning it is not <i>unjust</i>. The remaining question is whether abortion is <i>indecent</i>. Thomson argues that while decency requires us to make small sacrifices for others, it absolutely does not require women to make the massive, physical, 9-month sacrifice of pregnancy just to be a "Good Samaritan."
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
    <b>The Marquis Principle: Why is killing wrong? 🌟</b><br>
    Don Marquis thinks the traditional abortion debate is stuck in a rut. Pro-lifers rely on biology ("it has human DNA"), while pro-choicers rely on psychology ("it isn't a rational person yet"). Marquis bypasses all of this by asking a more fundamental question: <b>Why is it wrong to kill a normal adult human being?</b><br>
    It isn't just about the brutalization of the killer, and it isn't just about the grief of the victim's family. Marquis argues the primary wrongness of killing is that it deprives the victim of their future—specifically, a <b>Valuable Future Like Ours (VFP / FLO)</b>. This includes all the future experiences, projects, enjoyments, and milestones they would have otherwise lived to see.<br>
    Because a standard fetus has a valuable future identical to that of a young child or adult, Marquis argues that abortion inflicts the exact same massive loss on the fetus. Therefore, abortion is prima facie (at first glance) seriously morally wrong.<br><br>
    
    <b>The Fatal Flaw? The "Circle of Death" Challenge 🔄☠️</b><br>
    Here is the massive counter-argument your professor highlighted against Marquis' logic:<br>
    To deprive someone of a valuable future, they must actually <i>possess</i> that future independently. You cannot logically deprive me of an Olympic Gold Medal, because I don't have one and was never on track to get one!<br><br>
    
    When you kill a normal adult, they <i>would have</i> reached their future if the killer simply left them alone. They are self-sustaining. 
    A fetus is entirely different. A fetus <b>does not have an independent trajectory toward a future</b>. It desperately needs to use the mother's organs, blood, and body to even survive to reach that future. It is not self-sustaining.<br><br>
    
    So, unplugging a fetus isn't like shooting a healthy adult; it is more like refusing to pull someone out of a burning building or refusing to hook yourself up to a dying violinist. The mother gets stuck in a logical loop (The Circle of Death): She needs to know if the fetus genuinely "has" a valuable future to determine if abortion is wrong. But the fetus only "has" that valuable future <i>if</i> she first decides to sacrifice her body to grant it to them! Because the future is contingent on the mother's continuous bodily assistance, Marquis' attempt to say the fetus inherently "has a future" falls apart.
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
    st.markdown("<h2 style='text-align: center; color: #FF1493; font-weight: bold;'>🎊 100% COMPLETED! GO ACE THAT EXAM! 🎊</h2>", unsafe_allow_html=True)
    if st.button("Reset Dashboard & Study Again 🔄"):
        st.session_state.progress = 0
        st.rerun()
