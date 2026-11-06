# บทที่ 18: รวมตาราง

## ทบทวน

บทที่ 17 สอนแปลงข้อความให้เป็นตัวเลขและวันที่ ทำให้แต่ละตารางมีชนิดข้อมูลที่ถูกต้องแล้ว

แต่ข้อมูลยังกระจายอยู่คนละตาราง ตาราง `orders` มี `customer_id` แต่ไม่มีชื่อลูกค้า ตาราง `customers` มีชื่อแต่ไม่รู้ว่าซื้ออะไร ตาราง `products` มีราคาแต่ไม่รู้ว่าใครซื้อ

การรวมตาราง (merge) คือการต่อข้อมูลจากหลายตารางเข้าด้วยกัน โดยอาศัยค่าที่ตรงกันในคอลัมน์หนึ่ง

## กุญแจเชื่อม

กุญแจเชื่อม (join key) คือคอลัมน์ที่ใช้จับคู่แถวระหว่างสองตาราง

ในชุดข้อมูลนี้มีสองกุญแจ

| กุญแจ | ตารางซ้าย | ตารางขวา |
|---|---|---|
| `customer_id` | `orders` | `customers` |
| `product_id` | `orders` | `products` |

กุญแจเชื่อมต้องมีค่าเหมือนกันจริง ๆ ทั้งชนิดข้อมูลและรูปแบบ ถ้าฝั่งหนึ่งเป็น `"C001 "` มีช่องว่างท้าย แต่อีกฝั่งเป็น `"C001"` การจับคู่จะล้มเหลวเงียบ ๆ

```python
import pandas as pd

orders = pd.DataFrame({"customer_id": ["C001 ", "C002"]})
customers = pd.DataFrame({"customer_id": ["C001", "C002"], "name": ["Anan", "Malee"]})

joined = orders.merge(customers, on="customer_id", how="left")

print(joined.to_string(index=False))
```

ผลลัพธ์

```txt
customer_id  name
      C001    NaN
       C002 Malee
```

แถวแรกหาไม่เจอทั้งที่ตาคนอ่านแล้วเหมือนกัน นี่คือเหตุผลที่บทที่ 16 สอนให้ตัดช่องว่างก่อนรวมตาราง

## การเชื่อมแบบคงแถวซ้าย

`DataFrame.merge` คือเมธอดที่ต่อสองตารางตามกุญแจที่กำหนด

พารามิเตอร์ที่ใช้บ่อยมีสามตัว

- `on` คือชื่อคอลัมน์ที่ใช้จับคู่
- `how` คือชนิดของการเชื่อม
- `suffixes` คือส่วนต่อท้ายชื่อคอลัมน์เมื่อสองตารางมีชื่อคอลัมน์ซ้ำกัน

ตัวอย่างแรกเชื่อมตาราง `orders` กับ `customers` แบบคงแถวซ้าย (left join)

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

joined = orders.merge(customers, on="customer_id", how="left")

print(joined.shape)
print(list(joined.columns))
```

ผลลัพธ์

```txt
(56, 13)
['order_id', 'customer_id', 'product_id', 'quantity', 'unit_price', 'order_date', 'status', 'name', 'email', 'phone', 'country', 'signup_date', 'loyalty_tier']
```

ได้ 13 คอลัมน์เพราะคอลัมน์ของสองตารางต่อกัน และได้ 56 แถวทั้งที่ `orders` มีแค่ 42 แถว นี่คืออาการที่ต้องอธิบายในหัวข้อถัดไป

## คีย์ซ้ำทำให้แถวบวม

`merge` ไม่ได้สนใจว่ากุญแจฝั่งขวาซ้ำหรือไม่ ถ้าฝั่งขวามี `customer_id` เดียวกันสามแถว ทุกออเดอร์ที่ใช้รหัสนั้นจะกลายเป็นสามแถว

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")

print(len(customers))
print(customers["customer_id"].nunique())

unique_customers = customers.drop_duplicates("customer_id")
joined = orders.merge(unique_customers, on="customer_id", how="left")

print(joined.shape)
```

