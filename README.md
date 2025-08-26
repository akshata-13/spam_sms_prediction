# 📱 SMS Spam Detection

A Machine Learning project to detect whether an SMS message is **Spam** or **Ham (Not Spam)**.  
It uses **TF-IDF Vectorization** and a trained **Logistic Regression** classifier with a **custom probability threshold (0.3)** to improve spam detection.  
The project also provides an interactive **Streamlit app** for easy predictions.

---

## 🚀 Features
- Clean and preprocess SMS text
- Convert text to numerical features using **TF-IDF**
- Classify messages with **Logistic Regression**
- Uses a **custom probability threshold (0.3)** for better spam detection
- Evaluate model using accuracy, confusion matrix & classification report
- Interactive **Streamlit web app** (`app.py`)
- Dataset included (`SMSSpamCollection`)

## Run the Streamlit App

streamlit run app.py

## Install dependencies:
```bash
pip install -r requirements.txt
