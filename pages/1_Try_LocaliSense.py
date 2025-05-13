import streamlit as st
from geopy.geocoders import Nominatim

st.set_page_config(
    page_title="Try LocaliSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown("### Try LocaliSense")

# --- Styling ---
st.markdown("""
    <style>
        html, body, textarea, input, [class^="st-"], [class*="stMarkdown"], .main {
            font-family: 'Georgia', serif !important;
            background-color: #ffffff;
            color: #111111;
        }

        .stButton>button {
            background-color: black;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 20px;
            padding: 0.6rem 1.2rem;
            margin-top: 0.5rem;
        }

        .input-box {
            background-color: #f9f9f9;
            padding: 1.2rem;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .post-box {
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 16px;
            margin-top: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .divider {
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 1.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Header ---
st.title("Try LocaliSense")
st.markdown("Input a generic AI summary and see how LocaliSense adapts it for real-world users.")

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# --- Localization Form ---
with st.form("localization_form"):
    st.markdown("<div class='input-box'>", unsafe_allow_html=True)

    st.subheader("Enter AI Summary")
    summary = st.text_area("Paste your AI-generated summary here:")

    st.subheader("Localization Preferences")
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Country", ["India", "Mexico", "USA"])
    with col2:
        education = st.selectbox("Education Level", ["basic", "intermediate", "advanced"])
    language = st.selectbox("Language", ["English", "Hindi", "Spanish"])

    submitted = st.form_submit_button("Localize Summary")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Civic Context + Analogy Logic ---
def civic_data_lookup(country):
    db = {
        "India": "NEP 2020 aims to make education localized and multidisciplinary.",
        "Mexico": "SEP Reforma adds bilingualism and cultural responsiveness.",
        "USA": "The Every Student Succeeds Act supports local control in schools."
    }
    return db.get(country, "")

def tone_scaled_analogy(education, language):
    analogies = {
        "basic": {
            "English": "Example: Like when drought hits farmers in your region.",
            "Hindi": "उदाहरण: जैसे सूखा आपके इलाके की फसलें बर्बाद कर देता है।",
            "Spanish": "Ejemplo: como cuando la sequía arruina los cultivos en tu zona."
        },
        "intermediate": {
            "English": "Example: Think of urban schools struggling to stay open after climate disruptions.",
            "Hindi": "उदाहरण: जैसे शहरों के स्कूल मौसम की वजह से बंद हो जाते हैं।",
            "Spanish": "Ejemplo: como cuando las escuelas urbanas cierran por fenómenos climáticos."
        },
        "advanced": {
            "English": "Example: Similar to how regional policies struggle to adapt to shifting environmental baselines.",
            "Hindi": "उदाहरण: जैसे क्षेत्रीय नीतियाँ बदलते पर्यावरणीय मानकों से तालमेल नहीं बैठा पाती हैं।",
            "Spanish": "Ejemplo: como cuando las políticas regionales no se adaptan al cambio ambiental."
        }
    }
    return analogies.get(education, {}).get(language, "")

# --- Full Localization ---
def mock_localize(summary, country, language, education):
    context = civic_data_lookup(country)
    analogy = tone_scaled_analogy(education, language)
    source = f"\n\n_Source: Ministry of Education, {country}_" if country == "India" else \
             f"\n\n_Source: National Education Policy, {country}_"

    return f"{summary}\n\n[Context: {context}]\n\n{analogy}{source}"

# --- Output ---
if submitted:
    localized_result = mock_localize(summary, country, language, education)

    st.markdown("<h4>Localized Output</h4>", unsafe_allow_html=True)
    with st.container():
        st.markdown(f"<div class='post-box'>", unsafe_allow_html=True)
        st.markdown(f"**{country} – {education.capitalize()}**")
        st.markdown(localized_result)
        st.markdown("</div>", unsafe_allow_html=True)

    st.download_button(
        label="Download Localized Summary",
        data=localized_result,
        file_name="localized_summary.txt"
    )

    # --- Feedback Prompt ---
    st.markdown("### Did this feel relevant?")
    relevance = st.radio("Your feedback helps us improve:", ["👍 Yes", "👎 Not really"], horizontal=True)
    st.success("Thanks for your feedback!") if relevance else None
