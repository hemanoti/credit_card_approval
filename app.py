from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("models/credit_card_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Convert Age and Years Employed into dataset format
    age = int(request.form["AGE"])
    days_birth = -(age * 365)

    years_employed = int(request.form["YEARS_EMPLOYED"])
    days_employed = -(years_employed * 365)

    # Create input data
    data = {
        "CODE_GENDER": int(request.form["CODE_GENDER"]),
        "FLAG_OWN_CAR": int(request.form["FLAG_OWN_CAR"]),
        "FLAG_OWN_REALTY": int(request.form["FLAG_OWN_REALTY"]),
        "CNT_CHILDREN": int(request.form["CNT_CHILDREN"]),
        "AMT_INCOME_TOTAL": float(request.form["AMT_INCOME_TOTAL"]),
        "NAME_INCOME_TYPE": int(request.form["NAME_INCOME_TYPE"]),
        "NAME_EDUCATION_TYPE": int(request.form["NAME_EDUCATION_TYPE"]),
        "NAME_FAMILY_STATUS": int(request.form["NAME_FAMILY_STATUS"]),
        "NAME_HOUSING_TYPE": int(request.form["NAME_HOUSING_TYPE"]),
        "DAYS_BIRTH": days_birth,
        "DAYS_EMPLOYED": days_employed,
        "OCCUPATION_TYPE": int(request.form["OCCUPATION_TYPE"]),
        "CNT_FAM_MEMBERS": float(request.form["CNT_FAM_MEMBERS"])
    }

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    if prediction[0] == 0:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)