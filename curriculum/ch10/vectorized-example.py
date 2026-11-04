import numpy as np

prices = np.array([450.0, 300.0, 1200.0, 89.0])
quantities = np.array([2, 5, 1, 10])

line_totals = prices * quantities
print("ยอดต่อบรรทัด", line_totals)

with_vat = line_totals * 1.07
print("รวมภาษีมูลค่าเพิ่ม", with_vat)

discounted = line_totals - 50
print("หักส่วนลดคนละห้าสิบ", discounted)

counts = np.array([1, 2, 3])
print("หารด้วยสอง", counts / 2)
print("ชนิดหลังหาร", (counts / 2).dtype)
print("หารเอาเฉพาะจำนวนเต็ม", counts // 2)
