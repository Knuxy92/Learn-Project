import pandas as pd
import pytest
from helpers import import_exercise

MODULE = "ch18-join-tables.py"


def make_orders() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "order_id": ["O1", "O2", "O3"],
            "customer_id": ["C1", "C2", "C9"],
            "product_id": ["P1", "P2", "P9"],
            "quantity": [1, 2, 3],
            "unit_price": [100.0, 50.0, 100.0],
        }
    )


def make_customers() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "customer_id": ["C1", "C2"],
            "name": ["Anan", "Malee"],
            "country": ["Thailand", "Laos"],
        }
    )


def make_products() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "product_id": ["P1", "P2"],
            "product_name": ["Keyboard", "Mouse"],
            "list_price": [100, 50],
        }
    )


def test_join_orders_customers_keeps_every_order_row():
    module = import_exercise(MODULE)
    joined = module.join_orders_customers(make_orders(), make_customers())

    assert len(joined) == 3
    assert joined["order_id"].tolist() == ["O1", "O2", "O3"]
    assert joined["name"].tolist()[:2] == ["Anan", "Malee"]
    assert pd.isna(joined["name"].iloc[2])


def test_join_orders_customers_suffixes_overlapping_columns():
    module = import_exercise(MODULE)
    orders = make_orders().assign(country="TH")
    joined = module.join_orders_customers(orders, make_customers())

    assert "country" in joined.columns
    assert "country_customer" in joined.columns


def test_join_orders_products_keeps_every_order_row():
    module = import_exercise(MODULE)
    joined = module.join_orders_products(make_orders(), make_products())

    assert len(joined) == 3
    assert joined["product_name"].tolist()[:2] == ["Keyboard", "Mouse"]
    assert pd.isna(joined["product_name"].iloc[2])


def test_unmatched_orders_returns_only_orphans():
    module = import_exercise(MODULE)
    orphans = module.unmatched_orders(make_orders(), make_customers())

    assert orphans["order_id"].tolist() == ["O3"]
    assert list(orphans.columns) == list(make_orders().columns)


def test_unmatched_orders_handles_all_matched():
    module = import_exercise(MODULE)
    orders = make_orders().iloc[:2]
    orphans = module.unmatched_orders(orders, make_customers())

    assert orphans.empty
    assert list(orphans.columns) == list(orders.columns)


def test_unmatched_orders_on_real_data_finds_c013_and_c014():
    module = import_exercise(MODULE)
    orders, customers, _ = module.load_raw()

    orphans = module.unmatched_orders(orders, customers)

    assert len(orphans) == 5
    assert sorted(orphans["customer_id"].unique()) == ["C013", "C014"]


def test_revenue_by_customer_sums_and_sorts_descending():
    module = import_exercise(MODULE)
    master = pd.DataFrame(
        {
            "customer_id": ["C1", "C1", "C2"],
            "revenue": [100.0, 50.0, 400.0],
        }
    )

    summary = module.revenue_by_customer(master)

    assert list(summary.columns) == ["customer_id", "revenue"]
    assert summary["customer_id"].tolist() == ["C2", "C1"]
    assert summary["revenue"].tolist() == [400.0, 150.0]
    assert summary.index.tolist() == [0, 1]


def test_revenue_by_customer_requires_revenue_column():
    module = import_exercise(MODULE)
    master = pd.DataFrame({"customer_id": ["C1"]})

    with pytest.raises(ValueError):
        module.revenue_by_customer(master)


def test_to_number_cleans_currency_text():
    module = import_exercise(MODULE)
    values = pd.Series(["฿1,150", "300.00", "", "-1"])

    result = module.to_number(values)

    assert result.iloc[0] == 1150.0
    assert result.iloc[1] == 300.0
    assert pd.isna(result.iloc[2])
    assert result.iloc[3] == -1.0
