import pytest 
from sports_pipeline.metrics import ip_to_outs, era

def test_invalid_additional_outs() -> None:
    with pytest.raises(ValueError):
        ip_to_outs("158.3")

def test_ip_to_outs_complete_innings() -> None:
    assert ip_to_outs("158.0") == 474

def test_ip_to_outs_with_partial_innings() -> None:
    assert ip_to_outs("158.2") == 476

def test_era() -> None:
    assert era(77, 553) == pytest.approx(3.76, abs=6.008)

def test_era_null() -> None:
    assert era(5, 0) is None

def test_k_rate() -> None:
    assert k_rate(248, 746) == pytest.approx(0.3324, abs=0.00009)

