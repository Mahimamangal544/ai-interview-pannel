import pytest
from app.services.evaluation_service import EvaluationService

ev = EvaluationService()

def test_evaluate_returns_expected_keys():
    result = ev.evaluate("What is inheritance?", "Inheritance allows a class to reuse fields and methods of another class.")
    assert "correctness" in result
    assert "technical_depth" in result
    assert "clarity" in result
    assert "completeness" in result
    assert "final_score" in result
    assert "feedback" in result

def test_evaluate_scores_are_valid_range():
    result = ev.evaluate("What is a REST API?", "A REST API uses HTTP requests.")
    assert 0.0 <= result["correctness"] <= 10.0
    assert 0.0 <= result["final_score"] <= 10.0
