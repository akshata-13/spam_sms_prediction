# 📱 SMS Spam Detection

A Machine Learning app built using **TF-IDF + Logistic Regression** and deployed with **Streamlit**.  
It classifies SMS messages as **Spam** or **Ham (Not Spam)** using text features.  
The model is trained on the popular **SMSSpamCollection dataset**.

---

# ✨ Features
- Detects whether an SMS is Spam or Ham
- Uses **TF-IDF Vectorization** for text features
- **Logistic Regression classifier** with a **custom threshold (0.3)**
- High accuracy (~98%)
- Clean and interactive **Streamlit interface**
- Easy local or cloud deployment

---

# 📊 Dataset
This app uses the **SMSSpamCollection dataset** (UCI ML Repository).  
It contains **5,574 SMS messages** labeled as:
- **Ham** → Normal messages  
- **Spam** → Unwanted/advertisement messages  

Dataset link: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection  

---

# 📈 Results
- **Custom Threshold**: 0.3  
- **Accuracy**: 97.94%  

# Run the app

streamlit run app.py

# ⚙️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/akshata-13/spam_sms_prediction
pip install -r requirements.txt


