from src.reduction import full_reduction


def test_rule_e0485eeb_full_200_minus_25():
    assert full_reduction(200) == 25
    assert full_reduction(199) == 10
    assert full_reduction(99) == 0


def test_rule_1842905d_negative_amount_returns_zero():
    assert full_reduction(-5) == 0
