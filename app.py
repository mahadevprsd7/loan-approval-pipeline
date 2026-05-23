from flask import Flask
import numpy as np
import joblib
import os

model_loaded = joblib.load('loan_approval_pipeline.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    data = [[2, 1, 0, 500000, 1000000, 10, 750, 3000000, 0, 500000, 400000]]

    pred = model_loaded.predict(data)

    if pred[0] == 1:
        return 'Loan Approved'
    else:
        return 'Loan Rejected'
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 5000))
    )