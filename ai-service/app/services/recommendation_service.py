from typing import Dict, Any, List


class RecommendationService:

    def generate_recommendations(
        self,
        skill_scores: Dict[str, float]
    ) -> List[str]:

        recommendations = []

        for skill, score in skill_scores.items():

            if score < 50:

                recommendations.append(
                    f"Focus on {skill} fundamentals and "
                    f"practice basic concepts regularly."
                )

            elif score < 60:

                recommendations.append(
                    f"Improve {skill} by practicing more "
                    f"problems and strengthening core concepts."
                )

            elif score < 70:

                recommendations.append(
                    f"Practice intermediate {skill} concepts "
                    f"and improve problem-solving ability."
                )

            elif score < 80:

                recommendations.append(
                    f"Revise intermediate {skill} concepts "
                    f"and focus on practical implementation."
                )

        # No weak skill
        if not recommendations:

            recommendations.append(
                "Maintain the current technical performance "
                "and continue practicing advanced concepts."
            )

        return recommendations

    def generate_summary(
        self,
        overall_score: float,
        skill_scores: Dict[str, float],
        strengths: List[str],
        weaknesses: List[str]
    ) -> str:

        # Strength text
        if strengths:

            strength_text = ", ".join(strengths)

        else:

            strength_text = "No major strengths identified"

        # Weakness text
        if weaknesses:

            weakness_text = ", ".join(weaknesses)

        else:

            weakness_text = "No major weaknesses identified"

        summary = (
            f"The candidate achieved an overall technical "
            f"score of {overall_score}/100. "
            f"Strong areas include {strength_text}. "
            f"Areas requiring improvement include "
            f"{weakness_text}."
        )

        return summary