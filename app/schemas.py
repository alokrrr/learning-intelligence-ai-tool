from pydantic import BaseModel
from typing import List

class LearningRecord(BaseModel):
    student_id: str
    course_id: str
    chapter_id: str
    chapter_order: int
    time_spent: float
    score: float
    completed: int

class LearningData(BaseModel):
    records: List[LearningRecord]
