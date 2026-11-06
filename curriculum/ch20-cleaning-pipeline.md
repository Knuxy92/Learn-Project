# บทที่ 20: ประกอบเป็นไปป์ไลน์ทำความสะอาด

## ทบทวน

บทที่แล้วเราตรวจคุณภาพข้อมูลได้แล้ว คือดูค่าว่าง ดูแถวซ้ำ และดูแถวที่อ้างรหัสซึ่งไม่มีอยู่จริง

บทที่ 16 ถึง 17 สอนกฎทำความสะอาดทีละข้อ ทั้งตัดช่องว่าง ปรับตัวพิมพ์ แปลงราคา และแปลงวันที่

บทที่ 18 สอนต่อตารางด้วย `merge`

บทนี้เอาทุกอย่างมาร้อยเป็นลำดับเดียวที่รันซ้ำได้ เรียกว่าไปป์ไลน์ (pipeline)

## ไปป์ไลน์คืออะไร

ไปป์ไลน์คือลำดับขั้นที่กำหนดตายตัว เริ่มจากข้อมูลดิบ แล้วจบที่ข้อมูลพร้อมใช้

ทำไมต้องมี เพราะงานทำความสะอาดที่ทำมือทีละขั้นจะลืมขั้นใดขั้นหนึ่งเสมอ และผลลัพธ์จะเปลี่ยนทุกครั้งที่รันใหม่

ไปป์ไลน์ที่ดีมีสมบัติสามข้อ

1. รันซ้ำได้ ผลออกมาเหมือนเดิมทุกครั้ง
2. แยกขั้นชัดเจน รู้ว่าขั้นไหนทำอะไร
3. คืนค่าออกมา ไม่พิมพ์ผลข้างใน

เริ่มจากดูขนาดตารางดิบทั้งสามตารางก่อน

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)
orders = pd.read_csv("data/raw/orders.csv", dtype=str)
products = pd.read_csv("data/raw/products.csv", dtype=str)

print(f"customers {customers.shape}")
print(f"orders    {orders.shape}")
print(f"products  {products.shape}")
```

ผลลัพธ์

```txt
customers (14, 7)
orders    (42, 7)
products  (8, 4)
```

บรรทัดนี้บอกอะไรเราหลายอย่าง ลูกค้ามี 14 แถว แต่รหัสไม่ซ้ำแค่ 12 ตัว แปลว่ามีแถวซ้ำปนอยู่

## ขั้นที่หนึ่ง อ่านทุกตารางเป็นข้อความก่อน

จุดที่พลาดบ่อยที่สุดคือปล่อยให้ Pandas เดาชนิดข้อมูลเอง

ถ้าปล่อยให้เดา คอลัมน์ `quantity` ที่มีค่าว่างจะกลายเป็นทศนิยม จำนวนเต็มกลายเป็น `1.0`, `5.0` ซึ่งผิดความหมายของจำนวนชิ้น

ส่วนคอลัมน์รหัสอย่าง `order_id` ที่มีตัวอักษรนำยังปลอดภัย แต่รหัสที่หน้าตาเป็นตัวเลขล้วนจะกลายเป็นจำนวนเต็มและเสียศูนย์นำหน้าไป

เราจึงอ่านทุกคอลัมน์เป็นข้อความด้วย `dtype=str` แล้วค่อยแปลงชนิดเองทีหลัง

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)

print(orders["quantity"].dtype)
print(orders["quantity"].head(4).tolist())
```

ผลลัพธ์

```txt
str
['2', '5', '-1', '3']
```

ค่าที่ไม่ว่างจะถูกอ่านเป็นข้อความ ส่วนช่องว่างที่ Pandas มองเป็น missing value ยังคงเป็นค่าว่างตามค่าเริ่มต้นของ read_csv เราจึงคุมการแปลงชนิดในขั้นถัดไปได้เอง

## ขั้นที่สอง ตัดแถวซ้ำด้วยกุญแจ

แถวซ้ำคือแถวที่ค่าของกุญแจ (key) ซ้ำกับแถวอื่น

กุญแจของลูกค้าคือ `customer_id` กุญแจของออเดอร์คือ `order_id`

