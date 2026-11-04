def describe_customer(name: str, age: int, spend: float, is_member: bool) -> str:
    """รับข้อมูลลูกค้าหนึ่งคน คืนข้อความสรุปข้อมูลของลูกค้าคนนั้น"""
    status = "member" if is_member else "guest"

    return f"{name} | {age} | {spend:.2f} | {status}"


def type_report(value: object) -> str:
    """รับค่าอะไรก็ได้ คืนชื่อชนิดของค่านั้นเป็นข้อความ"""
    return type(value).__name__


if __name__ == "__main__":
    print(describe_customer("Somchai", 34, 1250.5, True))
    print(describe_customer("Malee", 28, 0.0, False))
    print(type_report(3))
    print(type_report(3.5))
    print(type_report("x"))
    print(type_report(True))
