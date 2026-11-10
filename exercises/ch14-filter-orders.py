"""แบบฝึกหัดบทที่ 14: เลือกและกรองข้อมูล

โจทย์
เขียนฟังก์ชันทั้งสี่ตามข้อกำหนดใน curriculum/ch14
ใช้ข้อมูลตัวอย่างที่เตรียมไว้ทดสอบการกรองและเลือกคอลัมน์

ชื่อฟังก์ชัน พารามิเตอร์ และข้อมูลตัวอย่างเตรียมไว้ให้
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

SAMPLE_ORDERS = pd.DataFrame(
    {
        "order_id": ["O1", "O2", "O3", "O4"],
        "customer_id": ["C001", "C002", "C003", "C004"],
        "status": ["paid", " PAID ", "pending", "Paid"],
        "country": ["Thailand", "thailand ", "LA", "THAILAND"],
        "total": [450.0, 1200.0, 300.0, 2400.0],
    }
)


def filter_paid(df: pd.DataFrame) -> pd.DataFrame:
    """รับตารางออเดอร์ คืนเฉพาะแถวที่สถานะเป็น paid โดยไม่สนตัวพิมพ์และช่องว่างหัวท้าย"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def filter_by_country(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """รับตารางกับชื่อประเทศ คืนเฉพาะแถวที่ประเทศตรงกันหลังตัดช่องว่างและปรับตัวพิมพ์"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """รับตารางกับรายชื่อคอลัมน์ คืนตารางที่มีเฉพาะคอลัมน์เหล่านั้นตามลำดับที่ให้"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def filter_amount(df: pd.DataFrame, min_total: float, column: str = "total") -> pd.DataFrame:
    """รับตารางกับยอดขั้นต่ำ คืนเฉพาะแถวที่ค่าคอลัมน์ไม่น้อยกว่ายอดขั้นต่ำ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")

    paid = filter_paid(orders)
    print(f"ออเดอร์ที่จ่ายแล้ว {len(paid)} แถว")

    thai = filter_by_country(SAMPLE_ORDERS, "thailand")
    print(f"ลูกค้าประเทศไทยในตัวอย่าง {len(thai)} แถว")

    picked = select_columns(SAMPLE_ORDERS, ["order_id", "total"])
    print(picked.to_string(index=False))

    big = filter_amount(SAMPLE_ORDERS, 1000)
    print(f"ยอดตั้งแต่ 1000 ขึ้นไป {len(big)} แถว")
