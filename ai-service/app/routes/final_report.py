from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    FinalReportRequest,
    FinalReportResponse
)

from app.services.evaluation_store import (
    evaluation_store
)

from app.services.skill_analysis_service import (
    SkillAnalysisService
)

from app.services.recommendation_service import (
    RecommendationService
)


router = APIRouter(
    prefix="/api/final-report",
    tags=["Final Technical Report"]
)


skill_analysis_service = SkillAnalysisService()

recommendation_service = RecommendationService()


@router.post(
    "",
    response_model=FinalReportResponse
)
def generate_final_report(
    request: FinalReportRequest
):

    try:

        # ------------------------------------
        # Get all evaluations for interview
        # ------------------------------------

        evaluations = evaluation_store.get_evaluations(
            request.interview_id
        )

        # ------------------------------------
        # Check evaluations
        # ------------------------------------

        if not evaluations:

            raise HTTPException(
                status_code=404,
                detail=(
                    "No evaluated answers found for "
                    f"interview {request.interview_id}"
                )
            )

        # ------------------------------------
        # Skill analysis
        # ------------------------------------

        analysis = skill_analysis_service.analyze(
            evaluations
        )

        overall_score = analysis["overall_score"]

        skill_scores = analysis["skill_scores"]

        strengths = analysis["strengths"]

        weaknesses = analysis["weaknesses"]

        # ------------------------------------
        # Generate recommendations
        # ------------------------------------

        recommendations = (
            recommendation_service
            .generate_recommendations(
                skill_scores
            )
        )

        # ------------------------------------
        # Generate summary
        # ------------------------------------

        summary = (
            recommendation_service
            .generate_summary(
                overall_score,
                skill_scores,
                strengths,
                weaknesses
            )
        )

        # ------------------------------------
        # Final report
        # ------------------------------------

        return {
            "interview_id": request.interview_id,

            "overall_score": overall_score,

            "skill_scores": skill_scores,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "summary": summary,

            "recommendations": recommendations
        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate final report: {str(e)}"
        )