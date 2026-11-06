def say_hello():
    print("สวัสดี")
    print("ยินดีต้อนรับสู่ Python")


def greet(name):
    print(f"สวัสดี {name}")


def calculate_total(price, quantity):
    total = price * quantity
    return total


def shipping_fee(total):
    if total >= 1000:
        return 0
    return 50


print("== ฟังก์ชัน ==")
say_hello()

print("== พารามิเตอร์ ==")
greet("Mali")
greet("Somchai")

print("== return ==")
result = calculate_total(450, 3)
print(result)
print(result + 100)

print("== if ในฟังก์ชัน ==")
print(shipping_fee(1200))
print(shipping_fee(450))
