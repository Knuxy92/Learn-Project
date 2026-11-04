# บทที่ 21: งานท้าย ทำความสะอาดชุดข้อมูลจริง

## ทบทวน

บทที่แล้วเราประกอบไปป์ไลน์ที่รันซ้ำได้จากข้อมูลดิบสามตาราง

บทนี้คืองานท้าย เราไม่ได้เรียนแนวคิดใหม่ แต่เอาไปป์ไลน์เดิมมาขยายเป็นงานที่ต้องส่งมอบจริง คือมีรายงาน มีไฟล์ผลลัพธ์ และมีคำอธิบายว่าทำไมจึงตัดสินใจแบบนั้น

ความต่างหลักมีสามข้อ

1. บทที่แล้วไปป์ไลน์รับตารางที่อ่านมาแล้ว บทนี้รับโฟลเดอร์และอ่านเอง
2. บทที่แล้วได้ตารางรวมตารางเดียว บทนี้ได้ตารางสรุปสองแบบที่ตอบคำถามทางธุรกิจ
3. บทที่แล้วไม่มีรายงาน บทนี้ต้องเขียนรายงานคุณภาพข้อมูลและบันทึกการตัดสินใจ

## งานท้ายคืออะไร

งานท้ายคือการรับโจทย์ที่กว้างกว่าบทอื่น แล้วเลือกเองว่าจะทำอย่างไร

โจทย์ของเราคือ ทำความสะอาดข้อมูลร้านค้าสามตาราง แล้วตอบคำถามสองข้อ

1. ลูกค้าแต่ละคนสร้างรายได้เท่าไร
2. แต่ละเดือนยอดขายเป็นอย่างไร

ทำไมต้องมีรายงาน เพราะข้อมูลจริงไม่เคยสะอาดพอ การบอกว่า "ลบ 2 แถวทิ้ง" โดยไม่บอกว่าลบเพราะอะไร ทำให้คนที่อ่านผลลัพธ์ต่อเชื่อตัวเลขไม่ได้

รายงานที่ดีตอบสามคำถาม คือเจออะไร เสียหายแค่ไหน และเลือกทำอะไรกับมัน

## ขั้นที่หนึ่ง สำรวจก่อนแตะข้อมูล

ก่อนเขียนโค้ดทำความสะอาด ให้วัดปัญหาก่อนว่ามีเท่าไร

ทำไมต้องวัด เพราะถ้าเราไม่รู้ขนาดปัญหา เราจะบอกไม่ได้ว่าหลังทำความสะอาดแล้วหายไปเท่าไร

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)
customers = pd.read_csv("data/raw/customers.csv", dtype=str)
products = pd.read_csv("data/raw/products.csv", dtype=str)

for name, frame in (("customers", customers), ("orders", orders), ("products", products)):
    print(f"{name} {frame.shape[0]} แถว {frame.shape[1]} คอลัมน์")
    print(f"  ช่องที่ว่าง {int(frame.isna().sum().sum())} ช่อง")
```

ผลลัพธ์

```txt
customers 14 แถว 7 คอลัมน์
  ช่องที่ว่าง 3 ช่อง
orders 42 แถว 7 คอลัมน์
  ช่องที่ว่าง 10 ช่อง
products 8 แถว 4 คอลัมน์
  ช่องที่ว่าง 0 ช่อง
```

ตารางสินค้าสะอาดที่สุด ไม่มีช่องว่างเลย ตารางออเดอร์สกปรกที่สุด

ต่อด้วยการวัดปัญหาที่เป็นเชิงโครงสร้าง คือแถวซ้ำและรหัสที่อ้างไม่ถึง

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)
orders = pd.read_csv("data/raw/orders.csv", dtype=str)

print(f"รหัสลูกค้าซ้ำ {int(customers['customer_id'].duplicated().sum())} แถว")
print(f"รหัสออเดอร์ซ้ำ {int(orders['order_id'].duplicated().sum())} แถว")

known = set(customers["customer_id"])
orphans = orders.loc[~orders["customer_id"].isin(known)]
print(f"ออเดอร์ที่ไม่มีลูกค้า {len(orphans)} แถว")
print(sorted(orphans["customer_id"].unique()))
```