ผลลัพธ์

```txt
14
12
(42, 13)
```

ตารางลูกค้ามี 14 แถวแต่มีรหัสไม่ซ้ำแค่ 12 รหัส เพราะ `C003` ปรากฏสามครั้ง

หลังตัดแถวซ้ำด้วย `drop_duplicates` แล้ว จำนวนแถวกลับมาเท่ากับจำนวนออเดอร์พอดี

กฎที่ต้องจำคือก่อนเชื่อมตารางฝั่งที่ควรมีหนึ่งแถวต่อหนึ่งรหัส ต้องตรวจความซ้ำก่อนเสมอ

ถ้าไม่ตรวจ ยอดรวมจะพองขึ้นแบบนี้

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8")
products = pd.read_csv("data/raw/products.csv", encoding="utf-8")


def prepare(customers_table: pd.DataFrame) -> pd.DataFrame:
    merged = orders.merge(customers_table, on="customer_id", how="left")
    merged = merged.merge(products, on="product_id", how="left")
    merged["quantity"] = pd.to_numeric(
        merged["quantity"].astype("string").str.strip(), errors="coerce"
    )
    merged["unit_price"] = pd.to_numeric(
        merged["unit_price"]
        .astype("string")
        .str.replace("฿", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip(),
        errors="coerce",
    )
    merged["revenue"] = merged["quantity"] * merged["unit_price"]
    return merged


naive = prepare(customers)
fixed = prepare(customers.drop_duplicates("customer_id"))

print(len(naive), naive["revenue"].sum())
print(len(fixed), fixed["revenue"].sum())
print(naive.loc[naive["customer_id"] == "C003", "revenue"].sum())
print(fixed.loc[fixed["customer_id"] == "C003", "revenue"].sum())
```

ผลลัพธ์

```txt
56 98865.0
42 72245.0
39930.0
13310.0
```

ยอดของ `C003` พองจาก 13310 เป็น 39930 เพราะถูกคูณสามรอบ และยอดรวมทั้งตารางเกินจริงไป 26620

## ชนิดของการเชื่อม

`how` กำหนดว่าจะเก็บแถวไหนไว้บ้าง

| ชนิด | เก็บแถวไหน |
|---|---|
| `inner` | เก็บเฉพาะแถวที่จับคู่ได้ทั้งสองฝั่ง |
| `left` | เก็บทุกแถวของฝั่งซ้าย แถวที่จับคู่ไม่ได้เติมค่าว่าง |
| `right` | เก็บทุกแถวของฝั่งขวา |
| `outer` | เก็บทุกแถวของทั้งสองฝั่ง |

ลองกับข้อมูลจริงโดยตัดรหัสลูกค้าซ้ำก่อน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8").drop_duplicates("customer_id")

for how in ("inner", "left", "right", "outer"):
    result = orders.merge(customers, on="customer_id", how=how)
    print(how, len(result))
```

ผลลัพธ์

```txt
inner 37
left 42
right 38
outer 43
```

อ่านตัวเลขนี้ให้ออก

- `inner` ได้ 37 เพราะออเดอร์ 5 แถวที่อ้างถึง `C013` กับ `C014` ถูกตัดทิ้ง
- `left` ได้ 42 เท่ากับจำนวนออเดอร์ทั้งหมด จึงเป็นชนิดที่เหมาะกับงานทำความสะอาด เพราะไม่ทำข้อมูลหาย
- `right` ได้ 38 เพราะเก็บลูกค้าทุกรายไว้ รวม `C010` ที่ยังไม่เคยสั่งซื้อ และทิ้งออเดอร์ 5 แถวที่หาลูกค้าไม่เจอ
- `outer` ได้ 43 เพราะเก็บทั้งออเดอร์ที่ไม่มีลูกค้าและลูกค้าที่ไม่มีออเดอร์

## หาแถวที่จับคู่ไม่สำเร็จ

พารามิเตอร์ `indicator` จะเพิ่มคอลัมน์ `_merge` บอกว่าแต่ละแถวมาจากฝั่งไหน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
customers = pd.read_csv("data/raw/customers.csv", encoding="utf-8").drop_duplicates("customer_id")

checked = orders.merge(
    customers[["customer_id"]],
    on="customer_id",
    how="left",
    indicator=True,
)

print(checked["_merge"].value_counts().to_string())
print(sorted(checked.loc[checked["_merge"] == "left_only", "customer_id"].unique()))
```

ผลลัพธ์

```txt
_merge
both          37
left_only      5
right_only     0
['C013', 'C014']
```

มีออเดอร์ 5 แถวที่อ้างถึง `C013` และ `C014` ซึ่งไม่มีอยู่ในตารางลูกค้าเลย

ข้อมูลแบบนี้เรียกว่าปัญหาความเชื่อมโยง (referential integrity) และบทที่ 19 จะจัดการอย่างเป็นระบบ

## ตั้งชื่อคอลัมน์ที่ชนกัน

ถ้าสองตารางมีชื่อคอลัมน์เหมือนกัน pandas จะเติม `_x` กับ `_y` ให้ ซึ่งอ่านยาก

```python
import pandas as pd

orders = pd.DataFrame({"order_id": ["O1"], "customer_id": ["C1"], "country": ["TH"]})
customers = pd.DataFrame({"customer_id": ["C1"], "country": ["Thailand"]})

print(list(orders.merge(customers, on="customer_id", how="left").columns))
print(list(orders.merge(customers, on="customer_id", how="left", suffixes=("", "_customer")).columns))
```

ผลลัพธ์

```txt
['order_id', 'customer_id', 'country_x', 'country_y']
['order_id', 'customer_id', 'country', 'country_customer']
```

`suffixes=("", "_customer")` ทำให้คอลัมน์ฝั่งซ้ายคงชื่อเดิม และคอลัมน์ฝั่งขวาเติมคำบอกที่มา

## ต่อตารางสินค้าแล้วคำนวณรายได้

งานจริงมักต้องต่อหลายตารางติดกัน ตัวอย่างนี้ต่อ `orders` กับ `products` แล้วคำนวณยอดเงิน

```python
import pandas as pd

orders = pd.read_csv("data/raw/orders.csv", encoding="utf-8")
products = pd.read_csv("data/raw/products.csv", encoding="utf-8")


def to_number(series: pd.Series) -> pd.Series:
    cleaned = (
        series.astype("string")
        .str.replace("฿", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


merged = orders.merge(products, on="product_id", how="left")
merged["quantity"] = to_number(merged["quantity"])
merged["unit_price"] = to_number(merged["unit_price"])
merged["revenue"] = merged["quantity"] * merged["unit_price"]

print(merged.shape)
print(
    merged[["order_id", "product_name", "quantity", "unit_price", "revenue"]]
    .head(5)
    .to_string(index=False)
)
```

ผลลัพธ์

```txt
(42, 11)
order_id product_name  quantity  unit_price  revenue
   O0001     Monitor        2.0      4200.0   8400.0
   O0002    Desk Lamp       5.0      1150.0   5750.0
   O0003    Keyboard       -1.0       450.0   -450.0
   O0004        Mouse       3.0       300.0    900.0
   O0005        Mouse       0.0       300.0      0.0
```

จำนวนแถวยังเป็น 42 เพราะสินค้าทุกตัวที่อ้างถึงมีอยู่จริง

สังเกตว่า `O0003` ได้รายได้ติดลบ เพราะจำนวนชิ้นเป็น `-1` การรวมตารางทำให้เห็นปัญหานี้ชัดขึ้น ซึ่งเป็นเรื่องของบทถัดไป

## สรุปยอดต่อลูกค้า

เมื่อได้ตารางหลัก (master table) แล้ว การสรุปยอดใช้ `groupby`

```python
import pandas as pd

master = pd.DataFrame(
    {
        "customer_id": ["C1", "C1", "C2", "C2", "C3"],
        "revenue": [100.0, 250.0, 400.0, 50.0, 900.0],
    }
)

summary = (
    master.groupby("customer_id", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
    .reset_index(drop=True)
)

print(summary.to_string(index=False))
```

ผลลัพธ์

```txt
customer_id  revenue
         C3    900.0
         C2    450.0
         C1    350.0
```

`as_index=False` ทำให้ `customer_id` กลับมาเป็นคอลัมน์ธรรมดา ไม่ใช่ดัชนี

`reset_index(drop=True)` ทำให้เลขแถวเริ่มใหม่จากศูนย์หลังเรียงลำดับ

## สรุป

เลือกชนิดการเชื่อมตามคำถามที่ต้องการตอบ

| ต้องการ | ใช้ |
|---|---|
| เฉพาะแถวที่ข้อมูลครบทั้งสองฝั่ง | `inner` |
| เก็บออเดอร์ทุกแถวไว้ตรวจต่อ | `left` |
| หาแถวที่จับคู่ไม่สำเร็จ | `left` กับ `indicator=True` |
| ดูภาพรวมว่าฝั่งไหนขาด | `outer` |

ลำดับที่ปลอดภัยสำหรับงานทำความสะอาดมีสี่ขั้น

1. ตรวจว่ากุญแจฝั่งที่ควรมีค่าเดียวต่อหนึ่งรหัสไม่มีรหัสซ้ำ
2. ตัดช่องว่างและปรับตัวพิมพ์ของกุญแจทั้งสองฝั่ง
3. เชื่อมแบบ `left` เพื่อไม่ให้ข้อมูลหาย
4. ตรวจจำนวนแถวหลังเชื่อมว่ายังเท่าเดิม ถ้าเพิ่มขึ้นแปลว่ากุญแจฝั่งขวายังซ้ำ

## โจทย์ที่ต้องทำ

เปิดไฟล์ `exercises/ch18-join-tables.py` แล้วเติมห้าฟังก์ชันนี้

1. `join_orders_customers` เชื่อม `orders` กับ `customers` ด้วย `customer_id` แบบคงแถวซ้าย และใช้ `suffixes=("", "_customer")`
2. `join_orders_products` เชื่อม `orders` กับ `products` ด้วย `product_id` แบบคงแถวซ้าย
3. `unmatched_orders` คืนเฉพาะแถวที่ `customer_id` ไม่มีในตารางลูกค้า โดยคงคอลัมน์เดิมของ `orders` ทั้งหมด
4. `revenue_by_customer` สรุปยอด `revenue` ต่อ `customer_id` เรียงจากมากไปน้อย และรีเซ็ตดัชนี
5. `to_number` แปลงข้อความที่มี `฿` กับ `,` ให้เป็นจำนวน โดยค่าที่แปลงไม่ได้ให้เป็นค่าว่าง

เงื่อนไขของ `revenue_by_customer` คือถ้าตารางไม่มีคอลัมน์ `revenue` ให้โยน `ValueError`

## ผลลัพธ์ที่คาดหวัง

รันคำสั่งนี้จากโฟลเดอร์โปรเจกต์

```cmd
python exercises/ch18-join-tables.py
```

ต้องได้ผลแบบนี้

```txt
orders 42 แถว customers 14 แถว
join ก่อนตัดรหัสลูกค้าซ้ำได้ 56 แถว
join หลังตัดรหัสลูกค้าซ้ำได้ 42 แถว
ออเดอร์ที่ไม่มีข้อมูลลูกค้า 5 แถว
order_id customer_id
   O0009        C013
   O0014        C014
   O0016        C013
   O0017        C014
   O0035        C013
รวมสินค้าแล้วได้ 42 แถว
ห้าอันดับลูกค้าที่มียอดรวมสูงสุด
customer_id  revenue
       C003  13310.0
       C007  12720.0
       C002   9300.0
       C008   8400.0
       C012   6735.0
```

## เสร็จแล้วพิมพ์

```txt
ตรวจ Ch18
```
