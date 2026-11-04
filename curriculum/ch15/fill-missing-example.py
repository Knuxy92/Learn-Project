from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_customers() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")


def main() -> None:
    customers = load_customers()

    filled = customers.copy()
    filled["loyalty_tier"] = filled["loyalty_tier"].str.strip().replace("", pd.NA)
    filled["loyalty_tier"] = filled["loyalty_tier"].fillna("Unknown")
    print("ระดับสมาชิกหลังเติมค่า")
    print(filled["loyalty_tier"].value_counts().to_string())
    print(f"ต้นฉบับยังมีค่าว่าง {customers['loyalty_tier'].isna().sum()} แถว")

    dropped = customers.dropna(subset=["email"])
    print(f"\nตัดแถวที่ไม่มีอีเมล เหลือ {len(dropped)} แถว")

    email_filled = customers["email"].fillna("ยังไม่มีอีเมล")
    print("\nอีเมลหลังเติมข้อความ")
    print(email_filled.loc[customers["customer_id"] == "C007"].to_string(index=False))

    forward = pd.Series([None, "a", None, None, "b"])
    print("\nเติมค่าด้วยค่าก่อนหน้า")
    print(forward.ffill().tolist())

    print("\nเติมค่าด้วยค่าถัดไป")
    print(forward.bfill().tolist())

    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8", keep_default_na=False)
    status = orders["status"].str.strip().replace("", pd.NA)
    print(f"\nสถานะที่ว่างเปล่าก่อนเติม {status.isna().sum()} แถว")
    print(status.fillna("unknown").value_counts().to_string())


if __name__ == "__main__":
    main()
