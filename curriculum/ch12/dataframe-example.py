from __future__ import annotations

import pandas as pd


def build_orders() -> pd.DataFrame:
    """สร้างตาราง orders จากรายการของดิกชันนารี"""
    rows = [
        {"order_id": "O0001", "customer_id": "C002", "quantity": 2, "unit_price": 4200.0},
        {"order_id": "O0002", "customer_id": "C006", "quantity": 5, "unit_price": 1150.0},
        {"order_id": "O0003", "customer_id": "C003", "quantity": -1, "unit_price": 450.0},
    ]
    return pd.DataFrame(rows)


def build_orders_from_columns() -> pd.DataFrame:
    """สร้างตารางเดียวกันจากดิกชันนารีที่เก็บคอลัมน์ละลิสต์"""
    columns = {
        "order_id": ["O0001", "O0002", "O0003"],
        "quantity": [2, 5, -1],
        "unit_price": [4200.0, 1150.0, 450.0],
    }
    return pd.DataFrame(columns)


def main() -> None:
    orders = build_orders()
    print(orders)
    print()

    print("shape คือ", orders.shape)
    print("columns คือ", list(orders.columns))
    print("index คือ", list(orders.index))
    print()

    print(orders.dtypes)
    print()

    quantity = orders["quantity"]
    print(type(quantity))
    print(quantity)
    print()

    print(orders.loc[0, "order_id"])
    print()

    with_revenue = orders.copy()
    with_revenue["revenue"] = with_revenue["quantity"] * with_revenue["unit_price"]
    print(with_revenue)
    print()

    print("ตารางเดิมมีคอลัมน์ revenue หรือไม่", "revenue" in orders.columns)
    print()

    print(with_revenue.sort_values("revenue", ascending=False).head(2))
    print()

    print(with_revenue.nlargest(2, "revenue").reset_index(drop=True))
    print()

    print(build_orders_from_columns())
    print()

    print(with_revenue[["order_id", "revenue"]].to_string(index=False))


if __name__ == "__main__":
    main()
