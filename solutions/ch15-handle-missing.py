from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def missing_counts(df: pd.DataFrame) -> pd.Series:
    """คืนจำนวนค่าที่หายไปของแต่ละคอลัมน์ เฉพาะคอลัมน์ที่มากกว่าศูนย์"""
    counts = df.isna().sum()
    return counts[counts > 0].astype(int)


def drop_missing_key(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """คืน DataFrame ที่ตัดแถวซึ่งคอลัมน์ที่ระบุเป็นค่าว่างออก"""
    return df.dropna(subset=[column])


def empty_to_na(series: pd.Series) -> pd.Series:
    """ตัดช่องว่างหัวท้ายแล้วเปลี่ยนข้อความว่างให้เป็นค่าที่หายไป"""
    return series.str.strip().replace("", pd.NA)


def fill_text(df: pd.DataFrame, column: str, value: str = "Unknown") -> pd.DataFrame:
    """คืนสำเนาที่เติมทั้งค่าว่างและค่าที่หายไปในคอลัมน์ด้วย value"""
    result = df.copy()
    result[column] = empty_to_na(result[column]).fillna(value)
    return result


if __name__ == "__main__":
    customers = pd.read_csv(RAW_DIR / "customers.csv", encoding="utf-8")
    print("จำนวนค่าที่หายไปในตารางลูกค้า")
    print(missing_counts(customers).to_string())

    without_email = drop_missing_key(customers, "email")
    print(f"\nลูกค้าที่มีอีเมล {len(without_email)} แถว จาก {len(customers)} แถว")

    filled = fill_text(customers, "loyalty_tier")
    print("\nระดับสมาชิกหลังเติมค่า")
    print(filled["loyalty_tier"].value_counts().to_string())
    print(f"ต้นฉบับยังมีค่าว่าง {customers['loyalty_tier'].isna().sum()} แถว")

    orders = pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8", keep_default_na=False)
    status = empty_to_na(orders["status"])
    print(f"\nสถานะที่เป็นค่าว่างหรือหายไป {status.isna().sum()} แถว")
    print(status.fillna("unknown").value_counts().to_string())
