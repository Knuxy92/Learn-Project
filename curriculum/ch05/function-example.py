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


def clean_row(row: dict) -> dict:
    return {
        "name": clean_text(row.get("name")),
        "price": parse_price(row.get("price")),
    }


message = "ข้อความจากภายนอก"


def demo_scope() -> str:
    message = "ข้อความในฟังก์ชัน"
    return message


def main() -> None:
    print("== นิยามฟังก์ชัน ==")
    print(f"ชื่อที่สะอาดแล้วคือ {clean_text('  Somchai   Jaidee ')!r}")
    print(f"ค่าจาก None คือ {clean_text(None)!r}")

    print("== return ==")
    name = clean_text("  Malee   Wongsakul ")
    print(f"สวัสดี {name}")
    print(len(name))

    print("== แปลงราคา ==")
    for raw in ["฿1,150", "300.00", "", "abc"]:
        print(f"{raw!r} กลายเป็น {parse_price(raw)!r}")

    print("== ประกอบฟังก์ชัน ==")
    rows = [
        {"name": "  Nattapong   Sri ", "price": "฿4,200"},
        {"name": None, "price": ""},
    ]
    for row in rows:
        print(clean_row(row))

    print("== ขอบเขตตัวแปร ==")
    print(demo_scope())
    print(message)


if __name__ == "__main__":
    main()
