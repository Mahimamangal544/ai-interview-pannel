from typing import List, Dict, Any

class ScoringService:
    def calculate_overall_score(self, scores: List[float]) -> float:
        """
        Computes overall average score from a list of question scores.
        """
        if not scores:
            return 0.0
        return round(sum(scores) / len(scores), 2)
