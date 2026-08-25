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