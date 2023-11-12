from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def make_prediction(features):
    prediction = model.predict([features])[0]
    return prediction

@app.route('/')
def home():
    return render_template('index.html', prediction=None, result_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[f]) for f in ["rd_spend", "administration", "marketing_spend"]]

        prediction = make_prediction(features)

        return render_template('index.html', prediction=prediction, result_text=f"Model Prediction: {prediction}")
    
    except ValueError:
        return render_template('index.html', prediction=None, result_text="Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    app.run(debug=True)
