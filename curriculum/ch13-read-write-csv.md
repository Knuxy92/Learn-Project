# บทที่ 13: อ่านและเขียนไฟล์ CSV

## ทบทวน

บทที่แล้วเราสร้าง DataFrame ขึ้นมาเองจากข้อมูลที่พิมพ์ไว้ในโค้ด

แต่ข้อมูลจริงไม่ได้อยู่ในโค้ด มันอยู่ในไฟล์ที่คนอื่นส่งมา บทนี้จึงว่าด้วยการพาไฟล์เข้าและพาตารางออก

## CSV คืออะไร

CSV (comma separated values) คือไฟล์ข้อความธรรมดาที่ใช้ลูกน้ำคั่นแต่ละช่อง และขึ้นบรรทัดใหม่เมื่อจบแถว

บรรทัดแรกมักเป็นชื่อคอลัมน์ เรียกว่า header

มันสำคัญเพราะเป็นรูปแบบที่ทุกเครื่องมือส่งออกได้ ไม่ว่าจะเป็น Excel, Google Sheets หรือระบบหลังบ้าน และเป็นรูปแบบที่ข้อมูลดิบในโปรเจกต์นี้ใช้

เปิดไฟล์ดิบดูตรง ๆ ก่อนจะอ่านด้วยโค้ดทุกครั้ง เป็นนิสัยที่ควรสร้าง

```txt
customer_id,name,email,phone,country,signup_date,loyalty_tier
C001,  Nattapong Sri  ,customer1@example.com,+66801002003,Thailand,2024-11-22,GOLD
C002,Malee Wongsakul,customer2@example.com,(66) 802003004,LA,2024/04/25,gold
```

จะเห็นแล้วว่าชื่อมีช่องว่างหัวท้ายติดมา และช่องที่ค่ามีลูกน้ำอยู่ข้างในจะถูกครอบด้วยเครื่องหมายคำพูด ซึ่งเป็นเรื่องปกติของ CSV

## อ่านไฟล์ด้วย `pd.read_csv`

`pd.read_csv` เปิดไฟล์และสร้าง DataFrame ให้ในคำสั่งเดียว

มันสำคัญเพราะแทนที่เราจะเขียนลูปอ่านทีละบรรทัดเอง Pandas จัดการเรื่อง header, ลูกน้ำในเครื่องหมายคำพูด และการเดาชนิดข้อมูลให้

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(customers.shape)
print()
print(customers.head(3).to_string())
```

ผลลัพธ์

```txt
(14, 7)

  customer_id               name                  email           phone   country signup_date loyalty_tier
0        C001    Nattapong Sri    customer1@example.com    +66801002003  Thailand  2024-11-22         GOLD
1        C002    Malee Wongsakul  customer2@example.com  (66) 802003004        LA  2024/04/25         gold
2        C003           Kanya P.  customer3@example.com    080-300-4005  Thailand  2024/08/20       silver
```

`.head(3)` เอาแค่สามแถวแรกมาดู ใช้ตรวจว่าอ่านถูกก่อนไปต่อ

`.to_string()` สั่งให้พิมพ์ทุกคอลัมน์ในบรรทัดเดียว ไม่ตัดด้วย `...` ซึ่งเป็นค่าเริ่มต้นเมื่อคอลัมน์เยอะ

ไฟล์นี้มี 14 แถว 7 คอลัมน์ ตรงกับที่เราคาด

## ชนิดข้อมูลที่ Pandas เดาให้

Pandas ดูค่าทั้งคอลัมน์แล้วเดาชนิดให้เอง

```python
print(customers.dtypes)
```

ผลลัพธ์

```txt
customer_id     str
name            str
email           str
phone           str
country         str
signup_date     str
loyalty_tier    str
dtype: object
```

ทุกคอลัมน์กลายเป็นข้อความ เพราะในไฟล์นี้ทุกช่องเป็นข้อความจริง ๆ

ดูคอลัมน์ country จะเห็นปัญหาที่จะตามมา

```python
print(customers["country"].head(5).to_string())
```

ผลลัพธ์

```txt
0     Thailand
1           LA
2     Thailand
3    thailand 
4           LA
```

ค่าเดียวกันเขียนได้หลายแบบ ทั้งตัวพิมพ์เล็ก ตัวพิมพ์ใหญ่ และมีช่องว่างต่อท้าย

การอ่านไฟล์ไม่เคยทำความสะอาดให้เรา มันแค่พาข้อมูลเข้ามาตามสภาพเดิม

## ตัวเลขที่กลายเป็นทศนิยมเพราะมีค่าว่าง

นี่คือกับดักที่เจอบ่อยที่สุดตอนอ่าน CSV

```python
orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(orders.dtypes)
```

ผลลัพธ์

```txt
order_id           str
customer_id        str
product_id         str
quantity       float64
unit_price         str
order_date         str
status             str
dtype: object
```

คอลัมน์ quantity ควรเป็นจำนวนเต็ม แต่กลับกลายเป็น `float64`

สาเหตุคือมีบางแถวที่ช่องนี้ว่าง Pandas จึงต้องใช้ค่าที่แทนความว่างได้ ซึ่งก็คือ NaN และ NaN เป็นทศนิยม

ผลคือเลข 2 กลายเป็น 2.0 ทั้งที่เราไม่ต้องการ

ส่วน unit_price ยังเป็นข้อความ เพราะมีค่าแบบ `฿1,150` ปนอยู่จนเดาเป็นตัวเลขไม่ได้

## บังคับให้ทุกคอลัมน์เป็นข้อความ

เมื่อใดที่เราจะทำความสะอาดเองทุกขั้น วิธีที่ปลอดภัยคือบอก Pandas ว่าไม่ต้องเดาอะไร ให้อ่านมาเป็นข้อความทั้งหมด

```python
raw_orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8", dtype=str)

