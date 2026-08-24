import os
import json
from typing import Dict, Any

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