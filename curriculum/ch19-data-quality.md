# บทที่ 19: ตรวจคุณภาพข้อมูล

## ทบทวน

บทที่ 18 สอนรวมตาราง และเห็นว่าการเชื่อมทำให้ปัญหาหลายอย่างโผล่ขึ้นมา เช่น ออเดอร์ 5 แถวที่อ้างถึงลูกค้าที่ไม่มี และยอดรายได้ที่พองขึ้นเพราะรหัสลูกค้าซ้ำ

บทนี้จะเปลี่ยนการสังเกตแบบนั้นให้เป็นขั้นตอนที่ทำซ้ำได้ เรียกว่าการตรวจคุณภาพข้อมูล (data quality check)

## คุณภาพข้อมูลสี่ด้าน

งานทำความสะอาดที่ไม่มีระบบตรวจจะพึ่งสายตาอย่างเดียว ซึ่งไม่พอเมื่อข้อมูลมีหลายพันแถว

ปัญหาที่เจอบ่อยแบ่งได้สี่ด้าน

| ด้าน | คำถามที่ถาม | ตัวอย่างในชุดข้อมูลนี้ |
|---|---|---|
| ความครบถ้วน | ค่าไหนหายไป | `quantity` ว่าง 2 แถว |
| ความไม่ซ้ำ | แถวไหนซ้ำ | `O0006` ซ้ำ 3 แถว |
| ความเชื่อมโยง | รหัสที่อ้างถึงมีจริงไหม | `C013` กับ `C014` ไม่มีในตารางลูกค้า |
| ความสมเหตุสมผล | ค่าอยู่ในช่วงที่ควรเป็นไหม | `quantity` เป็น `-1` กับ `0` |

ทั้งสี่ด้านควรเขียนเป็นฟังก์ชัน ไม่ใช่ตรวจด้วยมือทีละครั้ง

## ภาพรวมตารางด้วยคำสั่งเดียว

ก่อนลงรายละเอียด ควรเห็นภาพรวมก่อนว่าคอลัมน์ไหนมีปัญหา

`DataFrame.info` บอกชนิดข้อมูลและจำนวนค่าที่ไม่ว่าง แต่ผลลัพธ์เป็นข้อความ ไม่สะดวกนำไปกรองต่อ

วิธีที่ยืดหยุ่นกว่าคือสร้างตารางสรุปเอง โดยใช้สามเมธอดนี้

- `isna()` คืนค่าจริงเท็จว่าช่องไหนว่าง
- `nunique()` นับจำนวนค่าที่ไม่ซ้ำ โดยไม่นับค่าว่าง
- `dtype` บอกชนิดข้อมูลของคอลัมน์

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

report = pd.DataFrame(
    {
        "column": orders.columns,
        "missing": [int(orders[c].isna().sum()) for c in orders.columns],
        "unique": [int(orders[c].nunique()) for c in orders.columns],
        "dtype": [str(orders[c].dtype) for c in orders.columns],
    }
).sort_values("column").reset_index(drop=True)

print(report.to_string(index=False))
print(report.loc[report["missing"] > 0, "column"].tolist())
```

ผลลัพธ์

```txt
     column  missing  unique   dtype
customer_id        0      13     str
 order_date        0      40     str
   order_id        0      40     str
 product_id        0       8     str
   quantity        2       6 float64
     status        5       7     str
 unit_price        3      17     str
['quantity', 'status', 'unit_price']
```

อ่านตารางนี้ได้สามอย่างในครั้งเดียว

- `order_id` มี 40 ค่าไม่ซ้ำจาก 42 แถว แปลว่ามีแถวซ้ำ
- `quantity` มีค่าว่าง 2 แถว และชนิดเป็น `float64` ทั้งที่ควรเป็นจำนวนเต็ม
- `status` มีค่าว่าง 5 แถว

บรรทัดสุดท้ายกรองเอาเฉพาะคอลัมน์ที่มีค่าว่าง ซึ่งเป็นรายการที่ต้องจัดการต่อ

## หาแถวซ้ำ

`duplicated` คือเมธอดที่บอกว่าแถวไหนซ้ำกับแถวก่อนหน้า

พารามิเตอร์ `subset` กำหนดว่าจะเทียบจากคอลัมน์ไหน และ `keep=False` กำหนดให้ทำเครื่องหมายทุกแถวที่ซ้ำ ไม่ใช่แค่แถวหลัง

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

mask = orders.duplicated(subset=["order_id"], keep=False)

print(int(mask.sum()))
print(orders.loc[mask, ["order_id", "customer_id", "product_id"]].to_string(index=False))
```

