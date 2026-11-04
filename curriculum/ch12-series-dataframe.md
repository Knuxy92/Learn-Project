# บทที่ 12: Series และ DataFrame

## ทบทวน

บทที่แล้วเราสรุปค่าจาก array ด้วย NumPy ได้แล้ว ทั้งค่าเฉลี่ย มัธยฐาน ค่าต่ำสุด และค่าสูงสุด

แต่ array มีข้อจำกัดที่เจ็บตอนทำงานจริงสามข้อ

- ทุกช่องต้องเป็นชนิดเดียวกัน ถ้าเอาข้อความปนกับตัวเลขจะกลายเป็นข้อความทั้งหมด
- ไม่มีชื่อคอลัมน์ ต้องจำเองว่า index 0 คืออะไร
- ไม่มีป้ายกำกับแถว ทำให้จับคู่ข้อมูลสองตารางได้ยาก

Pandas แก้ทั้งสามข้อนี้ และจะกลายเป็นเครื่องมือหลักของเราตั้งแต่บทนี้ไปจนจบหลักสูตร

## Series คืออะไร

Series คืออาร์เรย์หนึ่งมิติที่ทุกช่องมีป้ายกำกับ เรียกป้ายนั้นว่า index

ลองนึกถึงคอลัมน์เดียวในสเปรดชีต ที่มีเลขกำกับแถวอยู่ข้างซ้าย

มันสำคัญกับงานทำความสะอาดข้อมูลเพราะคอลัมน์หนึ่งคอลัมน์ในตารางจริงคือ Series ตัวหนึ่ง การเข้าใจ Series จึงหมายถึงเข้าใจทุกคอลัมน์ที่เราจะต้องแก้

```python
import pandas as pd

prices = pd.Series(
    [450.0, 300.0, 60.0],
    index=["P001", "P002", "P003"],
    name="list_price",
)

print(prices)
```

ผลลัพธ์

```txt
P001    450.0
P002    300.0
P003     60.0
Name: list_price, dtype: float64
```

อ่านบรรทัดแรกออกเสียงว่า P001 มีค่า 450.0

ค่า `name` ที่เราตั้งไว้จะไปโผล่ท้ายตาราง และ `dtype` บอกชนิดข้อมูลของทั้งคอลัมน์

```python
print("ชื่อของ Series คือ", prices.name)
print("ชนิดข้อมูลคือ", prices.dtype)
print("index คือ", list(prices.index))
```

ผลลัพธ์

```txt
ชื่อของ Series คือ list_price
ชนิดข้อมูลคือ float64
index คือ ['P001', 'P002', 'P003']
```

สร้าง Series จากดิกชันนารีก็ได้ ผลออกมาเหมือนกัน เพราะดิกชันนารีเก็บคู่กุญแจกับค่าอยู่แล้ว

```python
from_dict = pd.Series({"P001": 450.0, "P002": 300.0, "P003": 60.0})
print(from_dict)
```

ผลลัพธ์

```txt
P001    450.0
P002    300.0
P003     60.0
dtype: float64
```

## เลือกค่าจาก Series

เราเลือกได้สองแบบ คือเลือกตามป้ายด้วย `.loc` หรือเลือกทั้งกลุ่มด้วยเงื่อนไข

แบบแรกใช้เมื่อรู้ป้ายที่ต้องการ

```python
print(prices.loc["P002"])
```

ผลลัพธ์

```txt
300.0
```

แบบที่สองใช้เมื่ออยากได้ทุกแถวที่เข้าเงื่อนไข ผลที่ได้ยังเป็น Series ที่มี index ติดมาด้วย

```python
print(prices[prices > 400])
```

ผลลัพธ์

```txt
P001    450.0
Name: list_price, dtype: float64
```

แบบที่สองนี้สำคัญมาก เพราะการกรองแถวที่ผิดปกติในงานทำความสะอาดข้อมูลใช้รูปแบบนี้ทั้งนั้น

## index และการจัดแนว

นี่คือจุดที่มือใหม่พลาดบ่อยที่สุด

เวลาคูณ Series สองตัว Pandas ไม่ได้จับคู่ตามลำดับแถว แต่จับคู่ตาม index

ถ้า index ตรงกันก็คูณกันได้ ถ้าไม่ตรง ช่องที่ขาดจะกลายเป็นค่าว่างทันที

