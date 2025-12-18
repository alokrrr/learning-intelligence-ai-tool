from fastapi import FastAPI
from app.schemas import LearningData
from app.preprocess import preprocess_records
from app.features import build_features
from app.predict import predict_completion
from app.chapters import detect_chapter_difficulty
from app.insights import generate_insights

app = FastAPI(title="Learning Intelligence AI Tool")

# ---------------- HEALTH CHECK ----------------
@app.get("/health")
def health_check():
    return {"status": "API is running"}

# ---------------- MAIN ANALYSIS ENDPOINT ----------------
@app.post("/analyze")
def analyze_learning(data: LearningData):
    # Step 1: Preprocess raw records
    df = preprocess_records(data.records)

    # Step 2: Feature engineering (student-level)
    features = build_features(df)

    # Step 3: Predict course completion probability
    probs = predict_completion(features)

    results = []
    for i, row in features.iterrows():
        results.append({
            "student_id": row["student_id"],
            "completion_probability": round(float(probs[i]), 2),
            "risk": "HIGH" if probs[i] < 0.4 else "LOW"
        })

    # Step 4: Chapter difficulty detection
    chapter_difficulty_df = detect_chapter_difficulty(df)
    chapter_difficulty = chapter_difficulty_df.to_dict(orient="records")

    # Step 5: Generate human-readable insights
    insights = generate_insights(results, chapter_difficulty)

    # Step 6: Final response
    return {
        "students_analyzed": len(results),
        "results": results,
        "chapter_difficulty": chapter_difficulty,
        "insights": insights
    }
