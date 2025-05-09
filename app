import streamlit as st
from geopy.geocoders import Nominatim

# --- Mock Localizer ---
def mock_localize_with_gpt(prompt, region, language, education_level):
    localized_examples = {
        "hi": "\ud83d\udccc \u0909\u0926\u093e\u0939\u0930\u0923: \u092f\u0939 \u0935\u0948\u0938\u093e \u0939\u0940 \u0939\u0948 \u091c\u0948\u0938\u0947 \u0906\u092a\u0915\u0947 \u092e\u094b\u0939\u0932\u094d\u0932\u0947 \u092e\u0947\u0902 \u092e\u094c\u0938\u092e \u0915\u0940 \u0935\u091c\u0939 \u0938\u0947 \u092b\u0938\u0932 \u0928\u093e\u0937\u094d\u091f \u0939\u094b \u091c\u093e\u090f।",
        "es": "\ud83d\udccc Ejemplo: como cuando la sequ\u00eda afecta las cosechas en tu regi\u00f3n.",
        "en": "\ud83d\udccc Example: like how farmers in your area face unpredictable rainfall."
    }
    fallback = localized_examples.get(language, "\ud83d\udccc [Example not available for this language]")
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
st.title("\ud83c\udf0d LocaliSense: Context-Aware AI Summaries")

summary = st.text_area("\ud83d\udcdd Enter a generic AI summary:")
language = st.selectbox("\ud83c\udf10 Target Language", ["en", "es", "hi"])
education = st.selectbox("\ud83d\udd22 Education Level", ["basic", "intermediate", "advanced"])

lat = st.number_input("\ud83c\udf0f Latitude", value=28.6139)
lon = st.number_input("\ud83c\udf0f Longitude", value=77.2090)

if st.button("\u2728 Localize Summary"):
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

        st.markdown("### \ud83d\udd8b\ufe0f Localized Output")
        st.text(localized)

        st.download_button(
            label="\ud83d\udce5 Download Output",
            data=localized,
            file_name="localisense_localized_summary.txt"
        )
    except Exception as e:
        st.error(f"\u26a0\ufe0f Error fetching location: {e}")
