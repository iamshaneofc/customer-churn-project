from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model (replace 'your_model.pkl' with your actual model file)
model = pickle.load(open('model.sav', 'rb'))

# Define the exact columns your model expects
expected_cols = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender_Female', 'gender_Male',
                'Partner_No', 'Partner_Yes', 'Dependents_No', 'Dependents_Yes', 'PhoneService_No',
                'PhoneService_Yes', 'MultipleLines_No', 'MultipleLines_No phone service', 'MultipleLines_Yes',
                'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No', 'OnlineSecurity_No',
                'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No',
                'OnlineBackup_No internet service', 'OnlineBackup_Yes', 'DeviceProtection_No',
                'DeviceProtection_No internet service', 'DeviceProtection_Yes', 'TechSupport_No',
                'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No',
                'StreamingTV_No internet service', 'StreamingTV_Yes', 'StreamingMovies_No',
                'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_Month-to-month',
                'Contract_One year', 'Contract_Two year', 'PaperlessBilling_No', 'PaperlessBilling_Yes',
                'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)',
                'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'tenure_group_0-1 year',
                'tenure_group_1-2 years', 'tenure_group_2-3 years', 'tenure_group_3-4 years',
                'tenure_group_4-5 years', 'tenure_group_5-6 years']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect raw form data into a dictionary
    data = {
        'SeniorCitizen': 1 if request.form['SeniorCitizen'] == 'Yes' else 0,  # Map Yes/No to 1/0
        'MonthlyCharges': float(request.form['MonthlyCharges']),
        'TotalCharges': float(request.form['TotalCharges']),
        'gender': request.form['gender'],
        'Partner': request.form['Partner'],
        'Dependents': request.form['Dependents'],
        'PhoneService': request.form['PhoneService'],
        'MultipleLines': request.form['MultipleLines'],
        'InternetService': request.form['InternetService'],
        'OnlineSecurity': request.form['OnlineSecurity'],
        'OnlineBackup': request.form['OnlineBackup'],
        'DeviceProtection': request.form['DeviceProtection'],
        'TechSupport': request.form['TechSupport'],
        'StreamingTV': request.form['StreamingTV'],
        'StreamingMovies': request.form['StreamingMovies'],
        'Contract': request.form['Contract'],
        'PaperlessBilling': request.form['PaperlessBilling'],
        'PaymentMethod': request.form['PaymentMethod'],
        'tenure_group': request.form['tenure_group']
    }

    # Convert to a single-row DataFrame
    input_df = pd.DataFrame([data])

    # Perform one-hot encoding (mapping categorical to binary)
    input_df_encoded = pd.get_dummies(input_df)

    # Align with expected columns (add missing with 0s)
    for col in expected_cols:
        if col not in input_df_encoded.columns:
            input_df_encoded[col] = 0

    # Reorder columns to match model’s expected order
    input_df_encoded = input_df_encoded[expected_cols]

    # Make prediction
    prediction = model.predict(input_df_encoded)[0]  # Assuming binary output (e.g., 0 or 1)

    # Interpret prediction
    result = "Customer will likely to churn 😔" if prediction == 1 else "Customer will not likely to churn 😊"

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=False)