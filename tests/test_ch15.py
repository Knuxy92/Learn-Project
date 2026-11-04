import pandas as pd
import pytest
from helpers import import_exercise


@pytest.fixture()
def customers() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "customer_id": ["C001", "C002", "C003", "C004"],
            "name": ["Somchai", None, "Malee", "Kanya"],
            "email": ["", "malee@example.com", None, "kanya@example.com"],
            "loyalty_tier": ["gold", "", "silver", None],
        }
    )


def test_missing_counts_returns_only_columns_with_gaps(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.missing_counts(customers)

    assert result.to_dict() == {"name": 1, "email": 1, "loyalty_tier": 1}


def test_missing_counts_uses_integer_dtype(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.missing_counts(customers)

    assert str(result.dtype) == "int64"


def test_missing_counts_on_complete_frame_is_empty():
    module = import_exercise("ch15-handle-missing.py")
    complete = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})

    result = module.missing_counts(complete)

    assert result.empty


def test_drop_missing_key_removes_none_rows(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.drop_missing_key(customers, "email")

    assert result["customer_id"].tolist() == ["C001", "C002", "C004"]
    assert len(customers) == 4


def test_empty_to_na_strips_and_converts_blank(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.empty_to_na(customers["loyalty_tier"])

    assert result.isna().tolist() == [False, True, False, True]
    assert result.iloc[0] == "gold"


def test_empty_to_na_strips_whitespace():
    module = import_exercise("ch15-handle-missing.py")
    series = pd.Series(["  gold  ", "   ", "silver"])

    result = module.empty_to_na(series)

    assert result.iloc[0] == "gold"
    assert result.isna().tolist() == [False, True, False]


def test_fill_text_fills_blank_and_missing(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.fill_text(customers, "loyalty_tier")

    assert result["loyalty_tier"].tolist() == ["gold", "Unknown", "silver", "Unknown"]


def test_fill_text_returns_copy(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.fill_text(customers, "loyalty_tier", value="none")

    assert customers["loyalty_tier"].iloc[0] == "gold"
    assert customers["loyalty_tier"].iloc[1] == ""
    assert pd.isna(customers["loyalty_tier"].iloc[3])
    assert result["loyalty_tier"].iloc[1] == "none"


def test_fill_text_uses_custom_value(customers):
    module = import_exercise("ch15-handle-missing.py")

    result = module.fill_text(customers, "name", value="ไม่ระบุ")

    assert result["name"].tolist() == ["Somchai", "ไม่ระบุ", "Malee", "Kanya"]
