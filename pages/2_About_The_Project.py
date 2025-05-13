import streamlit as st

st.set_page_config(page_title="About", layout="wide")
st.sidebar.markdown("### About")

# --- Style ---
st.markdown("""
    <style>
        html, body, [class*="css"], textarea, input {
            font-family: 'Georgia', serif !important;
            background-color: #ffffff;
            color: #111111;
        }

        .content-box {
            background-color: #f9f9f9;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .divider {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 1.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("About LocaliSense")
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class='content-box'>
    <p>
    LocaliSense is a localization intelligence layer built on top of generative AI outputs. Its mission is to transform generic summaries into versions that are linguistically accurate, culturally aware, and civically grounded.
    </p>
    <p>
    Unlike basic translation tools, LocaliSense adapts tone, semantic context, and real-world examples based on the user’s country, education level, and language.
    </p>
    <p>
    Ideal for global deployments of AI in education, civic tech, and search — LocaliSense helps close the gap between technological fluency and cultural relevance.
    </p>
    </div>
    """, unsafe_allow_html=True)
