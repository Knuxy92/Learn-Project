from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def filter_paid(df: pd.DataFrame) -> pd.DataFrame:
    """คืนเฉพาะแถวที่สถานะเป็น paid โดยไม่สนตัวพิมพ์และช่องว่างหัวท้าย"""
    status = df["status"].str.strip().str.lower()
    return df.loc[status == "paid"]


def filter_by_country(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """คืนเฉพาะแถวที่ประเทศตรงกับ country หลังตัดช่องว่างและปรับตัวพิมพ์"""
    normalized = df["country"].str.strip().str.title()
    return df.loc[normalized == country.strip().title()]


def select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """คืน DataFrame ที่มีเฉพาะคอลัมน์ที่ระบุ ตามลำดับที่ให้"""
    return df.loc[:, columns]


def filter_amount(df: pd.DataFrame, min_total: float, column: str = "total") -> pd.DataFrame:
    """คืนเฉพาะแถวที่ค่าคอลัมน์ไม่น้อยกว่า min_total"""
    return df.loc[df[column] >= min_total]


if __name__ == "__main__":
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")
    paid = filter_paid(orders)
    print(f"ออเดอร์ที่จ่ายแล้ว {len(paid)} แถว จากทั้งหมด {len(orders)} แถว")
    print(paid[["order_id", "quantity", "status"]].head(5).to_string(index=False))

    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    thai = filter_by_country(customers, "thailand")
    print(f"\nลูกค้าประเทศไทย {len(thai)} แถว")
    print(thai[["customer_id", "country"]].to_string(index=False))

    products = pd.read_csv(RAW_DIR / "products.csv", encoding="utf-8")
    picked = select_columns(products, ["product_id", "list_price"])
    print("\nสองคอลัมน์ที่เลือก")
    print(picked.head(3).to_string(index=False))

    pricey = filter_amount(products, 1000, column="list_price")
    print(f"\nสินค้าราคา 1000 ขึ้นไป {len(pricey)} ชิ้น")
    print(pricey[["product_id", "list_price"]].to_string(index=False))
