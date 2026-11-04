"""คำตอบอ้างอิง บทที่ 19 ตรวจคุณภาพข้อมูล"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def load_raw() -> tuple[pd.DataFrame, pd.DataFrame]:
    """อ่านตาราง orders และ customers จากโฟลเดอร์ข้อมูลดิบ"""
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    return orders, customers


def quality_report(df: pd.DataFrame) -> pd.DataFrame:
    """สรุปจำนวนค่าที่หายไป จำนวนค่าที่ไม่ซ้ำ และชนิดของแต่ละคอลัมน์"""
    rows = [
        {
            "column": column,
            "missing": int(df[column].isna().sum()),
            "unique": int(df[column].nunique(dropna=True)),
            "dtype": str(df[column].dtype),
        }
        for column in df.columns
    ]
    report = pd.DataFrame(rows, columns=["column", "missing", "unique", "dtype"])
    return report.sort_values("column").reset_index(drop=True)


def find_duplicates(df: pd.DataFrame, subset: list[str]) -> pd.DataFrame:
    """คืนทุกแถวที่ค่าใน subset ซ้ำกับแถวอื่น"""
    mask = df.duplicated(subset=subset, keep=False)
    return df.loc[mask].reset_index(drop=True)


def find_out_of_range(
    df: pd.DataFrame,
    column: str,
    low: float,
    high: float,
) -> pd.DataFrame:
    """คืนแถวที่ค่าของ column นอกช่วง low ถึง high แบบรวมขอบ"""
    values = pd.to_numeric(df[column], errors="coerce")
    mask = (values < low) | (values > high)
    return df.loc[mask].reset_index(drop=True)


def referential_issues(child: pd.DataFrame, parent: pd.DataFrame, key: str) -> pd.DataFrame:
    """คืนแถวของ child ที่ค่า key ไม่มีอยู่ใน parent"""
    parent_keys = parent[key].dropna().unique()
    mask = ~child[key].isin(parent_keys)
    return child.loc[mask].reset_index(drop=True)


def main() -> None:
    orders, customers = load_raw()

    print("ภาพรวมตาราง orders")
    print(quality_report(orders).to_string(index=False))

    duplicated_orders = find_duplicates(orders, ["order_id"])
    print(f"แถวที่ order_id ซ้ำ {len(duplicated_orders)} แถว")
    print(duplicated_orders[["order_id", "customer_id", "product_id"]].to_string(index=False))

    duplicated_customers = find_duplicates(customers, ["customer_id"])
    print(f"แถวที่ customer_id ซ้ำ {len(duplicated_customers)} แถว")

    orphans = referential_issues(orders, customers, "customer_id")
    print(f"ออเดอร์ที่ชี้ไปยังลูกค้าที่ไม่มี {len(orphans)} แถว")
    print(orphans[["order_id", "customer_id"]].to_string(index=False))

    bad_quantity = find_out_of_range(orders, "quantity", 1, 100)
    print(f"ออเดอร์ที่จำนวนอยู่นอกช่วงหนึ่งถึงหนึ่งร้อย {len(bad_quantity)} แถว")
    print(bad_quantity[["order_id", "quantity"]].to_string(index=False))


if __name__ == "__main__":
    main()
