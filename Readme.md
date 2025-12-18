🚀 Learning Intelligence AI Tool
🔹 What It Is

Executable AI-powered Learning Intelligence system

Built as a production-ready REST API

Designed for internship / training platforms

🔹 What It Solves

Predicts course completion

Detects early dropout risk

Identifies difficult chapters

Generates actionable insights for mentors

🔹 Core AI Capabilities

Binary Classification → Course completion prediction

Risk Scoring → HIGH / LOW risk students

Chapter Difficulty Detection → Time, score, dropout-based

Insight Generation → Human-readable summaries

🔹 AI Pipeline

JSON Input

Data Validation

Preprocessing

Feature Engineering

ML Model Inference

Chapter Analytics

Insight Generation

JSON Output

🔹 Tech Stack

Python

FastAPI

Scikit-learn

Pandas

Joblib

🔹 How to Run
git clone <repo-url>
cd learning_ai_tool
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

🔹 API Endpoints

GET /health → API status

POST /analyze → Learning analysis & predictions

🔹 ML Details

Model: Logistic Regression

Training: Offline

Inference: Loaded inside API

Reproducible predictions

🔹 Insights Output

High-risk students list

Key completion risk factors

Most difficult chapters

🔹 AI Usage Disclosure

AI tools used for architecture guidance & documentation

All ML logic and implementation written and verified independently

🔹 Why This Project Stands Out

No notebooks

Real AI tool, not a demo

Clean modular architecture

Explainable & actionable outputs

🔹 Assessment Compliance

✔ Executable AI tool

✔ Integrated ML model

✔ Risk detection

✔ Chapter difficulty analysis

✔ Insight generation
