import streamlit as st

st.set_page_config(
    page_title="LocaliSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar label override ---
st.sidebar.markdown("### Home")

# --- Threads-style UI + Georgia Font ---
st.markdown("""
    <style>
        html, body, textarea, input, [class^="st-"], [class*="stMarkdown"], .main {
            font-family: 'Georgia', serif !important;
            background-color: #ffffff;
            color: #111111;
        }

        .main h1, .main h2, .main h3, .main h4 {
            font-family: 'Georgia', serif !important;
        }

        .markdown-text-container {
            font-family: 'Georgia', serif !important;
        }

        section[data-testid="stSidebar"] {
            font-family: 'Georgia', serif !important;
        }

        .stButton>button {
            background-color: black;
            color: white;
            border: none;
            font-weight: bold;
            border-radius: 20px;
            padding: 0.6rem 1.2rem;
        }

        .post-box {
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .divider {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 1.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Heading ---
st.title("LocaliSense")
st.markdown("### Where AI Meets Cultural Relevance")

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# --- Simulated Threads-style feed ---
sample_posts = [
    {
        "author": "India – Basic Education",
        "time": "10 mins ago",
        "content": "Climate change is reducing rainfall. It's like when farmers in my village lose crops due to late monsoons. NEP 2020 helps us localize education around this."
    },
    {
        "author": "Mexico – Intermediate",
        "time": "25 mins ago",
        "content": "SEP Reforma includes bilingualism to support learning that reflects both local culture and national goals. AI summaries should do the same."
    },
    {
        "author": "USA – Advanced",
        "time": "1 hr ago",
        "content": "The Every Student Succeeds Act promotes local decision-making in schools. LocaliSense adapts AI content with the same spirit."
    },
]

# --- Feed Loop ---
for post in sample_posts:
    with st.container():
        st.markdown(f"<div class='post-box'>", unsafe_allow_html=True)
        st.markdown(f"**{post['author']}**  •  {post['time']}")
        st.markdown(post["content"])
        st.markdown("</div>", unsafe_allow_html=True)

# --- CTA Button ---
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("Want to test your own AI summary?")

if st.button("Try LocaliSense Tool"):
    st.switch_page("Try LocaliSense")  # Make sure this matches the page title
