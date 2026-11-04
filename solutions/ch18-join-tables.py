"""คำตอบอ้างอิง บทที่ 18 รวมตาราง"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def load_raw() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """อ่านตาราง orders customers และ products จากโฟลเดอร์ข้อมูลดิบ"""
    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    products = pd.read_csv(RAW_DIR / "products.csv", encoding="utf-8")
    return orders, customers, products


def join_orders_customers(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """ต่อตารางออเดอร์กับตารางลูกค้าด้วย customer_id แบบคงออเดอร์ทุกแถว"""
    return orders.merge(
        customers,
        on="customer_id",
        how="left",
        suffixes=("", "_customer"),
    )


def join_orders_products(orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    """ต่อตารางออเดอร์กับตารางสินค้าด้วย product_id แบบคงออเดอร์ทุกแถว"""
    return orders.merge(
        products,
        on="product_id",
        how="left",
        suffixes=("", "_product"),
    )


def unmatched_orders(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """คืนออเดอร์ที่ customer_id ไม่มีอยู่ในตารางลูกค้า"""
    merged = orders.merge(
        customers[["customer_id"]],
        on="customer_id",
        how="left",
        indicator=True,
    )
    orphans = merged.loc[merged["_merge"] == "left_only", orders.columns]
    return orphans.reset_index(drop=True)


def revenue_by_customer(master: pd.DataFrame) -> pd.DataFrame:
    """สรุปยอดรายได้ต่อลูกค้า เรียงจากมากไปน้อย"""
    if "revenue" not in master.columns:
        raise ValueError("ตารางต้องมีคอลัมน์ revenue ก่อนสรุปยอด")

    summary = (
        master.groupby("customer_id", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .reset_index(drop=True)
    )
    return summary


def to_number(series: pd.Series) -> pd.Series:
    """แปลงข้อความตัวเลขที่อาจมีสัญลักษณ์บาทหรือ comma ให้เป็นจำนวน"""
    cleaned = (
        series.astype("string")
        .str.replace("฿", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def main() -> None:
    orders, customers, products = load_raw()
    print(f"orders {len(orders)} แถว customers {len(customers)} แถว")

    raw_join = join_orders_customers(orders, customers)
    print(f"join ก่อนตัดรหัสลูกค้าซ้ำได้ {len(raw_join)} แถว")

    unique_customers = customers.drop_duplicates("customer_id")
    joined = join_orders_customers(orders, unique_customers)
    print(f"join หลังตัดรหัสลูกค้าซ้ำได้ {len(joined)} แถว")

    orphans = unmatched_orders(orders, customers)
    print(f"ออเดอร์ที่ไม่มีข้อมูลลูกค้า {len(orphans)} แถว")
    print(orphans[["order_id", "customer_id"]].to_string(index=False))

    with_products = join_orders_products(joined, products)
    print(f"รวมสินค้าแล้วได้ {len(with_products)} แถว")

    master = with_products.assign(
        quantity=to_number(with_products["quantity"]),
        unit_price=to_number(with_products["unit_price"]),
    )
    master = master.assign(revenue=master["quantity"] * master["unit_price"])

    summary = revenue_by_customer(master)
    print("ห้าอันดับลูกค้าที่มียอดรวมสูงสุด")
    print(summary.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
