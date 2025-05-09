# LocaliSense

**LocaliSense** is an AI-powered localization layer that transforms generic AI summaries into culturally relevant, civically informed, and contextually appropriate outputs.

Built as a multi-page Streamlit web app, it showcases how cognitive localization can enhance the accessibility, clarity, and trustworthiness of generative AI for global users.

---

## 🌐 Live Demo

Access the deployed app here:  
**[https://localisense.streamlit.app](https://localisense.streamlit.app)**

---

## 🧭 What LocaliSense Does

- Localizes AI-generated summaries based on **country, language, and education level**
- Enriches content with **regional civic data** (e.g., NEP 2020 for India)
- Adapts **tone and examples** for local relevance and user clarity
- Supports multiple languages: **English, Spanish, Hindi, French, Arabic**
- Accepts user feedback for continuous improvement

---

## 📁 App Structure

This is a multi-page Streamlit app using the `pages/` folder:

localisense/
│
├── app.py # Homepage
├── requirements.txt
├── README.md
│
└── pages/
├── 1_Try_LocaliSense.py # The core tool interface
├── 2_About_The_Project.py # Concept, architecture, vision
├── 3_Feedback.py # Anonymous user feedback form
└── 4_Contact.py # Contact info and external links


---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/localisense.git
   cd localisense
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
📦 Requirements
txt
Copy
Edit
streamlit>=1.32.0
geopy>=2.3.0
✍️ About the Creator
Rumiza Shaikh
Cornell Tech MBA 2025
Product Strategy | Applied AI | Global Information Equity

Email: rumiza.shaikh@gmail.com

LinkedIn: linkedin.com/in/rumizashaikh

Portfolio: rumizashaikh.github.io

💡 Future Plans
Integrate real OpenAI / Gemini LLMs

Connect civic data APIs across more regions

Add user re-ranking loop for feedback-based improvement

Package as an API layer for third-party AI platforms

