"""แบบฝึกหัดบทที่ 13: อ่านและเขียน CSV ด้วย Pandas

โจทย์
เขียนฟังก์ชันทั้งสี่ตามข้อกำหนดใน curriculum/ch13
ให้คำนึงถึงการเข้ารหัสไฟล์และรูปแบบผลลัพธ์ที่โจทย์ระบุ

เส้นทางไฟล์เริ่มต้นและส่วนเรียกใช้งานเตรียมไว้ให้
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DEFAULT_CUSTOMERS_PATH = "data/raw/customers.csv"
DEFAULT_THAI_CUSTOMERS_PATH = "data/raw/customers_th.csv"


def load_customers(path: str | Path = DEFAULT_CUSTOMERS_PATH) -> pd.DataFrame:
    """อ่านไฟล์ CSV ลูกค้าภาษาอังกฤษด้วยการเข้ารหัส utf-8"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def load_thai_customers(path: str | Path = DEFAULT_THAI_CUSTOMERS_PATH) -> pd.DataFrame:
    """อ่านไฟล์ CSV ลูกค้าภาษาไทยที่บันทึกพร้อม BOM ด้วยการเข้ารหัส utf-8-sig"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def save_clean(df: pd.DataFrame, path: str | Path) -> None:
    """เขียนตารางลงไฟล์ CSV โดยไม่ใส่วงศ์ index และใช้การเข้ารหัส utf-8"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def shape_of(df: pd.DataFrame) -> tuple[int, int]:
    """คืนจำนวนแถวกับจำนวนคอลัมน์ของตาราง"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def main() -> None:
    customers = load_customers()
    print(shape_of(customers))
    print(customers.head(3).to_string())
    print()

    thai = load_thai_customers()
    print(shape_of(thai))
    print(thai.to_string())
    print()

    print(list(thai.columns))
    print(thai.loc[0, "name"])


if __name__ == "__main__":
    main()
