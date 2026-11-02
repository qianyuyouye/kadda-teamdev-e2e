from src.invoice import INVOICE_TITLE


def test_rule_3185c3ca_invoice_title_constant():
    assert INVOICE_TITLE == "发票"
    assert isinstance(INVOICE_TITLE, str)