print(raw_orders.dtypes)
```

ผลลัพธ์

```txt
order_id       str
customer_id    str
product_id     str
quantity       str
unit_price     str
order_date     str
status         str
dtype: object
```

ทีนี้ค่าที่ว่างจะกลายเป็น NaN แทนที่จะเป็นสตริงว่าง ซึ่งเราตรวจได้ง่าย

```python
print(raw_orders["quantity"].isna().sum())
```

ผลลัพธ์

```txt
2
```

มีสองแถวที่ไม่มีจำนวนสินค้า

ถ้าเราไม่อยากให้ช่องว่างกลายเป็น NaN แต่ต้องการสตริงว่างจริง ๆ ให้ใส่ `keep_default_na=False` เพิ่ม

```python
raw_orders = pd.read_csv(
    "data/raw/orders.csv",
    encoding="utf-8",
    dtype=str,
    keep_default_na=False,
)

print(raw_orders[["quantity", "unit_price"]].head(3).to_string())
```

ผลลัพธ์

```txt
  quantity unit_price
0        2    4200.00
1        5     ฿1,150
2       -1        450
```

ทั้งสองแบบใช้ได้ เลือกให้ตรงกับวิธีตรวจของเราว่าจะเช็ก `isna()` หรือเช็กสตริงว่าง

## อ่านแค่บางคอลัมน์หรือบางแถว

ไฟล์ใหญ่ไม่จำเป็นต้องอ่านทั้งหมดถ้าแค่อยากดูตัวอย่าง

`usecols` จำกัดคอลัมน์ `nrows` จำกัดจำนวนแถว

```python
preview = pd.read_csv(
    "data/raw/orders.csv",
    encoding="utf-8",
    usecols=["order_id", "status"],
    nrows=3,
)

print(preview.to_string())
```

ผลลัพธ์

```txt
  order_id     status
0    O0001  cancelled
1    O0002   canceled
2    O0003  cancelled
```

สองตัวเลือกนี้ทำให้เปิดไฟล์ขนาดหลายล้านแถวได้เร็วขึ้นมาก เพราะอ่านแค่ส่วนที่ต้องการ

## ไฟล์ภาษาไทยกับ BOM

BOM (byte order mark) คือรอยประทับสามไบต์ที่บางโปรแกรมใส่ไว้ต้นไฟล์เพื่อบอกว่าไฟล์นี้เป็น UTF-8

ถ้าเปิดด้วยการเข้ารหัส utf-8 ธรรมดา รอยนี้จะติดมาเป็นส่วนหนึ่งของชื่อคอลัมน์แรก

พิสูจน์ได้ด้วยการอ่าน header ด้วย csv module ของ Python

```python
import csv

with open("data/raw/customers_th.csv", encoding="utf-8", newline="") as file:
    plain_header = next(csv.reader(file))

