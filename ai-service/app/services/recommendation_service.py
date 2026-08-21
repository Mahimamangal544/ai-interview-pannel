from typing import Dict, Any

class RecommendationService:
    def generate_recommendations(self, score: float) -> Dict[str, str]:
        """
        Formulates structural recommendations based on performance.
        """
        if score >= 8.0:
            return {
                "summary": "Excellent performance! The candidate showed deep system architecture and language proficiency.",
                "recommendations": "Explore advanced system design topics, cloud deployments, and concurrent algorithms."
            }
        elif score >= 5.0:
            return {
                "summary": "Good conceptual understanding with minor implementation gaps.",
                "recommendations": "Review database indexing, practice code complexity, and study framework lifecycles."
            }
        else:
            return {
                "summary": "Requires improvement. Significant difficulty with base structures.",
                "recommendations": "Focus on core OOP concepts, simple data structures, and fundamental algorithms."
            }
