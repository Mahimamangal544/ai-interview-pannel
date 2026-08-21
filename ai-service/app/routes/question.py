from fastapi import APIRouter
from app.models.schemas import GenerateQuestionRequest, QuestionResponse, NextQuestionRequest
from app.services.question_service import QuestionService
from app.session_store import sessions

router = APIRouter(prefix="/ai", tags=["question"])
question_service = QuestionService()


@router.post("/generate-question", response_model=QuestionResponse)
def generate_question(request: GenerateQuestionRequest):
    q = question_service.get_initial_question(request.skill, request.topic, request.difficulty)
    return QuestionResponse(
        question=q["question"],
        skill=q["skill"],
        topic=q["topic"],
        difficulty=q["difficulty"]
    )


@router.post("/next-question", response_model=QuestionResponse)
def next_question(request: NextQuestionRequest):
    session = sessions.get(request.interview_id)
    diff = request.difficulty

    if session:
        session["scores"].append(request.last_score)
        diff = session["difficulty"]

    q = question_service.get_next_adaptive_question(request.last_score, diff)

    if session:
        session["difficulty"] = q["difficulty"]

    return QuestionResponse(
        question=q["question"],
        skill=q["skill"],
        topic=q["topic"],
        difficulty=q["difficulty"]
    )
