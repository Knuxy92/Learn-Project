# ruff: noqa: UP003
print("ชนิดข้อมูลพื้นฐาน")
print(type(42))
print(type(3.5))
print(type("C001"))
print(type(True))

print("แปลงชนิดข้อมูล")
print(int("42") + 8)
print(float("1250.50"))
print(str(2024))

print("ค่าจริงและเท็จ")
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("paid"))

print("ไม่มีค่า")
email = None
print(email)
print(email is None)

print("จัดรูปแบบตัวเลข")
spend = 1250.5
print(f"ยอดใช้จ่าย {spend:.2f} บาท")
print(f"ยอดใช้จ่าย {spend:,.2f} บาท")
