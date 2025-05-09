import streamlit as st

st.set_page_config(page_title="About LocaliSense", layout="centered")

st.title("About the Project")
st.markdown("---")

st.subheader("The Problem")
st.markdown("""
Generative AI tools like ChatGPT, Bard, and Google's SGE often produce summaries that are:
- Linguistically accurate, but **culturally tone-deaf**
- Biased toward **Western contexts**
- Lacking **civic or regional relevance** for users in non-English or emerging markets

This limits trust, clarity, and ultimately user retention — especially for global-scale platforms.
""")

st.subheader("The LocaliSense Solution")
st.markdown("""
LocaliSense is an **AI-powered localization layer** designed to sit on top of any generative summary engine and transform the output into:
- Regionally grounded content
- Tone adapted to the user's education level
- Enhanced with real-world civic examples

This helps users **understand better, relate faster**, and trust AI results — especially in multilingual or underserved markets.
""")

st.subheader("How It Works (Prototype)")
st.markdown("""
1. **Input:** A generic AI summary (e.g., from an LLM)
2. **User Context:** Country, preferred language, education level
3. **Civic Injection:** Pull civic data or region-specific reforms (e.g., NEP 2020 in India)
4. **Localization Engine:** Adjust tone, translate meaningfully, and add culturally aligned examples
5. **Output:** A localized summary that resonates

> Currently, the prototype uses mock civic data and a simulated LLM. Real-time integration with OpenAI or Gemini APIs is a planned upgrade.
""")

st.subheader("Why It Matters")
st.markdown("""
- **Knowledge equity**: Not all users process AI summaries the same way
- **Trust & retention**: Localized output reduces bounce rates and improves comprehension
- **Scalable impact**: Plug-and-play for Search, Translate, Lens, civic tech, and more
""")

st.info("This project was built by Rumiza Shaikh as part of her Cornell Tech MBA, with the vision of making AI-generated information truly inclusive and universally useful.")

