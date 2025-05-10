import streamlit as st

st.set_page_config(
    page_title="LocaliSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Rename 'app' to 'Home' in sidebar ---
st.sidebar.markdown("### Home")

# --- Optional custom styling ---
st.markdown("""
    <style>
        .main h1 {
            color: #003262;
            font-weight: 700;
        }
        .main h4 {
            color: #555555;
        }
        .block {
            background-color: #f5f5f5;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.title("LocaliSense")
st.markdown("### Making Generative AI Truly Local and Useful")

st.markdown("""
<div class='block'>
LocaliSense is an AI-powered localization layer that adapts generic AI summaries into **culturally relevant, civically aware, and contextually appropriate** outputs.  
Unlike basic translation, it reshapes tone, examples, and semantics to fit real-world users across geographies and languages.

If generative AI is the future of information access, LocaliSense is how we ensure it works for everyone, not just the English-speaking world.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='block'>
<b>What You Can Do With LocaliSense:</b>
- Convert AI summaries into local language + context  
- Add regional civic data (education, policy, etc.)  
- Adjust tone based on user background  
- Improve clarity and trust for diverse audiences  
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='block'>
<h4>Try the App</h4>
Use the **sidebar on the left** to navigate to the Localizer Tool and start testing.
</div>
""", unsafe_allow_html=True)
