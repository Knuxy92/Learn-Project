from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_orders() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")


def main() -> None:
    orders = load_orders()
    prices = orders["unit_price"]

    print("ราคา ค่าดิบ")
    print(prices.head(6).tolist())

    print()
    print("ราคา หลังตัดสัญลักษณ์บาทกับ comma")
    cleaned = prices.str.replace("฿", "", regex=False).str.replace(",", "", regex=False)
    print(cleaned.head(6).tolist())

    print()
    print("ราคา หลังแปลงเป็นตัวเลข")
    numeric = pd.to_numeric(cleaned.str.strip(), errors="coerce")
    print(numeric.head(6).tolist())
    print(numeric.dtype)

    print()
    print("จำนวน ค่าดิบและชนิดที่อ่านได้")
    print(orders["quantity"].head(6).tolist())
    print(orders["quantity"].dtype)

    print()
    print("จำนวน หลังแปลงเป็นจำนวนเต็มแบบมีช่องว่าง")
    quantity = pd.to_numeric(orders["quantity"], errors="coerce").astype("Int64")
    print(quantity.head(6).tolist())
    print(quantity.dtype)

    print()
    print("จำนวนแถวที่ราคาแปลงไม่ได้")
    print(int(numeric.isna().sum()))

    print()
    print("จำนวนแถวที่จำนวนแปลงไม่ได้")
    print(int(quantity.isna().sum()))


if __name__ == "__main__":
    main()
