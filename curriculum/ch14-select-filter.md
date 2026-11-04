# บทที่ 14: เลือกและกรองข้อมูล

## ทบทวน

บทที่แล้วเราอ่าน CSV เข้ามาเป็น DataFrame ได้แล้ว และรู้ว่าแต่ละคอลัมน์มีชนิดข้อมูล (dtype) ของตัวเอง

ปัญหาคือตารางดิบทั้งตารางไม่ค่อยมีประโยชน์เท่าที่ควร เราต้องดึงเฉพาะแถวที่สนใจออกมาก่อน เช่น เฉพาะออเดอร์ที่จ่ายเงินแล้ว หรือเฉพาะลูกค้าประเทศไทย

บทนี้สอนวิธีเลือกแถวและเลือกคอลัมน์จาก DataFrame

## การเลือกด้วยชื่อแถวและชื่อคอลัมน์ (`loc`)

`loc` คือเครื่องมือเลือกข้อมูลโดยอ้างชื่อป้าย (label) ทั้งชื่อแถวและชื่อคอลัมน์

ทำไมต้องใช้ในงานทำความสะอาดข้อมูล เพราะข้อมูลจริงมักมีดัชนี (index) ที่ไม่ใช่เลขเรียงสวย ๆ และเราต้องอ้างถึงแถวด้วยค่าจริง เช่น รหัสลูกค้า

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(orders.loc[0:2, ["order_id", "quantity", "status"]])
```

ผลลัพธ์

```txt
  order_id  quantity     status
0    O0001       2.0  cancelled
1    O0002       5.0   canceled
2    O0003      -1.0  cancelled
```

จุดสำคัญคือ `0:2` ของ `loc` นับหัวด้วยและนับท้ายด้วย จึงได้สามแถว ไม่ใช่สองแถว

ถ้าใส่ชื่อแถวเดียวและชื่อคอลัมน์เดียว จะได้ค่าเดี่ยวออกมา ไม่ใช่ตาราง

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(orders.loc[0, "order_id"])
print(orders.loc[5:7, "quantity"].tolist())
```

ผลลัพธ์

```txt
O0001
[nan, 1.0, 3.0]
```

## การเลือกด้วยตำแหน่ง (`iloc`)

`iloc` เลือกด้วยตำแหน่งตัวเลข นับจากศูนย์เหมือนลิสต์ และไม่สนว่าชื่อแถวคืออะไร

เราใช้มันเมื่อรู้ว่า "เอาสามแถวแรก" หรือ "เอาสองคอลัมน์แรก" โดยไม่ต้องรู้ชื่อ

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(orders.iloc[0:3, 0:3])
print(orders.iloc[-2:, 0])
```

ผลลัพธ์

```txt
  order_id customer_id product_id
0    O0001        C002       P004
1    O0002        C006       P006
2    O0003        C003       P001
40    O0006
41    O0006
Name: order_id, dtype: str
```

ต่างจาก `loc` ตรงที่ `0:3` ของ `iloc` ไม่นับท้าย จึงได้แถวที่ 0, 1, 2

## เลือกเฉพาะคอลัมน์

บางครั้งเราต้องการตัดคอลัมน์ที่ไม่ใช้ทิ้ง เพื่อให้ตารางอ่านง่ายและเบาลง

เขียนเป็นลิสต์ชื่อคอลัมน์ไว้ในวงเล็บเหลี่ยมสองชั้น

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(type(orders["order_id"]).__name__)
print(type(orders[["order_id", "quantity"]]).__name__)
print(orders[["order_id", "quantity"]].shape)
```

ผลลัพธ์

```txt
Series
DataFrame
(42, 2)
```

วงเล็บเดียวได้ Series สองวงเล็บได้ DataFrame ตรงนี้คือจุดที่มือใหม่พลาดบ่อยที่สุด

## เงื่อนไขจริงเท็จ (boolean mask)

มาสก์ (mask) คือ Series ที่เก็บค่าจริงเท็จ ใช้เป็นเงื่อนไขเลือกแถว

