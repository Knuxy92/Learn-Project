"""ตัวอย่างการหาแถวซ้ำในตาราง orders"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_orders() -> pd.DataFrame:
    """อ่านตาราง orders จากข้อมูลดิบ"""
    return pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")


def duplicate_rows(df: pd.DataFrame, subset: list[str]) -> pd.DataFrame:
    """คืนทุกแถวที่ค่าใน subset ซ้ำกับแถวอื่น"""
    return df.loc[df.duplicated(subset=subset, keep=False)]


def main() -> None:
    orders = load_orders()

    print(f"จำนวนแถวทั้งหมด {len(orders)}")
    print(f"order_id ที่ไม่ซ้ำ {orders['order_id'].nunique()}")

    repeated = duplicate_rows(orders, ["order_id"])
    print(f"แถวที่ order_id ซ้ำ {len(repeated)} แถว")
    print(repeated[["order_id", "customer_id", "product_id"]].to_string(index=False))

    deduped = orders.drop_duplicates(subset=["order_id"], keep="last")
    print(f"หลังเก็บแถวสุดท้ายของแต่ละ order_id เหลือ {len(deduped)} แถว")

    same_all_columns = orders.duplicated(keep=False).sum()
    print(f"แถวที่ซ้ำทุกคอลัมน์ {same_all_columns} แถว")


if __name__ == "__main__":
    main()
