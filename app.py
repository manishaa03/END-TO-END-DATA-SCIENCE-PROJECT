from flask import Flask, request, render_template
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", features_count=4)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)
        return render_template("index.html", features_count=4, prediction_text=f"Predicted Species: {prediction[0]}")
    except Exception as e:
        return render_template("index.html", features_count=4, prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
