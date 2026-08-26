import os
import random
from typing import Dict, Any, List

from dotenv import load_dotenv
from openai import OpenAI

from app.models.prompts import QUESTION_GENERATION_PROMPT

load_dotenv()


class QuestionService:

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if api_key:
            self.client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )
        else:
            self.client = None

        # Local fallback questions
        self.question_pool = [
            {
                "question": "What is inheritance in Java?",
                "skill": "Java",
                "topic": "OOP",
                "difficulty": "EASY"
            },
            {
                "question": "What are the rules of encapsulation in Java?",
                "skill": "Java",
                "topic": "OOP",
                "difficulty": "EASY"
            },
            {
                "question": "Explain the difference between HashMap and TreeMap in Java.",
                "skill": "Java",
                "topic": "Data Structures",
                "difficulty": "MEDIUM"
            },
            {
                "question": "How does Spring Boot resolve dependency injection cycles?",
                "skill": "Spring Boot",
                "topic": "Core",
                "difficulty": "MEDIUM"
            },
            {
                "question": "What are the ACID properties in database management systems?",
                "skill": "MySQL",
                "topic": "DBMS",
                "difficulty": "MEDIUM"
            },
            {
                "question": "How do database indexes speed up query performance?",
                "skill": "MySQL",
                "topic": "DBMS",
                "difficulty": "MEDIUM"
            },
            {
                "question": "Explain the difference between a process and a thread in Operating Systems.",
                "skill": "Operating Systems",
                "topic": "Processes",
                "difficulty": "MEDIUM"
            },
            {
                "question": "Design a system that handles 100k concurrent read/write requests. How would you design caching and replication?",
                "skill": "Algorithms",
                "topic": "System Design",
                "difficulty": "HARD"
            },
            {
                "question": "What is the time complexity of searching and balancing elements in a Red-Black Tree?",
                "skill": "Data Structures",
                "topic": "Trees",
                "difficulty": "HARD"
            },
        ]

    def generate_ai_question(
        self,
        role: str,
        skill: str,
        topic: str,
        difficulty: str,
        previous_questions: List[str] | None = None
    ) -> Dict[str, Any]:

        previous_questions = previous_questions or []

        prompt = QUESTION_GENERATION_PROMPT.format(
            role=role,
            skill=skill,
            topic=topic,
            difficulty=difficulty.upper(),
            previous_questions="\n".join(previous_questions)
            if previous_questions
            else "None"
        )

        try:
            response = self.client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=300
            )

            question = response.choices[0].message.content.strip()

            if not question:
                raise ValueError("AI returned an empty question")

            return {
                "question": question,
                "skill": skill,
                "topic": topic,
                "difficulty": difficulty.upper()
            }

        except Exception as e:
            print(f"AI question generation failed: {e}")
            return self.get_fallback_question(
                skill,
                topic,
                difficulty,
                previous_questions
            )

    def get_fallback_question(
        self,
        skill: str,
        topic: str,
        difficulty: str,
        previous_questions: List[str] | None = None
    ) -> Dict[str, Any]:

        previous_questions = previous_questions or []

        filtered = [
            q for q in self.question_pool
            if q["skill"].lower() == skill.lower()
            and q["topic"].lower() == topic.lower()
            and q["difficulty"].upper() == difficulty.upper()
            and q["question"] not in previous_questions
        ]

        if not filtered:
            filtered = [
                q for q in self.question_pool
                if q["skill"].lower() == skill.lower()
                and q["topic"].lower() == topic.lower()
            ]

        if not filtered:
            filtered = [
                q for q in self.question_pool
                if q["skill"].lower() == skill.lower()
            ]

        if not filtered:
            filtered = self.question_pool

        return random.choice(filtered)

    def get_initial_question(
        self,
        role: str,
        skill: str,
        topic: str,
        difficulty: str,
        previous_questions: List[str] | None = None
    ) -> Dict[str, Any]:

        return self.generate_ai_question(
            role=role,
            skill=skill,
            topic=topic,
            difficulty=difficulty,
            previous_questions=previous_questions
        )