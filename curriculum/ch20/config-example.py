"""ตัวอย่าง บทที่ 20 แยกกฎทำความสะอาดออกเป็นฟังก์ชันย่อย"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "data" / "raw"

COUNTRY_MAP = {"Th": "Thailand", "Thailand": "Thailand", "La": "Laos", "Laos": "Laos"}
STATUS_MAP = {"canceled": "cancelled"}


def normalize_country(series: pd.Series) -> pd.Series:
    titled = series.astype("string").str.strip().str.title()
    return titled.map(COUNTRY_MAP).fillna(titled)


def normalize_status(series: pd.Series) -> pd.Series:
    lowered = series.astype("string").str.strip().str.lower()
    filled = lowered.replace("", pd.NA).fillna("unknown")
    return filled.replace(STATUS_MAP)


def normalize_tier(series: pd.Series) -> pd.Series:
    titled = series.astype("string").str.strip().str.title()
    return titled.replace("", pd.NA).fillna("Unknown")


def parse_price(series: pd.Series) -> pd.Series:
    text = (
        series.astype("string")
        .str.replace("฿", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(r"\s+", "", regex=True)
    )
    return pd.to_numeric(text, errors="coerce")


def main() -> None:
    customers = pd.read_csv(RAW_DIR / "customers.csv", dtype=str)
    orders = pd.read_csv(RAW_DIR / "orders.csv", dtype=str)

    print("ประเทศก่อนและหลัง")
    print(customers["country"].value_counts().to_string())
    print()
    print(normalize_country(customers["country"]).value_counts().to_string())

    print()
    print("สถานะก่อนและหลัง")
    print(orders["status"].value_counts(dropna=False).to_string())
    print()
    print(normalize_status(orders["status"]).value_counts().to_string())

    print()
    print("ระดับสมาชิกก่อนและหลัง")
    print(customers["loyalty_tier"].value_counts(dropna=False).to_string())
    print()
    print(normalize_tier(customers["loyalty_tier"]).value_counts().to_string())

    print()
    print("ราคาต่อหน่วยที่แปลงได้และแปลงไม่ได้")
    prices = parse_price(orders["unit_price"])
    print(f"แปลงได้ {prices.notna().sum()} แถว แปลงไม่ได้ {prices.isna().sum()} แถว")


if __name__ == "__main__":
    main()
