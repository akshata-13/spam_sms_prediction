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

---

## 📂 Project Structure
smspred/
│── app.py # Streamlit app for prediction
│── smspred.ipynb # Notebook for training & evaluation
│── sms+spam+collection/
│ │── SMSSpamCollection # Dataset file
│ │── readme # Dataset description
│── requirements.txt # Project dependencies
│── README.md # Documentation


---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/akshata-13/spam_sms_prediction.git
cd spam_sms_prediction/smspred

Install dependencies:

pip install -r requirements.txt

▶️ Usage
Run the Streamlit App
streamlit run app.py

📊 Dataset

The dataset used is SMSSpamCollection (UCI ML Repository).
It contains ham (non-spam) and spam SMS messages.

📈 Model

Vectorizer: TF-IDF

Classifier: Logistic Regression

Custom Probability Threshold: 0.3

Saved model → spam_model.pkl

Saved vectorizer → tfidf_vectorizer.pkl

📊 Results

📊 Custom Threshold: 0.3
✅ Accuracy: 97.94%
