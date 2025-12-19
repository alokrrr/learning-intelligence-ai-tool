import joblib
import os

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build absolute path to model
MODEL_PATH = os.path.join(BASE_DIR, "models", "completion_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_completion(features_df):
    probs = model.predict_proba(
        features_df.drop("student_id", axis=1)
    )[:, 1]
    return probs
