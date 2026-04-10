# 🛍️ Amazon Review Sentiment Analyser

A machine learning web app that classifies Amazon product reviews as positive or negative in real time using Natural Language Processing (NLP).

## 🔗 Live Demo
[👉 Click here to try the app](https://danielakbank-amazon-sentiment-analysis-appapp-tuvxjr.streamlit.app/)

---

## 📌 Project Overview

This project builds an end-to-end sentiment analysis pipeline on 500,000+ real Amazon food product reviews. Two models are trained, evaluated and compared, with the best model deployed as an interactive web application.

**Business Value:**
- Automatically identifies negative reviews so teams can respond faster
- Highlights recurring themes in positive reviews to reinforce strengths
- Scales to analyse thousands of reviews instantly — no manual reading required
- Supports data-driven decisions around product quality and customer experience

---

## 📊 Results

| Model | Accuracy | Macro F1 | Notes |
|-------|----------|----------|-------|
| Logistic Regression | 94% | 0.88 | Strong, fast baseline |
| Neural Network | 94% | 0.89 | Marginal improvement, higher compute cost |

**Key finding:** The logistic regression baseline matches the neural network in overall accuracy, demonstrating that simpler models can be highly effective when combined with strong feature engineering.

---

## 🗂️ Project Structure
amazon-sentiment-analysis/
│── data/                        # Raw data and saved visualisations
│── notebooks/
│     ├── 01_eda_baseline.ipynb  # EDA and logistic regression
│     └── 02_neural_network.ipynb# Neural network model
│── models/                      # Saved model files
│── app/
│     └── app.py                 # Streamlit web application
│── src/
│     └── preprocess.py          # Reusable text cleaning module
│── requirements.txt
└── README.md

---

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Data Processing | Python, Pandas, NumPy |
| NLP | TF-IDF, n-grams, regex |
| Machine Learning | Scikit-learn, Logistic Regression |
| Deep Learning | TensorFlow, Keras |
| Visualisation | Matplotlib, Seaborn, WordCloud |
| Deployment | Streamlit, Streamlit Cloud |
| Version Control | Git, GitHub |

---

## 🚀 Run Locally

```bash
git clone https://github.com/YOURUSERNAME/amazon-sentiment-analysis.git
cd amazon-sentiment-analysis
pip install -r requirements.txt
streamlit run app/app.py
```

---

## 📈 Business Insights

- **Negative reviews** frequently mention delivery issues, product quality, and misleading descriptions
- **Positive reviews** highlight taste, value for money, and repeat purchase intent
- The model achieves **94% accuracy** on unseen data with strong performance on both classes
- Class imbalance (85% positive / 15% negative) was handled using stratified splitting

---

## 👤 Author
**Your Name**  
[LinkedIn](YOUR_LINKEDIN_URL) | [GitHub](YOUR_GITHUB_URL)
