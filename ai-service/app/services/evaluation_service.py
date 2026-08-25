from typing import Dict, Any

from app.services.llm_service import LLMService


class EvaluationService:

    def __init__(self):
        self.llm_service = LLMService()

    def evaluate(
        self,
        question_text: str,
        answer_text: str,
        expected_concepts: list[str]
    ) -> Dict[str, Any]:

        return self.llm_service.evaluate_answer(
            question=question_text,
            answer=answer_text,
            expected_concepts=expected_concepts
        )