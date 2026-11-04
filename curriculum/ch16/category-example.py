from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

COUNTRY_ALIASES = {
    "Th": "Thailand",
    "Thailand": "Thailand",
    "La": "Laos",
    "Laos": "Laos",
}

STATUS_ALIASES = {"canceled": "cancelled"}


def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / name, encoding="utf-8")


def main() -> None:
    customers = load_csv("customers.csv")
    orders = load_csv("orders.csv")
    products = load_csv("products.csv")

    print("ประเทศ ค่าดิบ")
    print(customers["country"].value_counts().to_string())

    print()
    print("ประเทศ หลังตัดช่องว่างและปรับตัวพิมพ์")
    titled = customers["country"].str.strip().str.title()
    print(titled.value_counts().to_string())

    print()
    print("ประเทศ หลังรวมชื่อเรียก")
    print(titled.replace(COUNTRY_ALIASES).value_counts().to_string())

    print()
    print("สถานะ ค่าดิบ")
    print(orders["status"].value_counts(dropna=False).to_string())

    print()
    print("สถานะ หลังปรับ")
    status = orders["status"].str.strip().str.lower().replace(STATUS_ALIASES)
    status = status.mask(status.isna() | status.eq(""), "unknown")
    print(status.value_counts().to_string())

    print()
    print("หมวดสินค้า ค่าดิบ")
    print(products["category"].unique().tolist())

    print()
    print("หมวดสินค้า หลังปรับ")
    print(products["category"].str.strip().str.title().unique().tolist())


if __name__ == "__main__":
    main()
