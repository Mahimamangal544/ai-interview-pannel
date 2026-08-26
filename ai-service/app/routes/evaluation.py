from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    EvaluateAnswerRequest,
    EvaluationResponse
)

from app.services.evaluation_service import EvaluationService
from app.session_store import sessions


from app.services.evaluation_store import evaluation_store

router = APIRouter(prefix="/ai", tags=["evaluation"])

evaluation_service = EvaluationService()


@router.post("/evaluate-answer", response_model=EvaluationResponse)
def evaluate_answer(request: EvaluateAnswerRequest):

    try:
        eval_result = evaluation_service.evaluate(
            role=request.role,
            skill=request.skill,
            topic=request.topic,
            difficulty=request.difficulty,
            question_text=request.question_text,
            answer_text=request.answer_text,
            expected_concepts=request.expected_concepts
        )

        session = sessions.get(request.interview_id)

        if session:
            if "scores" not in session:
                session["scores"] = []
            session["scores"].append(eval_result["final_score"])

        # Store the evaluation in the central evaluation_store for the final report
        evaluation_store.add_evaluation(
            interview_id=request.interview_id,
            question_id=request.question_id,
            question_text=request.question_text,
            skill=request.skill,
            evaluation=eval_result
        )

        return EvaluationResponse(
            correctness=eval_result["correctness"],
            technical_depth=eval_result["technical_depth"],
            clarity=eval_result["clarity"],
            completeness=eval_result["completeness"],
            problem_solving=eval_result.get("problem_solving", 0.0),
            final_score=eval_result["final_score"],
            feedback=eval_result["feedback"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Evaluation failed: {str(e)}"
        )