ผลลัพธ์

```txt
รหัสลูกค้าซ้ำ 2 แถว
รหัสออเดอร์ซ้ำ 2 แถว
ออเดอร์ที่ไม่มีลูกค้า 5 แถว
['C013', 'C014']
```

`duplicated().sum()` นับแถวที่ซ้ำ ไม่ได้นับจำนวนชุดที่ซ้ำ รหัส C003 มีสามแถว จึงถูกนับเป็นสอง

## ขั้นที่สอง ตัดสินใจเรื่องค่าที่ผิดปกติ

ออเดอร์มีจำนวนติดลบและจำนวนเป็นศูนย์

ทำไมต้องคิดให้ดี เพราะการลบแถวทิ้งเปลี่ยนยอดรวม และอาจลบยอดที่ลูกค้าคืนสินค้าจริงออกไป

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)
quantity = pd.to_numeric(orders["quantity"], errors="coerce")

print(f"ติดลบ {int((quantity < 0).sum())} แถว")
print(f"เป็นศูนย์ {int((quantity == 0).sum())} แถว")
print(f"ว่าง {int(quantity.isna().sum())} แถว")
print(sorted(quantity.dropna().unique().tolist()))
```

ผลลัพธ์

```txt
ติดลบ 4 แถว
เป็นศูนย์ 6 แถว
ว่าง 2 แถว
[-1.0, 0.0, 1.0, 2.0, 3.0, 5.0]
```

ค่าที่เป็นไปได้มีแค่หกค่า และค่าติดลบมีค่าเดียวคือ `-1`

การที่ค่าติดลบมีแค่ `-1` แปลว่านี่ไม่ใช่ยอดคืนสินค้าที่มีขนาดต่างกัน แต่เป็นรหัสแทนความหมายบางอย่าง เช่น ยกเลิก หรือส่งคืนทั้งออเดอร์

ในงานนี้เราเลือกเก็บไว้และติดลบในรายได้ เพราะไม่มีเอกสารยืนยันความหมาย แต่ถ้าเป็นงานจริงต้องถามเจ้าของข้อมูลก่อน

ผลของการเก็บไว้เห็นได้ชัดเมื่อคำนวณรายได้

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)
quantity = pd.to_numeric(orders["quantity"], errors="coerce")
price = pd.to_numeric(
    orders["unit_price"].str.replace("฿", "", regex=False).str.replace(",", "", regex=False),
    errors="coerce",
)
revenue = quantity * price

print(f"ออเดอร์ที่รายได้ติดลบ {int((revenue < 0).sum())} แถว")
print(f"แถวที่คำนวณรายได้ไม่ได้ {int(revenue.isna().sum())} แถว")
print(f"ยอดรวมทั้งตาราง {revenue.sum():,.0f} บาท")
```

ผลลัพธ์

```txt
ออเดอร์ที่รายได้ติดลบ 4 แถว
แถวที่คำนวณรายได้ไม่ได้ 5 แถว
ยอดรวมทั้งตาราง 72,245 บาท
```

ห้าแถวที่คำนวณไม่ได้คือแถวที่ราคาว่าง หรือจำนวนว่าง สองอย่างนี้รวมกันทำให้ `revenue` เป็นค่าว่าง

`sum()` ข้ามค่าว่างไป จึงยังได้ตัวเลขออกมา แต่ตัวเลขนั้นไม่ครบ

## ขั้นที่สาม อ่านข้อมูลดิบจากโฟลเดอร์

ไปป์ไลน์จริงรับโฟลเดอร์ ไม่ได้ฝังชื่อไฟล์ไว้ในโค้ด

ทำไมต้องเป็นแบบนั้น เพราะเราต้องรันกับข้อมูลเดือนใหม่ได้โดยไม่แก้โค้ด

