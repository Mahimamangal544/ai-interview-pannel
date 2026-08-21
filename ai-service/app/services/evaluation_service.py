from typing import Dict, Any
from app.services.llm_service import LLMService

class EvaluationService:
    def __init__(self):
        self.llm_service = LLMService()

    def evaluate(self, question_text: str, answer_text: str) -> Dict[str, Any]:
        """
        Coordinates text grading with LLM parameters.
        """
        return self.llm_service.evaluate_answer(question_text, answer_text)
