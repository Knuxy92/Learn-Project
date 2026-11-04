ORDERS = [
    {"order_id": "O0001", "status": "paid", "total": 4200.0},
    {"order_id": "O0002", "status": "pending", "total": 1150.0},
    {"order_id": "O0003", "status": "paid", "total": 450.0},
    {"order_id": "O0004", "status": "cancelled", "total": 2600.0},
    {"order_id": "O0005", "status": "paid", "total": 300.0},
]


def total_revenue(rows: list[dict]) -> float:
    total = 0.0
    for row in rows:
        total += row["total"]
    return total


def count_by_status(rows: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        status = row["status"]
        counts[status] = counts.get(status, 0) + 1
    return counts


def paid_ids(rows: list[dict]) -> list[str]:
    result: list[str] = []
    for row in rows:
        if row["status"] != "paid":
            continue
        result.append(row["order_id"])
    return result


def find_first_large(rows: list[dict]) -> dict | None:
    for row in rows:
        if row["total"] >= 2000:
            return row
    return None


def main() -> None:
    print("== for ==")
    for row in ORDERS:
        print(row["total"])

    print("== enumerate ==")
    for position, row in enumerate(ORDERS, start=1):
        print(f"แถวที่ {position} คือ {row['order_id']}")

    print("== ตัวสะสม ==")
    print(f"ยอดรวมทั้งหมด {total_revenue(ORDERS):.2f} บาท")

    print("== นับด้วยดิกชันนารี ==")
    for status, count in count_by_status(ORDERS).items():
        print(f"{status} มี {count} รายการ")

    print("== break ==")
    for row in ORDERS:
        if row["status"] == "cancelled":
            print(f"เจอรายการยกเลิกที่ {row['order_id']} จึงหยุด")
            break

    print("== continue ==")
    print(paid_ids(ORDERS))

    print("== while ==")
    remaining = 3
    while remaining > 0:
        print(f"เหลืออีก {remaining} แถว")
        remaining -= 1

    print("== return ในลูป ==")
    print(find_first_large(ORDERS))
    print(find_first_large([{"total": 100}]))


if __name__ == "__main__":
    main()
