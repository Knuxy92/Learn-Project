prices = [120, 250, 300]
print("== for ==")
for price in prices:
    print(price)

print("== ตัวสะสม ==")
total = 0
for price in prices:
    total += price
print(f"ยอดรวม: {total}")

print("== break ==")
for price in [120, 250, 300, 1500]:
    if price >= 500:
        print(f"เจอราคาสูง: {price}")
        break

print("== continue ==")
for price in [120, 250, 300, 1500]:
    if price < 200:
        continue
    print(price)

print("== while ==")
remaining = 3
while remaining > 0:
    print(f"เหลืออีก {remaining} รอบ")
    remaining -= 1
