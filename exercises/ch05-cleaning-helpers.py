def clean_text(value: str | None) -> str:
    """ตัดช่องว่างหัวท้ายและยุบช่องว่างที่ติดกันให้เหลือช่องเดียว ค่า None ให้เป็นข้อความว่าง"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def parse_price(value: str | None) -> float | None:
    """แปลงข้อความราคาที่มีสัญลักษณ์บาทกับจุลภาคเป็นจำนวนจริง ค่าที่แปลงไม่ได้ให้คืน None"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def safe_int(value: str | int | None, default: int = 0) -> int:
    """แปลงค่าเป็นจำนวนเต็ม ถ้าแปลงไม่ได้ให้คืนค่า default"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    print(f"ชื่อที่ทำความสะอาดแล้วคือ {clean_text('  Somchai   Jaidee ')!r}")
    print(f"ชื่อจากค่า None คือ {clean_text(None)!r}")
    print(f"ราคาจาก ฿1,150 คือ {parse_price('฿1,150')}")
    print(f"ราคาจาก 300.00 คือ {parse_price('300.00')}")
    print(f"ราคาที่แปลงไม่ได้คือ {parse_price('abc')}")
    print(f"จำนวนเต็มจาก 12 คือ {safe_int('12')}")
    print(f"ค่า default เมื่อแปลงไม่ได้คือ {safe_int('x', -1)}")
    print(f"จำนวนเต็มจาก None คือ {safe_int(None)}")
