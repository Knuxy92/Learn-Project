"""แบบฝึกหัดบทที่ 16: ทำความสะอาดข้อความและหมวดหมู่

โจทย์
เขียนฟังก์ชันทั้งสี่ตามข้อกำหนดใน curriculum/ch16
จัดการชื่อ ประเทศ สถานะ และหมวดสินค้าให้เป็นรูปแบบมาตรฐาน

ตารางข้อมูลและค่าจับคู่ที่โจทย์กำหนดเตรียมไว้ให้
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

COUNTRY_ALIASES = {
    "Th": "Thailand",
    "Thailand": "Thailand",
    "La": "Laos",
    "Laos": "Laos",
}

STATUS_ALIASES = {"canceled": "cancelled"}


def clean_name(series: pd.Series) -> pd.Series:
    """รับคอลัมน์ชื่อ คืนคอลัมน์ที่ตัดช่องว่างหัวท้าย ยุบช่องว่างซ้อน และปรับเป็นคำขึ้นต้น"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def normalize_country(series: pd.Series) -> pd.Series:
    """รับคอลัมน์ประเทศ คืนคอลัมน์ที่มีแค่ Thailand กับ Laos"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def normalize_status(series: pd.Series) -> pd.Series:
    """รับคอลัมน์สถานะ คืนคอลัมน์ตัวพิมพ์เล็ก รวม canceled เป็น cancelled ช่องว่างเป็น unknown"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def normalize_category(series: pd.Series) -> pd.Series:
    """รับคอลัมน์หมวดสินค้า คืนคอลัมน์ที่ตัดช่องว่างและปรับเป็นคำขึ้นต้น"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def main() -> None:
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    products = pd.read_csv(RAW_DIR / "products.csv", encoding="utf-8")
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")

    print(clean_name(customers["name"]).head().tolist())
    print(normalize_country(customers["country"]).unique().tolist())
    print(normalize_status(orders["status"]).unique().tolist())
    print(normalize_category(products["category"]).unique().tolist())


if __name__ == "__main__":
    main()
