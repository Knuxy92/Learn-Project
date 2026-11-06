price = 450
quantity = 3

total = price * quantity
print(f"ยอดรวมรายการแรก: {total}")

discount_percent = 10
discounted_total = total - (total * discount_percent / 100)
print(f"ยอดหลังหักส่วนลด: {discounted_total}")

print(f"ยอดถึงเกณฑ์ส่งฟรี: {total >= 1000}")
print(f"ยอดต่ำกว่าเกณฑ์ส่งฟรี: {total < 1000}")
