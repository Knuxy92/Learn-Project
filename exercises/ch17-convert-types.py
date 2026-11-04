from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

PRICE_NOISE = ("฿", ",")
ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"


def parse_price_series(series: pd.Series) -> pd.Series:
    """รับคอลัมน์ราคาเป็นข้อความ คืนคอลัมน์ทศนิยมที่ตัดสัญลักษณ์บาทและ comma แล้ว"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def parse_quantity(series: pd.Series) -> pd.Series:
    """รับคอลัมน์จำนวน คืนคอลัมน์จำนวนเต็มแบบมีช่องว่างได้"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def parse_dates(series: pd.Series) -> pd.Series:
    """รับคอลัมน์วันที่สามรูปแบบ คืนคอลัมน์ชนิดวันที่ โดยไม่สลับวันกับเดือน"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def add_month_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """รับตารางกับชื่อคอลัมน์วันที่ คืนตารางใหม่ที่เพิ่มคอลัมน์ month รูปแบบ ปี-เดือน"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def main() -> None:
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")

    print(parse_price_series(orders["unit_price"]).head().tolist())
    print(parse_quantity(orders["quantity"]).head().tolist())
    print(parse_dates(orders["order_date"]).head().tolist())
    months = add_month_column(orders, "order_date")
    print(months[["order_id", "month"]].head().to_string(index=False))


if __name__ == "__main__":
    main()