ทำไมต้องตัด เพราะถ้าไม่ตัด ยอดรวมจะเกินจริง และการต่อตารางจะทำให้แถวบานออกเป็นทวีคูณ

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)
before = len(orders)
orders = orders.drop_duplicates(subset=["order_id"], keep="last")

print(f"ก่อน {before} แถว หลัง {len(orders)} แถว")
print(orders.loc[orders["order_id"] == "O0006", ["order_id", "customer_id", "quantity"]].to_string(index=False))
```

ผลลัพธ์

```txt
ก่อน 42 แถว หลัง 40 แถว
order_id customer_id quantity
   O0006        C006        1
```

ออเดอร์ O0006 มีสามแถว สองแถวแรกเป็นสำเนากัน ส่วนแถวสุดท้ายเป็นข้อมูลจริงที่ต่างออกไป

`keep="last"` จึงเก็บแถวสุดท้ายไว้ ซึ่งเป็นแถวที่ข้อมูลครบกว่าในชุดนี้

ทางเลือกคือ `keep="first"` และ `keep=False` ที่ทิ้งทุกแถวที่ซ้ำ เราเลือก `keep="last"` ให้ตรงกันทั้งหลักสูตร

ดูแถวที่รหัสลูกค้าซ้ำบ้าง

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)
same_id = customers.loc[customers["customer_id"] == "C003", ["name", "email", "signup_date"]]

print(same_id.to_string(index=False))
```

ผลลัพธ์

```txt
            name                 email signup_date
        Kanya P. customer3@example.com  2024/08/20
        Kanya P. customer3@example.com  2024/08/20
Malee Wongsakul      malee@example.com  2024-03-15
```

สองแถวแรกเหมือนกันทุกตัวอักษร แถวสุดท้ายเป็นคนละคนแต่ใช้รหัสเดียวกัน

นี่คือปัญหาจริงที่ต้องตัดสินใจ แถวสุดท้ายดูเหมือนข้อมูลที่แก้ไขล่าสุด เราจึงเก็บไว้ แต่ต้องบันทึกไว้ว่าเป็นการตัดสินใจ ไม่ใช่ความจริงที่พิสูจน์ได้

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)
print(f"C003 ก่อนตัดซ้ำ {customers['customer_id'].eq('C003').sum()} แถว")

customers = customers.drop_duplicates(subset=["customer_id"], keep="last")
print(f"C003 หลังตัดซ้ำ {customers['customer_id'].eq('C003').sum()} แถว")
print(f"ลูกค้าทั้งหมด {len(customers)} แถว")
```

ผลลัพธ์

```txt
C003 ก่อนตัดซ้ำ 3 แถว
C003 หลังตัดซ้ำ 1 แถว
ลูกค้าทั้งหมด 12 แถว
```

## ขั้นที่สาม ทำความสะอาดชื่อและอีเมล

ชื่อมีช่องว่างหัวท้ายและช่องว่างซ้อนกลางคำ

อีเมลมีตัวพิมพ์ใหญ่ปน และมีช่องที่ว่างเปล่า

ทำไมต้องทำ เพราะการเทียบชื่อหรืออีเมลจะพลาดทันทีถ้าตัวพิมพ์ไม่ตรงกัน

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)

name = customers["name"].astype("string").str.strip()
cleaned = name.str.replace(r"\s+", " ", regex=True).str.title()

print(repr(customers["name"].iloc[0]))
print(repr(cleaned.iloc[0]))
```

ผลลัพธ์

```txt
'  Nattapong Sri  '
'Nattapong Sri'
```

ลำดับสำคัญมาก คือตัดหัวท้ายก่อน แล้วค่อยยุบช่องว่างที่อยู่ติดกันให้เหลือช่องเดียว แล้วค่อยปรับตัวพิมพ์

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)

email = customers["email"].astype("string").str.strip().str.lower()

