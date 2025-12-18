Learning Intelligence AI Tool
Overview

An executable AI-powered Learning Intelligence system that analyzes student behavior data to predict course completion, detect dropout risk early, identify difficult chapters, and generate actionable insights for mentors and administrators.

Built as a production-style REST API (not a notebook).

Key Capabilities

Course Completion Prediction (Binary Classification)

Early Dropout Risk Detection

Chapter Difficulty Analysis (time, score, dropout rate)

Human-Readable Insights for Decision Making

AI Pipeline
JSON Input → Validation → Preprocessing → Feature Engineering
→ ML Inference → Chapter Analytics → Insights → JSON Output

Tech Stack

Python, FastAPI

Scikit-learn, Pandas

Joblib (model persistence)

Run Locally
git clone <repo-url>
cd learning_ai_tool
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

API Usage

POST /analyze
Input: Student learning data (JSON)
Output: Completion probability, risk flags, chapter difficulty, insights

ML Details

Model: Logistic Regression

Training: Offline

Inference: Loaded inside API

Predictions are reproducible

AI Usage Disclosure

AI tools were used for architectural guidance and documentation support.
All ML logic, feature design, and implementation were independently written and verified.

Why This Project

Executable AI tool (no notebooks)

Clear ML → product integration

Production-ready structure

Explainable outputs for real users