with open("data/raw/customers_th.csv", encoding="utf-8-sig", newline="") as file:
    sig_header = next(csv.reader(file))

print("หัวตารางเมื่อเปิดด้วย utf-8 คือ", repr(plain_header[0]))
print("หัวตารางเมื่อเปิดด้วย utf-8-sig คือ", repr(sig_header[0]))
```

ผลลัพธ์

```txt
หัวตารางเมื่อเปิดด้วย utf-8 คือ '\ufeffcustomer_id'
หัวตารางเมื่อเปิดด้วย utf-8-sig คือ 'customer_id'
```

`\ufeff` ที่เห็นข้างหน้าคือ BOM

ถ้าปล่อยไว้ ชื่อคอลัมน์แรกจะไม่เท่ากับ `"customer_id"` ที่เราเขียนในโค้ด ทำให้ `df["customer_id"]` พังทั้งที่ดูด้วยตาเหมือนถูก

`utf-8-sig` คือการเข้ารหัสที่กิน BOM ให้ก่อน แล้วค่อยส่งเนื้อไฟล์ให้เรา จึงเป็นค่าที่ปลอดภัยที่สุดสำหรับไฟล์ที่มีอักษรไทย

Pandas ตัด BOM ให้เองเมื่ออ่านด้วย utf-8 แต่เครื่องมืออื่นไม่ทำแบบนั้น การใส่ `utf-8-sig` ไว้จึงทำให้โค้ดเดียวกันใช้ได้ทั้งกับ Pandas และ csv module

```python
thai = pd.read_csv("data/raw/customers_th.csv", encoding="utf-8-sig")

print(thai.shape)
print(thai.to_string())
```

ผลลัพธ์

```txt
(3, 4)
  customer_id           name       province                  email
0        C001     สมชาย ใจดี  กรุงเทพมหานคร    somchai@example.com
1        C002    นัฐพงษ์ ศรี      เชียงใหม่  nattapong@example.com
2        C003  มาลี วงศ์สกุล        ขอนแก่น      malee@example.com
```

ตรวจชื่อคอลัมน์ว่าสะอาดจริง

```python
print(list(thai.columns))
```

ผลลัพธ์

```txt
['customer_id', 'name', 'province', 'email']
```

เข้าถึงค่าภาษาไทยได้ตามปกติ

```python
print(thai.loc[0, "name"])
```

ผลลัพธ์

```txt
สมชาย ใจดี
```

## เขียนไฟล์ด้วย `to_csv`

`to_csv` รับ DataFrame แล้วเขียนลงไฟล์

มันสำคัญเพราะปลายทางของงานทำความสะอาดข้อมูลคือไฟล์ที่คนอื่นเปิดต่อได้ ไม่ใช่ตัวแปรในหน่วยความจำ

มีสองพารามิเตอร์ที่ต้องใส่ทุกครั้ง

- `index=False` ไม่ให้เขียนเลข index ลงไปเป็นคอลัมน์แรก
- `encoding="utf-8"` บังคับการเข้ารหัส

ถ้าลืม `index=False` ไฟล์ผลลัพธ์จะมีคอลัมน์แปลก ๆ โผล่มาเป็นคอลัมน์แรก ซึ่งคนปลายทางจะงงว่ามันคืออะไร

```python
from pathlib import Path

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
sample = customers.head(3)

