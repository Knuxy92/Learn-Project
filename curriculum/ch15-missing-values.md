# บทที่ 15: จัดการค่าที่หายไป

## ทบทวน

บทที่แล้วเราเลือกและกรองแถวได้แล้ว รู้จักมาสก์ การรวมเงื่อนไข และการเลือกเฉพาะคอลัมน์

แต่ตารางที่กรองแล้วยังมีปัญหาเงียบ ๆ อยู่อย่างหนึ่ง คือบางช่องไม่มีค่าเลย ถ้าไม่จัดการก่อน การคำนวณทุกอย่างหลังจากนี้จะเพี้ยน

บทนี้สอนวิธีหาค่าที่หายไป นับมัน แล้วเลือกว่าจะเติมหรือตัดทิ้ง

## ค่าที่หายไปคืออะไร

ค่าที่หายไป (missing value) คือช่องที่ไม่มีข้อมูลจริง pandas แทนด้วย `NaN` หรือ `NaT` หรือ `pd.NA` ขึ้นกับชนิดคอลัมน์

ในงานทำความสะอาดข้อมูล เราต้องรู้ก่อนว่ามีเท่าไร อยู่ตรงไหน และควรเติมหรือตัด เพราะแต่ละทางเลือกกระทบผลสรุปคนละแบบ

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(customers.isna().sum())
```

ผลลัพธ์

```txt
customer_id     0
name            0
email           1
phone           1
country         0
signup_date     0
loyalty_tier    1
dtype: int64
```

`isna` ให้ตารางจริงเท็จขนาดเท่าต้นฉบับ พอเติม `.sum()` ก็ได้จำนวนต่อคอลัมน์

## ข้อความว่างไม่ใช่ค่าที่หายไป

จุดที่พลาดกันบ่อยที่สุด ข้อความว่าง `""` ไม่นับเป็นค่าที่หายไป pandas มองว่ามันเป็นข้อความปกติที่ยาวศูนย์

เวลา pandas อ่าน CSV มันแปลงช่องว่างให้เป็น `NaN` ให้เอง แต่ข้อมูลที่สร้างจากที่อื่นหรือผ่านการทำความสะอาดมาบางรอบมักมี `""` ติดมา

ถ้าเราเช็คแค่ `isna` เราจะมองไม่เห็นช่องที่ถูกกรอกเป็นช่องว่าง

```python
import pandas as pd

series = pd.Series(["gold", "", None, "   "])

print(series.isna().tolist())
print(series.str.strip().isna().tolist())
print(series.str.strip().replace("", pd.NA).isna().tolist())
```

ผลลัพธ์

```txt
[False, False, True, False]
[False, False, True, False]
[False, True, True, True]
```

บรรทัดแรกเห็นแค่ `None` บรรทัดสุดท้ายเห็นครบทั้งช่องว่างและช่องที่มีแต่เว้นวรรค

ถ้าอยากเห็นช่องว่างจาก CSV โดยไม่ให้ถูกแปลงตั้งแต่ตอนอ่าน ใช้ `keep_default_na=False`

```python
import pandas as pd

default_read = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
raw_read = pd.read_csv("data/raw/orders.csv", encoding="utf-8", keep_default_na=False)

print(default_read["status"].isna().sum())
print(raw_read["status"].isna().sum())
print(raw_read["status"].str.strip().eq("").sum())
```

ผลลัพธ์

```txt
5
0
5
```

ห้าช่องที่หายไปกลายเป็นข้อความว่างเมื่อปิดการแปลง นี่คือเหตุผลว่าทำไมต้องรู้ว่าข้อมูลผ่านอะไรมาก่อน

## เปลี่ยนข้อความว่างให้เป็นค่าที่หายไป

วิธีมาตรฐานคือตัดช่องว่างหัวท้ายก่อน แล้วเปลี่ยนข้อความว่างเป็น `pd.NA`

ทำแบบนี้ก่อนทุกครั้งที่ต้องนับหรือเติมค่า ไม่อย่างนั้นตัวเลขจะต่ำกว่าความจริง

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

tier = customers["loyalty_tier"].str.strip().replace("", pd.NA)
print(tier.isna().sum())
print(tier.dtype)
```

ผลลัพธ์

```txt
1
str
```

ค่าที่หายไปหนึ่งแถวมาจากช่องที่ว่างเปล่าในไฟล์ CSV ซึ่ง pandas อ่านเป็น `NaN` ตั้งแต่ต้น

## นับเฉพาะคอลัมน์ที่มีปัญหา

ตารางจริงมีหลายสิบคอลัมน์ การเห็นเลขศูนย์เต็มไปหมดทำให้อ่านยาก