```python
quantities = pd.Series([2, 5], index=["P001", "P002"], name="quantity")

print(prices * quantities)
```

ผลลัพธ์

```txt
P001     900.0
P002    1500.0
P003       NaN
dtype: float64
```

P003 ไม่มีจำนวนใน Series ขวา ผลจึงเป็น NaN แทนที่จะเป็นศูนย์

ในงานจริงนี่คือต้นเหตุของค่าว่างที่โผล่มาโดยไม่มีใครเขียนค่าว่างลงไป เราจึงต้องตรวจ index ให้ตรงกันก่อนคำนวณทุกครั้ง

ถ้า Series ตัวเดียวอยู่ในสมการ index ไม่มีผลอะไร ค่าคงที่ถูกบวกเข้าทุกช่อง

```python
print(prices + 10)
```

ผลลัพธ์

```txt
P001    460.0
P002    310.0
P003     70.0
Name: list_price, dtype: float64
```

การบวกค่าคงที่ไม่ได้สนใจ index เลย เพราะมี Series เดียวในสมการ

สรุปค่าทั้งคอลัมน์ก็ทำได้เหมือน NumPy

```python
print(prices.mean())
```

ผลลัพธ์

```txt
270.0
```

ถ้าอยากได้ลิสต์ธรรมดาไปใช้ต่อ เรียก `.to_list()` ได้

```python
print(prices.to_list())
```

ผลลัพธ์

```txt
[450.0, 300.0, 60.0]
```

## DataFrame คืออะไร

DataFrame คือตารางสองมิติที่แต่ละคอลัมน์มีชื่อ และมี index กำกับแถวร่วมกันทั้งตาราง

พูดง่าย ๆ คือหลาย Series ที่ใช้ index ชุดเดียวกันมาเรียงข้างกัน

มันสำคัญเพราะข้อมูลดิบที่เราอ่านจากไฟล์ CSV หนึ่งไฟล์คือ DataFrame หนึ่งตัว งานทำความสะอาดข้อมูลเกือบทั้งหมดจึงเป็นการแก้ DataFrame

สร้างจากรายการของดิกชันนารีได้ วิธีนี้ทำให้อ่านโค้ดแล้วเห็นว่าค่าไหนคู่กับคอลัมน์ไหน

```python
rows = [
    {"order_id": "O0001", "customer_id": "C002", "quantity": 2, "unit_price": 4200.0},
    {"order_id": "O0002", "customer_id": "C006", "quantity": 5, "unit_price": 1150.0},
    {"order_id": "O0003", "customer_id": "C003", "quantity": -1, "unit_price": 450.0},
]
orders = pd.DataFrame(rows)

print(orders)
```

ผลลัพธ์

```txt
  order_id customer_id  quantity  unit_price
0    O0001        C002         2      4200.0
1    O0002        C006         5      1150.0
2    O0003        C003        -1       450.0
```

สร้างจากดิกชันนารีที่เก็บคอลัมน์ละลิสต์ก็ได้ ผลเหมือนกัน

```python
columns = {
    "order_id": ["O0001", "O0002", "O0003"],
    "quantity": [2, 5, -1],
    "unit_price": [4200.0, 1150.0, 450.0],
}
print(pd.DataFrame(columns))
```

ผลลัพธ์

```txt
  order_id  quantity  unit_price
0    O0001         2      4200.0
1    O0002         5      1150.0
2    O0003        -1       450.0
```

## รูปร่าง ชื่อคอลัมน์ และ index

สามอย่างนี้คือสิ่งที่ต้องตรวจก่อนลงมือแก้อะไรทั้งสิ้น

ถ้า `shape` ไม่ตรงกับที่คาด แปลว่าเราอ่านไฟล์ผิดหรือไฟล์เปลี่ยนไปแล้ว

```python
print("shape คือ", orders.shape)
print("columns คือ", list(orders.columns))
print("index คือ", list(orders.index))
```

ผลลัพธ์

```txt
shape คือ (3, 4)
columns คือ ['order_id', 'customer_id', 'quantity', 'unit_price']
index คือ [0, 1, 2]
```

`shape` คืนมาเป็นคู่ (จำนวนแถว, จำนวนคอลัมน์) โดยแถวมาก่อนเสมอ

