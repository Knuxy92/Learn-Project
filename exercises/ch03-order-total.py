# กำหนดราคาต่อชิ้นและจำนวนสินค้า
price = 450
quantity = 3

# คำนวณยอดรวม
total = price * quantity
print(f"ยอดรวมรายการแรก: {total}")

# คำนวณยอดหลังหักส่วนลด 10 เปอร์เซ็นต์
discount_percent = 10
discounted_total = total - (total * discount_percent / 100)
print(f"ยอดหลังหักส่วนลด: {discounted_total}")

# ตรวจว่ายอดถึงเกณฑ์ส่งฟรี 1,000 บาทหรือไม่
print(f"ยอดถึงเกณฑ์ส่งฟรี: {total >= 1000}")
print(f"ยอดต่ำกว่าเกณฑ์ส่งฟรี: {total < 1000}")
