# 📱 SMS Spam Detection

A Machine Learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)**.  
It uses **TF-IDF Vectorization** and a trained **Logistic Regression** model with a **custom probability threshold (0.3)** to improve spam detection accuracy.  
The project also provides a simple **Streamlit web app** for real-time predictions.

---

## 🚀 Features
✔️ Preprocessing of SMS text (cleaning & tokenization)  
✔️ Text vectorization using **TF-IDF**  
✔️ Classification with **Logistic Regression**  
✔️ **Custom probability threshold (0.3)** for improved spam recall  
✔️ Detailed evaluation (accuracy, classification report)  
✔️ Interactive **Streamlit app** for easy predictions  

---

## 📂 Project Structure
```bash
smspred/
├── app.py                     # Streamlit app for prediction
├── smspred.ipynb              # Jupyter Notebook (training & evaluation)
├── spam_model.pkl             # Saved Logistic Regression model
├── tfidf_vectorizer.pkl       # Saved TF-IDF vectorizer
├── sms+spam+collection/
│   ├── SMSSpamCollection      # Dataset file
│   └── readme                 # Dataset description
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation

---

## Dataset

The dataset used is SMSSpamCollection (from UCI ML Repository).
It contains labeled SMS messages in two categories:

Ham → Normal messages

Spam → Unwanted/advertisement messages

## 🤖 Model

Vectorizer: TF-IDF

Classifier: Logistic Regression

Custom Probability Threshold: 0.3

Saved model → spam_model.pkl

Saved vectorizer → tfidf_vectorizer.pkl

## 📈 Results

📊 Custom Threshold: 0.3
✅ Accuracy: 97.94%
