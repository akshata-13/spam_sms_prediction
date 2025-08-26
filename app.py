# app.py
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained model and vectorizer
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.title("📱 SMS Spam Detector")
st.write("Type a message below to check if it's spam or not.")

user_input = st.text_area("✉️ Enter your SMS or email message:")

if st.button("🔍 Detect"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # Transform input and predict
        input_vec = vectorizer.transform([user_input])
        prob = model.predict_proba(input_vec)[0][1]  # Probability of spam
        label = "🚫 Spam" if prob >= 0.15 else "✅ Ham (Safe)"

        st.markdown(f"**Prediction:** {label}")
        st.markdown(f"**Spam Probability:** `{prob:.2f}`")
