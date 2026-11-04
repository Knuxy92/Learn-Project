customers = [
    "  Nattapong Sri  ",
    "Malee Wongsakul",
    "Kanya P.",
    "Anan Chaiyaporn",
]

print("จำนวนลูกค้า", len(customers))
print("คนแรกแบบดิบ", repr(customers[0]))
print("คนแรกหลัง strip", customers[0].strip())
print("คนสุดท้าย", customers[-1])
print("สามคนแรก", customers[:3])
print()

customers = [
    "  Nattapong Sri  ",
    "Malee Wongsakul",
    "Kanya P.",
]

print("คนแรก", customers[0].strip())
print("คนสุดท้าย", customers[-1].strip())
print("จำนวนสมาชิก", len(customers))

for name in customers:
    print("ชื่อที่ตัดแล้ว", name.strip())
print()

customers = ["Nattapong Sri", "Malee Wongsakul", "Kanya P."]

customers.append("Suda Meesuk")
print("หลังเพิ่ม", len(customers))

for name in customers:
    print(name)
print()

spends = [4200.0, 1850.5, 990.0, 12500.0, 640.25]

print("ยอดรวม", sum(spends))
print("ยอดมากสุด", max(spends))
print("ยอดน้อยสุด", min(spends))
print("จำนวนรายการ", len(spends))
print("ค่าเฉลี่ย", round(sum(spends) / len(spends), 2))
print()

spends = [4200.0, 1850.5, 990.0, 12500.0, 640.25]

high_spenders = [amount for amount in spends if amount >= 1000]
print("ลูกค้าที่จ่ายตั้งแต่ 1000 บาทขึ้นไป", high_spenders)
print()

spends = [4200.0, 1850.5, 990.0, 12500.0, 640.25]

print("เรียงจากน้อยไปมาก", sorted(spends))
print("เรียงจากมากไปน้อย", sorted(spends, reverse=True))
print("ของเดิมไม่เปลี่ยน", spends)
