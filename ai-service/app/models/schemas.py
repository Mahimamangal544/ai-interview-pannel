from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class StartInterviewRequest(BaseModel):
    interview_id: int
    role: str
    skill: str
    topic: str
    difficulty: str = "MEDIUM"

class GenerateQuestionRequest(BaseModel):
    interview_id: int
    role: str
    skill: str
    topic: str
    difficulty: str = "MEDIUM"

class QuestionResponse(BaseModel):
    question: str
    skill: str
    topic: str
    difficulty: str

class EvaluateAnswerRequest(BaseModel):
    interview_id: int
    question_id: int
    role: str
    skill: str
    topic: str
    difficulty: str
    question_text: str
    answer_text: str
    expected_concepts: List[str] = []

class EvaluationResponse(BaseModel):

    correctness: float = Field(..., ge=0.0, le=10.0)
    technical_depth: float = Field(..., ge=0.0, le=10.0)
    completeness: float = Field(..., ge=0.0, le=10.0)
    clarity: float = Field(..., ge=0.0, le=10.0)
    problem_solving: float = Field(..., ge=0.0, le=10.0)
    final_score: float = Field(..., ge=0.0, le=10.0)
    feedback: str

class NextQuestionRequest(BaseModel):
    interview_id: int
    last_score: float
    difficulty: str = "MEDIUM"

class FinalReportRequest(BaseModel):
    interview_id: int

class FinalReportResponse(BaseModel):

    interview_id: int

    overall_score: float

    skill_scores: Dict[str, float]

    strengths: List[str]

    weaknesses: List[str]

    summary: str

    recommendations: List[str]
