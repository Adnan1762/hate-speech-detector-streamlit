

# 🌍 Multilingual Hate Speech Detection App

This **Multilingual Hate Speech Detection App** uses state-of-the-art natural language processing (NLP) models to detect hate speech in text input in any language. The app supports language detection, translation (if needed), and analysis for hate speech or toxicity.

It’s built with **Streamlit** for the frontend and uses **Hugging Face's APIs** for language detection, translation, and hate speech analysis.

### 🔗 **Live Demo**: [Try the app here](https://hate-detector.streamlit.app/)

## Features
- **Multilingual Support**: Analyze text in any language.
- **Language Detection**: Detects the language of the input text.
- **Automatic Translation**: If the input text is not in English, the app translates it for further analysis.
- **Hate Speech Detection**: Analyzes the text for toxic, harmful, or hateful content.
- **User-friendly Interface**: Easily interact with the app using Streamlit’s interface.

## Technologies Used
- **Frontend**: Streamlit
- **Backend**: Hugging Face API for language detection, translation, and hate speech detection.
- **Language Detection Model**: [XLM-Roberta](https://huggingface.co/papluca/xlm-roberta-base-language-detection)
- **Translation Model**: [Helsinki-NLP Opus-MT](https://huggingface.co/Helsinki-NLP/opus-mt-mul-en)
- **Hate Speech Model**: [Toxic-BERT](https://huggingface.co/unitary/toxic-bert)

## Requirements
- **Python**: 3.7+
- **Streamlit**: For running the app in a browser.
- **Requests**: For sending API requests to Hugging Face.
- **Hugging Face Token**: Required for accessing the models.

## How to Run the App Locally

Follow the steps below to run the **Multilingual Hate Speech Detection App** on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/multilingual-hate-speech-detection.git
cd multilingual-hate-speech-detection
```

### 2. Install dependencies
Make sure you have Python 3.7 or later installed, then install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Add Hugging Face Token
- Create a `secrets.toml` file (if you don't have it already) in the root directory of the project and add your Hugging Face API token like so:
  ```toml
  [api]
  huggingface_token = "your_hugging_face_api_token"
  ```

You can obtain your Hugging Face API token by signing up on [Hugging Face](https://huggingface.co/) and generating a token in your account settings.

### 4. Run the App
To launch the app, run the following command:
```bash
streamlit run app.py
```

This will open the app in your default web browser. Now, you can input any text, and the app will analyze it for hate speech and toxicity.

## How to Use the App
1. **Input Text**: Type or paste any text in the text input box.
2. **Language Detection**: The app will first detect the language of the text.
3. **Translation (if needed)**: If the text is not in English, the app will automatically translate it.
4. **Hate Speech Detection**: The app will analyze the translated or original text and display the hate speech or toxicity results.

## Background
- **Positive Scenario**: A peaceful, neutral background is displayed if no significant toxicity is detected.
- **Negative Scenario**: If the text is identified as toxic or hateful, the background will change to a more ominous one.

## Contributing
Feel free to fork the repository, open issues, or submit pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
