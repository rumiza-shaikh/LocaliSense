import streamlit as st

st.set_page_config(
    page_title="Feedback",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Feedback")
st.markdown("---")

st.markdown("""
We welcome your input to make LocaliSense better.

Let us know what worked, what didn’t, or what you'd like to see next.
""")

with st.form("feedback_form"):
    st.subheader("Share Your Thoughts")
    name = st.text_input("Your Name (optional)")
    role = st.selectbox("You are a:", ["General User", "Product Manager", "Engineer", "Designer", "Researcher", "Other"])
    comments = st.text_area("Your feedback:")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Thank you! Your feedback has been recorded.")

st.caption("This prototype stores feedback anonymously.")