```python
from pathlib import Path

import pandas as pd


def load_raw(raw_dir: str | Path = "data/raw") -> dict[str, pd.DataFrame]:
    base = Path(raw_dir)
    return {
        "customers": pd.read_csv(base / "customers.csv", dtype=str, encoding="utf-8"),
        "orders": pd.read_csv(base / "orders.csv", dtype=str, encoding="utf-8"),
        "products": pd.read_csv(base / "products.csv", dtype=str, encoding="utf-8"),
    }


tables = load_raw()
print(sorted(tables))
print(len(tables["customers"]), len(tables["orders"]), len(tables["products"]))
```

ผลลัพธ์

```txt
['customers', 'orders', 'products']
14 42 8
```

การคืนดิกชันแทนการคืนทูเปิลทำให้เรียกใช้ด้วยชื่อได้ อ่านแล้วรู้ทันทีว่าตัวไหนคือตารางอะไร

ถ้าเป็นทูเปิล `customers, orders, products = load_raw()` จะพังเงียบ ๆ ถ้าสลับลำดับ

## ขั้นที่สี่ ทำความสะอาดทั้งชุดด้วยกฎเดิม

ขั้นนี้คือการนำกฎจากบทที่แล้วมาใช้ซ้ำ ไม่มีกฎใหม่

ทำไมต้องใช้กฎเดิม เพราะถ้าแต่ละบทใช้กฎต่างกัน ผลลัพธ์จะเทียบกันไม่ได้

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)
customers = customers.drop_duplicates(subset=["customer_id"], keep="last")

country = customers["country"].astype("string").str.strip().str.title()
mapping = {"Th": "Thailand", "Thailand": "Thailand", "La": "Laos", "Laos": "Laos"}
customers["country"] = country.map(mapping).fillna(country)

print(f"ลูกค้า {len(customers)} แถว")
print(customers["country"].value_counts().to_string())
```

ผลลัพธ์

```txt
ลูกค้า 12 แถว
country
Thailand    7
Laos        5
```

ออเดอร์ใช้กฎหกข้อเรียงกัน คือตัดรหัสซ้ำ แปลงจำนวน แปลงราคา แปลงวันที่ ปรับสถานะ และตัดแถวที่ไม่มีกุญแจ

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)

for column in ("order_id", "customer_id", "product_id"):
    orders[column] = orders[column].astype("string").str.strip().replace("", pd.NA)

orders = orders.drop_duplicates(subset=["order_id"], keep="last")
orders = orders.dropna(subset=["order_id", "customer_id", "product_id"])
orders["quantity"] = pd.to_numeric(orders["quantity"], errors="coerce").astype("Int64")

status = orders["status"].astype("string").str.strip().str.lower()
status = status.replace("", pd.NA).fillna("unknown")
orders["status"] = status.replace({"canceled": "cancelled"})

print(f"ออเดอร์ {len(orders)} แถว")
print(orders["status"].value_counts().to_string())
print(orders["quantity"].dtype)
```

ผลลัพธ์

```txt
ออเดอร์ 40 แถว
status
cancelled    13
unknown      10
paid          9
pending       8
Int64
```

สังเกตว่าหลังตัดแถวซ้ำแล้ว จำนวน `paid` ลดจาก 11 เหลือ 9 เพราะสองในสามแถวของ O0006 ที่ซ้ำกันถูกตัดออก

## ขั้นที่ห้า ต่อตารางและคำนวณรายได้

ขั้นนี้เหมือนบทที่แล้วทุกประการ ต่างกันแค่รับดิกชันเข้ามาแทนที่จะรับสามตัวแปร

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)
customers = pd.read_csv("data/raw/customers.csv", dtype=str)
products = pd.read_csv("data/raw/products.csv", dtype=str)

orders = orders.drop_duplicates(subset=["order_id"], keep="last")
customers = customers.drop_duplicates(subset=["customer_id"], keep="last")

master = orders.merge(customers, on="customer_id", how="left")
master = master.merge(products, on="product_id", how="left")

