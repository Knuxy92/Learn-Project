import pandas as pd
from helpers import import_exercise


def test_build_orders_has_expected_columns_and_rows():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()

    assert isinstance(orders, pd.DataFrame)
    assert list(orders.columns) == ["order_id", "customer_id", "quantity", "unit_price"]
    assert len(orders) == 4
    assert orders.loc[0, "order_id"] == "O0001"


def test_build_orders_has_numeric_types():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()

    assert pd.api.types.is_integer_dtype(orders["quantity"])
    assert pd.api.types.is_float_dtype(orders["unit_price"])


def test_add_revenue_returns_new_frame():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()
    result = module.add_revenue(orders)

    assert "revenue" not in orders.columns
    assert "revenue" in result.columns


def test_add_revenue_multiplies_quantity_by_price():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()
    result = module.add_revenue(orders)

    assert result["revenue"].tolist() == [8400.0, 5750.0, -450.0, 0.0]


def test_top_rows_sorts_descending_and_resets_index():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()
    result = module.top_rows(orders, 2, "unit_price")

    assert list(result.index) == [0, 1]
    assert result["unit_price"].tolist() == [4200.0, 1150.0]
    assert result["order_id"].tolist() == ["O0001", "O0002"]


def test_top_rows_does_not_mutate_input():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()
    before = orders.copy()
    module.top_rows(orders, 1, "quantity")

    pd.testing.assert_frame_equal(orders, before)


def test_column_types_reports_each_column():
    module = import_exercise("ch12-build-dataframe.py")

    orders = module.build_orders()
    types = module.column_types(orders)

    assert list(types) == ["order_id", "customer_id", "quantity", "unit_price"]
    assert types["quantity"] == "int64"
    assert types["unit_price"] == "float64"
    assert all(isinstance(value, str) for value in types.values())
