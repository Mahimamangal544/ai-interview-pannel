import pytest
from app.services.question_service import QuestionService

qs = QuestionService()

def test_get_initial_question_returns_question():
    result = qs.get_initial_question("Java", "OOP", "EASY")
    assert "question" in result
    assert "skill" in result
    assert "difficulty" in result

def test_get_next_adaptive_question_low_score_returns_easy():
    result = qs.get_next_adaptive_question(3.0, "MEDIUM")
    assert result["difficulty"].upper() == "EASY"

def test_get_next_adaptive_question_high_score_returns_hard():
    result = qs.get_next_adaptive_question(9.5, "MEDIUM")
    assert result["difficulty"].upper() == "HARD"

def test_get_next_adaptive_question_medium_score():
    result = qs.get_next_adaptive_question(6.5, "MEDIUM")
    assert result["difficulty"].upper() == "MEDIUM"
