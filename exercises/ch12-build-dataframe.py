"""แบบฝึกหัดบทที่ 12: สร้างและจัดการ DataFrame

โจทย์
เขียนฟังก์ชันทั้งสี่ตามข้อกำหนดใน curriculum/ch12
ต้องสร้างตาราง เพิ่มรายได้ เลือกแถวบนสุด และรายงานชนิดข้อมูล

ข้อมูลตัวอย่างและส่วนเรียกใช้งานเตรียมไว้ให้
"""

from __future__ import annotations

import pandas as pd

ORDER_COLUMNS = ["order_id", "customer_id", "quantity", "unit_price"]

ORDER_ROWS = [
    {"order_id": "O0001", "customer_id": "C002", "quantity": 2, "unit_price": 4200.0},
    {"order_id": "O0002", "customer_id": "C006", "quantity": 5, "unit_price": 1150.0},
    {"order_id": "O0003", "customer_id": "C003", "quantity": -1, "unit_price": 450.0},
    {"order_id": "O0004", "customer_id": "C001", "quantity": 0, "unit_price": 300.0},
]


def build_orders() -> pd.DataFrame:
    """สร้างตาราง orders จาก ORDER_ROWS

    คืนค่า DataFrame ที่มีคอลัมน์ order_id, customer_id, quantity, unit_price
    """
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """เพิ่มคอลัมน์ revenue เป็น quantity คูณ unit_price

    คืนค่า DataFrame ใหม่ ไม่แก้ตารางที่ส่งเข้ามา
    """
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def top_rows(df: pd.DataFrame, n: int, column: str) -> pd.DataFrame:
    """เลือก n แถวที่ค่าคอลัมน์มากที่สุด เรียงจากมากไปน้อย และรีเซ็ต index"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def column_types(df: pd.DataFrame) -> dict[str, str]:
    """คืนชื่อคอลัมน์พร้อมชนิดข้อมูลของแต่ละคอลัมน์เป็นข้อความ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def main() -> None:
    orders = build_orders()
    print(orders.to_string())
    print()

    with_revenue = add_revenue(orders)
    print(with_revenue.to_string())
    print()

    print(top_rows(with_revenue, 2, "revenue").to_string())
    print()

    print(column_types(with_revenue))


if __name__ == "__main__":
    main()