print(customers["email"].head(4).tolist())
print(email.head(4).tolist())
```

ผลลัพธ์

```txt
['customer1@example.com', 'customer2@example.com', 'customer3@example.com', 'CUSTOMER4@EXAMPLE.COM']
['customer1@example.com', 'customer2@example.com', 'customer3@example.com', 'customer4@example.com']
```

ช่องที่ว่างเปล่าอ่านเข้ามาเป็นค่าว่างอยู่แล้ว ไม่ต้องเติมอะไรเพิ่ม

## ขั้นที่สี่ แปลงรหัสโทรศัพท์

เบอร์โทรในชุดนี้มีสี่รูปแบบปนกัน คือ `+66801002003`, `(66) 802003004`, `080-300-4005` และ `0804005006`

รูปแบบที่ต้องการมีแบบเดียว คือเลขสิบหลักที่ขึ้นต้นด้วยศูนย์

ทำไมต้องบังคับ เพราะเบอร์เดียวกันที่เขียนต่างกันจะถูกนับเป็นคนละคนเวลาจับคู่

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)

phone = customers["phone"].astype("string").str.replace(r"[()+\-\s]", "", regex=True)
print(phone.head(4).tolist())

phone = phone.str.replace(r"^66", "0", regex=True)
print(phone.head(4).tolist())
```

ผลลัพธ์

```txt
['66801002003', '66802003004', '0803004005', '0804005006']
['0801002003', '0802003004', '0803004005', '0804005006']
```

ขั้นแรกเก็บเฉพาะตัวเลข แล้วขั้นที่สองเปลี่ยนรหัสประเทศ 66 ที่อยู่ต้นให้เป็นศูนย์

จากนั้นตรวจว่าที่เหลือมีสิบหลักและขึ้นต้นด้วยศูนย์จริง ถ้าไม่ผ่านให้เป็นค่าว่างแทนที่จะเก็บค่าเสียไว้

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)

phone = customers["phone"].astype("string").str.replace(r"[()+\-\s]", "", regex=True)
phone = phone.str.replace(r"^66", "0", regex=True)
valid = phone.str.fullmatch(r"0\d{9}")

print(f"ผ่าน {valid.sum()} แถว จาก {phone.notna().sum()} แถว")
print(f"กลายเป็นค่าว่าง {phone.where(valid, pd.NA).isna().sum()} แถว")
```

ผลลัพธ์

```txt
ผ่าน 13 แถว จาก 13 แถว
กลายเป็นค่าว่าง 1 แถว
```

แถวที่กลายเป็นค่าว่างคือแถวที่ไม่มีเบอร์ตั้งแต่ต้น ซึ่งถูกต้องแล้ว

## ขั้นที่ห้า รวมหมวดหมู่ให้เหลือค่าเดียว

ค่าที่เขียนต่างกันแต่หมายถึงสิ่งเดียวกันทำให้การนับผิด

ประเทศมี `Thailand`, `TH`, `thailand `, ` Thailand`, `LA` และ `Laos`

ทำไมต้องรวม เพราะการนับลูกค้าตามประเทศจะได้คำตอบผิดถ้าแยกเป็นหกกลุ่ม

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)

country = customers["country"].astype("string").str.strip().str.title()
print(country.value_counts().to_string())

mapping = {"Th": "Thailand", "Thailand": "Thailand", "La": "Laos", "Laos": "Laos"}
canonical = country.map(mapping).fillna(country)
print()
print(canonical.value_counts().to_string())
```

ผลลัพธ์

```txt
country
Thailand    8
La          4
Laos        1
Th          1

country
Thailand    9
Laos        5
```

`title` ก่อนแล้วค่อย `map` เป็นลำดับที่สั้นที่สุด เพราะทำให้ตัวพิมพ์ตรงกับกุญแจในดิกชันนารี

`fillna(country)` กันค่าแปลกที่ไม่อยู่ในแผนที่ไว้ ไม่ให้หายไปเงียบ ๆ

สถานะมีปัญหาเดียวกัน คือ `canceled` กับ `cancelled` คือคำเดียวกัน และช่องว่างต้องกลายเป็น `unknown`

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)

status = orders["status"].astype("string").str.strip().str.lower()
print(status.value_counts(dropna=False).to_string())

filled = status.replace("", pd.NA).fillna("unknown")
print()
print(filled.replace({"canceled": "cancelled"}).value_counts().to_string())
```

ผลลัพธ์

```txt
status
paid         11
pending       8
cancelled     7
canceled      6
<NA>          5
unknown       5

