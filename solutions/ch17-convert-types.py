from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

PRICE_NOISE = ("฿", ",")
ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"


def parse_price_series(series: pd.Series) -> pd.Series:
    """ตัดสัญลักษณ์บาทกับ comma แล้วแปลงราคาเป็นตัวเลขทศนิยม ค่าที่แปลงไม่ได้เป็นค่าว่าง"""
    text = series.astype("string")
    for symbol in PRICE_NOISE:
        text = text.str.replace(symbol, "", regex=False)
    return pd.to_numeric(text.str.strip(), errors="coerce").astype("float64")


def parse_quantity(series: pd.Series) -> pd.Series:
    """แปลงจำนวนเป็นจำนวนเต็มแบบมีช่องว่างได้ ค่าที่แปลงไม่ได้เป็นค่าว่าง"""
    numeric = pd.to_numeric(series.astype("string").str.strip(), errors="coerce")
    return numeric.astype("Int64")


def parse_dates(series: pd.Series) -> pd.Series:
    """แปลงวันที่สามรูปแบบให้เป็นชนิดวันที่ โดยแยกวันที่แบบปีขึ้นก่อนออกมาก่อน"""
    text = series.astype("string").str.strip()
    iso_like = text.str.match(ISO_DATE_PATTERN)

    iso = pd.to_datetime(text.where(iso_like), format="mixed", dayfirst=False, errors="coerce")
    day_first = pd.to_datetime(
        text.where(~iso_like), format="mixed", dayfirst=True, errors="coerce"
    )

    return iso.fillna(day_first)


def add_month_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """เพิ่มคอลัมน์ month รูปแบบ ปี-เดือน โดยไม่แก้ตารางต้นฉบับ"""
    result = df.copy()
    dates = result[column]
    if not pd.api.types.is_datetime64_any_dtype(dates):
        dates = parse_dates(dates)
    result["month"] = dates.dt.strftime("%Y-%m")
    return result


def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / name, encoding="utf-8")


def main() -> None:
    orders = load_csv("orders.csv")

    print("ราคาต่อหน่วย ก่อนและหลัง")
    prices = pd.DataFrame(
        {
            "ก่อน": orders["unit_price"].head(6),
            "หลัง": parse_price_series(orders["unit_price"]).head(6),
        }
    )
    print(prices.to_string(index=False))
    print(parse_price_series(orders["unit_price"]).dtype)

    print()
    print("จำนวน ก่อนและหลัง")
    quantities = pd.DataFrame(
        {
            "ก่อน": orders["quantity"].head(6),
            "หลัง": parse_quantity(orders["quantity"]).head(6),
        }
    )
    print(quantities.to_string(index=False))
    print(parse_quantity(orders["quantity"]).dtype)

    print()
    print("วันที่ ก่อนและหลัง")
    dates = pd.DataFrame(
        {
            "ก่อน": orders["order_date"].head(6),
            "หลัง": parse_dates(orders["order_date"]).head(6),
        }
    )
    print(dates.to_string(index=False))
    print(parse_dates(orders["order_date"]).dtype)

    print()
    print("คอลัมน์ month")
    with_month = add_month_column(orders, "order_date")
    print(with_month[["order_id", "order_date", "month"]].head(6).to_string(index=False))


if __name__ == "__main__":
    main()
