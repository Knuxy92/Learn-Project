def describe_customer(name: str, age: int, spend: float, is_member: bool) -> str:
    """รับชื่อ อายุ ยอดใช้จ่าย และสถานะสมาชิก คืนข้อความสรุปของลูกค้าหนึ่งคน"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


def type_report(value: object) -> str:
    """รับค่าอะไรก็ได้ คืนชื่อชนิดของค่านั้นเป็นข้อความ"""
    raise NotImplementedError("เขียนโค้ดตรงนี้")


if __name__ == "__main__":
    print(describe_customer("Somchai", 34, 1250.5, True))
    print(describe_customer("Malee", 28, 0.0, False))
    print(type_report(3))
    print(type_report(3.5))
    print(type_report("x"))
    print(type_report(True))
