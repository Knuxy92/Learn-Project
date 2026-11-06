# แก้ค่าตัวแปรด้านล่างตามโจทย์
customer_name = "Somchai"
customer_age = 34
customer_spend = 1250.5
is_member = True

# แสดงข้อมูลลูกค้า
print(f"ชื่อ: {customer_name}")
print(f"อายุ: {customer_age}")
print(f"ยอดใช้จ่าย: {customer_spend:.2f} บาท")
print(f"เป็นสมาชิก: {is_member}")

# ตรวจชนิดของค่า
print(f"ชนิดของอายุ: {type(customer_age)}")
print(f"ชนิดของยอดใช้จ่าย: {type(customer_spend)}")