status
cancelled    13
paid         11
unknown      10
pending       8
```

ข้อควรระวังคือ `replace("", pd.NA)` ต้องมาก่อน `fillna` ไม่อย่างนั้นช่องว่างจะถูกนับเป็นค่าปกติ

ระดับสมาชิกใช้กฎเดียวกัน แต่ค่าเริ่มต้นคือ `Unknown`

```python
import pandas as pd

customers = pd.read_csv("data/raw/customers.csv", dtype=str)

tier = customers["loyalty_tier"].astype("string").str.strip().str.title()
print(tier.replace("", pd.NA).fillna("Unknown").value_counts().to_string())
```

ผลลัพธ์

```txt
loyalty_tier
Silver    8
Gold      5
Unknown   1
```

## ขั้นที่หก แปลงราคา จำนวน และวันที่

ราคามีทั้ง `450`, `฿1,150`, `1,150` และ `300.00`

ทำไมต้องแปลง เพราะคูณข้อความด้วยข้อความไม่ได้

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)

print(orders["unit_price"].head(6).tolist())

price = (
    orders["unit_price"]
    .astype("string")
    .str.replace("฿", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(r"\s+", "", regex=True)
)
print(price.head(6).tolist())
print(pd.to_numeric(price, errors="coerce").head(6).tolist())
```

ผลลัพธ์

```txt
['4200.00', '฿1,150', '450', '300.00', '300', '1150.00']
['4200.00', '1150', '450', '300.00', '300', '1150.00']
[4200.0, 1150.0, 450.0, 300.0, 300.0, 1150.0]
```

ใช้ `errors="coerce"` ให้ค่าที่แปลงไม่ได้กลายเป็นค่าว่าง แทนที่จะทำให้ทั้งไปป์ไลน์พัง

จำนวนใช้ `Int64` ซึ่งเป็นจำนวนเต็มที่เก็บค่าว่างได้

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)

quantity = pd.to_numeric(orders["quantity"], errors="coerce").astype("Int64")

print(quantity.dtype)
print(f"ค่าว่าง {quantity.isna().sum()} แถว")
```

ผลลัพธ์

```txt
Int64
ค่าว่าง 2 แถว
```

อย่าใช้ `int` ธรรมดา เพราะมันแทนค่าว่างไม่ได้และจะพังทันทีที่เจอช่องว่าง

วันที่มีสามรูปแบบ คือ `2025/02/23`, `19/03/2025` และ `2025-06-11`

ถ้าส่งทั้งหมดเข้า `dayfirst=True` พร้อมกัน วันที่ขึ้นต้นด้วยปีจะถูกอ่านผิดเป็นวันที่ 6 พฤศจิกายน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)

wrong = pd.to_datetime(orders["order_date"], format="mixed", dayfirst=True, errors="coerce")

print(wrong.head(4).dt.strftime("%Y-%m-%d").tolist())
```

ผลลัพธ์

```txt
['2025-02-23', '2025-03-19', '2025-11-06', '2025-02-26']
```

`O0003` มีวันที่จริงคือ `2025-06-11` แต่กลายเป็น `2025-11-06`

ทางแก้คือแยกสองกลุ่มก่อน แบบที่บทที่แล้วสอนไว้

```python
import pandas as pd

ISO_DATE_PATTERN = r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$"

orders = pd.read_csv("data/raw/orders.csv", dtype=str)


def parse_mixed_dates(series: pd.Series) -> pd.Series:
    text = series.astype("string").str.strip()
    iso_like = text.str.match(ISO_DATE_PATTERN)

    iso = pd.to_datetime(text.where(iso_like), format="mixed", dayfirst=False, errors="coerce")
    day_first = pd.to_datetime(
        text.where(~iso_like), format="mixed", dayfirst=True, errors="coerce"
    )

    return iso.fillna(day_first)


dates = parse_mixed_dates(orders["order_date"])

print(dates.head(4).dt.strftime("%Y-%m-%d").tolist())
print(f"แปลงไม่ได้ {dates.isna().sum()} แถว")
print(dates.dtype)
```

ผลลัพธ์

