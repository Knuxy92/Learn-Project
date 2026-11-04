from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_orders() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")


def main() -> None:
    orders = load_orders()
    status = orders["status"].str.strip().str.lower()

    paid = orders.loc[status == "paid"]
    print(f"ออเดอร์ที่จ่ายแล้ว {len(paid)} แถว")
    print(paid[["order_id", "status"]].head(3).to_string(index=False))

    big_paid = orders.loc[(status == "paid") & (orders["quantity"] >= 2)]
    print(f"\nจ่ายแล้วและซื้อตั้งแต่ 2 ชิ้น {len(big_paid)} แถว")
    print(big_paid[["order_id", "quantity", "status"]].to_string(index=False))

    not_paid = orders.loc[status != "paid"]
    print(f"\nยังไม่จ่าย {len(not_paid)} แถว")

    selected = orders.loc[status.isin(["paid", "pending"]), ["order_id", "status"]]
    print(f"\nจ่ายแล้วหรือรอชำระ {len(selected)} แถว")

    in_range = orders.loc[orders["quantity"].between(2, 4)]
    print(f"\nจำนวนสินค้าระหว่าง 2 ถึง 4 {len(in_range)} แถว")

    by_query = orders.query("quantity > 3")
    print(f"\nquery หา quantity มากกว่า 3 ได้ {len(by_query)} แถว")
    print(by_query[["order_id", "quantity"]].to_string(index=False))

    subset = orders.loc[:, ["order_id", "customer_id"]]
    print(f"\nเลือกสองคอลัมน์ได้ขนาด {subset.shape}")


if __name__ == "__main__":
    main()
