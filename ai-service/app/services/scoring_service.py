from typing import Dict


class ScoringService:

    def calculate_score(
        self,
        correctness: float,
        technical_depth: float,
        completeness: float,
        clarity: float,
        problem_solving: float
    ) -> float:

        scores = [
            correctness,
            technical_depth,
            completeness,
            clarity,
            problem_solving
        ]

        final_score = sum(scores) / len(scores)

        return round(final_score, 2)

    def validate_score(self, score: float) -> float:

        if score < 0:
            return 0.0

        if score > 10:
            return 10.0

        return round(score, 2)