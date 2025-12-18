import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Sample training data (for demo)
data = {
    "avg_time_spent": [30, 50, 20, 60, 15],
    "avg_score": [70, 85, 40, 90, 35],
    "chapters_attempted": [5, 10, 3, 12, 2],
    "completion_ratio": [0.7, 0.9, 0.3, 1.0, 0.2],
}

df = pd.DataFrame(data)

# Create target
df["completed_course"] = df["completion_ratio"].apply(lambda x: 1 if x >= 0.6 else 0)

X = df.drop("completed_course", axis=1)
y = df["completed_course"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "models/completion_model.pkl")

print("Model trained and saved.")
