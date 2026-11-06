total = 1200

print("== if กับ else ==")
if total >= 1000:
    print("ส่งฟรี")
else:
    print("ค่าส่ง 50 บาท")

print("== if, elif และ else ==")
if total < 500:
    print("ยอดเล็ก")
elif total < 2000:
    print("ยอดปานกลาง")
else:
    print("ยอดใหญ่")

print("== รวมหลายเงื่อนไข ==")
status = "pending"
if status == "pending" and total >= 2000:
    print("ต้องตรวจสอบรายการนี้")
if status == "paid" or status == "pending":
    print("เป็นสถานะที่ระบบรู้จัก")

print("== ตรวจหลายรายการ ==")
prices = [120, 250, 300, 1500]
for price in prices:
    if price >= 500:
        print(f"ราคาสูง: {price}")
