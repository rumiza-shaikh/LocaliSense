import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Feedback", layout="wide")
st.sidebar.markdown("### Feedback")

feedback_file = "feedback_log.csv"

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

# --- Feedback Form ---
with st.form("feedback_form"):
    with st.container():
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        role = st.selectbox("You are a...", ["Student", "Educator", "Policy Analyst", "Product Manager", "Other"])
        feedback = st.text_area("Your feedback")
        submitted = st.form_submit_button("Submit")
        st.markdown("</div>", unsafe_allow_html=True)

# --- Save and Show Feedback ---
if submitted:
    new_entry = pd.DataFrame({
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "role": [role],
        "feedback": [feedback]
    })

    try:
        existing = pd.read_csv(feedback_file)
        all_feedback = pd.concat([existing, new_entry], ignore_index=True)
    except FileNotFoundError:
        all_feedback = new_entry

    all_feedback.to_csv(feedback_file, index=False)
    st.success("Thank you for your feedback!")

    st.markdown("### Recent Feedback")

    for _, row in all_feedback.tail(5).iterrows():
        st.markdown(f"""
        <div style='background-color:#f9f9f9; padding:1rem; border-radius:16px; margin-bottom:1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);'>
        <strong>{row['role']}</strong> — <span style='font-size: 0.85rem; color: gray;'>{row['timestamp']}</span>
        <br>{row['feedback']}
        </div>
        """, unsafe_allow_html=True)
