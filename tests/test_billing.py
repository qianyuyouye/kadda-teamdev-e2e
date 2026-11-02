from src.billing import BILLING_TITLE


def test_rule_cd987896_billing_title_is_my_billing():
    """Rule cd987896: src/billing.py must define BILLING_TITLE as string '我的账单'."""
    assert BILLING_TITLE == "我的账单"
    assert isinstance(BILLING_TITLE, str)
