from typing import Dict, Any, List

from app.services.llm_service import LLMService

class EvaluationService:

    def __init__(self):
        self.llm_service = LLMService()

    def evaluate(
        self,
        role: str,
        skill: str,
        topic: str,
        difficulty: str,
        question_text: str,
        answer_text: str,
        expected_concepts: List[str]
    ) -> Dict[str, Any]:
        """
        Coordinates text grading with LLM parameters.
        """
        return self.llm_service.evaluate_answer(
            role=role,
            skill=skill,
            topic=topic,
            difficulty=difficulty,
            question=question_text,
            answer=answer_text,
            expected_concepts=expected_concepts
        )
