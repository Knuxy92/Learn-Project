def classify_amount(total: float) -> str:
    if total < 500:
        return "small"
    if total < 2000:
        return "medium"
    return "large"


def count_by_status(rows: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        status = row["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts


def find_first_large(rows: list[dict]) -> dict | None:
    for row in rows:
        if row["total"] >= 2000:
            return row
    return None


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
