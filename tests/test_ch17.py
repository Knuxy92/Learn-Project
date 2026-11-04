import pandas as pd
import pytest
from helpers import import_exercise


@pytest.fixture(scope="module")
def module():
    return import_exercise("ch17-convert-types.py")


def test_parse_price_series_strips_symbols(module):
    result = module.parse_price_series(pd.Series(["450", "฿1,150", "", "300.00"]))

    assert result.tolist()[:2] == [450.0, 1150.0]
    assert pd.isna(result.tolist()[2])
    assert result.tolist()[3] == 300.0


def test_parse_price_series_returns_float_dtype(module):
    result = module.parse_price_series(pd.Series(["450", "฿1,150", "", "300.00"]))

    assert result.dtype == "float64"


def test_parse_price_series_handles_numeric_input(module):
    result = module.parse_price_series(pd.Series([450, 1150.5]))

    assert result.tolist() == [450.0, 1150.5]


def test_parse_quantity_returns_nullable_int(module):
    result = module.parse_quantity(pd.Series(["1", "", "-1"]))

    assert result.tolist() == [1, pd.NA, -1]
    assert str(result.dtype) == "Int64"


def test_parse_quantity_keeps_zero_and_negative(module):
    result = module.parse_quantity(pd.Series(["0", "-1", "3"]))

    assert result.tolist() == [0, -1, 3]


def test_parse_dates_reads_three_formats(module):
    result = module.parse_dates(pd.Series(["2024-05-25", "14/05/2024", "2024/04/25"]))

    assert [value.year for value in result.tolist()] == [2024, 2024, 2024]
    assert pd.api.types.is_datetime64_any_dtype(result)


def test_parse_dates_keeps_iso_month_and_day(module):
    result = module.parse_dates(pd.Series(["2025-06-11", "2025/11/08"]))

    assert result.iloc[0].month == 6
    assert result.iloc[0].day == 11
    assert result.iloc[1].month == 11
    assert result.iloc[1].day == 8


def test_parse_dates_keeps_day_first_for_slash_dates(module):
    result = module.parse_dates(pd.Series(["19/03/2025", "14/05/2024"]))

    assert result.iloc[0].month == 3
    assert result.iloc[0].day == 19
    assert result.iloc[1].month == 5
    assert result.iloc[1].day == 14


def test_parse_dates_marks_unparsable(module):
    result = module.parse_dates(pd.Series(["2024-05-25", "", "not a date"]))

    assert pd.isna(result.iloc[1])
    assert pd.isna(result.iloc[2])


def test_add_month_column_adds_year_month(module):
    df = pd.DataFrame({"order_date": ["2024-05-25", "14/05/2024", "2024/04/25"]})
    result = module.add_month_column(df, "order_date")

    assert result["month"].tolist() == ["2024-05", "2024-05", "2024-04"]


def test_add_month_column_marks_missing_date(module):
    df = pd.DataFrame({"order_date": ["2024-05-25", ""]})
    result = module.add_month_column(df, "order_date")

    assert result["month"].iloc[0] == "2024-05"
    assert pd.isna(result["month"].iloc[1])


def test_add_month_column_does_not_mutate_input(module):
    df = pd.DataFrame({"order_date": ["2024-05-25"]})
    module.add_month_column(df, "order_date")

    assert "month" not in df.columns
    assert df["order_date"].tolist() == ["2024-05-25"]


def test_add_month_column_accepts_datetime_column(module):
    df = pd.DataFrame({"order_date": pd.to_datetime(["2024-05-25"])})
    result = module.add_month_column(df, "order_date")

    assert result["month"].tolist() == ["2024-05"]


def test_price_and_quantity_on_real_orders(module):
    orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
    prices = module.parse_price_series(orders["unit_price"])
    quantities = module.parse_quantity(orders["quantity"])

    assert prices.notna().sum() == 39
    assert quantities.notna().sum() == 40
