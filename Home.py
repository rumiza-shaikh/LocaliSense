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
        .cta-button {
            background-color: #003262;
            color: white;
            font-weight: 600;
            padding: 0.5rem 1.2rem;
            border-radius: 6px;
            margin-top: 1rem;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<h2 class='tagline'>AI is Global. So Should Its Voice Be.</h2>", unsafe_allow_html=True)
st.title("LocaliSense")
st.markdown("Making Generative AI Truly Local and Useful")

# --- Tool Preview Image (optional demo image) ---
st.image("images/localisense-preview.png", caption="LocaliSense adapts summaries by region, language, and tone.", use_column_width=True)

# --- What Is LocaliSense ---
st.markdown("""
<div class='highlight-box'>
LocaliSense is an AI-powered localization layer that adapts generic AI summaries into <strong>culturally relevant, civically aware, and contextually appropriate</strong> outputs.
Unlike basic translation, it reshapes tone, examples, and semantics to fit real-world users across geographies and educational backgrounds.
</div>
""", unsafe_allow_html=True)

# --- Key Features Section ---
st.markdown("### What You Can Do With LocaliSense")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Contextual Localization</h4>
    Converts AI summaries into regionally grounded language with local analogies and examples.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='highlight-box'>
    <h4>Civic-Aware Output</h4>
    Automatically injects public policy and education context based on the user's region.
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
    Ready to be integrated with any generative search, translate, or civic tool.
    </div>
    """, unsafe_allow_html=True)

# --- CTA Section ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Try the App")

st.markdown("""
Use the <strong>sidebar on the left</strong> to start using the Localizer Tool and see how summaries can be transformed into culturally resonant content.
""", unsafe_allow_html=True)

if st.button("Go to Localizer Tool"):
    st.switch_page("Try LocaliSense")  # Make sure this matches your sidebar title exactly
