"""ตัวอย่างการรวมตาราง orders กับ products"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_table(name: str) -> pd.DataFrame:
    """อ่านตารางจากโฟลเดอร์ข้อมูลดิบตามชื่อไฟล์"""
    return pd.read_csv(RAW_DIR / f"{name}.csv", encoding="utf-8")


def to_number(series: pd.Series) -> pd.Series:
    """แปลงข้อความตัวเลขที่มีสัญลักษณ์บาทหรือ comma ให้เป็นจำนวน"""
    cleaned = (
        series.astype("string")
        .str.replace("฿", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def add_revenue(orders: pd.DataFrame) -> pd.DataFrame:
    """เพิ่มคอลัมน์ revenue จากจำนวนชิ้นคูณราคาต่อหน่วย"""
    result = orders.copy()
    result["quantity"] = to_number(result["quantity"])
    result["unit_price"] = to_number(result["unit_price"])
    result["revenue"] = result["quantity"] * result["unit_price"]
    return result


def main() -> None:
    orders = load_table("orders")
    products = load_table("products")

    merged = orders.merge(products, on="product_id", how="left", suffixes=("", "_product"))
    print("คอลัมน์หลังรวม")
    print(list(merged.columns))
    print(f"แถวก่อนรวม {len(orders)} แถวหลังรวม {len(merged)}")

    with_revenue = add_revenue(merged)
    print("ห้าแถวแรกพร้อมยอดเงิน")
    print(
        with_revenue[["order_id", "product_name", "quantity", "unit_price", "revenue"]]
        .head(5)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
