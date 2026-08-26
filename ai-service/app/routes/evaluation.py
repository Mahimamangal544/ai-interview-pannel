from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    EvaluateAnswerRequest,
    EvaluationResponse
)

from app.services.evaluation_service import (
    EvaluationService
)


router = APIRouter(
    prefix="/api/evaluation",
    tags=["Evaluation"]
)


<<<<<<< HEAD
evaluation_service = EvaluationService()


@router.post(
    "",
    response_model=EvaluationResponse
)
def evaluate_answer(
    request: EvaluateAnswerRequest
):

    try:

        result = evaluation_service.evaluate(
            question_text=request.question_text,
            answer_text=request.answer_text,
            expected_concepts=request.expected_concepts
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Evaluation failed: {str(e)}"
        )
=======
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
>>>>>>> origin/main
