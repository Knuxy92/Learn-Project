import numpy as np

revenue = np.array([900.0, 1500.0, 1200.0, 890.0, 4200.0, 300.0])

print("ค่าเฉลี่ย", revenue.mean())
print("มัธยฐาน", np.median(revenue))
print("ค่าน้อยสุด", revenue.min())
print("ค่ามากสุด", revenue.max())
print("ผลรวม", revenue.sum())

print("ตำแหน่งของยอดสูงสุด", revenue.argmax())
print("ยอดที่ตำแหน่งนั้น", revenue[revenue.argmax()])

by_month = np.array(
    [
        [900.0, 1500.0, 1200.0],
        [890.0, 4200.0, 300.0],
    ]
)
print("ยอดรวมของแต่ละเดือน", by_month.sum(axis=1))
print("ยอดรวมของแต่ละช่อง", by_month.sum(axis=0))

with_missing = np.array([10.0, np.nan, 30.0])
print("ค่าเฉลี่ยเมื่อมีค่าหายไป", with_missing.mean())
print("ค่าเฉลี่ยที่ข้ามค่าหายไป", np.nanmean(with_missing))
print("ผลรวมที่ข้ามค่าหายไป", np.nansum(with_missing))