มันคือหัวใจของการกรองข้อมูล เพราะเราเขียนเงื่อนไขหนึ่งครั้งแล้วใช้กับทั้งตารางพร้อมกัน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

mask = orders["status"].str.strip().str.lower() == "paid"
print(mask.dtype)
print(mask.sum())
print(orders.loc[mask, ["order_id", "status"]].head(3))
```

ผลลัพธ์

```txt
bool
11
  order_id status
5    O0006  Paid 
6    O0007  Paid 
8    O0009   paid
```

เห็นว่าค่าในตารางมีทั้ง `paid`, `PAID` และ `Paid ` แต่เราตัดช่องว่างและปรับเป็นตัวพิมพ์เล็กก่อนเปรียบเทียบ จึงจับได้ครบทั้ง 11 แถว

ถ้าเทียบตรง ๆ โดยไม่ทำความสะอาดก่อน จะได้แค่ 4 แถว

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print((orders["status"] == "paid").sum())
print((orders["status"].str.strip().str.lower() == "paid").sum())
```

ผลลัพธ์

```txt
4
11
```

## รวมหลายเงื่อนไข

ใช้ `&` สำหรับ "และ" ใช้ `|` สำหรับ "หรือ" ใช้ `~` สำหรับ "ไม่"

ต้องครอบแต่ละเงื่อนไขด้วยวงเล็บเสมอ เพราะตัวดำเนินการของ Python มีลำดับความสำคัญที่ทำให้ผลออกมาผิดได้

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

paid = orders["status"].str.strip().str.lower() == "paid"
big = orders["quantity"] >= 2
both = paid & big

print(both.sum())
print(orders.loc[both, ["order_id", "quantity", "status"]])
```

ผลลัพธ์

```txt
5
   order_id  quantity status
8     O0009       3.0   paid
10    O0011       2.0   PAID
12    O0013       2.0  Paid 
23    O0024       2.0   paid
38    O0039       2.0  Paid 
```

เครื่องหมาย `~` ใช้กลับเงื่อนไข เอาไว้หาว่าแถวไหนไม่เข้าเงื่อนไข

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

mask = orders["status"].str.strip().str.lower() == "paid"
print(orders.loc[mask, "order_id"].tolist()[:3])
print(orders.loc[~mask, "order_id"].shape[0])
```

ผลลัพธ์

```txt
['O0006', 'O0007', 'O0009']
31
```

## ตรวจหลายค่าพร้อมกันด้วย `isin`

`isin` ใช้ถามว่า ค่าอยู่ในชุดที่กำหนดหรือไม่

เราใช้มันเมื่อต้องกรองหลายสถานะพร้อมกัน ซึ่งเขียนด้วย `|` หลายตัวจะยาวและอ่านยาก

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

status = orders["status"].str.strip().str.lower()

print(status.isin(["paid", "pending"]).sum())
print(orders["quantity"].between(2, 4).sum())
print(len(orders.query("quantity > 3")))
```

ผลลัพธ์

```txt
19
22
2
```

`between` ใช้กรองช่วงตัวเลข โดยนับหัวและนับท้ายด้วย

## เขียนเงื่อนไขแบบข้อความด้วย `query`

`query` ให้เราเขียนเงื่อนไขเป็นข้อความสั้น ๆ อ่านง่าย

ข้อดีคือโค้ดสั้นและอ่านออกทันที ข้อเสียคือชื่อคอลัมน์ที่มีช่องว่างหรืออักขระพิเศษจะใช้ยาก

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(orders.query("quantity > 3")[["order_id", "quantity"]])
print(orders.query("status == 'paid'").shape)
```

ผลลัพธ์

```txt
   order_id  quantity
1     O0002       5.0
25    O0026       5.0
(4, 7)
```

สังเกตว่า `query` เปรียบเทียบตรงตัว ไม่ได้ตัดช่องว่างให้ จึงได้เพียง 4 แถว ไม่ใช่ 11

