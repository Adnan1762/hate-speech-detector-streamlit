import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="🌍 Multilingual Hate Speech Detection",
    page_icon="💬",
    layout="centered"
)

# Darker background images for both Positive and Negative scenarios
POSITIVE_BG = "https://images.pexels.com/photos/10451136/pexels-photo-10451136.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
NEGATIVE_BG = "https://images.pexels.com/photos/10481285/pexels-photo-10481285.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

# Background setter function
# Background setter
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center; /* This centers the background image */
            transition: background-image 2s ease-in-out;
            -webkit-transition: background-image 2s ease-in-out;
            -moz-transition: background-image 2s ease-in-out;
            -o-transition: background-image 2s ease-in-out;
            color: black !important;
        }}

        h1, h2, h3, h4, h5, h6, p, label, span, div {{
            color: white !important;
        }}

        .stMarkdown, .css-10trblm, .css-1v0mbdj {{
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        color: white !important;
        background-color: #4CAF50;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: bold;
    }

    div.stButton > button:first-child:hover {
        background-color: #45a049;
    }

    .stProgress > div > div > div > div {
        background-color: white !important;
    }

    div[data-testid="stVerticalBlock"] p {
        font-size: 22px !important;
        font-weight: bold !important;
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Set default background (darker for both positive and negative)
set_background(POSITIVE_BG)

# App title and intro
st.markdown("<h1 style='text-align: center;'>🌍 Multilingual Hate Speech Detection App</h1>", unsafe_allow_html=True)
st.markdown("### 🔎 Enter any text in any language to analyze for potential **hate speech** or **toxicity**.\n"
            "We’ll detect the language, translate it if needed, and analyze it using a powerful AI model.", unsafe_allow_html=True)

# Input field
text_input = st.text_area("✍️ Input Text:", placeholder="Type or paste text here...")

# Hugging Face APIs
DETECTION_API = "https://api-inference.huggingface.co/models/papluca/xlm-roberta-base-language-detection"
TRANSLATE_API = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-mul-en"
HATE_SPEECH_API = "https://api-inference.huggingface.co/models/unitary/toxic-bert"

# API headers
headers = {
    "Authorization": f"Bearer {st.secrets['api']['huggingface_token']}"
}

# Generic query function
def query(api_url, payload):
    response = requests.post(api_url, headers=headers, json=payload)
    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid response from API."}

# On button click
if st.button("🚀 Analyze Text"):
    if text_input.strip():
        # 1. Language Detection
        with st.spinner("🌐 Detecting language..."):
            lang_result = query(DETECTION_API, {"inputs": text_input})
            try:
                lang_label = lang_result[0][0]["label"]
                lang_score = lang_result[0][0]["score"]
                st.success(f"🗣️ Detected Language: `{lang_label.upper()}` ({lang_score:.2%} confidence)")
            except (KeyError, IndexError, TypeError):
                st.error("⚠️ Could not detect language. Please try again.")
                st.stop()

        # 2. Translation to English (if needed)
        translated_text = text_input
        if lang_label != "en":
            with st.spinner("🔁 Translating to English..."):
                trans_result = query(TRANSLATE_API, {"inputs": text_input})
                if isinstance(trans_result, list) and "translation_text" in trans_result[0]:
                    translated_text = trans_result[0]["translation_text"]
                    st.success("✅ Successfully Translated!")
                    st.markdown(f"**📝 Translated Text:** _{translated_text}_")
                else:
                    st.warning("⚠️ Translation failed. Proceeding with original text.")

        # 3. Hate Speech Detection
        with st.spinner("🧠 Analyzing for hate speech..."):
            output = query(HATE_SPEECH_API, {"inputs": translated_text})
            if isinstance(output, dict) and output.get("error"):
                st.error(f"❌ Error: {output['error']}")
            else:
                st.markdown("### 🔍 Hate Speech Detection Results")
                try:
                    for result in output[0]:
                        label = result['label']
                        score = result['score']
                        st.markdown(f"**{label}:** {score:.2%}")
                        st.progress(score)

                    toxic_scores = [r['score'] for r in output[0] if "toxic" in r['label'].lower()]
                    if toxic_scores and max(toxic_scores) > 0.5:
                        set_background(NEGATIVE_BG)
                        st.error("⚠️ Potential **toxic or hateful content** detected.")
                    else:
                        set_background(POSITIVE_BG)
                        st.success("✅ No significant toxicity detected.")
                except (KeyError, TypeError, IndexError):
                    st.error("❌ Unexpected format from hate speech model.")
    else:
        st.warning("📭 Please enter some text to analyze.")
