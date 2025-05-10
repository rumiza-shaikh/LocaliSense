import streamlit as st

st.set_page_config(
    page_title="LocaliSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar label override ---
st.sidebar.markdown("### Home")

# --- Global Indigo + Georgia Styling ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Georgia', serif !important;
            background-color: #F6F1EB !important;
        }

        .main h1, .main h2, .main h3, .main h4, .main p {
            font-family: 'Georgia', serif !important;
        }

        .main h1 {
            color: #2B2C3F;
            font-weight: 700;
        }

        .main h2 {
            font-size: 1.6rem;
            font-weight: 600;
            color: #2B2C3F;
        }

        .main h4 {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2B2C3F;
        }

        .tagline {
            font-size: 1.4rem;
            margin-top: 1.5rem;
            color: #2B2C3F;
        }

        .highlight-box {
            background-color: #FFFFFF;
            border-left: 6px solid #3E3D77;
            border-radius: 6px;
            padding: 1rem;
            margin-bottom: 1.5rem;
        }

        .stButton>button {
            background-color: #3E3D77;
            color: white;
            font-weight: bold;
            padding: 0.6rem 1.2rem;
            border: none;
            border-radius: 6px;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
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
    Converts summaries into regionally grounded, culturally appropriate content.
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Civic-Aware Output</h4>
    Embeds region-specific education and policy context automatically.
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Education-Based Tone</h4>
    Matches tone and complexity to user education level.
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Plug-and-Play Architecture</h4>
    Designed to enhance any AI-based tool or product interface.
    </div>
    """, unsafe_allow_html=True)

# --- CTA ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Ready to Explore?")
st.markdown("Start transforming AI content into something that truly resonates.")

if st.button("Try LocaliSense Now"):
    st.switch_page("Try LocaliSense")
