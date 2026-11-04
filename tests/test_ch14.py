import pandas as pd
import pytest
from helpers import import_exercise


@pytest.fixture()
def orders() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "order_id": ["O1", "O2", "O3", "O4", "O5"],
            "status": ["paid", " PAID ", "pending", "Paid", None],
            "country": ["Thailand", "thailand ", "LA", "THAILAND", "Laos"],
            "total": [450.0, 1200.0, 300.0, 2400.0, 90.0],
        }
    )


def test_filter_paid_ignores_case_and_spaces(orders):
    module = import_exercise("ch14-filter-orders.py")

    result = module.filter_paid(orders)

    assert result["order_id"].tolist() == ["O1", "O2", "O4"]


def test_filter_paid_does_not_mutate_input(orders):
    module = import_exercise("ch14-filter-orders.py")
    before = orders.copy()

    module.filter_paid(orders)

    pd.testing.assert_frame_equal(orders, before)


def test_filter_by_country_matches_normalized_value(orders):
    module = import_exercise("ch14-filter-orders.py")

    result = module.filter_by_country(orders, "thailand")

    assert result["order_id"].tolist() == ["O1", "O2", "O4"]


def test_filter_by_country_returns_empty_for_unknown_country(orders):
    module = import_exercise("ch14-filter-orders.py")

    result = module.filter_by_country(orders, "Japan")

    assert result.empty
    assert list(result.columns) == list(orders.columns)


def test_select_columns_keeps_requested_order(orders):
    module = import_exercise("ch14-filter-orders.py")

    result = module.select_columns(orders, ["total", "order_id"])

    assert list(result.columns) == ["total", "order_id"]
    assert len(result) == len(orders)


def test_filter_amount_includes_boundary(orders):
    module = import_exercise("ch14-filter-orders.py")

    result = module.filter_amount(orders, 1200.0)

    assert result["order_id"].tolist() == ["O2", "O4"]


def test_filter_amount_uses_given_column(orders):
    module = import_exercise("ch14-filter-orders.py")

    result = module.filter_amount(orders, 1000.0, column="total")

    assert len(result) == 2