index ที่เห็นเป็นเลข 0 1 2 คือ index ที่ Pandas สร้างให้เองตอนสร้างตาราง

## ชนิดข้อมูลของแต่ละคอลัมน์

`.dtypes` บอกชนิดของทุกคอลัมน์พร้อมกัน

เราดูมันก่อนเสมอ เพราะคอลัมน์ที่ควรเป็นตัวเลขแต่กลายเป็นข้อความ จะทำให้การคำนวณพังหรือเงียบไปเฉย ๆ

```python
print(orders.dtypes)
```

ผลลัพธ์

```txt
order_id           str
customer_id        str
quantity         int64
unit_price     float64
dtype: object
```

Pandas 3 เรียกคอลัมน์ข้อความว่า `str` ส่วนเลขจำนวนเต็มคือ `int64` และเลขทศนิยมคือ `float64`

ชื่อคอลัมน์ที่เห็นเป็น `str` นี้ไม่ใช่ปัญหา แต่ถ้าเจอ `quantity` เป็น `str` ทั้งที่ควรเป็นตัวเลข นั่นคือสัญญาณว่ามีอะไรแปลกในไฟล์

## คอลัมน์หนึ่งคอลัมน์คือ Series

เลือกคอลัมน์ด้วยวงเล็บเหลี่ยมแล้วได้ Series กลับมา ไม่ใช่ DataFrame

```python
quantity = orders["quantity"]
print(type(quantity))
print(quantity)
```

ผลลัพธ์

```txt
<class 'pandas.Series'>
0    2
1    5
2   -1
Name: quantity, dtype: int64
```

ชื่อคอลัมน์กลายเป็น `name` ของ Series ให้อัตโนมัติ

การรู้ว่าได้ Series กลับมาสำคัญ เพราะเมธอดที่ใช้ต่อจะต่างกัน เช่น Series ใช้ `.mean()` ได้ แต่ DataFrame ต้องระบุคอลัมน์ก่อน

เลือกค่าเดี่ยวด้วย `.loc` โดยให้แถวก่อนแล้วคอลัมน์

```python
print(orders.loc[0, "order_id"])
```

ผลลัพธ์

```txt
O0001
```

## เพิ่มคอลัมน์ใหม่

การเพิ่มคอลัมน์ทำได้ด้วยการกำหนดค่าให้ชื่อคอลัมน์ที่ยังไม่มี

แต่ต้องระวังให้ดี การกำหนดค่าลงบน DataFrame เดิมจะแก้ของเดิมทันที เราจึงเรียก `.copy()` ก่อนทุกครั้งที่ไม่อยากให้ต้นฉบับเปลี่ยน

```python
with_revenue = orders.copy()
with_revenue["revenue"] = with_revenue["quantity"] * with_revenue["unit_price"]

print(with_revenue)
```

ผลลัพธ์

```txt
  order_id customer_id  quantity  unit_price  revenue
0    O0001        C002         2      4200.0   8400.0
1    O0002        C006         5      1150.0   5750.0
2    O0003        C003        -1       450.0   -450.0
```

ตรวจว่าต้นฉบับไม่ถูกแก้

```python
print("ตารางเดิมมีคอลัมน์ revenue หรือไม่", "revenue" in orders.columns)
```

ผลลัพธ์

```txt
ตารางเดิมมีคอลัมน์ revenue หรือไม่ False
```

สังเกตว่าแถว O0003 ได้ revenue ติดลบ เพราะ quantity เป็น -1

การคูณไม่รู้ว่าค่าติดลบคือข้อมูลเสีย มันคูณตามสั่ง นี่คือเหตุผลที่เราต้องตรวจค่าผิดปกติก่อนคำนวณยอดขายเสมอ

## เรียงลำดับและเลือกแถวบนสุด

`sort_values` เรียงทั้งตารางตามคอลัมน์ที่ระบุ

```python
print(with_revenue.sort_values("revenue", ascending=False).head(2))
```

ผลลัพธ์

```txt
  order_id customer_id  quantity  unit_price  revenue
0    O0001        C002         2      4200.0   8400.0
1    O0002        C006         5      1150.0   5750.0
```

