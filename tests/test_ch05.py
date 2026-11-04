from helpers import import_exercise


def test_clean_text_collapses_internal_spaces():
    module = import_exercise("ch05-cleaning-helpers.py")

    assert module.clean_text("  Somchai   Jaidee ") == "Somchai Jaidee"


def test_clean_text_handles_missing_values():
    module = import_exercise("ch05-cleaning-helpers.py")

    assert module.clean_text(None) == ""
    assert module.clean_text("") == ""


def test_parse_price_strips_currency_and_separators():
    module = import_exercise("ch05-cleaning-helpers.py")

    assert module.parse_price("฿1,150") == 1150.0
    assert module.parse_price("300.00") == 300.0
    assert module.parse_price(" 1,150 ") == 1150.0


def test_parse_price_returns_none_for_unusable_input():
    module = import_exercise("ch05-cleaning-helpers.py")

    assert module.parse_price("") is None
    assert module.parse_price(None) is None
    assert module.parse_price("abc") is None


def test_safe_int_converts_or_falls_back():
    module = import_exercise("ch05-cleaning-helpers.py")

    assert module.safe_int("12") == 12
    assert module.safe_int(7) == 7
    assert module.safe_int("x", -1) == -1
    assert module.safe_int(None) == 0
