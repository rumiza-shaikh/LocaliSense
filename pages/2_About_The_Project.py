import streamlit as st

st.set_page_config(
    page_title="About the Project",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("About the Project")
st.markdown("---")

st.subheader("The Problem")
st.markdown("""
Generative AI tools like ChatGPT, Bard, and Google's SGE often produce summaries that are:
- Linguistically accurate, but **culturally tone-deaf**
- Biased toward **Western contexts**
- Lacking **civic or regional relevance** for users in non-English or emerging markets
""")

st.subheader("The LocaliSense Solution")
st.markdown("""
LocaliSense is an AI-powered localization layer that transforms generic summaries into:
- Regionally grounded content
- Tone adapted to user context
- Civic-aware, example-rich output
""")

st.subheader("How It Works (Prototype)")
st.markdown("""
1. Input: AI summary  
2. User inputs: Country, language, education level  
3. Adds civic context from a regional knowledge base  
4. Adjusts language, tone, and examples  
5. Outputs a localized result  

Currently, this is done with mock data — integration with live APIs is on the roadmap.
""")

st.subheader("Why It Matters")
st.markdown("""
- **Trust**: Users relate better to content grounded in their region  
- **Clarity**: Tone and examples adapted to educational background  
- **Equity**: A step toward fairer access to information across borders  
""")

st.caption("Built by Rumiza Shaikh, Cornell Tech MBA 2025.")
