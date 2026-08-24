from fastapi import APIRouter
from app.models.schemas import StartInterviewRequest, FinalReportRequest, FinalReportResponse
from app.services.scoring_service import ScoringService
from app.services.recommendation_service import RecommendationService
from app.session_store import sessions

router = APIRouter(prefix="/ai", tags=["interview"])

scoring_service = ScoringService()
recommendation_service = RecommendationService()


@router.post("/start-interview")
def start_interview(request: StartInterviewRequest):

    sessions[request.interview_id] = {
        "role": request.role,
        "skill": request.skill,
        "topic": request.topic,
        "difficulty": request.difficulty.upper(),
        "scores": [],
        "asked_questions": []
    }

    return {
        "status": "success",
        "message": f"Interview {request.interview_id} initialized."
    }


@router.post("/final-report", response_model=FinalReportResponse)
def final_report(request: FinalReportRequest):

    session = sessions.get(
        request.interview_id,
        {"scores": [7.5, 8.0, 7.8]}
    )

    avg_score = scoring_service.calculate_overall_score(
        session["scores"]
    )

    recs = recommendation_service.generate_recommendations(
        avg_score
    )

    return FinalReportResponse(
        overall_score=avg_score,
        summary=recs["summary"],
        recommendations=recs["recommendations"]
    )