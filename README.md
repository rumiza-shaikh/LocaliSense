# 🌍 LocaliSense — Context-Aware AI Localization Layer

**Your words. Your world. Your context.**

LocaliSense is an AI-powered web app that transforms generic AI-generated summaries into culturally relevant, civically informed, and region-specific outputs. Instead of simple translation, LocaliSense localizes tone, examples, and semantics based on user location, education level, and language preferences.

---

## 🚀 Live Demo

👉 [Launch the App](https://localisense.streamlit.app) *(hosted on Streamlit Cloud)*

---

## ✨ Features

- 🧭 **Geographic Localization:** Detects region from latitude/longitude
- 🗣️ **Multilingual Output:** Supports English, Spanish, and Hindi (mock-based)
- 🧠 **Civic Context Enrichment:** Adds region-specific civic data to summaries
- 🧑‍🏫 **Tone Adaptation:** Adjusts content based on education level
- 💬 **Mock LLM Output:** Simulates GPT-based localization for demonstration
- 📥 **Export to Text:** Download customized summaries as `.txt` files

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — Python web app framework
- [Geopy](https://geopy.readthedocs.io/) — Reverse geocoding for location metadata
- `mock_localize_with_gpt()` — Simulated LLM behavior (API-free fallback)

> Note: You can replace the mock localizer with OpenAI's GPT-4 or other LLMs once you have API access.

---

## 📷 Screenshots

| Input Summary | Localized Output |
|---------------|------------------|
| “Climate change reduces crop yields.” | “El cambio climático reduce las cosechas. 📌 Ejemplo: como cuando la sequía afecta a agricultores en Oaxaca.” |

---

## 🧪 Example Use Case

A user in New Delhi enters:
> “How does climate change affect agriculture?”

**LocaliSense**:
- Detects their location
- Adds civic info: *“India’s NEP 2020 emphasizes climate literacy in education”*
- Translates and adapts tone for Hindi speakers with basic education
- Returns:
> “जलवायु परिवर्तन से वर्षा के पैटर्न में बदलाव आता है और फसलों की पैदावार घट जाती है।  
📌 उदाहरण: यह वैसा ही है जैसे आपके मोहल्ले में मौसम के कारण फसल बर्बाद हो जाए।”

---

## 🧑‍💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/your-username/localisense.git
cd localisense

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
