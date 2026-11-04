def classify_amount(total: float) -> str:
    """รับยอดเงิน คืนกลุ่ม small เมื่อต่ำกว่า 500, medium เมื่อต่ำกว่า 2000, ที่เหลือเป็น large"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def count_by_status(rows: list[dict]) -> dict[str, int]:
    """รับรายการแถว คืนดิกชันนารีที่นับจำนวนแถวแยกตามค่าของคีย์ status"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def find_first_large(rows: list[dict]) -> dict | None:
    """รับรายการแถว คืนแถวแรกที่ total ตั้งแต่ 2000 ขึ้นไป ถ้าไม่มีให้คืน None"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    sample = [
        {"order_id": "O0001", "status": "paid", "total": 4200.0},
        {"order_id": "O0002", "status": "pending", "total": 1150.0},
        {"order_id": "O0003", "status": "paid", "total": 450.0},
        {"order_id": "O0004", "status": "cancelled", "total": 2600.0},
    ]

    print(f"499.99 อยู่ในกลุ่ม {classify_amount(499.99)}")
    print(f"500 อยู่ในกลุ่ม {classify_amount(500)}")
    print(f"2000 อยู่ในกลุ่ม {classify_amount(2000)}")
    print(f"นับตามสถานะได้ {count_by_status(sample)}")
    print(f"แถวแรกที่ยอดใหญ่คือ {find_first_large(sample)}")
