import numpy as np

quantities = np.array(
    [
        [2, 1, 3],
        [4, 0, 2],
    ]
)
prices = np.array([450.0, 300.0, 1200.0])

print("ขนาดของตาราง", quantities.shape)
print("ขนาดของราคา", prices.shape)
print(quantities * prices)

rows = np.array([[1.0, 2.0, 3.0], [10.0, 20.0, 30.0]])
print(rows - rows.mean(axis=1, keepdims=True))

scores = np.array([3.0, 5.0, 7.0, 9.0])
lowest = scores.min()
highest = scores.max()
print("ช่วงคะแนน", lowest, highest)
print("ปรับให้อยู่ระหว่างศูนย์กับหนึ่ง", (scores - lowest) / (highest - lowest))

try:
    quantities * np.array([1.0, 2.0])
except ValueError as error:
    print("ขนาดไม่เข้ากันจึงล้มเหลว")
    print(str(error).strip())

overdue_days = np.array([3, -2, 5, -7])
print("วันคงค้างก่อนแก้", overdue_days)
print("วันคงค้างหลังแก้ค่าติดลบ", np.where(overdue_days < 0, 0, overdue_days))
