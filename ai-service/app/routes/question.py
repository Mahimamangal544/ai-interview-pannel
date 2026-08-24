from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    GenerateQuestionRequest,
    QuestionResponse,
    NextQuestionRequest
)

from app.services.question_service import QuestionService
from app.session_store import sessions


router = APIRouter(prefix="/ai", tags=["question"])

question_service = QuestionService()


@router.post("/generate-question", response_model=QuestionResponse)
def generate_question(request: GenerateQuestionRequest):

    session = sessions.get(request.interview_id)

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Interview session not found. Start the interview first."
        )

    # Generate question using session information
    q = question_service.get_initial_question(
        role=session["role"],
        skill=session["skill"],
        topic=session["topic"],
        difficulty=session["difficulty"],
        previous_questions=session["asked_questions"]
    )

    # Store question so it is not repeated
    session["asked_questions"].append(q["question"])

    return QuestionResponse(
        question=q["question"],
        skill=q["skill"],
        topic=q["topic"],
        difficulty=q["difficulty"]
    )


@router.post("/next-question", response_model=QuestionResponse)
def next_question(request: NextQuestionRequest):

    session = sessions.get(request.interview_id)

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Interview session not found. Start the interview first."
        )

    # Store candidate score
    session["scores"].append(request.last_score)

    # Adaptive difficulty
    current_difficulty = session["difficulty"]

    if request.last_score < 5:
        current_difficulty = "EASY"

    elif request.last_score >= 8:
        if current_difficulty == "EASY":
            current_difficulty = "MEDIUM"
        elif current_difficulty == "MEDIUM":
            current_difficulty = "HARD"
        else:
            current_difficulty = "HARD"

    session["difficulty"] = current_difficulty
    print("DEBUG - New difficulty:", current_difficulty)

    # Generate NEW AI question
    q = question_service.generate_ai_question(
        role=session["role"],
        skill=session["skill"],
        topic=session["topic"],
        difficulty=current_difficulty,
        previous_questions=session["asked_questions"]
    )

    # Save question to prevent repetition
    session["asked_questions"].append(q["question"])

    return QuestionResponse(
        question=q["question"],
        skill=q["skill"],
        topic=q["topic"],
        difficulty=q["difficulty"]
    )