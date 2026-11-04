def clean_text(value: str | None) -> str:
    if value is None:
        return ""
    return " ".join(value.split())


def parse_price(value: str | None) -> float | None:
    if value is None:
        return None

    cleaned = value.replace("฿", "").replace(",", "").replace(" ", "")
    if not cleaned:
        return None

    body = cleaned.lstrip("+-")
    if body.count(".") > 1 or not body.replace(".", "", 1).isdecimal():
        return None

    return float(cleaned)


def safe_int(value: str | int | None, default: int = 0) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.strip().lstrip("+-").isdecimal():
        return int(value)
    return default


if __name__ == "__main__":
    print(f"ชื่อที่ทำความสะอาดแล้วคือ {clean_text('  Somchai   Jaidee ')!r}")
    print(f"ชื่อจากค่า None คือ {clean_text(None)!r}")
    print(f"ราคาจาก ฿1,150 คือ {parse_price('฿1,150')}")
    print(f"ราคาจาก 300.00 คือ {parse_price('300.00')}")
    print(f"ราคาที่แปลงไม่ได้คือ {parse_price('abc')}")
    print(f"จำนวนเต็มจาก 12 คือ {safe_int('12')}")
    print(f"ค่า default เมื่อแปลงไม่ได้คือ {safe_int('x', -1)}")
    print(f"จำนวนเต็มจาก None คือ {safe_int(None)}")
