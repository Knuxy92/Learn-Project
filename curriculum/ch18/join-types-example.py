"""ตัวอย่างชนิดของการเชื่อมตาราง"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    """อ่านตาราง orders กับ customers"""
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    return orders, customers


def join_with(orders: pd.DataFrame, customers: pd.DataFrame, how: str) -> pd.DataFrame:
    """เชื่อมตารางด้วย customer_id ตามชนิดที่กำหนด"""
    return orders.merge(customers, on="customer_id", how=how, suffixes=("", "_customer"))


def main() -> None:
    orders, customers = load_frames()

    for how in ("inner", "left", "right", "outer"):
        joined = join_with(orders, customers, how)
        print(f"แบบ {how} ได้ {len(joined)} แถว")

    left_join = join_with(orders, customers, "left")
    missing_customer = int(left_join["name"].isna().sum())
    print(f"แถวที่หาข้อมูลลูกค้าไม่เจอ {missing_customer} แถว")

    print("รหัสลูกค้าที่หาไม่เจอ")
    print(sorted(left_join.loc[left_join["name"].isna(), "customer_id"].unique()))


if __name__ == "__main__":
    main()
