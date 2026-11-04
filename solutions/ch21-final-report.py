"""คำตอบอ้างอิง บทที่ 21 งานท้าย ทำความสะอาดชุดข้อมูลจริง"""

from pathlib import Path

import pandas as pd

COUNTRY_MAP = {"Th": "Thailand", "Thailand": "Thailand", "La": "Laos", "Laos": "Laos"}
STATUS_MAP = {"canceled": "cancelled"}
ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"
OUTPUT_FILES = ("customer_summary.csv", "master.csv", "monthly_summary.csv")
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
    """อ่านสามตารางดิบจากโฟลเดอร์ข้อมูลดิบ"""
    base = Path(raw_dir)
    return {
        "customers": pd.read_csv(base / "customers.csv", dtype=str, encoding="utf-8"),
        "orders": pd.read_csv(base / "orders.csv", dtype=str, encoding="utf-8"),
        "products": pd.read_csv(base / "products.csv", dtype=str, encoding="utf-8"),
    }


def parse_mixed_dates(series: pd.Series) -> pd.Series:
    """แปลงวันที่สามรูปแบบโดยแยกวันที่ขึ้นต้นด้วยปีออกมาก่อนเพื่อไม่ให้สลับวันกับเดือน"""
    text = series.astype("string").str.strip()
    iso_like = text.str.match(ISO_DATE_PATTERN)

    iso = pd.to_datetime(text.where(iso_like), format="mixed", dayfirst=False, errors="coerce")
    day_first = pd.to_datetime(
        text.where(~iso_like), format="mixed", dayfirst=True, errors="coerce"
    )

    return iso.fillna(day_first)


def clean_all(raw: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """ทำความสะอาดทั้งสามตารางด้วยกฎชุดเดียวกับบทที่แล้ว"""
    return {
        "customers": _clean_customers(raw["customers"]),
        "orders": _clean_orders(raw["orders"]),
        "products": _clean_products(raw["products"]),
    }


def _clean_customers(df: pd.DataFrame) -> pd.DataFrame:
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


def _clean_orders(df: pd.DataFrame) -> pd.DataFrame:
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


def _clean_products(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned["product_id"] = cleaned["product_id"].astype("string").str.strip()

    name = cleaned["product_name"].astype("string").str.strip()
    cleaned["product_name"] = name.str.replace(r"\s+", " ", regex=True).str.title()
    cleaned["category"] = cleaned["category"].astype("string").str.strip().str.title()

    return cleaned.reset_index(drop=True)


def build_master(cleaned: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """ต่อตารางออเดอร์เข้ากับลูกค้าและสินค้า แล้วคำนวณรายได้"""
    master = cleaned["orders"].merge(cleaned["customers"], on="customer_id", how="left")
    master = master.merge(cleaned["products"], on="product_id", how="left")
    master["revenue"] = master["quantity"] * master["unit_price"]

    return master[MASTER_COLUMNS].reset_index(drop=True)


def customer_summary(master: pd.DataFrame) -> pd.DataFrame:
    """สรุปจำนวนออเดอร์และรายได้ต่อลูกค้า เรียงจากรายได้มากไปน้อย"""
    summary = (
        master.groupby("customer_id", as_index=False)
        .agg(
            name=("name", "first"),
            orders=("order_id", "count"),
            revenue=("revenue", "sum"),
        )
        .sort_values("revenue", ascending=False)
        .reset_index(drop=True)
    )
    return summary[["customer_id", "name", "orders", "revenue"]]


def monthly_summary(master: pd.DataFrame) -> pd.DataFrame:
    """สรุปจำนวนออเดอร์และรายได้รายเดือน เรียงตามเดือนจากเก่าไปใหม่"""
    dated = master.assign(month=master["order_date"].dt.strftime("%Y-%m"))
    summary = (
        dated.groupby("month", as_index=False)
        .agg(orders=("order_id", "count"), revenue=("revenue", "sum"))
        .sort_values("month")
        .reset_index(drop=True)
    )
    return summary[["month", "orders", "revenue"]]


def save_outputs(
    master: pd.DataFrame,
    customer_summary: pd.DataFrame,
    monthly_summary: pd.DataFrame,
    out_dir: str | Path,
) -> list[str]:
    """เขียนผลลัพธ์สามไฟล์ลงโฟลเดอร์ปลายทาง"""
    output_path = Path(out_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    frames = {
        "master.csv": master,
        "customer_summary.csv": customer_summary,
        "monthly_summary.csv": monthly_summary,
    }
    for filename, frame in frames.items():
        frame.to_csv(output_path / filename, index=False, encoding="utf-8")

    return sorted(frames)


def run(raw_dir: str | Path, out_dir: str | Path) -> dict[str, int]:
    """รันทั้งไปป์ไลน์ตั้งแต่ข้อมูลดิบจนถึงไฟล์สรุป"""
    cleaned = clean_all(load_raw(raw_dir))
    master = build_master(cleaned)
    by_customer = customer_summary(master)
    by_month = monthly_summary(master)
    save_outputs(master, by_customer, by_month, out_dir)

    return {
        "customers": len(cleaned["customers"]),
        "orders": len(cleaned["orders"]),
        "products": len(cleaned["products"]),
        "master": len(master),
        "customer_summary": len(by_customer),
        "monthly_summary": len(by_month),
    }


def main() -> None:
    counts = run("data/raw", "data/processed/final")
    for table, rows in counts.items():
        print(f"{table} {rows} แถว")


if __name__ == "__main__":
    main()
