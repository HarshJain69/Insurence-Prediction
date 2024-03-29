# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from main import load_and_preprocess_data, train_linear_regression, predict_for_new_customers

app = Flask(__name__)

# Load and preprocess data
df = load_and_preprocess_data("insurance.csv")

# Define features (X) and target variable (y)
X = df.drop(['charges'], axis=1)
y = df['charges']

# Train linear regression model
linreg = train_linear_regression(X, y)

# Define the exchange rate
exchange_rate_usd_to_egp = 15.0  # 1 USD = 15 EGP

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        age = int(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])

        # Create DataFrame for the new customer
        new_customer_data = {'age': age, 'bmi': bmi, 'children': children, 'smoker': smoker}
        new_customer_df = pd.DataFrame([new_customer_data])

        # Predict medical insurance cost for the new customer
        cost_pred = predict_for_new_customers(linreg, new_customer_df, X.columns)

        # Convert predicted cost to EGP
        cost_pred_egp = cost_pred * exchange_rate_usd_to_egp

        # Return prediction as JSON response
        return jsonify({'prediction': cost_pred_egp[0]})

if __name__ == '__main__':
    app.run(debug=True)
