"""แบบฝึกหัดบทที่ 5: สร้างฟังก์ชันช่วยคำนวณ

โจทย์
เขียนฟังก์ชัน order_total, apply_discount และ shipping_fee
ให้คืนค่าตามคำอธิบายของแต่ละฟังก์ชัน และแสดงผลตาม curriculum/ch05

ส่วนประกาศฟังก์ชันและชื่อพารามิเตอร์เตรียมไว้เพื่อให้ตรวจคำตอบได้
นักเรียนต้องเขียนคำสั่งภายในฟังก์ชันเอง
"""

def order_total(price, quantity):
    """รับราคาต่อชิ้นและจำนวนสินค้า แล้วคืนยอดรวม"""
    # TODO: คูณ price กับ quantity แล้ว return ผลลัพธ์
    return 0


def apply_discount(total, percent):
    """รับยอดรวมและเปอร์เซ็นต์ส่วนลด แล้วคืนยอดหลังหักส่วนลด"""
    # TODO: คำนวณส่วนลดและ return ยอดคงเหลือ
    return 0


def shipping_fee(total):
    """คืน 0 เมื่อยอดตั้งแต่ 1000 บาทขึ้นไป มิฉะนั้นคืน 50"""
    # TODO: ใช้ if ตรวจ total แล้ว return ค่าส่ง
    return 0


print(f"ยอดรวมรายการแรก: {order_total(450, 3)}")
print(f"ยอดหลังหักส่วนลด: {apply_discount(1000, 10)}")
print(f"ค่าส่งของยอด 450: {shipping_fee(450)}")
print(f"ค่าส่งของยอด 1200: {shipping_fee(1200)}")
