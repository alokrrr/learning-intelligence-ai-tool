import joblib

model = joblib.load("models/completion_model.pkl")

def predict_completion(features_df):
    probs = model.predict_proba(features_df.drop("student_id", axis=1))[:, 1]
    return probs
