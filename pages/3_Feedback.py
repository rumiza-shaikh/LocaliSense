import streamlit as st

st.set_page_config(page_title="Feedback", layout="wide")
st.sidebar.markdown("### Feedback")

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

st.title("Feedback")
st.markdown("Let us know how LocaliSense worked for you.")

with st.form("feedback_form"):
    with st.container():
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        role = st.selectbox("You are a...", ["Student", "Educator", "Policy Analyst", "Product Manager", "Other"])
        feedback = st.text_area("Your feedback")
        submitted = st.form_submit_button("Submit")
        st.markdown("</div>", unsafe_allow_html=True)

if submitted:
    st.success("Thank you for your feedback!")
