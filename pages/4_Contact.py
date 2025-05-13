import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")
st.sidebar.markdown("### Contact")

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

        .stButton>button {
            background-color: black;
            color: white;
            border: none;
            font-weight: bold;
            border-radius: 20px;
            padding: 0.5rem 1.2rem;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Contact")
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class='content-box'>
    <p><strong>For partnership inquiries:</strong><br> reach@localisense.ai</p>
    <p><strong>For research collaborations:</strong><br> collaborate@localisense.ai</p>
    <p><strong>Built by:</strong><br> Rumiza Shaikh @ Cornell Tech</p>
    </div>
    """, unsafe_allow_html=True)
