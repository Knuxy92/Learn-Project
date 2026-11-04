from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_customers() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")


def main() -> None:
    customers = load_customers()
    names = customers["name"]

    print("ค่าดิบ")
    for value in names.head(4):
        print(repr(value))

    print()
    print("ตัดช่องว่างหัวท้าย")
    for value in names.str.strip().head(4):
        print(repr(value))

    print()
    print("ยุบช่องว่างซ้อนในชื่อ")
    padded = pd.Series(["  Somchai   Jaidee  ", "Malee  Wongsakul"])
    print(padded.str.strip().str.replace(r"\s+", " ", regex=True).tolist())

    print()
    print("ปรับตัวพิมพ์เป็นคำขึ้นต้น")
    for value in names.str.strip().str.title().head(4):
        print(repr(value))

    print()
    print("ตัวพิมพ์เล็กและใหญ่")
    tiers = customers["loyalty_tier"]
    print(tiers.unique().tolist())
    print(tiers.str.strip().str.title().unique().tolist())

    print()
    print("ค่าที่หายไปหลังปรับตัวพิมพ์")
    tier_clean = tiers.str.strip().str.title().fillna("Unknown")
    print(tier_clean.value_counts().to_string())


if __name__ == "__main__":
    main()