ผลลัพธ์

```txt
3
order_id customer_id product_id
   O0006        C011       P006
   O0006        C011       P006
   O0006        C006       P002
```

`O0006` ปรากฏสามครั้ง สองครั้งแรกเหมือนกันทุกช่อง แต่ครั้งที่สามต่างกันที่ลูกค้าและสินค้า

แถวแบบนี้ตัดสินยากว่าแถวไหนถูก ต้องถามคนที่รู้ที่มาของข้อมูล ไม่ใช่เลือกเองตามสะดวก

ถ้าไม่ใส่ `keep=False` จะได้แค่ 2 เพราะ pandas ถือว่าแถวแรกเป็นตัวจริง

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(len(orders))
print(orders["order_id"].nunique())
print(int(orders["order_id"].duplicated().sum()))
```

ผลลัพธ์

```txt
42
40
2
```

42 แถว ลบด้วย 40 รหัสที่ไม่ซ้ำ เท่ากับ 2 แถวเกินมา

## นับซ้ำทั้งแถวกับซ้ำบางคอลัมน์

การนับซ้ำสองแบบนี้ให้คำตอบต่างกัน และสับสนกันบ่อย

- ซ้ำทั้งแถว คือทุกคอลัมน์เหมือนกันหมด
- ซ้ำบางคอลัมน์ คือเฉพาะคอลัมน์ที่ใช้เป็นกุญแจเหมือนกัน

```python
import pandas as pd

orders = pd.DataFrame(
    {
        "order_id": ["O1", "O1", "O2", "O3"],
        "quantity": [1, 1, 2, 3],
        "status": ["paid", "paid", "pending", "paid"],
    }
)

print(int(orders.duplicated(subset=["order_id"]).sum()))
print(int(orders.duplicated().sum()))
print(orders.duplicated(subset=["order_id"], keep=False).tolist())
print(orders.duplicated(subset=["order_id", "quantity"], keep=False).tolist())
```

ผลลัพธ์

```txt
1
1
[True, True, False, False]
[True, True, False, False]
```

ในตัวอย่างนี้สองบรรทัดแรกได้ผลเท่ากัน เพราะแถวที่ซ้ำเหมือนกันทุกคอลัมน์ แต่ถ้าแถวที่สองของ `O1` มี `status` ต่างออกไป บรรทัดที่สองจะกลายเป็นศูนย์ทันที

หลักคือถ้าตรวจกุญแจ ให้ระบุ `subset` เสมอ อย่าปล่อยให้เทียบทุกคอลัมน์

## เลือกแถวที่จะเก็บ

เมื่อรู้ว่ามีแถวซ้ำ ต้องตัดสินว่าจะเก็บแถวไหน `drop_duplicates` มี `keep` ให้เลือก

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

print(len(orders.drop_duplicates(subset=["order_id"], keep="first")))
print(len(orders.drop_duplicates(subset=["order_id"], keep="last")))
print(int(orders.duplicated().sum()))
```

ผลลัพธ์

```txt
40
40
1
```

ทั้งสองแบบเหลือ 40 แถวเท่ากัน แต่เก็บคนละแถว

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

repeated = orders.loc[orders.duplicated(subset=["order_id"], keep=False)]

print(repeated[["order_id", "customer_id", "product_id", "quantity"]].to_string(index=False))
print("---keep first---")
print(
    orders.drop_duplicates(subset=["order_id"], keep="first")
    .loc[lambda d: d["order_id"] == "O0006", ["order_id", "customer_id", "product_id"]]
    .to_string(index=False)
)
print("---keep last---")
print(
    orders.drop_duplicates(subset=["order_id"], keep="last")
    .loc[lambda d: d["order_id"] == "O0006", ["order_id", "customer_id", "product_id"]]
    .to_string(index=False)
)
```

ผลลัพธ์

```txt
order_id customer_id product_id  quantity
   O0006        C011       P006       NaN
   O0006        C011       P006       NaN
   O0006        C006       P002       1.0
---keep first---
order_id customer_id product_id
   O0006        C011       P006
---keep last---
order_id customer_id product_id
   O0006        C006       P002
