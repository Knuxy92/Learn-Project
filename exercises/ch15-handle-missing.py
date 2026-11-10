"""แบบฝึกหัดบทที่ 15: จัดการ Missing Values

โจทย์
เขียนฟังก์ชันทั้งสี่ตามข้อกำหนดใน curriculum/ch15
พิจารณาทั้งค่าที่หายไปจริงและข้อความว่างตามที่บทเรียนอธิบาย

ข้อมูลตัวอย่างและส่วนเรียกใช้งานเตรียมไว้ให้
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

SAMPLE_CUSTOMERS = pd.DataFrame(
    {
        "customer_id": ["C001", "C002", "C003", "C004"],
        "name": ["Somchai", None, "Malee", "Kanya"],
        "email": ["", "malee@example.com", None, "kanya@example.com"],
        "loyalty_tier": ["gold", "", "silver", None],
    }
)


def missing_counts(df: pd.DataFrame) -> pd.Series:
    """รับตาราง คืนจำนวนค่าที่หายไปของแต่ละคอลัมน์ เฉพาะคอลัมน์ที่มากกว่าศูนย์"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def drop_missing_key(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """รับตารางกับชื่อคอลัมน์ คืนตารางที่ตัดแถวซึ่งคอลัมน์นั้นเป็นค่าว่างออก"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def empty_to_na(series: pd.Series) -> pd.Series:
    """รับ Series ข้อความ คืน Series ที่ตัดช่องว่างหัวท้ายและเปลี่ยนข้อความว่างเป็นค่าที่หายไป"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def fill_text(df: pd.DataFrame, column: str, value: str = "Unknown") -> pd.DataFrame:
    """รับตารางกับชื่อคอลัมน์ คืนสำเนาที่เติมทั้งข้อความว่างและค่าที่หายไปด้วย value"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")

    print(missing_counts(customers).to_string())

    without_email = drop_missing_key(customers, "email")
    print(f"เหลือ {len(without_email)} แถว")

    print(empty_to_na(SAMPLE_CUSTOMERS["email"]).tolist())

    filled = fill_text(SAMPLE_CUSTOMERS, "loyalty_tier")
    print(filled["loyalty_tier"].tolist())
