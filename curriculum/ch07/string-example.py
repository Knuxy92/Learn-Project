code = "P001-KEYBOARD"

print("ทั้งข้อความ", code)
print("ตัวแรก", code[0])
print("สามตัวแรก", code[:3])
print("ห้าตัวท้าย", code[-5:])
print("จำนวนตัวอักษร", len(code))
print()

raw_name = "  Nattapong   Sri  "

print("ก่อนทำความสะอาด", repr(raw_name))
print("หลัง strip", repr(raw_name.strip()))
print("หลังยุบช่องว่างซ้ำ", repr(" ".join(raw_name.split())))
print()

raw_country = "thailand "

print("ตัวพิมพ์เล็ก", raw_country.strip().lower())
print("ตัวพิมพ์ใหญ่", raw_country.strip().upper())
print("ขึ้นต้นคำด้วยตัวใหญ่", raw_country.strip().title())
print()

raw_price = "฿1,150"

print("ตัดสัญลักษณ์บาท", raw_price.replace("฿", ""))
print("ตัดบาทกับ comma", raw_price.replace("฿", "").replace(",", ""))
print("แปลงเป็นตัวเลข", float(raw_price.replace("฿", "").replace(",", "")))
print()

raw_phone = "(66) 802003004"
plus_phone = "+66801002003"

cleaned_phone = raw_phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print("แบบมีวงเล็บ", cleaned_phone)
print("แบบมีเครื่องหมายบวก", plus_phone)
print("ขึ้นต้นด้วยรหัสประเทศ", plus_phone.startswith("+66"))
print("แทนรหัสประเทศด้วยศูนย์", plus_phone.replace("+66", "0", 1))
print()

line = "P001, Keyboard ,Accessory,450"

fields = line.split(",")
print("แยกด้วย comma", fields)
print("ต่อกลับ", "-".join(["P001", "Keyboard", "450"]))
print("ตัดช่องว่างแต่ละช่อง", [field.strip() for field in fields])
print("มีคำว่า Accessory หรือไม่", "Accessory" in fields)
print()

print(f"{'สินค้า':<12}{'ราคา':>8}")
print(f"{'Keyboard':<12}{450:>8}")
print(f"{'Monitor':<12}{4200:>8,.2f}")