```

`keep="first"` เก็บแถวแรกที่เจอ `keep="last"` เก็บแถวสุดท้าย

ในไปป์ไลน์จริงมักเลือก `keep="last"` เพราะถือว่าแถวที่ถูกเพิ่มทีหลังคือข้อมูลที่แก้ไขล่าสุด แต่ต้องยืนยันกับเจ้าของข้อมูลก่อนเสมอ

## ตรวจความเชื่อมโยงระหว่างตาราง

ความเชื่อมโยง (referential integrity) คือเงื่อนไขที่ว่ารหัสทุกตัวในตารางลูก ต้องมีอยู่ในตารางแม่

ตารางลูก (child) คือตารางที่อ้างถึง เช่น `orders` ตารางแม่ (parent) คือตารางที่ถูกอ้างถึง เช่น `customers`

วิธีตรวจคือเอารหัสของตารางแม่มาเก็บเป็นชุด แล้วถามว่าค่าในตารางลูกอยู่ในชุดนั้นไหม

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

parent_keys = customers["customer_id"].dropna().unique()
mask = ~orders["customer_id"].isin(parent_keys)

print(int(mask.sum()))
print(orders.loc[mask, ["order_id", "customer_id"]].to_string(index=False))
```

ผลลัพธ์

```txt
5
order_id customer_id
   O0009        C013
   O0014        C014
   O0016        C013
   O0017        C014
   O0035        C013
```

`dropna()` ก่อนดึงรหัสสำคัญ เพราะถ้าตารางแม่มีค่าว่าง ค่าว่างจะกลายเป็นรหัสที่ทุกแถวของตารางลูกที่มีค่าว่างจับคู่ได้ ซึ่งไม่ใช่สิ่งที่ต้องการ

ออเดอร์ 5 แถวนี้ชี้ไปยัง `C013` กับ `C014` ซึ่งไม่มีอยู่จริง

ตรวจฝั่งสินค้าด้วยวิธีเดียวกัน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
products = pd.read_csv("data/raw/products.csv", encoding="utf-8")

missing_products = orders.loc[
    ~orders["product_id"].isin(products["product_id"]), "product_id"
].unique()
unused_products = products.loc[
    ~products["product_id"].isin(orders["product_id"]), "product_id"
].unique()

print(sorted(missing_products.tolist()))
print(len(missing_products))
print(sorted(unused_products.tolist()))
```

ผลลัพธ์

```txt
[]
0
[]
```

ฝั่งสินค้าไม่มีปัญหาเลย ทุกออเดอร์อ้างถึงสินค้าที่มีจริง และสินค้าทุกตัวถูกสั่งซื้ออย่างน้อยหนึ่งครั้ง

การเห็นว่า `0` มีค่ามากพอ ๆ กับการเห็นว่า `5` เพราะมันยืนยันว่าปัญหาอยู่ที่ตารางลูกค้าเพียงจุดเดียว

## ตรวจช่วงค่าที่สมเหตุสมผล

การตรวจช่วง (range check) คือการถามว่าค่าอยู่ในช่วงที่ยอมรับได้ไหม

ต้องแปลงเป็นตัวเลขก่อน เพราะการเทียบข้อความจะให้ผลผิด

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")

quantity = pd.to_numeric(orders["quantity"], errors="coerce")
outside = (quantity < 1) | (quantity > 100)

print(int(outside.sum()))
print(orders.loc[outside, ["order_id", "quantity"]].to_string(index=False))
```

ผลลัพธ์

```txt
10
order_id  quantity
   O0003      -1.0
   O0005       0.0
   O0010      -1.0
   O0015      -1.0
   O0018       0.0
   O0020      -1.0
   O0025       0.0
   O0033       0.0
   O0034       0.0
   O0036       0.0
```

มี 10 แถวที่จำนวนชิ้นไม่สมเหตุสมผล แบ่งเป็น `-1` สี่แถวกับ `0` หกแถว

`errors="coerce"` ทำให้ค่าที่แปลงไม่ได้กลายเป็นค่าว่าง ซึ่งไม่ถูกนับว่านอกช่วง เพราะ `NaN` เทียบกับตัวเลขแล้วได้เท็จทั้งสองข้าง

นี่คือพฤติกรรมที่ต้องการ เพราะค่าว่างมีปัญหาอีกแบบหนึ่ง ไม่ควรปนกับการตรวจช่วง

## แยกค่าว่างออกจากข้อความว่าง

`read_csv` แปลงข้อความว่างเป็นค่าว่างให้อัตโนมัติ แต่บางครั้งต้องรู้ว่าต้นฉบับเป็นอะไร

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
raw = pd.read_csv("data/raw/orders.csv", dtype=str, keep_default_na=False)

