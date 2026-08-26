import pytest
from app.services.evaluation_service import EvaluationService
from app.services.llm_service import LLMService

ev = EvaluationService()

def test_evaluate_returns_expected_keys():
    result = ev.evaluate(
        role="Backend Developer",
        skill="Java",
        topic="OOP",
        difficulty="EASY",
        question_text="What is inheritance?",
        answer_text="Inheritance allows a class to reuse fields and methods of another class.",
        expected_concepts=["Reuse", "Class", "extends"]
    )
    assert "correctness" in result
    assert "technical_depth" in result
    assert "completeness" in result
    assert "clarity" in result
    assert "problem_solving" in result
    assert "final_score" in result
    assert "feedback" in result

def test_evaluate_scores_are_valid_range():
    result = ev.evaluate(
        role="Backend Developer",
        skill="API Design",
        topic="REST",
        difficulty="EASY",
        question_text="What is a REST API?",
        answer_text="A REST API uses HTTP requests.",
        expected_concepts=["HTTP", "Stateless"]
    )
    for key in ["correctness", "technical_depth", "completeness", "clarity", "problem_solving", "final_score"]:
        assert 0.0 <= result[key] <= 10.0