`nlargest` ให้ผลเหมือนกันแต่สั้นกว่าเมื่อต้องการแค่ n แถวแรก

```python
print(with_revenue.nlargest(2, "revenue").reset_index(drop=True))
```

ผลลัพธ์

```txt
  order_id customer_id  quantity  unit_price  revenue
0    O0001        C002         2      4200.0   8400.0
1    O0002        C006         5      1150.0   5750.0
```

`reset_index(drop=True)` เปลี่ยน index ให้เริ่มใหม่จาก 0 ตามลำดับที่เรียงแล้ว

ถ้าไม่รีเซ็ต index จะติดค่าของแถวเดิมมาด้วย เช่น 0 กับ 1 ที่อาจไม่ต่อเนื่อง ทำให้อ่านรายงานสับสน

เลือกแค่บางคอลัมน์ออกมาดูก็ทำได้

```python
print(with_revenue[["order_id", "revenue"]].to_string(index=False))
```

ผลลัพธ์

```txt
order_id  revenue
   O0001   8400.0
   O0002   5750.0
   O0003   -450.0
```

## สรุป

| อยากทำอะไร | ใช้คำสั่ง |
|---|---|
| สร้างคอลัมน์เดียว | `pd.Series(values, index=..., name=...)` |
| สร้างตาราง | `pd.DataFrame(rows)` |
| ดูขนาดตาราง | `df.shape` |
| ดูชื่อคอลัมน์ | `list(df.columns)` |
| ดูชนิดทุกคอลัมน์ | `df.dtypes` |
| เลือกหนึ่งคอลัมน์ | `df["column"]` |
| เลือกค่าเดี่ยว | `df.loc[row, "column"]` |
| เพิ่มคอลัมน์ | `df["new"] = ...` หลัง `df.copy()` |
| เรียงจากมากไปน้อย | `df.sort_values("column", ascending=False)` |
| เอา n แถวบนสุด | `df.nlargest(n, "column")` |
| รีเซ็ต index | `df.reset_index(drop=True)` |

กฎที่ต้องจำให้ขึ้นใจคือ Series สองตัวจะคำนวณกันตาม index ไม่ใช่ตามลำดับแถว

## โจทย์ที่ต้องทำ

เปิด `exercises/ch12-build-dataframe.py`

เขียนสี่ฟังก์ชันนี้

1. `build_orders()` สร้างตาราง orders จาก `ORDER_ROWS` ที่เตรียมไว้ให้แล้ว โดยให้คอลัมน์เรียงตาม `ORDER_COLUMNS`
2. `add_revenue(df)` คืนตารางใหม่ที่เพิ่มคอลัมน์ revenue ซึ่งเท่ากับ quantity คูณ unit_price ห้ามแก้ตารางที่รับเข้ามา
3. `top_rows(df, n, column)` คืน n แถวที่ค่าคอลัมน์มากที่สุด เรียงจากมากไปน้อย และ index เริ่มใหม่จาก 0
4. `column_types(df)` คืนดิกชันนารีที่จับคู่ชื่อคอลัมน์กับชนิดข้อมูลเป็นข้อความ

## ผลลัพธ์ที่คาดหวัง

เมื่อเขียนครบแล้วรันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```bash
.venv/bin/python exercises/ch12-build-dataframe.py
```

จะได้ผลแบบนี้

```txt
  order_id customer_id  quantity  unit_price
0    O0001        C002         2      4200.0
1    O0002        C006         5      1150.0
2    O0003        C003        -1       450.0
3    O0004        C001         0       300.0

  order_id customer_id  quantity  unit_price  revenue
0    O0001        C002         2      4200.0   8400.0
1    O0002        C006         5      1150.0   5750.0
2    O0003        C003        -1       450.0   -450.0
3    O0004        C001         0       300.0      0.0

  order_id customer_id  quantity  unit_price  revenue
0    O0001        C002         2      4200.0   8400.0
1    O0002        C006         5      1150.0   5750.0

{'order_id': 'str', 'customer_id': 'str', 'quantity': 'int64', 'unit_price': 'float64', 'revenue': 'float64'}
```

ตรวจงานตัวเองด้วยคำสั่งนี้

```bash
.venv/bin/python -m pytest tests/test_ch12.py
```

## เสร็จแล้วพิมพ์ ตรวจ Ch12
