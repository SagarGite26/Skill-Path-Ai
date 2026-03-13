import streamlit as st
import json
from app.skill_graph import load_skill_graph
from app.ai_skill_recommender import get_related_skills_from_path
from app.path_generator import (
    get_learning_path,
    calculate_total_time,
    filter_known_skills,
)

# ---------------- LOAD DATA ----------------

graph = load_skill_graph()

with open("data/domains.json") as f:
    domain_topics = json.load(f)


# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "domain" not in st.session_state:
    st.session_state.domain = "Programming"


# ---------------- CSS ----------------

st.markdown(
    """
<style>

.stApp{
background: radial-gradient(circle at top,#111827,#020617);
}

.hero-title{
text-align:center;
font-size:64px;
font-weight:700;
background: linear-gradient(90deg,#60a5fa,#a78bfa);
-webkit-background-clip:text;
color:transparent;
}

.hero-sub{
text-align:center;
font-size:20px;
color:#9ca3af;
margin-bottom:40px;
}

.card{
background:#111827;
border-radius:16px;
padding:30px;
border:1px solid #1f2937;
text-align:center;
transition:0.25s;
}

.card:hover{
transform:translateY(-6px) scale(1.03);
border:1px solid #60a5fa;
box-shadow:0 15px 30px rgba(0,0,0,0.6);
}

.card-icon{
font-size:42px;
margin-bottom:10px;
}

.card-title{
font-size:20px;
font-weight:600;
color:#e5e7eb;
}

</style>
""",
    unsafe_allow_html=True,
)


# ---------------- NAVBAR ----------------


def navbar():

    col1, col2 = st.columns([8, 1])

    with col1:
        st.markdown("### Skills-Path AI")

    with col2:
        st.button("Login")


# ---------------- LANDING PAGE ----------------

if st.session_state.page == "landing":

    navbar()

    st.markdown("<div class='hero-title'>Skills-Path AI</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='hero-sub'>Build structured learning paths for mastering technical skills</div>",
        unsafe_allow_html=True,
    )

    center = st.columns([2, 1, 2])

    with center[1]:
        if st.button("Find Your Path"):
            st.session_state.page = "explore"


# ---------------- EXPLORE PAGE ----------------

elif st.session_state.page == "explore":

    navbar()

    st.title("Explore Domains")

    icons = {
        "Programming": "💻",
        "DSA": "🧠",
        "Web Development": "🌐",
        "Data & AI": "🤖",
        "Databases": "🗄",
        "DevOps": "⚙",
        "Security": "🔐",
    }

    domains = list(domain_topics.keys())

    for i in range(0, len(domains), 3):

        cols = st.columns(3)

        for col, domain in zip(cols, domains[i : i + 3]):

            with col:

                icon = icons.get(domain, "📚")

                st.markdown(
                    f"""
                <div class="card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{domain}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                btn = st.columns([1, 2, 1])

                with btn[1]:

                    if st.button("Explore", key=domain):

                        st.session_state.domain = domain
                        st.session_state.page = "planner"


# ---------------- PLANNER PAGE ----------------

elif st.session_state.page == "planner":

    navbar()

    st.title("Learning Planner")

    # -------- SIDEBAR --------

    st.sidebar.header("Settings")

    selected_domain = st.sidebar.selectbox(
        "Domain",
        list(domain_topics.keys()),
        index=list(domain_topics.keys()).index(st.session_state.domain),
    )

    topics = domain_topics[selected_domain]

    goal1 = st.sidebar.selectbox("Goal", [t for t in topics if t in graph])

    goal2 = st.sidebar.selectbox(
        "Second Goal (optional)", ["None"] + [t for t in topics if t in graph]
    )

    # -------- PATH PREVIEW --------

    path_preview = []

    if goal1:

        path_preview = get_learning_path(graph, goal1)

        if goal2 != "None":
            path_preview += get_learning_path(graph, goal2)

        path_preview = list(dict.fromkeys(path_preview))

    # -------- SKILLS YOU KNOW --------

    known_skills = st.sidebar.multiselect("Skills you already know", path_preview)

    generate = st.sidebar.button("Generate Path")

    # -------- OUTPUT --------

    if generate and path_preview:

        filtered_path = filter_known_skills(path_preview, known_skills)

        final_path = list(dict.fromkeys(filtered_path))

        total_time = calculate_total_time(graph, final_path)

        col1, col2 = st.columns(2)

        col1.metric("Skills", len(path_preview))
        col2.metric("Estimated Time", f"{total_time} hrs")

        completed = len(known_skills)
        total = len(path_preview)

        progress = completed / total if total > 0 else 0

        st.subheader("Progress")

        st.progress(progress)

        st.write(f"{completed}/{total} skills completed ({int(progress*100)}%)")

        # -------- AI EXPLANATION --------

        st.subheader("🤖 AI Explanation")

        st.info("""
        This roadmap is generated using prerequisite relationships between skills.

        The system:
        • Identifies foundational topics required for your goal  
        • Removes the skills you already know  
        • Orders the remaining topics logically
        """)

        # -------- ROADMAP --------
        # -------- RELATED SKILLS --------

        # -------- INDUSTRY INSIGHT --------

        # -------- INDUSTRY INSIGHT --------

        related = get_related_skills_from_path(path_preview)

        if related:

            st.subheader("💡 Industry Insight")

            st.write(
                f"Based on analysis of job descriptions related to **{goal1}**, "
                "these skills frequently appear together in industry roles:"
            )

            for skill, count in related:

                st.write(f"• {skill} — mentioned in {count} job postings")

            st.caption(
                "These complementary skills were extracted by analyzing job descriptions "
                "and identifying frequently co-occurring skills."
            )

        for i, skill in enumerate(final_path, start=1):

            difficulty = graph[skill]["difficulty"]
            hours = graph[skill]["estimated_hours"]

            st.markdown(f"### {i}. {skill}")

            c1, c2 = st.columns(2)

            c1.write(f"Difficulty: {difficulty}")
            c2.write(f"Time: {hours} hrs")

            st.divider()

        st.success(f"Estimated learning time: {total_time} hours")

        # -------- DISCLAIMER --------

        st.markdown("---")

        st.caption("""
⚠️ **Disclaimer:**  
• The estimated learning time is an approximate value and may vary depending on your learning pace and prior knowledge.  
• The recommended learning path is generated automatically based on skill prerequisites and job-description analysis.  
• While the pathway aims to be logically structured, it may not be perfect for every learner and should be used as a general guideline.
""")

    # -------- RETURN BUTTON --------

    bottom = st.columns([2, 1, 2])

    with bottom[1]:

        if st.button("Return Home"):
            st.session_state.page = "landing"