quantity = pd.to_numeric(master["quantity"], errors="coerce")
price = pd.to_numeric(
    master["unit_price"].str.replace("฿", "", regex=False).str.replace(",", "", regex=False),
    errors="coerce",
)
master["revenue"] = quantity * price

print(f"ตารางรวม {len(master)} แถว")
print(f"ลูกค้าที่ปรากฏในตาราง {master['customer_id'].nunique()} คน")
print(f"แถวที่ไม่มีชื่อลูกค้า {int(master['name'].isna().sum())} แถว")
```

ผลลัพธ์

```txt
ตารางรวม 40 แถว
ลูกค้าที่ปรากฏในตาราง 13 คน
แถวที่ไม่มีชื่อลูกค้า 5 แถว
```

สิบสามคนนี้มาจากลูกค้าสิบสองคนบวกอีกสองรหัสที่ไม่มีในตารางลูกค้า ลบหนึ่งคนที่ไม่มีออเดอร์เลย

คนที่ไม่มีออเดอร์คือ C010 ซึ่งหายไปจากตารางรวมเพราะเราต่อจากฝั่งออเดอร์

## ขั้นที่หก สรุปรายลูกค้า

การสรุปคือการยุบหลายแถวให้เหลือแถวเดียวต่อกลุ่ม

ทำไมต้องสรุป เพราะคำถามทางธุรกิจถามว่ารายได้ต่อคนเท่าไร ไม่ได้ถามว่าออเดอร์แต่ละใบเป็นอย่างไร

```python
import pandas as pd

master = pd.DataFrame(
    {
        "customer_id": ["C1", "C1", "C2"],
        "name": ["Malee", "Malee", "Anan"],
        "order_id": ["O1", "O2", "O3"],
        "revenue": [100.0, 250.0, 50.0],
    }
)

summary = master.groupby("customer_id", as_index=False).agg(
    name=("name", "first"),
    orders=("order_id", "count"),
    revenue=("revenue", "sum"),
)
print(summary.to_string(index=False))
```

ผลลัพธ์

```txt
customer_id  name  orders  revenue
         C1 Malee       2    350.0
         C2  Anan       1     50.0
```

`agg` แบบมีชื่อ (named aggregation) ให้เราตั้งชื่อคอลัมน์ผลลัพธ์ได้เอง พร้อมระบุว่าคอลัมน์นั้นมาจากคอลัมน์ไหนและใช้ฟังก์ชันอะไร

ต่างจากการเขียน `["revenue"].sum()` ตรงที่ทำได้หลายคอลัมน์พร้อมกันในครั้งเดียว

`as_index=False` เก็บ `customer_id` ไว้เป็นคอลัมน์ธรรมดา ไม่ย้ายไปเป็นดัชนี

จากนั้นเรียงจากรายได้มากไปน้อย

```python
import pandas as pd

master = pd.DataFrame({"customer_id": ["C1", "C2", "C3"], "revenue": [100.0, 900.0, 400.0]})

print(master.sort_values("revenue", ascending=False).reset_index(drop=True).to_string(index=False))
```

ผลลัพธ์

```txt
customer_id  revenue
         C2    900.0
         C3    400.0
         C1    100.0
```

`reset_index(drop=True)` จำเป็นทุกครั้งหลังเรียง เพราะการเรียงไม่ได้เปลี่ยนดัชนีเดิม ถ้าไม่รีเซ็ต ไฟล์ที่เขียนออกมาจะมีเลขดัชนีกระโดด

## ขั้นที่เจ็ด สรุปรายเดือน

การสรุปรายเดือนต่างจากรายลูกค้าตรงที่ต้องสร้างคอลัมน์เดือนก่อน

ทำไมต้องสร้าง เพราะ `groupby` กับวันที่แบบเต็มจะได้หนึ่งกลุ่มต่อหนึ่งวัน ซึ่งไม่ใช่สิ่งที่เราต้องการ

```python
import pandas as pd

ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"


