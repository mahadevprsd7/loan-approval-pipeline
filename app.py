import joblib

model_loaded = joblib.load('loan_approval_pipeline.pkl')

data = [[2, 1, 0, 500000, 1000000, 10, 750, 3000000, 0, 500000, 400000]]

pred = model_loaded.predict(data)

if pred[0] == 1:
    print('Loan Approved')
else:
    print('Loan Rejected')