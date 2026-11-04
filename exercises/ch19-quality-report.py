"""โจทย์ บทที่ 19 ตรวจคุณภาพข้อมูล

เติมโค้ดในแต่ละฟังก์ชันให้ทำงานตามที่ docstring บอก
รันไฟล์นี้ด้วย `.venv/bin/python exercises/ch19-quality-report.py` เพื่อดูผล
"""

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
    """สรุปคอลัมน์ missing unique และ dtype ของทั้งตาราง เรียงตามชื่อคอลัมน์"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def find_duplicates(df: pd.DataFrame, subset: list[str]) -> pd.DataFrame:
    """คืนทุกแถวที่ค่าใน subset ซ้ำกับแถวอื่น"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def find_out_of_range(
    df: pd.DataFrame,
    column: str,
    low: float,
    high: float,
) -> pd.DataFrame:
    """คืนแถวที่ค่าของ column นอกช่วง low ถึง high แบบรวมขอบ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def referential_issues(child: pd.DataFrame, parent: pd.DataFrame, key: str) -> pd.DataFrame:
    """คืนแถวของ child ที่ค่า key ไม่มีอยู่ใน parent"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def main() -> None:
    orders, customers = load_raw()

    print("ภาพรวมตาราง orders")
    print(quality_report(orders).to_string(index=False))

    repeated = find_duplicates(orders, ["order_id"])
    print(f"แถวที่ order_id ซ้ำ {len(repeated)} แถว")

    orphans = referential_issues(orders, customers, "customer_id")
    print(f"ออเดอร์ที่ชี้ไปยังลูกค้าที่ไม่มี {len(orphans)} แถว")

    bad_quantity = find_out_of_range(orders, "quantity", 1, 100)
    print(f"ออเดอร์ที่จำนวนอยู่นอกช่วง {len(bad_quantity)} แถว")


if __name__ == "__main__":
    main()