print(int(orders["quantity"].isna().sum()))
print(int(raw["quantity"].eq("").sum()))
print(int(orders["status"].isna().sum()))
print(int(raw["status"].eq("").sum()))
```

ผลลัพธ์

```txt
2
2
5
5
```

ทั้งสองแบบได้ตัวเลขเท่ากันในชุดข้อมูลนี้ เพราะช่องว่างในไฟล์เป็นข้อความว่างจริง ไม่ใช่ช่องที่ไม่มีข้อมูล

แต่ถ้าเจอไฟล์ที่ใช้ `NA` หรือ `-` แทนค่าว่าง สองวิธีนี้จะให้คำตอบต่างกัน

`keep_default_na=False` สำคัญเมื่อต้องแยกให้ออกว่าข้อมูลหายไปหรือผู้กรอกตั้งใจใส่ค่าว่าง

## ผลกระทบของปัญหาต่อการวิเคราะห์

ตัวเลขปัญหาแต่ละด้านดูเล็ก แต่ผลรวมแล้วเปลี่ยนข้อสรุป

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

joined = orders.merge(customers[["customer_id", "name"]], on="customer_id", how="left")

print(int(joined["name"].isna().sum()))
print(int(joined["name"].notna().sum()))
print(f"{joined['name'].notna().mean():.3f}")
```

ผลลัพธ์

```txt
5
51
0.911
```

ถ้ารายงานว่า "ลูกค้าทุกคนซื้อสินค้า" จะผิด เพราะออเดอร์ 5 แถวไม่รู้ว่าเป็นของใคร

และถ้ารายงานยอดขายต่อลูกค้าโดยไม่ตรวจรหัสซ้ำก่อน ยอดจะพองขึ้นอีกชั้นหนึ่งเหมือนที่เห็นในบทที่ 18

## สรุป

ลำดับการตรวจที่ใช้ซ้ำได้

| ขั้น | ฟังก์ชัน | คำถามที่ตอบ |
|---|---|---|
| 1 | `isna()` กับ `nunique()` | คอลัมน์ไหนมีปัญหา |
| 2 | `duplicated(keep=False)` | แถวไหนซ้ำ |
| 3 | `isin()` | รหัสที่อ้างถึงมีจริงไหม |
| 4 | `to_numeric()` แล้วเทียบช่วง | ค่าสมเหตุสมผลไหม |

หลักที่ต้องจำ

- ตรวจกุญแจด้วย `subset` เสมอ ไม่ปล่อยให้เทียบทุกคอลัมน์
- `keep=False` เมื่อต้องการเห็นทุกแถวที่เกี่ยวข้อง ไม่ใช่แค่แถวที่เกินมา
- `dropna()` ก่อนดึงรหัสจากตารางแม่
- `errors="coerce"` ก่อนตรวจช่วง เพื่อไม่ให้ค่าที่แปลงไม่ได้ถูกนับผิด
- เก็บผลการตรวจไว้เป็นตาราง ไม่ใช่พิมพ์ทิ้ง เพราะต้องเอาไปรายงาน

## โจทย์ที่ต้องทำ

เปิดไฟล์ `exercises/ch19-quality-report.py` แล้วเติมสี่ฟังก์ชันนี้

1. `quality_report` คืนตารางสรุปที่มีคอลัมน์ `column` `missing` `unique` `dtype` เรียงตามชื่อคอลัมน์
2. `find_duplicates` คืนทุกแถวที่ค่าใน `subset` ซ้ำกับแถวอื่น
3. `find_out_of_range` คืนแถวที่ค่าของ `column` นอกช่วง `low` ถึง `high` โดยรวมขอบทั้งสองข้าง
4. `referential_issues` คืนแถวของ `child` ที่ค่า `key` ไม่มีอยู่ใน `parent`

ทุกฟังก์ชันต้องคืนตารางใหม่ ไม่แก้ตารางที่รับเข้ามา

## ผลลัพธ์ที่คาดหวัง

รันคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```cmd
python exercises/ch19-quality-report.py
```

ต้องได้ผลแบบนี้

```txt
ภาพรวมตาราง orders
     column  missing  unique   dtype
customer_id        0      13     str
 order_date        0      40     str
   order_id        0      40     str
 product_id        0       8     str
   quantity        2       6 float64
     status        5       7     str
 unit_price        3      17     str
แถวที่ order_id ซ้ำ 3 แถว
ออเดอร์ที่ชี้ไปยังลูกค้าที่ไม่มี 5 แถว
ออเดอร์ที่จำนวนอยู่นอกช่วง 10 แถว
```

## เสร็จแล้วพิมพ์

```txt
ตรวจ Ch19
```
