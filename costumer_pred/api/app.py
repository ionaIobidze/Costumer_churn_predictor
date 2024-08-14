from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON data from request
    features = np.array(data['features']).reshape(1, -1)  # Convert to NumPy array and reshape for prediction
    prediction = model.predict(features)[0]  # Make prediction
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
