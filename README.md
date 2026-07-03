# 💳 Credit Card Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a credit card application is likely to be **Approved** or **Rejected** using Machine Learning. A Flask web application provides a simple interface where users enter applicant details and receive a prediction instantly.

The model was trained using historical applicant information and credit records.

---
DEMO LINK:https://drive.google.com/file/d/1hibnLJB9lj_Gaj73Znhr90dd1uRwcSsD/view?usp=drive_link

## 🎯 Objective

The objective of this project is to:

- Predict credit card approval status using Machine Learning.
- Build an interactive web application using Flask.
- Demonstrate the end-to-end Machine Learning workflow from data preprocessing to deployment.

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- Joblib

---

## 📂 Project Structure

```
credit_card_approval/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── credit_card_model.pkl
│
├── notebook/
│   └── credit_card_approval.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── dataset/
```

---

## 📊 Features Used

The prediction model uses the following applicant details:

- Gender
- Own Car
- Own House
- Number of Children
- Annual Income
- Income Type
- Education Type
- Family Status
- Housing Type
- Age
- Years Employed
- Occupation Type
- Number of Family Members

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Handling Missing Values
4. Label Encoding
5. Feature Selection
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving using Joblib
10. Flask Web Application Development

---

## 🚀 How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/your-username/credit_card_approval.git
```

### Open the Project Folder

```bash
cd credit_card_approval
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Application Screens

### Home Page

- User enters applicant details.
- Clicks the **Predict** button.

### Result Page

The application displays either:

- ✅ Credit Card Approved

or

- ❌ Credit Card Rejected

---

## 📈 Model

- Algorithm: Random Forest Classifier
- Data Preprocessing:
  - Missing Value Handling
  - Label Encoding
  - Feature Selection
- Model saved using Joblib.

---

## 🎓 Learning Outcomes

Through this project, we learned:

- Data preprocessing techniques
- Feature engineering
- Machine Learning model training
- Flask web development
- Model deployment
- GitHub project management

---

## 👥 Team Members

- Team Leader: Hema
- Team Members:
  - nerella lakshmi thanmai
  - harika patti
  - patan jahur
  - poornima.p


---

## 📌 Future Enhancements

- Improve prediction accuracy using advanced models.
- Add user authentication.
- Store prediction history in a database.
- Deploy the application to a cloud platform.
- Improve UI/UX with charts and dashboards.

---

## 📄 License

This project is developed for educational purposes as part of an academic Machine Learning project.

---

## ⭐ Acknowledgement

We would like to thank our faculty members and institution for their guidance and support throughout the development of this project.
