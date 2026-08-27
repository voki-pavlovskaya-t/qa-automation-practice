import pytest
from scoring import calculate_score

@pytest.mark.parametrize("base_score, is_hard_level, expected", [
    (12, True, 24),
    (45, False, 45),
    (0, False, 0),
])
def test_earn_score(base_score, is_hard_level, expected):
    assert calculate_score(base_score, is_hard_level) == expected