import numpy as np

statuses = np.array(["paid", " PAID ", "pending", "Paid", "cancelled", "paid"])

cleaned = np.strings.lower(np.strings.strip(statuses))
print("สถานะหลังทำความสะอาด", cleaned)

paid_mask = cleaned == "paid"
print("มาสก์ของออเดอร์ที่จ่ายแล้ว", paid_mask)

revenue = np.array([900.0, 1500.0, 1200.0, 890.0, 4200.0, 300.0])

big_paid = paid_mask & (revenue >= 1000)
print("จ่ายแล้วและยอดตั้งแต่หนึ่งพัน", revenue[big_paid])

paid_or_big = paid_mask | (revenue >= 2000)
print("จ่ายแล้วหรือยอดตั้งแต่สองพัน", revenue[paid_or_big])

labels = np.where(paid_mask, "ชำระแล้ว", "รอตรวจ")
print("ป้ายกำกับ", labels)
