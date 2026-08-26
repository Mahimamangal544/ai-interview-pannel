import pytest
from app.services.scoring_service import ScoringService

sc = ScoringService()

def test_calculate_score():
    result = sc.calculate_score(8.0, 7.0, 6.0, 9.0, 7.0)
    assert result == pytest.approx(7.4, rel=1e-2)

def test_validate_score_negative():
    result = sc.validate_score(-5.0)
    assert result == 0.0

def test_validate_score_too_high():
    result = sc.validate_score(15.0)
    assert result == 10.0

def test_validate_score_valid():
    result = sc.validate_score(8.5)
    assert result == 8.5