output_path = Path("data/processed/customers_three.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
sample.to_csv(output_path, index=False, encoding="utf-8")

print(output_path.read_text(encoding="utf-8"))
```

ผลลัพธ์

```txt
customer_id,name,email,phone,country,signup_date,loyalty_tier
C001,  Nattapong Sri  ,customer1@example.com,+66801002003,Thailand,2024-11-22,GOLD
C002,Malee Wongsakul,customer2@example.com,(66) 802003004,LA,2024/04/25,gold
C003,Kanya P.,customer3@example.com,080-300-4005,Thailand,2024/08/20,silver
```

ไฟล์ที่ได้มี header หนึ่งบรรทัดกับข้อมูลสามบรรทัด ไม่มีคอลัมน์ index เกินมา

## อ่านไฟล์ที่เราเพิ่งเขียนกลับมา

ขั้นตอนนี้คือการตรวจว่าไฟล์ที่เขียนยังใช้ได้จริง

```python
with output_path.open(encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

print("จำนวนแถวที่อ่านกลับมาได้", len(rows))
print("แถวแรกคือ", repr(rows[0]["customer_id"]), repr(rows[0]["name"]))
```

ผลลัพธ์

```txt
จำนวนแถวที่อ่านกลับมาได้ 3
แถวแรกคือ 'C001' '  Nattapong Sri  '
```

สังเกตว่าช่องว่างหัวท้ายชื่อยังอยู่ครบ การเขียนไฟล์ไม่ทำความสะอาดให้เหมือนกับการอ่าน

อ่านด้วย Pandas กลับมาอีกครั้งแล้วเทียบกับต้นฉบับ

```python
reloaded = pd.read_csv(output_path, encoding="utf-8")

print(reloaded.shape)
print(reloaded.columns.tolist())
print()
print(reloaded.equals(sample))
```

ผลลัพธ์

```txt
(3, 7)
['customer_id', 'name', 'email', 'phone', 'country', 'signup_date', 'loyalty_tier']

True
```

`equals` คืน `True` แปลว่าเขียนแล้วอ่านกลับมาได้ค่าเดิมครบทุกช่อง

การตรวจแบบนี้ควรทำทุกครั้งหลังเขียนไฟล์ เพราะปัญหาการเข้ารหัสหรือเครื่องหมายคำพูดจะโผล่ตอนอ่านกลับเท่านั้น ไม่โผล่ตอนเขียน

## สรุป

| อยากทำอะไร | ใช้คำสั่ง |
|---|---|
| อ่านไฟล์ทั่วไป | `pd.read_csv(path, encoding="utf-8")` |
| อ่านไฟล์ภาษาไทย | `pd.read_csv(path, encoding="utf-8-sig")` |
| ไม่ให้เดาชนิด | `dtype=str` |
| เก็บช่องว่างเป็นสตริงว่าง | เพิ่ม `keep_default_na=False` |
| อ่านแค่บางคอลัมน์ | `usecols=[...]` |
| อ่านแค่บางแถว | `nrows=n` |
| ดูตัวอย่างบนสุด | `df.head(n)` |
| ดูขนาด | `df.shape` |
| ดูชนิดคอลัมน์ | `df.dtypes` |
| เขียนไฟล์ | `df.to_csv(path, index=False, encoding="utf-8")` |
| เทียบสองตาราง | `df.equals(other)` |

## โจทย์ที่ต้องทำ

เปิด `exercises/ch13-load-csv.py`

เขียนสี่ฟังก์ชันนี้

1. `load_customers(path)` อ่านไฟล์ลูกค้าด้วยการเข้ารหัส utf-8 โดยค่าเริ่มต้นคือ `data/raw/customers.csv`
2. `load_thai_customers(path)` อ่านไฟล์ลูกค้าภาษาไทยด้วยการเข้ารหัส utf-8-sig โดยค่าเริ่มต้นคือ `data/raw/customers_th.csv`
3. `save_clean(df, path)` เขียนตารางลงไฟล์ CSV โดยไม่ใส่วงศ์ index และใช้การเข้ารหัส utf-8
4. `shape_of(df)` คืนคู่จำนวนแถวกับจำนวนคอลัมน์

## ผลลัพธ์ที่คาดหวัง

รันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```cmd
python exercises/ch13-load-csv.py
```

จะได้ผลแบบนี้

```txt
(14, 7)
  customer_id               name                  email           phone   country signup_date loyalty_tier
0        C001    Nattapong Sri    customer1@example.com    +66801002003  Thailand  2024-11-22         GOLD
1        C002    Malee Wongsakul  customer2@example.com  (66) 802003004        LA  2024/04/25         gold
2        C003           Kanya P.  customer3@example.com    080-300-4005  Thailand  2024/08/20       silver

(3, 4)
  customer_id           name       province                  email
0        C001     สมชาย ใจดี  กรุงเทพมหานคร    somchai@example.com
1        C002    นัฐพงษ์ ศรี      เชียงใหม่  nattapong@example.com
2        C003  มาลี วงศ์สกุล        ขอนแก่น      malee@example.com

['customer_id', 'name', 'province', 'email']
สมชาย ใจดี
```

ตรวจงานตัวเองด้วยคำสั่งนี้

```cmd
python -m pytest tests/test_ch13.py
```

## เสร็จแล้วพิมพ์ ตรวจ Ch13
