import pytest
from app.services.scoring_service import ScoringService

sc = ScoringService()

def test_calculate_overall_score_average():
    result = sc.calculate_overall_score([8.0, 6.0, 7.0])
    assert result == pytest.approx(7.0, rel=1e-2)

def test_calculate_overall_score_empty():
    result = sc.calculate_overall_score([])
    assert result == 0.0

def test_calculate_overall_score_single():
    result = sc.calculate_overall_score([9.5])
    assert result == 9.5
