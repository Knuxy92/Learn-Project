from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

CUSTOMERS_PATH = Path("data/raw/customers.csv")
ORDERS_PATH = Path("data/raw/orders.csv")
THAI_CUSTOMERS_PATH = Path("data/raw/customers_th.csv")


def main() -> None:
    customers = pd.read_csv(CUSTOMERS_PATH, encoding="utf-8")
    print(customers.shape)
    print()

    print(customers.head(3).to_string())
    print()

    print(customers.dtypes)
    print()

    print(customers["country"].head(5).to_string())
    print()

    orders = pd.read_csv(ORDERS_PATH, encoding="utf-8")
    print(orders.dtypes)
    print()

    raw_orders = pd.read_csv(ORDERS_PATH, encoding="utf-8", dtype=str)
    print(raw_orders.dtypes)
    print()

    print(raw_orders[["quantity", "unit_price"]].head(3).to_string())
    print()

    print(raw_orders["quantity"].isna().sum())
    print()

    preview = pd.read_csv(ORDERS_PATH, encoding="utf-8", usecols=["order_id", "status"], nrows=3)
    print(preview.to_string())
    print()

    thai = pd.read_csv(THAI_CUSTOMERS_PATH, encoding="utf-8-sig")
    print(thai.shape)
    print(thai.to_string())
    print()

    print(list(thai.columns))
    print()

    with THAI_CUSTOMERS_PATH.open(encoding="utf-8", newline="") as file:
        plain_header = next(csv.reader(file))

    with THAI_CUSTOMERS_PATH.open(encoding="utf-8-sig", newline="") as file:
        sig_header = next(csv.reader(file))

    print("หัวตารางเมื่อเปิดด้วย utf-8 คือ", repr(plain_header[0]))
    print("หัวตารางเมื่อเปิดด้วย utf-8-sig คือ", repr(sig_header[0]))


if __name__ == "__main__":
    main()
