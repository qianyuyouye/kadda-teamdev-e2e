from src.app import healthcheck, PROFILE_TITLE


def test_healthcheck():
    assert healthcheck() == "ok"


def test_rule_eb4dcc62_profile_title_is_personal_profile():
    assert PROFILE_TITLE == "个人资料"
