import streamlit as st
from geopy.geocoders import Nominatim

st.set_page_config(
    page_title="Try LocaliSense",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Mock Localizer ---
def mock_localize_with_gpt(prompt, region, language, education_level):
    localized_examples = {
        "hi": "उदाहरण: यह वैसा ही है जैसे आपके मोहल्ले में मौसम के कारण फसल बर्बाद हो जाए।",
        "es": "Ejemplo: como cuando la sequía afecta las cosechas en tu región.",
        "en": "Example: like how farmers in your area face unpredictable rainfall.",
        "fr": "Exemple : comme lorsque la sécheresse détruit les récoltes dans votre région.",
        "ar": "مثال: مثل عندما تؤثر موجات الجفاف على المحاصيل في منطقتك."
    }
    fallback = localized_examples.get(language, "Example not available for this language")
    return f"""[MOCK LOCALIZATION]\nTarget Language: {language}\nRegion: {region}\nEducation Level: {education_level}\n\nLocalized Summary:\n{prompt}\n\n{fallback}"""

# --- Civic Data ---
def civic_data_lookup(topic, region):
    mock_civic_database = {
        "India": {
            "education": "India's NEP 2020 aims to make education more localized, flexible, and multidisciplinary."
        },
        "Mexico": {
            "education": "SEP Reforma is designed to modernize education through bilingualism and cultural responsiveness."
        },
        "USA": {
            "education": "The Every Student Succeeds Act emphasizes local control and equity in K–12 education."
        }
    }
    country = region.get("country", "Unknown")
    topic_data = mock_civic_database.get(country, {}).get(topic.lower())
    return topic_data or f"No civic data available for {topic} in {country}."

# --- App Page ---
st.title("Try LocaliSense")
st.markdown("Convert a generic AI summary into a localized, civic-aware version tailored for real-world users.")

LANGUAGE_OPTIONS = {
    "English": "en",
    "Spanish": "es",
    "Hindi": "hi",
    "French": "fr",
    "Arabic": "ar"
}

COUNTRY_OPTIONS = ["India", "Mexico", "USA"]

with st.form("localization_form"):
    st.subheader("1. Input your AI Summary")
    summary = st.text_area("Enter the AI-generated summary you'd like to localize:")

    st.subheader("2. Choose Localization Preferences")
    cols = st.columns(2)
    with cols[0]:
        display_lang = st.selectbox("Target Language", list(LANGUAGE_OPTIONS.keys()))
        language = LANGUAGE_OPTIONS[display_lang]
    with cols[1]:
        education = st.selectbox("Education Level", ["basic", "intermediate", "advanced"])

    st.subheader("3. Select Your Country")
    country = st.selectbox("Select your region/country", COUNTRY_OPTIONS)

    submitted = st.form_submit_button("Localize Summary")

if submitted:
    try:
        region_meta = {"country": country}
        civic_context = civic_data_lookup("education", region_meta)
        enriched_prompt = f"{summary}\n\n[Context: {civic_context}]"

        localized = mock_localize_with_gpt(
            enriched_prompt,
            region_meta['country'],
            language,
            education
        )

        st.markdown("---")
        st.subheader("Localized Summary")
        st.code(localized, language="text")

        with st.expander("See Context Details"):
            st.markdown(f"**Region:** {region_meta['country']}")
            st.markdown(f"**Civic Context:** {civic_context}")

        st.download_button(
            label="Download Localized Summary",
            data=localized,
            file_name="localisense_localized_summary.txt"
        )

    except Exception as e:
        st.error(f"Error generating localization: {e}")
