import os
from typing import Dict, Any

class LLMService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")

    def generate_text(self, prompt: str) -> str:
        """
        Sends prompt to LLM or returns mock text if no key is configured.
        """
        if not self.api_key:
            return "Mock text response generated because OPENAI_API_KEY is not set."
        # Placeholder for real LLM client integration (e.g. openai.chat.completions.create)
        return "Real LLM integration placeholder text."

    def evaluate_answer(self, question: str, answer: str) -> Dict[str, Any]:
        """
        Returns structured evaluations from LLM or structured mock payload.
        """
        if not self.api_key:
            # High-fidelity mock evaluation
            return {
                "correctness": 8.0,
                "technical_depth": 7.0,
                "clarity": 9.0,
                "completeness": 6.5,
                "final_score": 7.6,
                "feedback": "Mock evaluation feedback: The candidate's response matches the core concept correctly, although deep details regarding concurrency control could be expanded."
            }
        
        # Real call will parse json from LLM output
        return {
            "correctness": 9.0,
            "technical_depth": 8.0,
            "clarity": 9.0,
            "completeness": 8.0,
            "final_score": 8.5,
            "feedback": "Real LLM parsing feedback."
        }