```txt
['2025-02-23', '2025-03-19', '2025-06-11', '2025-02-26']
แปลงไม่ได้ 0 แถว
datetime64[us]
```

## ขั้นที่เจ็ด ต่อตารางและคำนวณรายได้

เมื่อทั้งสามตารางสะอาดแล้ว ก็ต่อกันด้วย `merge` แบบคงออเดอร์ทุกแถว

ทำไมต้องคงออเดอร์ไว้ เพราะออเดอร์คือหน่วยที่เราต้องการรายงาน ถ้าตัดทิ้งเพราะหาลูกค้าไม่เจอ ตัวเลขรายได้จะหายไปด้วย

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", dtype=str)
customers = pd.read_csv("data/raw/customers.csv", dtype=str)

orders = orders.drop_duplicates(subset=["order_id"], keep="last")
customers = customers.drop_duplicates(subset=["customer_id"], keep="last")

master = orders.merge(customers, on="customer_id", how="left")

print(master.shape)
print(f"แถวที่ไม่มีชื่อลูกค้า {master['name'].isna().sum()} แถว")
print(master.loc[master["name"].isna(), "customer_id"].unique().tolist())
```

ผลลัพธ์

```txt
(40, 13)
5
['C013', 'C014']
```

ห้าแถวนี้คือออเดอร์ที่อ้างรหัสลูกค้าซึ่งไม่มีในตารางลูกค้า

เราไม่ลบทิ้ง แต่ปล่อยให้ชื่อเป็นค่าว่าง แล้วบันทึกเป็นข้อจำกัดของข้อมูล

จากนั้นต่อสินค้าและคำนวณรายได้

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
print(f"ยอดรวม {master['revenue'].sum():,.0f} บาท")
print(master[["order_id", "customer_id", "product_name", "revenue"]].head(3).to_string(index=False))
```

ผลลัพธ์

```txt
ตารางรวม 40 แถว
ยอดรวม 72,245 บาท
order_id customer_id product_name  revenue
   O0001        C002     Monitor    8400.0
   O0002        C006    Desk Lamp   5750.0
   O0003        C003      Keyboard    -450.0
```

ยอดรวมนี้ยังมีค่าติดลบปนอยู่ เพราะออเดอร์ที่จำนวนเป็นลบยังไม่ถูกตัดออก

การตัดหรือไม่ตัดเป็นเรื่องของการตัดสินใจทางธุรกิจ ไม่ใช่เรื่องของโค้ด บทนี้จึงคงไว้และบันทึกไว้ในรายงาน

## รวมทุกขั้นเป็นฟังก์ชันเดียว

ตอนนี้เรามีขั้นครบแล้ว หน้าที่ของไปป์ไลน์คือเรียกขั้นเหล่านี้ตามลำดับในฟังก์ชันเดียว

ฟังก์ชันย่อยหนึ่งตัวต่อหนึ่งขั้น รับ DataFrame คืน DataFrame ไม่พิมพ์อะไรข้างใน

```python
from pathlib import Path

import pandas as pd


def load_table(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, encoding="utf-8")


def dedupe(df: pd.DataFrame, key: str) -> pd.DataFrame:
    return df.drop_duplicates(subset=[key], keep="last").reset_index(drop=True)


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    quantity = pd.to_numeric(result["quantity"], errors="coerce")
    price = pd.to_numeric(
        result["unit_price"].str.replace("฿", "", regex=False).str.replace(",", "", regex=False),
        errors="coerce",
    )
    result["revenue"] = quantity * price
    return result


def main() -> None:
    customers = dedupe(load_table("data/raw/customers.csv"), "customer_id")
    orders = dedupe(load_table("data/raw/orders.csv"), "order_id")

    master = orders.merge(customers, on="customer_id", how="left")
    master = add_revenue(master)

    print(f"ลูกค้า {len(customers)} แถว")
    print(f"ออเดอร์ {len(orders)} แถว")
    print(f"ตารางรวม {len(master)} แถว")
    print(f"คอลัมน์ใหม่ {master.columns[-1]}")


if __name__ == "__main__":
    main()
```

ผลลัพธ์

