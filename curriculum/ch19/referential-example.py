"""ตัวอย่างการตรวจความเชื่อมโยงระหว่างตาราง"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    """อ่านตาราง orders กับ customers"""
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    return orders, customers


def orphan_rows(child: pd.DataFrame, parent: pd.DataFrame, key: str) -> pd.DataFrame:
    """คืนแถวของ child ที่ค่า key ไม่มีอยู่ใน parent"""
    return child.loc[~child[key].isin(parent[key])]


def main() -> None:
    orders, customers = load_frames()

    print(f"รหัสลูกค้าในตารางลูกค้า {customers['customer_id'].nunique()} รหัส")
    print(f"รหัสลูกค้าที่ออเดอร์อ้างถึง {orders['customer_id'].nunique()} รหัส")

    orphans = orphan_rows(orders, customers, "customer_id")
    print(f"ออเดอร์ที่อ้างถึงลูกค้าที่ไม่มี {len(orphans)} แถว")
    print(orphans[["order_id", "customer_id"]].to_string(index=False))

    known = orders["customer_id"].isin(customers["customer_id"])
    print(f"ออเดอร์ที่อ้างถึงลูกค้าที่มีอยู่จริง {int(known.sum())} แถว")

    products = pd.read_csv(RAW_DIR / "products.csv", encoding="utf-8")
    print(f"ออเดอร์ที่อ้างถึงสินค้าที่ไม่มี {len(orphan_rows(orders, products, 'product_id'))} แถว")


if __name__ == "__main__":
    main()
