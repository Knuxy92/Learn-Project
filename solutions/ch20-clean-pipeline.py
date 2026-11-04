"""คำตอบอ้างอิง บทที่ 20 ประกอบเป็นไปป์ไลน์ทำความสะอาด"""

from pathlib import Path

import pandas as pd

COUNTRY_MAP = {"Th": "Thailand", "Thailand": "Thailand", "La": "Laos", "Laos": "Laos"}
STATUS_MAP = {"canceled": "cancelled"}
ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"
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


def parse_mixed_dates(series: pd.Series) -> pd.Series:
    """แปลงวันที่สามรูปแบบโดยแยกวันที่ขึ้นต้นด้วยปีออกมาก่อนเพื่อไม่ให้สลับวันกับเดือน"""
    text = series.astype("string").str.strip()
    iso_like = text.str.match(ISO_DATE_PATTERN)

    iso = pd.to_datetime(text.where(iso_like), format="mixed", dayfirst=False, errors="coerce")
    day_first = pd.to_datetime(
        text.where(~iso_like), format="mixed", dayfirst=True, errors="coerce"
    )

    return iso.fillna(day_first)


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """ทำความสะอาดตารางลูกค้าและตัดรหัสลูกค้าซ้ำโดยเก็บแถวหลังสุด"""
    cleaned = df.copy()

    cleaned["customer_id"] = cleaned["customer_id"].astype("string").str.strip()
    cleaned = cleaned.drop_duplicates(subset=["customer_id"], keep="last")

    name = cleaned["name"].astype("string").str.strip()
    cleaned["name"] = name.str.replace(r"\s+", " ", regex=True).str.title()
    cleaned["email"] = cleaned["email"].astype("string").str.strip().str.lower()

    phone = cleaned["phone"].astype("string").str.replace(r"[()+\-\s]", "", regex=True)
    phone = phone.str.replace(r"^66", "0", regex=True)
    cleaned["phone"] = phone.where(phone.str.fullmatch(r"0\d{9}"), pd.NA)

    country = cleaned["country"].astype("string").str.strip().str.title()
    cleaned["country"] = country.map(COUNTRY_MAP).fillna(country)

    tier = cleaned["loyalty_tier"].astype("string").str.strip().str.title()
    cleaned["loyalty_tier"] = tier.replace("", pd.NA).fillna("Unknown")

    cleaned["signup_date"] = parse_mixed_dates(cleaned["signup_date"])

    return cleaned.reset_index(drop=True)


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """ทำความสะอาดตารางออเดอร์ ตัดรหัสออเดอร์ซ้ำ และทิ้งแถวที่ไม่มีกุญแจอ้างอิง"""
    cleaned = df.copy()

    for column in ("order_id", "customer_id", "product_id"):
        cleaned[column] = cleaned[column].astype("string").str.strip().replace("", pd.NA)

    cleaned = cleaned.drop_duplicates(subset=["order_id"], keep="last")
    cleaned = cleaned.dropna(subset=["order_id", "customer_id", "product_id"])

    cleaned["quantity"] = pd.to_numeric(cleaned["quantity"], errors="coerce").astype("Int64")

    price = (
        cleaned["unit_price"]
        .astype("string")
        .str.replace("฿", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(r"\s+", "", regex=True)
    )
    cleaned["unit_price"] = pd.to_numeric(price, errors="coerce")

    cleaned["order_date"] = parse_mixed_dates(cleaned["order_date"])

    status = cleaned["status"].astype("string").str.strip().str.lower()
    status = status.replace("", pd.NA).fillna("unknown")
    cleaned["status"] = status.replace(STATUS_MAP)

    return cleaned.reset_index(drop=True)


def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    """ทำความสะอาดชื่อสินค้าและหมวดสินค้าให้ตัวพิมพ์สม่ำเสมอ"""
    cleaned = df.copy()

    cleaned["product_id"] = cleaned["product_id"].astype("string").str.strip()

    name = cleaned["product_name"].astype("string").str.strip()
    cleaned["product_name"] = name.str.replace(r"\s+", " ", regex=True).str.title()
    cleaned["category"] = cleaned["category"].astype("string").str.strip().str.title()

    return cleaned.reset_index(drop=True)


def build_master(
    orders: pd.DataFrame,
    customers: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:
    """ต่อสามตารางเข้าด้วยกันและคำนวณรายได้ต่อแถว"""
    master = orders.merge(customers, on="customer_id", how="left")
    master = master.merge(products, on="product_id", how="left")
    master["revenue"] = master["quantity"] * master["unit_price"]

    return master[MASTER_COLUMNS].reset_index(drop=True)


def run_pipeline(raw_dir: str | Path, out_dir: str | Path) -> dict[str, int]:
    """อ่านข้อมูลดิบ ทำความสะอาด ต่อตาราง และเขียนผลลัพธ์ลงดิสก์"""
    raw_path = Path(raw_dir)
    output_path = Path(out_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    customers = clean_customers(pd.read_csv(raw_path / "customers.csv", dtype=str))
    orders = clean_orders(pd.read_csv(raw_path / "orders.csv", dtype=str))
    products = clean_products(pd.read_csv(raw_path / "products.csv", dtype=str))
    master = build_master(orders, customers, products)

    customers.to_csv(output_path / "customers_clean.csv", index=False, encoding="utf-8")
    master.to_csv(output_path / "master.csv", index=False, encoding="utf-8")

    return {
        "customers": len(customers),
        "orders": len(orders),
        "products": len(products),
        "master": len(master),
    }


def main() -> None:
    counts = run_pipeline("data/raw", "data/processed")
    for table, rows in counts.items():
        print(f"{table} {rows} แถว")


if __name__ == "__main__":
    main()
