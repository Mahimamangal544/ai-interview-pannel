import pytest
from app.services.question_service import QuestionService

qs = QuestionService()

def test_get_initial_question_returns_question():
    result = qs.get_initial_question(
        role="Backend Developer",
        skill="Java",
        topic="OOP",
        difficulty="EASY"
    )
    assert "question" in result
    assert "skill" in result
    assert "difficulty" in result
