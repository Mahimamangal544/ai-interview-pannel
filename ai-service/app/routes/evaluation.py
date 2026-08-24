from fastapi import APIRouter
from app.models.schemas import EvaluateAnswerRequest, EvaluationResponse
from app.services.evaluation_service import EvaluationService
from app.session_store import sessions

router = APIRouter(prefix="/ai", tags=["evaluation"])

evaluation_service = EvaluationService()


@router.post("/evaluate-answer", response_model=EvaluationResponse)
def evaluate_answer(request: EvaluateAnswerRequest):

    eval_result = evaluation_service.evaluate(
        request.role,
        request.skill,
        request.topic,
        request.difficulty,
        request.question_text,
        request.answer_text
    )

    session = sessions.get(request.interview_id)

    if session:
        session["scores"].append(eval_result["final_score"])

    return EvaluationResponse(
        correctness=eval_result["correctness"],
        technical_depth=eval_result["technical_depth"],
        clarity=eval_result["clarity"],
        completeness=eval_result["completeness"],
        final_score=eval_result["final_score"],
        feedback=eval_result["feedback"]
    )