def parse_mixed_dates(series: pd.Series) -> pd.Series:
    text = series.astype("string").str.strip()
    iso_like = text.str.match(ISO_DATE_PATTERN)

    iso = pd.to_datetime(text.where(iso_like), format="mixed", dayfirst=False, errors="coerce")
    day_first = pd.to_datetime(
        text.where(~iso_like), format="mixed", dayfirst=True, errors="coerce"
    )

    return iso.fillna(day_first)


orders = pd.read_csv("data/raw/orders.csv", dtype=str)
orders["quantity"] = pd.to_numeric(orders["quantity"], errors="coerce").astype("Int64")
orders["order_date"] = parse_mixed_dates(orders["order_date"])
orders = orders.assign(month=orders["order_date"].dt.strftime("%Y-%m"))

summary = orders.groupby("month", as_index=False).agg(orders=("order_id", "count"))
print(summary.head(4).to_string(index=False))
print(f"จำนวนเดือน {len(summary)}")
```

ผลลัพธ์

```txt
  month  orders
2025-01       3
2025-02       5
2025-03       4
2025-04       7
จำนวนเดือน 11
```

`strftime("%Y-%m")` ให้ข้อความอย่าง `2025-01` ซึ่งเรียงตามตัวอักษรแล้วได้ลำดับเดียวกับการเรียงตามเวลา

ถ้าใช้ `dt.month` เอาแต่เลขเดือน จะเรียงข้ามปีผิดทันที

## ขั้นที่แปด เขียนผลลัพธ์สามไฟล์

งานท้ายต้องส่งมอบไฟล์ ไม่ได้จบที่ตัวเลขบนหน้าจอ

ทำไมต้องมีตารางสรุปแยกจากตารางรวม เพราะคนอ่านต่างกันใช้ไฟล์ต่างกัน คนทำรายงานใช้ตารางสรุป คนตรวจสอบใช้ตารางรวม

```python
from pathlib import Path

import pandas as pd

out_dir = Path("data/processed/final")
out_dir.mkdir(parents=True, exist_ok=True)

frames = {
    "master.csv": pd.DataFrame({"order_id": ["O1", "O2"], "revenue": [100.0, 250.0]}),
    "customer_summary.csv": pd.DataFrame({"customer_id": ["C1"], "revenue": [350.0]}),
    "monthly_summary.csv": pd.DataFrame({"month": ["2025-01"], "revenue": [350.0]}),
}
for filename, frame in frames.items():
    frame.to_csv(out_dir / filename, index=False, encoding="utf-8")

print(sorted(frames))
print(sorted(path.name for path in out_dir.glob("*.csv")))
```

ผลลัพธ์

```txt
['customer_summary.csv', 'master.csv', 'monthly_summary.csv']
['customer_summary.csv', 'master.csv', 'monthly_summary.csv']
```

การคืนรายชื่อไฟล์ที่เขียนออกมาเป็นประโยชน์ เพราะขั้นถัดไปสามารถตรวจได้ว่าครบสามไฟล์จริง

## ตัวอย่างที่รันได้

ไฟล์ `curriculum/ch21/final-example.py` ทำรายงานคุณภาพข้อมูลก่อนลงมือทำความสะอาด

```txt
    ตาราง      คอลัมน์  ค่าหายไป  ค่าไม่ซ้ำ ชนิด
customers  customer_id         0         12  str
customers         name         0         11  str
customers        email         1         12  str
customers        phone         1         12  str
customers      country         0          5  str
customers  signup_date         0         13  str
customers loyalty_tier         1          5  str

 ตาราง     คอลัมน์  ค่าหายไป  ค่าไม่ซ้ำ ชนิด
orders    order_id         0         40  str
orders customer_id         0         13  str
orders  product_id         0          8  str
orders    quantity         2          6  str
orders   unit_price         3         17  str
orders    order_date         0         40  str
orders      status         5          7  str

   ตาราง      คอลัมน์  ค่าหายไป  ค่าไม่ซ้ำ ชนิด
