from typing import Dict, Any

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
        answer_text: str
    ) -> Dict[str, Any]:

        return self.llm_service.evaluate_answer(
            role=role,
            skill=skill,
            topic=topic,
            difficulty=difficulty,
            question=question_text,
            answer=answer_text
        )