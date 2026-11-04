from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_customers() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")


def main() -> None:
    customers = load_customers()

    print("จำนวนค่าที่หายไปต่อคอลัมน์")
    print(customers.isna().sum().to_string())

    print("\nเฉพาะคอลัมน์ที่มีค่าหายไป")
    counts = customers.isna().sum()
    print(counts[counts > 0].to_string())

    print("\nแถวที่อีเมลหายไป")
    print(customers.loc[customers["email"].isna(), ["customer_id", "email"]].to_string(index=False))

    print("\nแถวที่ไม่มีค่าหายไปเลย")
    complete = customers.loc[customers.notna().all(axis=1)]
    print(f"ได้ {len(complete)} แถว")

    print("\nเทียบข้อความว่างกับค่าที่หายไป")
    sample = pd.Series(["", "x", None])
    print(sample.isna().to_string())
    print(f"ข้อความว่างนับว่าหายไปหรือไม่ {sample.isna().iloc[0]}")

    print("\nสัดส่วนค่าที่หายไปเป็นเปอร์เซ็นต์")
    percent = (customers.isna().mean() * 100).round(1)
    print(percent.to_string())


if __name__ == "__main__":
    main()