เรากรองเอาเฉพาะคอลัมน์ที่มากกว่าศูนย์ และแปลงเป็นจำนวนเต็มเพื่อให้อ่านง่าย

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

counts = customers.isna().sum()
print(counts[counts > 0].astype(int).to_dict())
print(counts.dtype)
```

ผลลัพธ์

```txt
{'email': 1, 'phone': 1, 'loyalty_tier': 1}
int64
```

## ดูเป็นสัดส่วน

จำนวนดิบไม่บอกว่าแย่แค่ไหน คอลัมน์ที่มีหนึ่งช่องจากสิบแถวต่างจากหนึ่งช่องจากหมื่นแถว

ใช้ `mean` กับมาสก์จริงเท็จ จะได้สัดส่วนของแถวที่หายไป แล้วคูณร้อยเป็นเปอร์เซ็นต์

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(customers.isna().mean().mul(100).round(1))
```

ผลลัพธ์

```txt
customer_id     0.0
name            0.0
email           7.1
phone           7.1
country         0.0
signup_date     0.0
loyalty_tier    7.1
dtype: float64
```

## ดูแถวที่หายไปจริง

ตัวเลขรวมไม่พอ เราต้องเปิดดูว่าแถวไหนหาย เพื่อตัดสินใจได้ว่าควรเติมด้วยอะไร

ใช้มาสก์จากบทที่แล้วกรองแถวนั้นออกมาได้เลย

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(customers.loc[customers["email"].isna(), ["customer_id", "email"]])
```

ผลลัพธ์

```txt
  customer_id email
6        C007   NaN
```

## นับทั้งแถว

บางครั้งเราสนใจว่ามีแถวไหนสมบูรณ์บ้าง ไม่ใช่คอลัมน์ไหนมีปัญหา

`all(axis=1)` ถามว่า ทุกช่องในแถวนี้จริงหรือไม่ ส่วน `any(axis=1)` ถามว่า มีช่องไหนจริงบ้าง

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(customers.notna().all(axis=1).sum())
print(customers.isna().any(axis=1).sum())
```

ผลลัพธ์

```txt
11
3
```

จาก 14 แถว มี 11 แถวที่ครบทุกช่อง และ 3 แถวที่มีช่องหายอย่างน้อยหนึ่งช่อง

## เติมค่าด้วย `fillna`

`fillna` เปลี่ยนค่าที่หายไปเป็นค่าที่เรากำหนด

เราใช้เมื่อค่าที่หายไปมีความหมายที่เดาได้ เช่น ลูกค้าที่ไม่ได้ระบุระดับสมาชิก ก็ให้เป็นระดับเริ่มต้น

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

filled = customers.copy()
filled["loyalty_tier"] = filled["loyalty_tier"].fillna("Unknown")
print(filled["loyalty_tier"].isna().sum())
print(customers["loyalty_tier"].isna().sum())
```

ผลลัพธ์

```txt
0
1
```

ต้องเรียก `.copy()` ก่อนเสมอ ไม่อย่างนั้นการแก้จะไปโดนต้นฉบับด้วย

ถ้าคอลัมน์มีทั้งข้อความว่างและค่าที่หายไปจริง ต้องแปลงข้อความว่างก่อนแล้วค่อยเติม

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

tier = customers["loyalty_tier"].str.strip().replace("", pd.NA)
print(tier.fillna("Unknown").value_counts())
```

ผลลัพธ์

```txt
loyalty_tier
silver     8
Gold       3
GOLD       1
gold       1
Unknown    1
Name: count, dtype: int64
```

## เติมด้วยค่าข้างเคียง

บางข้อมูลเรียงตามเวลา เช่น ยอดขายรายวัน การเติมด้วยค่าก่อนหน้าหรือค่าถัดไปจึงสมเหตุสมผลกว่าการเติมค่าคงที่

`ffill` หมายถึงดึงค่าก่อนหน้ามาเติม ส่วน `bfill` หมายถึงดึงค่าถัดไปมาเติม

```python
import pandas as pd

series = pd.Series([None, "a", None, None, "b"])

print(series.ffill().tolist())
print(series.bfill().tolist())
print(series.fillna("x").tolist())
```

ผลลัพธ์

```txt
[nan, 'a', 'a', 'a', 'b']
['a', 'a', 'b', 'b', 'b']
['x', 'a', 'x', 'x', 'b']
```

ช่องแรกยังเป็น `nan` เพราะไม่มีค่าก่อนหน้าให้ดึง

## ตัดแถวทิ้งด้วย `dropna`

ถ้าเติมไม่ได้หรือไม่ควรเดา ทางเลือกคือตัดแถวนั้นทิ้ง