```txt
ลูกค้า 12 แถว
ออเดอร์ 40 แถว
ตารางรวม 40 แถว
คอลัมน์ใหม่ revenue
```

สังเกตว่า `main` ไม่รู้รายละเอียดว่าตัดช่องว่างอย่างไรหรือแปลงราคาอย่างไร มันรู้แค่ว่าต้องเรียกอะไรก่อนหลัง

นี่คือประโยชน์ของการแยกขั้น เราเปลี่ยนกฎข้อใดข้อหนึ่งได้โดยไม่ต้องแตะขั้นอื่น

## เขียนผลลัพธ์ลงดิสก์

ขั้นสุดท้ายคือเขียนผลลัพธ์ออกเป็นไฟล์ CSV

ทำไมต้องเขียน เพราะไปป์ไลน์ที่ดีย้ายข้อมูลจากที่หนึ่งไปอีกที่หนึ่งได้ ไม่ได้หยุดอยู่ที่การคำนวณในหน่วยความจำ

```python
from pathlib import Path

import pandas as pd

out_dir = Path("data/processed")
out_dir.mkdir(parents=True, exist_ok=True)

frame = pd.DataFrame({"order_id": ["O1", "O2"], "revenue": [100.0, 250.0]})
frame.to_csv(out_dir / "demo.csv", index=False, encoding="utf-8")

print((out_dir / "demo.csv").exists())
print(pd.read_csv(out_dir / "demo.csv").shape)
```

ผลลัพธ์

```txt
True
(2, 2)
```

`mkdir(parents=True, exist_ok=True)` ทำให้สร้างโฟลเดอร์ซ้อนได้ และไม่พังถ้ามีอยู่แล้ว

`index=False` จำเป็น เพราะดัชนีของ Pandas ไม่ใช่ข้อมูลจริง ถ้าเขียนออกไปจะได้คอลัมน์แปลกปลอมเพิ่มมา

## ไฟล์ตัวอย่างที่รันได้

ในโฟลเดอร์ `curriculum/ch20/` มีสองไฟล์

`pipeline-example.py` แสดงลำดับขั้นแบบสั้นที่สุด

```txt
ลูกค้าก่อนตัดซ้ำ 14 แถว
ลูกค้าหลังตัดซ้ำ 12 แถว
ออเดอร์ก่อนตัดซ้ำ 42 แถว
ออเดอร์หลังตัดซ้ำ 40 แถว
ตารางรวม 40 แถว
order_id customer_id             name  revenue
   O0001        C002  Malee Wongsakul   8400.0
   O0002        C006      Prasit Kaew   5750.0
   O0003        C003 Malee Wongsakul    -450.0
   O0004        C002  Malee Wongsakul    900.0
```

`config-example.py` แยกกฎทำความสะอาดออกเป็นฟังก์ชันย่อย และแสดงการนับก่อนกับหลัง

```txt
ประเทศก่อนและหลัง
country
Thailand     4
LA           4
thailand     4
Laos         1
TH           1

country
Thailand    9
Laos        5

สถานะก่อนและหลัง
status
pending      8
cancelled    7
canceled     6
Paid         6
NaN          5
unknown      5
paid         4
PAID         1

status
cancelled    13
paid         11
unknown      10
pending       8

ระดับสมาชิกก่อนและหลัง
loyalty_tier
silver     4
silver     4
Gold       3
GOLD       1
gold       1
NaN        1

loyalty_tier
Silver     8
Gold       5
Unknown    1

ราคาต่อหน่วยที่แปลงได้และแปลงไม่ได้
แปลงได้ 39 แถว แปลงไม่ได้ 3 แถว
```

บรรทัด `silver 4` ที่ซ้ำกันสองครั้งคือ `silver` กับ `silver ` ที่มีช่องว่างต่อท้าย ตาเปล่ามองไม่เห็น แต่โปรแกรมเห็นเป็นคนละค่า

## สรุป

