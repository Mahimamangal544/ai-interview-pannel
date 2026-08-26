# working of this file 
#Java score calculate karna
#Spring Boot score calculate karna
#MySQL score calculate karna
#DSA score calculate karna
#OOP score calculate karna
#overall technical score calculate karna
#strongest skills identify karna
#weakest skills identify karna


from typing import Dict, List, Any
from collections import defaultdict


class SkillAnalysisService:

    STRENGTH_THRESHOLD = 80
    WEAKNESS_THRESHOLD = 60

    def analyze(
        self,
        evaluations: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        if not evaluations:
            return {
                "overall_score": 0,
                "skill_scores": {},
                "strengths": [],
                "weaknesses": []
            }

        # ----------------------------------------
        # Group evaluations by skill
        # ----------------------------------------

        skill_scores = defaultdict(list)

        for evaluation in evaluations:

            skill = evaluation.get("skill", "Unknown")

            final_score = evaluation.get(
                "final_score",
                0
            )

            # Convert 0-10 to 0-100
            score_100 = float(final_score) * 10

            skill_scores[skill].append(score_100)

        # ----------------------------------------
        # Calculate skill-wise average
        # ----------------------------------------

        final_skill_scores = {}

        for skill, scores in skill_scores.items():

            average_score = sum(scores) / len(scores)

            final_skill_scores[skill] = round(
                average_score,
                2
            )

        # ----------------------------------------
        # Calculate overall score
        # ----------------------------------------

        overall_score = (
            sum(final_skill_scores.values())
            / len(final_skill_scores)
        )

        overall_score = round(
            overall_score,
            2
        )

        # ----------------------------------------
        # Identify strengths
        # ----------------------------------------

        strengths = []

        for skill, score in final_skill_scores.items():

            if score >= self.STRENGTH_THRESHOLD:
                strengths.append(skill)

        # ----------------------------------------
        # Identify weaknesses
        # ----------------------------------------

        weaknesses = []

        for skill, score in final_skill_scores.items():

            if score < self.WEAKNESS_THRESHOLD:
                weaknesses.append(skill)

        return {
            "overall_score": overall_score,
            "skill_scores": final_skill_scores,
            "strengths": strengths,
            "weaknesses": weaknesses
        }