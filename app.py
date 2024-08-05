from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS  # Import the CORS library

# Load the model and scaler
model = joblib.load('ridge_regression_model.pkl')
print("Model loaded successfully")

scaler = joblib.load('scaler.pkl')
print("Scaler loaded successfully")

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app

@app.route('/predict', methods=['POST'])
def predict():
    app.logger.debug("Request received")
    data = request.get_json(force=True)
    app.logger.debug(f"Received data: {data}")

    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        df = pd.DataFrame([data])
        app.logger.debug(f"DataFrame: {df}")
        df_scaled = scaler.transform(df)
        app.logger.debug(f"Scaled Data: {df_scaled}")
        prediction = model.predict(df_scaled)
        app.logger.debug(f"Prediction: {prediction}")
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
