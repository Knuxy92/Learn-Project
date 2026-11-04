"""ตัวอย่าง บทที่ 20 ไปป์ไลน์ทำความสะอาดแบบสั้น"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"


def load_table(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / name, dtype=str, encoding="utf-8")


def dedupe(df: pd.DataFrame, key: str) -> pd.DataFrame:
    return df.drop_duplicates(subset=[key], keep="last").reset_index(drop=True)


def main() -> None:
    customers = load_table("customers.csv")
    orders = load_table("orders.csv")

    print(f"ลูกค้าก่อนตัดซ้ำ {len(customers)} แถว")
    customers = dedupe(customers, "customer_id")
    print(f"ลูกค้าหลังตัดซ้ำ {len(customers)} แถว")

    print(f"ออเดอร์ก่อนตัดซ้ำ {len(orders)} แถว")
    orders = dedupe(orders, "order_id")
    print(f"ออเดอร์หลังตัดซ้ำ {len(orders)} แถว")

    orders["quantity"] = pd.to_numeric(orders["quantity"], errors="coerce").astype("Int64")
    master = orders.merge(customers, on="customer_id", how="left")
    master["revenue"] = master["quantity"] * pd.to_numeric(
        master["unit_price"].str.replace("฿", "", regex=False).str.replace(",", "", regex=False),
        errors="coerce",
    )

    print(f"ตารางรวม {len(master)} แถว")
    print(master[["order_id", "customer_id", "name", "revenue"]].head(4).to_string(index=False))


if __name__ == "__main__":
    main()
