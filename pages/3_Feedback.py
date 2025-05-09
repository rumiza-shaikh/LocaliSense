import streamlit as st

st.set_page_config(page_title="Feedback", layout="centered")

st.title("Feedback")
st.markdown("---")

st.markdown("""
We'd love to hear from you.

Whether you're a user, researcher, or product leader, your feedback helps us improve LocaliSense and make it more useful across geographies and use cases.
""")

with st.form("feedback_form"):
    st.subheader("Tell us what you think")
    name = st.text_input("Your Name (optional)")
    role = st.selectbox("Are you a:", ["General User", "Product Manager", "Engineer", "Designer", "Researcher", "Other"])
    comments = st.text_area("What's working well? What could be improved?")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Thank you! Your feedback has been recorded.")

st.markdown("---")
st.caption("Note: This is a prototype. Feedback is stored anonymously and not linked to any user identity.")
