import os
from typing import Dict, Any, List


class LLMService:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")

    def generate_text(self, prompt: str) -> str:
        """
        Sends prompt to LLM or returns mock text if no API key is configured.
        """

        if not self.api_key:
            return "Mock text response generated because OPENAI_API_KEY is not set."

        # Real LLM integration can be added here later.
        return "Real LLM integration placeholder text."

    def evaluate_answer(
        self,
        question: str,
        answer: str,
        expected_concepts: List[str]
    ) -> Dict[str, Any]:
        """
        Evaluates candidate answer.

        Input:
        - question
        - candidate answer
        - expected concepts

        Output:
        - correctness
        - technical depth
        - completeness
        - clarity
        - problem solving
        - final score
        - feedback
        """

        # --------------------------------------------------
        # MOCK EVALUATION
        # Used when OPENAI_API_KEY is not configured.
        # --------------------------------------------------

        if not self.api_key:

            # Empty answer
            if not answer.strip():
                return {
                    "correctness": 0.0,
                    "technical_depth": 0.0,
                    "completeness": 0.0,
                    "clarity": 0.0,
                    "problem_solving": 0.0,
                    "final_score": 0.0,
                    "feedback": "The candidate did not provide an answer."
                }

            # Basic mock evaluation
            return {
                "correctness": 8.0,
                "technical_depth": 7.0,
                "completeness": 6.5,
                "clarity": 9.0,
                "problem_solving": 7.0,
                "final_score": 7.5,
                "feedback": (
                    "The candidate demonstrates a good understanding "
                    "of the core concept. The answer is clear, but "
                    "additional technical details and examples could "
                    "improve the response."
                )
            }

        # --------------------------------------------------
        # REAL LLM INTEGRATION
        # --------------------------------------------------

        # This section can later call OpenAI/Gemini/etc.
        # For now returning a structured placeholder response.

        return {
            "correctness": 9.0,
            "technical_depth": 8.0,
            "completeness": 8.0,
            "clarity": 9.0,
            "problem_solving": 8.0,
            "final_score": 8.4,
            "feedback": (
                "The candidate provided a strong technical answer "
                "with good clarity and understanding."
            )
        }