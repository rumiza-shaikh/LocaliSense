import streamlit as st
from geopy.geocoders import Nominatim

# --- Mock Localizer ---
def mock_localize_with_gpt(prompt, region, language, education_level):
    localized_examples = {
        "hi": "उदाहरण: यह वैसा ही है जैसे आपके मोहल्ले में मौसम के कारण फसल बर्बाद हो जाए।",
        "es": "Ejemplo: como cuando la sequía afecta las cosechas en tu región.",
        "en": "Example: like how farmers in your area face unpredictable rainfall."
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

# --- Streamlit App ---
st.set_page_config(page_title="LocaliSense", layout="centered")
st.title("LocaliSense: Context-Aware AI Summaries")

summary = st.text_area("Enter a generic AI summary:")
language = st.selectbox("Target Language", ["en", "es", "hi"])
education = st.selectbox("Education Level", ["basic", "intermediate", "advanced"])

lat = st.number_input("Latitude", value=28.6139)
lon = st.number_input("Longitude", value=77.2090)

if st.button("Localize Summary"):
    try:
        geolocator = Nominatim(user_agent="localisense-streamlit")
        location = geolocator.reverse((lat, lon), language='en', timeout=10)
        region = location.raw['address']

        civic_context = civic_data_lookup("education", region)
        enriched_prompt = f"{summary}\n\n[Context: {civic_context}]"

        localized = mock_localize_with_gpt(
            enriched_prompt,
            region.get("country", "Unknown"),
            language,
            education
        )

        st.markdown("### Localized Output")
        st.text(localized)

        st.download_button(
            label="Download Output",
            data=localized,
            file_name="localisense_localized_summary.txt"
        )
    except Exception as e:
        st.error(f"Error fetching location: {e}")
