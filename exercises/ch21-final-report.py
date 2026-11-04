"""โจทย์ บทที่ 21 งานท้าย ทำความสะอาดชุดข้อมูลจริง

เขียนให้ครบทุกขั้นแล้วรันไฟล์นี้เพื่อสร้างรายงานฉบับสมบูรณ์
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


def load_raw(raw_dir: str | Path = "data/raw") -> dict[str, pd.DataFrame]:
    """อ่านสามตารางดิบ คืนดิกชันที่มีคีย์ customers orders products"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def clean_all(raw: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """รับดิกชันตารางดิบ คืนดิกชันตารางที่ทำความสะอาดแล้วด้วยกฎเดิมจากบทที่แล้ว"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def build_master(cleaned: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """รับดิกชันตารางที่สะอาดแล้ว คืนตารางรวมที่มีคอลัมน์ revenue"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def customer_summary(master: pd.DataFrame) -> pd.DataFrame:
    """คืนตารางสรุปลูกค้าที่มีคอลัมน์ customer_id name orders revenue เรียงรายได้มากไปน้อย"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def monthly_summary(master: pd.DataFrame) -> pd.DataFrame:
    """คืนตารางสรุปรายเดือนที่มีคอลัมน์ month orders revenue เรียงเดือนเก่าไปใหม่"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def save_outputs(
    master: pd.DataFrame,
    customer_summary: pd.DataFrame,
    monthly_summary: pd.DataFrame,
    out_dir: str | Path,
) -> list[str]:
    """เขียนสามไฟล์ CSV ลง out_dir คืนรายชื่อไฟล์ที่เขียนเรียงตามตัวอักษร"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def run(raw_dir: str | Path, out_dir: str | Path) -> dict[str, int]:
    """รันทั้งไปป์ไลน์ คืนจำนวนแถวของทุกตารางที่ได้"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    counts = run("data/raw", "data/processed/final")
    for table, rows in counts.items():
        print(f"{table} {rows} แถว")
