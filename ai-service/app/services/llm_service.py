import os
<<<<<<< HEAD
from typing import Dict, Any, List

=======
import json
from typing import Dict, Any
>>>>>>> origin/main

from dotenv import load_dotenv
from openai import OpenAI

from app.models.prompts import ANSWER_EVALUATION_PROMPT


load_dotenv()


class LLMService:

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY", "")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        self.model = "openai/gpt-oss-20b"

    def generate_text(self, prompt: str) -> str:
<<<<<<< HEAD
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
=======

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not configured.")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()

    def evaluate_answer(
        self,
        role: str,
        skill: str,
        topic: str,
        difficulty: str,
        question: str,
        answer: str
    ) -> Dict[str, Any]:

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not configured.")

        prompt = ANSWER_EVALUATION_PROMPT.format(
            role=role,
            skill=skill,
            topic=topic,
            difficulty=difficulty,
            question=question,
            answer=answer
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert technical interviewer. Return only valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()

        try:
            result = json.loads(content)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Groq returned invalid JSON: {content}"
            ) from e

        required_fields = [
            "correctness",
            "technical_depth",
            "clarity",
            "completeness",
            "final_score",
            "feedback"
        ]

        for field in required_fields:
            if field not in result:
                raise ValueError(
                    f"Missing field in evaluation response: {field}"
                )

        return result
>>>>>>> origin/main