products   product_id         0          8  str
products product_name         0          8  str
products     category         0          7  str
products   list_price         0          8  str

รหัสลูกค้าซ้ำ 2 แถว
รหัสออเดอร์ซ้ำ 2 แถว
ออเดอร์ที่ไม่มีลูกค้า 5 แถว
order_id customer_id
   O0009        C013
   O0014        C014
   O0016        C013
   O0017        C014
   O0035        C013
```

อ่านตารางนี้ให้เป็น จะเห็นปัญหาครบก่อนเขียนโค้ดสักบรรทัด

`customers` มีค่าไม่ซ้ำสิบสองจากสิบสี่แถว แปลว่ามีรหัสซ้ำ

`orders` มีรหัสลูกค้าไม่ซ้ำสิบสามค่า แต่ตารางลูกค้ามีแค่สิบสองรหัส แปลว่ามีรหัสที่อ้างถึงไม่ได้อย่างน้อยหนึ่งรหัส

`products` มีค่าไม่ซ้ำแปดจากแปดแถวทั้งสี่คอลัมน์ แปลว่าสะอาดจริง

## รายงานที่ต้องเขียน

รายงานของคุณต้องมีสี่ส่วน

1. ปัญหาที่พบ พร้อมจำนวนที่วัดได้จริง
2. การตัดสินใจในแต่ละปัญหา และเหตุผล
3. ผลลัพธ์หลังทำความสะอาด เทียบกับก่อนทำ
4. ข้อจำกัดที่ยังเหลืออยู่

ส่วนที่สี่คือส่วนที่คนมักลืม แต่เป็นส่วนที่ทำให้รายงานน่าเชื่อถือ

ตัวอย่างข้อจำกัดที่ต้องเขียนในงานนี้

- ออเดอร์ห้าแถวอ้างรหัสลูกค้า C013 กับ C014 ซึ่งไม่มีในตารางลูกค้า เราคงแถวไว้เพราะรายได้ยังเป็นของจริง แต่ชื่อลูกค้าเป็นค่าว่าง
- ออเดอร์ที่จำนวนติดลบสี่แถวยังอยู่ในตารางรวม รายได้จึงติดลบด้วย ยังไม่มีเอกสารยืนยันว่าติดลบหมายถึงอะไร
- แถวที่ราคาว่างสามแถวหลังตัดรหัสซ้ำทำให้รายได้เป็นค่าว่าง ยอดรวมจึงไม่ครบ
- การเก็บแถวหลังสุดของรหัสที่ซ้ำเป็นการเดา ยังไม่ได้ยืนยันกับเจ้าของข้อมูล

ผลลัพธ์จริงที่ได้คือ

```txt
customers 12 แถว
orders 40 แถว
products 8 แถว
master 40 แถว
customer_summary 13 แถว
monthly_summary 11 แถว
```

และตารางสรุปรายลูกค้าที่เขียนออกมาเป็นไฟล์

```txt
customer_id,name,orders,revenue
C003,Malee Wongsakul,7,13310.0
C007,Wilai Thongchai,4,12720.0
C002,Malee Wongsakul,4,9300.0
C008,Chatchai Boonmee,1,8400.0
C012,Malee Wongsakul,6,6735.0
C006,Prasit Kaew,2,6050.0
C013,,3,5700.0
C004,Anan Chaiyaporn,1,3180.0
C005,Suda Meesuk,4,2410.0
C014,,2,1790.0
C009,Ratana Srisuk,2,1150.0
C011,Nattapong Sri,2,900.0
C001,Nattapong Sri,2,600.0
```

สองแถวที่ชื่อว่างคือ C013 กับ C014 ตรงกับข้อจำกัดที่เขียนไว้ข้างบน

ยอดรวมของทุกลูกค้าคือ 72,245 บาท ซึ่งเท่ากับยอดรวมของตารางรวม

## สรุป

| งาน | ฟังก์ชันที่ใช้ | จุดที่พลาดบ่อย |
|---|---|---|
| อ่านทั้งโฟลเดอร์ | `read_csv(base / "name.csv")` | ฝังชื่อไฟล์ในโค้ด |
| วัดปัญหา | `isna().sum()`, `duplicated().sum()` | นับชุดที่ซ้ำแทนที่จะนับแถว |
| ตัดซ้ำ | `drop_duplicates(keep="last")` | ลืมบอก `subset` |
| สรุปกลุ่ม | `groupby().agg()` | ลืม `as_index=False` |
| เรียงแล้วรีเซ็ต | `sort_values().reset_index(drop=True)` | ลืมรีเซ็ตก่อนเขียนไฟล์ |
| สร้างเดือน | `dt.strftime("%Y-%m")` | ใช้ `dt.month` แล้วเรียงข้ามปีผิด |
| เขียนไฟล์ | `to_csv(index=False)` | ลืม `index=False` |
| คืนรายชื่อไฟล์ | `sorted(frames)` | คืนเป็นลิสต์ที่ลำดับไม่แน่นอน |

หลักจำง่าย ๆ

- วัดก่อนแก้ ตัวเลขก่อนกับหลังต้องเทียบกันได้
- ทุกแถวที่หายไปต้องมีเหตุผลเขียนไว้
- ข้อจำกัดที่ยังเหลืออยู่ต้องเขียนไว้ ไม่ใช่ซ่อน
- ไปป์ไลน์ต้องรันซ้ำได้ ผลเท่าเดิมทุกครั้ง

## โจทย์ที่ต้องทำ

เปิด `exercises/ch21-final-report.py` แล้วเขียนเจ็ดฟังก์ชันนี้

1. `load_raw` รับโฟลเดอร์ คืนดิกชันที่มีคีย์ `customers`, `orders`, `products`
2. `clean_all` รับดิกชันตารางดิบ คืนดิกชันตารางที่ทำความสะอาดแล้วด้วยกฎเดิมจากบทที่แล้ว
3. `build_master` รับดิกชันตารางที่สะอาดแล้ว คืนตารางรวมที่มีคอลัมน์ `revenue`
4. `customer_summary` คืนตารางสรุปลูกค้าที่มีคอลัมน์ `customer_id`, `name`, `orders`, `revenue` เรียงรายได้มากไปน้อย
5. `monthly_summary` คืนตารางสรุปรายเดือนที่มีคอลัมน์ `month`, `orders`, `revenue` เรียงเดือนเก่าไปใหม่
6. `save_outputs` เขียนสามไฟล์ CSV คืนรายชื่อไฟล์ที่เขียนเรียงตามตัวอักษร
7. `run` เรียกทุกขั้นตามลำดับ คืนจำนวนแถวของทุกตาราง

กติกาเพิ่มเติม

- ห้ามแก้ตารางต้นฉบับ
- ฟังก์ชันคืนค่า ไม่พิมพ์ผลข้างใน
- `run` ต้องสร้างโฟลเดอร์ปลายทางเองถ้ายังไม่มี
- จำนวนแถวใน `customer_summary` กับ `monthly_summary` ต้องรวมกันได้เท่ากับจำนวนแถวในตารางรวม

## ผลลัพธ์ที่คาดหวัง

เมื่อรันไฟล์โจทย์จะได้ผลแบบนี้

```txt
customers 12 แถว
orders 40 แถว
products 8 แถว
master 40 แถว
customer_summary 13 แถว
monthly_summary 11 แถว
```

และมีไฟล์สามไฟล์ในโฟลเดอร์ `data/processed/final/`

```txt
customer_summary.csv
master.csv
monthly_summary.csv
```

ตัวเลขทั้งหกต้องตรง ถ้า `customer_summary` ได้ 12 แปลว่าต่อตารางแล้วตัดลูกค้าที่ไม่มีข้อมูลทิ้ง ซึ่งผิดโจทย์

## เสร็จแล้วพิมพ์

```txt
ตรวจ Ch21
```
