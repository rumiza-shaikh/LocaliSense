import streamlit as st

st.set_page_config(
    page_title="LocaliSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar label override ---
st.sidebar.markdown("### Home")

# --- Page Styling ---
st.markdown("""
    <style>
        .main h1 {
            color: #003262;
            font-weight: 700;
        }
        .main h2 {
            font-size: 1.6rem;
            font-weight: 600;
            color: #002b45;
        }
        .main h4 {
            font-size: 1.1rem;
            font-weight: 600;
        }
        .tagline {
            font-size: 1.4rem;
            margin-top: 1.5rem;
            color: #2c3e50;
        }
        .highlight-box {
            background-color: #f2f4f7;
            border-radius: 6px;
            padding: 1rem;
            margin-bottom: 1.5rem;
        }
        .button-container button {
            background-color: #003262 !important;
            color: white !important;
            font-weight: 600;
            border-radius: 6px;
            padding: 0.6rem 1.2rem;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header and Tagline ---
st.markdown("<h2 class='tagline'>AI is Global. So Should Its Voice Be.</h2>", unsafe_allow_html=True)
st.title("LocaliSense")
st.markdown("Making Generative AI Truly Local and Useful")

# --- Overview Box ---
st.markdown("""
<div class='highlight-box'>
LocaliSense is an AI-powered localization layer that adapts generic AI summaries into <strong>culturally relevant, civically aware, and contextually appropriate</strong> outputs.
Unlike basic translation, it reshapes tone, examples, and semantics to fit real-world users across geographies and educational backgrounds.
</div>
""", unsafe_allow_html=True)

# --- Feature Cards ---
st.markdown("### What You Can Do With LocaliSense")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Contextual Localization</h4>
    Converts AI summaries into regionally grounded language with local analogies and tone adjustments.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Civic-Aware Output</h4>
    Automatically injects public policy and education context based on the user's location.
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Education-Based Tone</h4>
    Adjusts complexity and style for users with basic, intermediate, or advanced education levels.
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Plug-and-Play Architecture</h4>
    Ready to be integrated with any generative search, translate, or civic application.
    </div>
    """, unsafe_allow_html=True)

# --- CTA Section ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Ready to Explore?")
st.markdown("Start transforming AI content into something that truly resonates.")

with st.container():
    col1, col2 = st.columns([1, 6])
    with col1:
        pass
    with col2:
        if st.button("Try LocaliSense Now"):
            st.switch_page("Try LocaliSense")  # Replace with static link if needed
