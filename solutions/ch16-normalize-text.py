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
    """ตัดช่องว่างหัวท้าย ยุบช่องว่างซ้อน และปรับตัวพิมพ์เป็นแบบคำขึ้นต้น"""
    trimmed = series.str.strip()
    collapsed = trimmed.str.replace(r"\s+", " ", regex=True)
    return collapsed.str.title()


def normalize_country(series: pd.Series) -> pd.Series:
    """แปลงชื่อประเทศทุกรูปแบบให้เหลือ Thailand หรือ Laos"""
    titled = series.str.strip().str.title()
    return titled.replace(COUNTRY_ALIASES)


def normalize_status(series: pd.Series) -> pd.Series:
    """แปลงสถานะเป็นตัวพิมพ์เล็ก รวม canceled เข้ากับ cancelled และเติม unknown"""
    lowered = series.str.strip().str.lower()
    unified = lowered.replace(STATUS_ALIASES)
    return unified.mask(unified.isna() | unified.eq(""), "unknown")


def normalize_category(series: pd.Series) -> pd.Series:
    """ตัดช่องว่างหัวท้ายและปรับชื่อหมวดสินค้าเป็นแบบคำขึ้นต้น"""
    return series.str.strip().str.title()


def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / name, encoding="utf-8")


def main() -> None:
    customers = load_csv("customers.csv")
    products = load_csv("products.csv")
    orders = load_csv("orders.csv")

    print("ชื่อลูกค้า ก่อนและหลัง")
    names = pd.DataFrame(
        {
            "ก่อน": customers["name"].head(4),
            "หลัง": clean_name(customers["name"]).head(4),
        }
    )
    print(names.to_string(index=False))

    print()
    print("ประเทศ ก่อนและหลัง")
    print(customers["country"].value_counts().to_string())
    print()
    print(normalize_country(customers["country"]).value_counts().to_string())

    print()
    print("สถานะ ก่อนและหลัง")
    print(orders["status"].value_counts(dropna=False).to_string())
    print()
    print(normalize_status(orders["status"]).value_counts().to_string())

    print()
    print("หมวดสินค้า ก่อนและหลัง")
    print(products["category"].unique().tolist())
    print(normalize_category(products["category"]).unique().tolist())


if __name__ == "__main__":
    main()
