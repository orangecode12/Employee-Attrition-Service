import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model.bin'

with open (model_file, 'rb') as md_file:
    dv, model = pickle.load(md_file)

app = Flask('predict')

@app.route('/predict', methods = ['POST'])

def predict():
    employee = request.get_json()
    X = dv.transform([employee])
    y_pred = model.predict_proba(X)[0,1]
    prediction = 'Yes' if y_pred >= 0.34 else 'No'

    result = {
        'Employee is going to leave ': prediction,
        'The probability is ': y_pred
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)