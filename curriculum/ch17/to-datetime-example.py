from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"


def load_orders() -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / "orders.csv", encoding="utf-8")


def parse_dates(series: pd.Series) -> pd.Series:
    text = series.astype("string").str.strip()
    iso_like = text.str.match(ISO_DATE_PATTERN)

    iso = pd.to_datetime(text.where(iso_like), format="mixed", dayfirst=False, errors="coerce")
    day_first = pd.to_datetime(
        text.where(~iso_like), format="mixed", dayfirst=True, errors="coerce"
    )

    return iso.fillna(day_first)


def main() -> None:
    orders = load_orders()
    raw_dates = orders["order_date"]

    print("วันที่ ค่าดิบ")
    print(raw_dates.head(6).tolist())

    print()
    print("แบบอ่านวันก่อนเดือน กับวันที่ขึ้นต้นด้วยปี")
    wrong = pd.to_datetime(raw_dates, format="mixed", dayfirst=True, errors="coerce")
    print(wrong.head(6).dt.strftime("%Y-%m-%d").tolist())

    print()
    print("แบบแยกวันที่ขึ้นต้นด้วยปีออกมาก่อน")
    correct = parse_dates(raw_dates)
    print(correct.head(6).dt.strftime("%Y-%m-%d").tolist())
    print(correct.dtype)

    print()
    print("วันที่ที่แปลงไม่ได้")
    print(raw_dates[correct.isna()].tolist())

    print()
    print("ดึงปี เดือน และวันออกมา")
    print(correct.dt.year.head(3).tolist())
    print(correct.dt.month.head(3).tolist())
    print(correct.dt.day.head(3).tolist())

    print()
    print("คอลัมน์ month รูปแบบ ปี-เดือน")
    months = correct.dt.strftime("%Y-%m")
    print(months.head(6).tolist())
    print(months.value_counts().sort_index().to_string())

    print()
    print("นับจำนวนออเดอร์ตามเดือน")
    orders_with_month = orders.assign(month=months)
    print(orders_with_month.groupby("month").size().to_string())


if __name__ == "__main__":
    main()
