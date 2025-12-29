# 🎓 Online Learning Dropout Prediction using Machine Learning

A Machine Learning–based project that predicts whether a student is likely to drop out of an online course using academic and demographic data.  
This project helps educational institutions identify at-risk students early and take preventive actions.

---

## 🔍 Problem Statement

Online learning platforms face high dropout rates due to lack of engagement, academic difficulty, and personal factors.  
Early identification of students at risk of dropping out can help institutions provide timely support and improve course completion rates.

---

## 🎯 Project Objective

- Predict student dropout using Machine Learning
- Analyze key factors influencing dropout
- Build a reliable classification model for early intervention

---

## 📊 Dataset Description

- Real-world student academic dataset
- Each record represents a student enrolled in an online course

### 📌 Features Used
- **Gender**
- **Age Band**
- **Highest Education**
- **Studied Credits**
- **Number of Previous Attempts**
- **IMD Band (Socio-economic indicator)**

### 🎯 Target Variable
- **dropout**
  - `1` → Student dropped out
  - `0` → Student continued the course

---

## 🧠 Machine Learning Approach

- **Problem Type:** Binary Classification
- **Algorithm Used:** Logistic Regression
- **Train–Test Split:** 80% – 20%

### 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score

---

## 🛠️ Technologies & Tools

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **IDE:** Visual Studio Code  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure
online-learning-dropout/
│
├── README.md
├── data.py # Data loading & preprocessing
├── features.py # Feature selection
├── model.py # Model training & evaluation
├── final_dataset.csv # Dataset
└── .gitignore

📈 Results

. The model successfully predicts student dropout

. Achieved ~70% accuracy

. Performs well in identifying non-dropout students

. Can be improved further using advanced models

⭐ Conclusion

This project demonstrates how Machine Learning can be applied in the education domain to reduce dropout rates and improve student success through data-driven insights.
