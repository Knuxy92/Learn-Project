"""โจทย์ บทที่ 20 ประกอบเป็นไปป์ไลน์ทำความสะอาด

เขียนห้าฟังก์ชันให้ครบ แล้วรันไฟล์นี้เพื่อดูผลลัพธ์
"""

from pathlib import Path

import pandas as pd

COUNTRY_MAP = {"Th": "Thailand", "Thailand": "Thailand", "La": "Laos", "Laos": "Laos"}
STATUS_MAP = {"canceled": "cancelled"}
MASTER_COLUMNS = [
    "order_id",
    "customer_id",
    "name",
    "product_id",
    "product_name",
    "category",
    "quantity",
    "unit_price",
    "revenue",
    "order_date",
    "status",
]


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """รับตารางลูกค้าดิบ คืนตารางที่ตัดรหัสซ้ำและทำความสะอาดทุกคอลัมน์แล้ว"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """รับตารางออเดอร์ดิบ คืนตารางที่ตัดรหัสซ้ำ แปลงชนิด และทิ้งแถวที่ไม่มีกุญแจ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    """รับตารางสินค้าดิบ คืนตารางที่ชื่อสินค้ากับหมวดเป็นตัวพิมพ์สม่ำเสมอ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def build_master(
    orders: pd.DataFrame,
    customers: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:
    """รับสามตารางที่สะอาดแล้ว คืนตารางรวมที่มีคอลัมน์ revenue"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def run_pipeline(raw_dir: str | Path, out_dir: str | Path) -> dict[str, int]:
    """อ่านข้อมูลดิบจาก raw_dir เขียนผลลัพธ์ลง out_dir คืนจำนวนแถวของแต่ละตาราง"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    counts = run_pipeline("data/raw", "data/processed")
    for table, rows in counts.items():
        print(f"{table} {rows} แถว")