`subset` ใช้จำกัดว่าดูเฉพาะคอลัมน์ไหน ไม่ระบุแปลว่าต้องครบทุกคอลัมน์จึงจะรอด

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

dropped = customers.dropna(subset=["email"])
print(len(customers), len(dropped))
print(dropped["customer_id"].tolist())
```

ผลลัพธ์

```txt
14 13
['C001', 'C002', 'C003', 'C004', 'C005', 'C006', 'C008', 'C009', 'C010', 'C011', 'C012', 'C003', 'C003']
```

ถ้าไม่ใส่ `subset` ทุกคอลัมน์ต้องมีค่าครบ แถวที่หายไปหนึ่งช่องจะถูกตัดทันที

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(customers.dropna().shape)
print(customers.dropna(how="all").shape)
```

ผลลัพธ์

```txt
(11, 7)
(14, 7)
```

`how="all"` หมายถึงตัดเฉพาะแถวที่ทุกช่องว่างพร้อมกัน ซึ่งในข้อมูลชุดนี้ไม่มีเลย

## เลือกวิธีให้ตรงกับความหมายของข้อมูล

ไม่มีคำตอบเดียวที่ถูกทุกสถานการณ์ ขึ้นกับว่าค่าที่หายไปหมายถึงอะไร

| สถานการณ์ | วิธีที่เหมาะ |
|---|---|
| ค่าที่หายไปมีความหมายว่า ไม่ระบุ | เติมค่าคงที่ เช่น `Unknown` |
| ข้อมูลเรียงตามเวลาและค่าต่อเนื่อง | `ffill` หรือ `bfill` |
| คอลัมน์นั้นสำคัญต่อการคำนวณ | `dropna` แถวนั้นทิ้ง |
| ยังไม่รู้จะทำอะไร | นับก่อน แล้วค่อยตัดสินใจ |

## สรุป

| งานที่ต้องทำ | วิธีเขียน |
|---|---|
| เช็คค่าว่างทีละช่อง | `series.isna()` |
| นับค่าว่างต่อคอลัมน์ | `df.isna().sum()` |
| นับเฉพาะคอลัมน์ที่มีปัญหา | `counts[counts > 0]` |
| ดูเป็นเปอร์เซ็นต์ | `df.isna().mean() * 100` |
| เปลี่ยนข้อความว่างเป็นค่าว่าง | `s.str.strip().replace("", pd.NA)` |
| เติมค่าคงที่ | `s.fillna(value)` |
| เติมด้วยค่าข้างเคียง | `s.ffill()` หรือ `s.bfill()` |
| ตัดแถวที่ขาดคอลัมน์สำคัญ | `df.dropna(subset=[column])` |
| นับแถวที่สมบูรณ์ | `df.notna().all(axis=1).sum()` |

หลักจำง่าย ๆ

- `""` ไม่ใช่ค่าที่หายไป ต้องแปลงก่อน
- นับก่อน เติมทีหลัง
- เติมหรือตัดต้องดูความหมายของคอลัมน์ ไม่ใช่ดูแค่ตัวเลข
- แก้ข้อมูลต้องเรียก `.copy()` ก่อน

## โจทย์ที่ต้องทำ

เปิด `exercises/ch15-handle-missing.py` แล้วเขียนสี่ฟังก์ชันนี้

1. `missing_counts` รับตาราง คืน Series ที่นับจำนวนค่าที่หายไปต่อคอลัมน์ เฉพาะคอลัมน์ที่มากกว่าศูนย์ และเป็นจำนวนเต็ม
2. `drop_missing_key` รับตารางกับชื่อคอลัมน์ คืนตารางที่ตัดแถวซึ่งคอลัมน์นั้นเป็นค่าว่างออก
3. `empty_to_na` รับ Series ข้อความ คืน Series ที่ตัดช่องว่างหัวท้ายและเปลี่ยนข้อความว่างเป็นค่าที่หายไป
4. `fill_text` รับตารางกับชื่อคอลัมน์และค่าที่จะเติม คืนสำเนาที่เติมทั้งข้อความว่างและค่าที่หายไป

## ผลลัพธ์ที่คาดหวัง

เมื่อเขียนครบแล้วรันด้วยคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```bash
.venv/bin/python exercises/ch15-handle-missing.py
```

จะได้ผลแบบนี้

```txt
email           1
phone           1
loyalty_tier    1
เหลือ 13 แถว
[nan, 'malee@example.com', nan, 'kanya@example.com']
['gold', 'Unknown', 'silver', 'Unknown']
```

ตรวจงานตัวเองด้วยคำสั่งนี้

```bash
.venv/bin/python -m pytest tests/test_ch15.py
```

## เสร็จแล้วพิมพ์ ตรวจ Ch15
