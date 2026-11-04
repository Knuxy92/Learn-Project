"""ตัวอย่าง บทที่ 21 รายงานคุณภาพข้อมูลก่อนทำความสะอาด"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"


def quality_report(df: pd.DataFrame, label: str) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "ตาราง": label,
            "คอลัมน์": df.columns,
            "ค่าหายไป": [int(df[column].isna().sum()) for column in df.columns],
            "ค่าไม่ซ้ำ": [int(df[column].nunique(dropna=True)) for column in df.columns],
            "ชนิด": [str(df[column].dtype) for column in df.columns],
        }
    )


def main() -> None:
    tables = {
        "customers": pd.read_csv(RAW_DIR / "customers.csv", dtype=str),
        "orders": pd.read_csv(RAW_DIR / "orders.csv", dtype=str),
        "products": pd.read_csv(RAW_DIR / "products.csv", dtype=str),
    }

    for label, frame in tables.items():
        print(quality_report(frame, label).to_string(index=False))
        print()

    customers = tables["customers"]
    orders = tables["orders"]
    print(f"รหัสลูกค้าซ้ำ {customers['customer_id'].duplicated().sum()} แถว")
    print(f"รหัสออเดอร์ซ้ำ {orders['order_id'].duplicated().sum()} แถว")

    known = set(customers["customer_id"])
    orphans = orders.loc[~orders["customer_id"].isin(known)]
    print(f"ออเดอร์ที่ไม่มีลูกค้า {len(orphans)} แถว")
    print(orphans[["order_id", "customer_id"]].to_string(index=False))


if __name__ == "__main__":
    main()