| ขั้น | สิ่งที่ทำ | กฎที่ใช้ |
|---|---|---|
| อ่าน | อ่านทุกตารางเป็นข้อความ | `dtype=str` |
| ตัดซ้ำ | เก็บแถวสุดท้ายของแต่ละกุญแจ | `drop_duplicates(keep="last")` |
| ชื่อ | ตัดหัวท้าย ยุบช่องว่าง ปรับตัวพิมพ์ | `strip` แล้ว `replace` แล้ว `title` |
| อีเมล | ตัดหัวท้าย ปรับเป็นตัวพิมพ์เล็ก | `strip` แล้ว `lower` |
| โทรศัพท์ | เก็บตัวเลข เปลี่ยน 66 เป็น 0 ตรวจสิบหลัก | `fullmatch(r"0\d{9}")` |
| ประเทศ | ปรับตัวพิมพ์แล้วแมป | `Thailand`, `Laos` |
| สถานะ | ปรับตัวพิมพ์ แมป canceled เติม unknown | `cancelled` |
| ระดับ | ปรับตัวพิมพ์ เติม Unknown | `Gold`, `Silver`, `Unknown` |
| ราคา | ตัดสัญลักษณ์บาทกับ comma แล้วแปลง | `to_numeric(errors="coerce")` |
| จำนวน | แปลงเป็นจำนวนเต็มที่ว่างได้ | `astype("Int64")` |
| วันที่ | แยกกลุ่มปีขึ้นก่อนแล้วค่อยแปลง | `parse_mixed_dates` |
| ต่อตาราง | คงออเดอร์ทุกแถว | `merge(how="left")` |
| รายได้ | จำนวนคูณราคา | `quantity * unit_price` |

หลักจำง่าย ๆ

- อ่านเป็นข้อความก่อน แล้วแปลงชนิดเองทีหลัง
- ตัดแถวซ้ำก่อนทำอย่างอื่น เพราะทุกขั้นหลังจากนั้นจะนับแถวผิดถ้ายังมีแถวซ้ำ
- ฟังก์ชันย่อยรับตารางคืนตาราง ไม่พิมพ์อะไรข้างใน
- ทุกการตัดสินใจที่เปลี่ยนจำนวนแถวต้องเขียนบันทึกไว้

## โจทย์ที่ต้องทำ

เปิด `exercises/ch20-clean-pipeline.py` แล้วเขียนห้าฟังก์ชันนี้

1. `clean_customers` รับตารางลูกค้าดิบ คืนตารางที่ตัดรหัสซ้ำด้วย `keep="last"` และทำความสะอาดชื่อ อีเมล โทรศัพท์ ประเทศ ระดับ และวันที่
2. `clean_orders` รับตารางออเดอร์ดิบ คืนตารางที่ตัดรหัสซ้ำ แปลงจำนวนเป็น `Int64` แปลงราคา แปลงวันที่ ปรับสถานะ และทิ้งแถวที่ไม่มีรหัสลูกค้าหรือรหัสสินค้า
3. `clean_products` รับตารางสินค้าดิบ คืนตารางที่ชื่อสินค้าและหมวดเป็นตัวพิมพ์สม่ำเสมอ
4. `build_master` รับสามตารางที่สะอาดแล้ว คืนตารางรวมที่มีคอลัมน์ `revenue`
5. `run_pipeline` รับโฟลเดอร์ข้อมูลดิบกับโฟลเดอร์ปลายทาง เขียน `master.csv` กับ `customers_clean.csv` แล้วคืนจำนวนแถวของทั้งสี่ตาราง

กติกาเพิ่มเติม

- ห้ามแก้ตารางต้นฉบับ ให้เรียก `df.copy()` ก่อนทุกครั้ง
- ฟังก์ชันคืนค่า ไม่พิมพ์ผลข้างใน
- ใช้รายชื่อคอลัมน์ใน `MASTER_COLUMNS` ตามลำดับที่ให้มา

## ผลลัพธ์ที่คาดหวัง

เมื่อรันไฟล์โจทย์จะได้ผลแบบนี้

```txt
customers 12 แถว
orders 40 แถว
products 8 แถว
master 40 แถว
```

ตัวเลขต้องตรงกับข้อมูลจริงใน `data/raw/` ถ้าได้ 41 แปลว่าตัดแถวซ้ำไม่ครบ ถ้าได้ 39 แปลว่าตัดเกิน

## เสร็จแล้วพิมพ์

```txt
ตรวจ Ch20
```
