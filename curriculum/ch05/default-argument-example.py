def greet(name, prefix="คุณ"):
    print(f"สวัสดี{prefix}{name}")


def describe_order(price, quantity):
    print(f"ราคา {price} บาท จำนวน {quantity} ชิ้น")


print("== ค่าเริ่มต้น ==")
greet("Mali")
greet("Somchai", "คุณ")

print("== ระบุชื่อพารามิเตอร์ ==")
describe_order(quantity=3, price=450)
