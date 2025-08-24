from flask import Flask,request,jsonify,render_template
import sklearn
import joblib
import pandas as pd
from predict_traffic import TrafficPred 




# Create the FLASK app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# Prediction endpoint
@app.route('/predict',methods = ['POST'])
def predict():
    lag1 = int(request.form['lag1'])
    lag2 = int(request.form['lag2'])
    output = TrafficPred(lag1,lag2)
    return render_template('index.html' , prediction_text=f'Prediction:{output}')

# Run the app
if __name__ == "__main__":
    app.run(debug=False)
