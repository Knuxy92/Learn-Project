def shipping_fee(total: float) -> float:
    if total >= 1000:
        return 0.0
    return 50.0


def classify_amount(total: float) -> str:
    if total < 500:
        return "small"
    elif total < 2000:
        return "medium"
    else:
        return "large"


def needs_review(status: str, total: float) -> bool:
    return status == "pending" and total >= 2000


def is_suspicious(status: str) -> bool:
    return status == "" or status == "unknown"


def describe_status(status: str) -> str:
    if status == "paid":
        return "ชำระแล้ว"
    if status in {"cancelled", "canceled"}:
        return "ยกเลิก"
    if status == "":
        return "ไม่ระบุ"
    return "รอดำเนินการ"


def main() -> None:
    print("== if กับ else ==")
    for total in [450.0, 1000.0, 2500.0]:
        print(f"ยอด {total:.2f} ค่าส่ง {shipping_fee(total):.2f} บาท")

    print("== if กับ elif ==")
    for total in [120.0, 499.99, 500.0, 1999.0, 2000.0, 4500.0]:
        print(f"ยอด {total:>8.2f} บาท อยู่ในกลุ่ม {classify_amount(total)}")

    print("== and กับ or ==")
    for status, total in [("pending", 2600.0), ("pending", 450.0), ("paid", 4200.0)]:
        print(f"{status} ยอด {total:.2f} ต้องตรวจหรือไม่ {needs_review(status, total)}")
    print(is_suspicious(""))
    print(is_suspicious("unknown"))
    print(is_suspicious("paid"))

    print("== ตรวจค่าอยู่ในกลุ่ม ==")
    for status in ["paid", "cancelled", "canceled", "", "pending"]:
        print(f"{status!r} แปลว่า {describe_status(status)}")

    print("== ค่าจริงเท็จ ==")
    for value in [0, -1, "", "0", [], None]:
        print(f"{value!r} เป็นจริงหรือไม่ {bool(value)}")

    print("== ตรวจ None ==")
    email = None
    print(f"อีเมลเป็น None หรือไม่ {email is None}")
    print(f"อีเมลเท่ากับข้อความว่างหรือไม่ {email == ''}")


if __name__ == "__main__":
    main()