## สำเนากับต้นฉบับ

การกรองได้ DataFrame ใหม่ แต่บางครั้งข้อมูลข้างในยังผูกกับต้นฉบับ

ถ้าจะแก้ค่าที่กรองมาแล้ว ให้เรียก `.copy()` ก่อนเสมอ เพื่อไม่ให้ไปเปลี่ยนต้นฉบับโดยไม่ตั้งใจ

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

status = orders["status"].str.strip().str.lower()
paid = orders.loc[status == "paid"].copy()
paid["status"] = "confirmed"

print(paid["status"].unique().tolist())
print(orders.loc[5, "status"])
```

ผลลัพธ์

```txt
['confirmed']
Paid 
```

ต้นฉบับยังเป็น `Paid ` อยู่ ไม่ได้เปลี่ยนตาม

## สรุป

| งานที่ต้องทำ | วิธีเขียน |
|---|---|
| เลือกแถวและคอลัมน์ด้วยชื่อ | `df.loc[rows, cols]` |
| เลือกด้วยตำแหน่ง | `df.iloc[rows, cols]` |
| เลือกเฉพาะคอลัมน์ | `df[["a", "b"]]` |
| กรองด้วยเงื่อนไขเดียว | `df.loc[df["c"] == value]` |
| กรองหลายเงื่อนไข | `df.loc[(a) & (b)]` |
| กรองหลายค่า | `df.loc[df["c"].isin(values)]` |
| กรองช่วงตัวเลข | `df.loc[df["c"].between(low, high)]` |
| กรองด้วยข้อความ | `df.query("c > 3")` |
| แก้ผลลัพธ์โดยไม่กระทบต้นฉบับ | `df.loc[mask].copy()` |

หลักจำง่าย ๆ

- `loc` ใช้ชื่อ และนับหัวนับท้าย
- `iloc` ใช้ตำแหน่ง และนับหัวไม่นับท้าย
- เงื่อนไขต้องอยู่ในวงเล็บก่อนใช้ `&` `|` `~`
- กรองก่อนแล้วค่อยแก้ และเรียก `.copy()` ก่อนแก้

## โจทย์ที่ต้องทำ

เปิด `exercises/ch14-filter-orders.py` แล้วเขียนสี่ฟังก์ชันนี้

1. `filter_paid` รับตารางออเดอร์ คืนเฉพาะแถวที่สถานะเป็น paid โดยตัดช่องว่างและปรับตัวพิมพ์ก่อนเทียบ
2. `filter_by_country` รับตารางกับชื่อประเทศ คืนเฉพาะแถวที่ประเทศตรงกัน โดยตัดช่องว่างและปรับตัวพิมพ์ทั้งสองฝั่ง
3. `select_columns` รับตารางกับรายชื่อคอลัมน์ คืนตารางที่มีเฉพาะคอลัมน์เหล่านั้นตามลำดับที่ให้
4. `filter_amount` รับตารางกับยอดขั้นต่ำและชื่อคอลัมน์ คืนเฉพาะแถวที่ค่าไม่น้อยกว่ายอดขั้นต่ำ

## ผลลัพธ์ที่คาดหวัง

เมื่อเขียนครบแล้วรันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```bash
.venv/bin/python exercises/ch14-filter-orders.py
```

จะได้ผลแบบนี้

```txt
ออเดอร์ที่จ่ายแล้ว 11 แถว
ลูกค้าประเทศไทยในตัวอย่าง 3 แถว
order_id  total
      O1  450.0
      O2 1200.0
      O3  300.0
      O4 2400.0
ยอดตั้งแต่ 1000 ขึ้นไป 2 แถว
```

ตัวเลขต้องตรงกับข้อมูลจริงใน `data/raw/orders.csv` และตัวอย่างในไฟล์

ตรวจงานตัวเองด้วยคำสั่งนี้

```bash
.venv/bin/python -m pytest tests/test_ch14.py
```

## เสร็จแล้วพิมพ์ ตรวจ Ch14
