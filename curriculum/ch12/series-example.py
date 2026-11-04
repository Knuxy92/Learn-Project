from __future__ import annotations

import pandas as pd


def build_price_series() -> pd.Series:
    """สร้าง Series ราคาสินค้าสามรายการพร้อม index เป็นรหัสสินค้า"""
    return pd.Series(
        [450.0, 300.0, 60.0],
        index=["P001", "P002", "P003"],
        name="list_price",
    )


def build_quantity_series() -> pd.Series:
    """สร้าง Series จำนวนชิ้นที่ขายได้ของสองสินค้าแรก"""
    return pd.Series([2, 5], index=["P001", "P002"], name="quantity")


def build_price_series_from_dict() -> pd.Series:
    """สร้าง Series เดียวกันจากดิกชันนารีที่ใช้รหัสสินค้าเป็นกุญแจ"""
    return pd.Series({"P001": 450.0, "P002": 300.0, "P003": 60.0})


def main() -> None:
    prices = build_price_series()
    print(prices)
    print()

    print("ชื่อของ Series คือ", prices.name)
    print("ชนิดข้อมูลคือ", prices.dtype)
    print("index คือ", list(prices.index))
    print()

    print(prices.loc["P002"])
    print()

    print(prices + 10)
    print()

    quantities = build_quantity_series()
    print(prices * quantities)
    print()

    print(prices[prices > 400])
    print()

    print(prices.mean())
    print()

    from_dict = build_price_series_from_dict()
    print(from_dict)
    print()

    print(prices.to_list())


if __name__ == "__main__":
    main()
